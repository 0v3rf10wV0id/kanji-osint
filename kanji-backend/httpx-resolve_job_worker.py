from pubsub import subscribe_channel,publish_message
from redishelper import add_domain_to_redis, get_domain_data
import json
from container_helper import run_container
import re

# Replace with your actual channel name
channel_name = "enrich-resolve-jobs"

channel_listener = subscribe_channel(channel_name)

print("Started HTTPX Worker")

for message in channel_listener():
    if type(message["data"]) != int:
        job = json.loads(message["data"])
        print(f"[RESOLVE] Resolving domains for {job['domain']} using httpx")
        print(job)
        resolve_res = run_container(f"httpx -l outputs/{job['dnsx_filename']} -o outputs/{job['domain']}-http-resolved.csv -td -sc -nc -mc 200,302,403 -ip -csv --silent")[:-1]
        print(f"[DONE] Resolved {len(resolve_res)} domains using httpx. ")
        job = get_domain_data(job['domain'])
        job["httpx_filename"] = job['domain']+"-http-resolved.csv"
        job_domain = job['domain']
        job = json.dumps(job)
        add_domain_to_redis(job_domain, job)
        # publish_message("tlsx-jobs", job)
