import time
import pickle
from random import shuffle
from collections import defaultdict


from task import Task
IN, OUT, ONLINE = range(3)



class TaskDB:

    task_types = ['sport & body', 'be good', 'adventures', 'waste my time', 'culture']

    def __init__(self, filename=''):
        if filename:
            self.filename = filename
            db_dict = pickle.load(open( filename, "rb"))
            self.tasks = db_dict['tasks']
            self.counter = db_dict['counter']
            del db_dict
        else:
            self.tasks = []
            self.counter = 0

    def save(self, filename):
        pickle.dump({'tasks': self.tasks, 'counter': self.counter}, open(filename, "wb"))

    def insert_task(self, title, desc, creator, in_out_online, task_type, location, value):
        self.tasks.append(Task(task_id=self.counter + 1, title=title, desc=desc, creator= creator,
                               in_out_everywhere=in_out_online, task_type=task_type, location=location, value=value))
        self.counter += 1
        self.save(self.filename)

    def get_tasks_dict(self):
        res = defaultdict(list)
        for task in self.tasks:
            res[task.get_type()].append(task)
        return dict(res)

    def get_tasks(self, in_out_online, task_type, num_of_tasks=None):
        return_list = [t for t in self.tasks if t.check_criteria(in_out_online=in_out_online, task_type=task_type)]
        shuffle(return_list)
        if num_of_tasks:
            return_list = return_list[:num_of_tasks]
        return return_list

    def get_by_id(self, task_id):
        for t in self.tasks:
            if t.task_id == task_id:
                return t
        return None

    def remove_by_id(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def num_tasks(self, task_type=""):
        return len(self.tasks)
