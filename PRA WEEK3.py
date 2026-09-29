import math
# select file to read
filename = "PRA2007/output-Set2.txt"
HEADER_FIELDS = 2
MOLECULE_ID_INDEX = 3                # Setting constants 
DATA_FIELD = 4
try:
    with open(filename, "r") as file:
        ...
except FileNotFoundError:
    print("File not found.")          # Protection/hardcore
    exit()
# N events ? 

# Molecule IDs
molecules = {
    211: "Carbon monoxide",
    -211: "Carbon-13 monoxide",
    321: "Nitric oxide",
    -321: "Ionised NO",
    2212: "Water",
    -2212: "Heavy water (D2O)",
    3122: "Methane (CH4)",
    -3122: "Methyl ion (CH3-)",
    3312: "Ethylene (C2H4)",
    -3312: "Ionised ethylene (C2H3-)",
    3334: "Ozone (O3)",
    -3334: "Superoxide anion (O2-)"
}

# Choose molecule 
wanted_id = int(input("Enter molecule ID:" ))
try:
    wanted_id = int(input("Enter molecule ID: "))
except ValueError:
    print("Please enter a valid integer.")         # Protection
    exit()

if wanted_id not in molecules:                     # Protection against unknown molecule id 
    print("Unknown molecule ID.")
    exit()

counts = []    # One entry per event
count = 0      # counter for the event being read

with open("PRA2007\output-Set2.txt", "r") as file:
    file.readline()    # Skip header, protect the file from crashing as header is only 2 input instead of 4

    for line in file:
        data = line.split()    # Split line to be read 

        if len(data) ==2:   
            counts.append(count)  
            count = 0
        else:
            molecule_id = int(data[3])
            if molecule_id == wanted_id:
                count += 1
# Final event 
counts.append(count)

# Average
N = len(counts)
average = sum(counts) / N

#Statistical uncertainty 
variance = sum((x - average)**2 for x in counts) / (N-1)  # sample variance
uncertainty = math.sqrt(variance / N)                     # standard error of the mean

print("\nMolecule:", molecules[wanted_id])
print("Events:", N)
print("Average:", average)
print("Statistical uncertainty:", uncertainty)
print(f"Result: {average:.4f} +/- {uncertainty:.4f}")










