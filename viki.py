list = []
for i in range(5):
    name = (input("Enter your name: "))
    num = int(input("Enter your number: "))
    value = {'name': name, 'num': num}
    list.append(value)
for person in list[:]:  
    if list[i]['name']=='vivek':
       print(list[i]['num'])
       list.remove(person) 
print(len_list)
#for i in range(4):
#print(list[i]['name'])       
#print(list['num'])
#print(list[3]['name'])
#print(list[3]['num']) 
