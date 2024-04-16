import redis

r = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)
rpb = r.pubsub()
def subscribe_channel(channel):
    rpb.subscribe(channel)
    return rpb.listen
    # for message in rpb.listen():
    #     print(message) # <-- you can literally do any thing with this message i am just printing it

def publish_message(channel,message):
    r.publish(channel, message)
