
# active

This project is for studying network connection ports

# What is a port?

Port is a "point of entry" for a network connection.
For example, if we say, that a network connection is a logistics company building, then various ports would be doors:
*door to office where you can talk to management
*door for customers to collect their packages
*door to mailbox for incoming mail
*bay doors for receiving products
*bay doors for leaving products

"open" and "closed" ports are the same as open or closed doors in this example

Ports use two kinds of protocols - TCP and UDP
TCP connection is slower, but more stable two-way communication between client and server
UDP is one-way protocol for sending data packets
We could compare TCP and UDP to receiving a package:
TCP package is given hand to hand, from courier to recipent, in exchange for a handshake
UDP package is simply thrown in an open door

# What is port scanning?

Port scanning is simply checking, whether a port is open for communication.

# Why port scanning is important in pentesting?

An open port is like an open door, or rather an open wound for infections(malware) to intrude. With port scanning, an entry point for a malicious attack could be found.

# How the program works

TCP port checking tries to establish a handshake. If handshake is successful, the port is open.
UDP port checking tries to send data to a port. If no error is returned, the port is open.

# usage

Then run the test with

```bash
bash test.sh
```

### Manual usage

Usage: ``` python3 tinyscanner [OPTIONS] [HOST] -p [PORT] ```
```

Options:
  -p               Range of ports to scan
  -u               UDP scan
  -t               TCP scan
  --help           Show this message and exit.
```