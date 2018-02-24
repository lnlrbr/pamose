from setuptools import setup, find_packages

setup(
    name='pamose',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
        'pytest',
        'werkzeug',
        'itsdangerous',
        'passlib',
        'sqlalchemy',
        'marshmallow-sqlalchemy',
        'flask',
        'flask-restful',
        'flask-sqlalchemy',
        'flask_marshmallow',
        'flask_httpauth'
    ],
    entry_points='''
        [console_scripts]
        pamose=pamose.launcher:cli
    ''',
)
