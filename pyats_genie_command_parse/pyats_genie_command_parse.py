from genie.libs.parser.utils.common import get_parser
from pyats.topology import Device


class GenieDevicelessParserV3(object):
    """
    Class to parse string output with Genie without requiring
    a testbed, just parse the string data
    """

    # This is a Mock Device to engage the parser
    class MockDevice(object):
        def __init__(self, show_output_data):
            self.show_output_data = show_output_data

        def execute(self, *args, **kwargs):
            return self.show_output_data

    # Set to hold supported nos
    supported_nos = {'nxos', 'ios', 'iosxe', 'iosxr'}

    def __init__(self, nos):
        self.MOCK_PYATS_DEVICE = Device('Mock')
        self.MOCK_PYATS_DEVICE.custom = {'abstraction': {'order': ['os']}}

        if nos not in self.supported_nos:
            raise LookupError('nos needs to be one of theses options {}'.format(self.supported_nos))

        else:
            self.nos = nos
            self.MOCK_PYATS_DEVICE.os = nos

        self.show_output_data = None
        self.show_command = None

    def parse_string(self, show_command, show_output_data):
        """
        Method to parse a show command using string data
        :param show_command: The show command to parse for, use full command
        :param show_output_data: String data to parse
        :return:
            Dict of parsed data
        """
        if not isinstance(show_output_data, str):
            raise TypeError('show_output_data must be a string')

        else:
            self.show_output_data = show_output_data

        return self.__parse(show_command)

    def parse_file(self, show_command, file_name_and_path):
        """
        Method to parse a show command using a text file
        :param show_command: The show command to parse for, use full command
        :param file_name_and_path: The full path and name of the file
        :return:
            Dict of parsed data
        """
        with open(file_name_and_path) as f:
            self.show_output_data = f.read()

        return self.__parse(show_command)

    @staticmethod
    def __remove_extra_spaces(string_item):
        """
        Private Method to remove extra spaces from a string
        :param string_item: String that you want to remove spaces from
        :return:
            String with single spacing
        """
        string_item = ' '.join(string_item.split())
        return string_item

    def __parse(self, show_command):
        """
        Private Method to parse commands using Genie parser
        :param show_command: The show command to parse for, use full command
        :return:
            Dict of parsed data
        """
        md = self.MockDevice(self.show_output_data)
        try:
            found_parser = get_parser(self.__remove_extra_spaces(show_command), self.MOCK_PYATS_DEVICE)[0]
            return found_parser(device=md).parse()

        except Exception as e:
            raise Exception('Could not find module_name for command {} for nos {} from genie: {}'.format(show_command,
                                                                                                         self.nos, e))



