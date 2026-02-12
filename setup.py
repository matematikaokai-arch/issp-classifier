from setuptools import setup

setup(
    name='issp-classifier',
    version='0.1.1',
    packages=['issp_classifier'],
    package_dir={'': '.'},
    install_requires=['numpy>=1.20'],
    author='Andrey Murdasov',
    author_email='[matematikaokai@gmail.com]',
    description='Galaxy classifier based on the Information Self-Sufficiency Principle (ISSP)',
    url='https://github.com/Andrey-Murdasov/issp-classifier',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    license='MIT'
)