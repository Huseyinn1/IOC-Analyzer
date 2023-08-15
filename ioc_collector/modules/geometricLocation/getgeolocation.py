# -*- coding: utf-8 -*-

import httpx
import logging
from bs4 import BeautifulSoup

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


def get_url_data(url):
    response = httpx.get(url, verify=False)
    if response.status_code == 200:
        return response.text
    else:
        return None





# Dosya indirme bağlantılarını bulan fonksiyon
def find_download_links(url_data):
    if url_data is None:
        return []

    soup = BeautifulSoup(url_data, "html.parser")
    download_links = [
        a["href"]
        for a in soup.find_all("a", href=True)
        if a["href"].endswith((".exe", ".msi", ".zip", ".rar"))
    ]
    return download_links


# Dosya indirme bağlantılarının izin kontrolleri
def check_download_links(download_links):
    safe_links = []
    for link in download_links:
        response = httpx.head(link)
        if response.status_code == 200:
            safe_links.append(link)
    return safe_links


