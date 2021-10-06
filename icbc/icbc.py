#!/usr/bin/python
import json, requests, argparse, re, time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


session = requests.Session()
# Set max retries
retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504, 403, 404 ])
session.mount('https://', HTTPAdapter(max_retries=retries))

parser = argparse.ArgumentParser()

# Important regex
yearAndMonthRegex = re.compile('[0-9]{4}\-[0-9]{2}\-')
dateOfBirthRegex = re.compile('[0-9]{4}\-[0-9]{2}\-[0-9]{2}')
phoneNumberRegex = re.compile('[0-9]{11}')
emailAddressRegex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')


argsToBeSet = ["--service", "--branch", "--minDay", "--maxDay", "--yearAndMonth", "--minHour", "--maxHour", "--phoneNum", "--email", "--first", "--last", "--dob"]

for i in argsToBeSet: 
    parser.add_argument(i, required=True)
    

args = parser.parse_args()
serviceLetter = args.service
branchPostalCode = args.branch
minDay = args.minDay
maxDay = args.maxDay

if yearAndMonthRegex.match(args.yearAndMonth):
    yearAndMonth = args.yearAndMonth
else:
    print("Year and month syntax wrong.")
    exit(1)

minHour = args.minHour
maxHour = args.maxHour



if phoneNumberRegex.match(args.phoneNum):
    phoneNumber     = args.phoneNum
else:
    print("Wrong phone number.")
    exit(1)


if emailAddressRegex.match(args.email):
    emailAddress = args.email
else:
    print("Email address syntax wrong.")
    exit(1)
firstName       = args.first
lastName        = args.last
if dateOfBirthRegex.match(args.dob):
    dateOfBirth = args.dob
else:
    print("Date of birth syntax wrong.")
    exit(1)

#print(serviceLetter, branchPostalCode, minHour, maxHour, minDay, maxDay, yearAndMonth, phoneNumber, emailAddress, firstName, lastName, dateOfBirth)


