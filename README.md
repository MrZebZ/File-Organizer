# 📁 File Organizer

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://github.com/YOUR-USERNAME/file-organizer/actions/workflows/ci.yml/badge.svg)

A simple Python automation tool that organizes a messy folder by sorting files into sub-folders based on their file extension.

Built during my first semester for an **Entrepreneurship** course. Our idea was to bring automation into file management, and this was the first step toward it.

## How It Works

**Before**

```
Downloads/
├── report.pdf
├── photo.jpg
├── notes.txt
├── resume.pdf
└── song.mp3
```

**After**

```
Downloads/
├── pdf/
│   ├── report.pdf
│   └── resume.pdf
├── jpg/
│   └── photo.jpg
├── txt/
│   └── notes.txt
└── mp3/
    └── song.mp3
```

## Features

- Sorts files into folders named after their extension
- Creates folders automatically when they don't exist
- Case-insensitive (`.PDF` and `.pdf` go in the same folder)
- Never overwrites files (duplicates are renamed `file_1.txt`, `file_2.txt`, ...)
- Skips files with no extension and ignores existing folders
- Prints a summary of what was moved
- Uses only the Python standard library, so there is nothing to install

## Getting Started

### Prerequisites

- Python 3.9 or higher

### Installation

```bash
git clone https://github.com/YOUR-USERNAME/file-organizer.git
cd file-organizer
```

### Usage

Pass the folder path as an argument:

```bash
python file_organizer.py "C:/Users/YourName/Downloads"
```

Or run it with no arguments and enter the path when prompted:

```bash
python file_organizer.py
Enter location: C:/Users/YourName/Downloads
```

Example output:

```
Organized 5 file(s):
  jpg/  <- 1 file(s)
  mp3/  <- 1 file(s)
  pdf/  <- 2 file(s)
  txt/  <- 1 file(s)
```

> ⚠️ **Tip:** Try it on a test folder first. Files are moved, not copied.

## Running Tests

```bash
pip install -r requirements.txt
pytest
```

## Project Structure

```
file-organizer/
├── file_organizer.py        # Main script
├── tests/
│   └── test_file_organizer.py
├── .github/workflows/ci.yml # Automated tests
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Future Improvements

- Organize by file category (Images, Documents, Videos) instead of raw extension
- Undo option to reverse the last organization
- Scheduled / automatic organization of a watched folder
- GUI version
- Dry-run mode to preview changes before moving files

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

**YOUR NAME**
[GitHub](https://github.com/YOUR-USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR-PROFILE)
