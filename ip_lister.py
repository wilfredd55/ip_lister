import ipaddress

# Open the input and output files
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Iterate over each line in the input file
    for line in input_file:
        # Remove any leading or trailing whitespace from the line
        line = line.strip()
        # Check if the line represents a range of IP addresses
        if '-' in line:
            # Split the line into two IP addresses representing the range
            start_ip, end_ip = line.split('-')
            # Convert the IP addresses to their integer representations
            start_int = int(ipaddress.IPv4Address(start_ip))
            end_int = int(ipaddress.IPv4Address(end_ip))
            # Iterate over all IP addresses in the range, converting them back to dotted-quad format and writing them to the output file
            for ip_int in range(start_int, end_int + 1):
                ip = str(ipaddress.IPv4Address(ip_int))
                output_file.write(ip + '\n')
        else:
            # The line represents a single IP address, so just write it to the output file
            output_file.write(line + '\n')