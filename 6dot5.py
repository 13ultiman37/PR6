import pandas as pd
import scipy.stats as sts

df = pd.read_csv("bmi.csv", delimiter=',')
NW = df[df["region"] == "northwest"]
SW = df[df["region"] == "southwest"]

res1 = sts.shapiro(NW["bmi"])
res2 = sts.shapiro(SW["bmi"])

print(res1, "\n", res2)

res = sts.bartlett(NW["bmi"], SW["bmi"])
print("\n", res)

t_res = sts.ttest_ind(NW["bmi"], SW["bmi"])
print("\n", t_res)
