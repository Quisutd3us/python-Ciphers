#!/usr/bin/env python
# Reverse Cipher
import argparse

parser = argparse.ArgumentParser(description="reverse Cipher App")
parser.add_argument('--msg', action='store', dest='msg', type=str, required=True)
get_args = parser.parse_args()
message = get_args.msg
cypher_message = ''
i = len(message) - 1
try:
    while i != -1:
        cypher_message += message[i]
        i -= 1
    print("[+] Successful reverse cipher : %s" %cypher_message)
except OSError as e:
    print("[-] Cipher machine has an error: %s" % cypher_message)
