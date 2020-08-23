import pytest


@pytest.mark.generic_tests
def test_bad_nos_exception(command_parse_class):
    with pytest.raises(LookupError):
        command_parse_class('nunya')


@pytest.mark.generic_tests
def test_bad_parse_args_exception(ios_command_parse_object, ios_show_ip_interface_brief_native):
    with pytest.raises(TypeError):
        ios_command_parse_object.parse_string(show_command=['test'],
                                              show_output_data=ios_show_ip_interface_brief_native)

    with pytest.raises(TypeError):
        ios_command_parse_object.parse_string(show_command='show ip interface brief',
                                              show_output_data={'bad': 'string'})


@pytest.mark.generic_tests
def test_bad_parse_file_args_exception(ios_command_parse_object, ios_text_file):
    with pytest.raises(TypeError):
        ios_command_parse_object.parse_file(show_command=['test'], file_name_and_path=ios_text_file)

    with pytest.raises(FileNotFoundError):
        ios_command_parse_object.parse_file(show_command='show interfaces',
                                            file_name_and_path='./tests/test_data/nunya.txt')


@pytest.mark.generic_tests
def test_bad_show_command_exception(ios_command_parse_object, ios_show_ip_interface_brief_native):
    with pytest.raises(ModuleNotFoundError):
        ios_command_parse_object.parse_string(show_command='sho ip int br',
                                              show_output_data=ios_show_ip_interface_brief_native)
