#!/bin/bash

#source secret.env

# All tests files
pytest -v

# Single test file
#pytest -v tests/test_api.py

# Single function
#pytest -v tests/test_snappy.py::TestSnappy::test_snappy_snap_roots