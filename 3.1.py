with open("F1.txt","w") as f1:  
    while True: 
        st=input("Введите строку(для окончания ввода введите пустую строку)")   
        if st == "":    
            break   
        f1.write(st+"\n")
    try:
        n1=int(input("Введите номер 1 строки"))
        n2=int(input("Введите номер 2 строки")) 
    except ValueError:
        print("Только цифры")   
with open("F1.txt","r") as f1, open("F2.txt","w") as f2:    
    sts=f1.readlines()  
    for i in range(n1-1,n2):    
        if sts[i].startswith("A"):  
            f2.write(sts[i])
with open("F2.txt", "r") as f2: 
    first=f2.readline() 
    count=len(first.split())    
    print(f"Количество слов в первой строке:{count}")