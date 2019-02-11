from distutils.core import setup, Extension

example_module = Extension('_calc',
                           sources=['calc_wrap.cxx', 'calc.cpp'],
                           )
setup(name='calc',
      version='1.0',
      author='Connor Burns',
      description="""Calculation module for python toplogical computer""",
      ext_modules=[example_module],
      py_modules=["calc"])
