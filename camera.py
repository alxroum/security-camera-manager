# import gui
import json


class Camera:

    def __init__(self, name='unnamed_cam_00', cam_type=0):
        self.__name = name
        self.__cam_type = cam_type

        self.__info_dict = {}

        if self.__cam_type != 0 or self.__cam_type != 1:
            self.__cam_type = 0

        if self.__cam_type == 0:  # wired camera
            pass
        else:  # network camera
            pass

    def get_cam_info(self):  # returns a dictionary with all cameras information intended for json writing

        self.__info_dict = {
            'Name': self.__name,
            'Type': self.__cam_type
        }

        return self.__info_dict

    def __str__(self):
        return json.dumps(self.get_cam_info(), indent=4)


def main():
    cam = Camera()
    print(cam)


if __name__ == '__main__':
    main()
