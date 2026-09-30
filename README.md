PRA2003- Simulating molecular emissions in a combustible reaction
# Davide Capurro - I6382558

## Goals
The goals of this analysis are:

1. Determine the **average count of each molecular species per event** and its statistical uncertainty.
2. Determine whether there is an **asymmetry between the normal and variant molecules**.

## Results

The analysis was performed using 10 subsamples. For each molecular species, the total number of particles was divided by the total number of events to obtain the average number of particles per event. The statistical uncertainty was determined from the variation between the 10 subsamples.

### Average count per event

| Molecular species        | Average count per event | Statistical uncertainty |
| ------------------------ | ----------------------: | ----------------------: |
| Carbon monoxide          |               19.949508 |              ± 0.032746 |
| Carbon-13 monoxide       |               19.917211 |              ± 0.031873 |
| Nitric oxide             |                2.509148 |              ± 0.004774 |
| Ionised NO               |                2.503457 |              ± 0.005504 |
| Water                    |                1.208034 |              ± 0.001896 |
| Heavy water (D2O)        |                1.184161 |              ± 0.002412 |
| Methane (CH4)            |                0.276599 |              ± 0.001074 |
| Methyl ion (CH3-)        |                0.271696 |              ± 0.000985 |
| Ethylene (C2H4)          |                0.039441 |              ± 0.000284 |
| Ionised ethylene (C2H3-) |                0.039000 |              ± 0.000402 |
| Ozone (O3)               |                0.001187 |              ± 0.000042 |
| Superoxide anion (O2-)   |                0.001152 |              ± 0.000051 |

Carbon monoxide has the highest average count, with approximately **19.95 particles per event**. Carbon-13 monoxide has a very similar average of **19.92 particles per event**. The least frequent species is ozone, with an average of approximately **0.0012 particles per event**.

---

## Pair Comparison

The normal and variant molecules were compared by calculating their difference and the uncertainty of this difference. The significance was then calculated in units of standard deviations:

$$
\text{Significance} =
\frac{|\text{Difference}|}
{\text{Uncertainty of difference}}
$$

| Pair                                 | Difference | Uncertainty | Significance |
| ------------------------------------ | ---------: | ----------: | -----------: |
| Carbon monoxide / Carbon-13 monoxide |   0.032297 |    0.004519 |   7.15 sigma |
| Nitric oxide / Ionised NO            |   0.005691 |    0.003294 |   1.73 sigma |
| Water / Heavy water                  |   0.023873 |    0.002373 |  10.06 sigma |
| Methane / Methyl ion                 |   0.004903 |    0.000583 |   8.41 sigma |
| Ethylene / Ionised ethylene          |   0.000441 |    0.000488 |   0.90 sigma |
| Ozone / Superoxide anion             |   0.000036 |    0.000069 |   0.52 sigma |

The largest differences relative to their uncertainties are found for:

* **Water vs Heavy water:** 10.06 sigma
* **Methane vs Methyl ion:** 8.41 sigma
* **Carbon monoxide vs Carbon-13 monoxide:** 7.15 sigma

The differences for nitric oxide, ethylene and ozone are smaller relative to their uncertainties, with significances of 1.73, 0.90 and 0.52 standard deviations respectively.

---

## Asymmetry

The asymmetry between each normal and variant molecule was calculated using:

$$
A =
\frac{N_{\text{normal}}-N_{\text{variant}}}
{N_{\text{normal}}+N_{\text{variant}}}
\times 100
$$

The results are:

| Pair                                 | Asymmetry |
| ------------------------------------ | --------: |
| Carbon monoxide / Carbon-13 monoxide |    0.081% |
| Nitric oxide / Ionised NO            |    0.114% |
| Water / Heavy water                  |    0.998% |
| Methane / Methyl ion                 |    0.894% |
| Ethylene / Ionised ethylene          |    0.562% |
| Ozone / Superoxide anion             |    1.519% |

All six pairs show a slightly higher average count for the normal molecule than for its corresponding variant.

However, the percentage asymmetry should be distinguished from its statistical significance. For example, ozone and superoxide have the largest percentage asymmetry (**1.519%**), but their difference corresponds to only **0.52 standard deviations**. This means that the measured difference is small compared with its statistical uncertainty.

---

## Goal 1: Average Count of Each Molecular Species

The first goal was to determine the average number of each molecular species produced per event and its statistical uncertainty.

The results show that carbon monoxide is the most abundant molecule in the dataset, with an average of:

**19.949508 ± 0.032746 particles per event**

In comparison, ozone is much less frequent:

**0.001187 ± 0.000042 particles per event**

The uncertainty represents the statistical variation between the 10 subsamples.

---

## Goal 2: Asymmetry Between Normal and Variant Molecules

The second goal was to investigate whether there is an asymmetry between the normal and variant molecules.

Every pair has a positive difference, meaning that the normal molecule has a slightly higher average count than its corresponding variant.

