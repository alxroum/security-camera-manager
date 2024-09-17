# import gui
import json


class Camera:

    def __init__(self, name='unnamed_cam_01', cv_id=0, cam_type=0, save_interval=120):
        # this class gets instanced for every camera in the list according to the json file
        self.__name = name
        self.__cv_id = cv_id
        self.__cam_type = cam_type  # wired or wireless - 0 or 1 respectively
        self.__save_interval = save_interval  # seconds between saves
        self.__is_recording = False

        self.__info_dict = {}

        # make sure camera type is in range
        if self.__cam_type != 0 or self.__cam_type != 1:
            self.__cam_type = 0

    def get_cam_info(self):  # returns a dictionary with all cameras information intended for json writing

        self.__info_dict = {
            'Name': self.__name,
            'CV_ID': self.__cv_id,
            'Type': self.__cam_type,
            'Save Interval': self.__save_interval,
            'Is Recording': self.__is_recording
        }

        return self.__info_dict

    def get_name(self):
        return self.__name

    def get_save_interval(self):
        return self.__save_interval

    def is_recording(self):
        return self.__is_recording


    def __str__(self):
        return json.dumps(self.get_cam_info(), indent=4)


def main():
    cam = Camera()
    print(cam)


if __name__ == '__main__':
    main()
