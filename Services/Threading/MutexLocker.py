from PyQt6 import QtCore


class MutexLocker(QtCore.QMutex):
    def __enter__(self):
        self.lock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unlock()

class RecursiveMutexLocker(QtCore.QRecursiveMutex):
    def __enter__(self):
        self.lock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unlock()