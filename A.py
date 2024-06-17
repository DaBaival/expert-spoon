import pyautogui
import time

# 设置鼠标需要移动到的位置坐标
x, y = 828, 648

# 将鼠标移动到指定坐标的间隔时间（秒）
num_seconds = 600

# 延迟8秒
time.sleep(8)

# 移动鼠标到指定坐标
pyautogui.moveTo(x, y, duration=num_seconds)

# 延迟3秒
time.sleep(3)

# 每隔12分钟点击一次鼠标
while True:
    time.sleep(num_seconds)
    pyautogui.click()