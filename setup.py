from setuptools import setup, find_packages
from auth0_sso.version import Version


setup(name='auth0_sso',
     version=Version('1.0.0').number,
     description='Auth0 SSO for Django',
     long_description=open('README.md').read().strip(),
     author='Bram Boogaard',
     author_email='padawan@hetnet.nl',
     url='https://github.com/bboogaard/auth0_sso',
     packages=find_packages(include=['auth0_sso', 'auth0_sso.templatetags', 'auth0_sso.migrations']),
     install_requires=[
         'pytest',
         'pytest-cov',
         'pytest-django==4.5.2',
         'django==3.2',
         'python-jose==3.3.0',
         'social-auth-app-django==5.1.0',
         'Pillow>=8.2.0',
         'admin-tool-button==1.0.5a0',
         'pseudo-cron==1.0.0'
     ],
     license='MIT License',
     zip_safe=False,
     keywords='Auth0 SSO',
     classifiers=['Packages', 'Auth0 SSO'])
