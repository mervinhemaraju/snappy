
from snappy.utils.matcher import *
from snappy.models.ec2 import Ec2

# > This is the Classifier class
# > It will break down the values to determine whether it is a volume id, instance id, ipv4 or instance name.
# > It will then make the API calls accordingly
class Classifier:

    def __init__(self, values) -> None:
        
        # * Retrieve the volume IDs
        self.volume_ids = [id for id in values if is_a_volume_id(id)]

        # * Retrieve the instance IDs
        self.instance_ids = [id for id in values if is_an_instance_id(id)]

        # * Retrieve the ip addresses
        self.ipv4s = [ip for ip in values if is_an_ipv4(ip)]

        # * Retrieve the instance names
        self.instance_names = list(set(values) - set(self.volume_ids + self.instance_ids + self.ipv4s))

        # * Define a list of instance details to be loaded
        self.instance_details = []

        # * Load the resources
        self.__load_resources()

    def __load_resources(self):

        # * Create an ec2 object
        ec2 = Ec2()
        
        # * If we obtained instance ids, retrieve by instance id
        if len(self.instance_ids) > 0:

            # * Set filter as instance ids and append to instance details
            self.instance_details += ec2.get_instance_details(
                filter=[
                    {
                        "Name": "instance-id",
                        "Values": self.instance_ids
                    }
                ]
            )

        # * If we obtained instance ips, retrieve by instance ip
        if len(self.ipv4s) > 0:

            # * Set filter as instance ipv4 and append to instance details
            self.instance_details += ec2.get_instance_details(
                filter=[
                    {
                        "Name": "private-ip-address",
                        "Values": self.ipv4s
                    }
                ]
            )

        # * If we obtained instance names, retrieve by instance names
        if len(self.instance_names) > 0:

            # * Set filter as instance ipv4 and append to instance details
            self.instance_details += ec2.get_instance_details(
                filter=[
                    {
                        "Name": "tag:Name",
                        "Values": self.instance_names
                    }
                ]
            )

        # * If we obtained volume ids, add them to the instance details
        if len(self.volume_ids) > 0:

            # * Set filter as instance ipv4 and append to instance details
            self.instance_details += ec2.get_volume_details(self.volume_ids)
