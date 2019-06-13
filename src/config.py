#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
'''
    this is the settings for the whole project
'''


class Namer(object):
    btn_import = 'btn_import'
    btn_export = 'btn_export'
    btn_go = 'btn_go'
    btn_save_as = 'btn_save_as'
    btn_clear = 'btn_clear'
    btn_show_data = 'btn_show_data'
    btn_exit = 'btn_exit'

    spbx_ave = 'spbx_ave'
    spbx_cv = 'spbx_cv'
    spbx_cs = 'spbx_cs'
    spbx_fac = 'spbx_fac'

    chkb_extreme_flood = 'chkb_extreme_flood'

    spbx_extreme_N = 'spbx_extreme_N'
    spbx_extreme_n = 'spbx_extreme_n'
    spbx_extreme_a = 'spbx_extreme_a'
    spbx_extreme_l = 'spbx_extreme_l'
    spbx_extreme_std = 'spbx_extreme_std'

    flood_data = 'flood_data'


splitter = None  # 分隔符，用于跨平台
PLATFORM = platform.system()
if PLATFORM == 'Linux' or PLATFORM == 'OSX':
    splitter = '/'
else:
    splitter = '\\\\'
WORKSPACE = os.path.abspath('.')

SRC_DIR = os.path.join(WORKSPACE, 'src')  # 源码路径
RES_DIR = os.path.join(WORKSPACE, 'res')  # 资源文件路径
IMG_DIR = os.path.join(RES_DIR, 'img')  # 图像路径
RCC_DIR = os.path.join(RES_DIR, 'UI' + splitter + 'res.py')  # 资源索引文件路径
DOCS_DIR = os.path.join(WORKSPACE, 'docs')  # 文档路径
DATABASE = "Flood.db"  # 数据库名称

HELP_DOC_PATH = os.path.join(RES_DIR, 'others.md')  # 帮助文件路径
HELP_HTML_PATH = os.path.join(RES_DIR, 'help_document.html')

GITHUB_URL = 'https://github.com/rainyl'

# 计算参数
FLOOD_ARGS = {
        "x_rsh": [],  # 调查洪水列表
        "x_mes": [],  # 实测洪水列表
        Namer.flood_data: [],
        Namer.spbx_extreme_std: 2000,  # 大洪水标准
        Namer.spbx_extreme_N: 102,  # 总计算年
        Namer.spbx_extreme_a: 2,  # N中的特大洪水
        Namer.spbx_extreme_n: 30,  # 实测年
        Namer.spbx_extreme_l: 0,  # n中的特大洪水
        Namer.spbx_ave: 1,
        Namer.spbx_cv: 1,
        Namer.spbx_cs: 1,
        Namer.spbx_fac: 2,  # Cs = factor * Cv
    }


# 用于数据库的参数
class DB:
    DB_OPEN_ERROR = 0
    DB_EXEC_SQL_ERROR = 1
    DB_SUCCEED = 2
