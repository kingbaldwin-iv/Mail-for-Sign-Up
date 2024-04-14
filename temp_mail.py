import sys
import requests
import time
from tqdm import tqdm
args = sys.argv[1:]

if len(args) != 1 or not args[0].isdigit():
	print("invalid argument")
	quit()

wait = int(args[0])
response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
if response.status_code == 200:
	email = response.json()[0].split("@")
	print("Generated Email:")
	print(response.json()[0])
	domain = email[1]
	login = email[0]
	print(f"Waiting {wait}s to check inbox...")
	for i in tqdm(range(wait)):
		time.sleep(1)
	response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
	if response.status_code == 200:
		if len(response.json()) == 0:
			quit()
		m_i = response.json()[0]['id']
		url = f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={m_i}'
		response = requests.get(url)
		if response.status_code == 200:
			print(response.json())
			quit()

