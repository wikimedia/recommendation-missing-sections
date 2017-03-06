from setuptools import setup, find_packages

setup(
    name='recommendation-missing-sections',
    version='0.0.1',
    url='https://github.com/schana/recommendation-missing-sections',
    license='Apache Software License',
    maintainer='Wikimedia Research',
    maintainer_email='nschaaf@wikimedia.org',
    description='Provide missing section recommendations',
    long_description='',
    packages=find_packages(exclude=['test', 'test.*', '*.test']),
    install_requires=['recommendation',
                      'flask',
                      'flask-restplus'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   'responses'])

