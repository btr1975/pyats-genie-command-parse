| BRANCH | STATUS |
|---|---|
| master | [![Unit-Testing, Coverage, Linting](https://github.com/btr1975/pyats-genie-command-parse/actions/workflows/test-coverage-lint.yml/badge.svg?branch=master)](https://github.com/btr1975/pyats-genie-command-parse/actions/workflows/test-coverage-lint.yml) |
| develop | [![Unit-Testing, Coverage, Linting](https://github.com/btr1975/pyats-genie-command-parse/actions/workflows/test-coverage-lint.yml/badge.svg?branch=develop)](https://github.com/btr1975/pyats-genie-command-parse/actions/workflows/test-coverage-lint.yml) |

[![Downloads](https://pepy.tech/badge/pyats-genie-command-parse)](https://pepy.tech/project/pyats-genie-command-parse)
[![Supported Versions](https://img.shields.io/pypi/pyversions/pyats-genie-command-parse.svg)](https://pypi.org/project/pyats-genie-command-parse)


# pyats-genie-command-parse
This is a library to be able to parse NOS command output using the available
[Genie parsers](https://developer.cisco.com/docs/genie-docs/), it seperates out 
needing to create a testbed.yml, and allows you to just get the output, and parse the 
output with [Genie parsers](https://developer.cisco.com/docs/genie-docs/). You can find the 
[Genie Parse Source here](https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser)

# Line 55 in pyats_genie_command_parse.py
```python
 supported_nos = {'aireos',
                  'apic',
                  'asa',
                  'bigip',
                  'cheetah',
                  'comware',
                  'dnac',
                  'gaia',
                  'ios',
                  'iosxe',
                  'iosxr',
                  'ironware',
                  'junos',
                  'linux',
                  'nxos',
                  'sros',
                  'viptela'}
```

# Some options to get the data
1. You could use [netmiko](https://ktbyers.github.io/netmiko/) to get the command output
   from devices and then parse using the string parser.

2. You could use [Cisco Network Services Orchestrator "NSO"](https://developer.cisco.com/docs/nso/)
   to get the command output from devices and then parse using the string parser.

3. Use your imagination, as long as you can get the output data in a string format the string parser
   will work.

4. If you prefer you could store the data in a text file, and then using the file parser, you can also
   parse the output data.
