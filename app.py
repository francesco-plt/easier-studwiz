from requests import get
from bs4 import BeautifulSoup as bs
from sys import argv

if len(argv) < 2 or len(argv) > 3:
    print("Usage: {} <url> [<download_path>]".format(argv[0]))
    exit(1)

# "https://www.studwiz.com/notes/polimi/engineering/05-computer-engineering/subject-208/index.php"
base_url = argv[1]
xpath = '//*[@id="postsGroup"]'
soup = bs(get(base_url).text, "html.parser")

# getting all pdf links
links = []
parent = soup.find("div", class_="postsGroup")
for res in parent.find_all("a"):
    path = res.get("href").replace(".html", ".pdf").replace("viewer", "uploads")
    links.append(base_url.replace("index.php", path))
print("found {} links".format(len(links)))
if len(links) == 0:
    print("no links found")
    exit(1)

# and downloading them
if len(argv) == 3:
    print("downloading to {}".format(argv[2]))
    for link in links:
        dlpath = argv[2]
        open(dlpath + "/" + link.split("/")[-1], "wb").write(get(link).content)
        print("downloaded {}".format(link))
else:
    for i in links:
        print(i)
