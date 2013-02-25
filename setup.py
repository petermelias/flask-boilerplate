"""
Flask Boilerplate
-----------------

This extension is in fact an evergrowing collection of boilerplate code applicable
to many web-apps. The modules range from things as simple as view helpers to things
like pre-baked models for common applications (like users or credit cards) pre-configured
for SQLAlchemy.

The extension is well-organized to faciliate the the piecemeal selection and there is little
to no coupling between modules or even functions / classes within.

Obviously a great deal of this code is taken from repeated best-practice code used in numerous
domain specific projects and so the mission to abstract ever further is always assumed.
That said-- ideally code does not make it into this boilerplate extension unless it is
sufficiently abstract to begin with.
	
"""

from setuptools import setup

setup(
	name='Flask-Boilerplate',
	version='0.1',
	url='http://github.com/petermelias/flask-boilerplate',
	license='BSD',
	author='Peter M. Elias',
	author_email='petermelias@gmail.com',
	description='Boilerplate code across various layers of flask, including domain abstractions.',
	long_description=__doc__,
	py_modules=['flask_boilerplate'],
	zip_safe=False,
	include_package_data=True,
	platforms='any',
	install_requires=[
		'Flask',
		'Werkzeug'
	],
	classifiers=[
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	test_suite='tests'
)