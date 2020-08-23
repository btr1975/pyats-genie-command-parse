import os
import sys
import pytest
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))
from tests.test_data import ios_show_interfaces_string, ios_show_interfaces_parsed, \
    ios_show_ip_interface_brief_string, ios_show_ip_interface_brief_parsed
from pyats_genie_command_parse import GenieCommandParse


@pytest.fixture
def ios_show_ip_interface_brief_native():
    return ios_show_ip_interface_brief_string


@pytest.fixture
def ios_show_ip_interface_brief_dict():
    return ios_show_ip_interface_brief_parsed


@pytest.fixture
def ios_show_interfaces_native():
    return ios_show_interfaces_string


@pytest.fixture
def ios_show_interfaces_dict():
    return ios_show_interfaces_parsed


@pytest.fixture
def ios_command_parse_object():
    yield GenieCommandParse(nos='ios')


@pytest.fixture
def command_parse_class():
    yield GenieCommandParse


@pytest.fixture
def text_file_location():
    return './tests/test_data'


@pytest.fixture
def ios_text_file(text_file_location):
    return '{}/ios_test_data.txt'.format(text_file_location)
