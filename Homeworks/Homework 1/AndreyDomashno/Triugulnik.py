import random

class Matrix():    
    def __init__(self, cap):
        self.stash=[[]]
        self.cap=cap
        for i in range (0,cap):
            self.stash.append([])
            for j in range (1,i+2):
                self.stash[i].append(random.randint(0,cap))

    def print(self):
        for i in range(0,len(self.stash)-1):
            print(str(i+1)+" - ",end='')
            print(self.stash[i])
            
    def find_biggest_sum(self):
        #self.print()
        #print("------")
        result=0
        temp=self.stash
        y =self.cap-1
        
        while(y!=0):
            for i in range(0,self.cap-(self.cap-y)):
                if(temp[y][i]<temp[y][i+1]):
                    temp[y-1][i]+=temp[y][i+1]
                else:
                    temp[y-1][i]+=temp[y][i]
            y-=1
        #self.print()
        return temp[0][0]

matrixT1 = Matrix(4)
matrixT1.stash = [[1],[2,3],[100,4,5],[1,1,1,2],[]]
            
matrixT2 = Matrix(4)
matrixT2.stash = [[3],[7, 4],[2, 4, 6,],[8, 5, 9, 3]]

matrixT1.print()
print("Biggest sum of triangleT1 is: "+str(matrixT1.find_biggest_sum()))

print("Biggest sum of triangleT2 is: "+str(matrixT2.find_biggest_sum()))

matrix100 = Matrix(100)
print("Biggest sum of triangle100 is: "+str(matrix100.find_biggest_sum()))
