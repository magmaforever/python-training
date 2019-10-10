import paramiko

# 创建一个ssh的客户端，用来连接服务器：
ssh = paramiko.SSHClient()
# 创建一个ssh的白名单：
know_host = paramiko.AutoAddPolicy()
# 加载创建的白名单
ssh.set_missing_host_key_policy(know_host)

# 连接服务器：
ssh.connect(hostname="172.16.100.2",
            port=22,
            username="admin1",
            password="Admin@123")

# 执行测试命令
stdin, stdout, stderr = ssh.exec_command("display version")
print(stdout.read().decode())
ssh.close()
