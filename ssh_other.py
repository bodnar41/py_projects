import paramiko

user = "Márk"
pwd = "****"
ip = "localhost"
cmd = "wmic cpu get name"



def ssh_comm(ip, usr, pwd, cmd):
    print("Creating SSH Client..")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("Connection..")
    ssh_client.connect(hostname=ip,username=usr,password=pwd)

    print("Command execution..")
    stdin,stdout,stderr = ssh_client.exec_command(cmd)

    print("Command executed..")
    stdout = stdout.readlines()

    with open("info.txt", "a") as f:
            k = str(stdout).replace("\r", "")
            f.write(k)

    print(stdout)
    ssh_client.close()

ssh_comm(ip, user, pwd, cmd)

