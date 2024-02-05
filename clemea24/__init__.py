"""App declaration for clemea24."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class Clemea24Config(NautobotAppConfig):
    """App configuration for the clemea24 app."""

    name = "clemea24"
    verbose_name = "Clemea24"
    version = __version__
    author = "Network to Code, LLC"
    description = "Cisco Live EMEA 2024 Nautobot Demo."
    base_url = "clemea24"
    required_settings = []
    min_version = "2.1.2"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = Clemea24Config  # pylint:disable=invalid-name
