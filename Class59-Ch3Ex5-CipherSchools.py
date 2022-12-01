a=input("enter name:")
temp=""
for i in a:
    b=a.count(i)
    if i not in temp:
        temp+=i
        print(f"{i}:{b}")
