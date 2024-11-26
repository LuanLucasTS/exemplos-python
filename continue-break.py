count = 0

#pula o loop 2
while count <=5:
    count +=1
    if count == 2: continue
    print(count)

#sai do loop depois do 3
count = 0
while count <=5:
    print(count)
    count +=1
    if count > 3: break