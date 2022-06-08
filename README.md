# subd0my

Simple python script to scan for sub domains.

I have now included a smallish wordlist to get you started, from here https://github.com/theMiddleBlue/DNSenum/tree/master/wordlist

Any suggestions are very welcome.


# Installation:
You will need python3 installed & follow the instructions to install the dependencies

- Update and install pip3:
```
sudo apt update && sudo apt install python3-pip
```

- Install the required dependencies:
```
pip3 install -r requirements.txt
```

- Clone the repository:
```
git clone https://github.com/0rgis/subd0my.git
```

- Run the tool:
```
python3 subd0my.py
```


# Usage:

Form          | Description   
------------- | -------------
-h            | Help command to list all forms and usages
-d            | Domain name to scan for subdomains
-w            | Wordlist of subdomains
-o            | Filename of the output file


# Examples: 

- Help (-h):
```
python3 subd0my.py -h
```

- Basic usage(-d, -w, -o):
```
python3 subd0my.py -d google.com -w wordlist.txt -o output.txt
```


# Credits:
https://github.com/OffXec for the file output help.

https://github.com/theMiddleBlue for the wordlists.
