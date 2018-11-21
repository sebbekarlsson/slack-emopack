from setuptools import setup, find_packages


setup(
    name='slack-emopack',
    version='1.0',
    install_requires=[
        'bs4',
        'requests',
        'fake_useragent'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'emopack = slack_emopack.bin:run'
        ]
    }
)
