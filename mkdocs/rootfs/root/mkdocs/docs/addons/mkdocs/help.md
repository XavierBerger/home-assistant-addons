# Help/FAQ

_This FAQ is provided by Addon maintener. Do not update it in your mkdocs addons config, it will be overwritten with next update._

???+ "My documentation is not updating"

    This is a known issue due to browser caching.

    If you don't update your documentation for a while, your browser is caching information and is not aware about changes.

    - Click on the top left icon ![](icon.png){ width=24} and Open the link in a new tab.
    - Remove `index.html` from the URL.
    - Refresh with ++ctrl+shift+r++ or ++ctrl+f5++

???+ "Find help to write my documentation"

    The source of your documentation presented by this addon is available in `/addon_configs/18ac940c_mkdocs`.
    To update it, you should modify the configuration file of mkdocs: `mkdocs.yml` and the `Markdown files` stored in the `docs` directory`.
    It is recommanded to use [Studio Code Server](https://github.com/hassio-addons/addon-vscode/blob/main/vscode/DOCS.md){target="_blank"} or [File Editor](https://github.com/home-assistant/addons/blob/master/configurator/DOCS.md){target="_blank"} for edition.

    For further informations and guides see:

    - [MkDocs User Guide](https://www.mkdocs.org/user-guide/writing-your-docs/){target="_blank"} : The heart of this addon.
    - [Markdown guide](https://www.markdownguide.org/tools/mkdocs/){target="_blank"} : Details of markdown synthax.
    - [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/){target="_blank"} : Additionnal features provided by Material for MkDocs.
    - [PlantUML web site](https://plantuml.com){target="_blank"} : A tool to create graphs.
    - [Draw.io](https://www.drawio.com/){target="_blank"} : A tool to draw beautiful diagrams (See bellow for installation and usage in VSCode)

??? "See real time update of my modification"

    A browser viewing [http://homeassistant.local:8000/](http://homeassistant.local:8000/){target="_blank"} is showing exact changes updated periodically.

    Visual Studio Code Server preview is rendering showing markdown in real time (with some limitation in markdown rendering such as admonition).

    Mkdocs integrated to Home Assistant require a refresh to see update.

??? "Edit documentation with VSCode addon"

    The installation of this add-on is pretty straightforward and not different in comparison to installing any other Home Assistant add-on.

    * Click the Home Assistant My button below to open the add-on on your Home
    Assistant instance.

    [![Open this add-on in your Home Assistant instance.](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_vscode&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository){target="_blank"}

    * Click the "Install" button to install the add-on.
    * Start the "Studio Code Server" add-on.
    * Check the logs of the "Studio Code Server" add-on to see if everything went
    well.
    * Click the "OPEN WEB UI" button to open Studio Code Server.

??? "Create diagrams with draw.io in VSCode"

    [Draw.io](https://www.drawio.com/){target="_blank"} is a web application allowing to create diagrams.

    A [VSCode extension](https://open-vsx.org/extension/hediet/vscode-drawio){target="_blank"} dedicated to VSCode allow to edit diagram directly in VSCode.

    To directly see your diagrams in MkDocs, it is recommanded to :

    * Configure draw.io extension to associate `.drawio.png` extension to draw.io extension
      ![drawio-settings](drawio-settings.png)
    * Create diagrams ending with the extension `.drawio.png`. It is editable in VSCode and visible in Mkdocs.
      ![example](example.drawio.png)

??? "How to remove or update the FAQ link in my documentation?"

    Edit `mkdocs.yml` in `/addon_configs/18ac940c_mkdocs/` and remove or update the following line:
    ```yaml
    - Help/FAQ: addons/mkdocs/help.md
    ```
