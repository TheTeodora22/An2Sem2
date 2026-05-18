from sklearn import preprocessing
import numpy as np
from sklearn import svm
from sklearn.metrics import f1_score

training_data = np.load('./data/training_sentences.npy', allow_pickle=True)
training_labels = np.load('./data/training_labels.npy', allow_pickle=True)

testing_data = np.load('./data/test_sentences.npy', allow_pickle=True)
testing_labels = np.load('./data/test_labels.npy', allow_pickle=True)


def normalize_data(train_data, test_data, type=None):
    if type == 'standard':
        scaler = preprocessing.StandardScaler()
        scaler.fit(train_data)
        train_data = scaler.transform(train_data)
        test_data = scaler.transform(test_data)

    if type == 'l1':
        scaler = preprocessing.Normalizer(norm='l1')
        scaler.fit(train_data)
        train_data = scaler.transform(train_data)
        test_data = scaler.transform(test_data)

    if type == 'l2':
        scaler = preprocessing.Normalizer(norm='l2')
        scaler.fit(train_data)
        train_data = scaler.transform(train_data)
        test_data = scaler.transform(test_data)
    return train_data, test_data

class BagOfWords:
    def __init__(self):
        self.dict = {}
        self.wordlist = []


    def build_vocabulary(self, data):
        id = 1
        for sentence in data:
            for word in sentence:
                if word not in self.dict:
                    self.dict[word] = id
                    self.wordlist.append(word)
                    id += 1  

    def get_features(self, data):
        matrix = []
        for sentence in data:
            vector = [0] * (len(self.dict) + 1)
            for word in sentence:
                if word in self.dict:
                    vector[self.dict[word]] += 1
            matrix.append(vector)
        return np.array(matrix)
    
def exercise3():
    bow = BagOfWords()
    bow.build_vocabulary(training_data)
    print("Dimensiunea vocabularului:", len(bow.dict))

def exercise5():
    bow = BagOfWords()
    bow.build_vocabulary(training_data)
    x_train = bow.get_features(training_data)
    x_test = bow.get_features(testing_data)

    x_train, x_test = normalize_data(x_train, x_test, type='l2')

    print(x_train[0])

    print(x_train.shape)
    print(x_test.shape)

def exercise6():
    bow = BagOfWords()
    bow.build_vocabulary(training_data)
    x_train = bow.get_features(training_data)
    x_test = bow.get_features(testing_data)

    x_train, x_test = normalize_data(x_train, x_test, type='standard')

    model = svm.SVC(kernel='linear')
    model.fit(x_train, training_labels)

    accuracy = model.score(x_test, testing_labels)
    print("Acuratetea:", accuracy)

    predictions = model.predict(x_test)
    print(f1_score(testing_labels, predictions, average='binary'))

    coef = model.coef_.ravel()
    word_coef = coef[1 : 1 + len(bow.wordlist)]
    top10_idx = np.argsort(word_coef)[-10:]
    neg10_idx = np.argsort(word_coef)[:10]
    top10_words = [bow.wordlist[i] for i in top10_idx]
    neg10_words = [bow.wordlist[i] for i in neg10_idx]

    print("10 cele mai mari coeficienti (cuvinte):", top10_words)
    print("10 cele mai mici coeficienti (cuvinte):", neg10_words)

exercise3()
exercise5()
exercise6()