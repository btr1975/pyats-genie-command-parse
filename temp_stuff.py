from pyats_genie_command_parse import GenieCommandParse
from tests.test_data import test_string, test_string_2

test_obj = GenieCommandParse(nos='ios')
print(test_obj.parse_string(show_command='show interfaces', show_output_data=test_string))
print(test_obj.parse_string(show_command='show ip interface brief', show_output_data=test_string_2))
