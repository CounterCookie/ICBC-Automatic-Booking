import requests

s = requests.Session()

s.headers.update(
    {
        "Host": "onlinebusiness.icbc.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "sec-ch-ua-platform": '"Linux"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://onlinebusiness.icbc.com/qmaticwebbooking/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cookie": "TS017453c8=01de3c983f5a243982ab33190084bd0a2978bc2751177406c1b99c8a285c8a6d75ceec470e8586d2beb1b084e5a037f956f4e573b2; JSESSIONID=93E0991F7E77B9DD5BE7F5C6944467E7; BIGipServer~ctn-e-018-prt~dlqwebprd-8080-iapp.app~dlqwebprd-8080-iapp_pool=rd3136o00000000000000000000ffff0aa58a28o8090; TS01eacd98=01de3c983f1eaa5777ab032ec21ec3334206aad156599d2a42897ea656788d8f399c7c44f4b589663ff36671b737bd5d56dd161a23",
    }
)

r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/available;servicePublicId=da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25",
)
# [
#   {
#     "addressCity": "Abbotsford",
#     "addressLine1": "31935 South Fraser Way",
#     "addressLine2": "Unit 150",
#     "addressZip": "V2T 5N7",
#     "custom": "{\"names\":{\"en\":\"Abbotsford\"}}",
#     "id": "7ca7e51b73b388a05f1d86a1d69f113272388294d514d3bfb71e8a2cc11db379",
#     "internalId": 1,
#     "name": "Abbotsford",
#     "qpId": "10",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Burnaby",
#     "addressLine1": "3880 Lougheed Highway",
#     "addressZip": "V5C6N4",
#     "custom": "{\"names\":{\"en\":\"Burnaby Lougheed\"}}",
#     "id": "53851ce8b410de56e26a0f0d2eda5a3e8d8cf4e05cc1b21af70121f53ef53b5d",
#     "internalId": 2,
#     "name": "Burnaby",
#     "qpId": "11",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Vancouver",
#     "addressLine1": "2750 Commercial Drive",
#     "addressZip": "V5N5P4",
#     "custom": "{\"names\":{\"en\":\"Vancouver Commercial Drive\"}}",
#     "id": "0ab916058f4b572eae9dfbdf0693fa9f2f97a34a19bee6c68d09cb28b78ac3c3",
#     "internalId": 3,
#     "name": "East Van",
#     "qpId": "9",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Surrey",
#     "addressLine1": "15285 - 101St Avenue",
#     "addressZip": "V3R 8X7",
#     "custom": "{\"names\":{\"en\":\"Surrey Guildford\"}}",
#     "id": "050a91560b08e8aedfef609cb69e0c41469b56e575f325681f98196495169661",
#     "internalId": 4,
#     "name": "Guildford",
#     "qpId": "19",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Kamloops",
#     "addressLine1": "937 Concordia Way",
#     "addressZip": "V2C 6V3",
#     "custom": "{\"names\":{\"en\":\"Kamloops\"}}",
#     "id": "b0e64a9abb67d579f5f1770343b057ee5dcfdaf229bb2607e30d9431a8d0535a",
#     "internalId": 5,
#     "name": "Kamloops",
#     "qpId": "18",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Kelowna",
#     "addressLine1": "1720 Springfield Road",
#     "addressZip": "V1Y 7W2",
#     "custom": "{\"names\":{\"en\":\"Kelowna\"}}",
#     "id": "32aff282e91ef1025580faae9be41ef790f218c69900d768e6a72e204ad1f5c9",
#     "internalId": 6,
#     "name": "Kelowna",
#     "qpId": "6",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Langley",
#     "addressLine1": "19950 Willowbrook Drive",
#     "addressLine2": "Unit 7",
#     "addressZip": "V2Y 1K9",
#     "custom": "{\"names\":{\"en\":\"Langley-Willowbrook\"}}",
#     "id": "09863cca687e2a677911a7e9d1b88c55eaba7b13c862bd9da8eca1426855ef1d",
#     "internalId": 7,
#     "name": "Langley-Willowbrook",
#     "qpId": "16",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Burnaby",
#     "addressLine1": "4820 Kingsway",
#     "addressLine2": "232",
#     "addressZip": "V5H 4P2",
#     "custom": "{\"names\":{\"en\":\"Burnaby Metrotown\"}}",
#     "id": "e879cd70e75ba8db2fb03b3d2060bf7c1c74e5d879ebea3cc585fd2d707a278d",
#     "internalId": 8,
#     "name": "Metrotown",
#     "qpId": "15",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Nanaimo",
#     "addressLine1": "6475 Metral Drive",
#     "addressLine2": "102",
#     "addressZip": "V9T 2L9",
#     "custom": "{\"names\":{\"en\":\"Nanaimo\"}}",
#     "id": "fe8bedd02aa78334a4d223ebc8dd9f948340a2b471dce12ec52ea88e1c8ec782",
#     "internalId": 9,
#     "name": "Nanaimo",
#     "qpId": "14",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "North Vancouver",
#     "addressLine1": "1331 Marine Drive",
#     "addressZip": "V7P 3E5",
#     "custom": "{\"names\":{\"en\":\"North Vancouver\"}}",
#     "id": "80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3",
#     "internalId": 10,
#     "name": "North Vancouver",
#     "qpId": "4",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Vancouver",
#     "addressLine1": "4126 Macdonald Street",
#     "addressZip": "V6L 2P2",
#     "custom": "{\"names\":{\"en\":\"Vancouver Point Grey\"}}",
#     "id": "542161df66423009309050c01dcc17f7d1db1ef8e7cea3012331509b79ea6959",
#     "internalId": 11,
#     "name": "Point Grey",
#     "qpId": "12",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Port Coquitlam",
#     "addressLine1": "1930 Oxford Connector",
#     "addressZip": "V3C 0A4",
#     "custom": "{\"names\":{\"en\":\"Port Coquitlam\"}}",
#     "id": "b40103f18229d5654343c6813aa147e8057cb2838e460530f136e3851bf5fa41",
#     "internalId": 12,
#     "name": "Port Coquitlam",
#     "qpId": "7",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Richmond",
#     "addressLine1": "5300 No. 3 Road",
#     "addressLine2": "Suite 402",
#     "addressZip": "V6X 2X9",
#     "custom": "{\"names\":{\"en\":\"Richmond\"}}",
#     "id": "b1d4daefba2458c80d880e3931798ef508477d19f6cf1652327459a4a1a27ee3",
#     "internalId": 13,
#     "name": "Richmond",
#     "qpId": "13",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Vancouver",
#     "addressLine1": "1055 West Georgia Street",
#     "addressLine2": "Suite 221",
#     "addressZip": "V6E 3R5",
#     "custom": "{\"names\":{\"en\":\"Vancouver Burrard Station \u2013 Royal Centre\"}}",
#     "id": "ea01f5e5ba07af767a739c1d66730bef9663a1a307b84e4674cffcd93caad1b5",
#     "internalId": 14,
#     "name": "Royal Centre",
#     "qpId": "2",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Surrey",
#     "addressLine1": "13426 - 78Th Avenue",
#     "addressZip": "V3W 8J6",
#     "custom": "{\"names\":{\"en\":\"Surrey - As of October 2, our office on 78th Ave will open Saturdays instead of 101st Ave location.\"},\"address\":{\"en\":{\"address1\":\"\",\"address2\":\"\",\"city\":\"\",\"country\":\"\"}}}",
#     "id": "d8225a23dd9830e9684fb00f8aea2fff279c892cb1065244aaa0ae05396a0fe2",
#     "internalId": 15,
#     "name": "Surrey",
#     "qpId": "5",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Victoria",
#     "addressLine1": "1150 McKenzie Avenue",
#     "addressLine2": "#1",
#     "addressZip": "V8P 2L7",
#     "custom": "{\"names\":{\"en\":\"Victoria - McKenzie Ave\"}}",
#     "id": "3293565aa3128e744b9b434d236166c67949a5f52bbd5cf2adc83cf771621813",
#     "internalId": 16,
#     "name": "Victoria - McKenzie Ave",
#     "qpId": "1",
#     "timeZone": "America/Vancouver"
#   },
#   {
#     "addressCity": "Victoria",
#     "addressLine1": "955 Wharf Street",
#     "addressZip": "V8W 3Y8",
#     "custom": "{\"names\":{\"en\":\"Victoria - Wharf St\"}}",
#     "id": "2d6b890b7f683d82a1f104ff3d882b466dae16b1715d3e385eaaf7fa5c25d0df",
#     "internalId": 17,
#     "name": "Victoria - Wharf St",
#     "qpId": "17",
#     "timeZone": "America/Vancouver"
#   }
# ]


