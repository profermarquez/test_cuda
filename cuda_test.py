import tensorflow as tf

# Verifica si TensorFlow puede acceder a la GPU
print("GPUs disponibles (TensorFlow):", len(tf.config.list_physical_devices('GPU')))
print(tf.config.list_physical_devices('GPU'))

import torch

# Verifica si CUDA está disponible
print("¿CUDA disponible? (PyTorch):", torch.cuda.is_available())

# Verifica cuántas GPUs tienes
print("Número de GPUs:", torch.cuda.device_count())

# Verifica el nombre de la GPU
if torch.cuda.is_available():
    print("Nombre de la GPU:", torch.cuda.get_device_name(0))
