from datetime import datetime
from calendar import monthrange


def get_end_of_month(input_date: datetime) -> datetime:
    """Returns the end of the month as a datetime object

    :param input_date: date for which end of month is desired
    """
    _, last_day_of_month = monthrange(input_date.year, input_date.month)
    return datetime(input_date.year, input_date.month, last_day_of_month)