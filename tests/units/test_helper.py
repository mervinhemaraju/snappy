import pytest
from snappy.utils.helper import *
        
class TestHelper:

    testdata = [
        (
            [],
            []
        ),
        (
            [{"volume_id": "vol-12345678"}, {"volume_id": "vol-123445"}, {"volume_id":"vol-123"}, {"volume_id":"vol-12345"}],
            [{"volume_id": "vol-12345678"}, {"volume_id": "vol-123445"}, {"volume_id":"vol-123"}, {"volume_id":"vol-12345"}]
        ),
        (
            [{"volume_id": "vol-12345678"}, {"volume_id": "vol-12345678"}, {"volume_id": "vol-12345678"}, {"volume_id":"vol-12345"}],
            [{"volume_id": "vol-12345678"}, {"volume_id":"vol-12345"}]
        ),
        (
            [{"volume_id": "vol-12345678"}, {"volume_id": "vol-12345678"}, {"volume_id":"vol-12345670"}, {"volume_id":"vol-12345"}],
            [{"volume_id": "vol-12345678"}, {"volume_id":"vol-12345670"}, {"volume_id":"vol-12345"}]
        ),
        (
            [{"volume_id": "vol-12345678"}, {"volume_id": "vol-12345678"}, {"volume_id": "vol-12345678"}, {"volume_id": "vol-12345678"}],
            [{"volume_id": "vol-12345678"}]
        )
    ]
    @pytest.mark.parametrize("test_data,expected_result", testdata)
    def test_remove_duplicate_ids(self,test_data, expected_result):
        
        # Act
        result = remove_duplicate_ids(test_data)
        
        # Assert
        assert result == expected_result
        assert len(result) == len(expected_result)