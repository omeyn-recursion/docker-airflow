# import requests
# import json
# import os

# #JOB DETAILS
# SLURM_TOKEN = 'my_super_secret_token' #logon to biohive, use 'scontrol token username=$(whoami)|tr '=' ' '| awk '{print $2}'' to get token
# username="joshua.fryer"
# job_name="Hello_World"
# partition="batch"
# std_out="/tmp/hello_world.out" #This is the std out path that the job host node will see
# std_err="/tmp/hello_world.err" #This is the std err path that the job host node will see 
# task_per_node="1"
# memory=2000

# #Script Data
# job_script = """#!/bin/bash

# # This is your job script, which includes your actual commands
# hostname
# echo "Hello World!" 
# sleep 120

# """

# SLURM_ENDPOINT="http://172.20.100.254:6820/slurm/v0.0.36/job/submit"
# SLURM_USER=username
# headers = {
#     "X-SLURM-USER-TOKEN": f'{SLURM_TOKEN}',
#     "X-SLURM-USER-NAME": f'{SLURM_USER}',
#     "Content-Type": "application/json"
# }

# data = {
#     "script": job_script,
#     "job": {
#         "name": f"{job_name}",
#         "partition": f"{partition}",
#         "standard_output": f"{std_out}",
#         "standard_error": f"{std_err}",
#         "tasks_per_node": f"{task_per_node}",
#         "memory_per_node": f"{memory}",
#         "environment": {"PATH": f"/mnt/ps/home/CORP/{username}/.local/bin:/mnt/ps/home/CORP/{username}/.pyenv/plugins/pyenv-virtualenv/shims:/mnt/ps/home/CORP/{username}/.pyenv/shims:/mnt/ps/home/CORP/{username}/.pyenv/bin:/mnt/ps/apps/easybuild/easybuild/software/Go/1.19.4/bin:/cm/local/apps/python3/bin:/mnt/ps/apps/easybuild/easybuild/software/gcloud/410.0.0/bin:/cm/local/apps/cuda/libs/current/bin:/cm/shared/apps/cuda11.8/sdk/11.8.0/bin/x86_64/linux/release:/cm/shared/apps/cuda11.8/toolkit/11.8.0/bin:/cm/shared/apps/slurm/current/sbin:/cm/shared/apps/slurm/current/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/lpp/mmfs/bin:.:/opt/TurboVNC/bin/"}
#     }
# }

# response = requests.request("POST", SLURM_ENDPOINT, headers=headers, data=json.dumps(data))

# print(response.text)
