# The Mirror Porject (A iiiExhibition2024 Project)

### Notes for myself on 2024-8-18
1. The system consists of two sets of cameras. Camera A is stationary and is for face detection, face location estimation and servo motor control via serial communication to a arduino board.
2. The second set of camera is mounted to the rotational platfrom driven by servos. The captured frame is sent to InsightFace for swapping and displaying.

### System checklist, just a reminder for myself that U NEED TO KEEPPPPPUPAAAAAAAAAAAAAA AAAAA
## Camera system A
1.  The platfrom mechanism.
2.  The electrical system(Switch power supply & voltage regulators) for powering the arduino and the servos.
3.  An Arduino which takes in target pose data for the servos, and update the servo control in each control cycle.
4.  A face detection script in python with cv2, estimates the location of the face and sends the control(filter is needed in future) to the Arduino board via serial.

## Camera system B
1.  A camera mounted on the rotational platfrom driven by system A.
2.  A multiprocessing python script which sends captured frame from system B through InsightFace, eventually to the display. Blur the output when there is no face detected.