import math
#select the file to read
file = open("PRA2007/output-Set0.txt", "r")

# skip header so that the first line of data does not crash the code 
file.readline()

for line in file: 
    px, py, pz, particle_id = line.split()           

    px = float(px)
    py = float(py)
    pz = float(pz)

    momentum = math.sqrt(px**2 + py**2 + pz**2)
    print(momentum)

# Calculating the magnitude of total momentum
total_px = 0
total_py = 0
total_pz = 0

file.seek(0)  # so we can read the file from the start, since we used in the first loop

for line in file:
    data = line.split()

    if len(data) != 4:    # check that it read 4 field, if not it skips the 'blank line' or header, prevent crash
        continue

    px, py, pz, particle_id = data

    px = float(px)
    py = float(py)
    pz = float(pz)

    total_px += px
    total_py += py
    total_pz += pz

total_momentum = (total_px**2 + total_py**2 + total_pz**2)**0.5 

print("total_px =", total_px)
print("total_py =", total_py)
print("total_pz =", total_pz)
print("Total momentum =", total_momentum)


