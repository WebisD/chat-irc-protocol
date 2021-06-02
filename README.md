<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/WebisD/chat-irc-protocol">

  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/WebisD/chat-irc-protocol">
  
  <a href="https://github.com/WebisD/chat-irc-protocol/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/WebisD/chat-irc-protocol">
  </a>
  
   <img alt="GitHub" src="https://img.shields.io/github/license/WebisD/chat-irc-protocol">
</p>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/WebisD/chat-irc-protocol">
    <img src=".github/logo.png" alt="Logo" width="550">
  </a>
</p>

<p align="center">
  <img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"/>
  <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#-documentation">Documentation</a>
    </li>
    <li>
      <a href="#-how-to-run">How To Run</a>
    </li>
    <li>
      <a href="#-commands">Commands</a>
        <ul>
          <li><a href="#-help">Help</a></li>
          <li><a href="#%EF%B8%8F-register">Register</a></li>
          <li><a href="#-login">Login</a></li>
          <li><a href="#-create">Create</a></li>
          <li><a href="#-list-room">Listroom</a></li>
          <li><a href="#-join">Join</a></li>
          <li><a href="#-message">Message</a></li>
          <li><a href="#-list-users">Listusers</a></li>
          <li><a href="#-leave">Leave</a></li>
          <li><a href="#-logout">Logout</a></li>
          <li><a href="#-quit">Quit</a></li>
        </ul>
    </li>
    <li>
      <a href="#-authors">Authors</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 💻 About The Project
In this project, we implemented a chat application mirroring that of discord's and whatsapp's main feature: a room to chat with friends.

Our application runs on the terminal using *telnet*.

Our application server was implemented according to the [RFC 1459](https://datatracker.ietf.org/doc/html/rfc1459#section-1.1), which defines the IRC protocol.

![app](https://github.com/WebisD/chat-irc-protocol/blob/master/.github/app.gif)


<!-- DOCUMENTATION -->
## 📖 Documentation
You can read the code documentation here:   

<a href="https://webisd.github.io/chat-irc-protocol/" target="_blank">
  <img alt="a" src="https://img.shields.io/badge/read-documentation-blue?style=for-the-badge">
</a>


<!-- HOW TO RUN -->
## 🚀 How To Run

⚠️ For a better experience, make the server terminal and client terminal the same size ⚠️

### Server
```bash

# Clone the repository
$ git clone https://github.com/WebisD/chat-irc-protocol.git

# Access the project folder in your terminal / cmd
$ cd chat-irc-protocol

# Download dependencies
$ pip3 install -r requirements.txt

# Enter the main file folder
$ cd src

# Run the application
$ python3 main.py

# The application will open on the port: 8083

```
### Client
```bash

# Use telnet to connect with our server
$ telnet localhost 8083

```

## 🛠 Commands
### 🆘 Help
Type `/help` to see all commands and arguments if needed

The available commands depend on whether you are logged in:

![](.github/help_logged.PNG)

or not:

![](.github/help_unlogged.PNG)


### ®️ Register
Type `/register <name> <nick> <pass>` to register in discord

This needs 3 arguments:

> **name**: your name

> **nick**: your nick name. This will show up for other users

> **pass**: your password. Don't forget this!

![](.github/register.PNG)

### 🔒 Login
Type `/login <nick> <pass>` to login in Concord

This needs 2 arguments:

> **nick**: your nick name. This will show up for other users

> **pass**: your password. I hope you remember that

![](.github/login.PNG)

### 🆕 Create
Type `/create <room_name> <size>` to create a new room and chat with your friends

This needs 2 arguments:

> **room_name**: the name of your room. Don't put spaces in the name, use '_' instead

> **size**: maximum number of users who can enter the room

![](.github/create.PNG)

### 📜 List room
Type `/listroom` or `/lr` to list all rooms in Concord

![](.github/listroom.PNG)

### 🚪 Join
Type `/join <room_name>` to enter in a room

> **room_name**: the name of the room you want to join

![](.github/join.PNG)

### 💬 Message
Type `/message <your_message>` or `/m <your_message>` to send a message to your friends

> **your_message**: the message you want to send to your friends
 server
Sender's view:
![](.github/message_send.PNG)

Receiver's view:
![](.github/message_receive.PNG)

### 📜 List users
Type `/listusers` or `/lu` to list all users in your current place

If you are in a room, this command will only show users in the room

If you are in the lobby, this command will only show users in Concord who are also not in a room

![](.github/listusers.PNG)

### 🚪 Leave
Type `/leave` to leave the room you are in

![](.github/leave.PNG)

### 🚪 Logout
Type `/logout` to logout of your account

![](.github/logout.PNG)

### 🚪 Quit
Type `/Quit` to fully get out of Concord

![](.github/quit.PNG)

<!-- AUTHORS -->
## 🤖 Authors

[Antonio Gustavo](https://github.com/antuniooh)           |  [João Vitor Dias](https://github.com/JoaoDias-223)           |  [Weverson da Silva](https://github.com/WebisD)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://avatars.githubusercontent.com/u/51217271?v=4" alt="drawing" width="150"/>  |  <img src="https://avatars.githubusercontent.com/u/63318342?v=4" alt="drawing" width="150"/>| <img src="https://avatars.githubusercontent.com/u/49571908?v=4" alt="drawing" width="150"/>
22.119.001-0 | 22.119.006-9 | 22.119.004-4
