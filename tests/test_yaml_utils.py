# tests/test_yaml_utils.py

from unittest.mock import patch

import pytest
import yaml

from darca_yaml import yaml_utils
from darca_yaml.yaml_utils import YamlUtils, YamlUtilsException


def test_load_yaml_file_success(tmp_path, valid_yaml_data):
    file_path = tmp_path / "data.yaml"
    file_path.write_text(yaml.dump(valid_yaml_data))

    result = YamlUtils.load_yaml_file(str(file_path))
    assert result == valid_yaml_data


def test_load_yaml_file_read_error():
    with patch(
        "darca_file_utils.file_utils.FileUtils.read_file",
        side_effect=IOError("boom"),
    ):
        with pytest.raises(YamlUtilsException) as exc:
            YamlUtils.load_yaml_file("invalid.yaml")
        assert "YAML_FILE_READ_ERROR" in str(exc.value)


def test_load_yaml_file_parse_error(tmp_path):
    file_path = tmp_path / "bad.yaml"
    file_path.write_text("::bad: yaml:::")

    with pytest.raises(YamlUtilsException) as exc:
        YamlUtils.load_yaml_file(str(file_path))
    assert "YAML_PARSE_ERROR" in str(exc.value)


def test_load_yaml_file_invalid_structure(tmp_path):
    file_path = tmp_path / "notadict.yaml"
    file_path.write_text("- a\n- b\n- c")

    with pytest.raises(YamlUtilsException) as exc:
        YamlUtils.load_yaml_file(str(file_path))
    assert "YAML_INVALID_STRUCTURE" in str(exc.value)


def test_validate_yaml_success(valid_yaml_data, valid_yaml_schema):
    assert YamlUtils.validate_yaml(valid_yaml_data, valid_yaml_schema)


def test_validate_yaml_fail(valid_yaml_schema):
    invalid_data = {"name": 123, "enabled": "yes"}
    with pytest.raises(YamlUtilsException) as exc:
        YamlUtils.validate_yaml(invalid_data, valid_yaml_schema)
    assert "YAML_VALIDATION_ERROR" in str(exc.value)


def test_save_yaml_file_success(tmp_path, valid_yaml_data):
    file_path = tmp_path / "saved.yaml"
    result = YamlUtils.save_yaml_file(str(file_path), valid_yaml_data)
    assert result
    assert file_path.exists()


def test_save_yaml_file_with_validation(
    tmp_path, valid_yaml_data, valid_yaml_schema
):
    file_path = tmp_path / "validated.yaml"
    result = YamlUtils.save_yaml_file(
        str(file_path),
        valid_yaml_data,
        validate=True,
        schema=valid_yaml_schema,
    )
    assert result
    assert file_path.exists()


def test_save_yaml_file_validation_schema_missing(tmp_path, valid_yaml_data):
    with pytest.raises(YamlUtilsException) as exc:
        YamlUtils.save_yaml_file(
            str(tmp_path / "x.yaml"), valid_yaml_data, validate=True
        )
    assert "YAML_VALIDATION_SCHEMA_MISSING" in str(exc.value)


def test_save_yaml_file_validation_failure(tmp_path, valid_yaml_schema):
    invalid_data = {"name": 123}
    with pytest.raises(YamlUtilsException) as exc:
        YamlUtils.save_yaml_file(
            str(tmp_path / "bad.yaml"),
            invalid_data,
            validate=True,
            schema=valid_yaml_schema,
        )
    assert "YAML_VALIDATION_ERROR" in str(exc.value)


def test_save_yaml_file_serialize_failure(tmp_path, valid_yaml_data):
    file_path = tmp_path / "fail.yaml"

    with patch(
        "darca_yaml.yaml_utils.yaml.dump",
        side_effect=TypeError("not serializable"),
    ):
        with pytest.raises(yaml_utils.YamlUtilsException) as exc:
            yaml_utils.YamlUtils.save_yaml_file(
                str(file_path), valid_yaml_data
            )

    assert "YAML_SERIALIZE_ERROR" in str(exc.value)


def test_save_yaml_file_write_failure(tmp_path, valid_yaml_data):
    with patch(
        "darca_file_utils.file_utils.FileUtils.write_file",
        side_effect=IOError("disk full"),
    ):
        with pytest.raises(YamlUtilsException) as exc:
            YamlUtils.save_yaml_file(
                str(tmp_path / "fail.yaml"), valid_yaml_data
            )
    assert "YAML_FILE_WRITE_ERROR" in str(exc.value)
