import datetime
def get_last_month(option: str=None) -> datetime.date:
    """現在日時から先月を取得する

    Returns:
        datetime.date: 当月1日 - 1日 = 先月末
    """
    now = datetime.datetime.now()
    first_day_of_this_month = datetime.datetime(now.year, now.month, 1)
    last_month = first_day_of_this_month - datetime.timedelta(days=1)
    
    if option == None:
        return last_month
    
    if option == 'yyyymm':
        return last_month.strftime('%Y%m')