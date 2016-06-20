#!/usr/bin/python

class Scenario:

	def __init__(self):
		self.__id = None
		self.__width = None
		self.__height = None
		self.__ball = None
		self.__player1 = None
		self.__player2 = None

	def set_id(self, id):
		self.__id = id

	def get_id(self):
		return self.__id

	def set_width(self, width):
		self.__width = width

	def get_width(self):
		return self.__width

	def set_height(self, height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_ball(self, ball):
		self.__ball = ball

	def get_ball(self):
		return self.__ball

	def set_player1(self, player1):
		self.__player1 = player1

	def get_player1(self):
		return self.__player1

	def set_player2(self, player2):
		self.__player2 = player2

	def get_player2(self):
		return self.__player2

	def run(self):
		# TODO
		pass

	def __del__(self):
		self.__id = None
		self.__width = None
		self.__height = None
		self.__ball = None
		self.__player1 = None
		self.__player2 = None

