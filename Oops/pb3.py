import random

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self , fro , to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}" )

    def getstatus(self):
        print(f"train no : {self.trainNo} is runnig on time ")

    def getFare(self,fro ,to ):
        print(f"Tickets fare in train no : {self.trainNo}  from {fro} to  {to} is {random.randint(222,5555)}")


t = Train(45334)
t.book("amarathi " , "delhi") 
t.getstatus()
t.getFare("amaravathi " , "delhi")
 