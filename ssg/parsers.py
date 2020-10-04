import shutil
from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path, 'r') as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext=".html"):
        full_path = Path(dest/path.with_suffix(ext).name)
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest):
        shutil.copy2(path, Path(dest/path.relative_to(source)))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)