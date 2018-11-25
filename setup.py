from setuptools import setup

setup(
    name='testsscrappeo',
    version='0.1.0',
    packages=['engien', 'server'],
    url='https://github.com/Jaimeardp/scrapy',
    license='',
    author='Jaime',
    author_email='jaimeardp@gmail.com',
    description='',
    entry_points = {
    'console_scripts': ['server.cli=server.cli:main'],
    }

)
