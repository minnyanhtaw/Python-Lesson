# if True:
#     print("hi")
# else:
#     print("no")

count = input("Your count : ")
pointer1 = 0
pointer2 = 1

for i in range(int(count)):
    result = pointer1 + pointer2
    print(result)
    pointer2 = pointer1
    pointer1 = result
