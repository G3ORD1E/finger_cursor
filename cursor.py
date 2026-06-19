import cv2 as c
import mediapipe as mp
import pyautogui 
#---------------------------
# this code is used to control the mouse cursor using hand tracking with the help of mediapipe , opencv and pyautogui libraries
#---------------------------
hand = mp.solutions.hands.Hands() #this is used to get hand tracking from mediapipe solutions
hand_draw = mp.solutions.drawing_utils #this is used to draw the hand landmarks on the video
livevideo = c.VideoCapture(0) # this live captures video from the camera by default it is default camera
livevideo.set(c.CAP_PROP_FRAME_WIDTH, 640)
livevideo.set(c.CAP_PROP_FRAME_HEIGHT, 480)
screen_x,screen_y = pyautogui.size() #this is used to get the size of the screen of the computer
while True:
    ret,frame = livevideo.read()
    if not ret:
        print("error : camera not working")
    rgbformat = c.cvtColor(frame,c.COLOR_BGR2RGB)
    handlandmark = hand.process(rgbformat)
    #---------------------------
    if handlandmark.multi_hand_landmarks:
        handLms = handlandmark.multi_hand_landmarks[0]
        index_pos = handLms.landmark[8]
        h,w,color_channels= frame.shape
        x = index_pos.x*w   #to find x value of index finger
        y = index_pos.y*h   #to find y value of index finger
        c.circle(frame,(int(x),int(y)),15,(0,255,0),-1)
        hand_draw.draw_landmarks(frame,handLms,mp.solutions.hands.HAND_CONNECTIONS)#this will draw full landmark of hand
        #-----------------------
        mouse_x = (x / w) * screen_x
        mouse_y = (y / h) * screen_y
        pyautogui.moveTo(mouse_x,mouse_y)
    #---------------------------
    c.imshow('CURSOR GO BRRRRR',frame)# now it creates the window and shows the video
    if c.waitKey(1) == ord("q"):# clicking on q 
        break

livevideo.release()
c.destroyAllWindows()
