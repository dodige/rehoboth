#!/bin/sh

tvservice -p

echo "on 0" | cec-client -d 1 -s
