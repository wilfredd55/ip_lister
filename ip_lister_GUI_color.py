import ipaddress
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog

def parse_ips():
    # If the input and output filenames haven't been selected yet, display an error message and do nothing
    if not input_filename or not output_filename:
        error_label.config(text="Please select input and output files")
        return

    # Open the input and output files
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
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

def select_input_file():
    global input_filename
    input_filename = filedialog.askopenfilename(title="Select Input File")
    input_file_label.config(text=input_filename)

def select_output_file():
    global output_filename
    output_filename = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt")
    output_file_label.config(text=output_filename)

# Create the GUI window
root = tk.Tk()
root.title("IP Address Parser")
root.config(bg="#f5f5f5")

# Set the font for the buttons
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create the buttons to select input and output files
input_button = tk.Button(root, text="Select Input File", command=select_input_file, padx=10, pady=5, bg="#105cb4", fg="white", font=button_font)
input_button.pack(side="left", padx=10, pady=5)

output_button = tk.Button(root, text="Select Output File", command=select_output_file, padx=10, pady=5, bg="#105cb4", fg="white", font=button_font)
output_button.pack(side="right", padx=10, pady=5)

# Create the button that runs the IP parsing script
parse_button = tk.Button(root, text="Parse IPs", command=parse_ips, padx=10, pady=5, bg="#105cb4", fg="white", font=button_font)
parse_button.pack(side="bottom", padx=10, pady=20)

# Create labels to display the selected input and output filenames
input_file_label = tk.Label(root, text="", fg="black")
input_file_label.pack()

output_file_label = tk.Label(root, text="", fg="black")
output_file_label.pack()

# Create a label to display error messages
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

# Start the GUI event loop
root.mainloop()
