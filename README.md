# easier_studwiz
This small script will either print the links or download the pdfs contained at a specific [studwiz]([Studwiz.com - University notes, exercises, exams](https://www.studwiz.com/)) page.

## Installation

```python
$ python -m pip install -r requirements.txt
```

## Usage

```python
$ python app.py <url> [<download_path>]
```

Where:

* `<url>` is the url which contains all the links you want to download.
* `<download_path>` is optional. If specified all the links will be downloaded to this directory.
