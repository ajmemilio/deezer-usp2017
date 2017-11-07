#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:26:35 2017

@author: joao
"""
import pandas as pd
import numpy as np

print("Started")
RS = 12357
np.random.seed(RS)
folder = '../'
train = pd.read_csv(folder + 'train.csv')
test = pd.read_csv(folder + 'test.csv')

genre_accepted_sum = train.groupby(['user_id', 'genre_id']).sum()['is_listened']
dict_genre_accepted_sum = dict(genre_accepted_sum)
    
def listened_user_by_genre_sum(row):
    user = row[0]
    genre = row[1]
    key = (user, genre)
    
    if key not in dict_genre_accepted_sum:
        return None
    else:
        return dict_genre_accepted_sum[key]

media_accepted_sum = train.groupby(['user_id', 'media_id']).sum()['is_listened']
dict_media_accepted_sum = dict(media_accepted_sum)
    
def listened_user_by_media_sum(row):
    user = row[0]
    media = row[1]
    key = (user, media)
    
    if key not in dict_media_accepted_sum:
        return None
    else:
        return dict_media_accepted_sum[key]

album_accepted_sum = train.groupby(['user_id', 'album_id']).sum()['is_listened']
dict_album_accepted_sum = dict(album_accepted_sum)

def listened_user_by_album_sum(row):
    user = row[0]
    album = row[1]
    key = (user, album)
    
    if key not in dict_album_accepted_sum:
        return None
    else:
        return dict_album_accepted_sum[key]
    
artist_accepted_sum  = train.groupby(['user_id', 'artist_id']).sum()['is_listened']
dict_artist_accepted_sum = dict(artist_accepted_sum)

def listened_user_by_artist_sum(row):
    user = row[0]
    artist = row[1]
    key = (user, artist)
    
    if key not in dict_artist_accepted_sum:
        return None
    else:
        return dict_artist_accepted_sum[key]

context_type_accpeted_sum = train.groupby(['user_id', 'context_type']).sum()['is_listened']
dict_context_type_accpeted_sum = dict(context_type_accpeted_sum)

def listened_user_by_context_type_sum(row):
    user = row[0]
    context_type = row[1]
    key = (user, context_type)
    
    if key not in dict_context_type_accpeted_sum:
        return None
    else:
        return dict_context_type_accpeted_sum[key]

ts_hour_accepted_sum  = train.groupby(['user_id', 'ts_hour']).sum()['is_listened']
dict_ts_hour_accepted_sum = dict(ts_hour_accepted_sum)  

def listened_user_by_ts_hour_sum(row):
    user = row[0]
    hour = row[1]
    key = (user, hour)

    if key not in dict_ts_hour_accepted_sum:
        return None
    else:
        return dict_ts_hour_accepted_sum[key]
"""
ts_hour_artist_accepted_sum  = train.groupby(['user_id', 'ts_hour', 'artist_id']).sum()['is_listened']
dict_ts_hour_artist_accepted_sum = dict(ts_hour_artist_accepted_sum)    

def listened_user_by_ts_hour_artist_sum(row):
    user = row[0]
    hour = row[1]
    artist = row[2]
    key = (user, hour, artist)

    if key not in dict_ts_hour_artist_accepted_sum:
        return None
    else:
        return dict_ts_hour_artist_accepted_sum[key]

ts_hour_media_accepted_sum  = train.groupby(['user_id', 'ts_hour', 'media_id']).sum()['is_listened']
dict_ts_hour_media_accepted_sum = dict(ts_hour_media_accepted_sum)    

def listened_user_by_ts_hour_media_sum(row):
    user = row[0]
    hour = row[1]
    media = row[2]
    key = (user, hour, media)

    if key not in dict_ts_hour_media_accepted_sum:
        return None
    else:
        return dict_ts_hour_media_accepted_sum[key]

ts_hour_album_accepted_sum  = train.groupby(['user_id', 'ts_hour', 'album_id']).sum()['is_listened']
dict_ts_hour_album_accepted_sum = dict(ts_hour_album_accepted_sum)    

def listened_user_by_ts_hour_album_sum(row):
    user = row[0]
    hour = row[1]
    album = row[2]
    key = (user, hour, album)

    if key not in dict_ts_hour_album_accepted_sum:
        return None
    else:
        return dict_ts_hour_album_accepted_sum[key]

ts_hour_genre_accepted_sum  = train.groupby(['user_id', 'ts_hour', 'genre_id']).sum()['is_listened']
dict_ts_hour_genre_accepted_sum = dict(ts_hour_genre_accepted_sum)    

