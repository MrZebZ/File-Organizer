"""File Organizer

Sorts the files inside a folder into sub-folders named after their file
extension (e.g. report.pdf -> pdf/report.pdf).

Usage:
    python file_organizer.py "C:/Users/me/Downloads"
    python file_organizer.py            # prompts for the folder path
"""

import shutil
import sys
from pathlib import Path


def unique_destination(destination: Path) -> Path:
    """Return a path that doesn't exist yet, adding _1, _2, ... if needed."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        counter += 1


def organize(path) -> dict:
    """Move every file in `path` into a sub-folder named after its extension.

    Files without an extension are left untouched. Existing files are never
    overwritten. Returns a dict mapping each extension to the number of files
    moved, e.g. {"pdf": 3, "jpg": 12}.
    """
    folder = Path(path).expanduser()
    if not folder.is_dir():
        raise NotADirectoryError(f"'{folder}' is not a valid folder.")

    this_script = Path(__file__).resolve()
    moved = {}

    for item in list(folder.iterdir()):
        if not item.is_file() or item.resolve() == this_script:
            continue

        extension = item.suffix.lstrip(".").lower()
        if not extension:
            continue

        target_dir = folder / extension
        if target_dir.exists() and not target_dir.is_dir():
            continue  # a file already uses this name, so skip safely
        target_dir.mkdir(exist_ok=True)

        shutil.move(str(item), str(unique_destination(target_dir / item.name)))
        moved[extension] = moved.get(extension, 0) + 1

    return moved


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else input("Enter location: ").strip()

    try:
        moved = organize(path)
    except NotADirectoryError as error:
        print(f"Error: {error}")
        sys.exit(1)

    if not moved:
        print("No files to organize.")
        return

    total = sum(moved.values())
    print(f"Organized {total} file(s):")
    for extension, count in sorted(moved.items()):
        print(f"  {extension}/  <- {count} file(s)")


if __name__ == "__main__":
    main()
