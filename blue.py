#server
import bluetooth

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server.bind(("", 1))
server.listen(1)

print("Waiting for client...")

client, address = server.accept()
print("Connected:", address)

while True:
    data = client.recv(1024)
    print("Received:", data)

client.close()
server.close()


#client
import bluetooth

bd_addr = "B8:27:EB:87:EB:3E"
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

while True:
    text = input("Enter a message: ")
    sock.send(text)

sock.close()