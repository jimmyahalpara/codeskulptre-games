import random
class Game:
    def __init__(self):
        self.main=[[' ' for a in range(5)] for a in range(5)]
        self.insert_into_random()
        self.insert_into_random()
        self.print_game()
    def insert_into_random(self,value=False):
        while True:
            i=random.randint(0,2)
            j=random.randint(0,2)
            if self.main[i][j]==' ':
                if value:
                    self.main[i][j]=str(random.choice([2,4]))
                else:
                    self.main[i][j]=str(2)
                break
    def shrink(self,lis):
        l=[]
        for a in lis:
            if a<>' ':
                l.append(a)
        while len(l)<len(lis):
            l.append(' ')
        return l
    def check(self,lis):
        l=lis[:]
        con=False
        for i in range(len(l)):
            if l[i]==' ':
                continue
            else:
                for j in range(i+1,len(l)):
                    if (l[i]==l[j]):
                        con=True
                    elif l[j]==' ':
                        continue
                    else:
                        break             
        return con
    def add(self,lis):
        l=lis[:]
        l=self.shrink(l)
        for i in range(len(l)-1):
            if (l[i]==l[i+1]) and l[i]<>' ':
                l[i+1]=' '
                n=int(l[i])
                n*=2
                l[i]=str(n)
                l=self.shrink(l)
        return l
    def print_game(self):
        for a in self.main:
            print a
    def main_process(self,side):
        if side=='up':
            for i in range(5):
                l=[]
                for j in range(5):
                    l.append(self.main[j][i])
                l=self.add(l)
                for j in range(5):
                    self.main[j][i]=l[j]
            self.insert_into_random()
        elif side=='down':
            for i in range(4,-1,-1):
                l=[]
                for j in range(5):
                    l.append(self.main[j][i])
                l=self.add(l)
                k=4
                for j in range(5):
                    self.main[j][i]=l[k]
                    k-=1
            self.insert_into_random()
        elif side=='left':
            for i in range(5):
                l=[]
                for j in range(5):
                    l.append(self.main[i][j])
                l=self.add(l)
                for j in range(5):
                    self.main[i][j]=l[j]
            self.insert_into_random()
        elif side=='right':
            for i in range(5):
                l=[]
                for j in range(4,-1,-1):
                    l.append(self.main[i][j])
                l=self.add(l)
                k=0
                for j in range(4,-1,-1):
                    self.main[i][j]=l[k]
                    k+=1
                    
        self.print_game()
    
                
                
    
