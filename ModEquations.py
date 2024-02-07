import math
method = int(input('1. inverse  2. equation ||  method: '))
set = int(input('Set = '))
numIn = input('a = ')
if method == 2 :
    b = int(input('b = '))
num = int(numIn)
if (num > set) :
    num = int(num%set)
    print(f'in Z-{set}, the equivalent class is {num}')
nGcd = math.gcd(num, set)
print (f'GCD is: {nGcd}')
count = 0
if (nGcd != 1) :
    print(f'there is no inverse in the Z-{set}')
elif (nGcd == 1) :
    var = 0
    while (((var)-1)%set != 0) :
        count += 1
        var = num*count
    res = int(var/num)
if method == 2 :
    res = res * b
    if res > set : res = res%set
    print (f'the solution is: {res}')
elif method == 1 :
    print(f'the inverse is: {res}')

input('press a key to exit')
