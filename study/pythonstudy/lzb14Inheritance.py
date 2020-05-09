class Bird:
    wind = ''
    foot = 0
    def flying(self):
        print("Bird is flying")
        return;
    def drink(self):
        print("Bird is drinking")

class Lark(Bird):
    def drink(self):
        print("Lark is drinking")

lark = Lark()
lark.flying()
lark.wind = 'small'
s = lark.__getattribute__("wind")
lark.__setattr__("foot",2)
f = lark.__getattribute__("foot")
print(f)

bird = Bird()
bird.drink()
lark.drink()