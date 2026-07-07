import dlib
import numpy as np
import face_recognition_models
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_five_point_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1)
        encodings.append(np.array(face_descriptor))

    return encodings


@st.cache_resource
def get_trained_model():
    X = []
    Y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get("face_embedding")

        if embedding:
            X.append(np.array(embedding))
            Y.append(student.get("student_id"))

    if len(X) == 0:
        return None

    clf = KNeighborsClassifier(
        n_neighbors=1,
        weights='distance'
    )

    try:
        clf.fit(X, Y)
    except ValueError:
        return None

    return {
        "clf": clf,
        "X": X,
        "Y": Y
    }


def train_classifier():
    st.cache_resource.clear()
    return bool(get_trained_model())


def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    model_data = get_trained_model()

    # Number of faces should come from encodings,
    # not whether a model exists.
    if not model_data:
        return {}, [], len(encodings)

    detected_students = {}

    clf = model_data["clf"]
    X_train = model_data["X"]
    y_train = model_data["Y"]

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:

        # More than one registered student
        if len(all_students) >= 2:

            distances, indices = clf.kneighbors([encoding], n_neighbors=1)
            distance = float(distances[0][0])
            predicted_id = int(y_train[indices[0][0]])

            DISTANCE_THRESHOLD = 0.55

            print(f"Predicted={predicted_id} Distance={distance:.3f}")

            if distance <= DISTANCE_THRESHOLD:
                detected_students[predicted_id] = True
            else:
                print("Unknown face ignored.")

        # Only one registered student
        else:

            predicted_id = int(all_students[0])

            student_embedding = X_train[y_train.index(predicted_id)]

            best_match_score = np.linalg.norm(student_embedding - encoding)

            resemblance_threshold = 0.6

            if best_match_score <= resemblance_threshold:
                detected_students[predicted_id] = True

    return detected_students, all_students, len(encodings)