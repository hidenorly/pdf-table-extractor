# pdf-table-extractor

```
usage: pdf-table-extractor.py [-h] [-j] [-c] [-m] [-s] [-g] [args ...]

Parse command line options.

positional arguments:
  args           Specify pdf files e.g. pdf1.pdf pdf2.pdf

optional arguments:
  -h, --help     show this help message and exit
  -j, --json     Output as json
  -c, --csv      Output as csv
  -m, --merge    Output table as merged
  -s, --stream   Enable parse stream mode. Otherwise use lattice mode
  -g, --noguess  Disable guess mode. You may need to use this for --stream
```

```
$ python3 pdf-table-extractor.py sample.pdf --csv > sample.csv
```

If you can't get any output, you may need to try with the following:

```
$ python3 pdf-table-extractor.py sample.pdf --csv --noguess --stream > sample.csv
```


# setup

```
$ pip install tabula-py
```