import threading
from dobot_api import DobotApiDashboard, DobotApi, DobotApiMove, MyType
from time import sleep
import numpy as np
from dobot_main import GetFeed, ClearRobotError

##  Connecting to robot arm
#
PARAMS = 0
def connect_robot():
    try:
        ip = "192.168.1.6"
        dashboard_p = 29999
        move_p = 30003
        feed_p = 30004
        print("Establishing connection...")
        dashboard = DobotApiDashboard(ip, dashboard_p)
        move = DobotApiMove(ip, move_p)
        feed = DobotApi(ip, feed_p)
        print(">.< Connection successful >!<")
        return dashboard, move, feed
    except Exception as e:
        print(":( Connection failed :(")
        raise e
    
## Running script
#
if __name__ == '__main__':

    dashboard, move, feed = connect_robot()

    """
        if PARAMS  Conditional compilation directive has parameters
            0:  Instruction without parameters
            1:  Instruction with parameters
    """
    dashboard.DisableRobot()