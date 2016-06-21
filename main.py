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
		self.canvas = Tkinter.Canvas(self.win, width=self.scenario.get_width(), height=self.scenario.get_width(), bg="#ffffff")
		self.canvas.pack()

		self.ball_img = self.canvas.create_oval(self.ball.get_x(), self.ball.get_y(),
			self.ball.get_x()+15, self.ball.get_y()+15, fill="#999999")

		self.player1_img = self.canvas.create_rectangle(self.player1.get_x(), self.player1.get_y(),
			self.player1.get_x()+70, self.player1.get_y()+10, fill="#006699")

		self.player2_img = self.canvas.create_rectangle(self.player2.get_x(), self.player2.get_y(),
			self.player2.get_x()+70, self.player2.get_y()+10, fill="#006699")

		self.canvas.bind("<Key>", self.move_players)
		self.canvas.focus_set()

		self.frame = Tkinter.Frame(self.win, width=300, height=120)
		self.frame.pack(side="bottom")

		self.lable1= Tkinter.Label(self.frame, text="Player 1 - A: Left / D: Right")
		self.lable1.pack()

		self.lable2= Tkinter.Label(self.frame, text="Player 2 - H: Left / K: Right")
		self.lable2.pack()

	def move_players(self, event):

		if event.char == 'A' or event.char == 'a':
			print "Player 1 para esquerda"
		elif event.char == 'D' or event.char == 'd':
			print "Player 1 para direita"

		if event.char == 'H' or event.char == 'h':
			print "Player 2 para esquerda"
		elif event.char == 'K' or event.char == 'k':
			print "Player 2 para direita"

	def start(self):
		self.win.mainloop()
		self.scenario.run()

if __name__ == "__main__":
	p = Pong()
	p.start()

