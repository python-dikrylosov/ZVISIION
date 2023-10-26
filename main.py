
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import matplotlib.pyplot as plt
weights, heights = pyautogui.size()

camera = cv2.VideoCapture(0)


while True:
    for i in range(1):
        plt.clf()
        ret, frame = camera.read()

        screen = np.array(ImageGrab.grab(bbox=(0,0,weights, heights)))

        resized = cv2.resize(screen,(640,360))


        cv2.imwrite("frame.png", frame)
        read = cv2.imread("frame.png")

        cv2.imwrite("screen.png", screen)
        screen = cv2.imread("screen.png")

        #cv2.imshow("frame.png", read)
        #cv2.imshow("screen.png", screen)
        cv2.imshow("resized", resized)

        img = cv2.imread("frame.png", cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"
        ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
        ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
        ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
        titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
        images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
        for i in range(6):
            plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        mframe = 1 / 30
        plt.pause(mframe)



    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.DestroyAlllWindows()
        break

plt.show()
