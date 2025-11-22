from azure.eventhub import EventHubProducerClient, EventData

# Replace with your Event Hubs Namespace connection string
CONNECTION_STR = "Endpoint=sb://vyuha-eventhubs.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=0ONi4q5aX9LuxzCltuUMiMSf8p5JX4bwK+AEhBoejy8="
EVENTHUB_NAME = "Vyuha-EventHubs"

def run():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        eventhub_name=EVENTHUB_NAME
    )

    with producer:
        event_batch = producer.create_batch()

        event_batch.add(EventData("First event"))
        event_batch.add(EventData("Second event"))
        event_batch.add(EventData("Third event"))

        print("Sending events...")
        producer.send_batch(event_batch)
        print("Events sent!")

if __name__ == '__main__':
    run()
