# Lab 3 way handshake

In this practice we are going to explore the TCP 3 way handshake

## Prerequisites:

- Make the [simple_flask](../scripts/simple_flask_app/) project work in your machine.
- Install wireshark
- Install tcpdump

## Steps

1. Run the flask app:

```shell
python3 flask_app.py
 * Serving Flask app 'flask_app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 735-997-262
```

2. Start a packet capture:

```shell
$ tcpdump -D                                    
1.wlo1 [Up, Running, Wireless, Associated]
2.any (Pseudo-device that captures on all interfaces) [Up, Running]
3.lo [Up, Running, Loopback]
4.bluetooth0 (Bluetooth adapter number 0) [Wireless, Association status unknown]
5.bluetooth-monitor (Bluetooth Linux Monitor) [Wireless]
6.nflog (Linux netfilter log (NFLOG) interface) [none]
7.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]
8.dbus-system (D-Bus system bus) [none]
9.dbus-session (D-Bus session bus) [none]

$ sudo tcpdump -i lo tcp -n -v -w handshake.pcap
[sudo] password for noe: 
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
Got 0
```

3. Create a raw connection to the web server:

```shell
$ telnet localhost 5000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
```

After you see the message "Connected to localhost." you will see packets are being captured in tcpdump:

```shell
sudo tcpdump -i lo tcp -n -v -w handshake.pcap
[sudo] password for noe: 
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
Got 3  <--- We have 3 packets!
```

You can now stop the packet capture and stop the web server.

![handshake_terminal_capture.png](../../../img/handshake_terminal_capture.png)


## Explore the packet capture

Open the packet capture with wireshark.

You can download the file here: [handshake.pcap](./handshake.pcap)

![wireshark_handshake.png](../../../img/wireshark_handshake.png)