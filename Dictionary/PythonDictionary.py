#in this program we append elements and its value to the dictionary

dick={}
inp=int(input("Enter the number of people you want to add :"))
for i in range(0,inp):
    name=input("Enter Person's Name")
    num=int(input("Enter his Number"))
    dick[name]=num
print("Dictionary is as follows : \n",dick)

print(dick['qwe'])

