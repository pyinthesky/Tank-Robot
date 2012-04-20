
class MotorShield(object):
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
class Servo(MotorShield):
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass

class Motor(MotorShield):

    def __init__(self, wheel_radius_cm = 0.1):
        self.decoder_value  = 0
        self.ang_velocity   = 0
        self.lin_velocity   = 0
        self.pwm            = 0
        self.radius         = wheel_radius_cm
    
    def __str__(self):
        pass
    
class Stepper(Motor):

    def __init__(self):
        pass
    
    def __str__(self):
        pass

class PositionRecorder(object):
    
    def __init__(self, orig_x, orig_y):
        self.pos    = OrderedDict()
        self.orig_x = orig_x
        self.orig_y = orig_y
    
    def set_pos(self, x_pos, y_pos)
        self.pos[time.time()] = (x_pos - self.orig_x, y_pos - self.orig_y)
    
    def write_pos(self)
    
    def write_record_to_file(self, fname):
        with open(fname, 'w') as f:
            f.write(pprint.pformat(self.pos))
    
class TankMotor(object):
    
    def __init__(self):
        self.lhs_motor  = Stepper()
        self.rhs_motor  = Stepper()
        
    
    def __str__(self):
        return '\n'.join([
                            "LHS Motor",
                            "----------------------------",
                            str(self.lhs_motor),
                            "",
                            "RHS Motor",
                            "----------------------------",
                            str(self.rhs_motor),
                            "",
                            "center distance traveled",
                            "average velocity",
                            "up time",
                            "travel time",
                        ])
    
    def rh_turn(self, deg, turn_radius):
        pass
    
    def lh_turn(self, deg, turn_radius):
        pass
    
