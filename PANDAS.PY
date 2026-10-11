import pandas as pd
import numpy as np

random_numbers = np.random.randint(1, 100, size=10)

series = pd.Series(random_numbers)

print("Pandas Series with Ten Random Numbers:")
print(series)