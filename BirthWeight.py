import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("birthweight.csv")
x_dict = {"Gestation": "Gestation period in weeks",
          "mage": "Mother's age",
          "mnocig": "Number of cigarettes per day smoked by mother",
          "mheight": "Mother's height",
          "mppwt": "Mother's pre-pregnancy weight",
          "fage": "Father's age",
          "fedyrs": "Father's years of education",
          "fnocig": "Number of cigarettes per day smoked by father",
          "fheight": "Height of father"}
y = df['Birthweight']

for col_name in df:
    if col_name == 'Birthweight':
        continue
    x = df[col_name]
    plt.scatter(x, y)
    plt.xlabel(x_dict[col_name])
    plt.ylabel("Baby's weight at birth")
    plt.title("Baby's weight at birth vs " + x_dict[col_name])
    plt.show()
