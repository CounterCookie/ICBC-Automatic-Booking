import json, requests

session = requests.Session()

def findServices():
    # TODO
    # Change this to a system argument after
    serviceLetter = 'B'
    # TODO
    servicesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/services'
    with session.get(servicesURL, headers=httpHeaders) as unparsedServices:
        services = json.loads(unparsedServices.text)
    for service in services:
        # Match the first letter of the object 'name'
        if service['name'][0] == serviceLetter:
            # escaped this var out of the function to global only, the rest aren't needed.
            global serviceID
            global serviceQPID
            global serviceName
            serviceID = service['publicId']
            serviceQPID = service['qpId']
            serviceName = service['name']
            return serviceID

def findBranches():
    # TODO
    # Change this to a system argument after
    branchPostalCode = 'V7P3E5'
    # TODO
    branchesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/available;servicePublicId=' + serviceID

    with session.get(branchesURL, headers=httpHeaders) as unparsedCities:
        cities = json.loads(unparsedCities.text)

    for city in cities:
        # Replace spaces with nothing
        if city['addressZip'].replace(" ", "") == branchPostalCode.replace(" ", ""):
            global cityID
            cityID = city['id']
            return cityID


def findDates():
    # TODO
    # Change this to a system argument after
    min_day = '28'
    max_day = '29'
    year_month = '2021-11-'
    # TODO
    datesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + cityID + '/dates;servicePublicId=' + serviceID  + ';customSlotLength=10'

    with session.get(datesURL, headers=httpHeaders) as unparsedDates:
        dates = json.loads(unparsedDates.text)
    for d in range(int(min_day), int(max_day)+1):     
        chosenDate = year_month + (str(d).zfill(2))
        for date in dates:
            if date['date'] == chosenDate:
                global dateID
                dateID = date['date']
                print(dateID)
                return dateID
    print("date not found")
    #TODO
    exit(1)


def findTimes():
    # The hours are in 24 hour format
    # TODO
    # Change this to a system argument after
    min_hour = '15'
    max_hour = '17'
    # TODO
    timesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + cityID + '/dates/' + dateID  + '/times;servicePublicId=' + serviceID  + ';customSlotLength=40'

    with session.get(timesURL, headers=httpHeaders) as unparsedTimes:
        times = json.loads(unparsedTimes.text)
    for h in range(int(min_hour), int(max_hour)+1):
        for m in range(60):
            hm = str(h).zfill(2) + ":" + str(m).zfill(2)
            for time in times:
                if str(hm) == time['time']:
                    chosenTime = time
                    global chosen_hour_min
                    chosen_hour_min = chosenTime['time']
                    print(chosenTime)
                    return chosenTime



def reserve():
    formData = str('{"services":[{"publicId":"' + serviceID  + '"}],"custom":"{\\"peopleServices\\":[{\\"publicId\\":\\"' + serviceID  + '\\",\\"qpId\\":\\"' + serviceQPID  + '\\",\\"adult\\":1,\\"name\\":\\"' + serviceName  + '\\",\\"child\\":0}]}"}').encode('utf-8')

    reserveURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + cityID + '/dates/' + dateID + '/times/' + chosen_hour_min  + '/reserve;customSlotLength=40'

    with session.post(reserveURL, headers=httpHeaders, data=formData) as reserveUnparsed:
        reserveParsed =  json.loads(reserveUnparsed.text)
        global reservePublicId
        reservePublicId = reserveParsed['publicId']
        print("Reserve Token: " + reservePublicId)


def checkMultiple():
    checkMultipleURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/checkMultiple;phone=' + phoneNumber  + ';email=' + emailAddress  + ';firstName=' + firstName  + ';lastName=' + lastName  + ';branchPublicId=' + cityID  + ';servicePublicId=' + serviceID  + ';date=' + dateID + ';time=' + chosen_hour_min

    with session.get(checkMultipleURL, headers=httpHeaders) as checkMultiple:
        response = json.loads(checkMultiple.text)
        
    if response['message'] == 'ERROR_MULTI_GLOBAL':
        print("Customer already exists.")
        exit(1)




def matchCustomer():
    formData = str('{"email":\"' + emailAddress  + '\","phone":\"' + phoneNumber  + '\","firstName":\"' + firstName  + '\","lastName":\"' + lastName  + '\","dateOfBirth":\"' + datesOfBirth  + '\","externalId":""}').encode('utf-8')

    matchCustomerURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/matchCustomer'

    with session.post(matchCustomerURL, headers=httpHeaders, data=formData) as match:
        response = json.loads(match.text)
    if response['allowOverwrite'] != False:
        print("Not allowed to overwrrite(?)")
        exit(1)


def bookAndConfirm():
    formData = str('{"customer":{"firstName":"' + firstName  + '","lastName":"' + lastName  + '","dateOfBirth":"' + datesOfBirth  + '","email":"' + emailAddress  + '","phone":"' + phoneNumber  + '","dob":"","externalId":""},"languageCode":"en","countryCode":"ca","notificationType":"","captcha":"","custom":"{\\"peopleServices\\":[{\\"publicId\\":\\"' + serviceID  + '\\",\\"qpId\\":\\"' + serviceQPID  + '\\",\\"adult\\":1,\\"name\\":\\"' + serviceName  + '\\",\\"child\\":0}],\\"totalCost\\":0,\\"createdByUser\\":\\"Qmatic Web Booking\\",\\"paymentRef\\":\\"\\",\\"customSlotLength\\":40}","notes":"","title":"Qmatic Web Booking"}').encode('utf-8')

    confirmUrl = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/' + reservePublicId  + '/confirm'
    with session.post(confirmUrl, headers=httpHeaders, data=formData) as confirm:
        print(confirm.text)
    




# Set and get initial cookies and X-token required throughout form completion
with session.get("https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/configuration") as initConfig:
    openToken = json.loads(initConfig.text)['token']

    httpHeaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, l ike Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Content-Type': 'application/json', 'X-CSRF-Token': openToken, 'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8', 'Connection': 'keep-alive', 'Host': 'onlinebusiness.icbc.com', 'Origin': 'https://onlinebusiness.icbc.com', 'Referer': 'https://onlinebusiness.icbc.com/qmaticwebbooking/', 'Sec-Fetch-Site': 'same-origin'}

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

    findServices()
    findBranches()
    findDates()
    findTimes()
    reserve()
    checkMultiple()
    matchCustomer()
    bookAndConfirm()
