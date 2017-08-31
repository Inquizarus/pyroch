"""
The controller is responsible for sending commands to 
the specific robot which it is jacked into
"""
class Controller(object):
    
    robot = None

    def __init__(self, robot):
        self.robot = robot

    def input(self, commands):
        print "Controller: Starting execution of sequence"
        for command in commands:
            if command in ["left", "right", "l", "r"]:
                result = self.robot.turn(command)
            elif command in ["forward", "f"]:
                result = self.robot.move_forward()
            elif command in ["backwards", "b"]:
                result = self.robot.move_backwards()
            else:
                print "Command %s is not valid"%(command)
                continue
            if 'result' in locals() and result is not True:
                print "Controller: Stopping operations"
                return result
        if 'result' in locals() and result is True:
            print "Controller: Stopping operations, sequence executed successfully!"