class User:
    name = ''
    password =''
    def getName(self):
        return self.name
    def getPassword(self):
        return self.password
    def setName(self,name):
        self.name = name
    def setPassword(self,password):
        self.password = password

user = User()
user.setName("zhangsan")
user.name = "lisi"
s = user.getName()
z = user.name
user.__setattr__("name","wangwu")  # 这是 python自带的set方法
n = user.__getattribute__("name") # 这是python 自带的get方法
print(s) #lisi
print(z) #lisi
print (n)



