#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 12:05:35 2017

@author: joao
"""

import numpy as np
import pandas as pd
import sqlite3 as db

print "Started"
RS = 12357
np.random.seed(RS)

folder = '../'
db_folder = 'deezer_db/'

def listened_diff_last_tslisten_train():
    conn = db.connect(db_folder + 'deezer.db')

    listenedDiffLastTslistenTrain = pd.read_sql_query('''
    SELECT   future.sample_id,
             (future.ts_listen - max(past.ts_listen)) as diff_last_tslisten
    FROM     train past, train future 
    WHERE    past.user_id == future.user_id
    AND      past.ts_listen < future.ts_listen
    GROUP BY future.sample_id;
    ''', conn)
    
    return listenedDiffLastTslistenTrain

def listened_diff_last_tslisten_test():
    conn = db.connect(db_folder + 'deezer.db')

    listenedDiffLastTslistenTest = pd.read_sql_query('''
    SELECT   future.sample_id,
             (future.ts_listen-max(past.ts_listen)) as diff_last_tslisten
    FROM     train past, test future 
    WHERE    past.user_id == future.user_id
    AND      past.ts_listen < future.ts_listen
    GROUP BY future.sample_id;
    ''', conn)
    
    return listenedDiffLastTslistenTest

def listened_120minutes_train():
    conn = db.connect(db_folder + 'deezer.db')
    listened120MinutesTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             COUNT(futuro.constant) AS sum_musics120_listened,
             AVG(passado.is_listened) AS perc_musics120_listened
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.ts_listen + 7200 > futuro.ts_listen
    AND      passado.ts_listen        < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened120MinutesTrain = listened120MinutesTrain.drop('user_id', axis=1)
    
    return listened120MinutesTrain

def listened_120minutes_test():
    conn = db.connect(db_folder + 'deezer.db')
    listened120MinutesTest = pd.read_sql_query('''
    SELECT futuro.sample_id,
           futuro.user_id,
           COUNT(futuro.constant) as sum_musics120_listened,
           AVG(passado.is_listened) as perc_musics120_listened
           FROM train passado, test futuro
           WHERE       passado.user_id == futuro.user_id
           AND     passado.ts_listen + 7200 > futuro.ts_listen
           AND     passado.ts_listen        < futuro.ts_listen
           GROUP BY futuro.sample_id;  
    ''', conn)

    listened120MinutesTest = listened120MinutesTest.drop('user_id', axis=1)
    
    return listened120MinutesTest

def listened_120minutes_by_media_train():
    conn = db.connect(db_folder + 'deezer.db')

    listened120MinutesByMediaTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             futuro.media_id,
             COUNT(futuro.constant) AS sum_musics120_listened_by_media,
             AVG(passado.is_listened) AS perc_musics120_listened_by_media
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.media_id == futuro.media_id
    AND      passado.ts_listen + 7200 > futuro.ts_listen
    AND      passado.ts_listen        < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened120MinutesByMediaTrain = listened120MinutesByMediaTrain[['sample_id', 'sum_musics120_listened_by_media', 'perc_musics120_listened_by_media']]
    
    return listened120MinutesByMediaTrain

def listened_120minutes_by_media_test():
    conn = db.connect(db_folder + 'deezer.db')

    listened120MinutesByMediaTest = pd.read_sql_query('''
    SELECT futuro.sample_id,
           futuro.user_id,
           futuro.media_id,
           COUNT(futuro.constant) as sum_musics120_listened_by_media,
           AVG(passado.is_listened) as perc_musics120_listened_by_media
           FROM     train passado, test futuro
           WHERE    passado.user_id == futuro.user_id
           AND      passado.media_id == futuro.media_id
           AND      passado.ts_listen + 7200 > futuro.ts_listen
           AND      passado.ts_listen        < futuro.ts_listen
           GROUP BY futuro.sample_id;
    ''', conn)

    listened120MinutesByMediaTest = listened120MinutesByMediaTest[['sample_id', 'sum_musics120_listened_by_media', 'perc_musics120_listened_by_media']]
    
    return listened120MinutesByMediaTest

def listened_120minutes_by_artist_train():
    return 0.0

def listened_120minutes_by_genre_train():
    return 0.0

def listened_120minutes_by_album_train():
    return 0.0

def listened_60minutes_train():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened60MinutesTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             COUNT(futuro.constant) AS sum_musics60_listened,
             AVG(passado.is_listened) AS perc_musics60_listened
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.ts_listen + 3600 > futuro.ts_listen
    AND      passado.ts_listen        < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened60MinutesTrain = listened60MinutesTrain.drop('user_id', axis=1)
    
    return listened60MinutesTrain

def listened_60minutes_test():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened60MinutesTest = pd.read_sql_query('''
    SELECT futuro.sample_id,
           futuro.user_id,
           COUNT(futuro.constant) as sum_musics60_listened,
           AVG(passado.is_listened) as perc_musics60_listened
           FROM train passado, test futuro
           WHERE       passado.user_id == futuro.user_id
           AND     passado.ts_listen + 3600 > futuro.ts_listen
           AND     passado.ts_listen        < futuro.ts_listen
           GROUP BY futuro.sample_id;  
    ''', conn)

    listened60MinutesTest = listened60MinutesTest.drop('user_id', axis=1)
    
    return listened60MinutesTest

def listened_30minutes_train():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened30MinutesTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             COUNT(futuro.constant) AS sum_musics30_listened,
             AVG(passado.is_listened) AS perc_musics30_listened
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.ts_listen + 1800 > futuro.ts_listen
    AND      passado.ts_listen        < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened30MinutesTrain = listened30MinutesTrain.drop('user_id', axis=1)
    
    return listened30MinutesTrain

def listened_30minutes_test():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened30MinutesTest = pd.read_sql_query('''
    SELECT futuro.sample_id,
           futuro.user_id,
           COUNT(futuro.constant) as sum_musics30_listened,
           AVG(passado.is_listened) as perc_musics30_listened
           FROM train passado, test futuro
           WHERE       passado.user_id == futuro.user_id
           AND     passado.ts_listen + 1800 > futuro.ts_listen
           AND     passado.ts_listen        < futuro.ts_listen
           GROUP BY futuro.sample_id;  
    ''', conn)
    
    listened30MinutesTest = listened30MinutesTest.drop('user_id', axis=1)
    
    return listened30MinutesTest

def listened_30minutes_by_media_train():
    conn = db.connect(db_folder + 'deezer.db')

    listened30MinutesByMediaTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             futuro.media_id,
             COUNT(futuro.constant) AS sum_musics30_listened_by_media,
             AVG(passado.is_listened) AS perc_musics30_listened_by_media
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.media_id == futuro.media_id
    AND      passado.ts_listen + 1800 > futuro.ts_listen
    AND      passado.ts_listen        < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened30MinutesByMediaTrain = listened30MinutesByMediaTrain[['sample_id', 'sum_musics30_listened_by_media', 'perc_musics30_listened_by_media']]
    
    return listened30MinutesByMediaTrain

def listened_30minutes_by_media_test():
    conn = db.connect(db_folder + 'deezer.db')

    listened30MinutesByMediaTest = pd.read_sql_query('''
    SELECT futuro.sample_id,
           futuro.user_id,
           futuro.media_id,
           COUNT(futuro.constant) as sum_musics30_listened_by_media,
           AVG(passado.is_listened) as perc_musics30_listened_by_media
           FROM     train passado, test futuro
           WHERE    passado.user_id == futuro.user_id
           AND      passado.media_id == futuro.media_id
           AND      passado.ts_listen + 1800 > futuro.ts_listen
           AND      passado.ts_listen        < futuro.ts_listen
           GROUP BY futuro.sample_id;
    ''', conn)

    listened30MinutesByMediaTest = listened30MinutesByMediaTest[['sample_id', 'sum_musics30_listened_by_media', 'perc_musics30_listened_by_media']]
    
    return listened30MinutesByMediaTest

def listened_10minutes_train():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened10MinutesTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             COUNT(futuro.constant) AS sum_musics10_listened,
             AVG(passado.is_listened) AS perc_musics10_listened
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.ts_listen + 600 > futuro.ts_listen
    AND      passado.ts_listen       < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened10MinutesTrain = listened10MinutesTrain.drop('user_id', axis=1)
    
    return listened10MinutesTrain

def listened_10minutes_test():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened10MinutesTest = pd.read_sql_query('''
    SELECT futuro.sample_id,
           futuro.user_id,
           COUNT(futuro.constant) as sum_musics10_listened,
           AVG(passado.is_listened) as perc_musics10_listened
           FROM train passado, test futuro
           WHERE       passado.user_id == futuro.user_id
           AND     passado.ts_listen + 600 > futuro.ts_listen
           AND     passado.ts_listen        < futuro.ts_listen
           GROUP BY futuro.sample_id;  
    ''', conn)
    
    listened10MinutesTest = listened10MinutesTest.drop('user_id', axis=1)
    
    return listened10MinutesTest

def listened_5minutes_train():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened5MinutesTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             COUNT(futuro.constant) AS sum_musics5_listened,
             AVG(passado.is_listened) AS perc_musics5_listened
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.ts_listen + 300 > futuro.ts_listen
    AND      passado.ts_listen       < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened5MinutesTrain = listened5MinutesTrain.drop('user_id', axis=1)
    
    return listened5MinutesTrain

def listened_5minutes_test():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened5MinutesTest = pd.read_sql_query('''
    SELECT futuro.sample_id,
           futuro.user_id,
           COUNT(futuro.constant) as sum_musics5_listened,
           AVG(passado.is_listened) as perc_musics5_listened
           FROM train passado, test futuro
           WHERE       passado.user_id == futuro.user_id
           AND     passado.ts_listen + 300 > futuro.ts_listen
           AND     passado.ts_listen        < futuro.ts_listen
           GROUP BY futuro.sample_id;  
    ''', conn)
    
    listened5MinutesTest = listened5MinutesTest.drop('user_id', axis=1)
    
    return listened5MinutesTest

def listened_1minutes_train():
    conn = db.connect(db_folder + 'deezer.db')
    
    listened1MinutesTrain = pd.read_sql_query('''
    SELECT   futuro.sample_id,
             futuro.user_id,
             COUNT(futuro.constant) AS sum_musics1_listened,
             AVG(passado.is_listened) AS perc_musics1_listened
    FROM     train passado,
             train futuro
    WHERE    passado.user_id == futuro.user_id
    AND      passado.ts_listen + 60 > futuro.ts_listen
    AND      passado.ts_listen      < futuro.ts_listen
    GROUP BY futuro.sample_id;  
    ''', conn)

    listened1MinutesTrain = listened1MinutesTrain.drop('user_id', axis=1)
    
    return listened1MinutesTrain

def main():
    conn = db.connect(db_folder + 'deezer.db')
    
    train = pd.read_sql_query('''
    SELECT * FROM train as t ORDER BY t.sample_id ASC
    ''', conn)
    
    test = pd.read_sql_query('''
    SELECT * FROM test as t ORDER BY t.sample_id ASC
    ''', conn)
    
    
    listened120MinutesTrain = listened_120minutes_train()
    train = pd.merge(train, listened120MinutesTrain, on='sample_id', how='left')
    del listened120MinutesTrain
    
    listened120MinutesByMediaTrain = listened_120minutes_by_media_train()
    train = pd.merge(train, listened120MinutesByMediaTrain, on='sample_id', how='left')
    del listened120MinutesByMediaTrain
    
    listened60MinutesTrain = listened_60minutes_train()
    train = pd.merge(train, listened60MinutesTrain, on='sample_id', how='left')
    del listened60MinutesTrain
    
    listened30MinutesTrain = listened_30minutes_train()
    train = pd.merge(train, listened30MinutesTrain, on='sample_id', how='left')
    del listened30MinutesTrain
    
    listened30MinutesByMediaTrain = listened_30minutes_by_media_train()
    train = pd.merge(train, listened30MinutesByMediaTrain, on='sample_id', how='left')
    del listened30MinutesByMediaTrain
    
    listened10MinutesTrain = listened_10minutes_train()
    train = pd.merge(train, listened10MinutesTrain, on='sample_id', how='left')
    del listened10MinutesTrain
    
    listened5MinutesTrain = listened_5minutes_train()
    train = pd.merge(train, listened5MinutesTrain, on='sample_id', how='left')
    del listened5MinutesTrain
    
    listenedDiffLastTslistenTrain = listened_diff_last_tslisten_train()
    train = pd.merge(train, listenedDiffLastTslistenTrain, on='sample_id', how='left')
    del listenedDiffLastTslistenTrain
    
    train.to_csv('trainv0.15.csv', index=False)
    
    listened120MinutesTest = listened_120minutes_test()
    test = pd.merge(test, listened120MinutesTest, on='sample_id', how='left')
    del listened120MinutesTest
    
    listened120MinutesByMediaTest = listened_120minutes_by_media_test()
    test = pd.merge(test, listened120MinutesByMediaTest, on='sample_id', how='left')
    del listened120MinutesByMediaTest
    
    listened60MinutesTest = listened_60minutes_test()
    test = pd.merge(test, listened60MinutesTest, on='sample_id', how='left')
    del listened60MinutesTest
    
    listened30MinutesTest = listened_30minutes_test()
    test = pd.merge(test, listened30MinutesTest, on='sample_id', how='left')
    del listened30MinutesTest
    
    listened30MinutesByMediaTest = listened_30minutes_by_media_test()
    test = pd.merge(test, listened30MinutesByMediaTest, on='sample_id', how='left')
    del listened30MinutesByMediaTest
    
    listened10MinutesTest = listened_10minutes_test()
    test = pd.merge(test, listened10MinutesTest, on='sample_id', how='left')
    del listened10MinutesTest
    
    listened5MinutesTest = listened_5minutes_test()
    test = pd.merge(test, listened5MinutesTest, on='sample_id', how='left')
    del listened5MinutesTest
    
    listenedDiffLastTslistenTest = listened_diff_last_tslisten_test()
    test = pd.merge(test, listenedDiffLastTslistenTest, on='sample_id', how='left')
    del listenedDiffLastTslistenTest
    
    test.to_csv('testv0.15.csv', index=False)
main()
print "Done"