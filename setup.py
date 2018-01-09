from setuptools import setup

setup(name='powerschool_alchemy',
      version='0.0.1',
      description='This library allows you to interact with a PowerSchool Database with SQLALchemy, a Python ORM',
      url='https://github.com/IronCountySchoolDistrict/powerschool-alchemy',
      author='Iron County School District',
      author_email='data@ironmail.org',
      license='MIT',
      packages=['powerschool_alchemy'],
      install_requires=[
          'python-dotenv',
          'SQLAlchemy',
      ],
      zip_safe=False)
