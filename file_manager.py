import gui
import cv2


def main():
    print('Starting Program ...')
    stream_video()


def stream_video():
    url = 'http://192.168.0.110:8080/video'
    cap = cv2.VideoCapture(url)

    while True:
        ret, frame = cap.read()
        if frame is not None:
            cv2.imshow("frame", frame)

        q = cv2.waitKey(1)
        if q == ord("q"):
            break

    cv2.destroyAllWindows



main()
