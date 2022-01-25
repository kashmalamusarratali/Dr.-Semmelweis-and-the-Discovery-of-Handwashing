import pandas as pd
import matplotlib.pyplot as plt
yearly = pd.read_csv("dataset/yearly_deaths_by_clinic.csv")
print(yearly.head())
print(yearly["clinic"].unique())
yearly["proportion_deaths"] = yearly["deaths"]/yearly["births"]
# Extract Clinic 1 data into clinic_1 and Clinic 2 data into clinic_2
clinic_1 = yearly[yearly["clinic"]== "clinic 1"]
clinic_2 = yearly[yearly["clinic"]== "clinic 2"]
# Print out clinic_1
print(clinic_1)
# Plot yearly proportion of deaths at the two clinics
ax = clinic_1.plot(x="year", y="proportion_deaths",
                         label="Clinic 1")
clinic_2.plot(x="year", y="proportion_deaths",
                   label="Clinic 2", ax=ax, ylabel="Proportion deaths")
plt.show()
# Read datasets/monthly_deaths.csv into monthly
monthly = pd.read_csv("dataset/monthly_deaths.csv")
print(monthly.head())
# Calculate proportion of deaths per no. births
monthly["proportion_deaths"] = monthly["deaths"]/monthly["births"]
monthly["date"] = pd.to_datetime(monthly["date"])
# Plot monthly proportion of deaths
ax = monthly.plot(x="date", y="proportion_deaths", ylabel="Proportion deaths")
plt.show()
# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing =  monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]

# Plot monthly proportion of deaths before and after handwashing
ax = before_washing.plot(x="date", y="proportion_deaths",
                         label="Before handwashing")
after_washing.plot(x="date", y="proportion_deaths",
                   label="After handwashing", ax=ax, ylabel="Proportion deaths")

plt.show()
# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing["proportion_deaths"]
after_proportion = after_washing["proportion_deaths"]
mean_diff = after_proportion.mean()-before_proportion.mean()
print(mean_diff)
# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append( boot_after.mean() - boot_before.mean() )

# Calculating a 95% confidence interval from boot_mean_diff
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
print(confidence_interval)
# The data Semmelweis collected points to that:
doctors_should_wash_their_hands = False
