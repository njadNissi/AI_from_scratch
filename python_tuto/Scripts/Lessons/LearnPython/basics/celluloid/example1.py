#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera


class Vehicle:
    def __init__(self,
                 x=0.0,
                 y=0.0,
                 yaw=0.0,
                 v=0.0,
                 dt=0.1,
                 l=3.0):
        self.steer = 0
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.dt = dt
        self.L = l  # 轴距
        self.x_front = x + l * math.cos(yaw)
        self.y_front = y + l * math.sin(yaw)

    def update(self, a, delta, max_steer=np.pi):
        delta = np.clip(delta, -max_steer, max_steer)
        self.steer = delta

        self.x = self.x + self.v * math.cos(self.yaw) * self.dt
        self.y = self.y + self.v * math.sin(self.yaw) * self.dt
        self.yaw = self.yaw + self.v / self.L * math.tan(delta) * self.dt

        self.v = self.v + a * self.dt
        self.x_front = self.x + self.L * math.cos(self.yaw)
        self.y_front = self.y + self.L * math.sin(self.yaw)


class VehicleInfo:
    # Vehicle parameter
    L = 3.0  #轴距
    W = 2.0  #宽度
    LF = 3.8  #后轴中心到车头距离
    LB = 0.8  #后轴中心到车尾距离
    MAX_STEER = 0.6  # 最大前轮转角
    TR = 0.5  # 轮子半径
    TW = 0.5  # 轮子宽度
    WD = W  #轮距
    LENGTH = LB + LF  # 车辆长度

def draw_trailer(x, y, yaw, steer, ax, vehicle_info=VehicleInfo, color='black'):
    vehicle_outline = np.array(
        [[-vehicle_info.LB, vehicle_info.LF, vehicle_info.LF, -vehicle_info.LB, -vehicle_info.LB],
         [vehicle_info.W / 2, vehicle_info.W / 2, -vehicle_info.W / 2, -vehicle_info.W / 2, vehicle_info.W / 2]])

    wheel = np.array([[-vehicle_info.TR, vehicle_info.TR, vehicle_info.TR, -vehicle_info.TR, -vehicle_info.TR],
                      [vehicle_info.TW / 2, vehicle_info.TW / 2, -vehicle_info.TW / 2, -vehicle_info.TW / 2, vehicle_info.TW / 2]])

    rr_wheel = wheel.copy() #右后轮
    rl_wheel = wheel.copy() #左后轮
    fr_wheel = wheel.copy() #右前轮
    fl_wheel = wheel.copy() #左前轮
    rr_wheel[1,:] += vehicle_info.WD/2
    rl_wheel[1,:] -= vehicle_info.WD/2

    #方向盘旋转
    rot1 = np.array([[np.cos(steer), -np.sin(steer)],
                     [np.sin(steer), np.cos(steer)]])
    #yaw旋转矩阵
    rot2 = np.array([[np.cos(yaw), -np.sin(yaw)],
                     [np.sin(yaw), np.cos(yaw)]])
    fr_wheel = np.dot(rot1, fr_wheel)
    fl_wheel = np.dot(rot1, fl_wheel)
    fr_wheel += np.array([[vehicle_info.L], [-vehicle_info.WD / 2]])
    fl_wheel += np.array([[vehicle_info.L], [vehicle_info.WD / 2]])

    fr_wheel = np.dot(rot2, fr_wheel)
    fr_wheel[0, :] += x
    fr_wheel[1, :] += y
    fl_wheel = np.dot(rot2, fl_wheel)
    fl_wheel[0, :] += x
    fl_wheel[1, :] += y
    rr_wheel = np.dot(rot2, rr_wheel)
    rr_wheel[0, :] += x
    rr_wheel[1, :] += y
    rl_wheel = np.dot(rot2, rl_wheel)
    rl_wheel[0, :] += x
    rl_wheel[1, :] += y
    vehicle_outline = np.dot(rot2, vehicle_outline)
    vehicle_outline[0, :] += x
    vehicle_outline[1, :] += y

    ax.plot(fr_wheel[0, :], fr_wheel[1, :], color)
    ax.plot(rr_wheel[0, :], rr_wheel[1, :], color)
    ax.plot(fl_wheel[0, :], fl_wheel[1, :], color)
    ax.plot(rl_wheel[0, :], rl_wheel[1, :], color)

    ax.plot(vehicle_outline[0, :], vehicle_outline[1, :], color)
    # ax.axis('equal')



if __name__ == "__main__":

    vehicle = Vehicle(x=0.0,
                      y=0.0,
                      yaw=0,
                      v=0.0,
                      dt=0.1,
                      l=VehicleInfo.L)
    vehicle.v = 3
    trajectory_x = []
    trajectory_y = []
    fig = plt.figure()
    # 保存动图用
    # camera = Camera(fig)
    for i in range(600):
        plt.cla()
        plt.gca().set_aspect('equal', adjustable='box')
        vehicle.update(0, np.pi / 10)
        draw_trailer(vehicle.x, vehicle.y, vehicle.yaw, vehicle.steer, plt)
        trajectory_x.append(vehicle.x)
        trajectory_y.append(vehicle.y)
        plt.plot(trajectory_x, trajectory_y, 'blue')
        plt.xlim(-12, 12)
        plt.ylim(-2.5, 21)
        plt.pause(0.001)
    #     camera.snap()
    # animation = camera.animate(interval=5)
    # animation.save('trajectory.gif')