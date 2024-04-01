import os
import time

# Assuming your Lambda function's EFS is mounted at /mnt/efs
EFS_MOUNT_PATH = '/mnt/efs'

def lambda_handler(event, context):
    # Define the file name based on the size provided in the event
    filesize = int(event['id_size'])
    num_lambdas = int(event['id_lambdas'])

    if filesize == 50:
        filename = '50MB_file.bin'
    elif filesize == 100:
        filename = '100MB_file.bin'
    elif filesize == 500:
        filename = '500MB_file.bin'
    else:
        print("Invalid filesize provided.")
        return {'statusCode': 400, 'body': 'Invalid filesize provided.'}

    file_path = os.path.join(EFS_MOUNT_PATH, filename)

    # Time the file access (read) operation
    access_time_start = time.time()
    
    # Assuming you just want to access (e.g., read) the file to simulate a download
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()  # Or perform another operation that suits your needs
        access_time_end = time.time()

        access_time = access_time_end - access_time_start
        print(f"Accessed filesize: {filesize} MB for Lambdas: {num_lambdas} in {access_time} seconds")
        return {
            'statusCode': 200,
            'body': f"Accessed filesize: {filesize} MB for Lambdas: {num_lambdas} in {access_time} seconds"
        }
    else:
        print(f"File not found: {file_path}")
        return {'statusCode': 404, 'body': 'File not found.'}
