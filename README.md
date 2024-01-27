# PMSF py-osc2 Framework

[![Build and Publish to PyPI](https://github.com/PMSFIT/py-osc2/actions/workflows/build-and-publish-pypi.yml/badge.svg)](https://github.com/PMSFIT/py-osc2/actions/workflows/build-and-publish-pypi.yml)
[![PyPI Latest Release](https://img.shields.io/pypi/v/py-osc2.svg)](https://pypi.org/project/py-osc2/)
[![Package Status](https://img.shields.io/pypi/status/py-osc2.svg)](https://pypi.org/project/py-osc2/)
[![License](https://img.shields.io/pypi/l/py-osc2.svg)](https://github.com/PMSFIT/py-osc2/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/py-osc2)](https://pepy.tech/project/py-osc2)

## What is it?

PMSF **py-osc2** is a Python package for working with ASAM OpenSCENARIO
DSL 2.x scenario files.

Note that this package is currently provided as a community service.
It is based on the current public review draft of version 2.1.0 of the
language, which is **non-final**, and might include updates based on
current developments.
It is offered without any support and should be considered draft alpha
quality.

Specifically both the public review draft standard, this rendering of
the grammar in ANTLR4, and any intermediate fixes might contain errors.

Nor is the rendering of the grammar in ANTLR4 intended for purposes
other than the goals of this package.

If you are interested in OpenSCENARIO DSL development, please feel free
to contact us directly.

## Main features

- ANTLR4-based parser and lexer for parsing ASAM OpenSCENARIO DSL 2.x
  files.
- Simple syntax checking driver `osc2parser` for parsing and checking
  ASAM OpenSCENARIO DSL 2.x files.

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

When rebuilding the parser from its grammar:

- [setuptools-antlr](https://pypi.org/project/setuptools-antlr/)

## Rebuilding the parser

To rebuild the parser, you need [setuptools-antlr](https://pypi.org/project/setuptools-antlr/)
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

(C) 2021-2024 PMSF IT Consulting Pierre R. Mai

[MPL 2.0](LICENSE)

## Documentation

After installation of the package, an executable script, called
`osc2parser`, is available to parse and check ASAM OpenSCENARIO DSL 2.x
files:

```sh
osc2parser examples/demo.osc
```

This script can optionally also output a tree-view of the parsed file
contents:

```sh
osc2parser -t examples/demo.osc
```
