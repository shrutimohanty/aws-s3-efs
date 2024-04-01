import boto3
import concurrent.futures
import json
import sys

# Initialize a boto3 client
region = "us-east-1"
lambda_client = boto3.client('lambda',region_name = region)

def invoke_lambda_sync(function_name, payload):
    """
    Invoke a Lambda function synchronously

    :param function_name: The name of the Lambda function to invoke
    :param payload: The payload to send to the Lambda function
    """
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',  # Use 'RequestResponse' for synchronous execution
        Payload=json.dumps(payload)
    )
    # Read the response payload
    response_payload = json.load(response['Payload'])
    return response_payload

def main():
    
    id_size = int(sys.argv[1])
    # Number of parallel invocations
    num_invocations = int(sys.argv[2])
    s3_efs = sys.argv[3]
    
    if s3_efs == 's3':
        # Name of your Lambda function
        function_name = 'arn:aws:lambda:us-east-1:966908692461:function:s3-download-1'
    else:
        # Name of your Lambda function
        function_name = 'arn:aws:lambda:us-east-1:966908692461:function:efs-read-files-1'
        
    
    # Payload to send to your Lambda function (example payload)
    payload = {
        'id_size': id_size,  # Example size, adjust as necessary
        'id_lambdas': num_invocations  # Example number of lambdas, adjust as necessary
    }
    
    

    # Use a ThreadPoolExecutor to invoke the Lambda function in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_invocations) as executor:
        # Prepare a list of futures
        futures = [executor.submit(invoke_lambda_sync, function_name, payload) for _ in range(num_invocations)]
        
        # Wait for the futures to finish and get their results
        for future in concurrent.futures.as_completed(futures):
            try:
                response_payload = future.result()
                print("Lambda response body:", response_payload.get('body'))
            except Exception as e:
                print("Error invoking Lambda:", e)

if __name__ == '__main__':
    main()
