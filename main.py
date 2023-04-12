import socket
import logging

DOMAIN = "example.com"  # Change this to the domain you want to check

logging.basicConfig(level=logging.INFO)

def get_ip_addresses(domain):
    """
    This function gets the IP addresses of a given domain.

    Parameters:
    domain (str): The domain to get the IP addresses of.

    Returns:
    list: A list of IP addresses associated with the domain.
    """
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[2]
        return ip_addresses
    except socket.gaierror:
        logging.error(f"Failed to resolve domain {domain}.")
        return None

def check_domain_ip_address(domain):
    """
    This function checks if a given domain has an IP address.

    Parameters:
    domain (str): The domain to check.

    Returns:
    bool: True if the domain has an IP address, False otherwise.
    """
    ip_addresses = get_ip_addresses(domain)
    if ip_addresses:
        logging.info(f"Domain {domain} has an A record (IPv4 address).")
        logging.info("Site is good.")
        return True
    else:
        logging.warning(f"Domain {domain} does not have any IP address.")
        logging.error("Domain doesn't have any IP address.")
        return False

check_domain_ip_address(DOMAIN)
