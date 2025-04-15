Usage Guide
===========

This section shows how to use the core functionality provided by **darca-yaml**.

Basic Loading Example
---------------------

To load a YAML file as a Python dictionary:

.. code-block:: python

    from darca_yaml import YamlUtils

    data = YamlUtils.load_yaml_file("config.yaml")
    print(data)


Saving Data to YAML
-------------------

You can save a Python dictionary to a YAML file:

.. code-block:: python

    data = {
        "name": "darca-yaml",
        "version": "1.0.0",
        "enabled": True,
        "items": ["a", "b", "c"]
    }

    YamlUtils.save_yaml_file("output.yaml", data)


Validating YAML Before Saving
-----------------------------

You can validate data against a schema before saving:

.. code-block:: python

    schema = {
        "name": {"type": "string", "required": True},
        "version": {"type": "string", "required": True},
        "enabled": {"type": "boolean", "required": True},
        "items": {"type": "list", "schema": {"type": "string"}}
    }

    YamlUtils.save_yaml_file("validated.yaml", data, validate=True, schema=schema)


String-Based Input
------------------

The module also supports YAML content passed as strings:

.. code-block:: python

    yaml_text = """
    name: darca-yaml
    version: 1.0.0
    enabled: true
    items:
      - a
      - b
      - c
    """

    # Validate from string
    YamlUtils.validate_yaml(yaml_text, schema)

    # Save from string
    YamlUtils.save_yaml_file("from_string.yaml", yaml_text)


Error Handling
--------------

All operations raise `YamlUtilsException` on failure:

.. code-block:: python

    from darca_yaml import YamlUtilsException

    try:
        YamlUtils.load_yaml_file("missing.yaml")
    except YamlUtilsException as e:
        print(f"YAML error: {e.error_code} - {e}")
