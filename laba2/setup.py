from setuptools import setup

setup(
    name = "lab2",
    version = "1.0",
    author = "Romankou Stsiapan",
    author_email = "romankoyv.stepa@mail.ru",
    packages = ["additional", "factory", "json_serializer", 
        "pickle_serializer", "yaml_serializer",
        "toml_serializer"],
    scripts = ["serializer.py"]
)
