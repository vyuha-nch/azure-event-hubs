from azure.eventhub import EventHubProducerClient, EventData

CONNECTION_STR = "Endpoint=sb://vyuha-eventhubs.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=0ONi4q5aX9LuxzCltuUMiMSf8p5JX4bwK+AEhBoejy8="
EVENTHUB_NAME = "trial_eventhub"

try:
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        eventhub_name=EVENTHUB_NAME
    )
    print("Connection successful!")
except Exception as e:
    print("Error:", e)

with producer:
    # create a small batch
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData("Test message"))
    producer.send_batch(event_data_batch)
    print("Event sent successfully!")
