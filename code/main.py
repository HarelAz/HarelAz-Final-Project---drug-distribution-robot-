'''
Main menu:
1.Machine ON
2.Patients List
3.View drug inventory
4.Collect a pill by name
5.calibration
6.machine off and close

'''









if __name__ == '__main__':
    ############################## Variable ##############################
    # Pill_Floor = int            #The floor where the pill is
    # Current_Floor = int         #The current floor where the arm is
    # Pill_Angle = int            #The angle where the pill is
    # Current_Angle = int         #The current floor where the arm is
    #
    # Pic1, Pic2, TempPic, Temp   #Future Variables
    #
    # Pill_List                   #List of patient pills
    Robot.spinLeft(15)

    ############################## Homing Function ##############################
    Homing()

    ############################## Start ##############################
    Pill_Amount =  # The amount of pills in the list


    def is_the_robot_in_right_floor(Current_Floor, Pill_Floor):
        """
        :param Current_Floor:
        :param Pill_Floor:
        :return: True/False
        """
        return Current_Floor > Pill_Floor


    while Pill_Amount > 0:
        for Pill_Num in [1, Pill_Amount]:

            Pill_Floor =
            Pill_Angle =

            # if Current_Floor > Pill_Floor: #check if ther robot is in the right posotopn
            if is_the_robot_in_right_floor(Current_Floor, Pill_Floor):  # check if ther robot is in the right posotopn
            # Current_Angle = 0#
            # Current_Floor = Down#
            elif Current_Floor < Pill_Floor:
            # Current_Angle = 0#
            # Current_Floor = Up#
            else:  # The arm on the right floor
                if Current_Angle > Pill_Angle:
                # Clockwise/Counterclockwise#
                elif Current_Angle < Pill_Angle:
                # Clockwise/Counterclockwise#
                else:  # The arm at the right angle
                    Camera_Pos = 1  # Switch the camera to position 1
                    QR  # Taking a picture for QR code
                    Camera_Pos = 2  # Switch the camera to position 2
                    Pic_1  # Taking a picture of the bottom of the glass
                    Pill_Out  # Pill out
                    Pic_2  # Taking a picture of the bottom of the glass
                    if Pic_1 = Pic_2:
                        Pill_Out  # Pill out
