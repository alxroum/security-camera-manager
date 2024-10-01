from camera import Camera
import json
import cv2


class CameraManager:

    def __init__(self, save_file):
        self.__cameras = {}
        self.__save_file = save_file
        self.read_file()  # always read the file first and get the saved data into the program

    def add_camera(self, camera: Camera):
        _id = len(self.__cameras)
        self.__cameras[_id] = camera.get_cam_info()

    def write_file(self):
        with open(self.__save_file, 'w') as file:
            json.dump(self.__cameras, file, indent=4)
            return True

    def read_file(self):
        temp = []
        try:
            with open(self.__save_file, 'r') as file:
                temp = json.load(file)
                self.__cameras = temp
        except FileNotFoundError:
            print('File Does Not Exist.')

    def make_cams_from_data(self):  # creates camera objects from the json file
        data = self.__cameras
        cams = []

        for i in data.keys():
            name = data[i]['Name']
            cv_id = data[i]['CV_ID']
            type_ = data[i]['Type']
            si = data[i]['Save Interval']
            temp = Camera(name, cv_id, type_, si)

    def get_entries(self):
        return self.__cameras

    def __str__(self):
        return json.dumps(self.__cameras, indent=4)


"""
c = CameraManager('camera_data.json')
c1 = Camera('Camera 1', 0, 0, 120)
c2 = Camera('Camera 2', 1, 0, 120)
c.add_camera(c1)
c.add_camera(c2)
c.write_file()
"""

c = CameraManager('cam_data_copy.json')
cams = c.make_cams_from_data()
print(cams)
