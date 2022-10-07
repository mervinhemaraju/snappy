
from snappy.models.classifier import Classifier
from snappy.models.ec2 import Ec2
from snappy.models.exceptions import SnappyInstancesRetrievalException
from snappy.utils.helper import remove_duplicate_ids
from snappy.utils.constants import EXCEPTION_MESSAGE_RESOURCES_RETRIEVAL_FAILED
from time import sleep

class Snappy():  
        
    def __init__(self, values):

        # * Create a classifier object to load the resources
        classifier = Classifier(values)

        # * Verify if there were any errors when fetching resources
        if (len(classifier.instance_details))!= len(values):

            # * Failed resources list
            failed_resources = []

            # * Determine the ones that failed
            r_vids = [instance['volume_id'] for instance in classifier.instance_details]
            r_iids = [instance['instance_id'] for instance in classifier.instance_details]
            r_ip = [instance['ipv4'] for instance in classifier.instance_details]
            r_names = [instance['instance_name'] for instance in classifier.instance_details]

            failed_resources = [
                resource
                for resource in values
                if resource not in (r_vids + r_iids + r_ip + r_names)
            ]

            # * Verify is failed resources obtained
            if failed_resources:
                raise SnappyInstancesRetrievalException(
                    EXCEPTION_MESSAGE_RESOURCES_RETRIEVAL_FAILED.format(failed_resources)
                )
    
        # * Remove duplicates in the list of instance details
        self.instance_details = remove_duplicate_ids(classifier.instance_details)       

    def take_snapshots(self, tags_specifications=None):

        # * Create empty list of snapshot responses
        snapshots = []

        # * Create an Ec2 object
        ec2 = Ec2()

        # * Iterate through list of instance details
        for detail in self.instance_details:
            
            # * Take the snapshot
            snapshots.append(
                ec2.create_snapshot(
                    volume_id=detail["volume_id"],
                    instance_id=detail["instance_id"],
                    instance_name=detail["instance_name"],
                    tags_specifications=tags_specifications,
                )
            )

            # * Throttle api call
            sleep(1.5)

            



