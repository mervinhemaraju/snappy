
import boto3
from snappy.utils.helper import format_today
from snappy.models.exceptions import *
from snappy.utils.constants import template_instance_details, template_snapshot_output, MESSAGE_DESCRIPTION_SNAPSHOT

# > This class handles the EC2 operations
# > It will fetch the required instance details
# > It will also perform snapshots of volumes on demand
class Ec2:

    def __init__(self) -> None:
        
        # * Create an empty instances list
        self.r_instances = []
        
        # * Create the ec2 client
        self.client = boto3.client("ec2")

    def get_instance_details(self, filter):

        # * Make api call to get the instance
        response_ips = self.client.describe_instances(
            Filters=filter
        )
        
        # * Filter and append instances obtained
        for r in response_ips['Reservations']:
            for i in r['Instances']:
                self.r_instances.append(i)

        # * Define empty list instance
        instances = []

        # * Retrieve the root volume id for each instance
        for instance in self.r_instances:        

            # * Extract instance information
            name = [tag["Value"] for tag in instance["Tags"] if tag["Key"] == "Name"][0] if 'Tags' in instance and "Name" in [tag["Key"] for tag in instance["Tags"]] else "-"
            id = instance["InstanceId"]
            ipv4 = instance["PrivateIpAddress"]

            # * Check if volumes exists before continuing
            if "BlockDeviceMappings" not in instance:
                raise SnappyVolumesNotFound(f"No volumes found on the instance {name} ({id})")
            
            # * Check if root device is present
            if "RootDeviceName" in instance:
                
                # * Get the root volume device name
                root_volume_device_name = instance["RootDeviceName"]

                # * Filter the root volume ID
                root_volume_data = [block for block in instance["BlockDeviceMappings"] if block["DeviceName"] == root_volume_device_name]

                # * Retrieve the root volume ID if not None
                if len(root_volume_data) == 0: raise SnappyVolumesNotFound(f"Root volume not found on instance: {name} ({id})")

                # * Append the instance details to the list
                instances.append(
                    template_instance_details(
                        volume_id=root_volume_data[0]["Ebs"]["VolumeId"],
                        instance_id=id,
                        ipv4=ipv4,
                        name=name
                    )
                )

        # * Return the list of instances
        return instances

    def get_volume_details(self, volume_ids):

        # * Create the EC2 client
        response = self.client.describe_volumes(
            VolumeIds = volume_ids
        )

        return [
            template_instance_details(
                volume_id=volume['VolumeId'],
                instance_id=volume['Attachments'][0]['InstanceId'] if 'Attachments' in volume else 'None',
                ipv4="N/A",
                name="N/A"
            )
            for volume in response['Volumes']
        ]

    def create_snapshot(self, volume_id, instance_id, instance_name, tags_specifications):

        # * Define Mandatory Tags
        mandatory_tags = [
            {
                "Key": "Date Taken",
                "Value": format_today()
            },
            {
                "Key": "Instance ID",
                "Value": instance_id
            },
            {
                "Key": "Instance Name",
                "Value": instance_name
            }
        ]
        
        # * Reformat tags scpefications
        if tags_specifications != None and tags_specifications != []:
            
            # * Add user defined tags to mandatory tags
            mandatory_tags = mandatory_tags + tags_specifications
            
            # * Re format tags to the specifications
            formated_tags_specs = [
                {
                    'ResourceType': 'snapshot',
                    'Tags': mandatory_tags
                },
            ]
            
        else:
            formated_tags_specs = [
                {
                    'ResourceType': 'snapshot',
                    'Tags': mandatory_tags
                },
            ]

        # * Create the snapshots
        response = self.client.create_snapshot(
            Description=MESSAGE_DESCRIPTION_SNAPSHOT.format(instance_id),
            VolumeId=volume_id,
            TagSpecifications=formated_tags_specs
        )
        
        # * Return the output
        return template_snapshot_output(response["SnapshotId"], instance_name, volume_id)

