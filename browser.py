while True:
    import requests
    x = requests.get(input('Enter a URL:\n'))
    x = x.text
    print(x)
