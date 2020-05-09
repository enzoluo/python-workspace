from collections import deque

L = [5,2,1,4,3]

L.append(6)
L.insert(0,0)
s = L.index(6)
#L.clear()
#del L[0]
#del L[:] 采用切片的方式进行删除
L.sort() #顺序排序，
L.reverse() # 倒序排序
L.extend([7,8,9])
#print(L)

#the useful of the list
'''1、将list当做一个堆栈来使用，堆栈是先进先出
stact = [1,2,3]
stact.append(4)
stact.append(5)
print(stact)
s1 = stact.pop()
s2 = stact.pop()
print(s1)
print(s2)
print(stact)'''

'''2、将list当做一个队列来使用，队列先进先出
queue = deque([1,2,3])
queue.append(4)
queue.append(5)
queue.append(6)
s1 = queue.popleft()
print(s)
print(queue)'''

'''列表推导式'''
vec = [2,4,6]
s = [3*x for x in vec if x >3]
print (s)

vec1 = [-4,5,7]
vec2 = [2,5,8]
s = [x*y for x in vec1 for y in vec2 ]
print(s)