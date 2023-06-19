import sys
import os
import wget
import click
from dotenv import load_dotenv
import requests 
from win10toast import ToastNotifier

load_dotenv()
# @click.group()
# def commands():
# 	pass

#config=dotenv_values(".env")

@click.command(epilog="Copyright @ Cisco(github.com/cisco100)")
@click.option("-u","--url",type=str,prompt="Paste your downoad link here to download ::>" ,help="""Paste the download link of the file you want to download""")
#@click.option("-q","--quit",type=str,prompt="Are you sure you want to cancel the download ??,[y/n]",help="Enter `y/Y` to cancel the download")
def download_file(url):
	toaster=ToastNotifier()
	download_link=str(url)

	try:
	 request = requests.get(download_link)
	 
	except requests.ConnectionError as e:
		click.echo("OOPS!! ConnectionError.")
	except requests.Timeout as e:
		click.echo("OOPS!! Timeout ")
	except requests.RequestException as e:
		click.echo("OOPS!! GeneralError or InvalidURL")
	except (KeyboardInterrupt, SystemExit):
			quit=str(input("Are you sure you want to cancel the download ??,[y/n]"))
			if quit=="y" or "Y":
				sys.exit(1)
			elif quit=='n' or 'N':
				click.echo("Continnuing...")
	# except TypeError:
	# 	click.echo("Can't download this file")
	else:
		click.echo("Download starting in a few seconds")
		click.echo("[+] File Started Downloading")
		wget.download(download_link, "download")
	toaster.show_toast(title='blazeGetz', msg='Download Done', icon_path=os.getenv("IMG_PATH ") or "assets/cloud-download.ico", duration=5, threaded=True)

# commands.command(download_file)
# commands.add_command(quit_download)

if __name__=="__main__":
	#commands()
	download_file()




