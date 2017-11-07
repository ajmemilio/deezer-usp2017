#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:51:07 2017

@author: joao
"""

import numpy as np
import pandas as pd

print("Started")
RS = 12357
np.random.seed(RS)
folder = '../'
train = pd.read_csv(folder + 'train.csv')
test = pd.read_csv(folder + 'test.csv')

genre_accepted = train.groupby(['user_id', 'genre_id']).mean()['is_listened']
dict_genre_accepted = dict(genre_accepted)

def listened_user_by_genre(row):
    user = row[0]
    genre = row[1]
    key = (user, genre)
    
    if key not in dict_genre_accepted:
        return None
    else:
        return dict_genre_accepted[key]

media_accepted = train.groupby(['user_id', 'media_id']).mean()['is_listened']
dict_media_accepted = dict(media_accepted)

def listened_user_by_media(row):
    user = row[0]
    media = row[1]
    key = (user, media)
    
    if key not in dict_media_accepted:
        return None
    else:
        return dict_media_accepted[key]

album_accepted = train.groupby(['user_id', 'album_id']).mean()['is_listened']
dict_album_accepted = dict(album_accepted)
    

def listened_user_by_album(row):
    user = row[0]
    album = row[1]
    key = (user, album)
    
    if key not in dict_album_accepted:
        return None
    else:
        return dict_album_accepted[key]

context_type_accpeted = train.groupby(['user_id', 'context_type']).mean()['is_listened']
dict_context_type_accpeted = dict(context_type_accpeted)

def listened_user_by_context_type(row):
    user = row[0]
    context_type = row[1]
    key = (user, context_type)
    
    if key not in dict_context_type_accpeted:
        return None
    else:
        return dict_context_type_accpeted[key]

artist_accepted  = train.groupby(['user_id', 'artist_id']).mean()['is_listened']
dict_artist_accepted = dict(artist_accepted)    

def listened_user_by_artist(row):
    user = row[0]
    artist = row[1]
    key = (user, artist)

    if key not in dict_artist_accepted:
        return None
    else:
        return dict_artist_accepted[key]

ts_hour_accepted  = train.groupby(['user_id', 'ts_hour']).mean()['is_listened']
dict_ts_hour_accepted = dict(ts_hour_accepted)    

def listened_user_by_ts_hour(row):
    user = row[0]
    hour = row[1]
    key = (user, hour)

    if key not in dict_ts_hour_accepted:
        return None
    else:
        return dict_ts_hour_accepted[key]

ts_hour_artist_accepted  = train.groupby(['user_id', 'ts_hour', 'artist_id']).mean()['is_listened']
dict_ts_hour_artist_accepted = dict(ts_hour_artist_accepted)    
"""
def listened_user_by_ts_hour_artist(row):
    user = row[0]
    hour = row[1]
    artist = row[2]
    key = (user, hour, artist)

    if key not in dict_ts_hour_artist_accepted:
        return None
    else:
        return dict_ts_hour_artist_accepted[key]

ts_hour_media_accepted  = train.groupby(['user_id', 'ts_hour', 'media_id']).mean()['is_listened']
dict_ts_hour_media_accepted = dict(ts_hour_media_accepted)    

def listened_user_by_ts_hour_media(row):
    user = row[0]
    hour = row[1]
    media = row[2]
    key = (user, hour, media)

    if key not in dict_ts_hour_media_accepted:
        return None
    else:
        return dict_ts_hour_media_accepted[key]

ts_hour_album_accepted  = train.groupby(['user_id', 'ts_hour', 'album_id']).mean()['is_listened']
dict_ts_hour_album_accepted = dict(ts_hour_album_accepted)    

def listened_user_by_ts_hour_album(row):
    user = row[0]
    hour = row[1]
    album = row[2]
    key = (user, hour, album)

    if key not in dict_ts_hour_album_accepted:
        return None
    else:
        return dict_ts_hour_album_accepted[key]

ts_hour_genre_accepted  = train.groupby(['user_id', 'ts_hour', 'genre_id']).mean()['is_listened']
dict_ts_hour_genre_accepted = dict(ts_hour_genre_accepted)    

def listened_user_by_ts_hour_genre(row):
    user = row[0]
    hour = row[1]
    genre = row[2]
    key = (user, hour, genre)

    if key not in dict_ts_hour_genre_accepted:
        return None
    else:
        return dict_ts_hour_genre_accepted[key]

