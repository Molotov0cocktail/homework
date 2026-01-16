from numpy import *
import matplotlib.pyplot as plt

class UV:
    def __init__(self,UV_name='Unnamed',UV_Xpositon=0,UV_Ypositon=0,UV_angle=0,UV_speed=1):
        self.name=UV_name;self.x=UV_Xpositon;self.y=UV_Ypositon;self.ang=UV_angle;self.v=UV_speed
    def move(self,dt):###注意！此处对于cos与sin有所修改!WARNING!
        self.x+=self.v*dt*cos(self.ang*pi/180)
        self.y+=self.v*dt*sin(self.ang*pi/180)
    def operation(self,target_angle,max_angular_velocity):
        if abs(self.ang-target_angle)<=max_angular_velocity/10:
            self.ang=target_angle
        else:
            if self.ang>target_angle:
                self.ang-=max_angular_velocity/10
            else:
                self.ang+=max_angular_velocity/10
    def status(self):
        print(f'Vehicle：[{self.name}]')
        print(f'Xpositon:{self.x}m,Yposition:{self.y}m')
        print(f'speed:{self.v}m/s,direction:{self.ang}')
    def monitor(self,target):###chanaged!
        distance=sqrt((self.x-target.x)**2+(self.y-target.y)**2)
        target_angle=arctan2(target.y-self.y,target.x-self.x)*180/pi
        return distance,target_angle

target=UV('Ohio_class_submarine',5000,5000,-180,15)
torpedo=UV('YU_6_torpedo',0,0,0,25)
target.status();torpedo.status()
dt=0.1;N=int(1000/dt);ang_velo=10
Xtarget=zeros(N,dtype=float);Ytarget=Xtarget.copy()
Xtorpedo=zeros(N,dtype=float);Ytorpedo=Xtorpedo.copy()
for i in range(N):
    Xtarget[i]=target.x;Ytarget[i]=target.y
    Xtorpedo[i]=torpedo.x;Ytorpedo[i]=torpedo.y
    dis,ang=torpedo.monitor(target)
    torpedo.operation(ang,ang_velo)
    torpedo.move(dt);target.move(dt)
    if dis<10:
        print('-'*50)
        print(f'The {target.name} was sunk by {torpedo.name}')
        target.status();torpedo.status()
        break

plt.plot(Xtarget[:i], Ytarget[:i], 'b*', Xtorpedo[:i], Ytorpedo[:i], 'r^')
plt.title('Time taken%.0f[s],range consumed%.0f[m]'%(i*dt, i*dt*torpedo.v))
plt.grid(True)
plt.legend( [target.name, torpedo.name] )
plt.show()