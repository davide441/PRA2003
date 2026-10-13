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

# Question 3: Asymetry as a function of the momentum
## Method

### Momentum bins

The momentum P (in units of 10⁻²³ kg m/s) was divided into 10 bins with edges:

```
[0, 0.5, 1, 1.5, 2, 2.5, 3, 4, 6, 8, inf]
```

The bins are narrow (0.5) at low P, that's where most of the molecules are, and wider at high P, where there are fewer. The last bin (P > 8) is open-ended. The fraction of all N + N′ counted inside the bins is 1.0000 for every pair, so no molecule is lost by the binning.

### Asymmetry in each bin

For every pair and every momentum bin, the asymmetry is

$$
A = \frac{N - N'}{N + N'}
$$

where N is the number of normal molecules and N′ the number of variant molecules in that bin.

A is calculated **separately in each sub-sample**. The value shown for a bin is the mean over the sub-samples, and the statistical uncertainty is the standard deviation of the sub-sample values. The significance of a bin is |A| / std.

### Overall (mean) asymmetry

The overall asymmetry of a pair is calculated from all momentum bins together, using the same sub-sample method. This gives one value of A with one uncertainty per pair. It is shown as the orange band in Figure 1.

### Checking that the sub-samples are consistent

Before trusting the sub-sample spread as an uncertainty, the code checks that:

* the sub-samples contain almost the same number of events (max/min = 1.001);
* the counts per event in each bin are similar in all sub-samples (spread compared with the Poisson expectation, and a z-score per sub-sample and per bin).

For most pairs the spread is close to the Poisson expectation (ratio of about 1). Carbon monoxide has a spread of 1.3 to 3.6 times the Poisson value.

### Testing the momentum dependence

Three tests were applied to the 10 bins of each pair:

1. **χ² against zero asymmetry**: tests whether the points are compatible with A = 0.
2. **χ² against a constant**: tests whether the points are compatible with a constant asymmetry equal to the overall mean.
3. **Linear fit** A = a + (dA/dP)·P: a slope significantly different from zero would mean that the asymmetry changes with momentum.

The χ² is

$$
\chi^2 = \sum_{i=1}^{10} \frac{(A_i - A_{\text{model}})^2}{\sigma_i^2}
$$

---

## Figures

### Figure 1: Asymmetry as a function of momentum

![Asymmetry as a function of momentum](PRA%20READM%20FIG%201.png)

**What the figure shows.** There is one panel per pair of molecules. The vertical axis is the asymmetry (N − N′)/(N + N′). The horizontal axis is the momentum P in 10⁻²³ kg m/s.

* Each **blue point** is the asymmetry in one momentum bin.
* The **vertical error bar** is the statistical uncertainty of that bin (how large is the spread between sub-samples).
* The **horizontal bar** is the width of the momentum bin. The label "last bin: P > 8" reminds the reader that the final bin is open-ended.
* The **orange band** is the overall asymmetry ± its uncertainty.
* The **dashed grey line** is zero asymmetry.
* The number in the corner is the χ² against zero asymmetry for 10 bins.

**How to read it.** All six panels share the same vertical scale, which is set by the large uncertainties of ozone. On this scale the asymmetries of carbon monoxide (about 0.001), water (about 0.01) and methane (about 0.009) look close to zero. The numbers in the table below give the exact values.
The important result is that in none of the panels do the points show a clear rise or fall with momentum. They pretty much all follow a flat line.

### Figure 2: Momentum spectra of the normal and variant molecules

![Momentum spectra](PRA%20README%20FIG%202.png)

**What the figure shows.** For each pair, the momentum spectrum of the normal molecule (blue) and of the variant (red). The vertical axis (logarithmic) is dN/dP, the number of counts per event per unit of momentum, which means that the counts in each bin are divided by the bin width. This makes bins of different widths comparable. The horizontal bars are the bin widths. The last bin (P > 8) is not drawn.

**What it tells us.**

