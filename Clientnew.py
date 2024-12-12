import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = '127.0.0.1'  # Use localhost or 127.0.0.1 for local testing
port = 9999

# Connect to the server
s.connect((host, port))

# Start the interaction with the server
while True:
    print("""Select one of the following options:
           1. Incident
           2. Change
           3. Jira
           4. Exit
    """)

    choice = input("Please select one of the following options (1/2/3/4): ")

    if choice == '4':  # Exit condition
        print("Closing connection to the server.")
        s.send(choice.encode('ascii'))
        s.close()
        break

    # Send the selected option to the server
    s.send(choice.encode('ascii'))

    # Receive the server's response
    msg = s.recv(1024)
    print(f"Server response: {msg.decode('ascii')}")

    # If the server asks for the ticket/change/Jira number
    if "Please enter" in msg.decode('ascii'):
        number = input(msg.decode('ascii'))
        s.send(number.encode('ascii'))

        # Receive and display the status of the ticket/change/Jira
        msg = s.recv(1024)
        print(f"Server response: {msg.decode('ascii')}")
