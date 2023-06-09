
import re

# Define regex patterns for IPV4 and IPV6 addresses with ports
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?::[0-9]{1,5})?\b'
ipv6_pattern = r'(?<![:.\w])(?:(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|(?:(?:[a-fA-F0-9]{1,4}:){0,6}[a-fA-F0-9]{1,4})?::(?:[a-fA-F0-9]{1,4}:){0,6}[a-fA-F0-9]{1,4})(?::[0-9]{1,5})?(?![\w:.])'
port_pattern = r':([0-9]{1,5})$'

# Open the input file and read its contents
with open('Unextracted-IPs.txt', 'r') as file:
    contents = file.read()

# Extract IPV4 and IPV6 addresses using regex patterns
ipv4_list = re.findall(ipv4_pattern, contents)
ipv6_list = re.findall(ipv6_pattern, contents)

# Remove duplicates from the extracted lists
ipv4_list = list(set(ipv4_list))
ipv6_list = list(set(ipv6_list))

# Initialize the dictionaries for IPV4 and IPV6 ports
ipv4_ports = {}
ipv6_ports = {}

# Define the port pattern
port_pattern = r':(\d{1,5})$'

# Extract ports from IPV4 addresses
for ipv4 in ipv4_list:
    port_match = re.search(port_pattern, ipv4)
    if port_match:
        port = port_match.group(1)
        ip = ipv4[:-len(port)-1]  # remove the port from the IP address
        ipv4_ports[ip] = port
    else:
        ipv4_ports[ipv4] = None  # no port in this IP address

# Extract ports from IPV6 addresses
for ipv6 in ipv6_list:
    ipv6_ports[ipv6] = None  # initialize the dictionary with all the IPV6 addresses
    port_match = re.search(port_pattern, ipv6)
    if port_match:
        port = port_match.group(1)
        ip = ipv6[:ipv6.rfind(']')+1]  # remove the port from the IP address
        ipv6_ports[ip] = port
    else:
        ipv6_ports[ipv6] = None  # no port in this IP address

# Remove duplicates from the extracted port lists
ipv4_ports = {k: v for k, v in set(ipv4_ports.items())}
ipv6_ports = {k: v for k, v in set(ipv6_ports.items())}


# Sort the lists in descending order
ipv4_list.sort(reverse=True)
ipv6_list.sort(reverse=True)

# Write the extracted IPs and ports to a file
with open('Extracted-IPs.txt', 'w') as file:
    file.write('Extracted IPV4 Addresses:\n')
    for ipv4 in ipv4_list:
        if ipv4_ports[ipv4]:
            file.write(f'{ipv4:<22} Port: {ipv4_ports[ipv4]}\n')
        else:
            file.write(f'{ipv4}\n')
    file.write('\nExtracted IPV6 Addresses:\n')
    for ipv6 in ipv6_list:
        if ipv6_ports[ipv6]:
            file.write(f'{ipv6:<40} Port: {ipv6_ports[ipv6]}\n')
        else:
            file.write(f'{ipv6}\n')
# Print the extracted IPs and ports
print('Extracted IPV4 Addresses:')
for ipv4 in ipv4_list:
    if ipv4_ports[ipv4]:
        print(f'{ipv4:<22} Port: {ipv4_ports[ipv4]}')
    else:
        print(ipv4)
print('\nExtracted IPV6 Addresses:')
for ipv6 in ipv6_list:
    if ipv6_ports[ipv6]:
        print(f'{ipv6:<40} Port: {ipv6_ports[ipv6]}')
    else:
        print(ipv6)
print('\nExtracted Ports:')
for ip, port in ipv4_ports.items():
    if port:
        print(f'{ip:<22} Port: {port}')
for ip, port in ipv6_ports.items():
    if port:
        print(f'{ip:<40} Port: {port}')
