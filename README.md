# Customer Support Ticket Management System

This project simulates a simple **Customer Support Ticket Management System** using Python sockets for communication between a server and a client. It allows users (clients) to query the status of their tickets (Incident, Change, Jira) and receive responses from the server.

## Features
- Server listens for incoming client connections.
- Client sends queries about ticket statuses.
- Server provides ticket statuses based on predefined lists:
  - **Open**
  - **In Progress**
  - **Resolved**
- Supports multiple types of tickets: Incident, Change, Jira.
- Allows clients to exit the session gracefully.

## How It Works
1. The server runs and waits for client connections.
2. The client connects to the server and selects a ticket type.
3. The client provides the ticket number for the selected type.
4. The server checks the ticket status from predefined lists and responds.
5. The client can repeat the process or exit.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of Python sockets.

## Files
1. **server.py**
   - Contains the server-side code.
   - Handles incoming client connections.
   - Processes client queries and sends responses.

2. **client.py**
   - Contains the client-side code.
   - Allows users to interact with the system by sending queries to the server.

## Usage

### Step 1: Start the Server
Run the server script first. This will make the server listen on a specified port for incoming connections.

```bash
python server.py
```

You should see output like:
```
I am server. I am starting a new stream for any queries:
Got a connection from ('127.0.0.1', 50593)
```

### Step 2: Start the Client
Open another terminal and run the client script. This will connect the client to the server.

```bash
python client.py
```

You will see a menu to select an option:
```
Select one of the following options:
   1. Incident
   2. Change
   3. Jira
   4. Exit

Please select one of the following options (1/2/3/4):
```

### Step 3: Interact
- Select a type (Incident, Change, Jira) by entering the corresponding number.
- Provide the ticket number when prompted.
- Receive the ticket status from the server.
- Select **4 (Exit)** to close the connection.

## Example Interaction
### Client:
```
Select one of the following options:
   1. Incident
   2. Change
   3. Jira
   4. Exit

Please select one of the following options (1/2/3/4): 1
Server response: You selected Incident. Please enter the incident number:
```

### Server:
```
Got a connection from ('127.0.0.1', 50593)
***************> b'1' <class 'bytes'>
========> 1 <class 'str'>
***************> b'tick1234' <class 'bytes'>
========> tick1234 <class 'str'>
```

## Implementation Details

### Server Logic
- Maintains three lists of tickets: `openincidents`, `resolvedincidents`, and `inprogressincidents`.
- Accepts a connection from the client.
- Processes ticket number queries and responds with appropriate statuses.

### Client Logic
- Connects to the server and sends queries.
- Displays menu options for ticket types.
- Receives and displays server responses.
- Provides an option to exit the session.

## Requirements
- Python 3.x

## Installation
1. Clone the repository or copy the files.
2. Run the `servernew.py` script to start the server.
3. Run the `clientnew.py` script to interact with the server.

## License
This project is open-source and available for modification and redistribution.

---

