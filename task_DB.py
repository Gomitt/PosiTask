import time
import json
from random import shuffle
# from tinydb import TinyDB, Query

from task import Task
IN, OUT, ONLINE = range(3)

class Task_DB:

    def __init__(self):
        self.file_name = ""
        self.update_time = 0
        self.tasks = []
        self.update_time = time

    def insert_task(self, title, desc, creator, in_out_online, task_type, location, value):
        self.tasks.append(Task(title, desc, creator, in_out_online, task_type, location, value))

    def get_task(self, words, creator, in_out_online, task_type, location, value, num_of_tasks):
        return_list = [t for t in self.tasks if t.check_criteria(words, creator, in_out_online, task_type, location, value)]
        shuffle(return_list)
        return return_list[0:num_of_tasks]

