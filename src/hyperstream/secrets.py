import secrets


def generate_secret(alphabet: str, length: int) -> str:
    if length < 0:
        raise ValueError(f"Secret length must be positive, {length} provided.")

    if len(alphabet) == 0:
        raise ValueError("Secret alphabet should have at least one character.")

    return "".join(secrets.choice(alphabet) for _ in range(length))
