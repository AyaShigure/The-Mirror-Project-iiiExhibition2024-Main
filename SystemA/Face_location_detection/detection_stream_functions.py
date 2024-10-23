# 2024-7-16
# Face dection from webcamera stream
# This script is for calculating the proper angel for the camera to point to.


# Notes/Todo 

# 1. (DONE) Get the biggest face from the video stream, or change the therothold of the face classifier
# 2. get some smooth filter in there: 
#       Filter logic: the detected face should have a speed, and it is not possible to change position too drastically.
# 3. (DONE) Estimate the distance from the camera the the viewer, using the size of bounding box
# 4. (DONE) Get the size of the captured image, display the central horizontal and vertical of the captured image
# 5. (DONE) Calculate the distance, then use the distances from the camera and distanc to the center to calculate the pitch and yaw angle.
# 5.5 Calculate/Estimate the angles & translation (homogeneous transformations?) from the camera frame

# 6. Need to get some data filtering to prevent uncontrollable shaking on the servo.
# 7. Kalman filter?

# 8. Currently this is a single process, upgrade this to multiprocess for better performance.


# Note 2024-7-22
# 1. Add logic: If face box is larger than xxx, active tracking and hardware serial communication and control.

# Note 2024-8-16
# 1. Updated face distance and angle estimations
# 2. Currently this is a single process, upgrade this to multiprocess for better performance.

# Note 2024-8-18
# 1. Updated the resolution settings, 680x420 reachs 30fps for detection.

import cv2
import numpy as np
import time


# CAMERA_RESILUTION = [100,100] # example: [1080, 720] # or [-1] for default maximun resolution.
CAMERA_RESILUTION = [-1] # example: [1080, 720] # or [-1] for default maximun resolution.

'''
    The CAMERA_RESILUTION can only be some few pre set value, but when inputing random width and height, the system will set the resolution to the closest one.

'''
# Initializations
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
video_capture = cv2.VideoCapture(0)
if CAMERA_RESILUTION[0] != -1:
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_RESILUTION[0])
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_RESILUTION[1])


# Get the input footage size
_, video_frame = video_capture.read()
# Input video size
video_size_x = video_frame.shape[1]
video_size_y = video_frame.shape[0]
x_central = int(video_size_x/2)
y_central = int(video_size_y/2)
print(f'video_size_x = {video_size_x}, video_size_y = {video_size_y}')


x_left = 0
x_right = video_size_x
y_low = 0
y_high = video_size_y
def add_central_lines(vid):
    '''
        Add cross lines on the screen
    '''
    # Green color in BGR
    color = (0, 255, 0)
    # Line thickness of 2 px
    thickness = 2

    horizontal_start_coord = (x_left, y_central) 
    horizontal_end_coord = (x_right, y_central)
    vertical_start_coord = (x_central, y_low)
    vertical_end_coord = (x_central, y_high)
    vid = cv2.line(vid, horizontal_start_coord, horizontal_end_coord, color, thickness)
    vid = cv2.line(vid, vertical_start_coord, vertical_end_coord, color, thickness)
    return vid


def detect_bounding_box(vid): 
    '''
        Modified on 2024/8/15:
            1.  Added logic to show only the biggest face
    '''
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(80, 80))
    print(f'len_faces = {len(faces)}')

    if len(faces) == 1:
        for (x, y, w, h) in faces:
            cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        return faces[0]
    elif len(faces) > 1: # Only show the biggest one 
        # Add bounding box
        detected_face_size = []
        for (x, y, w, h) in faces:
            # Notice that 'w' and 'h' are always the same
            detected_face_size.append(w)
        biggest_face_size = max(detected_face_size)
        biggest_face_index = detected_face_size.index(biggest_face_size)

        vid = cv2.rectangle(vid, 
                    (faces[biggest_face_index][0], faces[biggest_face_index][1]), 
                    (faces[biggest_face_index][0] + biggest_face_size, faces[biggest_face_index][1] + biggest_face_size), 
                    (0, 255, 0), 
                    4)
        
        return faces[biggest_face_index]

def add_arrawed_line_to_face_coord(vid, faces):
    # Center of the frame
    x_central = int(video_size_x/2)
    y_central = int(video_size_y/2)

    x,y,w,h = faces
    x_face = x + int(w/2)
    y_face = y + int(h/2)

    start_point = (x_central, y_central)  
    end_point = (x_face, y_face)  
    color = (0, 0, 255) # Green color in BGR  
    thickness = 2
    
    # Using cv2.arrowedLine() method  
    vid = cv2.arrowedLine(vid, start_point, end_point, 
                                        color, thickness) 

    return vid

