# method_checker.py-
A simple Python script to make HTTP requests (GET) and fetch website data using the requests library. 


import requests
options = input("GET  POST  PUT  DELETE  ENTER YOUR METHOD =   ").lower()
if options == "get":
    url  = input("ENTER YOUR URL ")
    req = requests.get(url)
    print(req.status_code)
elif options == "post":
    url = input("ENTER YOUR URL ")
    req = requests.post(url)
    print(req.status_code)
elif options == "put":
    url = input("ENTER YOUR URL ")
    req = requests.put(url)
    print(req.status_code)
elif options == "delete":
    url = input("ENTER YOUR URL ")
    req = requests.delete(url)
    print(req.status_code)

    if not url.startswith("http"):
        url = "https://" + url

else:
    print("Invalid option")

