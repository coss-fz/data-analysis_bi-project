install_packages:
	pip install -r requirements.txt

build_packages:
	pip install --upgrade wheel
	python3 setup.py bdist_wheel & \
	pip install .[tests]