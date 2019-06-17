import {{cookiecutter.directory_name}}
from {{cookiecutter.directory_name}}.{{cookiecutter.file_name}} import hello_world


def test_hello_world():
    hw = hello_world()
    assert hw == 'Hello world!'


def test_hello_author():
    ha = {{cookiecutter.directory_name}}.hello_author()
    assert ha == 'Hello, {{cookiecutter.author}}!'
