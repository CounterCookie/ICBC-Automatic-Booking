import json, requests

# So we're not very obvious
session = requests.Session()

def find_services():
    # TODO
    # Change this to a system argument after
    service_letter = 'B'
    # TODO
    services_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/services'
    with session.get(services_url, headers=http_headers) as unparsed_services:
        services = json.loads(unparsed_services.text)
    for service in services:
        # Match the first letter of the object 'name'
        if service['name'][0] == service_letter:
            # escaped this var out of the function to global only, the rest aren't needed.
            global serviceid
            global service_qpid
            global service_name
            serviceid = service['publicId']
            service_qpid = service['qpId']
            service_name = service['name']
            return serviceid

def find_branches():
    # TODO
    # Change this to a system argument after
    branch_postal_code = 'V7P3E5'
    # TODO
    branches_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/available;servicePublicId=' + serviceid

    with session.get(branches_url, headers=http_headers) as unparsed_cities:
        cities = json.loads(unparsed_cities.text)

    for city in cities:
        # Replace spaces with nothing
        if city['addressZip'].replace(" ", "") == branch_postal_code.replace(" ", ""):
            global city_id
            city_id = city['id']
            return city_id


def find_dates():
    # TODO
    # Change this to a system argument after
    min_day = '28'
    max_day = '29'
    year_month = '2021-11-'
    # TODO
    dates_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + city_id + '/dates;servicePublicId=' + serviceid  + ';customSlotLength=10'

    with session.get(dates_url, headers=http_headers) as unparsed_dates:
        dates = json.loads(unparsed_dates.text)
    for d in range(int(min_day), int(max_day)+1):     
        chosen_date = year_month + (str(d).zfill(2))
        for date in dates:
            if date['date'] == chosen_date:
                global date_id
                date_id = date['date']
                print(date_id)
                return date_id
    print("date not found")
    #TODO
    exit(1)


def find_times():
    # The hours are in 24 hour format
    # TODO
    # Change this to a system argument after
    min_hour = '15'
    max_hour = '17'
    # TODO
    times_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + city_id + '/dates/' + date_id  + '/times;servicePublicId=' + serviceid  + ';customSlotLength=40'

    with session.get(times_url, headers=http_headers) as unparsed_times:
        times = json.loads(unparsed_times.text)
    for h in range(int(min_hour), int(max_hour)+1):
        for m in range(60):
            hm = str(h).zfill(2) + ":" + str(m).zfill(2)
            for time in times:
                if str(hm) == time['time']:
                    chosen_time = time
                    global chosen_hour_min
                    chosen_hour_min = chosen_time['time']
                    print(chosen_time)
                    return chosen_time



def reserve():
    form_data = str('{"services":[{"publicId":"' + serviceid  + '"}],"custom":"{\\"peopleServices\\":[{\\"publicId\\":\\"' + serviceid  + '\\",\\"qpId\\":\\"' + service_qpid  + '\\",\\"adult\\":1,\\"name\\":\\"' + service_name  + '\\",\\"child\\":0}]}"}').encode('utf-8')

    reserve_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + city_id + '/dates/' + date_id + '/times/' + chosen_hour_min  + '/reserve;customSlotLength=40'

    with session.post(reserve_url, headers=http_headers, data=form_data) as reserve_unparsed:
        reserve_parsed =  json.loads(reserve_unparsed.text)
        global reservePublicId
        reservePublicId = reserve_parsed['publicId']
        print(reservePublicId)


def checkmultiple():
    checkmultiple_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/checkMultiple;phone=' + phoneNumber  + ';email=' + emailAddress  + ';firstName=' + firstName  + ';lastName=' + lastName  + ';branchPublicId=' + city_id  + ';servicePublicId=' + serviceid  + ';date=' + date_id + ';time=' + chosen_hour_min

    with session.get(checkmultiple_url, headers=http_headers) as checkMultiple:
        response = json.loads(checkMultiple.text)
        
    if response['message'] == 'ERROR_MULTI_GLOBAL':
        print("Customer already exists.")
        exit(1)




def matchcustomer():
    form_data = str('{"email":\"' + emailAddress  + '\","phone":\"' + phoneNumber  + '\","firstName":\"' + firstName  + '\","lastName":\"' + lastName  + '\","dateOfBirth":\"' + datesOfBirth  + '\","externalId":""}').encode('utf-8')

    matchcustomer_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/matchCustomer'

    with session.post(matchcustomer_url, headers=http_headers, data=form_data) as match:
        response = json.loads(match.text)
    if response['allowOverwrite'] != False:
        print("Not allowed to overwrrite(?)")
        exit(1)


def bookAndConfirm():
    form_data = str('{"customer":{"firstName":"' + firstName  + '","lastName":"' + lastName  + '","dateOfBirth":"' + datesOfBirth  + '","email":"' + emailAddress  + '","phone":"' + phoneNumber  + '","dob":"","externalId":""},"languageCode":"en","countryCode":"ca","notificationType":"","captcha":"","custom":"{\\"peopleServices\\":[{\\"publicId\\":\\"' + serviceid  + '\\",\\"qpId\\":\\"' + service_qpid  + '\\",\\"adult\\":1,\\"name\\":\\"' + service_name  + '\\",\\"child\\":0}],\\"totalCost\\":0,\\"createdByUser\\":\\"Qmatic Web Booking\\",\\"paymentRef\\":\\"\\",\\"customSlotLength\\":40}","notes":"","title":"Qmatic Web Booking"}').encode('utf-8')

    confirm_url = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/' + reservePublicId  + '/confirm'
    with session.post(confirm_url, headers=http_headers, data=form_data) as confirm:
        print(confirm.text)
    




# Set and get initial cookies and X-token required throughout form completion
with session.get("https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/configuration") as init_config:
    open_token = json.loads(init_config.text)['token']

    http_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, l ike Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Content-Type': 'application/json', 'X-CSRF-Token': open_token, 'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8', 'Connection': 'keep-alive', 'Host': 'onlinebusiness.icbc.com', 'Origin': 'https://onlinebusiness.icbc.com', 'Referer': 'https://onlinebusiness.icbc.com/qmaticwebbooking/', 'Sec-Fetch-Site': 'same-origin'}

    global phoneNumber 
    global emailAddress
    global FirstName   
    global lastName
    global datesOfBirth

    # TODO
    # Customer info
    phoneNumber     = '12133735252'
    emailAddress    = 'shaydari20@gmail.com'
    firstName       = 'Alex'
    lastName        = 'Jones'
    datesOfBirth    = '2001-05-13'

    find_services()
    find_branches()
    find_dates()
    find_times()
    reserve()
    checkmultiple()
    matchcustomer()
    bookAndConfirm()
