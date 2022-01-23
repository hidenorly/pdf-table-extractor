# pdf-table-extractor

```
usage: pdf-table-extractor.py [-h] [-j] [-c] [-m] [args ...]

Parse command line options.

positional arguments:
  args         Specify pdf files e.g. pdf1.pdf pdf2.pdf

optional arguments:
  -h, --help   show this help message and exit
  -j, --json   Output as json
  -c, --csv    Output as csv
  -m, --merge  Output table as merged
```

```
$ python3 pdf-table-extractor.py sample.pdf --csv > sample.csv
```

# setup

```
$ pip install tabula-py
```