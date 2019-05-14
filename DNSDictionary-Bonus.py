providers = ["Level3", "Verisign", "Google", "Quad9", "DNS.WATCH",
             "Comodo Secure DNS", "OpenDNS Home", "Norton ConnectSafe",
             "GreenTeamDNS", "SafeDNS", "OpenNIC", "SmartViper", "Dyn",
             "FreeDNS", "Alternate DNS", "Yandex.DNS", "UncensoredDNS",
             "Hurricane Electric", "puntCAT", "Neustar", "Cloudflare",
             "Fourth Estate"]

ips = ["209.244.0.3", "64.6.64.6", "8.8.8.8", "9.9.9.9", "84.200.69.80",
       "8.26.56.26", "208.67.222.222", "199.85.126.10", "81.218.119.11",
       "195.46.39.39", "69.195.152.204", "208.76.50.50", "216.146.35.35",
       "37.235.1.174", "198.101.242.72", "77.88.8.8", "91.239.100.100",
       "74.82.42.42", "109.69.8.51", "156.154.70.1", "1.1.1.1", "45.77.165.194"]


####################################
### Part 1 - Provider Dictionary ###
####################################

# Use a for loop to create a dictionary mapping the provider names to their IPs
DNS_dictionary = {}

for provider, ip in zip(providers, ips):
       DNS_dictionary[provider] = ip
print("DNS Dictionary: ")
print(DNS_dictionary)
print("--------")


# Use the dictionary to print Hurricane Electric's IP
print("Hurricane Electric's IP is: " + DNS_dictionary['Hurricane Electric'])
print("--------")
print("--------")


##################################
### Part 2 - List of Providers ###
##################################

# Use a for loop to create a list of dictionaries with the associated information
DNS_dictionaries = []

for provider, ip in zip(providers, ips):
       DNS_dictionaries.append({"provider_name": provider, "primary_server": ip})

print("DNS Dictionaries: ")
print(DNS_dictionaries)
print("--------")


# Use the list to print the total number of providers
print("Number of providers: " + str(len([key for provider_ip in DNS_dictionaries for key in provider_ip.keys() if key == "provider_name"])))
print("--------")
print("--------")


#############################################################
### Part 3 (Bonus) - Adding Secondaries to the Dictionary ###
#############################################################
secondary_ips = [
    {"provider": "Level3", "ip": "209.244.0.4"},
    {"provider": "Verisign", "ip": "64.6.65.6"},
    {"provider": "Google", "ip": "8.8.4.4"},
    {"provider": "Quad9", "ip": "149.112.112.112"},
    {"provider": "DNS.WATCH", "ip": "84.200.70.40"},
    {"provider": "Comodo Secure DNS", "ip": "8.20.247.20"},
    {"provider": "OpenDNS Home", "ip": "208.67.220.220"},
    {"provider": "Norton ConnectSafe", "ip": "199.85.127.10"},
    {"provider": "GreenTeamDNS", "ip": "209.88.198.133"},
    {"provider": "SafeDNS", "ip": "195.46.39.40"},
    {"provider": "OpenNIC", "ip": "23.94.60.240"},
    {"provider": "SmartViper", "ip": "208.76.51.51"},
    {"provider": "Dyn", "ip": "216.146.36.36"},
    {"provider": "FreeDNS", "ip": "37.235.1.177"},
    {"provider": "Alternate DNS", "ip": "23.253.163.53"},
    {"provider": "Yandex.DNS", "ip": "77.88.8.1"},
    {"provider": "UncensoredDNS", "ip": "89.233.43.71"},
    {"provider": "Neustar", "ip": "156.154.71.1"},
    {"provider": "Cloudflare", "ip": "1.0.0.1"},
]

# Use a for loop to update your dictionary from part 1 with the new IPs
for provider, ip in DNS_dictionary.items():

    # set provider value in dictionary to array of IPs (new and old)
       for secondary_ip in secondary_ips:
           if provider in secondary_ip.values():
                  DNS_dictionary[provider]=[ip, secondary_ip["ip"]]
if secondary_ip["provider"] not in DNS_dictionary.keys():
    print("Provider " + secondary_ip["provider"] + " does not exist in dictionary.")

print("DNS Dictionary Modified: ")
print(DNS_dictionary)
print("--------")

# Use the dictionary to print Google's IPs
## ** HASHTAGS ORIGINALLY SAID HURRICANE IP BUT INSTRUCTIONS ON GITLAB ASK FOR GOOGLE **
print("Google's IP's are: ")
for google_ips in DNS_dictionary["Google"]:
       print(google_ips)
print("--------")
print("--------")

#######################################################
### Part 4 (Bonus) - Adding Secondaries to the List ###
#######################################################

# Use nested for loops to update the list from part 2 with a "secondary_server" key.
for companies_ip in DNS_dictionaries:
    for secondary_companies_ip in secondary_ips:
        if secondary_companies_ip['provider'] in companies_ip['provider_name']:
            companies_ip['secondary_server'] = secondary_companies_ip['ip']
            break
        else:
            companies_ip['secondary_server'] = 'none'
print("DNS Dictionaries Modified: ")
print(DNS_dictionaries)
print("--------")
print("--------")

#import json
#print(json.dumps(DNS_dictionaries, indent = 1))
#Dictionaries are sorted by key before the display is computed.
import pprint
for companies_ip in DNS_dictionaries:
       companies_ip['Company Name'] = companies_ip['provider_name']
       companies_ip.pop('provider_name')
       companies_ip['Primary Server'] = companies_ip['primary_server']
       companies_ip.pop('primary_server')
       companies_ip['Secondary Server'] = companies_ip['secondary_server']
       companies_ip.pop('secondary_server')
pprint.pprint(DNS_dictionaries, indent=2)