

# ! If no volumes are found on an EC2, raise an exception.
class SnappyVolumesNotFound(Exception):
    pass

# ! This is an exception class that is raised when there is a problem retrieving the instances
class SnappyInstancesRetrievalException(Exception):
    pass