* The spectra of the normal and the variant molecules **almost overlap in every panel**. The two kinds of molecule are produced with the same momentum distribution, to within the precision visible on a logarithmic plot.
* The spectra have the same shape for all species: they rise to a maximum at low momentum (around P = 0.5 to 1.5, depending on the pair), then fall steeply by one to two orders of magnitude up to P = 8.
* The ozone / superoxide panel has the largest error bars, because there are very few of these molecule.
* A difference of 0.1% to 1% (the size of the asymmetries found here) cannot be seen by eye on a logarithmic spectrum. That is why Figure 1 plots the asymmetry directly.

Figure 2 therefore shows that the normal and variant molecules have the same momentum spectrum overall, and shows where the statistics are large (low and medium P) or small (high P and rare species). Figure 1 quantifies the small difference between them.

---

## Results

### Mean asymmetry of each pair

| Pair | Mean asymmetry A | Statistical uncertainty | Significance |
| ---- | ---------------: | ----------------------: | -----------: |
| Carbon monoxide / Carbon-13 monoxide | +0.00081 | ± 0.00012 | 6.8 sigma |
| Nitric oxide / Ionised NO | +0.00106 | ± 0.00065 | 1.6 sigma |
| Water / Heavy water (D2O) | +0.01012 | ± 0.00095 | 10.7 sigma |
| Methane (CH4) / Methyl ion (CH3-) | +0.00893 | ± 0.00112 | 7.9 sigma |
| Ethylene (C2H4) / Ionised ethylene (C2H3-) | +0.00564 | ± 0.00661 | 0.9 sigma |
| Ozone (O3) / Superoxide anion (O2-) | +0.01739 | ± 0.03018 | 0.6 sigma |

These agree with the percentage asymmetries given in the answer to questions 1 and 2 (for example 0.081 % for carbon monoxide and 0.998 % for water).

### Asymmetry in each momentum bin

Values are in units of 10⁻³, written as A ± uncertainty.

| P range | CO / ¹³CO | NO / NO⁺ | H₂O / D₂O | CH₄ / CH₃⁻ | C₂H₄ / C₂H₃⁻ | O₃ / O₂⁻ |
| ------- | --------: | -------: | --------: | ---------: | -----------: | -------: |
| 0 – 0.5 | 0.11 ± 0.66 | 1.39 ± 2.08 | 6.74 ± 4.72 | 13.14 ± 12.18 | 6.09 ± 51.95 | 105.59 ± 197.03 |
| 0.5 – 1 | 0.46 ± 0.36 | −0.44 ± 1.58 | 9.07 ± 2.29 | 7.77 ± 7.60 | 4.90 ± 18.20 | 8.88 ± 143.02 |
| 1 – 1.5 | 0.62 ± 0.65 | −0.90 ± 2.25 | 7.40 ± 4.40 | 5.34 ± 6.05 | 4.95 ± 14.20 | 81.31 ± 86.60 |
| 1.5 – 2 | 0.60 ± 0.74 | 0.00 ± 1.44 | 9.02 ± 3.34 | 7.58 ± 5.03 | 3.66 ± 26.62 | −1.41 ± 93.32 |
| 2 – 2.5 | 0.86 ± 0.74 | 0.87 ± 3.39 | 8.08 ± 5.21 | 7.65 ± 5.99 | 2.16 ± 19.59 | −10.34 ± 115.11 |
| 2.5 – 3 | 0.79 ± 0.99 | −0.07 ± 3.16 | 7.67 ± 5.42 | 4.13 ± 5.65 | −2.70 ± 26.43 | 85.41 ± 112.20 |
| 3 – 4 | 0.76 ± 0.81 | 1.23 ± 1.72 | 10.26 ± 3.51 | 6.85 ± 8.03 | 7.61 ± 19.55 | 48.03 ± 74.50 |
| 4 – 6 | 1.27 ± 0.62 | 1.95 ± 1.74 | 10.08 ± 3.63 | 9.87 ± 5.27 | 5.48 ± 14.70 | −10.61 ± 71.14 |
| 6 – 8 | 1.72 ± 0.93 | 0.04 ± 2.17 | 11.05 ± 4.33 | 7.32 ± 7.50 | 6.23 ± 13.66 | 15.70 ± 73.32 |
| 8 – inf | 1.75 ± 0.44 | 4.17 ± 1.96 | 13.57 ± 1.23 | 12.80 ± 2.67 | 8.25 ± 11.33 | 1.51 ± 67.45 |

