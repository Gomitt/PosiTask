from task_db import TaskDB

db = TaskDB()
db.insert_task(title='hi', desc='bye', creator='sdf', in_out_online=0, task_type=1, location="dsfsadf", value=2)
print()