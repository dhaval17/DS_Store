from ds_store import DSStore
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--target", help="Path to the DS_Store file", required=True)

args = parser.parse_args()

dsstore = DSStore.open(args.target, 'r+')
print("Files and folders :")
for data in dsstore:
	data = str(data)
	entry = data.translate(None, "<>")
	entry = entry.split(' ')
	if(entry[1] == 'Iloc'):
		print(entry[0])