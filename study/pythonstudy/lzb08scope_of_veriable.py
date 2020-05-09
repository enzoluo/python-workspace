# L（Local）局部作用域
# E （Enclosing）闭包函数外的函数中
# G（Global）全局作用域
# B（Built-in） 内建作用域

# 查找规则 L->E ->G->B 即 局部找不到到闭包，闭包找不到到全局，全局找不到到内建

scope_G = 30
scope_B = int(40.0)
def test_scope():
    scope_E = 20
    print(scope_E)
    print(scope_G)
    print(scope_G)
    print(scope_B)
    def inter():
        scope_L = 10
        print(scope_L)
        print(scope_E)
        print(scope_G)
        print(scope_B)



test_scope()
