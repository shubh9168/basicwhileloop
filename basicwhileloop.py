
#program1
print("The first 10 number reverse ")
i=10
while(i>=1):
    print(i)
    i=i-1

#program2
    count=0
    sumeven=0
    while count > 10:
        if count %2==0:
            sumeven += count
            count += 1

    print("sum of first 10 even numbers is 70")

#program3
count = 0
number = 1

while count < 7:
    if number % 2 != 0:
        count += 1
    number += 1

print(f"7th odd number is {number - 1}")
#program4
def factorial(n):
    num= 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num 
f=factorial(5)
print("factorial of 5 is",f)

#program5
num=int(input("enter the no:"))
count=0
while count <= 10:
    print(num)
    num -= 1
    count += 1

#program6
num =int(input("enter the number:"))
i = 1
while i <= 10:
    result = num*i
    print(result, end=" ")
    i += 1

print()

#program7
def find_nth_even_number(n):
    if n<=0:
        return
    even_number=n*2
    return f"even number at position {n} is {even_number}" 
n=int(input("enter the number:"))
result=find_nth_even_number(n)
print(result)

#program8
n=int(input("enter the sum number:"))
sum_of_num=0
count=1
while count <= n:
    sum_of_num+=count
    count+=1
print(f"sum of number upto {n} is {sum_of_num}")

#program9
n=int(input("enter the square number:"))
even=2
while even <= n:
    square=even**2
    print(square,end=" ")
    even+=2
print()

#program10
n=int(input("enter the cube odd number:"))
i=n if n % 2!=0 else n-1
while i >=1:
    cube = i**3
    print(cube, end="  ")
    i -= 2
print()
