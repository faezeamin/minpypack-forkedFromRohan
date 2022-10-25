import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minpypack",
    version="1.0",
    author="ABC",
    author_email="abc@xyz.com",
    description="Minimal python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["minpypack"],
    python_requires='>=3.6',
)