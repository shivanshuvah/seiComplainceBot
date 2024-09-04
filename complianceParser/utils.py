from urllib.parse import urlparse

def extract_domain(url):
    # Ensure the url starts with a scheme (http/https) to parse correctly
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    # Parse the URL
    parsed_url = urlparse(url)
    
    # Split the hostname and extract the domain part
    domain_parts = parsed_url.hostname.split('.')
    
    # If the URL starts with 'www.', discard it
    if domain_parts[0] == 'www':
        domain = domain_parts[1]
    else:
        domain = domain_parts[0]
    
    return domain