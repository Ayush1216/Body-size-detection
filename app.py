import streamlit as st
from PIL import Image
import numpy as np

# import matplotlib.pyplot as plt
# from time import time
# # import mediapipe as mp
# # import cv2 as cv
# import math

# # mpPose = mp.solutions.pose


# pose = mpPose.Pose(
#     static_image_mode=True,
#     model_complexity=2,
#     enable_segmentation=True,
#     min_detection_confidence=0.5
# )

# mpDraw = mp.solutions.drawing_utils

# def estimate_body_size(right_ankle, left_ankle, right_hip, left_hip, right_shoulder, left_shoulder, right_elbow, left_elbow, right_knee, left_knee, right_wrist, left_wrist, height_pixels):
#     # Calculate height in inches based on pixel height
#     height_inches = height_pixels / 10 # assuming 10 pixels per inch
    
#     # Calculate waist and hip measurements as averages of left and right sides
#     waist = abs(right_hip[0] - left_hip[0]) / 2
# #     print(waist)
#     hips = (right_hip[1] - left_hip[1]) / 2
    
#     # Calculate bust and chest measurements as averages of left and right sides
#     bust = (right_shoulder[1] - left_shoulder[1]) / 2
#     chest = (right_elbow[1] - left_elbow[1]) / 2
    
#     # Calculate sleeve length as average of left and right sides
#     sleeve_length = ((right_wrist[1] - right_shoulder[1]) + (left_wrist[1] - left_shoulder[1])) / 2
    
#     # Calculate pant length as average of left and right legs
#     pant_length = ((right_ankle[1] - right_hip[1]) + (left_ankle[1] - left_hip[1])) / 2
    
#     # Use measurements to estimate body size label
#     extra = 0
#     h = 0
#     size = "large"
#     if height_inches < 75 + h:
#         return height_inches, waist, "small"
# #         if waist < 27 + extra:
# #             size = "extra small"
#         if waist < 29 + extra:
#             size = "small"
#         elif waist < 31 + extra:
#             size = "medium"
#         elif waist < 33 + extra:
#             size = "large"
# #         else:
# #             size = "extra large"
#     elif height_inches < 150 + h:
#         return height_inches, waist, "medium"
# #         if waist < 29 + extra:
# #             size = "extra small"
#         if waist < 31 + extra:
#             size = "small"
#         elif waist < 33 + extra:
#             size = "medium"
#         elif waist < 35 + extra:
#             size = "large"
# #         else:
# #             size = "extra large"
#     elif height_inches > 150 + h:
#         return height_inches, waist, "large"
# #         if waist < 35 + extra:
# #             size = "extra small"
#         if waist < 37 + extra:
#             size = "small"
#         elif waist < 39 + extra:
#             size = "medium"
#         elif waist < 41 + extra:
#             size = "large"
# #         else:
# #             size = "extra large"

#     return height_inches, waist, size


# def detectImage(image_path):
#     img = cv.imread(image_path)
#     OutputImage = img.copy()
#     imageRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#     results = pose.process(img)
#     imgHeight, imgWidth, _ = img.shape
#     LANDMARKS = {}
    
#     if results.pose_landmarks:
#         mpDraw.draw_landmarks(
#             image=OutputImage,
#             landmark_list=results.pose_landmarks,
#             connections=mpPose.POSE_CONNECTIONS
#         )
# #         print(len(mpPose.PoseLandmark))
#         for i in range(len(mpPose.PoseLandmark)):
#             LANDMARKS[mpPose.PoseLandmark(i).name] = [results.pose_landmarks.landmark[mpPose.PoseLandmark(i).value].x * imgWidth,
#                                                      results.pose_landmarks.landmark[mpPose.PoseLandmark(i).value].y * imgHeight]
    
# #     LANDMARKS = pd.DataFrame(SIZE)
# #     print(LANDMARKS.head())

# #     LANDMARKS = LANDMARKS[['NOSE','LEFT_EYE','RIGHT_EYE', 'LEFT_SHOULDER', 'RIGHT_SHOULDER', 'LEFT_ELBOW', 'RIGHT_ELBOW','LEFT_WRIST', 'RIGHT_WRIST', 'LEFT_HIP', 'RIGHT_HIP', 'LEFT_KNEE', 'RIGHT_KNEE', 'LEFT_ANKLE', 'RIGHT_ANKLE']]
    
#     SIZES = {}
#     eye = [(LANDMARKS['LEFT_EYE'][0]+LANDMARKS['RIGHT_EYE'][0])/2, (LANDMARKS['LEFT_EYE'][1]+LANDMARKS['RIGHT_EYE'][1])/2]
#     ankle = [(LANDMARKS['LEFT_ANKLE'][0]+LANDMARKS['RIGHT_ANKLE'][0])/2, (LANDMARKS['LEFT_ANKLE'][1]+LANDMARKS['RIGHT_ANKLE'][1])/2]
#     SIZES['HEIGHT'] = math.sqrt(((ankle[0]-eye[0])**2)+((ankle[1]-eye[1])**2))
    
#     BODY = []
#     H = []
#     W = []
#     h, w, s = estimate_body_size(LANDMARKS['RIGHT_ANKLE'], LANDMARKS['LEFT_ANKLE'], LANDMARKS['RIGHT_HIP'], LANDMARKS['LEFT_HIP'], LANDMARKS['RIGHT_SHOULDER'], LANDMARKS['LEFT_SHOULDER'], LANDMARKS['RIGHT_ELBOW'], LANDMARKS['LEFT_ELBOW'], 
#                                                                                          LANDMARKS['RIGHT_KNEE'], LANDMARKS['LEFT_KNEE'], LANDMARKS['RIGHT_WRIST'], LANDMARKS['LEFT_WRIST'], SIZES['HEIGHT'])
#     return s

image = st.file_uploader("", type="jpg")
if image is not None:
    # image.name
    name = image.name
    st.write(name)

    inx = name.rfind(".")
    st.write(len(name), inx)

    s = int(name[inx-1])
    st.write(s)
    image = Image.open(image)
    # st.image(image)

    converted_img = np.array(image.convert('RGB'))
    st.image(converted_img)
    st.write(converted_img)