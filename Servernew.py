import socket

# Create a socket object
print("I am server. I am starting a new stream for any queries:")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = '127.0.0.1'
port = 9999

# Bind to the port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

clientsocket, addr = serversocket.accept()
print("=======> ", clientsocket, addr)
print("Got a connection from %s" % str(addr))

# Predefined ticket numbers (this can be extended)
openincidents = ['tick1234', 'tick5689', 'tick9999']
resolvedincidents = ['tick2222', 'tick6666', 'tick1111']
inprogressincidents = ['tick3333', 'tick0000', 'tick7777']

while True:
    # Ask for the option from the client
    q = clientsocket.recv(2048)
    print("***************> ", q, type(q))
    qs = q.decode('ascii')
    print("========> ", qs, type(qs))

    if qs == '1':  # Mapping number '1' to 'Incident'
        msg = "You selected Incident. Please enter the incident number:"
        clientsocket.send(msg.encode('ascii'))

        # Wait for the incident number
        incident_number = clientsocket.recv(2048).decode('ascii')
        if incident_number in openincidents:
            msg = f"Ticket {incident_number} is in Open status. Please wait while we assign it to an executive."
        elif incident_number in resolvedincidents:
            msg = f"Ticket {incident_number} has been resolved. Thanks for contacting the help desk."
        elif incident_number in inprogressincidents:
            msg = f"Ticket {incident_number} is in Progress. We will resolve it in 2-3 days."
        else:
            msg = "Ticket number not recognized."

        clientsocket.send(msg.encode('ascii'))

    elif qs == '2':  # Mapping number '2' to 'Change'
        msg = "You selected Change. Please enter the change number:"
        clientsocket.send(msg.encode('ascii'))

        # Wait for the change number
        change_number = clientsocket.recv(2048).decode('ascii')
        msg = f"Change request {change_number} is being processed."
        clientsocket.send(msg.encode('ascii'))

    elif qs == '3':  # Mapping number '3' to 'Jira'
        msg = "You selected Jira. Please enter the Jira number:"
        clientsocket.send(msg.encode('ascii'))

        # Wait for the Jira number
        jira_number = clientsocket.recv(2048).decode('ascii')
        msg = f"Jira task {jira_number} is in progress."
        clientsocket.send(msg.encode('ascii'))

    elif qs == '4':  # Exit option
        msg = "You selected Exit. Closing connection."
        clientsocket.send(msg.encode('ascii'))
        break  # Exit the loop and close connection

    else:
        msg = "Not able to understand your option."
        clientsocket.send(msg.encode('ascii'))

clientsocket.close()
