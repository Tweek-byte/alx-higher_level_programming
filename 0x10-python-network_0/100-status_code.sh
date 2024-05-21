#!/bin/bash
# Sends a GET req to a URL
curl -s -o /dev/null -w "%{http_code}" "$1"
