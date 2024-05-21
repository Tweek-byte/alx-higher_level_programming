#!/bin/bash
# get bytz size for an URL
curl -s "$1" | wc -c
