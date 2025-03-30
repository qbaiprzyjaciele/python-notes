# this simple script allows to control MIDI commands using hand gestures 
# detected in certain areas of the camera viewport

import cv2
import math
import mediapipe as mp
from mido import Message, open_output, get_output_names

MIDI_PORT = 'QbToAbleton 2'
print(get_output_names())
midi_out = open_output(MIDI_PORT)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6) 
drawing = mp.solutions.drawing_utils

video_capture = cv2.VideoCapture(1)

hand_detected = False

WRIST_INDEX = 0
THUMB_INDEX = 4
POINT_FINGER_TIP_INDEX = 8
POINT_FINGER_DOWN_INDEX = 6

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_withing_bounding_box(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

def is_in_top_right(x, y, width, height):
    return is_withing_bounding_box(x, y, 0.5*width, 0, width, 0.25*height)

while True:
    ret, frame  = video_capture.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    height, width, _ = frame.shape
    cv2.line(frame, (0, int( 0.25*height)), (width, int(0.25*height)), (0, 255, 0), 2)
    cv2.line(frame, (int(0.5*width), int( 0.25*height)), (int(0.5*width), 0), (0, 255, 0), 2)
    if results.multi_hand_landmarks:
        hand_detected = True
        for hand_landmarks in results.multi_hand_landmarks:
            wrist = hand_landmarks.landmark[WRIST_INDEX]
            point_finger_tip = hand_landmarks.landmark[POINT_FINGER_TIP_INDEX]
            sth = hand_landmarks.landmark[1]
            wrist_x = int(wrist.x * width)
            wrist_y = int(wrist.y * height)
            point_finger_tip_x = int(point_finger_tip.x * width)
            point_finger_tip_y = int(point_finger_tip.y * height)
            sth_x = int(sth.x * width)
            sth_y = int(sth.y * height)
            cv2.circle(frame, (point_finger_tip_x, point_finger_tip_y), 15, (0, 255, 0), -1)
            cv2.circle(frame, (wrist_x, wrist_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (sth_x, sth_y), 10, (0, 255, 0), -1)
            drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if is_in_top_right(point_finger_tip.x, point_finger_tip.y, 1, 1):
                tip_distance = distance(wrist.x, wrist.y, point_finger_tip.x, point_finger_tip.y)
                if tip_distance > 0.275:
                    scale_x = (point_finger_tip.x - 0.5)/0.5
                    scale_y = point_finger_tip.y/0.25
                    message_x = int(127*scale_x)
                    message_y = int(127*scale_y)
                    msg_x = Message('control_change', control=1, value=message_x)
                    msg_y = Message('control_change', control=2, value=message_y)
                    midi_out.send(msg_x)
                    midi_out.send(msg_y)
    else:
        hand_detected = False
    
    cv2.imshow("Tracking hands", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
