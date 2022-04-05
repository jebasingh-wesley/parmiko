import paramiko

hostname = "192.168.0.126"
username = "ubuntu"
password = "ubuntu"

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# read the BASH script content from the file
#bash_script = open("script.sh").read()

#stdin, stdout, stderr = client.exec_command("ls")

# execute the BASH script
stdin, stdout, stderr = client.exec_command("/bin/sh -c /home/ubuntu/Documents/script.sh")
# read the standard output and print it
print(stdout.read().decode())
# print errors if there are any
err = stderr.read().decode()
if err:
    print(err)
# close the connection
client.close()
