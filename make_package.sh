#!/bin/bash
# This script makes service.tgz with all needed files
tar -czf service.tgz info.yaml service/ro/translator service/ro/main.sed service/ro/common.sed service/rw/.gitkeep scripts/set_flag.py scripts/exploit.py scripts/get_flag.py scripts/benign.py src/README.md
