import cv2
import mediapipe as mp
import math
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
# Get audio device and volume interface
device = AudioUtilities.GetSpeakers()
interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

print(f"Audio output: {device.GetId()}")


vRange = volume.GetVolumeRange()
minv, maxv = vRange[0], vRange[1]


mp_hands = mp.solutions.hands
draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()


capture = cv2.VideoCapture(0)
tpx, tpy = 0, 0

while True:
    value, image = capture.read()
    rgbimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image = hands.process(rgbimage)
    print(processed_image.multi_hand_landmarks)

    if processed_image.multi_hand_landmarks:
        for handLandmarks in processed_image.multi_hand_landmarks:
            for finger_id, landmark_co in enumerate(handLandmarks.landmark):
                height, width, channel = image.shape
                cx, cy = int(landmark_co.x * width), int(landmark_co.y * height)

                if finger_id == 4:
                    cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                    tpx, tpy = cx, cy

                if finger_id == 8:
                    cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                    ipx, ipy = cx, cy
                    cv2.line(image, (tpx, tpy), (ipx, ipy), (0, 255, 0), 2)
                    distance = math.sqrt((ipx - tpx) ** 2 + (ipy - tpy) ** 2)
                    print(distance)
                    v = np.interp(distance, [25, 250], [minv, maxv])
                    volume.SetMasterVolumeLevel(v, None)

            draw.draw_landmarks(image, handLandmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Image capture', image)
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
