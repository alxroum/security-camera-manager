import gui
import cv2

def main():
    print('Starting Program ...')
    #capture_video("camera_1")


def capture_video(camera_name):
    vc = cv2.VideoCapture(0)

    while(True):

        frame = vc.read()

        cv2.imshow(camera_name, frame)

        


    vc.release()
    
    cv2.destroyAllWindows()

if __name__ == "__file_manager__":
    main()