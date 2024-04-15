#Codewars style ranking system

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def rank_up(self):
        while self.progress >= 100:
            self.progress -= 100
            self.rank = min(self.rank + 1, 8)
        if self.rank == 0:
            self.rank += 1

    def inc_progress(self, points):
        d = points - self.rank
        if d == 0:
            self.progress += 3
        elif 0 < d:
            self.progress += 10 * d * d
        elif d == -1:
            self.progress += 1
        #if d >= -1:
            #self.progress += User.difference[d]
        else:
            pass
        
        self.rank_up()

user = User()
user.inc_progress(1)
print(user.rank)
print(user.progress)
user.inc_progress(1)
print(user.rank)
print(user.progress)

class User():
    rank_vector =[i for i in range(-8,9,1) if ( i!=0)]

    def __init__(self):
        self.rank=-8
        self.progress=0

    def inc_progress(self,kata):
        if kata not in self.rank_vector:
            raise ValueError("Not in the specified Range of features")
        if (self.rank==8):
            progressmeter=0
        elif(self.rank_vector.index(kata) ==self.rank_vector.index(self.rank)):
            progressmeter=self.progress+3
        elif(self.rank_vector.index(kata)==self.rank_vector.index(self.rank)-1):
            progressmeter=self.progress+1
        elif(self.rank_vector.index(kata) <= self.rank_vector.index(self.rank)-2):
            progressmeter=self.progress
        elif(self.rank==-1 and kata==1):
            progressmeter=self.progress+10

        else:
            progressmeter=self.progress+ 10* pow(abs(self.rank_vector.index(kata)-self.rank_vector.index(self.rank)),2)
        progressIndex=list(divmod(progressmeter,100))
        self.progress=progressIndex[1]
        self.rank=self.__updaterank__(progressIndex[0])
        if self.rank==8:
            self.progress=0
        return self.progress


    def __updaterank__(self,level=1):

        if self.rank==8:
            return self.rank
        elif self.rank_vector.index(self.rank)+level > self.rank_vector.index(8):
            self.rank=8
        else:
            self.rank=self.rank_vector[self.rank_vector.index(self.rank)+level]
        return self.rank
