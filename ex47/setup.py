try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Franz Habison',
    'url': 'www.github.com/fraunz81',
    'download_url': 'Where to download it.',
    'author_email': 'habison.franz@gmx.at',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
