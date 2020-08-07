import requests

r = requests("https://www.schoology.com/")

while True:
    print(r.header)

