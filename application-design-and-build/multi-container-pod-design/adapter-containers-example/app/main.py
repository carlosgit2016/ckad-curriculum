from datetime import datetime
from time import sleep
from os import environ

def run():
    while True:
        logs_path = environ.get('LOGS_PATH')
        logs_prefix = environ.get('LOGS_PREFIX')
        now = datetime.now()
        append_new_line(logs_path, f'{logs_prefix} {now.strftime("%Y-%m-%d %H:%M:%S")}')
        sleep(5)

def append_new_line(file, str):
    '''
        Append a new line to a file, if the file is not empty, append a new line before
    '''
    with open(file, 'a+') as appender:
        appender.seek(0)
        if len(appender.read(100)) > 0:
            appender.write("\n")
        appender.write(str)


if __name__ == "__main__":
    run()