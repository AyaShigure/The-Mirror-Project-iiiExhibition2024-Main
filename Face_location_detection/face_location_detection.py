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


import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(0)

# Get the input footage size
_, video_frame = video_capture.read()
video_size_x = video_frame.shape[1]
video_size_y = video_frame.shape[0]
print(f'size_x = {video_size_x}, size_y = {video_size_y}')

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(80, 80))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

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

    x,y,w,h = faces[0]
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

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    face_coordinate_x = 0
    face_coordinate_y = 0
    # show_this_frame = cv2.flip(video_frame,1)
    show_this_frame = video_frame
    show_this_frame = add_central_lines(show_this_frame)

    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    
    # org 
    org = (50, 50) 
    
    # fontScale 
    fontScale = 1
    
    # Blue color in BGR 
    color = (255, 0, 0) 
    print(faces)
    # Line thickness of 2 px 
    thickness = 2
    try:
        show_this_frame = cv2.putText(show_this_frame, f'x = {faces[0][0]}, y = {faces[0][1]}, w = {faces[0][2]}, h = {faces[0][3]}', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
        show_this_frame = add_arrawed_line_to_face_coord(show_this_frame, faces)

    except:
        show_this_frame = cv2.putText(show_this_frame, 'No face is detected!', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow(
        "My Face Detection Project", show_this_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()