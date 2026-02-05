from pathlib import Path
from urllib import request
import logging
from rich.progress import Progress

dependencies_path = Path("./bin")
logger = logging.getLogger(__name__)


def download_dependency(name: str, url: str, filename: str) -> None:
    dependencies_path.mkdir(parents=True, exist_ok=True)
    logger.info("Downloading dependency: %s...", name)

    with Progress(transient=True) as progress:
        task = progress.add_task(f"Fetching {url}", total=None)

        def hook(blocknum: int, blocksize: int, totalsize: int) -> None:
            if totalsize > 0:
                progress.update(task, total=totalsize)
                progress.update(task, completed=blocknum * blocksize)

        _ = request.urlretrieve(url, dependencies_path / filename, reporthook=hook)

    logger.info("Downloaded: %s", name)
