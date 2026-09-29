import math
import os

folder = os.path.dirname(os.path.abspath(__file__))
files = [os.path.join(folder, f"output-Set{i}.txt") for i in range(1, 10)]

N_events = 500000
N_subsamples = len(files)

# Define the normal and variant molecule pairs
molecules = {
    211: "Carbon monoxide", -211: "Carbon-13 monoxide",
    321: "Nitric oxide", -321: "Ionised NO",
    2212: "Water", -2212: "Heavy water (D2O)",
    3122: "Methane (CH4)", -3122: "Methyl ion (CH3-)",
    3312: "Ethylene (C2H4)", -3312: "Ionised ethylene (C2H3-)",
    3334: "Ozone (O3)", -3334: "Superoxide anion (O2-)"
}

means = {ID: [] for ID in molecules}


# Count each molecule in each of the 9 files
for filename in files:

    counts = {ID: 0 for ID in molecules}

    with open(filename, "r") as file:
        file.readline()

        for line in file:
            data = line.split()

            if len(data) == 4:
                ID = int(data[3])

                if ID in counts:
                    counts[ID] += 1

    for ID in molecules:
        means[ID].append(counts[ID] / N_events)


# --------------------------------------------------
# TABLE 1: AVERAGE COUNT + UNCERTAINTY
# --------------------------------------------------

# Store overall averages and uncertainties
average = {}
uncertainty = {}

# Print table heading
print("\nTABLE 1: MOLECULAR COUNTS\n")
print(f"{'ID':>7} {'Molecule':<28} {'Average/event':>15} {'Uncertainty':>15}")

for ID, name in molecules.items():

    avg = sum(means[ID]) / N_subsamples

    # Standard deviation of the 9 sub-sample means
    sd = math.sqrt(
        sum((x - avg) ** 2 for x in means[ID])
        / (N_subsamples - 1)
    )

    # Statistical uncertainty using the sub-sampling method
    error = sd / math.sqrt(N_subsamples)

    average[ID] = avg
    uncertainty[ID] = error

    print(f"{ID:>7} {name:<28} {avg:>15.6f} {error:>15.6f}")


# --------------------------------------------------
# TABLE 2: NORMAL VS VARIANT
# --------------------------------------------------

pairs = [
    (211, -211, "Carbon monoxide"),
    (321, -321, "Nitric oxide"),
    (2212, -2212, "Water"),
    (3122, -3122, "Methane (CH4)"),
    (3312, -3312, "Ethylene (C2H4)"),
    (3334, -3334, "Ozone (O3)")
]

print("\nTABLE 2: ASYMMETRY\n")
print(f"{'Pair':<15} {'Asymmetry':>15} {'Uncertainty':>15} {'Significance':>15}")

# Loop through each molecule pair
for normal, variant, name in pairs:

    N1 = average[normal]
    N2 = average[variant]

    e1 = uncertainty[normal]
    e2 = uncertainty[variant]

    # Calculate asymmetry
    A = (N1 - N2) / (N1 + N2)

    # Calculate uncertainty on asymmetry
    eA = (2 / (N1 + N2)**2) * math.sqrt(
        N2**2 * e1**2 + N1**2 * e2**2
    )

    # Calculate significance of the asymmetry
    significance = abs(A) / eA

    print(
        f"{normal} / {variant:<8} "
        f"{A:>15.6f} "
        f"{eA:>15.6f} "
        f"{significance:>14.3f}"
    )


















