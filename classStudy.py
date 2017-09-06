# result = 0
#
# def adder(num):
#     global result
#     result += num
#     return result
#
# print(adder(30))
# print(adder(25))

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

class Service:
    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("Mr. %s, %s + %s = %s" % (self.name, a, b, result))

pey = Service("hong")
pey.sum(1, 2)


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

class HousePark:
    lastname = "park"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, traveled %s" % (self.fullname, where))
    def __add__(self, other):
        print("%s, %s married" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s divorced" % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "kim"

pey = HousePark("hehey")
pey.travel("seoul")

juliet = HouseKim("hongseob")
juliet.travel("dokdo")

pey + juliet
pey - juliet