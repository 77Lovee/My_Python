#coding: UTF-8
keywords=['if', 'then', 'else', 'while', 'do']
operators=['+','/', '-', '*', ';', '<', '>', '(', ')', '=',]
def isChar(c):
    if((c>='a'and c<='z') or (c>='A'and c<='Z')):
        return True
    else:
        return False
def isNum(c):
    if(c>='1' and c <='9'):
        return True
    else:
        return False

def isOct(c):
    if(c>='1' and c<='7'):
        return True
    else:
        return False
def isHex(c):
    if(isNum(c) or (c>='a' and c<='f') or (c>='A' and c<='F')):
        return True
    else:
        return False
def isOpt(c):
    if c in  operators:
        return True
    else:
        return False
class Cutter:
    string=""
    state=0
    index=-1
    recive=[]
    result=[]
    def readFile(self, fileName):
        f=open(fileName)

        for i in f.readlines():
            self.string+=i
        #print(string)
        print("************************"+fileName+"**********************")
        print(self.string)
        print("*******************************************************")
        return  self.string

    def run(self):
       while(self.index<len(self.string)-1):
            self.index=self.index+1
            readChar=self.string[self.index]
           # print(self.recive)
            #print(readChar)
            if(self.state==0 and isChar(readChar)):
                self.state=1
                self.recive.append(readChar)    # 状态0到转态1， 读入一个字母
            #	print(recive)

            elif(self.state==0 and readChar=='0'):
                self.state=2
                self.recive.append(readChar)     # 状态0到转态2， 读入一个0
            #	print(recive)

            elif(self.state==0 and isOpt(readChar)): # 状态0到状态5，读入一个操作符
                self.state=5
                self.recive.append(readChar)

            elif(self.state==1 and (isChar(readChar) or isNum(readChar))):
                self.state=1
                self.recive.append(readChar)   # 状态1到状态1，读入一个数字或字母
            #	print(recive)

            elif(self.state==1 and not(isChar(readChar) or isNum(readChar))):
                #       self.state=4		遇到一个非数字、字母符号，输出已读入字符串
                #      	re=recive
                #print(readChar)

                chars2string="".join(self.recive)
                if chars2string in keywords:
               #     print([chars2string, "-"])
                    self.result.append([chars2string, "-"])
                else:
               #     print(["0",chars2string])
                    self.result.append(["0",chars2string])
                #print(recive)
                self.recive=[]
                self.index=self.index-1
                self.state=0

            elif(self.state==2 and isOct(readChar)):
                self.state=3
                self.recive.append(readChar) # 状态2到状态2，读入[0-7]之间的一个数
            #print(recive)

            elif(self.state==3 and (readChar==0 or isOct(readChar))):
                self.state=3
                self.recive.append(readChar)

            elif(self.state==3 and not (readChar==0 or isOct(readChar))):
                chars2Oct="".join(self.recive)
               # print(["2",chars2Oct])
                self.result.append(["2",chars2Oct])
                self.recive=[]
                self.state=0
                self.index=self.index-1

            elif(self.state==2 and (readChar=='x' or readChar=='X')):
                self.state=4
                self.recive.append(readChar)


            elif(self.state==4 and isHex(readChar)):
                self.state=4
                self.recive.append(readChar)

            elif(self.state==4 and not isHex(readChar)):
                chars2Hex="".join(self.recive)
               # print(["3",chars2Hex])
                self.result.append(["3",chars2Hex])
                self.recive=[]
                self.index = self.index -1
                self.state=0

            elif (self.state==2 and (readChar!="x" or readChar!="X" or not isOct(readChar))):
              #  print([1,self.recive])
                self.result.append([1,self.recive])
                self.recive=[]
                self.index = self.index -1
                self.state = 0

            elif(self.state==5):   # 无论当前字符是什么，输出recive中的操作符，缺点是无法识别多目操作符
                chars2Opt = "".join(self.recive)
               # print(["-", chars2Opt])
                self.result.append(["-", chars2Opt])
                self.state = 0;
                self.recive=[];
                self.index = self.index-1



            # elif(self.state==5 and not isOpt(readChar)):
            #     chars2Opt =  "".join(self.recive)
            #     print(["-", chars2Opt])
            #     self.state = 0;
            #     self.recive=[];
            #     self.index = self.index-1

            elif(self.state==0 and isNum(readChar)):
                self.state=6;
                self.recive.append(readChar)

            elif(self.state==6 and (isNum(readChar) or readChar=='0')):
                self.state=6;
                self.recive.append(readChar)

            elif(self.state==6 and (not(isNum(readChar) or readChar=='0'))):

                chars2Num="".join(self.recive)
              #  print(["1",chars2Num])
                self.result.append(["1",chars2Num])
                self.state=0
                self.recive=[]
                self.index = self.index-1






if  __name__ =="__main__":
    cutter = Cutter()
    cutter.readFile("codes.txt")
    cutter.run()
    print()
    for e in cutter.result:
        print(e )
