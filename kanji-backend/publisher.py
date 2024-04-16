from pubsub import publish_message
import sys

def start_enumeration_job(url):
    print(f"Starting enumeration on domain : {url}")
    job = {
        "domain" : url
            }
    publish_message("enum-jobs", job)

start_enumeration_job(sys.argv[1])
