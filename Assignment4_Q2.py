#Triple of given list of integers using MAP function.

list1 = list(map(int,input("Enter your list: ").split()))

result =list(map(lambda x :  x*3,list1))
print("Triple of given list is:" ,result)

