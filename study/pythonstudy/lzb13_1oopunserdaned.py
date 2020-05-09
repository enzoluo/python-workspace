class User:
    def __init__(self,name,password): # 这个是构造方法
        self.name = name
        self.password = password

    def data(self):
        print("name:"+self.name,"password:"+self.password)

    def _updatePass(self,password):
        self.password = password

    def updateName(self,name):
        self.name = name
    def updateData(self,name,password):
        self.updateName(name)
        self._updatePass(password)



class Lzb(User):
    def printInfo(self):
        print("hello world")

user = User("zhangsan",'123')
name = user.__getattribute__('name')
print(name)
user.updateName('lisi')
name = user.__getattribute__('name')
print(name)

user.data()

lzb = Lzb('luozhibo','123')
lzb.data()
lzb.updateName('enzo')
lzb.data()
lzb.updateData('wuyi','123456')


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

