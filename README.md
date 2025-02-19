# instalar y activar el entorno virtual
virtualenv env

# requerimientos para Python 10 / CUDA 11.8 CUDNN 8.2.1
pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 torchaudio==2.1.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118

pip install tensorflow==2.10 

# Resultado:
GPUs disponibles (TensorFlow): 1
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
¿CUDA disponible? (PyTorch): True
Número de GPUs: 1
Nombre de la GPU: NVIDIA GeForce RTX xxxx