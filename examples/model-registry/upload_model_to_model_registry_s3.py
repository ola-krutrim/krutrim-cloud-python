from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

load_dotenv()

client = KrutrimCloud().registry.model_registry

bucket_name = "<your-bucket-name>"  # "my-bucket-name"
local_directory = "<local-dirpath-to-upload-files>"  # "./model"
model_name = "<your-model-name>"  # "my_model_name"
version = "<model-version>"  # "v1" <- without '.' in version string

try:
    files = client.list_model_files(bucket_name, model_name, version)
    print(f"Initially Files List: {files}")
    print("*" * 100)

    client.upload_files_to_s3(
        local_dir_path=local_directory,
        bucket_name=bucket_name,
        model_id=model_name,
        version=version,
    )

    model_id = client.fetch_model_id(model_name)
    print(f"Model ID: {model_id}")

    model_name = client.fetch_model_name(model_id)
    print(f"Model Name: {model_name}")

    files = client.list_model_files(bucket_name, model_name, version)
    print(f"After uploading, Files List: {files}")

    print("*" * 100)
    print("Downloading...")
    client.download_files(bucket_name, model_name, version, "./output_dir")

    print("*" * 100)
    print(f"Check Versions List in S3: {client.list_model_version(bucket_name, model_name)}")
except Exception as exc:
    print(exc)
