'''Sample input :
    python3 location_tracker.py -i www.google.com
    python3 location_tracker.py -i <ANY IP ADDRESS>'''

'''Install requests before running'''


import requests
import argparse
import json

if __name__ == "__main__":

    #parsing arguments
    parser = argparse.ArgumentParser()

    #adding help
    parser.add_argument("-i", "--ipaddress", help="IP address to track")

    #variable for arguments
    args = parser.parse_args()

    #variable for ip-address
    ip = args.ipaddress

    #Forming a url using args and ip variables
    url = "http://ip-api.com/json/" + ip

    #getting response in json format
    response = requests.get(url)

    data = json.loads(response.content)

    #displaying data here
    print("\t[+] IP\t\t\t", data["query"])
    print("\t[+] CITY\t\t", data["city"])
    print("\t[+] ISP\t\t\t", data["isp"])
    print("\t[+] LOC\t\t\t", data["country"])
    print("\t[+] REG\t\t\t", data["regionName"])
    print("\t[+] TIME\t\t", data["timezone"])
    print("\t[+] ZIP\t\t\t", data["zip"])
    print("\t[+] LAT\t\t\t", data["lat"])
    print("\t[+] LONG\t\t", data["lon"])