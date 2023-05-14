import os
from google.cloud import pubsub_v1
from config import Config

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/usr/src/app/linen-mason-384315-d051f5f132d3.json'

publisher = pubsub_v1.PublisherClient()

topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=Config.GOOGLE_CLOUD_PROJECT,
    topic='compress', 
)

def compress(file_id, type_task):
    data_str = f"file {file_id} to type_task {type_task}"
    data = data_str.encode("utf-8")
    future = publisher.publish(topic_name, data, file_id=str(file_id), type_task=str(type_task))
    future.result()
