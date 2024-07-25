# Home Assistant Add-on: MkDocs

![logo][logo-png]

[MkDocs](https://www.mkdocs.org) is a **fast**, **simple** and **downright gorgeous** static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

This addons has been designed to help Home Assistant users to manage documentation for exemple to keep a trace of modification and configuration they bring to Home Assistant.

## Installation

To install any of the add-ons offered in this repository, you must first add its repository URL to your Home Assistant instance. To do so, click the following button

[![Add repository to your Home Assistant instance.][repository-badge]][repository-url]

or manually add the the following repository URL in the Home Assistant add-on store:

`https://github.com/XavierBerger/hassio-addons`

Then search for any of the add-ons in our addon store (button below) to install them.

[![Open your Home Assistant instance and show the Supervisor add-on store.][addon-store-badge]][addon-store-url]

You can also install them over the buttons in the Readmes of the addon folders.

[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FXavierBerger%2Fhassio-addons

## MkDocs usage

### Write documentation

The source of the documentation presented by this addon is available in `/addon_configs/18ac940c_mkdocs`.

To update your documentation, you should update the configuration file of mkdocs: `mkdocs.yml` and the [Markdown](https://www.markdownguide.org/tools/mkdocs/) files stored in the `docs` directory.

For further informations and guides see:

- [MkDocs User Guide](https://www.mkdocs.org/user-guide/writing-your-docs/) : The heart of this addon.
- [Markdown guide](https://www.markdownguide.org/tools/mkdocs/) : Details of markdown synthax.
- [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/) : Additionnal features provided by Material for MkDocs.
- [PlantUML web site](https://plantuml.com) : A tool to create graphs.

### Real time update

A browser viewing [http://homeassistant.local:8000/](http://homeassistant.local:8000/) is showing exact changes updated periodically.

Visual Studio Code Server preview is rendering showing markdown in real time (with some limitation in markdown rendering such as admonition).

Mkdocs integrated to Home Assistant require a refresh to see update.

## Changelog & Releases

Change log is available in [CHANGELOG.md][changelog].

Releases are based on [Semantic Versioning][semver], and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## License

MIT License

Copyright (c) 2021 - 2024 Xavier Berger

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

[addon-store-url]: https://my.home-assistant.io/redirect/supervisor_store/
[addon-store-badge]: https://img.shields.io/badge/Open_Addon_store_on_my-Home%20Assistant-41BDF5?logo=home-assistant
[licence-badge]: https://img.shields.io/badge/license-MIT-green
[changelog]: https://github.com/XavierBerger/home-assistant-addons/blob/main/mkdocs/CHANGELOG.md
[logo-png]: logo.png
[mkdocs-url]: https://www.mkdocs.org
[repository-badge]: https://img.shields.io/badge/Add_addon_repository_to_my-Home%20Assistant-41BDF5?logo=home-assistant
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FXavierBerger%2Fhassio-addons
[semver]: http://semver.org/spec/v2.0.0.htm
