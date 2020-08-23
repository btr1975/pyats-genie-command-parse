File Parsing
============

What to Use File Parsing For
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use file parsing if you have output from a device saved in a text file.

Directions of the File Parser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The most important thing to know is you must use the full command for the data you are trying
  to parse.

* Example good command 'show interfaces'

* Example bad command 'sho int'

File Parsing Example
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pyats_genie_command_parse import GenieCommandParse


   parse_obj = GenieCommandParse(nos='ios')
   data = parse_obj.parse_file(show_command='show interfaces', file_name_and_path='./tests/test_data/ios_test_data.txt')
