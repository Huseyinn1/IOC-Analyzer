# -*- coding: utf-8 -*-
import logging
from ioc_collector.config import settings
import httpx

logger = logging.getLogger(__name__)

# config okunacak
ALIENVAULT_API_KEY = settings.ALIENVAULT_API_KEY
ALIENVAULT_URL = "https://otx.alienvault.com"

async def analyze_ioc_and_save(ioc: str) -> tuple[str, str]:
    """
    Analyze ioc and save them.

    Args:
        ioc: The ioc.
    
    Returns:
        Tags and TLP's
    """
    try:
        api_endpoint = f"{ALIENVAULT_URL}/api/v1/indicators/domain/{ioc}"
        logger.info(f"Sending API request to: {api_endpoint}")

        headers = {"X-OTX-API-KEY": ALIENVAULT_API_KEY}

        async with httpx.AsyncClient() as client:
            response = await client.get(api_endpoint, headers=headers)
            response.raise_for_status()

            threat_info = response.json()
            pulse_info = threat_info.get("pulse_info", {})
            pulses = pulse_info.get("pulses", [])
            tags = set()
            tlps = set()
            for pulse in pulses:
                pulse_tags = pulse.get("tags", [])
                tags.update(pulse_tags)

                tlp = pulse.get("TLP")
                if tlp:
                    tlps.add(tlp)

            return str((tags)), str((tlps))

    except httpx.RequestError as e:
        logger.error(f"AlienVault API isteği başarısız: {e}")
        return None, None
    except Exception as e:
        logger.error(f"Beklenmeyen bir hata oluştu: {e}")
        return None, None
