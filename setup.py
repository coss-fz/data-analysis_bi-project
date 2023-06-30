
"""
Script that configures the package
"""


from setuptools import setup, find_packages




with open("README.md", encoding='UTF-8') as readme_file:
    readme = readme_file.read()

with open("requirements.txt", encoding='UTF-8') as f:
    requirements = f.read().splitlines()


##Remember to change versions when it is modified
setup_requirements = [ ]
__version__ = '0.2.0' #######

test_requirements = ['pytest', 'pytest-cov']


if __name__ == "__main__":
    setup(
        description="Initial proyect to do a data analysis for a BI Team", #######
        author='coss-fz', #######
        author_email='email@domain.com', #######
        classifiers=[
            'Development Status :: Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.8' ####### 
        ],
        install_requires=requirements,
        license='MIT License',
        long_description=readme,
        include_package_data=True,
        keywords='package_module', #######
        name='package_module', #######
        packages=find_packages(where='src'),
        package_dir={"":"src"},
        setup_requires=setup_requirements,
        test_suite='pytest',
        extras_require={
            "tests":test_requirements,
        },
        url='',
        version=__version__,
        zip_safe=False,
    )
