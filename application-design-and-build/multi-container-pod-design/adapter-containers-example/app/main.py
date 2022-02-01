from datetime import datetime
from time import sleep
from os import environ
from pathlib import Path

def run():
    while True:
        logs_path = environ.get('LOGS_PATH')
        log_file_name = environ.get('LOG_FILE_NAME')
        logs_prefix = environ.get('LOGS_PREFIX')
        now = datetime.now()
        file_log_path = f'{logs_path}/{log_file_name}'
        create_if_not_exists(file_log_path)
        append_new_line(file_log_path, f'{logs_prefix} {now.strftime("%Y-%m-%d %H:%M:%S")}')
        sleep(5)

def create_if_not_exists(file):
    file_path = Path(file)
    if (not file_path.exists()):
        file_path.touch()

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