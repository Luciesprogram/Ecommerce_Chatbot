from setuptools import find_packages, setup

setup(
    name = "ECommercebot",
    version = "0.0.1",
    author = "Vikrant",
    packages=find_packages(),
    install_requires=["langchain",
"langchain-astradb",
"sentence_transformers",
"datasets",
"transformers",
"pypdf",
"flask",
"python-dotenv",
"langchain-huggingface"]
)