def rot_angle_estimator(face):
    '''
        !!!!! This block needs to be revised if the camera is changed.
    
        This is modeled with a linear equation d = ap+b, where p is pixels, d is dist, a and b are constants.

        Measured data: 100cm -> 140 pixels
                       42cm  -> 370 pixels
        
        Solve the inversion of constant matrix to solve a and b
        mat = np.matrix([[140,1],[370,1]])
        np.linalg.inv(mat) * np.matrix([[100], [42]])

        a = -0.25217391
        b = 135.30434783
    '''
    x,y,w,h = face

    # d = ap+b, p:pixels, d:dist
    a = -0.25217391
    b = 135.30434783
    est_dist = round(a * w + b, 2)
    pixels_per_centimeter = w / 15 # This constant is used to calculate the angles for the camera to rotate
    print(f'Estimated distance is {est_dist} cm')

    x_face = x + int(w/2)
    y_face = y + int(h/2)

    horizontal_distance_off_center = round((x_face - x_central) / pixels_per_centimeter, 2) # [pixel] / [pixel/cm] = [cm]
    vertical_distance_off_center = round((y_central - y_face) / pixels_per_centimeter, 2) # [pixel] / [pixel/cm] = [cm]
    print(f'Horizontal off center: {horizontal_distance_off_center}cm')
    print(f'Vertical off center: {vertical_distance_off_center}cm')

    theta_z_rad = round(np.arctan2(horizontal_distance_off_center, est_dist),4)
    theta_y_rad = round(np.arctan2(vertical_distance_off_center, est_dist), 4)
    theta_z_deg = round(np.rad2deg(theta_z_rad), 3)
    theta_y_deg = round(np.rad2deg(theta_y_rad), 3)
    print(f'Estmated rotation angle: theta_z = {theta_z_rad}rad, ({theta_z_deg}deg)')
    print(f'Estmated rotation angle: theta_y = {theta_z_rad}rad, ({theta_y_deg}deg)')

    return  theta_z_rad, theta_y_rad, theta_z_deg, theta_y_deg

# def run_frame_processing():
#     FPS = -1
#     while True:
#         FPS_timer_start_time = time.time()
#         result, video_frame = video_capture.read()  # read frames from the video
#         if result is False:
#             break  # terminate the loop if the frame is not read successfully
#         video_frame = cv2.flip(video_frame, 1)
#         faces = detect_bounding_box(
#             video_frame
#         ) 

#         show_this_frame = video_frame
#         show_this_frame = add_central_lines(show_this_frame)

#         # For displaying the
#         font = cv2.FONT_HERSHEY_SIMPLEX 
#         fontScale = 1
#         color = (255, 0, 0) 
#         print(faces)
#         # Line thickness of 2 px 
#         thickness = 2
#         try:
#             show_this_frame = cv2.putText(show_this_frame, f'x = {faces[0]}, y = {faces[1]}, w = {faces[2]}, h = {faces[3]}', (50, 50), font,  
#                     fontScale, color, thickness, cv2.LINE_AA)
#             show_this_frame = add_arrawed_line_to_face_coord(show_this_frame, faces)
#             theta_z_rad, theta_y_rad, theta_z_deg, theta_y_deg = rot_angle_estimator(faces)
#             show_this_frame = cv2.putText(show_this_frame, f'theta_y = {theta_z_deg}[deg], theta_z = {theta_y_deg}[deg]', (50,100), font,  
#                     fontScale, color, thickness, cv2.LINE_AA)
#             show_this_frame = cv2.putText(show_this_frame, f'FPS: {FPS}', (50,150), font,  
#                     fontScale, color, thickness, cv2.LINE_AA)
#         except:
#             show_this_frame = cv2.putText(show_this_frame, 'No face is detected!', (50, 50), font,  
#                     fontScale, color, thickness, cv2.LINE_AA)
        
#         cv2.imshow(
#             "My Face Detection Project", show_this_frame
#         )  # display the processed frame in a window named "My Face Detection Project"

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
        
#         one_cycle_time = time.time() - FPS_timer_start_time
#         FPS = round(1/one_cycle_time, 2)

#     # On exiting
#     video_capture.release()
#     cv2.destroyAllWindows()

