#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    dt_re = re.compile(r'^UTC(\+|\-)0?(\d+)\:\d+$')
    tz_utc_hours = dt_re.match(tz_str).groups()
    if tz_utc_hours[0] == '+':
        tz_utc = timezone(timedelta(hours=int(tz_utc_hours[1])))
    elif tz_utc_hours[0] == '-':
        tz_utc = timezone(timedelta(hours=-int(tz_utc_hours[1])))
    else:
        pass
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz_utc)
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
