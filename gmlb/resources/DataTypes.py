import pygame as pyg


class Matrix:

	def __init__(self, x: int, y: int):
		self.x, self.y = x, y #decompress size
		self.matrix = [
			[None for _ in range(x)]#fill the rows with None
			for _ in range(y)#put multiple rows together
		]

	def merge(self, matrix):
		"""
		merges two Matrices
		"""
		for coords, matrixData in matrix:
			if matrixData != None:
				continue

			x,y = coords
			matrix[x, y] = self[x, y]
		
	def fillWith(self, value):
		for coords, _ in self:
			x,y = coords
			self[x, y] = value

	def __str__(self):
		return str(self.matrix)
					

	def __add__(self, value):

		out = Matrix(self.x, self.y)

		if isinstance(value, Matrix):
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] + value[x, y]

		else:
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] + value

		return out

	def __sub__(self, value):
		
		out = Matrix(self.x, self.y)

		if isinstance(value, Matrix):
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] - value[x, y]

		else:
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] - value

		return out

	def __mul__(self, value):
		out = Matrix(self.x, self.y)

		if isinstance(value, Matrix):
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] * value[x, y]

		else:
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] * value

		return out

	def __truediv__(self, value):
		out = Matrix(self.x, self.y)

		if isinstance(value, Matrix):
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] / value[x, y]

		else:
			for coord, _ in out:
				x,y = coord
				out[x, y] = self[x, y] / value

		return out

	def __getitem__(self, coords):
		return self.matrix[coords[1]][coords[0]]
		
	def __setitem__(self, coords, value):
		self.matrix[coords[1]][coords[0]] = value

	def __iter__(self):#iterate
		for y, row in enumerate(self.matrix):
			for x, column in enumerate(row):
				yield ((x, y), column)


class AnimatedObject:
	def __init__(self, pos: tuple):
		"""
		An AnimatedObject is an object that simplifies the
		animation process by storing all frames in a list
		and also handles the states of an animation
		"""
		
		self.x,self.y=pos #Decompresses position variable of clarity
		self.pos=pos #Adds the position tuple to the class
		self.animState = 0 #For tracking the current frame in a animation
		self.animStates = ["NUL"]
		self.anims = [
			[]
		]
	def addAnimationState(self, animationStateName: str, animation: list):
		"""
		Adds a new animation to the animation list
		"""
		self.animations.append(animation)
		self.animationStates.append(animationStateName)
	def setAnimationState(self, state: int):
		if type(state) == int:
			self.animationState