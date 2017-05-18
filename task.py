# import geocoder?
import time
import json
# inOutOnline
IN, OUT, ONLINE = range(3)


class Task:
    def __init__(self, task_id, title, desc, creator, in_out_online, task_type, location, value=1):
        self.task_id = task_id
        self.title = title
        self.description = desc
        self.creator = creator
        self.in_out_online = in_out_online  # in / out / online
        self.task_type = task_type          # sport & body / be good / adventures / waste my time / culture

        self.location = location
        self.value = value
        self.creation_time = time.time()
        self.do_counter = 0
        self.complete_counter = 0
        self.del_counter = 0

    def get_title(self):
        return self.title

    def get_id(self):
        return self.task_id

    def get_description(self):
        return self.description

    def get_creator(self):
        return self.creator

    def get_in_out_online(self):
        return self.in_out_online

    def get_type(self):
        return self.task_type

    def get_loc(self):
        return self.location

    def get_value(self):
        return self.value

    def get_creation_time(self):
        return self.creation_time

    def get_do_count(self):
        return self.do_counter

    def get_done_count(self):
        return self.complete_counter

    def get_del_count(self):
        return self.del_counter

    def get_json(self):
        return json.dumps(self.__dict__)

    def inc_do_count(self):
        self.do_counter += 1

    def inc_complete_count(self):
        self.complete_counter += 1

    def inc_del_count(self):
        self.del_counter += 1

    def check_criteria(self, in_out_online, task_type):
        return (not in_out_online or self.in_out_online == in_out_online ) and \
            (not task_type or self.task_type == task_type)

