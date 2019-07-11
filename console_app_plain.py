import sys
import requests
import os

def main():
    try:
        args = open("written_urls.txt", "r").read().splitlines()
    except Exception as ex:
        print(ex)
        return
    print("Downloading...")
    for i, arg in enumerate(args):
        _, ext = os.path.splitext(arg)
        f = open("image_" + str(i) + ext, 'wb')
        temp = requests.get(arg).content
        f.write(temp)

if __name__ == '__main__':
    main()



# run: python console_app_plain.py