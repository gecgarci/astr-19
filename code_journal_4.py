class Giraffe:
	name = ""
	def __init__(self,name):
		self.name = name
Giraffe.legs = 6.0
Giraffe.eyes = 2
print(bool("A giraffe has a tail"))
print(bool("A giraffe is considered to be furry"))
print(f"Length of a giraffe's legs: {Giraffe.legs}ft , number of eyes a giraffe has: {Giraffe.eyes}")
