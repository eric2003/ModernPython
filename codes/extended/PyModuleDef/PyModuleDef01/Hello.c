#include "Python.h"

static PyObject* MyVersion(PyObject* self)
{
    return Py_BuildValue("s", "Version 3.14159");
}

//PyMethodDef is a struct
static PyMethodDef method_list[] = {
    {"MyVersion", (PyCFunction)MyVersion, METH_NOARGS, "return version." },
    {NULL, NULL, 0, NULL}
};

//register module
static struct PyModuleDef Hello = {
    PyModuleDef_HEAD_INIT,
    "Hello",
    NULL,
    -1,
    method_list
};

//initialization
PyMODINIT_FUNC PyInit_Hello(void) {
    return PyModule_Create(&Hello);
}