from cookiecutter.utils import simple_filter
from getpass import getuser


@simple_filter
def user(_: str) -> str:
    return getuser()
