import json 
companies=[]    
total_pribyl=0
count=0
with open("Firms.txt", "r") as f:   
    for l in f: 
        data=l.strip().split()  
        name=data[0]    
        dohod=float(data[2])    
        rashod=float(data[3])   
        pribyl=dohod-rashod 
        companies.append({name:pribyl}) 
        if pribyl>0:
            total_pribyl += pribyl 
            count+=1   
if count>0:
    average=total_pribyl/count 
else:   
    average=0
res=[companies,{"Средняя прибыль": average}]
with open("Firms.json", "w") as file:
    json.dump(res, file)
