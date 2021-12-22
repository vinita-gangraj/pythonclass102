import cv2
def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame =videoCaptureObject.read()
        print(ret)
        #cv2.imwrite() method is usedto save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result = False
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()
take_snapshot()


