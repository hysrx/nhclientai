<p align="center">
  <img height="150" style="margin-top:25px" src="https://raw.githubusercontent.com/hysrx/nhclientai/master/graphics/nhclientai-128.svg">
  <h1><center>nhclientai</center></h1>
  <i><center>The</i> nhentai CLI client, for the terminal-dwelling degenerates.</center>
</p>

## Current Situation

As of 13/10/2020, nhclientai is stated for an alpha¹ release by November 4th, 2020.

<details>
  <summary>
    Further Reading
  </summary>
  ¹ version scheming conventions are not traditional in a sense that releases are incrementally named after their respective greek name (Alpha, Beta, Gamma, etc)
</details>

### Planned Features (nhclientai Alpha)

- Homepage
- Query via Search
- Inbuilt Doujinshi Viewer

## System and Python Support

As of nhclientai Pre-Alpha, Linux is the only supported platform² and the minimum Python version required is `3.7`³. A SIXEL-supported terminal is required to run
nhclientai properly.

<details>
  <summary>
    Further Reading
  </summary>
  ² Due to libsixel being a Linux-oriented library, there is no current vanilla Windows support. Opportunities may arise in the future, but getting a working application is currently a priority. In the meantime, the Windows Subsystem for Linux will work nicely, also as it is primarily what is used to develop nhclientai.

  ---

  ³ Python 3.7 being the minimum is due to [hentai](https://github.com/hentai-chan/hentai) requiring the dataclass module, which was shipped only with Python 3.7 and onwards Another reason is that PyPy is what I primarily use in Python development, which has now Python 3.7 support.
</details>

## Setup

nhclientai is currently **not** in a usable state! Once it is, nhclientai will be distributed via pip and GitHub Packages.

###### For the _developer degenerates_, further reading is available in the [CONTRIBUTION.md](https://github.com/hysrx/nhclientai/blob/master/CONTRIBUTION.md) file, under the [Environment Setup](https://github.com/hysrx/nhclientai/blob/master/CONTRIBUTION.md#Environment-Setup) section.

## Contribution

Read further in the [CONTRIBUTION.md](https://github.com/hysrx/nhclientai/blob/master/CONTRIBUTION.md) file located within the repository.
