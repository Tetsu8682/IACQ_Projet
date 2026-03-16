# test_setup.py
import sys
print(f"Python: {sys.version}")

import serial
print(f"PySerial: {serial.__version__}")

import numpy as np
print(f"NumPy: {np.__version__}")

import matplotlib
print(f"Matplotlib: {matplotlib.__version__}")

import neurokit2 as nk
print(f"NeuroKit2: {nk.__version__}")

print("\n✓ All dependencies installed correctly!")