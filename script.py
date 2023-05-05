import js
from pyodide.ffi import create_proxy


def addTwoNumbers(a, b):
    return a + b


js.createObject(create_proxy(globals()), "pyodideGlobals")
