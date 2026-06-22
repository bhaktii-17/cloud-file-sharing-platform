import boto3

BUCKET_NAME = "bhakti-file-sharing-platform"

s3 = boto3.client("s3")

def upload_file(file_obj, filename):
    s3.upload_fileobj(file_obj, BUCKET_NAME, filename)

def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if "Contents" not in response:
        return []

    return [obj["Key"] for obj in response["Contents"]]

def generate_download_url(filename):
    return s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": filename
        },
        ExpiresIn=3600
    )
def delete_file(filename):
    s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=filename
    )
