File Organizer is a command-line automation tool written in Python that organizes cluttered directories by sorting files into folders based on their file extension. A Downloads folder with hundreds of mixed PDFs, images, documents, and audio files can be organized in seconds with a single command.

Background: I developed this project in my first semester for an Entrepreneurship course. Our team’s goal was to explore how automation could improve everyday file management, and this tool was the first step toward that idea. The project began as a simple script and was later refined into a more robust, tested tool.

How it works: The user provides a folder path. The program scans its contents, reads each file’s extension, creates a matching sub-folder if one doesn’t exist yet (for example pdf/, jpg/, txt/), and moves the file into it. When it finishes, it prints a summary of how many files were moved into each folder.

Key features:

Automatic folder creation based on file type
Case-insensitive handling, so .PDF and .pdf are treated the same
Duplicate protection: existing files are never overwritten; conflicts are renamed (report_1.pdf)
Safe skipping of files without extensions, existing folders, and the script itself
Clear error handling for invalid paths
Works from a command-line argument or an interactive prompt
Zero external dependencies, using only Python’s standard library (os/pathlib, shutil)

Quality and engineering practices: The project includes a unit test suite written with pytest covering the main behaviors and edge cases, plus a GitHub Actions workflow that runs the tests automatically on every push across multiple Python versions.

What I learned: Working with the file system in Python, handling edge cases defensively, structuring code into reusable functions, writing automated tests, and setting up a professional repository with documentation, licensing, and CI.

Planned improvements: Category-based sorting (Images, Documents, Videos), an undo feature, a dry-run preview mode, folder watching for automatic organization, and a simple GUI.

Tech stack: Python 3, pytest, GitHub Actions
