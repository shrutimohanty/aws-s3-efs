# Results Analysis Guide

## Overview

This document provides guidance on understanding the results generated from the parallel execution of AWS Lambda functions for file transfers to S3 and reads from EFS. The outcomes of these operations are saved in a structured format within the `output` folder. 

## File Naming Convention

The output files are named according to the following pattern: 

`out-<typeof_storage>-<file_size>-<numberof_lambdas>-<numberof_run>.txt`

### Example

For instance, the file `out-efs-50-10-1.txt` follows the naming convention as detailed below:

- **Storage Type**: `efs` indicates that the operations were performed on Amazon Elastic File System.
- **File Size**: `50` represents the size of the file in megabytes used in the operation.
- **Number of Lambdas**: `10` signifies that ten Lambda functions were invoked in parallel for the operation.
- **Run Number**: `1` denotes this as the first set of operations or 'run'.

## Understanding the Results

Inside each output file, the results detail the execution time for each Lambda function involved in the operation. Here is how to interpret the results found in the files, using `out-efs-50-10-1.txt` as an example:

```
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03223919868469238 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.036368370056152344 seconds
...
```

Each line corresponds to the outcome of a single Lambda function execution, providing a granular view of the performance across all functions involved. The timing information (`e.g., 0.03223919868469238 seconds`) indicates how long it took for the Lambda function to complete its assigned task, which could be transferring a file to S3 or reading the first byte from a file in EFS.

### Key Takeaways

- **Performance Insights**: These results offer insights into the performance and efficiency of parallel Lambda function executions for file operations on AWS S3 and EFS.
- **Operation Specifics**: For S3, the timing reflects the file transfer process. For EFS, it denotes the time taken to read the first byte of the file, providing a measure of the file system's responsiveness and the Lambda function's read performance.
- **Parallel Execution Analysis**: By analyzing the execution times across multiple Lambda functions, you can assess the scalability and concurrency benefits of using AWS Lambda for file operations on S3 and EFS.

This guide should help you navigate and interpret the results stored in the `output` folder effectively, offering valuable insights into your AWS Lambda functions' file operation performance.
