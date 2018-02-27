# -*- coding: UTF-8 -*-
import os


def dirs_list():
    for root, dirs, files in os.walk('F:\\baidu'):
        for name in files:
            print(os.path.join(root, name))


if __name__ == '__main__':
    dirs_list()