r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3/dates;servicePublicId=da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25;customSlotLength=40",
)
# [
#   {
#     "date": "2021-10-14"
#   },
#   {
#     "date": "2021-10-15"
#   },
#   {
#     "date": "2021-10-18"
#   },
#   {
#     "date": "2021-10-19"
#   },
#   {
#     "date": "2021-10-20"
#   },
#   {
#     "date": "2021-10-21"
#   },
#   {
#     "date": "2021-10-22"
#   },
#   {
#     "date": "2021-10-25"
#   },
#   {
#     "date": "2021-10-26"
#   },
#   {
#     "date": "2021-10-27"
#   },
#   {
#     "date": "2021-10-28"
#   },
#   {
#     "date": "2021-10-29"
#   },
#   {
#     "date": "2021-10-30"
#   },
#   {
#     "date": "2021-11-01"
#   },
#   {
#     "date": "2021-11-02"
#   },
#   {
#     "date": "2021-11-03"
#   },
#   {
#     "date": "2021-11-04"
#   },
#   {
#     "date": "2021-11-05"
#   },
#   {
#     "date": "2021-11-08"
#   },
#   {
#     "date": "2021-11-09"
#   },
#   {
#     "date": "2021-11-10"
#   },
#   {
#     "date": "2021-11-12"
#   },
#   {
#     "date": "2021-11-15"
#   },
#   {
#     "date": "2021-11-16"
#   },
#   {
#     "date": "2021-11-17"
#   },
#   {
#     "date": "2021-11-18"
#   },
#   {
#     "date": "2021-11-19"
#   },
#   {
#     "date": "2021-11-22"
#   },
#   {
#     "date": "2021-11-23"
#   },
#   {
#     "date": "2021-11-24"
#   },
#   {
#     "date": "2021-11-25"
#   },
#   {
#     "date": "2021-11-26"
#   },
#   {
#     "date": "2021-11-29"
#   },
#   {
#     "date": "2021-11-30"
#   },
#   {
#     "date": "2021-12-01"
#   },
#   {
#     "date": "2021-12-02"
#   },
#   {
#     "date": "2021-12-03"
#   },
#   {
#     "date": "2021-12-06"
#   },
#   {
#     "date": "2021-12-07"
#   },
#   {
#     "date": "2021-12-08"
#   },
#   {
#     "date": "2021-12-09"
#   },
#   {
#     "date": "2021-12-10"
#   },
#   {
#     "date": "2021-12-13"
#   },
#   {
#     "date": "2021-12-14"
#   },
#   {
#     "date": "2021-12-15"
#   },
#   {
#     "date": "2021-12-16"
#   },
#   {
#     "date": "2021-12-17"
#   },
#   {
#     "date": "2021-12-20"
#   },
#   {
#     "date": "2021-12-21"
#   },
#   {
#     "date": "2021-12-22"
#   }
# ]


