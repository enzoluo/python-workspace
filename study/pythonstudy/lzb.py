def sum_t(list):
    s = 0
    for x in list:
        s +=x
    return s

s = sum_t([1,2,3,4,5])

def printInfo(arg1,*vartuple):
    print("input")
    print(arg1)
    for x in vartuple:
        print(x)
    return
s = printInfo('nihao',(1,2,3,4,5,6,7,8))

print(s)
def main():
    print("123{}","456")

if __name__ == '__main__':
    main()