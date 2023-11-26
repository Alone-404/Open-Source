import os

try:
	import requests
except ImportError:
	os.system("pip install requests")

def download():
	os.system("clear")
	print("Script Downloader From Github")
	print("----------------------------")
	download_path = input("Enter Download Path : ")
	download_url = input("Enter Download Url : ")
	try:
		script = requests.get(download_url).text
		open(download_path, "a").write(f"#Downloaded By Mr Kazim\n{script}")
	except Exception as error:
		print(error)
	print("----------------------------")
	print("Successfully Downloaded")
	print("----------------------------")
	exit()

download()