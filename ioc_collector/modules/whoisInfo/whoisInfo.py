# -*- coding: utf-8 -*-

from urllib.request import urlopen
from typing import Any
from ioc_collector.config import settings

WHOIS_INFO_API_KEY = settings.WHOIS_INFO_API_KEY
WHOIS_URL = "https://www.whoisxmlapi.com/whoisserver/WhoisService"


async def get_whois_info(url: str) -> Any:
    """
    Retrieves WHOIS information for a given domain URL.

    Args:
        url (str): The domain URL for which to retrieve WHOIS information.

    Returns:
        Any: WHOIS information for the specified domain in JSON format.

    Raises:
        urllib.error.URLError: If there is an issue with the URL request.
    """
    return  ( 
        urlopen(
            f"{WHOIS_URL}?domain={url}&apiKey={WHOIS_INFO_API_KEY}&&outputFormat=JSON"
        )
        .read()
        .decode("utf8")
    )
