from main_code.moduless import  *
from main_code.confi import *



def take_pic_from_cam():
    cam = cv2.VideoCapture(1)  # 0 -> index of camera
    s, img = cam.read()

    return img


def save_pic_to_path(img, path):
    cv2.imwrite(path, img)


def checking_number_of_pills():
    save_pic_to_path(take_pic_from_cam(), "resuorses/Temp1.jpg")






    NumOfPills = 0


    return (NumOfPills)