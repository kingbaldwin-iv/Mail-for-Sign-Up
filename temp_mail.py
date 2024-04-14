import requests
from clint.textui import prompt
from tabulate import tabulate
import pandas as pd


class Mail_Gen():

	def __init__(self):
		print("Welcome to Mail Generator!")
		self.action = prompt.options("Pick Action:", ["Generate and Recieve E-Mail"],default = '1')
		if self.action == 1:
			response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
			if response.status_code == 200:
				email = response.json()[0].split("@")
				print("Generated Email:")
				print(response.json()[0])
				self.domain = email[1]
				self.login = email[0]
				self.option = prompt.options("Ready to Check Inbox:", ["Yes","No"],default = '1')
				while self.option == 2:
					self.option = prompt.options("Ready to Check Inbox:", ["Yes","No"],default = '1')
				url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}'
				response = requests.get(url)
				if response.status_code == 200:
					inbox = response.json()
					print(inbox)
					ids = [a['id'] for a in inbox] + [-1]
					if len(ids) == 1:
						print("empty inbox")
						return
					self.action2 = prompt.options("Pick Email To Look At:", ids) 
					if self.action2 > len(inbox): return
					url = f'https://www.1secmail.com/api/v1/?action=readMessage&login={self.login}&domain={self.domain}&id={ids[self.action2-1]}'
					response = requests.get(url)
					if response.status_code == 200:
						print(response.json())
						return
					else:
						print("Error:", response.status_code)
						return
				else:
					print("Error:", response.status_code)
					return
			else:
				print("Error:", response.status_code)
				return

		





if __name__ == '__main__':
	Mail_Gen()