The bins with a significance above 3 sigma are the last bin (P > 8) for carbon monoxide (4.0), water (11.0) and methane (4.8), and the bin 0.5 – 1 for water (4.0). These are the bins with the most counts, they have the smallest uncertainties.

### Quantification of the momentum dependence

| Pair | χ² vs zero (10 bins) | p-value | χ² vs constant | p-value | Slope dA/dP | Slope significance |
| ---- | -------------------: | ------: | -------------: | ------: | ----------: | -----------------: |
| CO / ¹³CO | 29.71 | 0.00095 | 8.39 | 0.59 | +0.00020 ± 0.00011 | 1.8 sigma |
| NO / NO⁺ | 7.03 | 0.72 | 5.36 | 0.87 | +0.00018 ± 0.00032 | 0.6 sigma |
| H₂O / D₂O | 176.46 | 1.3 × 10⁻³² | 9.49 | 0.49 | +0.00043 ± 0.00062 | 0.7 sigma |
| CH₄ / CH₃⁻ | 35.67 | 9.6 × 10⁻⁵ | 3.59 | 0.96 | +0.00021 ± 0.00117 | 0.2 sigma |
| C₂H₄ / C₂H₃⁻ | 1.28 | 0.999 | 0.21 | 1.00 | +0.00034 ± 0.00270 | 0.1 sigma |
| O₃ / O₂⁻ | 2.24 | 0.994 | 1.59 | 0.999 | −0.00732 ± 0.01483 | 0.5 sigma |

Slopes are in units of 10⁻²³ kg m/s per unit of P.

---

## Step 1: Mean asymmetry and its uncertainty

All six pairs have a **positive** mean asymmetry: the normal molecule is produced slightly more often than its variant. The size and the significance are very different from pair to pair:

* **Water / heavy water:** A = +0.01012 ± 0.00095 (10.7 sigma), about 1 %.
* **Methane / methyl ion:** A = +0.00893 ± 0.00112 (7.9 sigma), about 0.9 %.
* **Carbon monoxide / carbon-13 monoxide:** A = +0.00081 ± 0.00012 (6.8 sigma), about 0.08 %. This asymmetry is much smaller than for water and methane, but it is measured very precisely because carbon monoxide is by far the most abundant molecule.
* **Nitric oxide / ionised NO:** A = +0.00106 ± 0.00065 (1.6 sigma). Not significant.
* **Ethylene / ionised ethylene:** A = +0.00564 ± 0.00661 (0.9 sigma). Not significant.
* **Ozone / superoxide anion:** A = +0.01739 ± 0.03018 (0.6 sigma). Not significant. This is the largest asymmetry in size, but also the largest uncertainty, because there are only about 0.001 of these molecules per event.

## Step 2: Asymmetry as a function of momentum

Figure 1 and the χ² tests show that:

* For **carbon monoxide, water and methane**, the asymmetry is **significantly different from zero** (χ² against zero with p < 10⁻³), but **compatible with a constant value** (χ² against a constant with p = 0.49 to 0.96). The asymmetry does not depend significantly on momentum. The linear slopes are 1.8, 0.7 and 0.2 sigma from zero.
* For carbon monoxide, the points rise from about 0.0001 at low P to about 0.0018 at P > 8. This looks like a trend, but the slope is only 1.8 sigma so this is **not** enough evidence to declare a precise momentum dependence.
* For **nitric oxide, ethylene and ozone**, all bins are compatible with zero (p = 0.72, 0.999 and 0.994) and also with the overall mean. The uncertainties in these bins are too large to see any momentum dependence either.
* The most significant bins are at high P, but this is because these bins contain the most counts and not because the asymmetry is larger there.

## Step 3: Is there an asymmetry?

**Yes, for three pairs: water / heavy water, methane / methyl ion and carbon monoxide / carbon-13 monoxide.** In these pairs the normal molecule is produced more often than its variant. The overall significance is 6.8 to 10.7 sigma, and the χ² against zero is rejected with p < 10⁻³. The asymmetry is small (0.08 % to 1 %) and does not depend on momentum within the uncertainties.

