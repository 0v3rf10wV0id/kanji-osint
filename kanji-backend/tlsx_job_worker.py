from pubsub import subscribe_channel,publish_message
from redishelper import add_domain_to_redis,get_domain_data
import json
from container_helper import run_container
from jsonl_to_csv import convert_to_csv
import re

# Replace with your actual channel name
channel_name = "enrich-resolve-jobs"

channel_listener = subscribe_channel(channel_name)

print("Started TLSX Worker")

for message in channel_listener():
    if type(message["data"]) != int:
        job = json.loads(message["data"])
        print(f"[RESOLVE] Resolving domains for {job['domain']} using tlsx")
        print(job)
        resolve_res = run_container(f"tlsx -l outputs/{job['dnsx_filename']} -o outputs/{job['domain']}-tslx-resolved.jsonl -ex -ss -mm -re -un -j --silent")[:-1]
        print(f"[DONE] Resolved {len(resolve_res)} domains using tlsx. ")
        convert_to_csv(f"outputs/{job['domain']}-tslx-resolved.jsonl",f"outputs/{job['domain']}-tlsx-resolved.csv")

        job = get_domain_data(job['domain'])
        job["tlsx_filename"] = job['domain']+"-tlsx-resolved.csv"
        job_domain = job['domain']
        job = json.dumps(job)
        add_domain_to_redis(job_domain, job)
        # publish_message("tlsx-jobs", job)
