#################################### Utils #####################################
# Methods used accross the project and apps for utility
# Requires: Django
# Run:      not meant for direct run, use module import instead
#################################### Utils #####################################

from project.settings import BASE_DIR

DEFAULT_ENV_PATH = BASE_DIR / "project" / ".env"

def load_env_variable(key: str, env_file=DEFAULT_ENV_PATH) -> str | None:
    with open(env_file) as f:
        lines = f.read().splitlines()
    for line in lines:
        if "=" in line:
            k, v = line.split("=", 1)  # Split la línea en dos partes
            if k.strip() == key:
                return v.strip()
    return None
    