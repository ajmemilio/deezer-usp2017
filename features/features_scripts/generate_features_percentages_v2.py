#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:32:29 2017

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


listen_type_genre_accepted = train.groupby(['user_id', 'genre_id', 'listen_type']).mean()['is_listened']
dict_listen_type_genre_accepted = dict(listen_type_genre_accepted)
    
def listened_listen_type_genre_accepted(row):
    user = row[0]
    genre = row[1]
    flow = row[2]
    key = (user, genre, flow)
    
    if key not in dict_listen_type_genre_accepted:
        return 0.0
    else:
        return dict_listen_type_genre_accepted[key]

listen_type_media_accepted = train.groupby(['user_id', 'media_id', 'listen_type']).mean()['is_listened']
dict_listen_type_media_accepted = dict(listen_type_media_accepted)

def listened_listen_type_media_accepted(row):
    user = row[0]
    media = row[1]
    flow = row[2]
    key = (user, media, flow)

    if key not in dict_listen_type_media_accepted:
        return 0.0
    else:
        return dict_listen_type_media_accepted[key]
    
listen_type_artist_accepted = train.groupby(['user_id', 'artist_id', 'listen_type']).mean()['is_listened']
dict_listen_type_artist_accepted = dict(listen_type_artist_accepted)

def listened_listen_type_artist_accepted(row):
    user = row[0]
    artist = row[1]
    flow = row[2]
    key = (user, artist, flow)

    if key not in dict_listen_type_artist_accepted:
        return 0.0
    else:
        return dict_listen_type_artist_accepted[key]  

listen_type_hour_accepted = train.groupby(['user_id', 'ts_hour', 'listen_type']).mean()['is_listened']
dict_listen_type_hour_accepted = dict(listen_type_hour_accepted)
    
def listened_listen_type_hour_accepted(row):
    user = row[0]
    hour = row[1]
    flow = row[2]
    key = (user, hour, flow)

    if key not in dict_listen_type_hour_accepted:
        return 0.0
    else:
        return dict_listen_type_hour_accepted[key]  
    
listen_type_album_accepted = train.groupby(['user_id', 'album_id', 'listen_type']).mean()['is_listened']
dict_listen_type_album_accepted = dict(listen_type_album_accepted)
       
def listened_listen_type_album_accepted(row):
    user = row[0]
    album = row[1]
    flow = row[2]
    key = (user, album, flow)

    if key not in dict_listen_type_album_accepted:
        return 0.0
    else:
        return dict_listen_type_album_accepted[key]  

listen_type_context_type_accepted = train.groupby(['user_id', 'context_type', 'listen_type']).mean()['is_listened']
dict_listen_type_context_type_accepted = dict(listen_type_context_type_accepted)

def listened_listen_type_context_type_accepted(row):
    user = row[0]
    context_type = row[1]
    flow = row[2]
    key = (user, context_type, flow)
    
    if key not in dict_listen_type_context_type_accepted:
        return 0.0
    else:
        return dict_listen_type_context_type_accepted[key]  


def main():
    print "Generate features train..."
    train['listen_type_genre_accepted'] = train[['user_id', 'genre_id', 'listen_type']].apply(listened_listen_type_genre_accepted, axis=1, raw=True)
    train['listen_type_artist_accepted'] = train[['user_id', 'artist_id', 'listen_type']].apply(listened_listen_type_artist_accepted, axis=1, raw=True)
    train['listen_type_hour_accepted'] = train[['user_id', 'ts_hour', 'listen_type']].apply(listened_listen_type_hour_accepted, axis=1, raw=True)
    train['listen_type_album_accepted'] = train[['user_id', 'album_id', 'listen_type']].apply(listened_listen_type_album_accepted, axis=1, raw=True)
    train['listen_type_media_accepted'] = train[['user_id', 'media_id', 'listen_type']].apply(listened_listen_type_media_accepted, axis=1, raw=True)
    train['listen_type_context_type_accepted'] = train[['user_id', 'context_type', 'listen_type']].apply(listened_listen_type_context_type_accepted, axis=1, raw=True)
    
    train.to_csv('trainv0.13.csv', index=False)
    
    print "Generate features test..."
    test['listen_type_genre_accepted'] = test[['user_id', 'genre_id', 'listen_type']].apply(listened_listen_type_genre_accepted, axis=1, raw=True)
    test['listen_type_artist_accepted'] = test[['user_id', 'artist_id', 'listen_type']].apply(listened_listen_type_artist_accepted, axis=1, raw=True)
    test['listen_type_hour_accepted'] = test[['user_id', 'ts_hour', 'listen_type']].apply(listened_listen_type_hour_accepted, axis=1, raw=True)
    test['listen_type_album_accepted'] = test[['user_id', 'album_id', 'listen_type']].apply(listened_listen_type_album_accepted, axis=1, raw=True)
    test['listen_type_media_accepted'] = test[['user_id', 'media_id', 'listen_type']].apply(listened_listen_type_media_accepted, axis=1, raw=True)
    test['listen_type_context_type_accepted'] = test[['user_id', 'context_type', 'listen_type']].apply(listened_listen_type_context_type_accepted, axis=1, raw=True)
    
    test.to_csv('testv0.13.csv', index=False)
    
    
main()
print "Done"