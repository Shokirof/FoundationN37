import os
import datetime as dt
def show_time():
    hozir= dt.datetime.now()
    print(hozir.time())
if __name__ =="__main__":
    show_time()