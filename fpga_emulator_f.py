from fpga_emulator import Emulator
#problème avec cette librairie à creuser

# Use emulator mode
fpga = IACQ(port=None, emulator=True)
fpga.open()



# Same code works with real hardware
# fpga = IACQ(port='COM3', emulator=False)