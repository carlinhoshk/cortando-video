import cv2

def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)

    success, image = vidObj.read()

    cv2.imwrite("img_1.jpg", image)

if __name__ == '__main__':
    FrameCapture("12.mp4")
