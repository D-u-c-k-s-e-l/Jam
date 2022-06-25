import pygame as pyg
import asyncio as aio
from collections import deque
from json import *
from resources.DataTypes import Matrix

def getQuitClicked(invertResult: bool = False) -> bool:
    """checks if the 'X' button was clicked"""
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            if invertResult:
                return False
            return True
    if invertResult:
        return True
    return False

def QueryKey(value: str) -> (bool, None):
	return pyg.key.get_pressed()[ord(value[0].lower())]

class DebuggingPanel:

	def __init__(self):
		self.debugData = []

	def AddDebugEntry(self, title: str, data):
		self.debugData.append((title, data))

	def update(self):
		dat = []
		for data in self.debugData:
			dat.append(f"{data[0]} : {data[1]()}")

		print("\n"*50 + "\n".join(dat))

class GameEngine:

	def __init__(self, windowSize: tuple = (800, 600)):
		pyg.init()

		self.clock = pyg.time.Clock()

		self.Screen = pyg.display.set_mode(windowSize)
		self.__trackedKeys = None

	def Launch(self):
		running = True

		while running:
			running = getQuitClicked(True)
			self.clock.tick()
			pyg.display.update()
			pyg.event.get()
			#print(self.clock)

		
			
"""
Engine = GameEngine()
Engine.Launch()
"""

m1 = Matrix(3, 3)
m1.fillWith(12)
m2 = Matrix(3, 3)
m2.fillWith(10)

print(m1 / m2)