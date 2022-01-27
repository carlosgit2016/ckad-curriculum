import os
import pathlib
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def dispatch(self, event):
        path = pathlib.Path(event.src_path)
        if(path.is_file() and event.event_type == 'modified'):
            lines = path.open('r').readlines()
            print(f'Normalizaing data: [EVENT_NORMILIZED] {event.event_type} - {lines[len(lines) -1]}')  

def watch(*args):
    for a in args:
        observe(a)

def observe(path):
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    # observer.join()

def run():
    path1 = os.environ.get('LOGS_PATH1')
    path2 = os.environ.get('LOGS_PATH2')
    watch(path1, path2)
    # Exists for 1 hour to do not stop the container
    sleep(3600)

if __name__ == "__main__":
    run()