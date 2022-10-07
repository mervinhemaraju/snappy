
#*###############################################*#
#*###### All constants values resides here ######*#
#*###############################################*#


#*#####################*#
#*####### REGEX #######*#
#*#####################*#

REGEX_AWS_VOLUME_ID = "^vol-[a-f0-9]{8}(?:[a-f0-9]{9})?$"
REGEX_AWS_INSTANCE_ID = "^i-[a-f0-9]{8}(?:[a-f0-9]{9})?$"
REGEX_AWS_INSTANCE_IPV4 = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

#*###################################*#
#*####### TEMPLATES & FILTERS #######*#
#*###################################*#
    
def template_snapshot_output(snapshot_id, for_instance, volume_id):
    return {
        "SnapshotID": snapshot_id,
        "InstanceName": for_instance,
        "VolumeID": volume_id,
    }

def template_instance_details(volume_id, instance_id, ipv4, name):
    return {
        "volume_id": volume_id,
        "instance_id": instance_id,
        "instance_name": name,
        "ipv4": ipv4
    }
    
######################################
############## MESSAGES ##############
######################################
MESSAGE_DESCRIPTION_SNAPSHOT = 'Snapshot for {}'

########################################
############## EXCEPTIONS ##############
########################################
EXCEPTION_MESSAGE_RESOURCES_RETRIEVAL_FAILED = "The following resources could not be retrieved: {}"