import cv2
import numpy as np

def detect_lane_center(frame):
    height, width = frame.shape[:2] # set variables height and width to the dimensions of the 2d list frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # gray is a grayed out version of frame
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # blur is the gaussian blurred version of gray(removes imperfections in image)
    edges = cv2.Canny(blur, 50, 150) #Canny blur does similar to Gaussian Blur

    mask = np.zeros_like(edges) #sets every element in edges to 0
    roi_corners = np.array([[(0, height), (width, height), (width, int(height * 0.6)), (0, int(height * 0.6))]])
    cv2.fillPoly(mask, roi_corners, 255) # fill the lane shape
    cropped_edges = cv2.bitwise_and(edges, mask)

    lines = cv2.HoughLinesP(cropped_edges, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=50)
    if lines is None:
        return width // 2  # Default to center if no lines found

    lane_centers = []
    for line in lines: # for every line in the list of detected lines
        x1, y1, x2, y2 = line[0]
        mid_x = (x1 + x2) // 2
        lane_centers.append(mid_x) # add center of the lane to lane_centers list

    return int(np.mean(lane_centers)) # return the mean of the values in the mean centers list
