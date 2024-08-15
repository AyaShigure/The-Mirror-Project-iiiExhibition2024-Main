from detection_stream_functions import *

if __name__ == "__main__":



    while True:
        result, video_frame = video_capture.read()  # read frames from the video
        if result is False:
            break  # terminate the loop if the frame is not read successfully

        faces = detect_bounding_box(
            video_frame
        ) 
        # apply the function we created to the video frame
        # except:
        #     pass

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