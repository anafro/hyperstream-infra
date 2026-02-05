import inspect
import logging
from rich.logging import RichHandler

from hyperstream.dependencies.downloader import download_dependency
from hyperstream.vault.alphabets import alpha, alphanumeric
from hyperstream.vault.secrets import generate_secret
from hyperstream.vault.vault import Vault
from hyperstream.vault.filesystem import write


logger: logging.Logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[RichHandler(rich_tracebacks=True)],
    )

    logger.info("Creating secrets...")

    vault: Vault = Vault("./secrets", "./templates")
    postgresql_username = "root"
    postgresql_password = generate_secret(alphanumeric, 128)
    postgresql_database = "hyperstream"
    aws_access_key = "test"
    aws_secret_key = "test"
    rabbitmq_username = generate_secret(alpha, 16)
    rabbitmq_password = generate_secret(alphanumeric, 128)

    vault.new_file("postgresql-username.txt", postgresql_username)
    vault.new_file("postgresql-password.txt", postgresql_password)
    vault.new_file("postgresql-database.txt", postgresql_database)
    vault.new_file("aws-access-key.txt", aws_access_key)
    vault.new_file("aws-secret-key.txt", aws_secret_key)
    vault.new_file("rabbitmq-username.txt", rabbitmq_username)
    vault.new_file("rabbitmq-password.txt", rabbitmq_password)

    vault.new_file_from_template(
        "rabbitmq.conf",
        {
            "rabbitmq_username": rabbitmq_username,
            "rabbitmq_password": rabbitmq_password,
        },
    )

    vault.new_file_from_template(
        "postgres.sql",
        {
            "postgresql_username": postgresql_username,
            "postgresql_password": postgresql_password,
            "postgresql_database": postgresql_database,
        },
    )

    vault.new_file_from_template(
        "laravel.env",
        {
            "postgresql_username": postgresql_username,
            "postgresql_password": postgresql_password,
            "postgresql_database": postgresql_database,
        },
    )

    vault.new_file_from_template("nginx.conf", {})
    write(
        "./.env",
        inspect.cleandoc(f"""
    RABBITMQ_DEFAULT_USER={rabbitmq_username}
    RABBITMQ_DEFAULT_PASS={rabbitmq_password}
    POSTGRESQL_USERNAME={postgresql_username}
    POSTGRESQL_DATABASE={postgresql_database}
    """),
    )
    logger.info("Secrets created")

    logger.info("Downloading dependencies...")
    download_dependency(
        "Java agent for Open Telemetry",
        "https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v2.24.0/opentelemetry-javaagent.jar",
        "opentelemetry-javaagent.jar",
    )
    logger.info("Downloaded all dependencies")

    logger.info("Ready to go!")
    logger.info("Launch hyperstream via `docker compose up`")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Cancelled with Ctrl+C, cya!")
    except Exception as e:
        logger.exception(e)
