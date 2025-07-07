import nmap

# Create a PortScanner object
scanner = nmap.PortScanner()

# Scan a local IP (replace with your target IP)
scanner.scan('127.0.0.1', '1-1024')

# Print the result
print(scanner.scaninfo())   
print(scanner['127.0.0.1'].state())
print(scanner['127.0.0.1'].all_protocols())
print(scanner['127.0.0.1']['tcp'].keys())
