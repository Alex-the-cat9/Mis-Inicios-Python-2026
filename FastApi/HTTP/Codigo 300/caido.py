from requests import get
import webbrowser
url = "http://127.0.0.1:8000"
ver = get(url, allow_redirects=False)
print(ver.headers)
if "Location" in ver.headers:
    url_rick = ver.headers["Location"]
    webbrowser.open(url_rick)
else:
    print("no se encontro")