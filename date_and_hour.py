import time


def formate_date_and_hour():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
