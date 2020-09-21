import numpy as np
import cv2 as cv
import pyautogui
while True:
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    cv.imshow("Screen Shoot",screenshot)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
print("Done")