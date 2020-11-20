from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="thecolorapi",
    version="1.0.0",
    description="A simple python wrapper for 𝗧𝗵𝗲 𝗖𝗼𝗹𝗼𝗿 𝗔𝗣𝗜 ❤🧡💛💚💙💜",
    long_description=readme(),
    long_description_content_type='text/markdown',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    url="https://github.com/RealA10N/thecolorapi",
    project_urls={
        "Source code": "https://github.com/RealA10N/thecolorapi",
        "Website": "https://www.thecolorapi.com/",
    },

    author="RealA10N",
    author_email="downtown2u@gmail.com",

    keywords="color python api wrapper-api colorscheme colors",
    license="MIT",

    packages=find_packages(),
    install_requires=["requests"],
)
