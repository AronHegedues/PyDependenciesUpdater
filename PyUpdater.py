import requests
import pkg_resources
from subprocess import call
from termcolor import colored
from bs4 import BeautifulSoup

try:

    # get all dependencies and upgrade them
    packages = [dist.project_name for dist in pkg_resources.working_set]
    call("python.exe -m pip install --upgrade " + ' '.join(packages), shell=True)

except:
    print(colored("[Warning] Failed to upgrade package!", "yellow"))

# scrape Python version from website
response = requests.get("https://www.python.org/downloads/")

soup = BeautifulSoup(response.text, "html5lib")
aTag = soup.findAll('a')[79]

# format the version
txt = str(aTag).split("\n")[0].replace("</a>", "")
txt = txt.split(" ")

localVersion = sys.version.split(" ")[0]
localVersion = localVersion.replace(".", "")

version = txt[len(txt) - 1].replace(".", "")

# compare the versions
if int(version) > int(localVersion):
    print(colored("\n[Warning] Python is outdated!", "yellow"))

else:
    print(colored("\n[Okay] Python is up to date!", "green"))

time.sleep(1)
