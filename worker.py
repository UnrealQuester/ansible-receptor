#!/home/avbudden/.pyenv/shims/python
from ansible_runner.streaming import Worker
import os

class MyWorker(Worker):
    def event_handler(self, event_data):
        if "stdout" in event_data and event_data["stdout"]:
            print(event_data["stdout"], flush=True)

    def status_handler(self, status_data, runner_config):
        if "status" in status_data:
            print(status_data["status"], flush=True)

    def finished_callback(self, runner_obj):
        print("FINISHED")

devnull = open(os.devnull, "bw")

runner = MyWorker(_output=devnull)
runner.run()