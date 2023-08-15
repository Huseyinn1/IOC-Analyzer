import os
import httpx
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
VIRUS_TOTAL_URL = "https://www.virustotal.com"
HEADERS = {"x-apikey": VIRUSTOTAL_API_KEY}


async def get_domain_ips(domain:str) -> tuple:
    """
    Get IP addresses associated with a domain using VirusTotal API.

    Args:
        domain (str): The domain for which to retrieve IP addresses.

    Returns:
        tuple: A tuple containing the first IP address and a string representation
               of the list of IP addresses associated with the domain.
               If the request fails or no IP addresses are found, returns (None, None).
    """
    url = f"{VIRUS_TOTAL_URL}/api/v3/domains/{domain}/resolutions"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        result = []

        if response.status_code == 200:
            data = response.json()
            ips = [entry["attributes"]["ip_address"] for entry in data["data"]]
            first_ip = ips[0] if ips else None
            result.append({"first_ip": first_ip, "ip_list": ips})
            logger.info("Success to get IP addresses")
            return first_ip, str(ips)
        else:
            logger.info("Failed to get IP addresses")
            return None, None

