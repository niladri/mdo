import sys
from base64 import b64encode

def main():
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        print("Please enter the URL as the first command line parameter")
        return
        
    urlb64 = b64encode(url.encode())
    # string encodedUrl = "u!" + base64Value.TrimEnd('=').Replace('/','_').Replace('+','-');
    encodedUrl = 'u!' + urlb64.decode().rstrip('=').replace('/','_').replace('+','-')
    print(encodedUrl)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()