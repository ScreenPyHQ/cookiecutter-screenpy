from __future__ import annotations

from {{cookiecutter.project_name}} import __version__


def test_metadata() -> None:
    assert __version__.__title__ == "{{cookiecutter.project_name}}"
    assert __version__.__license__ == "MIT"
    assert __version__.__author__ == "{{cookiecutter.author}}"
