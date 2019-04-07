from setuptools import setup, find_packages

setup(
    name = 'Zeppi_Convert',
    version = '0.1.0',
    description="Convert your zeppelin notebooks to python",
    author="Harsha Karpurapu",
    author_email='kbsriharsha@gmail.com',
    packages = find_packages(exclude=['contrib', 'docs', 'tests']),
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points = {
        'console_scripts': [
            'Zeppi_Convert = Zeppi_Convert.__main__:main'
        ]
    })
