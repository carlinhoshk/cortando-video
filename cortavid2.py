import cv2
vidcap = cv2.VideoCapture('12.mp4')
currentFrame = 0
while(True):
	
	vidcap.set(cv2.CAP_PROP_POS_MSEC,1000)      # corta em 20 sec.
	success,image = vidcap.read()
	if success:
	    name = './data/frame' + str(currentFrame) + '.jpg'
	    cv2.imwrite(name, image)     # salva frame como JPEG 
	    cv2.imshow(name,image)
	    cv2.waitKey()    