s.headers.update({"Origin": "https://onlinebusiness.icbc.com"})

r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/fonts/KFOlCnqEu92Fr1MmWUlfBBc4.037d8304.woff2",
    headers={
        "Referer": "https://onlinebusiness.icbc.com/qmaticwebbooking/css/app.e2cdd0dc.css",
        "Host": None,
        "Connection": None,
        "Accept": None,
        "Sec-Fetch-Site": None,
        "Sec-Fetch-Mode": None,
        "Sec-Fetch-Dest": None,
        "Accept-Encoding": None,
        "Accept-Language": None,
        "Cookie": None,
    },
)


r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3/dates/2021-10-14/times;servicePublicId=da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25;customSlotLength=40",
    headers={"Origin": None},
)
# [
#   {
#     "date": "2021-10-14",
#     "time": "08:35"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "09:15"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "09:55"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "10:35"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "11:15"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "11:55"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "12:35"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "13:15"
#   },
#   {
#     "date": "2021-10-14",
#     "time": "13:55"
#   }
# ]


r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/fonts/KFOlCnqEu92Fr1MmEU9fBBc4.28546717.woff2",
    headers={
        "Referer": "https://onlinebusiness.icbc.com/qmaticwebbooking/css/app.e2cdd0dc.css",
        "Host": None,
        "Connection": None,
        "Accept": None,
        "Sec-Fetch-Site": None,
        "Sec-Fetch-Mode": None,
        "Sec-Fetch-Dest": None,
        "Accept-Encoding": None,
        "Accept-Language": None,
        "Cookie": None,
    },
)


