from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="DeepSearchLite",
    version="0.1.0",
    author="Ibad Rather",
    author_email="ibad.rather.ir@gmail.com",
    description="A package for image similarity search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibadrather/DeepSearchLite",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy",
        "pandas",
        "Pillow",
        "faiss-cpu",
        "tqdm",
    ],
)
