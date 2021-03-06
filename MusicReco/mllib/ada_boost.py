from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.pipeline import Pipeline

from .base import Base

class ADABoost(Base):

    def train(self, data = None, plugin=None):
        """ With dataframe train mllib """
        super(ADABoost, self).train(data, plugin)

            #cl = svm.SVC(gamma=0.001, C= 100, kernel='linear', probability=True)

        X = self.X_train.iloc[:,:-1]
        Y = self.X_train.iloc[:,-1]

        self.scaler = StandardScaler().fit(X)
        X = self.scaler.transform(X)

        cl = SGDClassifier(loss='hinge')
        p = Pipeline([("Scaler", self.scaler), ("svm", cl)])

        self.clf = BaggingClassifier(p, n_estimators=50)
        #self.clf = AdaBoostClassifier(p, n_estimators=10)
            #self.clf = AdaBoostClassifier(SGDClassifier(loss='hinge'),algorithm='SAMME', n_estimators=10)

        self.clf.fit(X, Y)

    def predict(self, file, plugin=None):
        super(ADABoost, self).predict(file, plugin)

        data = file.vector
        X = data[plugin]
        X = self.scaler.transform(X)
        guess = self.clf.predict(X)
        return self.getTag(guess)