ts_hour_context_type_accepted  = train.groupby(['user_id', 'ts_hour', 'context_type']).mean()['is_listened']
dict_ts_hour_context_type_accepted = dict(ts_hour_context_type_accepted)    

def listened_user_by_ts_hour_context_type(row):
    user = row[0]
    hour = row[1]
    context_type = row[2]
    key = (user, hour, context_type)

    if key not in dict_ts_hour_context_type_accepted:
        return None
    else:
        return dict_ts_hour_context_type_accepted[key]

"""
def main():
    print "Generate features train..."
    train['genre_accepted_ratio'] = train[['user_id', 'genre_id']].apply(listened_user_by_genre, axis=1, raw=True)
    train['media_accepted_ratio'] = train[['user_id', 'media_id']].apply(listened_user_by_media, axis=1, raw=True)
    train['album_accepted_ratio'] = train[['user_id', 'album_id']].apply(listened_user_by_album, axis=1, raw=True)
    train['context_type_accpeted_ratio'] = train[['user_id', 'context_type']].apply(listened_user_by_context_type, axis=1, raw=True)
    train['artist_accepted_ratio'] = train[['user_id', 'artist_id']].apply(listened_user_by_artist, axis=1, raw=True)
    train['ts_hour_accepted_ratio'] = train[['user_id', 'ts_hour']].apply(listened_user_by_ts_hour, axis=1, raw=True)

    #train['ts_hour_genre_accepted_ratio'] = train[['user_id', 'ts_hour', 'genre_id']].apply(listened_user_by_ts_hour_genre, axis=1, raw=True)
    #train['ts_hour_media_accepted_ratio'] = train[['user_id', 'ts_hour', 'media_id']].apply(listened_user_by_ts_hour_media, axis=1, raw=True)
    #train['ts_hour_album_accepted_ratio'] = train[['user_id', 'ts_hour', 'album_id']].apply(listened_user_by_ts_hour_album, axis=1, raw=True)
    #train['ts_hour_context_type_accepted_ratio'] = train[['user_id', 'ts_hour', 'context_type']].apply(listened_user_by_ts_hour_context_type, axis=1, raw=True)
    #train['ts_hour_artist_accepted_ratio'] = train[['user_id', 'ts_hour', 'artist_id']].apply(listened_user_by_ts_hour_artist, axis=1, raw=True)
    
    print "Generate features test..."
    test['genre_accepted_ratio'] = test[['user_id', 'genre_id']].apply(listened_user_by_genre, axis=1, raw=True)
    test['media_accepted_ratio'] = test[['user_id', 'media_id']].apply(listened_user_by_media, axis=1, raw=True)
    test['album_accepted_ratio'] = test[['user_id', 'album_id']].apply(listened_user_by_album, axis=1, raw=True)
    test['context_type_accpeted_ratio'] = test[['user_id', 'context_type']].apply(listened_user_by_context_type, axis=1, raw=True)
    test['artist_accepted_ratio'] = test[['user_id', 'artist_id']].apply(listened_user_by_artist, axis=1, raw=True)
    test['ts_hour_accepted_ratio'] = test[['user_id', 'ts_hour']].apply(listened_user_by_ts_hour, axis=1, raw=True)

    #test['ts_hour_genre_accepted_ratio'] = test[['user_id', 'ts_hour', 'genre_id']].apply(listened_user_by_ts_hour_genre, axis=1, raw=True)
    #test['ts_hour_media_accepted_ratio'] = test[['user_id', 'ts_hour', 'media_id']].apply(listened_user_by_ts_hour_media, axis=1, raw=True)
    #test['ts_hour_album_accepted_ratio'] = test[['user_id', 'ts_hour', 'album_id']].apply(listened_user_by_ts_hour_album, axis=1, raw=True)
    #test['ts_hour_context_type_accepted_ratio'] = test[['user_id', 'ts_hour', 'context_type']].apply(listened_user_by_ts_hour_context_type, axis=1, raw=True)
    #test['ts_hour_artist_accepted_ratio'] = test[['user_id', 'ts_hour', 'artist_id']].apply(listened_user_by_ts_hour_artist, axis=1, raw=True)

    train.to_csv('trainv0.123.csv', index=False)
    test.to_csv('testv0.123.csv', index=False)
    
    
main()
print "Done"