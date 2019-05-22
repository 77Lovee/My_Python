#coding: UTF-8
import re
import string
class Calc:
	Operators=[]
	OptExpression=[]
	Operand1=[]
	Operand2=[]
	calcTimes=0
	def getInput(self):
		self.calcTimes=eval(input())
		for i in range(self.calcTimes):
			self.OptExpression.append(input())
	
	def AnyliseExp(self):
		for exp in self.OptExpression:
			if '*' in exp:
				pieces=exp.split('*')
				self.Operators.append('*')
			elif '+' in exp:
				pieces=exp.split('+')
				self.Operators.append('+')
			elif '-' in exp:
				pieces=exp.split('-')
				self.Operators.append('-')
			elif '/' in exp:
				pieces=exp.split('/')
				self.Operators.append('/')
			else:
				pieces=exp.splie()
			self.Operand1.append(pieces[0])
			self.Operand2.append(pieces[1])

#		print([self.Operand1,self.Operand2,self.Operators])
	
	def add(self,opt1, opt2):
		print("%.2f"%(opt1+opt2))

	def sub(self,opt1, opt2):
		print("%.2f"%(opt1-opt2))

	def div(self,opt1, opt2):
		print("%.2f"%(opt1/opt2))

	def mul(self,opt1, opt2):
		print("%.2f"%(opt1*opt2))

	def calculate(self, operator, opt1, opt2):
		if opt1.isdigit() and opt2.isdigit():
			opt1=float(opt1)
			opt2=float(opt2)
			if operator=='*':
				self.mul(opt1, opt2)
			elif operator=='+':
				self.add(opt1, opt2)
			elif operator=='-':
				self.sub(opt1, opt2)
			elif operator=='/':
				if(opt2!=0):
					self.div(opt1, opt2)
				else:
					print("ZeroDivisionError")
			else:
				print("invalid operator")
		elif (not opt1.isdigit()) and opt2.isdigit():
			print("NameError")
		else:
			print("SyntaxError")

	def run(self):
		for i in range(self.calcTimes):
			self.calculate(self.Operators[i], self.Operand1[i], self.Operand2[i])

			
			

if __name__=="__main__":
	calc = Calc()
	calc.getInput()
	calc.AnyliseExp()
	calc.run()
