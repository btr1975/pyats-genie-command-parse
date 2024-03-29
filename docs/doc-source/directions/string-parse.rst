String Parsing
==============

What to Use String Parsing For
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use string parsing to parse string output from devices to run the data through genie
  parsers.

* Some options to get the data could be using netmiko, to pull data from a device and then
  run that pulled data through a parser.

* Another option could be using Cisco NSO to pull the data from a device and then run
  the output through a parser.


Directions of the String Parser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The most important thing to know is you must use the full command for the data you are trying
  to parse.

* Example good command 'show interfaces'

* Example bad command 'sho int'


String Parsing Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pyats_genie_command_parse import GenieCommandParse


   ios_show_interfaces_string = """
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


   parse_obj = GenieCommandParse(nos='ios')
   data = parse_obj.parse_string(show_command='show interfaces', show_output_data=ios_show_interfaces_string)
