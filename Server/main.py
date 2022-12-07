import socket
import comunicazione


print ('avvio server')
HOST = '127.0.0.1' 
PORT = 8080
s = socket.socket() #senza parametri protocollo tcp-ip
s.bind((HOST, PORT))
flag=true

while flag:
    s.listen()
    conn, addr = s.accept()
    with conn:
        x = threading.Thread(target=comunicazione.thread_comunicazione, args=(conn,))
        x.start()
        
s.close()    
print('Fine programma')