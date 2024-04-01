import time
import sys,os
import boto3
import json

TMP="/tmp/"



s3_client = boto3.client('s3')
INPUTBUCKET = 'sized-files-bucket-1'

def lambda_handler(event, context):
    # Delete temp files
    for file in os.listdir(TMP):
        if file.startswith("100MB_file") or file.startswith("500MB_file") or file.startswith("50MB_file"):
            os.remove(os.path.join(TMP, file))
    
    filesize = event['id_size']
    num_lambdas = event['id_lambdas']

    filename = ''
    if filesize == 50:
        filename = '50MB_file.bin'
    elif filesize == 100:
        filename = '100MB_file.bin'
    elif filesize == 500:
        filename = '500MB_file.bin'
    
    # Ensure filename is not empty
    if filename:
        download_s3_time_start = time.time()
        s3_client.download_file(INPUTBUCKET, filename, os.path.join(TMP, filename))  # S3
        download_s3_time_end = time.time()

        s3_download_time = download_s3_time_end - download_s3_time_start
        print(f"Downloaded filesize: {filesize} MB for Lambdas: {num_lambdas} from S3 in {s3_download_time} seconds")
        return {
        'statusCode': 200,
        'body': f"Downloaded filesize: {filesize} MB for Lambdas: {num_lambdas} from S3 in {s3_download_time} seconds"
        }
    else:
        print("Invalid filesize provided.")

        return {
            'statusCode': 200,
            'body': f"Invalid filesize provided."
        }