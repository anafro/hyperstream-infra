import logging
from pathlib import Path

from hyperstream.vault.filesystem import read, write
from hyperstream.vault.secrets import generate_secret
from hyperstream.vault.templates import fill_template


logger: logging.Logger = logging.getLogger(__name__)


class Vault:
    files_dir: Path
    templates_dir: Path

    def __init__(self, files_dir: str | Path, templates_dir: str | Path) -> None:
        self.files_dir = Path(files_dir)
        self.templates_dir = Path(templates_dir)

    def new_file(self, name: str, content: str) -> None:
        write(self.files_dir / name, content)
        logger.info(f"Created: {name}")

    def new_secret(self, name: str, alphabet: str, length: int) -> None:
        secret: str = generate_secret(alphabet, length)
        self.new_file(name, secret)

    def read_template(self, name: str) -> str:
        return read(self.templates_dir / name)

    def new_file_from_template(
        self, name: str, replacements: dict[str, object]
    ) -> None:
        template: str = self.read_template(name)
        filled_template: str = fill_template(template, replacements)
        self.new_file(name, filled_template)
