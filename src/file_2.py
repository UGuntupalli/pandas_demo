from datetime import datetime
from src.file_1 import get_end_of_month


# Test
my_date = datetime(2020, 2, 1)
end_of_month = get_end_of_month(my_date)

print(end_of_month)