import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands()

pTime = 0
cTime = 0
# handLms = hand landmark

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # imgRGB = cv2.flip(imgRGB, 1)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                # if id == 4:
                #     cv2.circle(img, (cx,cy), 25, (255,0,0), cv2.FILLED)
                cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
                cv2.putText(img,str(int(id)), (cx+8,cy+8), cv2.FONT_HERSHEY_SIMPLEX,0.35, (0,0,255), 1)
                
            thumb_tip = handLms.landmark[4] # get the landmark of thumb tip
            index_tip = handLms.landmark[8] # get the landmark of index finger tip
            thumb_x, thumb_y = int(thumb_tip.x*w), int(thumb_tip.y*h)
            index_x, index_y = int(index_tip.x*w), int(index_tip.y*h)
            distance = ((thumb_x-index_x)**2 + (thumb_y-index_y)**2)**0.5 # calculate the distance between the landmarks
            if distance < 50: # if distance is less than 50 pixels, fingers are considered touching
                print("true")
                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    cTime = time.time()
    fps = 1/(cTime-pTime)          
    pTime = cTime
    
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,2 , (255,0,255), 2) 
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
