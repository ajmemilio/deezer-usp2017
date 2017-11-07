#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:39:06 2017

@author: joao
"""

import pandas as pd

print "Started"

train = pd.read_csv("../train.csv")
test = pd.read_csv("../test.csv")

def get_day_period(hour):
    hour = hour[0]
    # --> Morning = 0400-1000
    mornStart = 6
    mornEnd = 11
    # --> Midday = 1000-1600
    midStart =  12
    midEnd = 17
    # --> Evening = 1600-2200
    eveStart = 18
    eveEnd = 23
    # --> Late Night = 2200-0400
    lateStart = 0
    lateEnd = 5

    if (hour >= mornStart) and (hour <= mornEnd):
      day_period = 0 #morning
    elif (hour >= midStart) and (hour <= midEnd):
      day_period = 1 #midday
    elif (hour >= eveStart) and (hour <= eveEnd):
      day_period = 2 #evening
    elif (hour >= lateStart) and (hour <= lateEnd):
      day_period = 3 #late night

    return day_period

def main():
    print "Generate features train..."
    train['day_period'] = train[['ts_hour']].apply(get_day_period, axis=1, raw=True)
    
    day_period_accepted = train.groupby(['user_id', 'day_period']).mean()['is_listened']
    dict_day_period_accepted = dict(day_period_accepted)
    
    def listened_user_by_day_period(row):
        user = row[0]
        day_period = row[1]
        key = (user, day_period)
        
        if key not in dict_day_period_accepted:
            return 0.0
        else:
            return dict_day_period_accepted[key]
    train['day_period_accepted_rate'] = train[['user_id', 'day_period']].apply(listened_user_by_day_period, axis=1, raw=True)
    
    train.to_csv('trainv6_25.csv', index=False)
    
    print "Generate features test..."
    test['day_period'] = test[['ts_hour']].apply(get_day_period, axis=1, raw=True)
    test['day_period_accepted_rate'] = test[['user_id', 'day_period']].apply(listened_user_by_day_period, axis=1, raw=True)
    
    test.to_csv('testv6_25.csv', index=False)
    
main()
print "Done"