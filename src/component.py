#!/usr/bin/python

class Component:

    def __init__(self):
        self.__id = None
        self.__x = None
        self.__y = None

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y

    def __del__(self):
        self.__id = None
        self.__x = None
        self.__y = None

