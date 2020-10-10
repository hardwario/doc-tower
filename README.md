# Repository: doc-tower

This repository contains source data for the online datasheet of TOWER. It uses **Sphinx** as a documentation generator altogether with **reStructuredText** as a lightweight markup language.

The documentation is hosted at [**Read The Docs**](https://readthedocs.org/) and is automatically built on commit to the master branch.

Once built, the site is available at: **https://tower.hardwario.com/**


## Setup

You can build your local version of the documentation. All you need is [**Docker Desktop**](https://www.docker.com/products/docker-desktop) and **Git**.

Follow these steps:

1. Open the terminal.

1. Clone the repository:

       git clone https://github.com/hardwario/doc-tower.git

1. Go to the repository:

       cd doc-tower

1. Build the Docker image:

       ./docker.sh build


## Usage

Generate the documentation:

    ./docker.sh generate

The documentation output is in the directory `build/html/`.

You can also run the local web server that watches source files for changes and automatically regenerates the documentation:

    ./docker.sh serve

Once started, the documentation is available at: **http://localhost:5500/**

If you want to clean the output (contents of the `build/` directory), just use:

    ./docker.sh clean


## Editing

The source files are located in the `source/` directory. Use an editor of your preference.

We recommend **Visual Studio Code** with these extensions:

* **EditorConfig** (to automatically follow `.editorconfig` file rules)
* **reStructuredText** (syntax support and highlight for `.rst` files)
* **Grammarly** (for spelling and grammar check)

Altogether with the `./docker.sh serve` mode, you can have editor and the live browser preview side-by-side.


## License

This project is licensed under the [**Creative Commons Attribution-ShareAlike 4.0 International License**](https://creativecommons.org/licenses/by-sa/4.0/) - see the [**LICENSE**](LICENSE) file for details.

---

Made with ❤️ by [**HARDWARIO s.r.o.**](https://www.hardwario.com/) in the heart of Europe.
