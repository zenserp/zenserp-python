try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='zenserp',
    version='0.1',
    packages=['zenserp'],
    url='https://github.com/zenserp/zenserp-python',
    license='MIT',
    author='zenserp',
    author_email='office@zenserp.com',
    description='Zenserp Python Client',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "requests"
    ]
)
