import logging
import boto3
from botocore.exceptions import ClientError


region = "us-east-1"
s3_client = boto3.client('s3')



def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True



upload_file_to_s3('50MB_file.bin', INPUTBUCKET)
upload_file_to_s3('100MB_file.bin', INPUTBUCKET)
upload_file_to_s3('500MB_file.bin', INPUTBUCKET)
