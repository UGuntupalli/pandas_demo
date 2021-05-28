import pandas as pd 
import numpy as np 
from datetime import datetime
from file_1 import get_end_of_month
from file_0 import cleanse_dataframe


# Test
my_date = datetime(2020, 2, 1)
end_of_month = get_end_of_month(my_date)

# Test 1 
df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))

print(end_of_month)