r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3/dates/2021-12-03/times;servicePublicId=da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25;customSlotLength=40",
    headers={"Origin": None},
)
# [
#   {
#     "date": "2021-12-03",
#     "time": "08:35"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "09:15"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "09:55"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "10:35"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "11:15"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "11:55"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "12:35"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "13:15"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "13:55"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "14:35"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "15:15"
#   },
#   {
#     "date": "2021-12-03",
#     "time": "15:55"
#   }
# ]


s.headers.update(
    {
        "X-CSRF-Token": "MTAuMTY1LjEzNy4zMVFtYXRpYyBXZWIgQm9va2luZyBpcyB2ZXJ5IHNlY3VyZSBtYWtlIHN1cmUgaXQgaXMuV2VkIFNlcCAyOSAyMToxNjowNCBQRFQgMjAyMQ=="
    }
)

r = s.post(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3/dates/2021-12-03/times/12:35/reserve;customSlotLength=40",
    json={
        "services": [
            {
                "publicId": "da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25"
            }
        ],
        "custom": '{"peopleServices":[{"publicId":"da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25","qpId":"3","adult":1,"name":"B: Single knowledge test for a new or expired learner’s licence (45 min)","child":0}]}',
    },
)
# {
#   "allday": false,
#   "appId": "qmaticwebbooking",
#   "blocking": false,
#   "branch": {
#     "addressCity": "North Vancouver",
#     "addressLine1": "1331 Marine Drive",
#     "addressZip": "V7P 3E5",
#     "custom": "{\"names\":{\"en\":\"North Vancouver\"}}",
#     "id": "80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3",
#     "internalId": 10,
#     "name": "North Vancouver",
#     "qpId": "4",
#     "timeZone": "America/Vancouver"
#   },
#   "branchName": "North Vancouver",
#   "created": 1632975590520,
#   "date": "2021-12-03",
#   "duration": 40,
#   "peopleServices": [],
#   "publicBranchId": "80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3",
#   "publicId": "7057140f425bdd8beef19e55b37cfc3a8238ea82e0d541a84a8ada48fa123c9c",
#   "publicServiceId": "da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25",
#   "serviceName": "B: Single knowledge test for a new or expired learner\u2019s licence (45 min)",
#   "services": [
#     {
#       "name": "B: Single knowledge test for a new or expired learner\u2019s licence (45 min)",
#       "publicId": "da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25"
#     }
#   ],
#   "status": 10,
#   "time": "12:35",
#   "title": "Pending reservation"
# }


r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/services",
    headers={"Origin": None, "X-CSRF-Token": None},
)
# [
#   {
#     "additionalDuration": 0,
#     "custom": "{\"names\":{\"en\":\"A: Renew / replace a BC licence or ID or apply for a new BCID or BC Service Card (10 min)\"}}",
#     "duration": 10,
#     "internalId": 7,
#     "name": "A: Renewal or replacement of an existing BC licence or ID, and new ID applications (10 min)",
#     "publicId": "c2a883f450951e191132a1dc0ccc3606293b454c65b72b81ac304eefae19e709",
#     "qpId": "2"
#   },
#   {
#     "additionalDuration": 0,
#     "custom": "{\"names\":{\"en\":\"B: Single knowledge test for a new or expired learner\u2019s licence (45 min)\"}}",
#     "duration": 40,
#     "internalId": 5,
#     "name": "B: Single knowledge test for a new or expired learner\u2019s licence (45 min)",
#     "publicId": "da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25",
#     "qpId": "3"
#   },
#   {
#     "additionalDuration": 0,
#     "custom": "{\"names\":{\"en\":\"C: Combination knowledge test for a new or expired learner\u2019s licence (75 min)\"}}",
#     "duration": 75,
#     "internalId": 6,
#     "name": "C: Combination knowledge test for a new or expired learner\u2019s licence (75 min)",
#     "publicId": "895063ac05ab8f9a4791fd0e8198d3e198c78de532dc7c985f4360a3ed080599",
#     "qpId": "11"
#   },
#   {
#     "additionalDuration": 0,
#     "custom": "{\"names\":{\"en\":\"D: All other in-person licensing services (excludes knowledge/road tests) (10 min)\"}}",
#     "duration": 10,
#     "internalId": 8,
#     "name": "D: All other in-person licensing services (excludes knowledge/road tests) (10 min)",
#     "publicId": "9d140201d792c24c15884ac50bbb52b6297768c05aad2edf40d81ca47a6e502d",
#     "qpId": "30"
#   }
# ]


