from tqdm import tqdm
import requests
import argparse
parser = argparse.ArgumentParser(description='@_@')
parser.add_argument("--url", help="File URL")
parser.add_argument("--name", help="Download file name")
args = parser.parse_args()
a = args.url
b = args.name
url = a
response = requests.get(url, stream=True)
total_size_in_bytes= int(response.headers.get('content-length', 0))
block_size = 1024
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
with open(b, 'wb') as file:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)
progress_bar.close()
if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
    print("ERROR, something went wrong")