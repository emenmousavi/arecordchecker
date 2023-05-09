import http.client

# Set up the HTTP connection
conn = http.client.HTTPSConnection("dns-lookup5.p.rapidapi.com")

# Set the headers with the API key and host
headers = {
    'X-RapidAPI-Key': "6aea87b649msh5ff12484a41ec8ep1a7a47jsn945fa87d8aec",
    'X-RapidAPI-Host': "dns-lookup5.p.rapidapi.com"
}

# Prompt the user for a domain to look up
domain = input("Enter a domain to look up: ")

# Construct the API request URL with the user's input
url = f"/simple?domain={domain}&recordType=A"

# Send the request to the API and get the response
conn.request("GET", url, headers=headers)
res = conn.getresponse()
data = res.read()

# Extract the IP address(es) from the response and print them
ip_addresses = data.decode("utf-8").strip().split("\n")
print("IP Address(es):")
for ip_address in ip_addresses:
    print(ip_address)
