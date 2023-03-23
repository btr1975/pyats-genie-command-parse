import pytest


@pytest.mark.ios_tests
def test_ios_show_ip_interface_brief(ios_command_parse_object, ios_show_ip_interface_brief_native,
                                     ios_show_ip_interface_brief_dict):
    returned_data = ios_command_parse_object.parse_string(show_command='show ip interface brief',
                                                          show_output_data=ios_show_ip_interface_brief_native)

    assert type(returned_data) == dict
    assert returned_data == ios_show_ip_interface_brief_dict


@pytest.mark.ios_tests
def test_ios_show_interfaces(ios_command_parse_object, ios_show_interfaces_native, ios_show_interfaces_dict):
    returned_data = ios_command_parse_object.parse_string(show_command='show interfaces',
                                                          show_output_data=ios_show_interfaces_native)

    assert type(returned_data) == dict
    assert returned_data == ios_show_interfaces_dict


@pytest.mark.ios_tests
def test_ios_show_interfaces_file(ios_command_parse_object, ios_text_file, ios_show_interfaces_dict):
    returned_data = ios_command_parse_object.parse_file(show_command='show interfaces',
                                                        file_name_and_path=ios_text_file)

    assert type(returned_data) == dict
    assert returned_data == ios_show_interfaces_dict
