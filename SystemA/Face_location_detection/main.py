from detection_stream_functions import *
from serial_communication_functions import *

if __name__ == "__main__":
    # Initialize arduino
    # port = '/dev/cu.usbserial-00000000'
    # arduinoObj = arduino_object(port)
    # arduinoObj.clear_read_buffer()
    FPS = -1
    theta_z_deg = 0
    theta_y_deg = 0
    while True:
        #################### Camera measurements ####################
        FPS_timer_start_time = time.time()
        result, video_frame = video_capture.read()  # read frames from the video
        if result is False:
            break  # terminate the loop if the frame is not read successfully
        video_frame = cv2.flip(video_frame, 1)
        faces = detect_bounding_box(
            video_frame
        ) 

        show_this_frame = video_frame
        show_this_frame = add_central_lines(show_this_frame)

        # For displaying the
        font = cv2.FONT_HERSHEY_SIMPLEX 
        fontScale = 1
        color = (255, 0, 0) 
        print(faces)
        # Line thickness of 2 px 
        thickness = 2
        try:
            show_this_frame = cv2.putText(show_this_frame, f'x = {faces[0]}, y = {faces[1]}, w = {faces[2]}, h = {faces[3]}', (50, 50), font,  
                    fontScale, color, thickness, cv2.LINE_AA)
            show_this_frame = add_arrawed_line_to_face_coord(show_this_frame, faces)
            theta_z_rad, theta_y_rad, theta_z_deg, theta_y_deg = rot_angle_estimator(faces)
            show_this_frame = cv2.putText(show_this_frame, f'theta_y = {theta_z_deg}[deg], theta_z = {theta_y_deg}[deg]', (50,100), font,  
                    fontScale, color, thickness, cv2.LINE_AA)
            show_this_frame = cv2.putText(show_this_frame, f'FPS: {FPS}', (50,150), font,  
                    fontScale, color, thickness, cv2.LINE_AA)
        except:
            show_this_frame = cv2.putText(show_this_frame, 'No face is detected!', (50, 50), font,  
                    fontScale, color, thickness, cv2.LINE_AA)
        
        cv2.imshow(
            "My Face Detection Project", show_this_frame
        )  # display the processed frame in a window named "My Face Detection Project"

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
        #################### Update camera control ####################
        # theta_z_command = deg_to_arduino_servo_control(theta_z_deg)
        # theta_y_command = deg_to_arduino_servo_control(theta_y_deg)
        # for i in range(1):
            # arduinoObj.fast_send_2_data_to_serial_dev(theta_z_command, theta_y_command)
        # arduinoObj.read_n_print()
        # time.sleep(0.5)
        print()
        ######## FPS counter
        one_cycle_time = time.time() - FPS_timer_start_time
        FPS = round(1/one_cycle_time, 2)

    # On exiting
    video_capture.release()
    cv2.destroyAllWindows()
