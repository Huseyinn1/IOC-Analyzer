# -*- coding: utf-8 -*-

import os
import httpx
import logging
from typing import Union
from dotenv import load_dotenv
load_dotenv()

GOOGLE_SAFE_BROWSING_API_KEY = os.getenv("GOOGLE_SAFE_BROWSING_API_KEY")
GOOGLE_SAFE_URL = "https://safebrowsing.googleapis.com"

logger =  logging.getLogger(__name__)

async def google_safe_browsing_check(url) -> Union[str,None] :
    """
    Checks the threat status of a URL using the Google Safe Browsing API.

    Args:
        url (str): The URL to be checked for threats.

    Returns:
        str or None: If the URL contains dangerous threats, it returns the type of threat. Otherwise, it returns None.
    """
    google_safe_browsing_api_url = f"{GOOGLE_SAFE_URL}/v4/threatMatches:find?key={GOOGLE_SAFE_BROWSING_API_KEY}"
    payload = {
        "client": {"clientId": "your-app-name", "clientVersion": "1.0.0"},
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "THREAT_TYPE_UNSPECIFIED",
                "UNWANTED_SOFTWARE",
                "POTENTIALLY_HARMFUL_APPLICATION",
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(google_safe_browsing_api_url, json=payload)

        if response.status_code == 200:
            data = response.json()
            if "matches" in data:
                threats = [match["threatType"] for match in data["matches"]]
                for threat in threats:
                    logger.info(f"Threat found for Url {url} : {threat}")
                    return threat
    logger.info(f"No threats found for URL {url}")
    return None
