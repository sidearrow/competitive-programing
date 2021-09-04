from datetime import datetime


class Timer:
    def __init__(self) -> None:
        self.__start_time = -1

    def start(self):
        self.__start_time = datetime.now().timestamp()

    def stop(self):
        stop_time = datetime.now().timestamp()