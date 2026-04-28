from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB


train_images = np.loadtxt('data/train_images.txt')
train_labels = np.loadtxt('data/train_labels.txt', 'int')
test_images = np.loadtxt('data/test_images.txt')
test_labels = np.loadtxt('data/test_labels.txt', 'int')


def ex1(data):
    c = len(data)
    fete = 0 
    baie = 0
    fx = 0
    bx = 0
    for h, g in data:
        if g == 'F':
            fete += 1
            if 171 <= h <= 180:
                fx += 1
        elif g == 'B':
            baie += 1
            if 171 <= h <= 180:
                bx += 1
    pf = fete / c
    pb = baie / c

    phf = fx / fete
    phb = bx / baie
    ph = (fx+bx) / c
    
    bayf = (phf * pf) / ph
    bayb = (phb * pb) / ph

    return bayf, bayb

def values_to_bins(matrix, capete):
        return np.digitize(matrix, capete) - 1

def ex2(train_img, train_lbl, test_img, num_bins):
    bins = np.linspace(start=0, stop=255, num=num_bins)
    
    train_images_bins = values_to_bins(train_img, bins)
    test_images_bins = values_to_bins(test_img, bins)


    naive_bayes_model = MultinomialNB()
    naive_bayes_model.fit(train_images_bins, train_lbl)
    
    return naive_bayes_model, train_images_bins, test_images_bins

def ex3(train_img, train_lbl, test_img, test_lbl, num_bins):
    naive_bayes_model, train_images_bins, test_images_bins = ex2(train_img, train_lbl, test_img, num_bins)
    acuratete = naive_bayes_model.score(test_images_bins, test_lbl)

    return acuratete

def ex5(train_img, train_lbl, test_img, test_lbl, num_bins):
    naive_bayes_model, train_images_bins, test_images_bins = ex2(train_img, train_lbl, test_img, num_bins)
    prediction = naive_bayes_model.predict(test_images_bins)
    misclasate = (prediction != test_lbl)
    count = 10
    for i in range(len(misclasate)):
        if misclasate[i]:
            image = test_images[i, :] 
            image = np.reshape(image, (28, 28))
            plt.imshow(image.astype(np.uint8), cmap='gray')
            plt.show()
            print(f"Am afisat imaginea cu indexul {i}")
            count -= 1
        if count == 0:
            break
    

def confusion_matrix(y_true, y_pred):
    n = max(np.max(y_true), np.max(y_pred)) + 1
    matrix = np.zeros((n, n), dtype=int)
    for i in range(len(y_true)):
        matrix[y_true[i], y_pred[i]] += 1
    return matrix

def ex6(train_img, train_lbl, test_img, test_lbl, num_bins):
    naive_bayes_model, _, test_images_bins = ex2(train_img, train_lbl, test_img, num_bins)
    prediction = naive_bayes_model.predict(test_images_bins)
    conf_matrix = confusion_matrix(test_lbl, prediction)
    print("Matricea de confuzie:")
    print(conf_matrix)

print("Exercitiul 1")
date_ex1 = [(160, 'F'), (165, 'F'), (155, 'F'), (172, 'F'), (175, 'B'), (180, 'B'), (177, 'B'), (190, 'B')]
pf, pb = ex1(date_ex1)
print(f"Probabilitatea sa fie fata: {pf}")
print(f"Probabilitatea sa fie baiat: {pb}\n")


print("Exercitiul 2")

naive_bayes_model, train_bins, test_bins = ex2(train_images, train_labels, test_images, 8)

print(naive_bayes_model)

print("\nExercitiul 3")

acuratete5 = ex3(train_images,train_labels, test_images, test_labels, 5)
print(f"Acuratetea pt 5 sub-intervale: {acuratete5 *100:.2f}%")

acuratete4 = ex3(train_images,train_labels, test_images, test_labels, 4)
print(f"Acuratetea pt 4 sub-intervale: {acuratete4 *100:.2f}%")

print("\nExercitiul 4")

num_bins = [3,5,7,9,11]

for n in num_bins:
    print(f"Pentru {n} sub-intervale: {ex3(train_images, train_labels, test_images, test_labels, n) * 100:.2f}%")

print("\nExercitiul 5")

bins = 7
ex5(train_images, train_labels, test_images, test_labels, bins)

print("\nExercitiul 6")


ex6(train_images, train_labels, test_images, test_labels, 5)

