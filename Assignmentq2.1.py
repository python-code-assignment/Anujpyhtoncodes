dic={}
n=int(input("Enter no of keys in dictionary"))
for i in range(0,n):
    k = int(raw_input("Enter the value of Key"))
    v = k**2
    dic.update({k:v})

print("The dictionary value is:")
print(dic)
