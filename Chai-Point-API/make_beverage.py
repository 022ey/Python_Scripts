from subprocess import Popen, PIPE, STDOUT




def make_order(beverage, qr=None):

    url = f'https://api.boxc.in/boxc/qr/scan?qrCodeId={qr}'
    cmd = 'curl -i -s ' + url + ' | grep location | cut -d " " -f 2'

    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    temp_url = p.stdout.read().decode().strip()
    print(temp_url)



    session_id =  temp_url.rsplit('/')[-1]


    request = f'''
    curl 'https://api.boxc.in/boxc/microsite/triggerDispense?optionId={beverage}&isPaid=false' \
    -H 'Connection: keep-alive' \
    -H 'Pragma: no-cache' \
    -H 'Cache-Control: no-cache' \
    -H 'Accept: application/json, text/plain, */*' \
    -H 'DNT: 1' \
    -H 'sessionId: {session_id}' \
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56' \
    -H 'Origin: https://microsite.boxc.in' \
    -H 'Sec-Fetch-Site: same-site' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Referer: https://microsite.boxc.in/' \
    -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8' \
    --compressed ;

    curl 'https://api.boxc.in/boxc/microsite/triggerDispense?optionId={beverage}&isPaid=false' \
    -X 'OPTIONS' \
    -H 'Connection: keep-alive' \
    -H 'Pragma: no-cache' \
    -H 'Cache-Control: no-cache' \
    -H 'Accept: */*' \
    -H 'Access-Control-Request-Method: GET' \
    -H 'Access-Control-Request-Headers: sessionid' \
    -H 'Origin: https://microsite.boxc.in' \
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Site: same-site' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Referer: https://microsite.boxc.in/' \
    -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8' \
    --compressed ;

    curl 'https://api.boxc.in/boxc/microsite/validateSession' \
   -X 'OPTIONS' \
   -H 'Connection: keep-alive' \
   -H 'Pragma: no-cache' \
   -H 'Cache-Control: no-cache' \
   -H 'Accept: */*' \
   -H 'Access-Control-Request-Method: GET' \
   -H 'Access-Control-Request-Headers: sessionid' \
   -H 'Origin: https://microsite.boxc.in' \
   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56' \
   -H 'Sec-Fetch-Mode: cors' \
   -H 'Sec-Fetch-Site: same-site' \
   -H 'Sec-Fetch-Dest: empty' \
   -H 'Referer: https://microsite.boxc.in/' \
   -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8' \
   --compressed ;

   curl 'https://api.boxc.in/boxc/microsite/validateSession' \
   -H 'Connection: keep-alive' \
   -H 'Pragma: no-cache' \
   -H 'Cache-Control: no-cache' \
   -H 'Accept: application/json, text/plain, */*' \
   -H 'DNT: 1' \
   -H 'sessionId: {session_id}' \
   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56' \
   -H 'Origin: https://microsite.boxc.in' \
   -H 'Sec-Fetch-Site: same-site' \
   -H 'Sec-Fetch-Mode: cors' \
   -H 'Sec-Fetch-Dest: empty' \
   -H 'Referer: https://microsite.boxc.in/' \
   -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8' \
   --compressed

   '''

    import os
    os.system(request)


if __name__ == '__main__':



    beverages = {  'tea' : 1, # add remaining later on
                  'strong chai': 2,
                  'filter coffee' :3,
                   'strong coffee': 4,
                   'black chai': 5,
                    'black coffee': 6,
                    'milk' : 7,
                   'water' : 8
                }


    make_order(beverages['tea'], 'XXXYY')   # find qr on the chai point machine
