import requests
import hashlib

def req_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char # it'll look for all the passwords which has same first five hash characters
    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f"Error code {res.status_code} chck the api and try again")
    return res

def get_pass_leak_counts(hashes,hash_to_chck):
    hashes=(line.split(":") for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_chck:
            return count
    return 0


def pwned_api_chck(password):
    #check password if its exists in Api response
    sha1password=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5,remaining=sha1password[:5],sha1password[5:]
    response = req_api_data(first5)
    print(first5,remaining)
    return get_pass_leak_counts(response,remaining)

with open("test.txt") as a:
    list=[]
    for l in a:
        print(l)
        line_list=l.split()
        list.append(line_list)
    print(list)

    def main(args):
        for i in list:
            for password in i:
                count = pwned_api_chck(password)
            if count:
                print(f"{password} was found {count} times... you should probably chhange password")
            else:
                print(f"{password} never hacked")

    if __name__ == "__main__":
        main(list)
