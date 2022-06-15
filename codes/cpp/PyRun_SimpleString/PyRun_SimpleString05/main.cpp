#include "Python.h"
#include <iostream>

int main(int argc, char** argv)
{
    Py_Initialize();
    if ( Py_IsInitialized() )
    {
        PyRun_SimpleString( "import sys" );
        PyRun_SimpleString( "import os" );
        PyRun_SimpleString( "sys.path.append('..')" );
        PyRun_SimpleString( "path1 = os.path.abspath('.')" );
        PyRun_SimpleString( "path2 = os.path.abspath('..')" );
        PyRun_SimpleString( "path3 = os.path.abspath('../..')" );
        PyRun_SimpleString( "print('path1=',path1)" );
        PyRun_SimpleString( "print('path2=',path2)" );
        PyRun_SimpleString( "print('path3=',path3)" );

        PyRun_SimpleString( "import hifile" );
        PyRun_SimpleString( "hi = hifile.hi" );
        PyRun_SimpleString( "hi()" );
    }
    else
    {
        std::cout << "Python environment initialization failed...\n";
    }
    Py_Finalize();
    
    return 0;
}