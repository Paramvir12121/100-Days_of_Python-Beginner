import pandas

students_data = {
    "student": ["Alice", "Bob", "Charlie"],
    "score": [92, 88, 94]  
}

df = pandas.DataFrame(students_data)

for (index,row) in df.iterrows():
    if row.student == "Alice":
        print(row.score)


diff = { index:row for (index,row) in df.iterrows() if row.score>90 }

print(pandas.DataFrame(diff))