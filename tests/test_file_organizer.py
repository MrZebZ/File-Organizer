import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from file_organizer import organize  # noqa: E402


def test_moves_files_into_extension_folders(tmp_path):
    (tmp_path / "notes.txt").write_text("hello")
    (tmp_path / "photo.jpg").write_text("img")

    result = organize(tmp_path)

    assert (tmp_path / "txt" / "notes.txt").exists()
    assert (tmp_path / "jpg" / "photo.jpg").exists()
    assert result == {"txt": 1, "jpg": 1}


def test_files_without_extension_are_skipped(tmp_path):
    (tmp_path / "README").write_text("no extension")

    organize(tmp_path)

    assert (tmp_path / "README").exists()


def test_extensions_are_case_insensitive(tmp_path):
    (tmp_path / "a.PDF").write_text("1")
    (tmp_path / "b.pdf").write_text("2")

    organize(tmp_path)

    assert len(list((tmp_path / "pdf").iterdir())) == 2


def test_existing_files_are_not_overwritten(tmp_path):
    (tmp_path / "txt").mkdir()
    (tmp_path / "txt" / "a.txt").write_text("old")
    (tmp_path / "a.txt").write_text("new")

    organize(tmp_path)

    assert (tmp_path / "txt" / "a.txt").read_text() == "old"
    assert (tmp_path / "txt" / "a_1.txt").read_text() == "new"


def test_invalid_path_raises_error(tmp_path):
    with pytest.raises(NotADirectoryError):
        organize(tmp_path / "does_not_exist")
