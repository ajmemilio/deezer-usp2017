#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:45:39 2017

@author: joao
"""

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

train = pd.read_csv(folder + 'train.csv', nrows=1000000)
test = pd.read_csv(folder + 'test.csv')

is_create_table_train = True
is_insert_data_train = True

is_create_table_test = True
is_insert_data_test = True

is_create_indexes = True

def create_table_train():
    conn = db.connect('deezer.db')
    c = conn.cursor()
    
    c.execute('''
    CREATE TABLE train (
            sample_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            genre_id INTEGER NOT NULL,
            ts_listen DATETIME NOT NULL,
            media_id INTEGER NOT NULL,
            album_id INTEGER NOT NULL,
            context_type INTEGER NOT NULL,
            release_date INTEGER NOT NULL,
            platform_name INTEGER NOT NULL,
            platform_family INTEGER NOT NULL,
            media_duration INTEGER NOT NULL,
            listen_type TINYINT NOT NULL,
            user_gender TINYINT NOT NULL,
            artist_id INTEGER NOT NULL,
            user_age INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            constant INTEGER NOT NULL,
            is_listened TINYINT NOT NULL
    );
    ''')
    
    conn.close()
    
def create_table_test():
    conn = db.connect('deezer.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE test (
            sample_id INTEGER PRIMARY KEY NOT NULL,
            genre_id INTEGER NOT NULL,
            ts_listen DATETIME NOT NULL,
            media_id INTEGER NOT NULL,
            album_id INTEGER NOT NULL,
            context_type INTEGER NOT NULL,
            release_date INTEGER NOT NULL,
            platform_name INTEGER NOT NULL,
            platform_family INTEGER NOT NULL,
            media_duration INTEGER NOT NULL,
            listen_type TINYINT NOT NULL,
            user_gender TINYINT NOT NULL,
            artist_id INTEGER NOT NULL,
            user_age INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            constant INTEGER NOT NULL
    );
    ''')
    
    conn.close()
    
def insert_data_train():
    conn = db.connect('deezer.db')
    c = conn.cursor()
    
    train['constant'] = np.repeat(1, train.shape[0])
    
    c.executemany('''
    INSERT INTO train (
            genre_id,
            ts_listen,
            media_id,
            album_id,
            context_type,
            release_date,
            platform_name,
            platform_family,
            media_duration,
            listen_type,
            user_gender,
            user_id,
            artist_id,
            user_age,
            constant,
            is_listened
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
    list(train[[
            'genre_id', 
            'ts_listen', 
            'media_id', 
            'album_id', 
            'context_type', 
            'release_date', 
            'platform_name', 
            'platform_family', 
            'media_duration', 
            'listen_type', 
            'user_gender',
            'user_id', 
            'artist_id', 
            'user_age',
            'constant',
            'is_listened'
    ]].to_records(index=False)))
    
    conn.commit()
    conn.close()
    
def insert_data_test():
    conn = db.connect('deezer.db')
    c = conn.cursor()
    
    test['constant'] = np.repeat(1, test.shape[0])
    
    c.executemany('''
    INSERT INTO test (
            sample_id,
            genre_id,
            ts_listen,
            media_id,
            album_id,
            context_type,
            release_date,
            platform_name,
            platform_family,
            media_duration,
            listen_type,
            user_gender,
            user_id,
            artist_id,
            user_age,
            constant
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
    list(test[[
            'sample_id',
            'genre_id', 
            'ts_listen', 
            'media_id', 
            'album_id', 
            'context_type', 
            'release_date', 
            'platform_name', 
            'platform_family', 
            'media_duration', 
            'listen_type', 
            'user_gender',
            'user_id', 
            'artist_id', 
            'user_age',
            'constant'
    ]].to_records(index=False)))
    
    conn.commit()
    conn.close()    

def create_indexes():
    conn = db.connect('deezer.db')
    c = conn.cursor()
    
    c.execute('CREATE INDEX index_userid_tslisten_train on train(user_id, ts_listen);')
    c.execute('CREATE INDEX index_userid_sampleid_train on train(user_id, sample_id)')
    c.execute('CREATE INDEX index_sampleid_userid_train on train(sample_id,user_id)')
    c.execute('CREATE INDEX index_userid_islistened_train on train(user_id, is_listened);')
    c.execute('CREATE INDEX index_userid_mediaid_islistened_train on train(user_id, media_id, is_listened);')
    c.execute('CREATE INDEX index_userid_artistid_islistened_train on train(user_id, artist_id, is_listened);')
    c.execute('CREATE INDEX index_userid_albumid_islistened_train on train(user_id, album_id, is_listened);')
    c.execute('CREATE INDEX index_userid_genreid_islistened_train on train(user_id, genre_id, is_listened);')
    
    c.execute('CREATE INDEX index_userid_tslisten_test on test(user_id, ts_listen);')
    c.execute('CREATE INDEX index_userid_mediaid_tslisten_test on test(user_id, media_id, ts_listen);')
    c.execute('CREATE INDEX index_userid_artistid_islistened_test on test(user_id, artist_id);')
    c.execute('CREATE INDEX index_userid_albumid_islistened_test on test(user_id, album_id);')
    c.execute('CREATE INDEX index_userid_genreid_islistened_test on test(user_id, genre_id);')
    
    conn.commit()
    conn.close()

def main():
    if is_create_table_train:
        print "Create table train"
        create_table_train()
        
    if is_create_table_test:
        print "Create table test"
        create_table_test()
    
    if is_insert_data_train:
        print "Insert data train"
        insert_data_train()
        
    if is_insert_data_test:
        print "Insert data test"
        insert_data_test()    
        
    if is_create_indexes:
        print "Create indexes"
        create_indexes()
    
main()
print "Done"