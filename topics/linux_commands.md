# Linux Commands

https://www.redhat.com/sysadmin/7-great-network-commands


## IP

## Telnet

Telnet es un protocolo de red que te permite conectarte y comunicarte con otro dispositivo a través de la red.

**Telnet no es seguro para transferir información confidencial, ya que los datos se envían en texto plano, lo que puede ser interceptado.**

El comando `telnet` establece una conexión con un servidor remoto en un puerto específico.

Sintaxis básica:

```shell
telnet [HOST] [PORT]
```

Ejemplo:

```shell
telnet example.com 80
```

Este comando establece una conexión Telnet al servidor "example.com" en el puerto 80.

You can also use the `telnet` command to stablish a raw TCP connection to a specified host and port.

Let's say you want to send a HTTP request, then you can use the `telnet` command to stablish the TCP connection:

```shell
$ telnet localhost 5000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET /greeting HTTP/1.1  # <-- Type this and then press Enter twice

HTTP/1.1 200 OK         # <-- Start of the response
Server: Werkzeug/3.0.1 Python/3.10.12
Date: Tue, 05 Dec 2023 02:02:17 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 13
Connection: close

Hello World!           # <-- Message
Connection closed by foreign host.
```

Note this is NOT using the telnet protocol, is using the telnet command which is used to create raw connections.


## Curl

## TCPDUMP

The tcpdump command is designed for capturing and displaying packets.

- Check if tcpdump is installed in your system:

    ```bash
    tcpdump --verison
    ```

- Output if installed:

    ```bash
    $ tcpdump --verison
    tcpdump version 4.99.1
    libpcap version 1.10.1 (with TPACKET_V3)
    OpenSSL 3.0.2 15 Mar 2022
    ```

- See available interfaces in the system:

    ```bash
    $ tcpdump -D
    1.eth0 [Up, Running, Connected]
    2.any (Pseudo-device that captures on all interfaces) [Up, Running]
    3.lo [Up, Running, Loopback]
    4.bluetooth-monitor (Bluetooth Linux Monitor) [Wireless]
    5.nflog (Linux netfilter log (NFLOG) interface) [none]
    6.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]
    7.dbus-system (D-Bus system bus) [none]
    8.dbus-session (D-Bus session bus) [none]
    ```

- Capture packets on a specific interface:
    - `tcpdump -i eth0`

- Capture packets from a specific IP address:
    - `tcpdump host 192.168.1.100`

- Capture packets on a specific port:
    - `tcpdump port 80`

- Save captured packets to a file for later analysis:
    - `tcpdump -i eth0 -w output.pcap`

- Read captured packets from a file:
    - `tcpdump -r input.pcap`

- Display only the number of packets being captured without showing the packet contents:
    - `tcpdump -c <packet_count> -q`

        -c option set a packet count limit\
        -q option to suppress packet details and headers