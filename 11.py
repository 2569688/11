import time

def concentration_timer(minutes):
    seconds = minutes * 60
    print(f"专注倒计时开始，时长为 {minutes} 分钟。\n")
    time.sleep(seconds)
    print("专注时间结束！")

# 设置专注时长为 25 分钟
concentration_timer(25)
