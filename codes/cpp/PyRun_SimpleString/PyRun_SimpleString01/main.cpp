#include "Python.h"
#include <iostream>

int main(int argc, char** argv)
{
    Py_Initialize();
    if ( Py_IsInitialized() )
    {
        PyRun_SimpleString( "import os" );
        PyRun_SimpleString( "path1 = os.path.abspath('.')" );
        PyRun_SimpleString( "path2 = os.path.abspath('..')" );
        PyRun_SimpleString( "print('path1=',path1)" );
        PyRun_SimpleString( "print('path2=',path2)" );
    }
    else
    {
        std::cout << "Python environment initialization failed...\n";
    }
    Py_Finalize();
    
    return 0;
}