# Snappy

Snappy is a Python library that facilitates taking snapshots on EBS.

There are two ways to take snapshots, you can either provide a `volume id` or an ec2 `instance id/instance ipv4/instance name`. If you provide an ec2 detail, it will take a snapshot of the root volume of the instance.

## Getting Started

Assuming that you have Python and virtualenv installed, set up your environment and install the required dependencies using pip:

```
pip install aws-snappy
```

## Using Snappy

After installing snappy, you need to import the main Snappy object and instantiate it to create a connection to AWS:

```
from snappy.snappy import Snappy

snappy = Snappy(values)
```

Here,

`instances` is your list of instances to take snapshots of. i.e. ['10.10.10.10', 'my_instance_name']
Instance can be indentified both by their private IP address or the instance name in the same list.
Snappy will break them apart and search them respectively.

### Available function for Snappy Object

*take_snapshots(tags_specifications)*

This function will take a snapshot of the root volume of the specified instances and return the output in a list in the following format:

#### Parameters

*tags_specifications `<optional>`*: A list of dictionaries containing the tags to be applied to the snapshots in the following format:

```
[{
    "Key": "",
    "Value": ""
}]
```

#### Output

```
[
    {
        "SnapshotID": "",
        "InstanceName": "",
        "VolumeID": "",
    },
    .
    .
    .
]
```

## Running Tests

You can run the tests by following the steps below:

1. Clone or download the project to a folder on your computer.
2. Connect to AWS using AWS CLI
3. Run the tests using the command `./run_test.sh`

## License

```
Copyright Mervin Hemaraju
```
