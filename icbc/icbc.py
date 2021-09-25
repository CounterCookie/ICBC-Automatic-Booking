import json, requests

# So we're not very obvious
http_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.0.0 Safari/537.36'}
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
            serviceid = service['publicId']
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
    min_day = '3'
    max_day = '5'
    year_month = '2021-12-'
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
                    print(chosen_time)
                    return chosen_time



# Set and get initial cookies required throughout form completion
with session.get("https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/configuration"):
    find_services()
    find_branches()
    find_dates()
    find_times()


print(session.cookies)
