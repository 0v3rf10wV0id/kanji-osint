from pubsub import publish_message
import sys
import json

def start_enumeration_job(url):
    print(f"Starting job on {url}")
    job = {"domain" : url}
    publish_message("enum-jobs",json.dumps(job))

start_enumeration_job(sys.argv[1])
