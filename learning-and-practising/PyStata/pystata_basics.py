# connect to stata
import stata_setup
stata_setup.config("C:/Program Files/Stata17", "se")

# its red underlined but works somehow
from PyStata import stata

# import data as dataframe
import pandas as pd
data = pd.read_csv("../Running/data/csv files/aggregated_running_data.csv")

# load dataframe to stata
stata.pdataframe_to_data(data, True)

# run some stata commands
stata.run('''reg speed heart_rate''')    # ''' for multiple lines in stata
stata.run("reg speed heart_rate")   # "" works only for single lines
stata.run("reg speed heart_rate", quietly=True)     # doesn't display results in console

# find more commands here:
# https://www.stata.com/python/pystata/stata.html

# how returns are stored in stata
stata.run("return list")
print("\n")
stata.run("ereturn list")
print("\n")
stata.run("sreturn list")
print("\n")

# get returns to python as dictionary
r = stata.get_return()
print(r)
r = r['r(table)']

# can also get s() and e() returns from stata
e = stata.get_ereturn()
print(e)
e = e["e(N)"]

s = stata.get_sreturn()

# create graphs etc --> works the same as in stata
stata.run("twoway(scatter speed heart_rate if timersec < 7*60 & speed > 2.5)", quietly=True)
stata.run("graph export test.svg, replace")