r = s.get(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/checkMultiple;phone=12133734253;email=test-1fn9lp5tx@srv1.mail-tester.com;firstName=Javad;lastName=Gummer;branchPublicId=80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3;servicePublicId=da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25;date=2021-12-03;time=12:35",
    headers={"Origin": None, "X-CSRF-Token": None},
)
# {
#   "message": "MULTIPLE_OK"
# }


r = s.post(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/matchCustomer",
    json={
        "email": "test-1fn9lp5tx@srv1.mail-tester.com",
        "phone": "12133734253",
        "firstName": "Javad",
        "lastName": "Gummer",
        "dateOfBirth": "2004-05-13",
        "externalId": "",
    },
)
# {
#   "allowOverwrite": false
# }


r = s.post(
    "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/appointments/7057140f425bdd8beef19e55b37cfc3a8238ea82e0d541a84a8ada48fa123c9c/confirm",
    json={
        "customer": {
            "firstName": "Javad",
            "lastName": "Gummer",
            "dateOfBirth": "2004-05-13",
            "email": "test-1fn9lp5tx@srv1.mail-tester.com",
            "phone": "12133734253",
            "dob": "",
            "externalId": "",
        },
        "languageCode": "en",
        "countryCode": "ca",
        "notificationType": "",
        "captcha": "",
        "custom": '{"peopleServices":[{"publicId":"da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25","qpId":"3","adult":1,"name":"B: Single knowledge test for a new or expired learner’s licence (45 min)","child":0}],"totalCost":0,"createdByUser":"Qmatic Web Booking","paymentRef":"","customSlotLength":40}',
        "notes": "",
        "title": "Qmatic Web Booking",
    },
)
# {
#   "allday": false,
#   "appId": "qmaticwebbooking",
#   "blocking": false,
#   "branch": {
#     "addressCity": "North Vancouver",
#     "addressLine1": "1331 Marine Drive",
#     "addressZip": "V7P 3E5",
#     "custom": "{\"names\":{\"en\":\"North Vancouver\"}}",
#     "id": "80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3",
#     "internalId": 10,
#     "name": "North Vancouver",
#     "qpId": "4",
#     "timeZone": "America/Vancouver"
#   },
#   "branchName": "North Vancouver",
#   "created": 1632975590520,
#   "customSlotLength": 40,
#   "customer": {
#     "allowOverwrite": false,
#     "dateOfBirth": "2004-05-13",
#     "email": "test-1fn9lp5tx@srv1.mail-tester.com",
#     "externalId": "",
#     "firstName": "Javad",
#     "id": 3237484,
#     "lastName": "Gummer",
#     "phone": "12133734253"
#   },
#   "date": "2021-12-03",
#   "duration": 40,
#   "errorMessage": "",
#   "externalId": "32374851235",
#   "languageCode": "en",
#   "notes": "",
#   "peopleServices": [
#     {
#       "name": "B: Single knowledge test for a new or expired learner\u2019s licence (45 min)",
#       "adult": 1,
#       "publicId": "da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25",
#       "qpId": "3",
#       "child": 0
#     }
#   ],
#   "publicBranchId": "80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3",
#   "publicId": "7057140f425bdd8beef19e55b37cfc3a8238ea82e0d541a84a8ada48fa123c9c",
#   "publicServiceId": "da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25",
#   "qrConciergeId": "{\"appointment_id\":\"3237485\",\"branch_name\":\"North Vancouver\",\"branch_id\":\"10\",\"appointment_date\":\"2021-12-03T12:35:00\"}",
#   "serviceName": "B: Single knowledge test for a new or expired learner\u2019s licence (45 min)",
#   "services": [
#     {
#       "name": "B: Single knowledge test for a new or expired learner\u2019s licence (45 min)",
#       "publicId": "da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25"
#     }
#   ],
#   "status": 20,
#   "time": "12:35",
#   "title": "Qmatic Web Booking",
#   "totalCost": 0.0
# }
