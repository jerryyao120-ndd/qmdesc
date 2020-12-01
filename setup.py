import os
import setuptools

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = '''QM descriptor predictions through ChemProp'''

setuptools.setup(
    name="qmdesc", # Replace with your own username
    version="v1.0",
    author="Yanfei Guan",
    author_email="yanfeig@mit.edu",
    description="A qm descriptor prediction package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=[
        'torch>=1.5.1',
        'numpy>=1.18.1',
    ],
    url="https://github.com/yanfeiguan/qmdesc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=[
        'chemistry',
        'machine learning',
        'QM descriptors',
    ]
)