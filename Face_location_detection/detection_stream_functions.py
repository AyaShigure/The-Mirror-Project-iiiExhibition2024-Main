# 2024-7-16
# Face dection from webcamera stream
# This script is for calculating the proper angel for the camera to point to.


# Notes/Todo 

# 1. Get the biggest face from the video stream, or change the therothold of the face classifier
# 2. get some smooth filter in there: 
#       Filter logic: the detected face should have a speed, and it is not possible to change position too drastically.
# 3. Estimate the distance from the camera the the viewer, using the size of bounding box
# 4. Get the size of the captured image, display the central horizontal and vertical of the captured image
# 5. Calculate the distance, then use the distances from the camera and distanc to the center to calculate the pitch and yaw angle.
# 5.5 Calculate/Estimate the angles & translation (homogeneous transformations?) from the camera frome

# 6. Need to get some data filtering to prevent uncontrollable shaking on the servo.
# 7. Kalman filter?


# Note 2024-7-22
# 1. Add logic: If face box is larger than xxx, active tracking and hardware serial communication and control.

import cv2


face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(0)

# Get the input footage size
_, video_frame = video_capture.read()
video_size_x = video_frame.shape[1]
video_size_y = video_frame.shape[0]
print(f'video_size_x = {video_size_x}, video_size_y = {video_size_y}')


def detect_bounding_box(vid): 
    '''
        Modified on 2024/8/15:
            1.  Added logic to show only the biggest face
    '''
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(80, 80))
    print(f'len_faces = {len(faces)}')

    # try:
    if len(faces) == 1:
        for (x, y, w, h) in faces:
            cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        return faces[0]
    elif len(faces) > 1: # Only show the biggest one 
        detected_face_size = []
        for (x, y, w, h) in faces:
            # Notice that 'w' and 'h' are always the same
            detected_face_size.append(w)
        biggest_face_size = max(detected_face_size)
        biggest_face_index = detected_face_size.index(biggest_face_size)

        cv2.rectangle(vid, 
                    (faces[biggest_face_index][0], faces[biggest_face_index][1]), 
                    (faces[biggest_face_index][0] + biggest_face_size, faces[biggest_face_index][1] + biggest_face_size), 
                    (0, 255, 0), 
                    4)
        return faces[biggest_face_index]
    # except:
    #     return 

def add_central_lines(vid):
    x_left = 0
    x_right = video_size_x
    x_central = int(video_size_x/2)
    y_low = 0
    y_high = video_size_y
    y_central = int(video_size_y/2)

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

def add_arrawed_line_to_face_coord(vid, faces):
    # Center of the frame
    x_central = int(video_size_x/2)
    y_central = int(video_size_y/2)

    x,y,w,h = faces
    x_face = x + int(w/2)
    y_face = y + int(h/2)

    # represents the top left corner of image  
    start_point = (x_central, y_central)  
    
    # End coordinate 
    end_point = (x_face, y_face)  
    
    # Green color in BGR  
    color = (0, 0, 255)  
    
    # Line thickness of 9 px  
    thickness = 2
    
    # Using cv2.arrowedLine() method  
    # Draw a diagonal green arrow line 
    # with thickness of 9 px  
    vid = cv2.arrowedLine(vid, start_point, end_point, 
                                        color, thickness) 

    return vid


def estimate_distance(face):
    '''
        average_width_of_a_head = 150 # mm
        width_of_a_head_in_pixel = w
        mm_per_pixel = average_width_of_a_head / width_of_a_head_in_pixel


        mat = np.matrix([[100,1],[42,1]])
        np.linalg.inv(mat) * np.matrix([[140], [370]])
    '''
    x,y,w,h = face

    # y = ax+b, y: pixels, x:dist
    a = -3.96551724
    b = 536.55172414

    x = round((y - b)/ a, 2)

    print(f'Estimated distance is {x}')
