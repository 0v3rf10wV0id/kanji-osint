from pubsub import subscribe_channel,publish_message
from redishelper import add_domain_to_redis
import json
from container_helper import run_container

# Replace with your actual channel name
channel_name = "dnsx-jobs"

channel_listener = subscribe_channel(channel_name)

print("Started DNSX Worker")

for message in channel_listener():
    if type(message["data"]) != int:
        job = json.loads(message["data"])
        print(f"[RESOLVE] Resolving domains for {job['domain']} using dnsx")
        resolve_res = run_container(f"dnsx -l outputs/{job['subdomain_filename']} -o outputs/{job['domain']}-dns-resolved.txt --silent")[:-1]
        print(f"[DONE] Resolved {len(resolve_res)} domains using dnsx. ")
        job["dnsx_filename"] = job['domain']+"-dns-resolved.txt"
        job_domain = job['domain']
        job = json.dumps(job)
        add_domain_to_redis(job_domain, job)
        publish_message("enrich-resolve-jobs", job)
