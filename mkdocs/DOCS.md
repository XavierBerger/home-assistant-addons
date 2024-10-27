# Home Assistant Add-on: MkDocs

![logo](https://raw.githubusercontent.com/spencermamer/home-assistant-notes-addons/main/mkdocs/logo.png)

[MkDocs](https://www.mkdocs.org) is a **fast**, **simple** and **downright gorgeous** static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.  
Start by reading the [introductory tutorial](https://www.mkdocs.org/getting-started/), then check the [User Guide](https://www.mkdocs.org/user-guide/) for more information.

Further information about the add-ons can be found in their dedicated folders.

## Installation

To install any of the add-ons offered in this repository, you must first add its repository URL to your Home Assistant instance. To do so, click the following button

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fspencermamer%2Fhome-assistant-notes-addons)

or manually add the following repository URL in the Home Assistant add-on store:

`https://github.com/spencermamer/home-assistant-notes-addons`

Then search for any of the add-ons in our addon store (button below) to install them.

[![Open your Home Assistant instance and show the add-on store.](https://my.home-assistant.io/badges/supervisor_store.svg)](https://my.home-assistant.io/redirect/supervisor_store/)

You can also install them over the buttons in the README of the addon folders.

## MkDocs usage

### Write documentation

The source of the documentation presented by this addon is available in `/addon_configs/18ac940c_mkdocs`.

To update your documentation, you should update the configuration file of mkdocs: `mkdocs.yml` and the [Markdown](https://www.markdownguide.org/tools/mkdocs/) files stored in the `docs` directory.

For further information and guides see:

- [MkDocs User Guide](https://www.mkdocs.org/user-guide/writing-your-docs/): The heart of this addon.
- [Markdown guide](https://www.markdownguide.org/tools/mkdocs/): Details of markdown syntax.
- [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/): Additional features provided by Material for MkDocs.
- [PlantUML web site](https://plantuml.com): A tool to create graphs.

### To go further

For tips and tricks using this addon, have a look at [Help/FAQ](rootfs/root/mkdocs/docs/addons/mkdocs/help.md).  
_Note: Rendering is designed to be displayed in the add-on itself and is not clean in GitHub._

## Changelog & Releases

The changelog is available in [CHANGELOG.md](https://github.com/spencermamer/home-assistant-notes-addons/blob/main/mkdocs/CHANGELOG.md).

Releases are based on [Semantic Versioning](http://semver.org/spec/v2.0.0.htm), and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## Experimental

Even if officially published addons are tested and work on my Home Assistant Yellow, addons might not be stable at all. Use at your own risk!

## License

MIT License

Copyright (c) 2021 - 2024 spencermamer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
