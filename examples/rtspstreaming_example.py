import cv2
from lucastamatescu import rtspstreaming

frame_queue=rtspstreaming.start_rtsp_streaming()

vs=cv2.VideoCapture(0)

while True:
    ret, frame = vs.read()
    rtspstreaming.update_frame(frame_queue, frame)
