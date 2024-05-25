import cv2
import threading


class cam_thread(threading.Thread):
    def __init__(self, preview_name, cam_id):
        threading.Thread.__init__(self)
        self.preview_name = preview_name
        self.cam_id = cam_id

    def run(self):
        print("Starting " + self.preview_name)
        cam_preview(self.preview_name, self.cam_id)


def cam_preview(preview_name, cam_id):
    cv2.namedWindow(preview_name)
    cam = cv2.VideoCapture(cam_id)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.imshow(preview_name, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(preview_name)


# Create two threads as follows
thread1 = cam_thread("Camera 0", 0)
thread2 = cam_thread("Camera 1", 1)
thread1.start()
thread2.start()