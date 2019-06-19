# coding: UTF-8
"""
对下面文法做消除左递归操作
G[E]：
 E->T|E+T;
 T->F|T*F;
 F->i|(E);

 E -> TM    此处的M相当于E', N 相当于T'
 M -> +TM | ε
 T -> FN
 N -> *FN | ε
 F ->(E) | i

"""
from  Tools import Stack
from Cutter import Cutter

Gram={"E":["TM"], "M":["+TM","ε"], "T":["FN"], "N":["*FN","ε"], "F":["(E)","i"]}
print("N" in Gram)

class Analyzer:
    FIRST={}
    FOLLOW={}
    Table={"E":{},"M":{},"T":{}, "N":{}, "F":{}}
    temp=[]
    flagStack=Stack()
    flagStack.push("#")
    flagStack.push("E")

    def stringReverse(self,line):
        data=[]
        for i in range(len(line)):
            data.append(line[len(line)-1-i])
        return "".join(data)
    def showGram(self):  # 查看语法
        print("<<<<<< 文法 >>>>>>")
        for g in Gram:
            if(len(Gram[g])==1):
                print(g+" -> "+Gram[g][0])
            if(len(Gram[g])==2):
                print(g+" -> "+Gram[g][0]+"|"+Gram[g][1])


    def isNoneT(self, c):                    # 判断是否为非终结符
        if(c>='A'and c<='Z'):
            return True
        else:
            return False
    """
    def isT(c):                         # 判断是否为终结符
        if((c>='a' and c<='z') or c == 'ε'):
            return True
        else:
            return False
    """

    def getOneFirst(self,Gram,key):                    # 获取FIRST 集
        for item in Gram[key]:                      # 文法右侧第一个字符是终结符则添加到列表，
            if not self.isNoneT(item[0]):           # 如果是非终结符的话，把它的FIRST集添加进来
                self.temp.append(item[0])
            elif self.isNoneT(item[0]):
                if(item[0] in Gram):
                    self.getOneFirst(Gram,item[0])
            else:
                print("Grammer is invalid")
        #print(key+"="+str(self.temp))
        self.FIRST[key]=self.temp

    def getFirst(self,Gram):
        for g in Gram:
            self.getOneFirst(Gram,g)
            self.temp=[]

    def existEmpty(self, key):    ## 判断某个非终结符的FIRST集中是否存在ε
        if 'ε' in self.FIRST[key]:
            return True
        else:
            return False

    def showFirst(self):
        print("<<<<<< FIRST集 >>>>>>")
        for g in self.FIRST:
            print("FIRST("+g+")="+str(self.FIRST[g]))

                                                            # 开始符号S: # 收入FOLLOW(U)
                                                            # ...Ua...： 直接把a收入FOLLOW(U)
                                                            # E ->...UP...:  FIRST(P)中没有ε，把FIRST(E)收入FOLLOW(U)
                                                            #                FIRST(P)中有ε，把FOLLOW(E)收入FOLLOW(U)
                                                            # E->...U: 把FOLLOW(E)收入FOLLOW(U)中
    def getOneFollow(self, Gram, key):
        dat=[]
        dic={}
        if key=='E':
            self.temp.append("#")
        for g in Gram:                   # 找出所有文法右侧含有key的文法
            for m in Gram[g]:
                if key in m:
                   # dat.append({g:m})
                    dic[g]=m
        #dic[key]=dat
       # print(dic)
        for g in dic:
            index = dic[g].index(key)
            if((index+1)<=len(dic[g])-1 and not self.isNoneT(dic[g][index+1])):   # 规则1
                self.temp.append(dic[g][index+1])

            elif((index+1)<=len(dic[g])-1 and self.isNoneT(dic[g][index+1])):     # 规则2
                self.temp.extend(self.FIRST[dic[g][index+1]])
                if(self.existEmpty(dic[g][index+1])):
                    self.temp.extend(self.FOLLOW[g])
                    self.temp.remove('ε')

                    #self.temp.extend(self.FOLLOW[g])
            elif(index==len(dic[g])-1):                                             # 规则三
                if(g==dic[g][len(dic[g])-1]):
                    pass
                else:
                    self.temp.extend(self.FOLLOW[g])
        self.FOLLOW[key]=set(self.temp)
       # print(self.temp)
        self.temp=[]

    def getFollow(self):
        analyser.getOneFollow(Gram,"E")
        analyser.getOneFollow(Gram,"M")
        analyser.getOneFollow(Gram,"T")
        analyser.getOneFollow(Gram,"N")
        analyser.getOneFollow(Gram,"F")

    def showFollow(self):
         print("<<<<<< FOLLOW集 >>>>>>")
         for g in self.FOLLOW:
            print("FOLLOW("+g+")="+str(self.FOLLOW[g]))


    def buildOneTable(self, Gram, key):                   # 构造分析表
        for val in Gram[key]:
            if self.isNoneT(val[0]):                    # 规则2
                #print(self.FIRST[val[0]])
                #self.temp.extend({"first":self.FIRST[val[0]]})
                for dat in self.FIRST[val[0]]:
                    self.Table[key][dat]={key:val}
            elif (not self.isNoneT(val[0])) and val[0]!='ε':
                self.Table[key][val[0]]={key:val}

            elif val[0]=='ε':                         # 规则3
                for dat in self.FOLLOW[key]:
                    self.Table[key][dat]={key:val}
            self.Table['E']['#']="Finish"
        self.temp=[]

    def buildTable(self,Gram):

        for key in Gram:
            for i in {'i','+','*','(',')','#'}:
                self.Table[key][i]="Error"
            self.buildOneTable(Gram,key)
       # print(self.temp)



    def showTable(self):
        print("<<<<<< Analyse Table >>>>>>")
        #print(" ",end='')
        for key2 in ['i','+','*','(',')','#']:
            print("\t\t"+key2,end="")
        print()
        for key1 in ['E','M','T','N','F']:
            print(key1,end="\t")
            for key2 in ['i','+','*','(',')','#']:
                if(self.Table[key1][key2]=='Error'):
                    print(self.Table[key1][key2]+"\t",end=" ")
                elif(self.Table[key1][key2]=="Finish"):
                    print(self.Table[key1][key2]+"\t",end=" ")
                else:
                    print(key1+"->"+self.Table[key1][key2][key1]+"\t",end=" ")
            print()

    def getData(self):
        cutter=Cutter()
        cutter.readFile("code.txt")
        cutter.run()

   # print(cutter.result)
        data=[]
        data2=[]
        for i in cutter.result:
            if i[0]=='1' or i[0]=='0':
                data.append("i")
            elif i[0]=='-':
                data.append(i[1])
            tmp= "".join(data)


        tmp=tmp.split(";")


          #  data2.append(i[1])
        return tmp
       # print(tmp)

    def startAnalyse(self,line,line2):
        lineStack=Stack()
        lineStack.push("#")
        print(line2)
      #  print(tmp)
        for i in self.stringReverse(line):
            lineStack.push(i)
        # for j in range(lineStack.size()):
        #     print(lineStack.pop())
        readflag = False
        currentChar=lineStack.pop()
        currentFlag='E'
        while(self.flagStack.size()>=0 and lineStack.size()>=0):
            #print([currentFlag,currentChar])
           # print([currentFlag,currentChar],end = ' ')
            # copyFlag=self.flagStack
            # copyLine=lineStack
           # print(" 符号栈:",end=' ')
           # self.flagStack.show()
           # print("\t",end=" ")
            # for i in range(copyFlag.size()):
            #     print(copyFlag.pop(),end=' ')
          #  print("输入串：",end=' ')

           # lineStack.show()
            # for i in range(copyLine.size()):
            #     print(copyLine.pop(),end=' ')
            #print()

            if  currentChar=="#" and currentFlag=="#":
                print("成功")
                return
                #exit(0)
            elif currentFlag==currentChar and currentFlag!='#' and currentChar!='#':
                currentChar = lineStack.pop()
                currentFlag= self.flagStack.pop()

            elif self.isNoneT(currentFlag):
                express = self.Table[currentFlag][currentChar]
                if express=="Error":
                    print("出错")
                    return
                elif express=="Finish":
                    pass
                else:
                    express = self.Table[currentFlag][currentChar][currentFlag]
                   # print(express)
                    if express != "Error":
                        if express == 'ε':
                            pass
                        else:
                            for i in self.stringReverse(express):
                                self.flagStack.push(i)


                currentFlag=self.flagStack.pop()

            else:
                print("出错")
                return
                #exit(0)
        #print(lineStack)

if __name__=="__main__":

    analyser=Analyzer()
    analyser.getFirst(Gram)
    analyser.getFollow()
    analyser.showGram()
   # print(analyser.FIRST)
    analyser.showFirst()
   # print(analyser.existEmpty("T"))
    analyser.showFollow()
    #analyser.getData()
    analyser.buildTable(Gram)
    analyser.showTable()
    cutter = Cutter()
    data = cutter.readFile("code.txt").split(";")
    print("****************************")
    i=0
    for test in analyser.getData():
         analyser.startAnalyse(test,data[i]+";")
         analyser.flagStack.push("#")   # 重置符号栈
         analyser.flagStack.push("E")
         i=i+1
       #  print()
   # analyser.startAnalyse("i")
   # print(analyser.Table)