The strongest statistical differences are observed for **water vs heavy water (10.06 sigma)**, **methane vs methyl ion (8.41 sigma)** and **carbon monoxide vs carbon-13 monoxide (7.15 sigma)**.

On the other hand, the differences for **nitric oxide vs ionised NO (1.73 sigma)**, **ethylene vs ionised ethylene (0.90 sigma)** and **ozone vs superoxide (0.52 sigma)** are small compared with their statistical uncertainties.

Therefore, the results show that the measured asymmetry is different for each molecular pair, and the statistical significance must be considered alongside the percentage asymmetry.

---

# How the Code Works

## 1. Defining the Molecular Species

The code first creates a dictionary connecting each particle ID to its molecular name:

```python
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
```

This allows the program to convert the particle IDs found in the input files into readable molecular names.

---

## 2. Defining the Pairs

The pairs of normal and variant molecules are stored in a list:

```python
pairs = [
    (211, -211),
    (321, -321),
    (2212, -2212),
    (3122, -3122),
    (3312, -3312),
    (3334, -3334)
]
```

Each pair contains the particle ID of the normal molecule followed by the ID of its variant.

---

## 3. Reading the Input Files

The `analyse_file()` function reads one subsample at a time.

The location of the Python script is found automatically:

```python
script_folder = os.path.dirname(os.path.abspath(__file__))
```

The corresponding input file is then constructed:

```python
filename = os.path.join(
    script_folder,
    "output-Set" + str(subsample) + ".txt"
)
```

This avoids hardcoding the complete file path.

---

## 4. Counting Events and Particles

The code reads the file line by line.

For each event, it first determines how many particles belong to that event:

```python
number_of_particles = int(line.split()[1])
```

Empty events are excluded:

```python
if number_of_particles > 0:
    number_of_events += 1
    remaining = number_of_particles
```

The variable `remaining` keeps track of how many particle lines are still part of the current event.

---

## 5. Counting the Selected Molecules

For each particle, the particle ID is extracted:

```python
particle_id = line.rsplit(None, 1)[1]
```

The code then checks whether the particle is one of the molecular species being studied:

```python
if particle_id in totals:
    totals[particle_id] += 1
```

Particles that are not included in the `molecules` dictionary are ignored.

---

## 6. Calculating the Average

After all files have been analysed, the total number of particles is divided by the total number of events:

```python
final_average = total_particles / total_events
```

This gives the average number of particles per event:

$$
\text{Average} =
\frac{\text{Total number of particles}}
{\text{Total number of events}}
$$

For example, the average number of carbon monoxide molecules is:

$$
\text{Average}_{CO}=19.949508
$$

particles per event.

---

## 7. Calculating the Statistical Uncertainty

The data are divided into 10 subsamples. An average is calculated independently for each subsample.

The function `spread()` calculates the sample standard deviation of these 10 values:

```python
def spread(values, centre):

    squared_differences = sum(
        (value - centre) ** 2
        for value in values
    )

    return math.sqrt(
        squared_differences / (len(values) - 1)
    )
```

The denominator is `len(values) - 1` because the code calculates the **sample standard deviation**.

This spread between the subsample averages is used as the statistical uncertainty.

---

## 8. Comparing the Molecular Pairs

For every normal/variant pair, the difference is calculated:

```python
difference = positive_average - negative_average
```

For example, for carbon monoxide:

$$
19.949508-19.917211=0.032297
$$

The difference is also calculated independently for every subsample. The spread of these differences provides the uncertainty of the difference.

---

## 9. Calculating the Significance

The significance is calculated using:

```python
significance = (
    abs(difference)
    / difference_uncertainty
)
```

For carbon monoxide and carbon-13 monoxide:

$$
\frac{0.032297}{0.004519}
=7.15
$$

Therefore, their difference corresponds to **7.15 standard deviations**.

---

## 10. Calculating the Asymmetry

Finally, the code calculates the asymmetry:

```python
asymmetry = (
    (positive_average - negative_average)
    / (positive_average + negative_average)
)
```

The result is multiplied by 100 to express it as a percentage.

For carbon monoxide and carbon-13 monoxide:

$$
A =
\frac{19.949508-19.917211}
{19.949508+19.917211}
\times100
$$

$$
A \approx 0.081\%
$$

The asymmetry therefore measures the relative difference between the normal and variant molecular populations.

---

## Conclusion

The analysis successfully determines the average number of each molecular species per event and its statistical uncertainty. Carbon monoxide is the most abundant species, while ozone and superoxide are the least abundant.

All six normal/variant pairs show a small positive asymmetry, with values ranging from **0.081% to 1.519%**. However, the statistical significance varies between the pairs. The strongest differences are observed for water, methane and carbon monoxide, while the differences for nitric oxide, ethylene and ozone are small compared with their uncertainties.

Question 3: asymmetry as a function of momentum. This question will be answered in next week assignement 


