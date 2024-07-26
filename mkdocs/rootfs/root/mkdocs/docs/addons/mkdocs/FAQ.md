# FAQ

_This FAQ is provided by Addon maintener. Do not update it in your mkdocs addons config, it will be overwritten with next update._

## Tips and tricks

??? "Find help to write my documentation"

    The source of the documentation presented by this addon is available in `/addon_configs/18ac940c_mkdocs`.

    To update your documentation, you should update the configuration file of mkdocs: `mkdocs.yml` and the [Markdown](https://www.markdownguide.org/tools/mkdocs/) files stored in the `docs` directory.

    For further informations and guides see:

    - [MkDocs User Guide](https://www.mkdocs.org/user-guide/writing-your-docs/) : The heart of this addon.
    - [Markdown guide](https://www.markdownguide.org/tools/mkdocs/) : Details of markdown synthax.
    - [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/) : Additionnal features provided by Material for MkDocs.
    - [PlantUML web site](https://plantuml.com) : A tool to create graphs.

??? "See real time update of my modification"

    A browser viewing [http://homeassistant.local:8000/](http://homeassistant.local:8000/) is showing exact changes updated periodically.

    Visual Studio Code Server preview is rendering showing markdown in real time (with some limitation in markdown rendering such as admonition).

    Mkdocs integrated to Home Assistant require a refresh to see update.

??? "Edit documentation with VSCode addon"

    The installation of this add-on is pretty straightforward and not different in comparison to installing any other Home Assistant add-on.

    1. Click the Home Assistant My button below to open the add-on on your Home
    Assistant instance.

    [![Open this add-on in your Home Assistant instance.](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_vscode&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository)

    1. Click the "Install" button to install the add-on.
    1. Start the "Studio Code Server" add-on.
    1. Check the logs of the "Studio Code Server" add-on to see if everything went
    well.
    1. Click the "OPEN WEB UI" button to open Studio Code Server.

??? "Create diagrams with draw.io in VSCode"

    [Draw.oi](https://www.drawio.com/) is a web application allowing to create diagrams.

    A [VSCode extension](https://open-vsx.org/extension/hediet/vscode-drawio) dedicated to VSCode allow to edit diagram directly in VSCode.

    To directly see your diagrams in MkDocs, it is recommanded to :

    * Configure draw.io extension to associate `.drawio.png` extension to draw.io extension
      ![drawio-settings](drawio-settings.png)
    * Create diagrams ending with the extension `.drawio.png`. It is editable in VSCode and visible in Mkdocs.
      ![example](example.drawio.png)

??? "Modify FAQ"

    ??? "How to remove the FAQ from my documentation?"

        Edit mkdocs.yml in `/addon_configs/18ac940c_mkdocs/` and remove the folowing lines:
        ```yaml
        - Mkdocs Addon:
            - addons/mkdocs/FAQ.md
        ```

    ??? "How to modify the FAQ location in my documentation?"

        Edit mkdocs.yml in `/addon_configs/18ac940c_mkdocs/` and modify the first line of the folowing code:
        ```yaml
        - Mkdocs Addon:
            - addons/mkdocs/FAQ.md
        ```
