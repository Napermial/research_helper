import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="research_helper-Napermial",
    version="0.0.1",
    author="Péter Hatvani",
    description="A small project to start and run experiments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/napermial/research-helper",
    project_urls={
        "Bug Tracker": "https://github.com/napermial/research-helper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)