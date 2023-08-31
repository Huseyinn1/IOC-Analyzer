from pathlib import Path
from dynaconf import Dynaconf

BASE_DIR = Path(__file__).resolve().parent.parent

settings = Dynaconf (
    load_dotenv = True,
    envvar_prefix_for_dynaconf = False,
    dotenv_path = str(BASE_DIR.joinpath("envs",".env")),
)