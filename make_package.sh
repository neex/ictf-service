#!/bin/bash
# This script makes service.tgz with all needed files
tar -czf service.tgz info.yaml service/ro/nadmozg service/ro/main.sed service/ro/common.sed service/rw/.gitkeep scripts/setflag.py scripts/exploit.py scripts/getflag.py scripts/benign.py src/README.md
