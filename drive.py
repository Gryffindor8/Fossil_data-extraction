import requests
from bs4 import BeautifulSoup

info = (
    requests.get("https://www.dropbox.com/scl/fi/xhqpesshpkbl391ihj9yv/corona-sample.docx?dl=0&rlkey"
                 "=rmgixm390me0xuj0qsjl5t8wf"))
iff = BeautifulSoup(info.content, "lxml")
name = "Dropbox - corona sample1.docx"
print(iff.text.strip() == name)
