Results are in output folder:

How to read the filename:
out-<typeof_storage>-<file_size>-<numberof_lambdas>-<numberof_run>.txt

e.g. out-efs-50-10-1.txt means the storage type is efs, the results show a 50MB file transfer where 10 lambdas are running in parallel. the result is for the first run. 

How to read the result in the file:
Inside the above example file (out-efs-50-10-1.txt)- 

Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03223919868469238 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.036368370056152344 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03244185447692871 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03184390068054199 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.04052591323852539 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03232383728027344 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.0312039852142334 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03130626678466797 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03375387191772461 seconds
Lambda response body: Accessed filesize: 50 MB for Lambdas: 10 in 0.03421664237976074 seconds

It tells how much time each of the 10 lambdas take to transfer(s3)/ or read the first byte(efs) from each of the filesystem.
