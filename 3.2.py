with open("Государство.txt","r") as f:  
    for st in f: 
        data=st.strip().split() 
        country=data[0] 
        population=int(data[2]) 
        if population>1000000:
            print(country)