import datetime
from PIL import ImageGrab
import numpy as np
import cv2 as cv
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f"{time_stamp}.mp4"

fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv.VideoWriter(file_name, fourcc, 20.0, (width, height))


while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv.cvtColor(img_np, cv.COLOR_BGR2RGB)
    cv.imshow("Screen Recorder", img_final)
    captured_video.write(img_final)
    if cv.waitKey(10) == ord('q'):
        break
