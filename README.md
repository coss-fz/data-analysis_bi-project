# BI Project: Data Analysis with Python
This repository contains a project about data analysis and visualization of the results in a basic 'dashboard', taking as reference public datasets, in order to understand the methodology.


## Quick Start
In order to run all the codes succesfully, you'll need to create a python virtual environment and install all the necessary requirements.

### Configure the Python Environment
1. Create the virtual environment (version is not mandatory, but `python 3.8` is recommended)
   ```sh
   python<version> -m venv <venv_name>
   ```
2. Activate the environment
   ```sh
   source <venv_name>/bin/activate
   ```
   Whenever you want to get out from the environment, just run the next command:
   ```sh
   deactivate
   ```

### Install the required python libraries and packages
1. Install the necessary libraries through the 'Makefile'
   ```sh
   make install_packages
   ```
2. Install the personalized packages through 'setup.py'
   ```sh
   make build_packages
   ```


## Navigate through the project
Once you are all set, feel free to browse through the project. 

* Go to 'processing_data', visualize the EDA and see the images that were generated
* Go to 'src/package_module' to see the functions that were used in the project
* Go to 'test' to see the functions used for the unit tests, and try to test the code yourself
   ```sh
   pytest tests/test_functions.py
   ```
* Go to 'src' to see the main code that generates the dashboard ('static' and 'templates' contain the necessary images, '.html', and '.css' files to run the code), and run it yourself
   ```sh
   python3 src/main.py
   ```

When you run the code when trying to generate the dashboard you should get something like the '[Dashboard-PD](Dashboard-PD.pdf)' file.
