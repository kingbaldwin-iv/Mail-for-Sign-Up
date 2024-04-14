import sys
import requests
import time
from tqdm import tqdm
args = sys.argv[1:]

if len(args) != 1 or not args[0].isdigit(): sys.exit("invalid argument")
response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
if response.status_code == 200:
	print("Generated Email: " + str(response.json()[0]))
	domain = response.json()[0].split("@")[1]
	login = response.json()[0].split("@")[0]
	print(f"Waiting {int(args[0])}s to check inbox...")
	for i in tqdm(range(int(args[0]))): time.sleep(1)
	response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
	if response.status_code == 200:
		if len(response.json()) == 0: sys.exit("empty inbox")
		ids = response.json()[0]['id']
		response = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={ids}')
		if response.status_code == 200: sys.exit(response.json())
