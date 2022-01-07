# PMSF py-osc2 Framework

## What is it?

PMSF **py-osc2** is a Python package for working with ASAM OpenSCENARIO 2
scenario files.

Note that this package is currently provided as a community service.
It is based on the current public review draft of the language, which
is **non-final**, and might include updates based on current developments.
It is offered without any support and should be considered draft alpha
quality.

Specifically both the public review draft standard, this rendering of
the grammar in ANTLR4, and any intermediate fixes might contain errors.

Nor is the rendering of the grammar in ANTLR4 intended for purposes
other than the goals of this package.

If you are interested in OpenSCENARIO 2 development, please feel free
to contact us directly.

## Main features

- ANTLR4-based parser and lexer for parsing ASAM OpenSCENARIO 2.x files.
- Simple syntax checking driver `osc2parser` for parsing and checking
  ASAM OpenSCENARIO 2.x files.

## Where to get it

The source code is currently hosted on GitHub at:
https://github.com/PMSFIT/py-osc2

Binary installers for the latest released version are available at the
[Python Package Index (PyPI)](https://pypi.org/project/py-osc2).

```sh
# or PyPI
pip install py-osc2
```

## Dependencies

- [antlr4-python3-runtime](https://pypi.org/project/antlr4-python3-runtime/)
- [antlr-denter](https://pypi.org/project/antlr-denter/)

When rebuilding the parser from its grammar:

- [setuptools-antlr](https://pypi.org/project/setuptools-antlr/)

## Rebuilding the parser

To rebuild the parser, you need [setuptools-antlr](https://cython.org/)
in addition to the normal dependencies above:

```sh
pip install setuptools-antlr
```

To rebuild the package with a rebuilt parser, execute:

```sh
python setup.py antlr build
```

or for installing:

```sh
python setup.py antlr install
```

or alternatively to install in development mode:

```sh
python setup.py antlr develop
```

## License

(C) 2021-2022 PMSF IT Consulting Pierre R. Mai

[MPL 2.0](LICENSE)

## Documentation

After installation of the package, an executable script, called
`osc2parser`, is available to parse and check ASAM OpenSCENARIO 2.x
files:

```sh
osc2parser examples/demo.osc
```

This script can optionally also output a tree-view of the parsed file
contents:

```sh
osc2parser -t examples/demo.osc
```
