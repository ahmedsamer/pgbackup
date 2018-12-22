from setuptools import setup, find_packages

with open('README.rst', encoding='UTF8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.1',
    description='Database backups locally or to AWS s3',
    long_description=readme,
    author='Ahmed Samir',
    author_email='ahmed.samer@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
