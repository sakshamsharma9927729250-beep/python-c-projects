# OOPs Concepts in Python
# Class , Object & Inheritance(class variable , instance variable , class method , instance method , static method , super() , method overriding)
class std:
    school = "Holy family"
    tot = 0
    def __init__(self , name = "saksham" , age = 0 , mar = 0 , num = 0):
        self.name = name
        self.age = age
        std.tot += 1
        self.mar = mar
        self.num = num
    def show(self):
        return f"my name is = {self.name} and my age is = {self.age} and my marks is = {self.mar}"
    def work(self):
        print("I am working...")
    @classmethod
    def count(cls):
        return f"Total student is = {cls.tot}"
    def check(self):
        if self.mar > 33:
            return "pass"
        else:
            return "fail"    
class teacher(std):
    def __init__(self , name  = "saksham", age = 0, mar = 0, num = 0, lang = "python"):
        super().__init__(name , age , mar , num)
        self.lang = lang
    def seen(self):
        print("Language is =" , self.lang)
        print(f"my name is = {self.name} and my age is = {self.age} and my marks is = {self.mar}")
    def work(self):
        print("I am checking the students work...")
    def abc(self):
        if self.age > 10:
            return "you are in school" 
        else:
            return f"you are not in school"
    def table(self):
        for i in range(11):
            print(self.num , "X" , i , "=", (self.num * i))
    @staticmethod        
    def see():
        while True:

            print("========")
            print("1.add content")
            print("2.seen content")
            print("3.exit")

            ch = input("enter a number you choice..: ")
            if ch == "1":

                a = input("enter a content...: ")
                with open("my.txt" , "a")as file:
                    file.write(a + "\n")
                    print("your data has been saved in the file...")
                file.close()

            elif ch == "2":
                with open("my.txt" , "r")as file:
                    data = file.read()
                    print("your data is = " , data)
                file.close()

            elif ch == "3":
                print("Thanks for using.....")
                break

            else:
                print("Invalid choice...")
class principal(teacher):
    def __init__(self , name  = "saksham", age = 0, mar = 0, num = 0, lang = "python", exp = 0):
        super().__init__(name , age , mar , num , lang)
        self.exp = exp
    def work(self):
        print("I am checking the teachers work...")
s1 = teacher("saksham" , 13 , 89 , 5 , "python")
s2 = teacher("sakshi" , 15 , 29 , 4, "java")
s3 = teacher("gurpreet" , 14 , 90 , 8, "c++")
p1 = principal("dr. smith" , 45 , 0 , 0 , "english" , 20)
s4 = std("sahil" , 12 , 45 , 6)
manag = [
    std(),
    teacher(),
    principal()
]
for man in manag:
    man.work()
print(s1.show())
print(s1.check())
print(s2.show())
print(s2.check())
print(std.school)
print(std.count())
print(s1.abc())
print(s1.table())
print(teacher.see())
print(s1.seen())
print(p1.work())
print(s1.work())
print(s4.show())
print(s4.work())

# polymorphism(Looping , Duck typing , composition)
class emp:
    def work(self):
        print("I am working...")
class manager(emp):
    def work(self):
        print("I am managing the employees...")
class developer(emp):
    def work(self):
        print("I am developing the software...")
employees = [
    emp(),
    manager(),
    developer()
]
for employee in employees:
    employee.work()

class Pdf:
    def export(self):
        print("Exporting PDF report")
class ExcelReport:
    def export(self):
        print("Exporting Excel report")
class CSVReport:
    def export(self):
        print("Exporting CSV report")

def generate(report):
    report.export()

generate(Pdf())
generate(ExcelReport())
generate(CSVReport())

class car:
    def start(self):
        print("car is start..")
    def stop(self):
        print("car is stop..")

class engine:
    def __init__(self):
        self.car = car()
    def start(self):
        self.car.start()
        print("engine is start..")
s1 = engine()
s1.start()