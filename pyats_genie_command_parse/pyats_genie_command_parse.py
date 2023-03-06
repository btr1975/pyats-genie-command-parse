"""
This is meant to separate out the genie parsers from Cisco pyats

It allows you to skip the testbed.yml or anything else before parsing the
output data.

All that is needed to parse the data, is telling the class what NOS, what
the full command is, and the output string data from the command.

"""
from genie.libs.parser.utils.common import get_parser
from pyats.topology import Device


class GenieCommandParse:
    """
    Class to parse string output with Genie without requiring
    a testbed, just parse the string data

    :type nos: String
    :param nos: One of the following {'nxos', 'ios', 'iosxe', 'iosxr'}

    :raises LookupError: If a supported nos is not found

    """

    # This is a Mock Device to engage the parser
    class MockDevice:  # pylint: disable=too-few-public-methods
        """
        Class that is a mock device to parse

        :type show_output_data: String
        :param show_output_data: The output data from the show command

        """
        def __init__(self, show_output_data):
            self.show_output_data = show_output_data

        def execute(self, *args, **kwargs):  # pylint: disable=unused-argument
            """
            Method to execute the MockDevice

            :type args: Arguments
            :param args: Unknown
            :type kwargs: Keywood Arguments
            :param kwargs: Unknown

            :rtype: String
            :return: The output data from the show command

            """
            return self.show_output_data

    # Set to hold supported nos
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

    def __init__(self, nos):
        self.mock_pyats_device = Device('Mock')
        self.mock_pyats_device.custom = {'abstraction': {'order': ['os']}}

        if nos not in self.supported_nos:
            raise LookupError(f'nos needs to be one of theses options {self.supported_nos}')

        self.nos = nos
        self.mock_pyats_device.os = nos

        self.show_output_data = None
        self.show_command = None

    def parse_string(self, show_command, show_output_data):
        """
        Method to parse a show command using string data

        :type show_command: String
        :param show_command: The show command to parse for, use full command!!
        :type show_output_data: String
        :param show_output_data: The output data from the show command

        :rtype: Dict
        :return: Dictionary of parsed data

        :raises TypeError: if the show_command is not a string
        :raises TypeError: if the show_output_data is not a string

        """
        if not isinstance(show_output_data, str):
            raise TypeError(f'show_output_data must be a string received a {type(show_output_data)}')

        self.show_output_data = show_output_data

        if not isinstance(show_command, str):
            raise TypeError(f'show_command must be a string received a {type(show_command)}')

        return self.__parse(show_command)

    def parse_file(self, show_command, file_name_and_path):
        """
        Method to parse a show command using a text file

        :type show_command: String
        :param show_command: The show command to parse for, use full command!!
        :type file_name_and_path: String
        :param file_name_and_path: The full path and name of the file

        :rtype: Dict
        :return: Dictionary of parsed data

        :raises TypeError: if the show_command is not a string
        :raises FileNotFoundError: if the file you are trying to parse can't be found

        """
        if not isinstance(show_command, str):
            raise TypeError(f'show_command must be a string received a {type(show_command)}')

        with open(file_name_and_path, 'r', encoding='utf-8') as file:
            self.show_output_data = file.read()

        return self.__parse(show_command)

    @staticmethod
    def __remove_extra_spaces(string_item):
        """
        Private Method to remove extra spaces from a string

        :type string_item: String
        :param string_item: The you want to remove spaces from

        :rtype: String
        :return: String with single spacing

        :raises TypeError: if the string_item is not a string

        """
        if not isinstance(string_item, str):  # pragma: no cover
            raise TypeError(f'string_item must be a string received a {type(string_item)}')

        string_item = ' '.join(string_item.split())
        return string_item

    def __parse(self, show_command):
        """
        Private Method to parse commands using Genie parser

        :type show_command: String
        :param show_command: The show command to parse for, use full command!!

        :rtype: Dict
        :return: Dictionary of parsed data

        :raises TypeError: if the show_command is not a string
        :raises ModuleNotFoundError: If it can not find a command to NOS mapping

        """
        if not isinstance(show_command, str):  # pragma: no cover
            raise TypeError(f'show_command must be a string received a {type(show_command)}')

        mock_device = self.MockDevice(self.show_output_data)
        try:
            found_parser = get_parser(self.__remove_extra_spaces(show_command), self.mock_pyats_device)[0]
            return found_parser(device=mock_device).parse()

        except Exception as error:
            raise ModuleNotFoundError(f'Could not find module_name for command {show_command} '
                                      f'for nos {self.nos} from genie: {error}') from error
