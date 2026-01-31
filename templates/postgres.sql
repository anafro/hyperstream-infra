CREATE USER `$postgresql_user` WITH PASSWORD `$postgresql_password`;
CREATE DATABASE IF NOT EXISTS `$postgresql_database`;
GRANT ALL PRIVILEGES ON `$postgresql_database` TO `$postgresql_user`;
