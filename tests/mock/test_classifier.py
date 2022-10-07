import pytest
from snappy.models.classifier import Classifier

class TestClassifier:

    testdata = [
        (
            [],
            [],
            [],
            [],
            []
        ),
        (
            ["i-yedef", "vol-eyef", "10.10.707"],
            [],
            [],
            [],
            ["i-yedef", "vol-eyef", "10.10.707"]
        ),
        (
            ["i-e12ef12f", "vol-231edaccc235", "10.10.10.10"],
            [],
            ["i-e12ef12f"],
            ["10.10.10.10"],
            ["vol-231edaccc235"]
        ),
        (
            ["i-e12ef12f", "i-76dfe78365abb563f", "i-e12ef12f"],
            [],
            ["i-e12ef12f", "i-76dfe78365abb563f", "i-e12ef12f"],
            [],
            []
        ),
        (
            ["i-e12ef12f", "vol-76dfe78365abb563f", "my-instance", "i-instance", "192.168.100.1"],
            ["vol-76dfe78365abb563f"],
            ["i-e12ef12f"],
            ["192.168.100.1"],
            ["my-instance", "i-instance"]
        ),
    ]
    @pytest.mark.parametrize("values,expected_vids,expected_iids,expected_ips,expected_inames", testdata)
    def test_classifier_init(self,values,expected_vids,expected_iids,expected_ips,expected_inames):

        # * Arrange

        # * Act
        sut_classifier = Classifier(values=values)
        result_vids = sut_classifier.volume_ids
        result_iids = sut_classifier.instance_ids
        result_ips = sut_classifier.ipv4s
        result_inames = sut_classifier.instance_names

        # * Assert
        assert sorted(result_iids) == sorted(expected_iids)
        assert sorted(result_vids) == sorted(expected_vids)
        assert sorted(result_ips) == sorted(expected_ips)
        assert sorted(result_inames) == sorted(expected_inames)