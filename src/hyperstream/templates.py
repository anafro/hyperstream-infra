def fill_template(template_string: str, replacements: dict[str, object]) -> str:
    filled_template: str = template_string

    for placeholder, substitution in replacements.items():
        filled_template = filled_template.replace(
            f"{{{{{placeholder}}}}}", str(substitution)
        )

    return filled_template
