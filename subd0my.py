#!/usr/bin/python3
# -*- coding: utf-8 -*-

# standard library modules
import sys
import argparse

# external modules
import requests
from colorama import Fore

banner = """
               _         _  ___                  
     ___ _   _| |__   __| |/ _ \ _ __ ___  _   _ 
    / __| | | | '_ \ / _` | | | | '_ ` _ \| | | |
    \__ \ |_| | |_) | (_| | |_| | | | | | | |_| |
    |___/\__,_|_.__/ \__,_|\___/|_| |_| |_|\__, |
                                            |___/
"""
print(Fore.GREEN + banner)
print("")


def main():
    print("")

    # Parser to parse the arguemnts from the command line
    parser = argparse.ArgumentParser(
        epilog="\tExample: \r\npython3 "
        + sys.argv[0]
        + " -d google.com -w wordlist.txt -o output.txt"
    )

    # Arguments
    parser.add_argument(
        "-d",
        dest="domain",
        help="Domain name to scan for subdomains",
        required=True,
    )
    parser.add_argument(
        "-w", dest="wordlist", help="Wordlist of subdomains", required=True
    )
    parser.add_argument(
        "-o ", dest="output", help="Filename for the output file", required=True
    )
    args = parser.parse_args()

    print(f"[+] Target: {args.domain}")
    print("[+] Discovered subdomains: \n")

    file = open(args.wordlist)  # path to file

    # read all content
    content = file.read()

    # split by new lines
    subdomains = content.splitlines()

    # brute forcing the sub doms
    for subdomain in subdomains:
        # construct the url
        url = f"http://{subdomain}.{args.domain}"

        try:
            # if this raises an ERROR, that means the subdomain does not exist
            requests.get(url)

        except requests.ConnectionError:
            # if the subdomain does not exist, just pass, print nothing
            pass
        else:
            print(url)

            # create a new text file
            text_file = open(args.output, "a")

            # write to the file
            text_file.write(url + "\n")


if __name__ == "__main__":
    main()
