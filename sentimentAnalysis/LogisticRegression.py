import numpy as np
class LogisticRegression:
    def __init__(self,lr=0.0001,number_itr=1000):
        self.lr=lr
        self.itr=number_itr
        self.weight=None;
        self.bias=None;
    def fit(self,X,y):
        number_sample,number_feature=X.shape
        self.weight=np.zeros(number_feature)
        self.bias=0
#         Gradient desent
        for _ in range(self.itr):
            linearModel=np.dot(X,self.weight)+self.bias
            y_predicted=self.sigmoid(linearModel)
            dw= (1/number_sample)*(np.dot(X.T,(y_predicted-y)))
            db=(1/number_sample)*(y_predicted-y)
            self.weight-=dw*self.lr;
            self.bias-=self.lr*db
        
    def predict(self,X):
        linearModel=np.dot(X,self.weight) + self.bias
        print(self.weight,self.bias)
        y_predict=self.sigmoid(linearModel)
        print(y_predict)
        y_predicted_cls=[1 if i>0.5 else 0 for i in y_predict]
        return y_predict
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))