#coding: UTF-8
import random

class simulator:
#	seed=0;
#	iterators=0
	def isUnique(self,data):
                if len(data)==len(set(data)):
                        return True;
                else:
                        return False;

	def run(self):
		seed, iteraters=map(int,input().split())
		random.seed(seed)
		Sum=0
		for i in range(iteraters):
			testData=[]
#			random.seed(seed) 
			for j in range(23):
				testData.append(random.randint(1,365))
			print(len(testData))
			if not self.isUnique(testData):
				Sum=Sum+1
		print('rate=%.2f'%(Sum/iteraters))
	


if __name__ =="__main__":
	sim = simulator()
	print(sim.isUnique([1,32,2,1,3]))
	sim.run()

			
