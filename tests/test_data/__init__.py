test_string = """
GigabitEthernet0/1 is administratively down, line protocol is down (disabled)
  Hardware is Gigabit Ethernet, address is 0019.aa7d.0701 (bia 0019.aa7d.0701)
  Description: UNUSED
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
"""
test_string_2 = """
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  192.168.1.251   YES NVRAM  up                    up
Vlan2                  192.168.2.1     YES NVRAM  administratively down down
Vlan5                  192.168.5.1     YES manual up                    up
Vlan10                 10.0.0.100      YES manual up                    up
GigabitEthernet0/1     unassigned      YES unset  administratively down down
GigabitEthernet0/2     unassigned      YES unset  administratively down down
GigabitEthernet0/3     unassigned      YES unset  up                    up
GigabitEthernet0/4     unassigned      YES unset  administratively down down
GigabitEthernet0/5     unassigned      YES unset  administratively down down
GigabitEthernet0/6     unassigned      YES unset  administratively down down
GigabitEthernet0/7     unassigned      YES unset  administratively down down
GigabitEthernet0/8     unassigned      YES unset  administratively down down
GigabitEthernet0/9     unassigned      YES unset  administratively down down
GigabitEthernet0/10    unassigned      YES unset  administratively down down
GigabitEthernet0/11    unassigned      YES unset  administratively down down
GigabitEthernet0/12    unassigned      YES unset  administratively down down
GigabitEthernet0/13    unassigned      YES unset  administratively down down
GigabitEthernet0/14    unassigned      YES unset  administratively down down
GigabitEthernet0/15    unassigned      YES unset  administratively down down
GigabitEthernet0/16    unassigned      YES unset  up                    up
GigabitEthernet0/17    unassigned      YES unset  administratively down down
GigabitEthernet0/18    unassigned      YES unset  administratively down down
GigabitEthernet0/19    unassigned      YES unset  administratively down down
GigabitEthernet0/20    unassigned      YES unset  administratively down down
GigabitEthernet0/21    unassigned      YES unset  administratively down down
GigabitEthernet0/22    unassigned      YES unset  administratively down down
GigabitEthernet0/23    unassigned      YES unset  administratively down down
GigabitEthernet0/24    unassigned      YES unset  administratively down down
GigabitEthernet0/25    unassigned      YES unset  administratively down down
GigabitEthernet0/26    unassigned      YES unset  administratively down down
GigabitEthernet0/27    unassigned      YES unset  administratively down down
GigabitEthernet0/28    unassigned      YES unset  administratively down down
GigabitEthernet0/29    unassigned      YES unset  up                    up
GigabitEthernet0/30    unassigned      YES unset  up                    up
GigabitEthernet0/31    unassigned      YES unset  administratively down down
GigabitEthernet0/32    unassigned      YES unset  administratively down down
GigabitEthernet0/33    unassigned      YES unset  administratively down down
GigabitEthernet0/34    unassigned      YES unset  administratively down down
GigabitEthernet0/35    unassigned      YES unset  administratively down down
GigabitEthernet0/36    unassigned      YES unset  administratively down down
GigabitEthernet0/37    unassigned      YES unset  administratively down down
GigabitEthernet0/38    unassigned      YES unset  administratively down down
GigabitEthernet0/39    unassigned      YES unset  administratively down down
GigabitEthernet0/40    unassigned      YES unset  administratively down down
GigabitEthernet0/41    unassigned      YES unset  administratively down down
GigabitEthernet0/42    unassigned      YES unset  administratively down down
GigabitEthernet0/43    unassigned      YES unset  down                  down
GigabitEthernet0/44    unassigned      YES unset  down                  down
GigabitEthernet0/45    unassigned      YES unset  up                    up
GigabitEthernet0/46    unassigned      YES unset  up                    up
GigabitEthernet0/47    unassigned      YES unset  down                  down
GigabitEthernet0/48    unassigned      YES unset  up                    up
GigabitEthernet0/49    unassigned      YES unset  administratively down down
GigabitEthernet0/50    unassigned      YES unset  administratively down down
GigabitEthernet0/51    unassigned      YES unset  administratively down down
GigabitEthernet0/52    unassigned      YES unset  administratively down down
Port-channel1          unassigned      YES unset  up                    up
Port-channel2          unassigned      YES unset  down                  down
Loopback0              192.168.10.1    YES NVRAM  up                    up
"""
