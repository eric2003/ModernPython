from distutils.core import setup, Extension

module = Extension('Hello',
                    sources = ['Hello.c'])

setup (name = 'OneFLOWPackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module]
)