import cv2
import numpy as np
 
# Read image
im = cv2.imread("./Capture.JPG")
cv2.imshow("f", im)
detector = cv2.SimpleBlobDetector()
keypoints = detector.detect(im)
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(100)