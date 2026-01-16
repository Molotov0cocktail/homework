from numpy import *
class UV:
    def __init__(self,UV_name='Unnamed',UV_Xpositon=0,UV_Ypositon=0,UV_angle=0,UV_speed=1):
        self.name=UV_name;self.x=UV_Xpositon;self.y=UV_Ypositon;self.ang=UV_angle;self.v=UV_speed
    def move(self,dt):###注意！此处对于cos与sin有所修改!WARNING!
        self.x+=self.v*dt*cos(self.ang*pi/180)
        self.y+=self.v*dt*sin(self.ang*pi/180)
    def operation(self,target_angle):
        self.ang=target_angle
    def status(self):
        print(f'Vehicle：{self.name}')
        print(f'Xpositon:{self.x}m,Yposition:{self.y}m')
        print(f'speed:{self.v}m/s,direction:{self.ang}')
    def monitor(self,target):###chanaged!
        distance=sqrt((self.x-target.x)**2+(self.y+target.y)**2)
        target_angle=arctan2(target.y-self.y,target.x-self.x)*180/pi
        return distance,target_angle


