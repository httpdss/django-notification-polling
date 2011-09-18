from setuptools import setup, find_packages

version = '0.1.0'

LONG_DESCRIPTION = """
=====================================
Django Notification Polling
=====================================
"""

setup(
        name='django-notification-polling',
        version=version,
        description="django-notification-polling",
        long_description=LONG_DESCRIPTION,
        classifiers=[
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Framework :: Django",
            "Environment :: Web Environment",
            ],
        keywords='django,notification,pinax,polling',
        author='Kenneth Belitzky',
        author_email='kenny@belitzky.com',
        license='MIT',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        setup_requires=['setuptools_git'],
        )
