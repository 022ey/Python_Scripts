import requests
import json 
import datetime
import openpyxl

__author__ = 'RVSB'

STATE = 'Karnataka'
DISTRICT = 'Tumkur'
AGE_LIMIT = 18




base_url = 'https://cdn-api.co-vin.in/api/v2'

endpoints = {

'meta_states' : '/admin/location/states',
'meta_districts' : '/admin/location/districts/{id}', # State_ID
'availability_district' : '/appointment/sessions/public/calendarByDistrict/?district_id={district_id}&date={date}' # date = dd-mm-yyyy

}



headers = {
   "Connection": "keep-alive",
   "Pragma": "no-cache",
   "Cache-Control": "no-cache",
   "sec-ch-ua-mobile": "?0", 
   "DNT": "1", 
   "Upgrade-Insecure-Requests": "1",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51", 
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
   "Sec-Fetch-Site": "none" ,
   "Sec-Fetch-Mode": "navigate", 
   "Sec-Fetch-User": "?1" ,
   "Sec-Fetch-Dest": "document", 
   "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8" 

}

def get_jsons( endpoint, data=None) :
    if data :
        print( endpoints[endpoint].format(**data))
        request = requests.get(base_url + endpoints[endpoint].format(**data), headers=headers )
    else:
        request = requests.get(base_url + endpoints[endpoint], headers=headers )
    if request.status_code == 200:
        return json.loads(request.content)

    else:
        print("error occured at", base_url + endpoints[endpoint])




states = {    state['state_name']:state['state_id'] for state in    get_jsons('meta_states')['states'] }

print(states)

districts =  {   district['district_name']:district['district_id'] for district in  get_jsons('meta_districts', { 'id' : states[STATE]})['districts'] }


#whilte True:
present = datetime.datetime.now()
availability_district = get_jsons('availability_district', { 'district_id' : districts[DISTRICT], 'date' : present.strftime('%d-%m-%Y' )} )


from collections import OrderedDict
avails = OrderedDict()

for centre in availability_district['centers']:
    for session in centre['sessions']:
        if session['available_capacity'] > 0 and session['min_age_limit'] <= AGE_LIMIT:
            data = {}
            data['hospital'] = centre['name']
            data['address']  = centre['address']
            data['fee_type'] = centre['fee_type']
            data['capacity'] = session['available_capacity']
            data['age']      = session['min_age_limit']
            if session['date'] in avails:
                avails[session['date']].append(data)
            else:
                avails[session['date']] = [data]



workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(['Hospital Name', 'Address', 'Date',  'Capacity',  'Minimum Age', 'Fee Type'])


data = []
for date in avails:
     for slot in avails[date]:
        data.append([slot['hospital'], slot['address'], date, slot['capacity'], slot['age'], slot['fee_type']])

data.sort(key=lambda x: (x[2], -1*x[3]))

for x in data:
   sheet.append(x)

workbook.save('slots.xlsx')
    