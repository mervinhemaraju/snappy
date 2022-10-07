import pytest
from snappy.utils.matcher import *

class TestMatcher:

    testdata = [
        ("1.1.1.1", True),
        ("10.10.10.10", True),
        ("1.10.100.255", True),
        ("255.255.255.255", True),
        ("255.255.255.256", False),
        ("255.255.256.255", False),
        ("255.256.255.255", False),
        ("256.255.255.255", False),
        ("192.168.100.", False),
        ("300.168.100.1", False),
        ("1.168.100.300", False),
        ("192.168..1", False),
        ("192..1.1", False),
        (".1.1.1", False),
        ("hello.168.100.1", False),
        ("t.r.s.a", False),
        ("100.1.1.1:20", False),
    ]
    @pytest.mark.parametrize("test_data,expected_result", testdata)
    def test_is_an_ipv4(self,test_data,expected_result):
        # * Arrange

        # * Act
        result = is_an_ipv4(test_data)

        # * Assert
        assert result == expected_result

    testdata = [
        ("i-cb99935c", True),
        ("i-ed3a2f7a", True),
        ("i-ed3a2f7A", True),
        ("i-0f607266527a79998", True),
        ("i-05e8e8055180a7a4c", True),
        ("i-05E8e8055180A7a4c", True),
        ("i-05E8055180A7a4c", False),
        ("i-0f607266527a79998add", False),
        ("i-1234567h", False),
        ("i-123456abdf8e340xz", False),
        ("i-0908978989798798", False),
        ("i-abcdefgh", False),
        ("j-abcdefgh", False),
        ("i-", False)
    ]
    @pytest.mark.parametrize("test_data,expected_result", testdata)
    def test_is_an_instance_id(self,test_data,expected_result):
        # * Arrange

        # * Act
        result = is_an_instance_id(test_data)

        # * Assert
        assert result == expected_result

    testdata = [
        ("vol-cb99935c", True),
        ("vol-ed3a2f7a", True),
        ("vol-ed3a2f7A", True),
        ("vol-0f607266527a79998", True),
        ("vol-05e8e8055180a7a4c", True),
        ("vol-05E8e8055180A7a4c", True),
        ("vol-05E8055180A7a4c", False),
        ("vol-0f607266527a79998add", False),
        ("vol-1234567h", False),
        ("vol-123456abdf8e340xz", False),
        ("vol-0908978989798798", False),
        ("vol-abcdefgh", False),
        ("voi-abcdefgh", False),
        ("vol-", False)
    ]
    @pytest.mark.parametrize("test_data,expected_result", testdata)
    def test_is_a_volume_id(self,test_data,expected_result):
        # * Arrange

        # * Act
        result = is_a_volume_id(test_data)

        # * Assert
        assert result == expected_result
