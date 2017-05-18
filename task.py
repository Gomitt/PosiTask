# import geocoder?
import time
import json

class Task:
    def __init__(self, task_id, title, desc, creator, in_out_everywhere, task_type, location, duration, value=1):
        self.task_id = task_id
        self.title = title
        self.description = desc
        self.creator = creator
        self.in_out_everywhere = in_out_everywhere  # in / out / everywhere
        self.task_type = task_type          # sport & body / be good / adventures / waste my time / culture
        self.location = location
        self.duration = duration
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

    def get_in_out_everywhere(self):
        return self.in_out_everywhere

    def get_type(self):
        return self.task_type

    def get_loc(self):
        return self.location

    def get_duration(self):
        return self.duration

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


