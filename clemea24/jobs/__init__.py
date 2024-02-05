"""Module for design jobs."""

from nautobot.apps.jobs import register_jobs

from clemea24.designs.initial_data.jobs import InitialDesign
from clemea24.designs.core_site.jobs import CoreSiteDesign
from clemea24.designs.edge_site.jobs import EdgeDesign

register_jobs(InitialDesign, CoreSiteDesign, EdgeDesign)
