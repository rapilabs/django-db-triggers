from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='django-db-triggers',
    version='0.1.0',
    author='shangxiao',
    description='Add database triggers, associated trigger functions and any other function to your database via migrations',
    long_description=readme(),
    url='https://github.com/rapilabs/django-db-triggesr',
    license='MIT',
    packages=find_packages(),
    install_requires=('django',),
)
