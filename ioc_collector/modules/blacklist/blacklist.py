# -*- coding: utf-8 -*-

import httpx
import logging
from ioc_collector.config import settings

logger = logging.getLogger(__name__)

BLACKLIST_API_KEY = settings.BLACKLIST_API_KEY
HETRIX_TOOLS_URL = "https://api.hetrixtools.com/v2"


async def get_blacklist_links(ioc_type, ioc) ->str:
    """
    Retrieve delist links for the given Indicator of Compromise (IOC) from blacklists.

    Args:
        ioc_type (str): Type of the Indicator of Compromise (e.g., "ip", "domain", etc.).
        ioc (str): Value of the Indicator of Compromise.

    Returns:
        str or None: A list of delist links for the blacklisted IOC, or None if not found.

    """
    endpoint = f"/{BLACKLIST_API_KEY}/blacklist-check/{ioc_type}/{ioc}/"
    url = HETRIX_TOOLS_URL + endpoint

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            data = response.json()

            delist_links = set()
            if "blacklisted_on" in data:
                for item in data["blacklisted_on"]:
                    delist_links.add(item["delist"])

            return str((delist_links)) 
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return None