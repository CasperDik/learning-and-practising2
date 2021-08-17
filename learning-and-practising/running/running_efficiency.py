# question: am i running more efficient when going faster?
# hypothesis:  yes. why: it feels like that

import pandas as pd
import stata_setup
stata_setup.config("C:/Program Files/Stata17", "se")
df = pd.read_csv("data/csv files/aggregated_running_data.csv")
df = df.drop(df[df["timer(sec)"] < 60*3].index)
df = df.drop(df[df["speed"] < 1.5].index)


from pystata import stata
stata.pdataframe_to_data(df, True)
stata.run(""" gen eff = speed/heart_rate
twoway(scatter eff speed)
graph export scatter_eff_speed.svg, replace
corr eff speed
reg eff temperature altitude distance 
reg eff speed temperature altitude distance cadence stance_time stance_time_balance step_length vertical_ratio
""")
