import paramiko
from scp import SCPClient

# Read server IPs or hostnames from a file (one per line)
with open('servers.txt', encoding='utf-8') as f:
    servers = [line.strip() for line in f if line.strip()]

username = 'leo'  # Replace with your SSH username
ssh_key_path = '/path/to/your/private/key'  # e.g., '~/.ssh/id_rsa'
local_file = '/path/to/local/file.txt'
remote_path = '/remote/path/file.txt'

for server in servers:
    print(f'Transferring to {server}...')
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())     # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  This line tells Paramiko what to do when the SSH server's host key is not known (i.e., it's not in your known_hosts file).
        ssh.connect(server, username=username, key_filename=ssh_key_path)
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(local_file, remote_path)
        ssh.close()
        print(f'Successfully transferred to {server}')
    except (paramiko.SSHException, FileNotFoundError, OSError) as e:
        print(f'Failed to transfer to {server}: {e}')



# This code reads server addresses from a file called servers.txt, with each server on a separate line. Here’s a breakdown:

# with open('servers.txt', encoding='utf-8') as f:
# Opens the file servers.txt for reading, using UTF-8 encoding. The with statement ensures the file is properly closed after reading.

# servers = [line.strip() for line in f if line.strip()]
# This is a list comprehension that:

# Reads each line from the file.
# Removes leading/trailing whitespace with strip().
# Ignores empty lines (if line.strip()).
# Collects all non-empty, stripped lines into the servers list.
# Result:
# servers will be a list of all server hostnames/IPs from the file, ready for use in your script.
