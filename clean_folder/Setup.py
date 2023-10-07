from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="0.0.2",
    description="Homerwork 7",
    url="https://github.com/tosss32/",
    author="tosss32",
    author_email="tosss32@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["clean-folder = clean_folder.clean:main"]},
)
