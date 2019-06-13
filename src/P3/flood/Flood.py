#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 水文频率曲线拟合
# 计算部分
import numpy as np
from scipy.special import gammaincinv
import src.P3.Heisen.Heisen as hs
from src.config import Namer


class Flood(object):
    # 接收参数字典，示例：
    # args = {
    #     x_rsh: [],      # 调查洪水列表
    #     x_mes: [],      # 实测洪水列表
    #     std: int(),     # 大洪水标准
    #     N: int(),       # 总计算年
    #     a: int(),       # N中的特大洪水
    #     n: int(),       # 实测年
    #     l: int(),       # n中的特大洪水
    #     fac: int(),  # Cs = fac * Cv
    # }
    def __init__(self, args, x_std=None):
        if x_std is None:
            self.x_std = hs.x_std
        self.x, self.y = None, None
        self.x_ori, self.y_ori = None, None
        self.ave, self.Cv, self.Cs = None, None, None
        self.fac = 2
        self.p = None
        self.alpha = None
        self.initArgs(args)

    # 初始化参数
    # data 是流量数据，接受list或者array
    def initArgs(self, args):
        self.data = args[Namer.flood_data]
        self.n = len(self.data)

        self.ave = self.x_ave()
        self.Cv = self.cv()
        self.Cs = self.cs()

    # 刷新参数
    def refreshArgs(self, args):
        self.p = self.P()  # 洪水概率
        self.alpha = self.alp()  #
        self.ave = args[Namer.spbx_ave]
        self.Cv = args[Namer.spbx_cv]
        self.fac = args[Namer.spbx_fac]
        self.Cs = self.cs()

    def x_ave(self):
        ave = np.array(self.data).sum()/len(self.data)
        return round(ave, 2)

    # 计算Cv
    def cv(self):
        Ki = [x/self.ave for x in self.data]  # 模比系数
        up = np.array([(ki-1)**2 for ki in Ki]).sum()
        down = len(self.data) - 1
        Cv = np.sqrt(up/down)
        return round(Cv, 2)

    # 计算Cs
    def cs(self):
        Cs = self.Cv * self.fac
        return round(Cs, 2)

    # 洪水频率计算
    def P(self):
        self.data.sort()  # 排序
        n = len(self.data)
        pm = [m/(n+1) for m in range(1, n+1)]
        return pm

    def alp(self):
        alpha = 4 / (self.Cv * self.fac) ** 2
        return alpha

    # 计算中间量 逆函数，计算参考 《水文频率曲线简捷计算和绘图技巧》，林莺，李世才，广西壮族自治区南宁水利电力设计院，2002
    def tp(self, x=None):
        if x is None:
            x = self.x_std
            x = [1 - x_ / 100 for x_ in x]
        xx = [1 - x_ / 100 for x_ in x]
        tp_ = [gammaincinv(self.alpha, p) for p in xx]
        return tp_

    def xp(self, x=None):
        ac_ = [0.5 * self.Cs * t - 2 / self.Cs for t in self.tp(x)]
        xp_ = [self.ave * (self.Cv * ac_ + 1) for ac_ in ac_]
        return xp_

    # 刷新界面
    def refresh(self, args):
        self.refreshArgs(args)
        self.go()

    # 计算流程
    def go(self):
        self.x_ori = hs.normal(self.p)  # x轴概率对应正态化后的值
        x = [x_ * 100 for x_ in self.p]
        self.y_ori = self.xp(x=x)  # 计算对应Y值

        self.x = hs.normal([i/100 for i in self.x_std])  # x轴概率对应正态化后的值
        x = [x_ * 100 for x_ in self.x_std]
        self.y = self.xp(x=self.x_std)  # 计算对应Y值
