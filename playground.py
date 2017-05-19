from task_db import TaskDB
import csv

filename = 'db/posiTask examples - tasks.csv'
comments = {'Mottig': 'Amazing task, really made me smile!!!',
            'Nofar': 'Totally changed my life :)',
            'Eshed The King': 'How am I ??',
            'LouisL': 'I wish I could\'ve go back in time and do it again'}
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
        db.insert_task(title=row[1],desc=row[2],creator=row[4],
                       in_out_everywhere=row[7],task_type=row[3],location=row[6],
                       duration=row[5],comments=comments,value=1)

for task_type, vals in db.get_tasks_dict().items():
    for t in vals:
        print(t.get_json())


db.save('db/db1.pickle')
