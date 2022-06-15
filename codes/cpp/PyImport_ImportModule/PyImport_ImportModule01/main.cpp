#include "Python.h"
#include <iostream>

int main(int argc, char** argv)
{
    Py_Initialize();

    if ( Py_IsInitialized() )
    {
        PyObject* pModule = NULL;
        PyObject* pFunc = NULL;
        PyRun_SimpleString( "import sys" );
        PyRun_SimpleString( "print(sys.path)" );
        PyRun_SimpleString( "sys.path.append( '../' )" );
        PyRun_SimpleString( "print(sys.path)" );
import os
path1 = os.path.abspath('.')
path2 = os.path.abspath('..')
print('path1=',path1)
print('path2=',path2)
        pModule = PyImport_ImportModule("../testprj");
        if ( pModule )
        {
            pFunc = PyObject_GetAttrString(pModule, "hello");
            PyEval_CallObject(pFunc, NULL);
        }
        else
        {
            std::cout << "Failed to import Python module...\n";
        }
    }
    else
    {
        std::cout << "Python environment initialization failed...\n";
    }
    Py_Finalize();
    
    return 0;
}