def findServices():
    servicesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/services'
    with session.get(servicesURL, headers=httpHeaders) as unparsedServices:
        services = json.loads(unparsedServices.text)

        status = str(unparsedServices.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")

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
    # The above return makes the function return a value and does not make it do anymore. in case of that failure, exit
    print("Service ID could not be set, wrong name first letter? eg. B")
    exit(1)

def findBranches():
    branchesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/available;servicePublicId=' + serviceID

    with session.get(branchesURL, headers=httpHeaders) as unparsedCities:
        cities = json.loads(unparsedCities.text)

        status = str(unparsedCities.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")

    for city in cities:
        # Replace spaces with nothing
        if city['addressZip'].replace(" ", "") == branchPostalCode.replace(" ", ""):
            global cityID
            cityID = city['id']
            return cityID
    # The above return makes the function return a value and does not make it do anymore. in case of that failure, exit
    print("Postal code not found or cityID for the service could not be set; These cities provide it though:")
    for availableCity in cities:
        print(availableCity['addressCity'] + ' : ' + availableCity['addressLine1'] + ' : ' + availableCity['addressZip'])
    exit(1)
            


def findDates():
    datesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + cityID + '/dates;servicePublicId=' + serviceID

    with session.get(datesURL, headers=httpHeaders) as unparsedDates:
        dates = json.loads(unparsedDates.text)

        status = str(unparsedDates.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")

    for d in range(int(minDay), int(maxDay)+1):     
        chosenDate = yearAndMonth + (str(d).zfill(2))
        for date in dates:
            if date['date'] == chosenDate:
                global dateID
                dateID = date['date']
                print(dateID)
                return dateID
    print("No Date")
    raise Exception("Error")

def findTimes():
    timesURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + cityID + '/dates/' + dateID  + '/times;servicePublicId=' + serviceID

    with session.get(timesURL, headers=httpHeaders) as unparsedTimes:
        times = json.loads(unparsedTimes.text)

        status = str(unparsedTimes.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")

    for h in range(int(minHour), int(maxHour)+1):
        for m in range(60):
            hm = str(h).zfill(2) + ":" + str(m).zfill(2)
            for time in times:
                if str(hm) == time['time']:
                    chosenTime = time
                    global chosenHourAndMinutes
                    chosenHourAndMinutes = chosenTime['time']
                    print(chosenTime)
                    return chosenTime
    print("No Time")
    raise Exception("Error")


def reserve():
    formData = str('{"services":[{"publicId":"' + serviceID  + '"}],"custom":"{\\"peopleServices\\":[{\\"publicId\\":\\"' + serviceID  + '\\",\\"qpId\\":\\"' + serviceQPID  + '\\",\\"adult\\":1,\\"name\\":\\"' + serviceName  + '\\",\\"child\\":0}]}"}').encode('utf-8')

    reserveURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/' + cityID + '/dates/' + dateID + '/times/' + chosenHourAndMinutes  + '/reserve'

    with session.post(reserveURL, headers=httpHeaders, data=formData) as reserveUnparsed:

        status = str(reserveUnparsed.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")
        reserveParsed =  json.loads(reserveUnparsed.text)
        global reservePublicId
        reservePublicId = reserveParsed['publicId']
        print("Reserve Token: " + reservePublicId)


def checkMultiple():
    checkMultipleURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/checkMultiple;phone=' + phoneNumber  + ';email=' + emailAddress  + ';firstName=' + firstName  + ';lastName=' + lastName  + ';branchPublicId=' + cityID  + ';servicePublicId=' + serviceID  + ';date=' + dateID + ';time=' + chosenHourAndMinutes

    with session.get(checkMultipleURL, headers=httpHeaders) as checkMultiple:
        response = json.loads(checkMultiple.text)

        status = str(checkMultiple.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")

        
    if response['message'] == 'ERROR_MULTI_GLOBAL':
        print("Customer already exists.")
        raise Exception("Error")




def matchCustomer():
    formData = str('{"email":\"' + emailAddress  + '\","phone":\"' + phoneNumber  + '\","firstName":\"' + firstName  + '\","lastName":\"' + lastName  + '\","dateOfBirth":\"' + dateOfBirth  + '\","externalId":""}').encode('utf-8')

    matchCustomerURL = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/matchCustomer'

    with session.post(matchCustomerURL, headers=httpHeaders, data=formData) as match:

        status = str(match.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")

        response = json.loads(match.text)
    if response['allowOverwrite'] != False:
        print("Not allowed to overwrrite(?)")
        raise Exception("Error")

def bookAndConfirm():
    formData = str('{"customer":{"firstName":"' + firstName  + '","lastName":"' + lastName  + '","dateOfBirth":"' + dateOfBirth  + '","email":"' + emailAddress  + '","phone":"' + phoneNumber  + '","dob":"","externalId":""},"languageCode":"en","countryCode":"ca","notificationType":"","captcha":"","custom":"{\\"peopleServices\\":[{\\"publicId\\":\\"' + serviceID  + '\\",\\"qpId\\":\\"' + serviceQPID  + '\\",\\"adult\\":1,\\"name\\":\\"' + serviceName  + '\\",\\"child\\":0}],\\"totalCost\\":0,\\"createdByUser\\":\\"Qmatic Web Booking\\",\\"paymentRef\\":\\"\\",\\"customSlotLength\\":40}","notes":"","title":"Qmatic Web Booking"}').encode('utf-8')

    confirmUrl = 'https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/' + reservePublicId  + '/confirm'

    # Spirits away
    with session.post(confirmUrl, headers=httpHeaders, data=formData) as book:

        status = str(book.status_code)
        if status != "200":
            print("HTTP error: " + status)
            raise Exception("Error")
            exit(1)

    print("Booked")
    




# Set and get initial cookies and X-token required throughout form completion
with session.get("https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/configuration") as initConfig:
    print("\n\n\n\n\n")
    status = str(initConfig.status_code)
    if status != "200":
        print("HTTP error: " + status)
        raise Exception("Http 403 Error")

    openToken = json.loads(initConfig.text)['token']

    httpHeaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, l ike Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Content-Type': 'application/json', 'X-CSRF-Token': openToken, 'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8', 'Connection': 'keep-alive', 'Host': 'onlinebusiness.icbc.com', 'Origin': 'https://onlinebusiness.icbc.com', 'Referer': 'https://onlinebusiness.icbc.com/qmaticwebbooking/', 'Sec-Fetch-Site': 'same-origin'}


    findServices()
    findBranches()
    tryNum = 0
    while True:
        while True:
            try:
                matchCustomer()
                findDates()
                findTimes()
                checkMultiple()
            except:
                tryNum += 1
                print("Time or date not found; try count:  ", tryNum)
                time.sleep(10)
                break
            reserve()
            checkMultiple()
            matchCustomer()
            bookAndConfirm()
            exit(0)
