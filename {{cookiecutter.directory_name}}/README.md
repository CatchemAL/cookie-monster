# Welcome to Cookie Monster!

Cookie monster is a template repository that shows you how to set up a Python project via cookie cutter.


## Installation

To install a project based on Cookie Monster, first navigate to the folder where you want to create your project. Ensure cookie cutter is installed (via pip) and input:

`cookiecutter gh:CatchemAl/cookie-monster`

This project uses the [src](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) layout. In order to debug the tests, you will need to pip install it in editable mode via
`pip install -e .`

To run the package as an application you need to call the package name which will run the \_\_main\_\_.py file. To do this, call 
`
py -m src.package_name
`

In VS Code, this is easily achieved by setting up a debug configuration that calls the module. Cookie Monster does this automatically.