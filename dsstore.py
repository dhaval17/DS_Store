#!/usr/bin/env python3
"""
DS_Store parser - View contents of .DS_Store files
"""
from ds_store import DSStore
from tqdm import tqdm
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Python script to view contents of .DS_Store file"
    )
    
    parser.add_argument(
        "-p", "--path",
        help="Path to the DS_Store file",
        required=True
    )
    parser.add_argument(
        "-t", "--type",
        help="Type of entry to filter: Iloc, bwsp, lsvp, lsvP, icvp",
        default='Iloc'
    )
    
    args = parser.parse_args()
    
    try:
        dsstore = DSStore.open(args.path, 'r+')
        for data in tqdm(dsstore):
            data_str = str(data)
            # Remove angle brackets and split
            entry = data_str.translate(str.maketrans('', '', '<>'))
            entry = entry.split(' ')
            if entry[1] == args.type:
                print(entry[0])
    except FileNotFoundError:
        print(f"Error: DS_Store file not found at {args.path}")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
