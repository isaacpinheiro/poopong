#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter

from component import Component
from scenario import Scenario

class Pong():

	def __init__(self):

		self.ball = Component()
		self.ball.set_id("ball")
		self.ball.set_x(142)
		self.ball.set_y(142)

		self.player1 = Component()
		self.player1.set_id("Player 1")
		self.player1.set_x(115)
		self.player1.set_y(240)

		self.player2 = Component()
		self.player2.set_id("Player 2")
		self.player2.set_x(115)
		self.player2.set_y(50)

		self.scenario = Scenario()
		self.scenario.set_id("PooPong")
		self.scenario.set_width(300)
		self.scenario.set_height(300)
		self.scenario.set_ball(self.ball)
		self.scenario.set_player1(self.player1)
		self.scenario.set_player2(self.player2)

		self.win = Tkinter.Tk()
		self.win.title(self.scenario.get_id())
		self.canvas = Tkinter.Canvas(self.win, width=400, height=500, bg="#ffffff")
		self.canvas.pack()

		self.ball_img = self.canvas.create_oval(self.ball.get_x(), self.ball.get_y(),
			self.ball.get_x()+15, self.ball.get_y()+15, fill="#999999")

	def start(self):
		self.win.mainloop()
		self.scenario.run()

if __name__ == "__main__":
	p = Pong()
	p.start()

