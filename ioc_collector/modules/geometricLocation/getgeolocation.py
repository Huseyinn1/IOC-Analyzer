# -*- coding: utf-8 -*-

import httpx
import logging

logger = logging.getLogger(__name__)

async def get_geometric_location(ip):
    """
    Get the geometric location (country, region, city) of an IP address using the ip-api.com service.

    :param ip: The IP address for which to retrieve location information.
    :type ip: str
    :return: A tuple containing the country, region, and city information. If the location cannot be determined,
             None values are returned for each component.
    :rtype: tuple[str, str, str]
    """
    url = f"http://ip-api.com/json/{ip}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                country = data["country"]
                region = data["regionName"]
                city = data["city"]
                return country, region, city
            else:
                return None, None, None
        except Exception as e:
            logger.error(f"Error while getting location data for IP {ip}: {e}")
            return None, None, None


def analyze_url(url):
    domain = url.split("//")[-1].split("/")[0]
    return domain


