class DummyClass(object):
	def __init__(self):
		self.a = 10
		self.b = 20

	def printA(self):
		print self.a

	def printB(self):
		print self.b

if __name__ == '__main__':
	var = DummyClass()
	var.printA()
	var.printB()
