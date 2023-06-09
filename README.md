# IP-Extractor
Parses txt files and Extracts IP addresses


Default setup
1. Create Unextracted-IPs.txt file
2. Paste raw text into file and save
3. PortIPExtractor will check the file for any IPV4/6 address and port numbers
4. It will then display and save all Ports and IPS


This was intended to make updating firewall rules easier. You can monitor traffic from whitelisted applications and copy the IPs that the software you are using to monitor the application reports. Then copy the apps output into your firewall using your firwalls mass IP import or similare feature.

# Features

- Define IP patterns using Regex
- Removes duplicate addresses and ports upon extract
- Sorts the extracted IPs in descending order
- Writes the extracted IPs and ports to a file
- Displays extracted IPs and ports in terminal
