from receptorctl import ReceptorControl
import ansible_runner
import io

output = io.BytesIO()
output.name = "output"
runner = ansible_runner.run(private_data_dir="project", playbook="playbook.yaml", streamer="transmit", _output=output)

print(output.getvalue())

receptor = ReceptorControl("tcp://localhost:2307")
res = receptor.submit_work("ansible", output.getvalue(), "executor", params={"params": "test"}, )
print(res)

jobid = res['unitid']

res = receptor.get_work_results(jobid)
for line in res:
    print(line.decode(), end="")