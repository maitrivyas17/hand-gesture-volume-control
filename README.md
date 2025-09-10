# Hand Gesture Volume Control 🎶✋

So here’s the story… I was sitting in a café one day, learned about **MediaPipe**, and thought — *“I just wanted to try out MediaPipe and OpenCV”*. After one 
Ice latte and cream cheese bagel ☕ and after wrestling with OpenCV, NumPy, and Pycaw, this little project was born.

Basically:  
👉 Move your **thumb and index finger apart** → volume goes up.  
👉 Bring them closer → volume goes down.  
Simple, fun, and surprisingly addictive to play with 

---

## What it does
- Tracks your hand in real-time using **MediaPipe Hands** 🖐  
- Uses **OpenCV** to capture webcam frames 🎥  
- Measures distance between thumb tip & index tip ✌️  
- Maps that distance to your **system volume** with **Pycaw** 🔊  
- Works only on Windows (because Pycaw is Windows-only)

---

## How to run it
1. Clone this repo:
   ```bash
   git clone https://github.com/maitrivyas17/hand-gesture-volume-control.git
   cd hand-gesture-volume-control
   ```
2. Install the requirements:
   ```bash
   pip install pip install opencv-python mediapipe numpy pycaw comtypes
   ```
3. Run the script:
   ```bash
   python demo.py
   ```

Press **ESC** to quit. (Otherwise it’ll just keep staring at you 👀)

---

## Requirements
- Python 3.8+
- Webcam
- Windows 10/11 (for audio control)
- Libraries: `opencv-python`, `mediapipe`, `numpy`, `pycaw`, `comtypes`

---

--

## Why I made this
Honestly? Pure curiosity. I just wanted to see if I could control my laptop volume without touching the keyboard. Ended up learning a lot about **computer vision**, **landmark detection**, and how system audio works in Windows.  

---


### P.S.
If you’re reading this, try it. You’ll end up pinching the air like a DJ at some point. haha!