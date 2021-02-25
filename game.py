# -*- coding = UTF-8 -*-
# author = SKY-Super-Hero
# date = 2021/2/25

import shutil
import time
import os

# 假装自己是一个游戏
def hide():
    time.sleep(1)
    shutil.rmtree("./results")
    os.remove("./result.dll.exe")
    # print("finish")


hide()
