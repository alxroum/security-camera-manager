from camera import Camera
import json


class CameraManager:

    def __init__(self, save_file):
        self.__cameras = []
        self.__save_file = save_file
        self.read_file()  # always read the file first and get the saved data into the program

    def add_camera(self, camera: Camera):
        self.__cameras.append(camera.get_cam_info())

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

    def __str__(self):
        return json.dumps(self.__cameras, indent=4)


c1 = Camera('Camera 1', 0, 0)
c2 = Camera('Camera 2', 0, 0)
c = CameraManager('camera_data.json')
c.add_camera(c1)
c.add_camera(c2)
#c.write_file()
c.read_file()
#print(c)
