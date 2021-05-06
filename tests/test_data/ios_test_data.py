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


ios_show_interfaces_parsed = {
    'GigabitEthernet0/1': {'port_channel': {'port_channel_member': False}, 'enabled': False, 'line_protocol': 'down',
                           'oper_status': 'down', 'connected': False, 'type': 'Gigabit Ethernet',
                           'mac_address': '0019.aa7d.0701', 'phys_address': '0019.aa7d.0701', 'description': 'UNUSED',
                           'delay': 10, 'mtu': 1500, 'bandwidth': 1000000, 'reliability': '255/255', 'txload': '1/255',
                           'rxload': '1/255', 'encapsulations': {'encapsulation': 'arpa'}, 'err_disabled': False,
                           'keepalive': 10,
                           'duplex_mode': 'full', 'port_speed': '1000mb/s', 'media_type': '10/100/1000BaseTX',
                           'flow_control': {'receive': False, 'send': False}, 'arp_type': 'arpa',
                           'arp_timeout': '04:00:00', 'last_input': 'never', 'last_output': 'never',
                           'output_hang': 'never',
                           'queues': {'input_queue_size': 0, 'input_queue_max': 75, 'input_queue_drops': 0,
                                      'input_queue_flushes': 0, 'total_output_drop': 0, 'queue_strategy': 'fifo',
                                      'output_queue_size': 0, 'output_queue_max': 40}, 'counters': {
            'rate': {'load_interval': 300, 'in_rate': 0, 'in_rate_pkts': 0, 'out_rate': 0, 'out_rate_pkts': 0},
            'last_clear': 'never', 'in_pkts': 0, 'in_octets': 0, 'in_no_buffer': 0, 'in_multicast_pkts': 0,
            'in_broadcast_pkts': 0, 'in_runts': 0, 'in_giants': 0, 'in_throttles': 0, 'in_errors': 0,
            'in_crc_errors': 0, 'in_frame': 0, 'in_overrun': 0, 'in_ignored': 0, 'in_watchdog': 0,
            'in_mac_pause_frames': 0, 'in_with_dribble': 0, 'out_pkts': 0, 'out_octets': 0, 'out_underruns': 0,
            'out_errors': 0, 'out_interface_resets': 1, 'out_collision': 0, 'out_babble': 0, 'out_late_collision': 0,
            'out_deferred': 0, 'out_buffer_failure': 0, 'out_buffers_swapped': 0}}}


ios_show_ip_interface_brief_string = """
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


ios_show_ip_interface_brief_parsed = {'interface': {
    'Vlan1': {'ip_address': '192.168.1.251', 'interface_is_ok': 'YES', 'method': 'NVRAM', 'status': 'up',
              'protocol': 'up'}, 'Vlan2': {'ip_address': '192.168.2.1', 'interface_is_ok': 'YES', 'method': 'NVRAM',
                                           'status': 'administratively down', 'protocol': 'down'},
    'Vlan5': {'ip_address': '192.168.5.1', 'interface_is_ok': 'YES', 'method': 'manual', 'status': 'up',
              'protocol': 'up'},
    'Vlan10': {'ip_address': '10.0.0.100', 'interface_is_ok': 'YES', 'method': 'manual', 'status': 'up',
               'protocol': 'up'},
    'GigabitEthernet0/1': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/2': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/3': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                           'protocol': 'up'},
    'GigabitEthernet0/4': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/5': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/6': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/7': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/8': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/9': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                           'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/10': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/11': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/12': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/13': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/14': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/15': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/16': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                            'protocol': 'up'},
    'GigabitEthernet0/17': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/18': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/19': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/20': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/21': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/22': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/23': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/24': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/25': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/26': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/27': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/28': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/29': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                            'protocol': 'up'},
    'GigabitEthernet0/30': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                            'protocol': 'up'},
    'GigabitEthernet0/31': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/32': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/33': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/34': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/35': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/36': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/37': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/38': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/39': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/40': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/41': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/42': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/43': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'down',
                            'protocol': 'down'},
    'GigabitEthernet0/44': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'down',
                            'protocol': 'down'},
    'GigabitEthernet0/45': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                            'protocol': 'up'},
    'GigabitEthernet0/46': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                            'protocol': 'up'},
    'GigabitEthernet0/47': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'down',
                            'protocol': 'down'},
    'GigabitEthernet0/48': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                            'protocol': 'up'},
    'GigabitEthernet0/49': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/50': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/51': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'GigabitEthernet0/52': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset',
                            'status': 'administratively down', 'protocol': 'down'},
    'Port-channel1': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'up',
                      'protocol': 'up'},
    'Port-channel2': {'ip_address': 'unassigned', 'interface_is_ok': 'YES', 'method': 'unset', 'status': 'down',
                      'protocol': 'down'},
    'Loopback0': {'ip_address': '192.168.10.1', 'interface_is_ok': 'YES', 'method': 'NVRAM', 'status': 'up',
                  'protocol': 'up'}}}
