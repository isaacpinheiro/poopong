#!/usr/bin/python

import unittest

from component import Component
from scenario import Scenario

class TestComponent(unittest.TestCase):

    def setUp(self):
        self.ball = Component()

    def test_component(self):
        self.ball.set_id("ball")
        self.ball.set_x(50)
        self.ball.set_y(50)
        self.assertEqual(self.ball.get_id(), "ball")
        self.assertEqual(self.ball.get_x(), 50)
        self.assertEqual(self.ball.get_y(), 50)

class TestScenario(unittest.TestCase):

    def setUp(self):
        self.scenario = Scenario()
        self.ball = Component()
        self.player1 = Component()
        self.player2 = Component()

    def test_scenario(self):

        self.ball.set_id("ball")
        self.ball.set_x(50)
        self.ball.set_y(50)

        self.player1.set_id("Player 1")
        self.player1.set_x(40)
        self.player1.set_y(40)

        self.player2.set_id("Player 2")
        self.player2.set_x(60)
        self.player2.set_y(60)

        self.scenario.set_id("pong")
        self.scenario.set_width(300)
        self.scenario.set_height(300)
        self.scenario.set_ball(self.ball)
        self.scenario.set_player1(self.player1)
        self.scenario.set_player2(self.player2)

        self.assertEqual(self.scenario.get_id(), "pong")
        self.assertEqual(self.scenario.get_width(), 300)
        self.assertEqual(self.scenario.get_height(), 300)
        self.assertEqual(self.scenario.get_ball().get_id(), "ball")
        self.assertEqual(self.scenario.get_ball().get_x(), 50)
        self.assertEqual(self.scenario.get_ball().get_y(), 50)
        self.assertEqual(self.scenario.get_player1().get_id(), "Player 1")
        self.assertEqual(self.scenario.get_player1().get_x(), 40)
        self.assertEqual(self.scenario.get_player1().get_y(), 40)
        self.assertEqual(self.scenario.get_player2().get_id(), "Player 2")
        self.assertEqual(self.scenario.get_player2().get_x(), 60)
        self.assertEqual(self.scenario.get_player2().get_y(), 60)

if __name__ == "__main__":
    unittest.main()

