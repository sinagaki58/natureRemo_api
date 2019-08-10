from datetime import datetime, timedelta

def parse_date_time(date_str: str):
  tz_jst = timedelta(hours=9)
  date_str = date_str.replace('Z', '')
  return (datetime.fromisoformat(date_str) + tz_jst).strftime('%Y-%m-%d %H:%M:%S')
