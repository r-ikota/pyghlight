from setuptools import setup

setup(name='pyghlight',
      version='0.2.0',
      description="",

      url='https://github.com/r-ikota/',
      py_modules=['pyghlight'],
      author='Ryo Ikota',
      author_email='r.ikota.mt@gmail.com',
      entry_points={
        'console_scripts': [
            'pyghlight=pyghlight:main',
        ],
      },
      license='BSD',
      keywords='syntax highliging'
      )
