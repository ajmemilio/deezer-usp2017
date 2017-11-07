import numpy as np
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

print("Started")
RS = 1993
np.random.seed(RS)
folder = '../data/'
train = pd.read_csv(folder + 'train.csv')
test = pd.read_csv(folder + 'test.csv')

def statistics():
	is_listened = len(train['is_listened'])
	class1 = len(train[train.is_listened == 1])
	class0 = len(train[train.is_listened == 0])
	distribuition = train['is_listened'].mean()
	print "is_listened {}".format(is_listened)
	print "class1 {}".format(class1)
	print "class0 {}".format(class0)
	print "distribuition {}".format(distribuition)

	corr = train.corr()
	f, ax = plt.subplots(figsize=(10, 8))
	sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)
	plt.show()

def ts_year(ts):
	return datetime.fromtimestamp(ts).year

def ts_month(ts):
	return datetime.fromtimestamp(ts).month

def ts_day(ts):
	return datetime.fromtimestamp(ts).day

def ts_hour(ts):
	return datetime.fromtimestamp(ts).hour

def ts_minute(ts):
	return datetime.fromtimestamp(ts).minute

def ts_second(ts):
	return datetime.fromtimestamp(ts).second

def to_year(date):
	year = re.findall('\d\d\d\d', str(date))[0]
	return int(year)

def to_month(date):
	month = re.findall('\d\d', str(date))[2]
	return int(month)

def to_day(date):
	day = re.findall('\d\d', str(date))[3]
	return int(day)

def ts_weekday(ts):
	return datetime.fromtimestamp(ts).weekday()

def main():
    print "Generate features train..."
    train['ts_weekday'] = train['ts_listen'].apply(ts_weekday)
    train['ts_year'] = train['ts_listen'].apply(ts_year)
    train['ts_month'] = train['ts_listen'].apply(ts_month)
    train['ts_day'] = train['ts_listen'].apply(ts_day)
    train['ts_hour'] = train['ts_listen'].apply(ts_hour)
    train['ts_minute'] = train['ts_listen'].apply(ts_minute)
    train['ts_second'] = train['ts_listen'].apply(ts_second)
        
    train['release_date_year'] = train['release_date'].apply(to_year)
    train['release_date_month'] = train['release_date'].apply(to_month)
    train['release_date_day'] = train['release_date'].apply(to_day)
        
    print "Generate features test..."
    test['ts_weekday'] = test['ts_listen'].apply(ts_weekday)
    test['ts_year'] = test['ts_listen'].apply(ts_year)
    test['ts_month'] = test['ts_listen'].apply(ts_month)
    test['ts_day'] = test['ts_listen'].apply(ts_day)
    test['ts_hour'] = test['ts_listen'].apply(ts_hour)
    test['ts_minute'] = test['ts_listen'].apply(ts_minute)
    test['ts_second'] = test['ts_listen'].apply(ts_second)
    
    test['release_date_year'] = test['release_date'].apply(to_year)
    test['release_date_month'] = test['release_date'].apply(to_month)
    test['release_date_day'] = test['release_date'].apply(to_day)
        
    train.to_csv('trainv0.12.csv', index=False)
    test.to_csv('testv0.12.csv', index=False)

main()
print "Done"