def listened_user_by_ts_hour_genre_sum(row):
    user = row[0]
    hour = row[1]
    genre = row[2]
    key = (user, hour, genre)

    if key not in dict_ts_hour_genre_accepted_sum:
        return None
    else:
        return dict_ts_hour_genre_accepted_sum[key]

ts_hour_context_type_accepted_sum  = train.groupby(['user_id', 'ts_hour', 'context_type']).sum()['is_listened']
dict_ts_hour_context_type_accepted_sum = dict(ts_hour_context_type_accepted_sum)    

def listened_user_by_ts_hour_context_type_sum(row):
    user = row[0]
    hour = row[1]
    context_type = row[2]
    key = (user, hour, context_type)

    if key not in dict_ts_hour_context_type_accepted_sum:
        return None
    else:
        return dict_ts_hour_context_type_accepted_sum[key]
"""

def main():
    print "Generate features train..."
    train['genre_accepted_sum'] = train[['user_id', 'genre_id']].apply(listened_user_by_genre_sum, axis=1, raw=True)
    train['media_accepted_sum'] = train[['user_id', 'media_id']].apply(listened_user_by_media_sum, axis=1, raw=True)
    train['album_accepted_sum'] = train[['user_id', 'album_id']].apply(listened_user_by_album_sum, axis=1, raw=True)
    train['artist_accepted_sum'] = train[['user_id', 'artist_id']].apply(listened_user_by_artist_sum, axis=1, raw=True)
    train['context_type_accepted_sum'] = train[['user_id', 'context_type']].apply(listened_user_by_context_type_sum, axis=1, raw=True)
    train['ts_hour_accepted_sum'] = train[['user_id', 'ts_hour']].apply(listened_user_by_ts_hour_sum, axis=1, raw=True)
    
    #train['ts_hour_genre_accepted_sum'] = train[['user_id', 'ts_hour', 'genre_id']].apply(listened_user_by_ts_hour_genre_sum, axis=1, raw=True)
    #train['ts_hour_media_accepted_sum'] = train[['user_id', 'ts_hour', 'media_id']].apply(listened_user_by_ts_hour_media_sum, axis=1, raw=True)
    #train['ts_hour_album_accepted_sum'] = train[['user_id', 'ts_hour', 'album_id']].apply(listened_user_by_ts_hour_album_sum, axis=1, raw=True)
    #train['ts_hour_context_type_accepted_sum'] = train[['user_id', 'ts_hour', 'context_type']].apply(listened_user_by_ts_hour_context_type_sum, axis=1, raw=True)
    #train['ts_hour_artist_accepted_sum'] = train[['user_id', 'ts_hour', 'artist_id']].apply(listened_user_by_ts_hour_artist_sum, axis=1, raw=True)

    print "Generate features test..."
    test['genre_accepted_sum'] = test[['user_id', 'genre_id']].apply(listened_user_by_genre_sum, axis=1, raw=True)
    test['media_accepted_sum'] = test[['user_id', 'media_id']].apply(listened_user_by_media_sum, axis=1, raw=True)
    test['album_accepted_sum'] = test[['user_id', 'album_id']].apply(listened_user_by_album_sum, axis=1, raw=True)
    test['artist_accepted_sum'] = test[['user_id', 'artist_id']].apply(listened_user_by_artist_sum, axis=1, raw=True)
    test['context_type_accepted_sum'] = test[['user_id', 'context_type']].apply(listened_user_by_context_type_sum, axis=1, raw=True)
    test['ts_hour_accepted_sum'] = test[['user_id', 'ts_hour']].apply(listened_user_by_ts_hour_sum, axis=1, raw=True)
    
    #test['ts_hour_genre_accepted_sum'] = test[['user_id', 'ts_hour', 'genre_id']].apply(listened_user_by_ts_hour_genre_sum, axis=1, raw=True)
    #test['ts_hour_media_accepted_sum'] = test[['user_id', 'ts_hour', 'media_id']].apply(listened_user_by_ts_hour_media_sum, axis=1, raw=True)
    #test['ts_hour_album_accepted_sum'] = test[['user_id', 'ts_hour', 'album_id']].apply(listened_user_by_ts_hour_album_sum, axis=1, raw=True)
    #test['ts_hour_context_type_accepted_sum'] = test[['user_id', 'ts_hour', 'context_type']].apply(listened_user_by_ts_hour_context_type_sum, axis=1, raw=True)
    #test['ts_hour_artist_accepted_sum'] = test[['user_id', 'ts_hour', 'artist_id']].apply(listened_user_by_ts_hour_artist_sum, axis=1, raw=True)

    train.to_csv('trainv0.14.csv', index=False)
    test.to_csv('testv0.14.csv', index=False)
    
    
main()
print "Done"
