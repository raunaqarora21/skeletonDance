import cv2
import numpy as np
import time
import mediapipe as mp
cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
cap.set(10,150)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
pTime = 0
mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
pose = mpPose.Pose(
     min_detection_confidence=0.5,
    min_tracking_confidence=0.5

)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
        

    frame = cv2.resize(frame, (600, 500))
    
    frame.flags.writeable = False
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)

    frame.flags.writeable = True
    main = results.pose_landmarks
    if results.pose_landmarks :
        # print(results.pose_landmarks)
        for landmark in main.landmark:
            landmark.x+= 0.4
            
            # landmark.y+=0.5
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS,  connection_drawing_spec= mpDraw.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2))
      
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # frame.translateXY(0, 0)
    # cv2.flip(frame, 1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
