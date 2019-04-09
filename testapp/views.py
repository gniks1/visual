
from django.shortcuts import render
#Create views

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from testapp.models import abc
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
def funct(request):
    datas = pd.read_csv('static/titanic.csv')
    #X=data.iloc[:,[2,3]].values
    #y=data.iloc[:,4].values
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    #sc = StandardScaler()
    #X_train = sc.fit_transform(X_train)
    #X_test = sc.transform(X_test)
    #datas =pd.read_csv('titanic.csv')

    X= datas.iloc[:,3].values
    y= datas.iloc[:,-1].values
    for i in range(2):

        if i==0:
            plt.bar(X,y)
            plt.savefig('static/'+str(i)+'.png')


        if i==1:
            plt2.plot(X,y)
            plt2.savefig('static/'+str(i)+'.png')
    #plt.hist(X,y)
    #plt.savefig('static/2.png')

    emp="hello"
    return render(request, 'testapp/results.html',{'h':emp})
