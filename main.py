import pyautogui
import math
import time

# 円の中心座標と半径を設定
center_x, center_y = 480, 540  # 円の中心（画面の座標）
radius = 120  # 半径
steps = 50  # 円を描くためのステップ数（精度）

# 円を描く
pyautogui.moveTo(center_x + radius, center_y)  # 初期位置に移動
time.sleep(1)  # ゲームが準備できるように待機
pyautogui.mouseDown()

for i in range(steps):
    angle = math.radians(i/steps*360)  # 角度をラジアンに変換
    x = center_x + radius * math.cos(angle)  # X座標
    y = center_y + radius * math.sin(angle)  # Y座標
    pyautogui.moveTo(x, y)  # 指定した座標にマウスを動かす
    
pyautogui.mouseUp()