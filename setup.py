from setuptools import setup

setup(name='nec_beamer',
      version='0.1',
      description='NEC Beamer Web Interface Wrapper',
      url='http://github.com/heinrich-foto/nec_beamer',
      author='Heinrich-Foto',
      author_email='nec_beamer@heinrich-foto.de',
      license='MIT',
      packages=['nec_beamer'],
      zip_safe=False,
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      )