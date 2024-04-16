import json
import redis

redis_host = "redis"  # Replace with your Redis server hostname/IP
redis_port = 6379  # Replace with your Redis server port (default)

redis_client = redis.Redis(host=redis_host, port=redis_port)

def add_domain_to_redis(domain,payload):
    """
    Adds the domain as a key and "Job Started" as the value to the Redis database.

    Args:
        domain (str): The domain name to add to Redis.
    """

    redis_client.set(domain, payload)

def get_domain_data(domain):
    domain_data = redis_client.get(domain)

    if domain_data == None:
        domain_data = {
            "status" : f"Not initiated for {domain}",
            "domain" : domain
                }
    else:
        domain_data = json.loads(domain_data)

    return domain_data
