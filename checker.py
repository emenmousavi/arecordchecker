import dns.resolver

print("[#] Welcome to A Record Checker [#]")

def find_a_record(domain):
    try:
        answers = dns.resolver.query(domain, 'A')
        for rdata in answers:
            print('[+] IP address:', rdata.address)
    except dns.resolver.NXDOMAIN:
        print('[-] No such domain', domain)
    except dns.resolver.NoAnswer:
        print('[-] No A record for', domain)

domain = input('Enter the domain name: ')
find_a_record(domain)
