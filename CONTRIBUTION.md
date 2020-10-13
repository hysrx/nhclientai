<p align="center">
  <img height="150" style="margin-top:25px" src="https://raw.githubusercontent.com/hysrx/nhclientai/master/graphics/nhclientai-128.svg">
  <h1><center>nhclientai</center></h1>
  <center>The Degenerate Developer's Guide.</center>
</p>

First of all, if you are planning on contributing to nhclientai, thank you! Even if the contribution does not come to fruition, It is cherished!

## Table of Contents

- [Environment Setup](#Environment-Setup)
- [Git Commit Message Guidelines](#Git-Commit-Message-Guidelines)
- [Submitting Issues / Pull Requests](#Submitting-Issues-/-Pull-Requests)
- [Submitting Rosetta Translations](#Submitting-Rosetta-Translations)

## Environment Setup

### What nhclientai is developed on, and what you should use

nhclientai is developed with the following stack:

- Debian GNU/Linux 9.5 (stretch) on Windows 10 x86_64 - [Page](https://docs.microsoft.com/en-us/windows/wsl/install-manual) / [Download](https://aka.ms/wsl-debian-gnulinux)

- Python 3.7.4 on PyPy 7.3.2 alpha - [Page](https://www.pypy.org/download.html) / [Download](https://downloads.python.org/pypy/pypy3.7-v7.3.2-linux64.tar.bz2)

- Poetry version 1.1.2 - [Page](https://python-poetry.org/)

*Listing these **does not** mean having the entire stack is an absolute requirement for development!*

It is advised to install the PyPy release of Python 3.7.4 to ensure the most compatibility, and having Poetry is a must.

### Repository Cloning

Firstly, clone the repositories of nhclientai and [saitoha/libsixel](https://github.com/saitoha/libsixel) repository to your computer;

```bash
$ git clone https://github.com/hysrx/nhclientai.git && git clone https://github.com/saitoha/libsixel
```

### Python Prerequisite Installation

Then assuming you have already installed Poetry, `cd` into the newly created `nhclientai` directory and run the following:

```bash
$ poetry install
```

<details>
  <summary>
    Further Reading: Poetry Installation Errors
  </summary>
  If using a fresh WSL Debian install you may get an OpenSSL related issue for the cryptography module.
  
  This can be resolved installing the developer package `libssl-dev` using the command `sudo apt-get install libssl-dev`. _Other distros may differ in needed packages._

</details>

<details>
  <summary>
    Further Reading: Pillow Build Errors
  </summary>
  If using PyPy, as of 13/10/2020, Pillow has not released wheels for PyPy7.3.2-alpha0, so Pillow builds from source.

  Errors regarding zlib and libjpeg can be resolved by installing the developer libraries via your distro's package manager. For Debian users, run `sudo apt-get install zlib1g-dev libjpeg-dev`

</details>

### libsixel and libsixel-python compilation

After installing nhclientai's prerequisites, you can proceed to compile and install libsixel for python. Instructions can be found on [saitoha's libsixel repository](https://github.com/saitoha/libsixel/tree/master/python). Issues regarding compiling libsixel on WSL may be created here, but there may not be much input depending on your case.

And if this wasn't obvious - you need `gcc` and `make`.

What I personally use to build libsixel-python is the following:

```bash
cd libsixel
./configure --disable-python
make install  # try sudo make install if this fails
cd python
python setup.py install
```

To see if everything works, pop up an interpreter and try:

```python
Python 3.7.4 (87875bf2dfd8, Sep 24 2020, 07:26:36)
[PyPy 7.3.2-alpha0 with GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>> from libsixel.encoder import Encoder
```

_(Taken from https://github.com/saitoha/libsixel/tree/master/python#install)_

<details>
  <summary>
    Further Reading: OSError: Cannot load library
  </summary>
  I do not know if this is good practice, but how I fixed the issue was,
  
  ```bash
  sudo cp src/.libs/* /usr/lib/ -r  # execute this in the root libsixel dir, not libsixel/python
  ```

</details>

### Final Notes

Assuming you got everything working, go ahead and do your thing! Do note that [flake8](https://pypi.org/project/flake8) is installed, so please use it alongside the repositories' `.flake8` file for linting!

## Git Commit Message Guidelines

_This may be revised later on_

The commit message should
- Not exceed 80 characters
- Must not be too vague
- Descriptive to an extent

Example: "`Refactored nhclientai.graphics to support PySixel`"

Anti-pattern: "`Changed a few lines to get things working`" (Vague)

## Submitting Issues / Pull Requests

Please raise an issue to seek approval before proceeding with a PR.

Please use the appropriate formats and fill out accordingly.

### Submitting Rosetta Translations

If the modification of code is to which a great extent (more than 50% of total Rosetta words), a pull request can be made - else a issue has to be made. In both scenarios, the following format has to be followed. (_This is done for you if you used a template issue during PR/Issue Creation_)

```markdown
# Translating en_gb to (language code)
## Background
- insert points
- native speaker
- learning for x years
- [proof](https://link-to.proof)

## Translated:
(Format: key.key.key, etc)
- input.next_doujin
- input.search

## Why I have Modified the File
(This portion would only be included if a troller was unknowingly allowed to tamper with the translation.)
```

Proof must meet the following criteria:

All personally identifiable information **must** be blanked out.

Photo must be an image of a
- Government-issued ID
- Membership Card with information that links it to a specific country
- Transport Card
with the language that the translator is translating to being a main language of the directly stated/textually implied country.

or

- A school/language center provided test paper with at least passing marks for the language that the translator is translating to.

Here is an example:

![rosetta-proof](https://i.imgur.com/n47SHC9.jpg)

From this image the following is deducted:

- The user being proven is `hysrx`.
  - Said user is living in Singapore - inferred from "`2. This card is only for Virtualand Serangoon.`", [DuckDuckGo Results](https://duckduckgo.com/?q=virtualand+serangoon)
  - Said user is eligible to prove that they speak *English, Chinese, Malay or Tamil* - inferred from [Languages of Singapore](https://en.wikipedia.org/wiki/Languages_of_Singapore)
