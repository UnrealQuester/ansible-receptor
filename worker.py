#!/home/avbudden/.pyenv/shims/python
from ansible_runner.streaming import Worker
import os
import sys
import json

class MyWorker(Worker):
    def event_handler(self, event_data):
        if "stdout" in event_data and event_data["stdout"]:
            print(event_data["stdout"], flush=True)

    def status_handler(self, status_data, runner_config):
        if "status" in status_data:
            print(status_data["status"], flush=True)

    def finished_callback(self, runner_obj):
        print("FINISHED")
        return
        print(runner_obj.config.fact_cache)
        for file in os.listdir(runner_obj.config.fact_cache):
            print(file)
            file = os.path.join(runner_obj.config.fact_cache, file)
            with open(file) as file:
                print(json.load(file))

devnull = open(os.devnull, "bw")

runner = MyWorker(_output=devnull)
runner.run()