from tensorflow.python.client import device_lib
"""Simple tensorflow functionality test"""
def print_devices():
    """prints information about local tensorflow devices"""
    print(device_lib.list_local_devices())
