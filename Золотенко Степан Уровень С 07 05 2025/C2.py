import numpy as np
from skimage import io, transform
import matplotlib.pyplot as plt

image = io.imread('volga.jpg')

output_shape = (image.shape[0] // 2, image.shape[1] // 2)


resized_image = transform.resize(image, output_shape, anti_aliasing=True)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image)
axes[0].set_title('Original Image with shape '+str(image.shape))

axes[1].imshow(resized_image)
axes[1].set_title('Resized Image with shape '+str(resized_image.shape))

plt.tight_layout()
plt.show()
