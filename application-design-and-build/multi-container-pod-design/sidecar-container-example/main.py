from time import sleep
import os
import pathlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def dispatch(self, event):
        path = pathlib.Path(event.src_path)
        if(path.is_file() and event.event_type == 'modified'):
            lines = path.open('r').readlines()
            print(f'Sending data for the cluster, event_type {event.event_type} - {lines[len(lines) -1]}')  

def run():
    path = os.environ.get('LOGS_PATH')
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    observer.join()

if __name__ == "__main__":
    run()