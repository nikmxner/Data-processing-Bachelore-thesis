import pandas as pd
import matplotlib .pyplot as plt
from matplotlib.pyplot import figure

#kinds of data
#aei = avatar, environment, interaction
aei = ["Avatar", "Environment", "Interaction"]
Simulation = ["Simulation"]
indsutries = ["Agriculture & Food", "Art", "Convention Industry", "E-Commerce", "Education", "Entertainment", "Finance", "Healthcare", "Infrastructure", "Manufacturing", "Public Sector", "Real-Estate", "Research", "Social Sector", "Sport", "Tourism"]

#read csv
raw_df = pd.read_csv('data.csv', sep=";", index_col=0, encoding='latin-1', engine="python")

#dataframes
simulation_df = raw_df[Simulation].copy()
industry_df = raw_df[indsutries].copy()
aei_df = raw_df[aei].copy()
Year_df = raw_df["Year"].copy()
simulation_by_industry = pd.concat([simulation_df, industry_df], axis=1).fillna(0)


#simulation type by industry
simulation_by_industry = simulation_by_industry.set_index(Simulation)
simulation_by_industry = simulation_by_industry.replace({"Agriculture & Food": 1, "Art": 1, "Convention Industry": 1, "E-Commerce": 1, "Education": 1, "Entertainment": 1, "Finance": 1, "Healthcare": 1, "Infrastructure": 1, "Manufacturing": 1, "Public Sector": 1, "Real-Estate": 1, "Research": 1, "Social Sector": 1, "Sport": 1, "Tourism": 1})
simulation_by_industry = simulation_by_industry.groupby(level=0).sum()
simulation_by_industry = simulation_by_industry.transpose()
sib_visual = simulation_by_industry.plot(kind='bar', colormap="copper", stacked=False, title="Simulation or Digital Twin by industry", figsize=(20,15), label="Simulation or Digital Twin by industry")
plt.savefig("[PLOT] Simulation_by_industry_bar_plot.png")


#simulation type 
simulation_visual = simulation_df.apply(pd.value_counts).fillna(0)
s_visual = simulation_visual.plot(kind='bar', colormap="copper", stacked=False, title="Simulation or Digital Twin", figsize=(20,15), label="Simulation or Digital Twin?")
plt.savefig("[PLOT] Simulation_bar_plot.png")

#industry type
industry_visual = industry_df.apply(pd.value_counts).fillna(0)
i_visual = industry_visual.plot(kind='bar', colormap="copper", stacked=True, title="Industry", figsize=(20,15), label="Industry")
plt.savefig("[PLOT] Industry_bar_plot.png")

#usage avatar, environment, interaction
aei_visual = aei_df.apply(pd.value_counts).fillna(0) 
aei_visual = aei_visual.plot(kind='bar', colormap="copper", stacked=True, title="Avatar, Environment, Interaction", figsize=(20,15), label="Avatar, Environment, Interaction")
plt.savefig("[PLOT] AEI_bar_plot.png")


