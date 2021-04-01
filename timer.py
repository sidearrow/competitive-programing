from time import time


class Timer:
    def __init__(self):
        self.__start_time = None
        self.__stop_time = None

    @property
    def __elapsed_time(self):
        return self.__stop_time - self.__start_time

    @staticmethod
    def __print(val):
        print("{:.5f}[sec]".format(val))

    def start(self):
        self.__start_time = time()

    def stop(self):
        self.__stop_time = time()
        self.__print(self.__elapsed_time)

    def reset(self):
        self.__start_time = None
        self.__stop_time = None
