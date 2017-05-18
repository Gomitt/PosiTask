from task_db import TaskDB
import csv

filename = 'db/posiTask examples - tasks.csv'
db = TaskDB()
with open(filename, newline='') as f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    counter = 0
    for row in reader:
        counter += 1
        row = [s.replace("\n","<br>") for s in row]
        print(row)
        db.insert_task(row[1],row[2],row[4],row[7],row[3],row[6],row[5],1)
        if counter > 6:
            break

for task_type, vals in db.get_tasks_dict().items():
    for t in vals:
        print(t.get_json())



db.save('db/dbshort.pickle')
