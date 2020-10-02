from setuptools import setup


setup(
    name='snappy',
    version='0.1',
    author="mrsiejas",
    author_email="dummy@email.com",
    description="Snappy is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['snappy'],
    url='https://github.com/mrsiejas/snappy',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snappy=snappy.snappy:cli
    '''
)
