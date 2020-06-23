import setuptools

setuptools.setup(
    name="odin",
    version="0.0.1",
    author="Gabriele Abbati",
    author_email="ao@ot.co",
    description="ODIN",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'scipy', 'tensorflow==1.13.*'],
    classifiers=(
        "Programming Language :: Python :: 3"),)
