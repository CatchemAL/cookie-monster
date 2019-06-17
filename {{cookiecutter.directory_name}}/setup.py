from setuptools import setup, find_packages

# Package meta-data.
NAME = '{{cookiecutter.directory_name}}'
DESCRIPTION = 'My short description for my project.'
URL = r'https://github.com/todo'
EMAIL = 'TODO@foobar.com'
AUTHOR = '{{cookiecutter.author}}'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.1'

REQUIRED = [
    # 'requests', 'maya', 'records',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=REQUIRED,  # external packages as dependencies
    entry_points = {
		'console_scripts': [ 
			'{{cookiecutter.directory_name}}main = {{cookiecutter.directory_name}}.__main__:main',
		],
	},
)
