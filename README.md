PRA2003- Simulating molecular emissions in a combustible reaction
# Davide Capurro - I6382558

Goals: (answer these questions):
1. What are the average counts of each molecular species and their statistical uncertainties ,
2. Is there an asymetry between the normal and the variant molecule ?
3. Is there any asymetry as a function of their momentum ? 

## Goals

The goals of this analysis are:

1. Determine the **average count of each molecular species per event** and its statistical uncertainty.
2. Determine whether there is an **asymmetry between the normal and variant molecules**.

The analysis uses **9 subsamples**, from `output-Set1.txt` to `output-Set9.txt`, excluding `output-Set0.txt`. Each file contains **500,000 events**, giving a total of **4,500,000 events**.

---

## Results

### 1. Average Molecular Counts

The average molecular count per event and its statistical uncertainty are:

| ID | Molecular species | Average/event | Statistical uncertainty |
|---:|---|---:|---:|
| 211 | Carbon monoxide | 18.422534 | 0.009307 |
| -211 | Carbon-13 monoxide | 18.392882 | 0.009056 |
| 321 | Nitric oxide | 2.316509 | 0.000957 |
| -321 | Ionised NO | 2.311606 | 0.001559 |
| 2212 | Water | 1.115786 | 0.000580 |
| -2212 | Heavy water (D₂O) | 1.093432 | 0.000680 |
| 3122 | Methane (CH₄) | 0.255393 | 0.000330 |
| -3122 | Methyl ion (CH₃⁻) | 0.250871 | 0.000306 |
| 3312 | Ethylene (C₂H₄) | 0.036391 | 0.000080 |
| -3312 | Ionised ethylene (C₂H₃⁻) | 0.035983 | 0.000123 |
| 3334 | Ozone (O₃) | 0.001099 | 0.000013 |
| -3334 | Superoxide anion (O₂⁻) | 0.001061 | 0.000016 |

### 2. Asymmetry Between Normal and Variant Molecules

The asymmetry was calculated for each normal/variant pair. A positive asymmetry indicates that the normal molecule has a higher average count than its variant.

| Pair | Asymmetry | Uncertainty | Significance |
|---|---:|---:|---:|
| 211 / -211 | 0.000805 | 0.000353 | 2.283 |
| 321 / -321 | 0.001059 | 0.000395 | 2.679 |
| 2212 / -2212 | 0.010118 | 0.000405 | 24.979 |
| 3122 / -3122 | 0.008932 | 0.000889 | 10.050 |
| 3312 / -3312 | 0.005640 | 0.002029 | 2.781 |
| 3334 / -3334 | 0.017389 | 0.009799 | 1.775 |

All six pairs show a **positive asymmetry**, meaning that the normal molecular species has a slightly higher average count than its corresponding variant.

The largest statistically supported asymmetries are observed for **water** and **methane**. The ozone pair has the largest numerical asymmetry, but also the largest relative uncertainty.

## How the Code Works

The code processes the data in several steps:

### 1. Select the input files

The code uses `output-Set1.txt` to `output-Set9.txt`, excluding `output-Set0.txt`. Each file contains 500,000 events, giving a total of 9 subsamples.

```python
files = [os.path.join(folder, f"output-Set{i}.txt") for i in range(1, 10)]
N_subsamples = len(files)
```

### 2. Count the molecular species

Each file is read line by line. Particle lines contain four values, with the fourth value corresponding to the molecular ID.

```python
if len(data) == 4:
    ID = int(data[3])
    if ID in counts:
        counts[ID] += 1
```

### 3. Calculate the average count per event

The number of molecules found in each file is divided by the 500,000 events in that file.

```python
means[ID].append(counts[ID] / N_events)
```

This produces one average count per event for each molecule in each subsample.

### 4. Calculate the overall average

The nine subsample averages are averaged to obtain the final molecular count per event.

```python
avg = sum(means[ID]) / N_subsamples
```

### 5. Calculate the statistical uncertainty

The standard deviation of the nine subsample means is calculated. The statistical uncertainty on the final average is then obtained by dividing the standard deviation by the square root of the number of subsamples.

```python
sd = math.sqrt(
    sum((x - avg) ** 2 for x in means[ID])
    / (N_subsamples - 1)
)

error = sd / math.sqrt(N_subsamples)
```

This is the **sub-sampling method** used to estimate the statistical uncertainty.

### 6. Calculate the asymmetry

For each normal/variant molecule pair, the asymmetry is calculated using:

$$
A = \frac{N_{\text{normal}} - N_{\text{variant}}}
{N_{\text{normal}} + N_{\text{variant}}}
$$

A positive asymmetry means that the normal molecule has a higher average count than its variant.

### 7. Calculate the asymmetry uncertainty

The uncertainty on the asymmetry is calculated using standard error propagation:

$$
\sigma_A =
\frac{2}{(N_1+N_2)^2}
\sqrt{N_2^2\sigma_1^2 + N_1^2\sigma_2^2}
$$

### 8. Calculate the significance

Finally, the significance of the asymmetry is calculated as:

$$
\text{Significance} = \frac{|A|}{\sigma_A}
$$

This compares the measured asymmetry with its statistical uncertainty. A larger value indicates that the asymmetry is larger relative to its uncertainty.

### Conclusion

All six molecule pairs show a **positive asymmetry**, meaning that the normal molecule is slightly more common than its variant.

For **water (24.979)** and **methane (10.050)**, the asymmetry is greater than 3, indicating a statistically significant difference compared with the statistical uncertainty.

For **carbon monoxide (2.283)**, **nitric oxide (2.679)**, **ethylene (2.781)** and **ozone (1.775)**, the asymmetry is below 3. Therefore, based on this 3-significance threshold, the results do not provide sufficient statistical evidence to conclude that these pairs have a significant asymmetry. The observed differences could be consistent with statistical fluctuations.
