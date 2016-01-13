class Point():
	def setdata(self,x,y,d):
		self.x=x
		self.y=y
		self.d=d
	def setx(self):
		result = self.x
		return result
	def sety(self):
		result = self.y
		return result
	def get(self):
		result=(self.x,self,y)
		return result
	def move(self):
		result=(self.x+self.d,self.y+self.d)
		return result