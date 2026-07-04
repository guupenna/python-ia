import pandas as pd

def print_statistics(feat):
    print(f"Mean: {feat.mean():.2f}")
    print(f"Median: {feat.median():.2f}")
    print(f"Standard deviation: {feat.std():.2f}")
    print(f"Min: {feat.min():.2f}")
    print(f"Max: {feat.max():.2f}")

df = pd.read_csv("healthcare-dataset-stroke-data.csv")

mask_stroke = df["stroke"] == 1
mask_not_stroke = df["stroke"] == 0

ages = df["age"]
bmi = df["bmi"].dropna()
gl_lvl = pd.to_numeric(df["avg_glucose_level"], errors="coerce").dropna()

print("Statistics for age with stroke:")
print_statistics(ages[mask_stroke])
print("Statistics for age without stroke:")
print_statistics(ages[mask_not_stroke])

print("\nStatistics for bmi with stroke:")
print_statistics(bmi[mask_stroke])
print("Statistics for bmi without stroke:")
print_statistics(bmi[mask_not_stroke])

print("\nStatistics for average glucose level with stroke:")
print_statistics(gl_lvl[mask_stroke])
print("Statistics for average glucose level without stroke:")
print_statistics(gl_lvl[mask_not_stroke])
