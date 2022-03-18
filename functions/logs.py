import json
import sys
from datetime import datetime

# load global config
with open('./notes/config.json', 'r') as f:
    config = json.load(f)


def log_info(msg):
    date_time_now = datetime.now()
    msg = str(date_time_now) + ' - INFO - ' + msg
    print(msg, end='')
    file_log_normal = open(config["log"]["information"], 'a')
    file_log_normal.write(msg)
    file_log_normal.close()
    file_log_all = open(config["log"]["all"], 'a')
    file_log_all.write(msg)
    file_log_all.close()

def log_warn(msg):
    date_time_now = datetime.now()
    msg = str(date_time_now) + ' - WARN - ' + msg
    print(msg, end='')
    file_log_normal = open(config["log"]["warning"], 'a')
    file_log_normal.write(msg)
    file_log_normal.close()
    file_log_all = open(config["log"]["all"], 'a')
    file_log_all.write(msg)
    file_log_all.close()


def log_error(msg):
    date_time_now = datetime.now()
    msg = str(date_time_now) + ' - ERROR - ' + msg
    print(msg, end='')
    file_log_normal = open(config["log"]["error"], 'a')
    file_log_normal.write(msg)
    file_log_normal.close()
    file_log_all = open(config["log"]["all"], 'a')
    file_log_all.write(msg)
    file_log_all.close()
