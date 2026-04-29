import torch
import sys
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

print(f"--- System Info ---")
print(f"Python Version: {sys.version}")
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")

if not torch.cuda.is_available():
    print("\n--- Troubleshooting ---")
    print(f"CUDA Version PyTorch was built with: {torch.version.cuda}")
    print(f"Is NVCC available in PATH? {os.system('nvcc --version') == 0}")
    
    # Check if a GPU is even visible to the OS
    try:
        import subprocess
        nvd = subprocess.check_output(["nvidia-smi"]).decode("utf-8")
        print("\nNVIDIA-SMI Output:")
        print(nvd)
    except:
        print("\nNVIDIA-SMI failed. Driver might not be installed.")
else:
    print(f"Device Name: {torch.cuda.get_device_name(0)}")

    
# --------------------
print("\n============ TensorFlow GPU Status ============")

import tensorflow as tf
import os

print(f"TensorFlow Version: {tf.__version__}")
print(f"Is built with CUDA: {tf.test.is_built_with_cuda()}")
print(f"Device List: {tf.config.list_physical_devices('GPU')}")

# Try to force initialization
try:
    tf.config.experimental.list_physical_devices('GPU')
    print("GPU initialization successful.")
except Exception as e:
    print(f"GPU initialization failed: {e}")

# If using NVIDIA GPU, ensure persistence mode is enabled
# !sudo nvidia-smi -pm 1