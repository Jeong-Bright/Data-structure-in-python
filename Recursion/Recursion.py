import random

def addNum(num):
    if num <= 1:
        return 1
    return num + addNum(num -1)

print(addNum(10))

def factorial(num):
    if num <= 1:
        return 1

def factorial(num):
    if num <= 1:
        return 1
    print("%d * %d 호출" % (num, num-1))
    retval = factorial(num-1)
    
    print("%d * %d!(=%d) 반환" % (num, num-1, retval))
    return num * retval

print ('10! = ', factorial(5))


# def gugu(n, num):
#     print("%d x %d = %d" % (n, num, n*num))
#     if num < 9:
#         gugu(n, num+1)

# for n in range(2, 10):
#     print("## %d단 ##" % n)
#     gugu(n, 1)
    
def arySum(arr,n):
    if n <= 0:
        return arr[0]
    return arySum(arr,n-1) + arr[n]

ary = [random.randint(0, 255) for i in range(random.randint(10,20))]
print(ary)
print('배열 합계 -->', arySum(ary, len(ary)-1))


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

print ('피보나치 수 --> 0 1 ', end = ' ')
for i in range(2, 20):
    print(fibo(i), end=' ')
    
def palindrome(pStr):
    if len(pStr) <= 1:
        return True
    
    if pStr[0] != pStr[-1]:
        return False
    
    return palindrome(pStr[1:len(pStr)-1])

strAry = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주"]
print('\n')

for i in strAry:
    print(i, end = '-->')
    i = i.lower().replace(' ', '')
    if palindrome(i):
        print('O')
    else:
        print('X')
