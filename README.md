# Static Site Generator

Welcome to the Static Site Generator project! This project aims to build a simple and efficient static site generator from scratch. A static site generator transforms raw content files (like Markdown and images) into a static website comprised of HTML and CSS files.

## Table of Contents

- [Introduction](#introduction)
- [Static vs Dynamic Sites](#static-vs-dynamic-sites)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Static sites are quite popular for blogs and other content-heavy websites because they're lightning-fast, secure, and easy to host. Some examples of popular static site generators include:

- [Hugo](https://gohugo.io/)
- [Eleventy](https://www.11ty.dev/)
- [Gatsby](https://www.gatsbyjs.com/)
- [Astro](https://astro.build/)
- [Jekyll](https://jekyllrb.com/)

## Static vs Dynamic Sites

A static site is exactly what it sounds like—**static**. No matter who interacts with the site, the content remains the same. Static sites do not support features like logins, comments, or file uploads. For those features, you would need a *dynamic* site, usually powered by a database and a custom web server.

## Prerequisites

To get started, ensure you have the following tools and dependencies installed:

- Git
- GitHub
- Python 3.11+
- A Unix-like shell (bash, zsh, fish, etc.)

## Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/hawkaii/static-site-generator.git
cd static-site-generator
```

Install any required Python dependencies (if applicable) using pip:

```sh
pip install -r requirements.txt
```

## Usage

Run the static site generator using the following command:
```sh
python generate.py
```

This will generate the static HTML and CSS files from the raw content files located in the designated content directory.

## Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository
    Create a new branch

