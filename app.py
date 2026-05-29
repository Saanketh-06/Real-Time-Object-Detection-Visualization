import streamlit as st
import cv2
import tempfile
from utils.detector import process_frame

st.set_page_config(
    page_title="Real-Time Object Detection",
    layout="wide"
)

st.title("Real-Time Object Detection and Visualization")

option = st.sidebar.selectbox(
    "Select Source",
    ("Webcam", "Upload Video")
)

frame_placeholder = st.empty()

if option == "Webcam":

    cap = cv2.VideoCapture(0)

    st.info("Webcam started...")

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            st.error("Failed to access webcam")
            break

        processed_frame = process_frame(frame)

        frame_placeholder.image(
            cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB),
            channels="RGB"
        )

    cap.release()

else:

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video:

        temp_video = tempfile.NamedTemporaryFile(delete=False)

        temp_video.write(uploaded_video.read())

        cap = cv2.VideoCapture(temp_video.name)

        st.success("Video uploaded successfully")

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            processed_frame = process_frame(frame)

            frame_placeholder.image(
                cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB),
                channels="RGB"
            )

        cap.release()