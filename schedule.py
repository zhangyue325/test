import pandas as pd
import datetime

with open("schedule.txt", "a") as f:
    f.write(str(datetime.datetime.now()))