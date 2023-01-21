#@title Прогнозирование предрасположенности к раку лёгкого. { display-mode: "form" }
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import ExtraTreesClassifier


class AI_Help():
    def __init__(self, smoking, il1b, tnf, apex1, xpd, egfr, chek2, tgfb1, ephx1):
       self.df = pd.read_csv("data_rak.csv", delimiter=';').dropna()
       smoking = smoking
       IL1b = il1b
       TNF = tnf
       APEX1 = apex1
       XPD = xpd
       EGFR = egfr
       CHEK2 = chek2
       TGFb1 = tgfb1
       EPHX1 = ephx1

       #prognoz data
       self.predict_df = {"Smoking": [smoking], "IL1b": [IL1b], "TNF": [TNF], "APEX1": [APEX1],
       "XPD": [XPD], "EGFR":[EGFR], "CHEK2":[CHEK2], "TGFb1":[TGFb1], "EPHX1 ":[EPHX1]}
       self.predict_df = pd.DataFrame(self.predict_df)

    def go_train(self, n_jobs = -1,max_depth=5, random_state = 1751, 
    bootstrap = 1, min_samples_split=2, n_estimators=25, 
    min_samples_leaf = 3, max_features='log2'):

        df = self.df
        predict_df = self.predict_df

        #Encoder
        encoder = LabelEncoder()
        for col in predict_df.columns:
            encoder.fit(df[col])
            predict_df[col] = encoder.transform(predict_df[col])
            df[col] = encoder.transform(df[col])

        #Разделение выборки
        y = df['Status'].values
        df = df.drop('Status', axis = 1)
        x = df.values
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state = 2958, stratify=y)

        #Model
        rf = ExtraTreesClassifier(n_jobs = n_jobs,max_depth=max_depth, random_state = random_state, 
        bootstrap = bootstrap, min_samples_split=min_samples_split, n_estimators=n_estimators, 
        min_samples_leaf = min_samples_leaf, max_features=max_features)
        rf.fit(x_train, y_train)
        rf_pred = rf.predict(x_test)
        acc_rf = accuracy_score(y_test, rf_pred)
        predict = rf.predict(predict_df)
        result = [predict, round(acc_rf,3)*100]
        return result




        


