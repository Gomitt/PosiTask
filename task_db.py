import time
import pickle
from random import shuffle
from collections import defaultdict

from task import Task
IN, OUT, ONLINE = range(3)
task_types = ['sport & body', 'be good', 'adventures', 'waste my time', 'culture']

class TaskDB:

    task_types = task_types

    def __init__(self, filename=''):
        if filename:
            db_dict = pickle.load(open(filename, "rb"))
            self.max_id = db_dict['max_id']
            self.tasks_dict = db_dict['task_dict']
            del db_dict
        else:
            self.tasks_dict = dict(zip(task_types, [list() for _ in task_types]))
            self.max_id = 0

    def save(self, filename):
        pickle.dump({'task_dict': self.tasks_dict, 'max_id': self.max_id}, open(filename, "wb"))

    def insert_task(self, title, desc, creator, in_out_everywhere, task_type, location, value):
        self.tasks_dict[task_type].append(Task(task_id=self.max_id + 1, title=title, desc=desc, creator=creator,
                                               in_out_everywhere=in_out_everywhere, task_type=task_type,
                                               location=location, value=value))
        self.max_id += 1

    def get_tasks_dict(self):
        return self.tasks_dict

    def get_by_id(self, task_id):
        for tasks_list in self.tasks_dict.values():
            for t in tasks_list:
                if t.task_id == task_id:
                    return t
        return None

    def remove_by_id(self, task_id):
        for task_type, tasks_list in self.tasks_dict.items():
            self.tasks_dict[task_type] = [t for t in tasks_list if t.task_id != task_id]

    def num_tasks(self):
        num = 0
        for tasks in self.tasks_dict.values():
            num += len(tasks)
        return num
