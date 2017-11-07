import numpy as np
import pandas as pd
import xgboost as xgb

print("Started")
seed = 1993
np.random.seed(seed)
folder = '../data/'
train = pd.read_csv(folder + 'train.csv')
test = pd.read_csv(folder + 'test.csv')

def run_xgb(train_X, train_y, test_X, test_y=None, feature_names=None, num_rounds=500):
    param = {}
    param['objective'] = 'binary:logistic'
    param['max_depth'] = 5
    param['silent'] = 1
    param['eval_metric'] = "auc"
    param['min_child_weight'] = 1
    param['subsample'] = 0.9
    param['colsample_bytree'] = 0.9
    param['nthreads'] = 3
    param['n_estimators'] = 100
    param['eta'] = 0.1
    param['seed'] = seed
    num_rounds = num_rounds

    plst = list(param.items())
    xgtrain = xgb.DMatrix(train_X, label=train_y)

    if test_y is not None:
        xgtest = xgb.DMatrix(test_X, label=test_y)
        watchlist = [ (xgtrain,'train'), (xgtest, 'test') ]
        model = xgb.train(plst, xgtrain, num_rounds, watchlist, early_stopping_rounds=20)
    else:
        xgtest = xgb.DMatrix(test_X)
        model = xgb.train(plst, xgtrain, num_rounds)

    pred_test_y = model.predict(xgtest)
    return pred_test_y, model

def validation(train):
    return 0

def main():
    features = ['genre_id', 'media_id', 'album_id', 'context_type',
                'media_duration', 'release_date', 'platform_name',
                'platform_family', 'user_age', 
                'listen_type', 'user_gender', 'user_id', 'artist_id', 
                'genre_accepted_ratio', 'genre_accepted_sum',
                'media_accepted_ratio', 'media_accepted_sum', 
                'album_accepted_ratio', 'album_accepted_sum', 
                'context_type_accpeted_ratio', 'context_type_accepted_sum',
                'artist_accepted_ratio', 'artist_accepted_sum',
                'ts_hour_accepted_ratio', 'ts_hour_accepted_sum'
                ]

    #features train
    df_train = train[features]
    #output
    df_train_y = train['is_listened']
    #features test
    df_test = test[features]

    print "Traning XGBoost"
    #predicts, model = run_xgb(x_train, y_train, x_valid, y_valid)
    predicts, model = run_xgb(df_train, df_train_y, df_test)

    submission = pd.DataFrame()
    submission['sample_id'] = test['sample_id']
    submission['is_listened'] = predicts
    submission.to_csv('submission_xgb06.csv', index=False)

main()
print "Done"