**No significant asymmetry is seen for nitric oxide, ethylene and ozone.** Their significance is below 3 sigma, and the data are compatible with zero. This is not proof that there is no asymmetry. For ethylene and ozone in particular, the uncertainties (0.7 % and 3 %) are larger than the asymmetries seen in water and methane, so an asymmetry of that size cannot be excluded with this dataset.

All six asymmetries have the same sign. This may suggest a common origin, but only three are significant on their own.

**Limitations:**

* The uncertainties are statistical only (spread between the sub-samples). Systematic effects are not included.
* The χ² tests assume that the momentum bins are independent.
* The number of sub-samples is small, so the uncertainty itself is only known approximately.
* The two plot present on this README file do not take into account output10 (file 10) due to its high rate of error. If file 10 was taken into consideration in this analysis, the second plot would have display larger vertical error bars, even if the plotted mean points look almost identical without the use of file 10. Removing this file from our analysis allowed more clearer results

ADD FILE 10 LIMITATIONS

---

# How the Code Works

## 1. Defining the momentum bins

```python
BINS = [0, 0.5, 1, 1.5, 2, 2.5, 3, 4, 6, 8, float("inf")]
```

Each particle is assigned to a bin according to its momentum P. For each sub-sample, the counts N (normal) and N′ (variant) are stored per bin.

## 2. Reading the sub-samples

The input files are read one sub-sample at a time, as in questions 1 and 2. For each event the particle ID and the momentum are read, and empty events are excluded from the number of events. The counts per event are obtained by dividing by the number of non-empty events of the sub-sample.

## 3. Asymmetry in each bin and sub-sample

```python
asymmetry = (N - N_prime) / (N + N_prime)
```

This is calculated for each of the 10 bins in each sub-sample, giving an array with one row per sub-sample and one column per bin.

## 4. Mean and uncertainty in each bin

```python
A_bin = asymmetry.mean(axis=0)
err_bin = asymmetry.std(axis=0, ddof=1)
significance = abs(A_bin) / err_bin
```

`ddof=1` gives the sample standard deviation, as in questions 1 and 2. These are the points and error bars of Figure 1.

## 5. Overall asymmetry

The overall asymmetry is calculated with all momentum bins together, in each sub-sample, and then averaged with its spread as the uncertainty. It is displayed as the orange band in Figure 1.

## 6. Quantifying the momentum dependence

```python
chi2_zero = np.sum((A_bin / err_bin) ** 2)
chi2_const = np.sum(((A_bin - A_mean) / err_bin) ** 2)
```

The p-values are obtained from the χ² distribution with 10 degrees of freedom. A weighted linear fit of A against the bin centres gives the slope and its uncertainty.

## 7. Homogeneity check

The code compares the counts per event in each bin between sub-samples, and calculates the relative spread and the Poisson expectation. A z-score is computed for each sub-sample and bin, and sub-samples with |z| > 2 are flagged. With 6 pairs × 10 bins and several sub-samples, a few flagged values (about 5 %) are expected by chance. The output shows a small number of flags, consistent with this.

## 8. Plots

* **Figure 1** plots A with its error bars against P, for each pair, with the overall mean as an orange band and the χ² against zero.
* **Figure 2** plots dN/dP (counts per event divided by the bin width) against P for the normal and variant molecules, on a logarithmic vertical axis.

---

## Conclusion

The asymmetry between normal and variant molecules was measured as a function of momentum in 10 bins. A small, positive asymmetry is seen for **water / heavy water (+1.0 %)**, **methane / methyl ion (+0.9 %)** and **carbon monoxide / carbon-13 monoxide (+0.08 %)**, with significances of 10.7, 7.9 and 6.8 sigma. In all three cases the asymmetry is compatible with a constant value over the whole momentum range. No significant slope with momentum is found (at most 1.8 sigma, for carbon monoxide).

For **nitric oxide, ethylene and ozone**, no significant asymmetry is observed (1.6, 0.9 and 0.6 sigma). The statistics of ethylene and ozone are too low to exclude an asymmetry of the size seen in the other pairs.


