import ctypes

__all__ = ['ControllerThread']


class ControllerThread:
    """Class of thread responsible for handling threads"""

    @staticmethod
    def terminate_thread(thread) -> None:
        """Terminates thread from another thread. 

        :param thread: the thread instance to stop 
        
        :returns: None
        """
        if not thread.isAlive():
            return
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread.ident), exc)
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
