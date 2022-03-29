import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="currency-symbols",
    version="2.0.2",
    author="Arshad Kazmi",
    author_email="arshadkazmi42@gmail.com",
    description="Get currency symbol by currency code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arshadkazmi42/currency-symbols",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
