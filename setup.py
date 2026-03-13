from setuptools import setup, find_namespace_packages, find_packages

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name='TL-MHC',
    version='1.0',
    description="A set of tools that use transfer learning techniques to improve stability and immunogenicity predictions",
    long_description=readme(),
    url='https://github.com/KavrakiLab/TL-MHC',
    author='R. Fasoulis, M. M. Rigo, D. A. Antunes, G. Paliouras, L. E. Kavrak',
    scripts=['tlbind/TLBind.py', 'tlimm/TLImm.py', 'tlstab/TLStab.py'],
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'torch',
        'biopython',
    ],
    zip_safe=False
)
