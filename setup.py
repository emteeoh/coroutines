from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='coroutines',
    version='0.1.4',
    packages=[ 'coroutines'],
    url='https://github.com/emteeoh/coroutines',
    license='AGPL',
    author='Richard Betel',
    author_email='emteeoh@gmail.com',
    description='A set of generic coroutines for doing things with pipelines.',
    long_description=long_description,
    long_description_content_type="text/markdown"
)

'''
run python setup.py sdist upload to send this module to pypi. Don't forget to update version first!
'''
