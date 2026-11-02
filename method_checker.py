import requests

options = input("GET POST PUT DELETE enter your method = ").lower()
url = input("ENTER YOUR URL ")

if not url.startswith("http"):
    url = "https://" + url

if options == "get":
    req = requests.get(url)
elif options == "post":
    req = requests.post(url)
elif options == "put":
    req = requests.put(url)
elif options == "delete":
    req = requests.delete(url)
else:
    print("Invalid option")
    exit()

print(req.status_code)  
