import datetime
import socket
import ssl
import yagmail 

port = '443'
context = ssl.create_default_context()
f = open("urlList.txt", "r")
for x in f:
    hostname = x
    hostname = hostname.strip("\n")
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            certificate = ssock.getpeercert()
            certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
    daysToExpiration = (certExpires - datetime.datetime.now()).days
    print(daysToExpiration)

yagmail.SMTP(me, password).send(to, '请注意证书的更新！', '以下是证书到期时间：' + certExpires +hostname)
