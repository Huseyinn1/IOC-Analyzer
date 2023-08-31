# -*- coding: utf-8 -*-
import httpx
from ioc_collector.config import settings


VIRUSTOTAL_API_KEY = settings.VIRUSTOTAL_API_KEY
VIRUS_TOTAL_URL = "https://www.virustotal.com"


async def virustotal_url(user_url):
    """
    Query VirusTotal API to submit a URL for analysis.

    Args:
        user_url (str): The URL to be submitted for analysis.

    Returns:
        str or None: The analysis ID of the submitted URL, or None if the request was not successful.
    """
    url = f"{VIRUS_TOTAL_URL}/api/v3/urls"
    payload = {"url": user_url}
    headers = {
        "accept": "application/json",
        "x-apikey": VIRUSTOTAL_API_KEY,
        "content-type": "application/x-www-form-urlencoded",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            url_analysis_id = data["data"]["id"].split("-")[1]
            return url_analysis_id
        else:
            return None

async def analyzed_virustotal_url(analysis_id):
    """
    Query VirusTotal API to retrieve analysis results for a submitted URL.

    Args:
        analysis_id (str): The analysis ID of the URL.

    Returns:
        dict or None: Analysis results of the URL, or None if the request was not successful.
    """
    url = f"{VIRUS_TOTAL_URL}/api/v3/urls/{analysis_id}"
    headers = {"accept": "application/json", "x-apikey": VIRUSTOTAL_API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

async def analyzed_virustotal(ioc_type, ioc):
    """
    Query VirusTotal API to retrieve analysis results for a specific indicator of compromise (IOC).

    Args:
        ioc_type (str): The type of the IOC, such as "urls", "domains", "ip_addresses".
        ioc (str): The IOC value to query for.

    Returns:
        dict or None: Non-clean analysis results from various engines, or None if the request was not successful.
    """
    url = f"{VIRUS_TOTAL_URL}/api/v3/{ioc_type}/{ioc}"
    headers = {"accept": "application/json", "x-apikey": VIRUSTOTAL_API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            non_clean_engines = {}
            last_analysis_results = data["data"]["attributes"]["last_analysis_results"]
            for engine, info in last_analysis_results.items():
                if info["result"] not in ["clean", "unrated"]:
                    non_clean_engines[engine] = info["result"]

            return non_clean_engines
        else:
            return None

