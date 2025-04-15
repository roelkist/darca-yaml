darca-yaml
==========

A lightweight YAML utility library with validation support using Cerberus, designed for simplicity and composability in structured Python projects.

|Build Status| |Deploy Status| |CodeCov| |Formatting| |License| |PyPi Version| |Docs|

.. |Build Status| image:: https://github.com/roelkist/darca-yaml/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/roelkist/darca-yaml/actions
.. |Deploy Status| image:: https://github.com/roelkist/darca-yaml/actions/workflows/cd.yml/badge.svg
   :target: https://github.com/roelkist/darca-yaml/actions
.. |Codecov| image:: https://codecov.io/gh/roelkist/darca-yaml/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/roelkist/darca-yaml
   :alt: Codecov
.. |Formatting| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black code style
.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
.. |PyPi Version| image:: https://img.shields.io/pypi/v/darca-yaml
   :target: https://pypi.org/project/darca-yaml/
   :alt: PyPi
.. |Docs| image:: https://img.shields.io/github/deployments/roelkist/darca-yaml/github-pages
   :target: https://roelkist.github.io/darca-yaml/
   :alt: GitHub Pages

Overview
--------

**darca-yaml** provides utilities for:

- 📖 Loading and saving YAML files
- ✅ Validating YAML content with Cerberus
- 🔗 Integrated exception handling (`darca-exception`)
- 📄 File handling via `darca-file-utils`
- 🧪 100% test coverage with Pytest and CI integration

Installation
------------

.. code-block:: bash

    pip install darca-yaml

Usage
-----

.. code-block:: python

    from darca_yaml.yaml_utils import YamlUtils

    schema = {"name": {"type": "string"}, "enabled": {"type": "boolean"}}

    data = YamlUtils.load_yaml_file("config.yaml")
    YamlUtils.validate_yaml(data, schema)
    YamlUtils.save_yaml_file("output.yaml", data, validate=True, schema=schema)

Development Setup
-----------------

Clone the repo and install dependencies:

.. code-block:: bash

    git clone https://github.com/roelkist/darca-yaml
    cd darca-yaml
    make install

Run checks before committing:

.. code-block:: bash

    make check

Run individual targets (faster iteration):

.. code-block:: bash

    make format
    make test
    make precommit
    make docs

Contribution Guide
------------------

We welcome contributions via **pull requests** to `main`.  
Please see the `CONTRIBUTING.rst` file for detailed instructions.

License
-------

MIT

