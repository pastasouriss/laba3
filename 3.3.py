subjects={} 
with open("Subjects.txt","r") as f: 
    for l in f: 
        data = l.strip().split(": ") 
        subject=data[0] 
        lessons=data[1].split() 
        vsego=sum(int(lesson.split("(")[0]) for lesson in lessons)
        subjects[subject]=vsego
print(subjects)


