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
          <li><a href="#-register">Register</a></li>
          <li><a href="#-login">Login</a></li>
          <li><a href="#-create">Create</a></li>
          <li><a href="#-listroom">Listroom</a></li>
          <li><a href="#-join">Join</a></li>
          <li><a href="#-message">Message</a></li>
          <li><a href="#-listusers">Listusers</a></li>
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
In this project, we implemented a chat application with the main feature of discord or whatsapp: creating a room to chat with friends.

Our application runs on the terminal using *telnet*.

The HTTP server was implemented according to the [RFC 1459](https://datatracker.ietf.org/doc/html/rfc1459#section-1.1), which defines the IRC protocol.

![app](https://github.com/WebisD/http-api-without-lib/blob/master/.github/app.gif)


<!-- DOCUMENTATION -->
## 📖 Documentation
You can read the code documentation here:   

<a href="https://webisd.github.io/chat-irc-protocol/" target="_blank">
  <img alt="a" src="https://img.shields.io/badge/read-documentation-blue?style=for-the-badge">
</a>


<!-- HOW TO RUN -->
## 🚀 How To Run
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
### 🆘 help
Type `/help` to see all commands and arguments if needed

The available commands depend on whether you are logged in or not:

![]()

### 🆘 register
Type `/help` to see all commands and arguments if needed

The available commands depend on whether you are logged in or not:

![]()




<!-- AUTHORS -->
## 🤖 Authors

[Antonio Gustavo](https://github.com/antuniooh)           |  [João Vitor Dias](https://github.com/JoaoDias-223)           |  [Weverson da Silva](https://github.com/WebisD)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://avatars.githubusercontent.com/u/51217271?v=4" alt="drawing" width="150"/>  |  <img src="https://avatars.githubusercontent.com/u/63318342?v=4" alt="drawing" width="150"/>| <img src="https://avatars.githubusercontent.com/u/49571908?v=4" alt="drawing" width="150"/>
22.119.001-0 | 22.119.006-9 | 22.119.004-4
