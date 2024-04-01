def create_file(filename, size_in_mb):
    """
    Create a file of a specific size in MB

    :param filename: The name of the file to create
    :param size_in_mb: The size of the file in megabytes
    """
    with open(filename, 'wb') as f:
        f.write(b'\0' * size_in_mb * 1048576)  # Write null bytes to achieve the desired file size

# Create files of 50MB, 100MB, and 500MB
create_file('50MB_file.bin', 50)
create_file('100MB_file.bin', 100)
create_file('500MB_file.bin', 500)

print("Files created successfully.")
