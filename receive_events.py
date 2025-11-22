import asyncio
from azure.eventhub.aio import EventHubConsumerClient

CONNECTION_STR = "Endpoint=sb://vyuha-eventhubs.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=0ONi4q5aX9LuxzCltuUMiMSf8p5JX4bwK+AEhBoejy8="
EVENTHUB_NAME = "Vyuha-EventHubs"

async def on_event(partition_context, event):
    print(f"Received event from partition {partition_context.partition_id}: {event.body_as_str()}")
    await partition_context.update_checkpoint(event)

async def main():
    consumer = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        consumer_group="$Default",
        eventhub_name=EVENTHUB_NAME
    )

    async with consumer:
        print("Listening for events...\n")
        await consumer.receive(
            on_event=on_event,
            starting_position="-1"  # From beginning
        )

if __name__ == "__main__":
    asyncio.run(main())
