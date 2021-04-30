import requests
selfVersion = 1
version = int(requests.get('https://henryruss2.github.io/update/version'))
if (selfVersion < version):
    update = requests.get('https://henryruss2.github.io/update/browser.py')
    f = open("browser.py", "w")
    f.write(update)
    f.close()
while True:
    x = requests.get(input('Enter a URL:\n'))
    x = x.text
    print('loaded!')
    print(x)
