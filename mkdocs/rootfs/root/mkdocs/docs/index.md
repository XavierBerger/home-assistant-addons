# MkDocs usage

![](images/logo.png)

[MkDocs](https://www.mkdocs.org) is a **fast**, **simple** and **downright gorgeous** static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

This addons has been designed to help Home Assistant users to manage documentation for exemple to keep a trace of modification and configuration they bring to Home Assistant.

## Write documentation

The source of the documentation presented by this addon is available in `/addon_configs/18ac940c_mkdocs`.

To update your documentation, you should update the configuration file of mkdocs: `mkdocs.yml` and the [Markdown](https://www.markdownguide.org/tools/mkdocs/) files stored in the `docs` directory.

For further informations and guides see:

- [MkDocs User Guide](https://www.mkdocs.org/user-guide/writing-your-docs/) : The heart of this addon.
- [Markdown guide](https://www.markdownguide.org/tools/mkdocs/) : Details of markdown synthax.
- [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/) : Additionnal features provided by Material for MkDocs.
- [PlantUML web site](https://plantuml.com) : A tool to create graphs.

## Real time update

A browser viewing [http://homeassistant.local:8000/](http://homeassistant.local:8000/) is showing exact changes updated periodically.

Visual Studio Code Server preview is rendering showing markdown in real time (with some limitation in markdown rendering such as admonition).

Mkdocs integrated to Home Assistant require a refresh to see update.
