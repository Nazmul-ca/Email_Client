from socket import *
import ssl
import base64


mailserver = 'smtp.gmail.com'
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect((mailserver, 465))
recv = clientSocket.recv(1024)
print(recv.decode())
if recv[:3].decode() != '220':
    print('220 reply not received from server.')

#Send HELO command and print server response
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1.decode())
if recv1[:3].decode() != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Start, end
# command = "STARTTLS\r\n"
# clientSocket.send(command.encode())
# recvdiscard = clientSocket.recv(1024)
# print(recvdiscard.decode())


id = base64.b64encode(bytes('nazmul.kuet@gmail.com', 'utf-8')).decode()+'\r\n'
password = base64.b64encode(bytes('09007601', 'utf-8')).decode()+'\r\n'
clientSocket.send('AUTH LOGIN\r\n'.encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())
clientSocket.send(id.encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())
clientSocket.send(password.encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())

clientSocket.send("MAIL From: <nazmul.kuet@gmail.com>\r\n".encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())

clientSocket.send("RCPT TO: <nazmul.kuet@gmail.com>\r\n".encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())

clientSocket.send("DATA\r\n".encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())

print("Sending Data...")
clientSocket.send("SUBJECT: SMTP Test\r\n".encode())
clientSocket.send("Hi\n Test OK\r\n".encode())
clientSocket.send(".\r\n".encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
