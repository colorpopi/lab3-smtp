from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mail_server = "127.0.0.1:1025"
    # port_num = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv_1 = clientSocket.recv(1024).decode()
    #print(recv1) 

    # Send MAIL FROM command and handle server response.
    # Fill in start
    email_from = "MAIL FROM: <dam693@nyu.edu>\r\n"
    clientSocket.send(email_from.encode())
    recv_2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    rcpt = "RCPT TO: <dam693@nyu.edu>\r\n"
    clientSocket.send(rcpt.encode())
    recv_3 = clientSocket.recv(1024).decode()
    # Fill in start
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = "DATA: \r\n"
    clientSocket.send(data.encode())
    recv_4 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    mail_subject = "Subject: SMPT Test\r\n"
    clientSocket.send(mail_subject.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    get_msg = clientSocket.recv(1024).decode()
    # Fill in start
    # Fill in end
    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    clientSocket.send("QUIT \r\n".encode())
    quit_msg = clientSocket.recv(1024.decode())
    clientSocket.close()
    # Fill in start
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')