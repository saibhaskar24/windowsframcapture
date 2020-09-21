import numpy as np
import cv2 as cv
import pyautogui
from time import time
from PIL import ImageGrab

start = time()
while True:
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    cv.imshow("Screen Shoot", screenshot)
    print(f'FPS { 1 / (time() - start) }')
    start = time()
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
print("Done")