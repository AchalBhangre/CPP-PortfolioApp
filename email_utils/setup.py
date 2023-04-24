import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emailsendingLib",
    # Replace with your own username above
    version="0.0.3",
    author="Aachal Bhangre",
    author_email="aachal2193@example.com",
    description="masters project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AchalBhangre/CPP-PortfolioApp",
    packages=setuptools.find_packages(),
    # if you have libraries that your module/package/library
    #you would include them in the install_requires argument
    install_requires=[''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)