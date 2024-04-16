from pubsub import subscribe_channel

channel_listener = subscribe_channel("enum-jobs")

for message in channel_listener():
    print(message)
