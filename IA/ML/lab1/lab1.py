import numpy as np
from skimage import io
import matplotlib.pyplot as plt

images = np.zeros((9,400,600))
for i in range(9):
    images[i] = np.load(f"images/car_{i}.npy")

sums = [np.sum(img) for img in images]

print("B: ")
print (np.sum(sums))

print("C: ")
print(*sums)

print("D: ")
print(np.argmax(sums))

print("E: ")
mean_image = np.mean(images, axis=0)
io.imshow(mean_image.astype(np.uint8))
plt.title("Mean Image")
io.show()

print("F: ")
print(np.std(images, axis=0))

print("G: ")
normalized_images = (images - np.mean(images, axis=0)) / np.std(images, axis=0)
io.imshow(normalized_images[0].astype(np.uint8))
plt.title("Normalized Image")
io.show()


print("H: ")
cropped_images = images[:, 200:300, 280:400]
io.imshow(cropped_images[0].astype(np.uint8))
plt.title("Cropped Image")
io.show()
