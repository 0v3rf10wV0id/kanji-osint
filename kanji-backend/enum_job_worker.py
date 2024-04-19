from pubsub import subscribe_channel,publish_message
import json
from redishelper import add_domain_to_redis
from container_helper import run_container
import os

channel_name = "enum-jobs"

channel_listener = subscribe_channel(channel_name)

print("Started Enum Worker")

for message in channel_listener():
    if type(message["data"]) != int:
        job = json.loads(message["data"])
        print(f"[ENUM]Generating sub domains for {job['domain']}")
        enum_result = run_container(
                f"subfinder -d {job['domain']} -o outputs/{job['domain']}-subdomains.txt -silent"
                )[:-1]
        print(f"[DONE] Enumerating for {job['domain']}. Found {len(enum_result)} domains.")
        payload = json.dumps({
                "status" : "Resolvers",
                "subdomain_filename" : f"{job['domain']}-subdomains.txt",
                "domain" : job['domain']
            })
        add_domain_to_redis(job['domain'], payload)
        publish_message("dnsx-jobs", payload)


