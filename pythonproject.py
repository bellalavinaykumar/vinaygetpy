class student:
    def __init__(self,name,roll,class_room):
        self.name=name
        self.roll=roll
        self.class_room=class_room

    def math_marks(self,mark):
        self.marks=mark
        return self.marks
    def comparing_marks(self,other):
        if self.math_marks>other.math_marks:
            print(self.name,"wins")
        else:
            print(other.name,"wins")

s1=student("ram",51,"4th")
s2=student("vinay",50,"4th")
print(s1.name,s2.name)
print(s1.math_marks(54))
print(s2.math_marks(58))

