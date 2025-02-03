# RMSD stability

From the RMSD computation CSV files of the rms script (https://github.com/njeanne/rms), compute the mean and 
standard deviation of the RMSD values from a start frame to an end frame.
A CSV file of the RMSD means and standard deviations for the selection and for the whole data is produced.

## Conda environment

A [conda](https://docs.conda.io/projects/conda/en/latest/index.html) YAML environment file is provided: `conda_env/rmsd_stability_env.yml`. The file contains all the dependencies to run the script.
The conda environment is created using the command:
```shell script
# create the environment
conda env create -f conda_env/rmsd_stability_env.yml

# activate the environment
conda activate rmsd_stability
```

## Usage

```shell script
./rmsd_stability.py --start 70000 --out results/first_frame_reference_RMSD_statistics.csv data
```

## Output

A CSV file of the means and standard deviations for the selected frames,
here from the 70 000th frame to the end, and from the first frame to the end:

|sample                       |selected frames|RMSD mean selected frames|RMSD standard deviation selected frames|all frames|RMSD mean all frames|RMSD standard deviation all frames|
|-----------------------------|---------------|-------------------------|---------------------------------------|----------|--------------------|----------------------------------|
|AB248520-3e_WT_ORF1_0        |70000 - 255000 |15.39                    |0.33                                   |1 - 255000|14.89               |1.31                              |
|AB291961-3f_WT_ORF1_0        |70000 - 255000 |16.99                    |0.2                                    |1 - 255000|16.76               |0.71                              |
|AB437318-3b_WT_ORF1_0        |70000 - 255000 |17.58                    |0.33                                   |1 - 255000|17.5                |0.85                              |
|EU495148-3f_WT_ORF1_0        |70000 - 255000 |16.09                    |0.36                                   |1 - 255000|15.9                |0.96                              |
|FJ653660-3f_WT_ORF1_0        |70000 - 255000 |13.81                    |0.28                                   |1 - 255000|13.71               |0.66                              |
|FJ956757-3f_WT_ORF1_0        |70000 - 255000 |14.97                    |0.35                                   |1 - 255000|14.53               |0.95                              |
|HEPAC-100_GATM_ORF1_0        |70000 - 255000 |18.75                    |0.54                                   |1 - 255000|18.41               |1.48                              |
|HEPAC-100_PEPB1_ORF1_0       |70000 - 255000 |16.37                    |0.21                                   |1 - 255000|15.96               |0.97                              |
|HEPAC-12-1_duplication_ORF1_0|70000 - 255000 |13.12                    |0.62                                   |1 - 255000|12.31               |1.58                              |
|HEPAC-12-2_duplication_ORF1_0|70000 - 255000 |21.58                    |0.36                                   |1 - 255000|20.98               |1.62                              |
|HEPAC-12-3_duplication_ORF1_0|70000 - 255000 |14.14                    |0.43                                   |1 - 255000|14.03               |0.59                              |
|HEPAC-154_KIF1B_ORF1_0       |70000 - 255000 |17.04                    |0.4                                    |1 - 255000|16.88               |0.6                               |
|HEPAC-26_RPL6_ORF1_0         |70000 - 255000 |38.37                    |0.98                                   |1 - 255000|35.47               |6.0                               |
|HEPAC-64_ZNF787_ORF1_0       |70000 - 255000 |14.91                    |0.31                                   |1 - 255000|14.7                |0.76                              |
|HEPAC-6_RNF19A_ORF1_0        |70000 - 255000 |18.93                    |0.5                                    |1 - 255000|18.16               |1.49                              |
|HEPAC-93_EEF1A1_ORF1_0       |70000 - 255000 |21.51                    |0.21                                   |1 - 255000|21.31               |0.96                              |
|HEPAC-93_RNA18SP5_ORF1_0     |70000 - 255000 |16.47                    |0.23                                   |1 - 255000|16.19               |0.77                              |
|HEPAC-95_duplication_ORF1_0  |70000 - 255000 |18.67                    |0.31                                   |1 - 255000|18.3                |1.0                               |
|JN837481-3a_WT_ORF1_0        |70000 - 255000 |10.28                    |0.18                                   |1 - 255000|10.23               |0.36                              |
|JN906974-3f_WT_ORF1_0        |70000 - 255000 |17.42                    |0.27                                   |1 - 255000|16.87               |1.16                              |
|JQ679013_RPS17_ORF1_0        |70000 - 255000 |14.41                    |0.21                                   |1 - 255000|13.82               |1.23                              |
|JQ679014_WT_ORF1_0           |70000 - 255000 |18.1                     |0.27                                   |1 - 255000|17.53               |1.51                              |
|KT447527-3efg_WT_ORF1_0      |70000 - 255000 |12.24                    |0.31                                   |1 - 255000|12.06               |0.74                              |
|KT447528-3a_WT_ORF1_0        |70000 - 255000 |14.75                    |0.25                                   |1 - 255000|14.74               |0.5                               |
|KU980235-3f_WT_ORF1_0        |70000 - 255000 |12.02                    |0.22                                   |1 - 255000|11.9                |0.55                              |
|KY232312-3f_WT_ORF1_0        |70000 - 255000 |17.81                    |0.43                                   |1 - 255000|17.71               |0.74                              |
|KY780957-3chi_WT_ORF1_0      |70000 - 255000 |12.47                    |0.78                                   |1 - 255000|11.98               |1.17                              |
|MF444031-3c_WT_ORF1_0        |70000 - 255000 |11.22                    |0.97                                   |1 - 255000|11.49               |1.14                              |
|MG783569-3_WT_ORF1_0         |70000 - 255000 |15.56                    |0.22                                   |1 - 255000|14.96               |1.25                              |
