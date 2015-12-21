from ds_store import DSStore
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="Path to the DS_Store file", required=True)
parser.add_argument("-t", "--type", help="Type : Iloc, bwsp, lsvp, lsvP, icvp", default=100)
args = parser.parse_args()

dsstore = DSStore.open(args.path, 'r+')
for data in dsstore:
	data = str(data)
	entry = data.translate(None, "<>")
	entry = entry.split(' ')
	if(entry[1] == args.type):
		print(entry[0])