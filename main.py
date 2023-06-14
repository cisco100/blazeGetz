import sys
import os
import wget
import requests 
from win10toast import ToastNotifier
toaster=ToastNotifier()
download_link=str(input("Paste your downoad link here to download ::> "))

try:
 request = requests.get(download_link)
 
except requests.ConnectionError as e:
	print("OOPS!! ConnectionError.")
except requests.Timeout as e:
	print("OOPS!! Timeout ")
except requests.RequestException as e:
	print("OOPS!! GeneralError or InvalidURL")
except (KeyboardInterrupt, SystemExit):
	quit=str(input("Are you sure you want to cancel the download ??,[y/n]"))
	if quit=='y':
		sys.exit(1)
	else:
		print("Continnuing...")
except TypeError:
	print("Can't download this file")
else:
	print("Download starting in a few seconds")
	print("[+] File Started Downloading")
	wget.download(download_link, "download")
toaster.show_toast(title='blazeGetz', msg='Download Done', icon_path="assets/cloud-download.ico", duration=5, threaded=True)




