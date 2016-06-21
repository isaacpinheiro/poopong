#!/usr/bin/python

from random import randrange
import time

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

	def run(self, ball_img, canvas):

		if randrange(0, 2) == 1:
			vertical = True
		else:
			vertical = False

		if randrange(0, 2) == 1:
			horizontal = True
		else:
			horizontal = False

		while True:

			if self.__ball.get_y() > 0 and self.__ball.get_y() < 284:

				if vertical == True:

					self.__ball.set_y(self.__ball.get_y() + 2)

					canvas.update()
					canvas.delete(ball_img)
					ball_img = canvas.create_oval(self.__ball.get_x(), self.__ball.get_y(),
						self.__ball.get_x()+15, self.__ball.get_y()+15, fill="#999999")

					if self.__ball.get_y() == 224 and ((self.__ball.get_x() + 15) >= self.__player1.get_x() and
						self.__ball.get_x() <= (self.__player1.get_x() + 69)):

						vertical = False

				else:

					self.__ball.set_y(self.__ball.get_y() - 2)

					canvas.update()
					canvas.delete(ball_img)
					ball_img = canvas.create_oval(self.__ball.get_x(), self.__ball.get_y(),
						self.__ball.get_x()+15, self.__ball.get_y()+15, fill="#999999")

					if self.__ball.get_y() == 62 and ((self.__ball.get_x() + 15) >= self.__player2.get_x() and
						self.__ball.get_x() <= (self.__player2.get_x() + 69)):

						vertical = True

				if horizontal == True:

					self.__ball.set_x(self.__ball.get_x() + 2)

					canvas.update()
					canvas.delete(ball_img)
					ball_img = canvas.create_oval(self.__ball.get_x(), self.__ball.get_y(),
						self.__ball.get_x()+15, self.__ball.get_y()+15, fill="#999999")

					if self.__ball.get_x() == 284:
						horizontal = False

				else:

					self.__ball.set_x(self.__ball.get_x() - 2)

					canvas.update()
					canvas.delete(ball_img)
					ball_img = canvas.create_oval(self.__ball.get_x(), self.__ball.get_y(),
						self.__ball.get_x()+15, self.__ball.get_y()+15, fill="#999999")

					if self.__ball.get_x() == 0:
						horizontal = True

			else:
				break

			time.sleep(.07)

	def __del__(self):
		self.__id = None
		self.__width = None
		self.__height = None
		self.__ball = None
		self.__player1 = None
		self.__player2 = None

