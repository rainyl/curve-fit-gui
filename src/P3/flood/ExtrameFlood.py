#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 水文频率曲线拟合
# 计算部分
import numpy as np
import src.P3.Heisen.Heisen as heisen
from src.P3.flood.Flood import Flood


class ExtremeFlood(Flood):
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
    def __init__(self, x_std=None):
        super().__init__(x_std)

    # 初始化参数
    def initArgs(self, args):
        self.x_rsh = args['x_rsh']
        self.x_mes = args['x_mes']
        self.std = args['std']
        self.N = args['N']
        self.a = args['a']
        self.n = args['n']
        self.l = args['l']
        self.fac = args['fac']

        self.N_a, self.n_l = self.na_nl()
        self.ave = self.x_ave()
        self.Cv = self.cv()
        self.Cs = self.cs()

        self.q_ori = []  # 原始点
        self.make_q_ori()

        self.return_data = {}
        self.return_data['ave'] = self.ave
        self.return_data['Cv'] = self.Cv
        self.return_data['Cs'] = self.Cs
        self.return_data['fac'] = self.fac

        return self.return_data

    # 刷新参数
    def refreshArgs(self, args):
        self.PM_ = self.PM()  # 特大洪水概率
        self.Pm_ = self.Pm()  # 非特大洪水概率
        self.alpha = self.alp()  #
        self.ave = args['ave']
        self.Cv = args['Cv']
        self.fac = args['fac']
        self.Cs = self.cs()

        self.return_data['ave'] = self.ave
        self.return_data['Cv'] = self.Cv
        self.return_data['Cs'] = self.Cs
        self.return_data['fac'] = self.fac

    # 构造原始数据集合并排序
    def make_q_ori(self):
        self.q_ori.extend(self.x_rsh)
        self.q_ori.extend(self.x_mes)
        self.q_ori.sort()

    def x_ave(self):
        ave = 1 / self.N * (self.N_a.sum() + (self.N - len(self.N_a)) / (len(self.n_l)) * self.n_l.sum())
        return round(ave, 2)

    def na_nl(self):
        N_a, n_l = [], []
        for x in self.x_rsh:
            if x > self.std:
                N_a.append(x)
        for x in self.x_mes:
            if x < self.std:
                n_l.append(x)
        N_a, n_l = np.array(N_a), np.array(n_l)
        return N_a, n_l

    # 计算Cv
    def cv(self):
        first = np.array([(x - self.ave) ** 2 for x in self.N_a]).sum()
        second = np.array([(x - self.ave) ** 2 for x in self.n_l]).sum()
        Cv = (1 / self.ave) * np.sqrt((1 / (self.N - 1)) * (first + ((self.N - len(self.N_a)) / len(self.n_l)) * second))
        return round(Cv, 2)

    # 特大洪水频率计算
    def PM(self):
        pm = [m / (self.N + 1) for m in range(1, len(self.x_rsh) + 1)]
        return pm

    # 一般洪水频率计算
    def Pm(self):
        pm = [self.PM_[-1] + (1 - self.PM_[-1]) * ((m - self.l) / (self.n - self.l + 1)) for m in range(self.l + 1, self.n + 1)]
        return pm

    # 刷新界面
    def refresh(self, args):
        self.refreshArgs(args)
        self.go()
        return self.return_data

    # 计算流程
    def go(self):
        p_all = []  # 总概率序列
        p_all.extend(self.PM_)
        p_all.extend(self.Pm_)

        tmp = [0.005, ]
        tmp.extend(p_all)
        p_x = heisen.normal(tmp)  # x轴概率对应正态化后的值

        x = [x_ * 100 for x_ in tmp]
        y = self.xp(x=x)  # 计算对应Y值

        self.return_data['x'] = p_x
        self.return_data['y'] = y
