from setuptools import setup, find_packages

setup(name='powerschool_alchemy',
      version='0.0.14',
      description='This library allows you to interact with a PowerSchool Database with SQLALchemy, a Python ORM',
      url='https://github.com/IronCountySchoolDistrict/powerschool-alchemy',
      author='Iron County School District',
      author_email='data@ironmail.org',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'python-dotenv',
          'SQLAlchemy',
          'cx-oracle',
      ],
      zip_safe=False)
