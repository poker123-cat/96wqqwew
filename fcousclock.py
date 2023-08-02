import time

def countdown(timer):
    while timer:
        mins, secs = divmod(timer, 60)
        timer_format = "{:02d}:{:02d}".format(mins, secs)
        print(timer_format, end="\r")
        time.sleep(1)
        timer -= 1
    
    print("时间到!")

# 设置专注时长，以秒为单位
focus_time = 25 * 60

print("专注时钟开始！")
countdown(focus_time)
