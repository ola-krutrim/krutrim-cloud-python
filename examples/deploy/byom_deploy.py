from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
import os

load_dotenv()

client = KrutrimCloud().deploy

bucket_name = "<your-bucket-name>"  # "my-bucket-name"
model_id = "<your-model-name>"  # "my_model_name"
version = "<model-version>"  # "v1" <- without '.' in version string

try:
    s3_path = f"s3://{bucket_name}/{model_id}/{version}"
    deploy_response = client.tasks.create(
        model=model_id,
        path=s3_path,
        s3_endpoint=os.environ.get("KRUTRIM_CLOUD_S3_BUCKET_ENDPOINT"),  # type: ignore
        s3_access_key=os.environ.get("KRUTRIM_CLOUD_S3_PUBLIC_KEY"),  # type: ignore
        s3_secret=os.environ.get("KRUTRIM_CLOUD_S3_SECRET_KEY"),  # type: ignore
        s3_region=os.environ.get("KRUTRIM_CLOUD_S3_REGION"),
    )
    deploy_model_name = deploy_response.name
    deploy_task_id = deploy_response.id

    print(f"Deployed Model Name: {deploy_model_name}")
    print(f"Deploy Task ID: {deploy_task_id}")

    retrieve_response = client.tasks.retrieve(id=deploy_task_id)  # type: ignore
    print(f"Deploy Task Status: {retrieve_response.status}")
    print("*" * 100)

    task_list = client.tasks.list().task_list
    for task in task_list:
        print(f"Task ID: {task['id']} | Status: {task['status']}")

    # Cancel Task
    client.tasks.cancel(deploy_task_id)

except Exception as exc:
    print(f"Exception: {exc}")
