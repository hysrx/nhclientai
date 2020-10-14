<p align="center">
  <img height="150" style="margin-top:25px" src="https://raw.githubusercontent.com/hysrx/nhclientai/master/graphics/nhclientai-128.svg">
</p>

<p align="center">
  The Degenerate Contributors's Guide.
</p>

<!-- markdownlint-disable -->
First of all, if you are planning on contributing to nhclientai, thank you! Even if the contribution does not come to fruition, It is cherished!
<!-- markdownlint-restore -->

## Table of Contents

- [Environment Setup](#Environment-Setup)
- [Git Commit Message Guidelines](#Git-Commit-Message-Guidelines)
- [Submitting Issues / Pull Requests](#Submitting-Issues-/-Pull-Requests)
- [Rosetta Localizations](#Rosetta-Localizations)

## Environment Setup

### What nhclientai is developed on, and what you should use

nhclientai is developed with the following stack:

- Debian GNU/Linux 9.5 (stretch) on Windows 10 x86_64 -
[Page](https://docs.microsoft.com/en-us/windows/wsl/install-manual)
/ [Download](https://aka.ms/wsl-debian-gnulinux)

- Python 3.7.4 on PyPy 7.3.2 alpha - [Page](https://www.pypy.org/download.html)
/ [Download](https://downloads.python.org/pypy/pypy3.7-v7.3.2-linux64.tar.bz2)

- Poetry version 1.1.2 - [Page](https://python-poetry.org/)

*Listing these **does not** mean having the entire stack is an absolute
requirement for development!*

It is advised to install the PyPy release of Python 3.7.4 to ensure the most
compatibility, and having Poetry is a must.

---

### Repository Cloning

Firstly, clone the repositories of nhclientai and
[saitoha/libsixel](https://github.com/saitoha/libsixel) repository to your computer;

```bash
git clone https://github.com/hysrx/nhclientai.git && git clone https://github.com/saitoha/libsixel
```

---

### Python Prerequisite Installation

Then assuming you have already installed Poetry, `cd` into the newly created
`nhclientai` directory and run the following:

```bash
poetry install
```

<details>
  <summary>
    Further Reading: Poetry Installation Errors
  </summary>
  If using a fresh WSL Debian install you may get an OpenSSL related issue for
  the cryptography module.
  
  This can be resolved installing the developer package `libssl-dev` using the command
  `sudo apt-get install libssl-dev`. _Other distros may differ in needed packages._
</details>

<details>
  <summary>
    Further Reading: Pillow Build Errors
  </summary>
  If using PyPy, as of 13/10/2020, Pillow has not released wheels for
  PyPy7.3.2-alpha0, so Pillow builds from source.

  Errors regarding zlib and libjpeg can be resolved by installing the developer
  libraries via your distro's package manager. For Debian users, run
  `sudo apt-get install zlib1g-dev libjpeg-dev`
</details>

---

### libsixel and libsixel-python compilation

After installing nhclientai's prerequisites, you can proceed to compile and
install libsixel for python. Instructions can be found on the
[saitoha/libsixel](https://github.com/saitoha/libsixel/tree/master/python)
repository. Issues regarding compiling libsixel on WSL may be created here, but
there may not be much input depending on your case.

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

_(Taken from [saitoha/libsixel/python#install](https://github.com/saitoha/libsixel/tree/master/python#install))_

<details>
  <summary>
    Further Reading: OSError: Cannot load library
  </summary>
  I do not know if this is good practice, but how I fixed the issue was with the
  following:
  
  ```bash
  # execute this in the root libsixel dir, not libsixel/python
  sudo cp src/.libs/* /usr/lib/ -r
  ```

</details>

### Final Notes

Assuming you got everything working, go ahead and do your thing! Do note that
[flake8](https://pypi.org/project/flake8) is installed, so please use it
alongside the repositories' `.flake8` file for linting!

## Git Commit Message Guidelines

Commits from `14/10/2020` onwards must have a commit message and a description
which follow the following guidelines.

The commit message should:

- Not exceed 50 characters
- Short yet descriptive
- Not too vague
- Gramatically correct if possible

The commit description should:

- Follow up on the commit message
- Short yet descriptive

Taking these into account: an example commit command should look like this:

```bash
git commit -m "Refactored graphics.py to support PySixel" -m "- Refactored all functions

- Improve readibility"
```

(_This may be revised later on_)

## Submitting Issues / Pull Requests

Please raise an issue to seek approval before proceeding with a Pull Request.

Please use the appropriate formats and fill out accordingly.

## Rosetta Localizations

Stay tuned!
