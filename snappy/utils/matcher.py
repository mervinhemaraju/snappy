import re
from snappy.utils.constants import *

def is_an_ipv4(data):
    """
    > It returns True if the data is an IPv4 address, and False otherwise
    
    > :param data: The string to be matched
    > :return: A boolean value.
    """
    pat = re.match(REGEX_AWS_INSTANCE_IPV4, data)
    return bool(pat)

def is_an_instance_id(data):
    """
    > It returns True if the data is an EC2 instance id, and False otherwise
    
    > :param data: The string to be matched
    > :return: A boolean value.
    """
    pat = re.match(REGEX_AWS_INSTANCE_ID, data.lower())
    return bool(pat)

def is_a_volume_id(data):
    """
    > It returns True if the data is an EBS volume id, and False otherwise
    
    > :param data: The string to be matched
    > :return: A boolean value.
    """
    pat = re.match(REGEX_AWS_VOLUME_ID, data.lower())
    return bool(pat)