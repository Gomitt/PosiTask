from task import Task
import time

t = Task(title='hi', desc='bye', creator='sdf', in_out_online=0, task_type=1, location="dsfsadf", value=2)
print(t.get_json())