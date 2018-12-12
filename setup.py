from setuptools import setup, find_packages

try:
    from pip._internal import main as pip_main
except:
    from pip import main as pip_main

pip_main(['install', '--upgrade', 'git+https://github.com/ibm-watson-iot/functions.git@'])

setup(
  name='pocfunction',
  version='0.1',
  packages=find_packages(),
  dependency_links=['git+https:github.com/ibm-watson-iot/functions.git@']
  )
