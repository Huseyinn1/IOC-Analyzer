# -*- coding: utf-8 -*-

import os
import httpx
import logging
import json
import asyncio
from typing import Union
from dotenv import load_dotenv

load_dotenv()
GREY_NOISE_KEY = os.getenv("GREY_NOISE_KEY")
GREY_NOISE_URL = "https://api.greynoise.io/v3/community"
headers = {"accept": "application/json", "key": GREY_NOISE_KEY}

logger = logging.getLogger(__name__)
  

async def analyzed_ip(ip)  -> Union[dict, None]:
    """
     Retrieve IP analysis from GreyNoise Community API.

    Args:
        ip (str): IP address to analyze.

    Returns:
        dict or None: Analysis information from the GreyNoise API,
        or None if response status is not 200.
    """
    url = f"{GREY_NOISE_URL}/{ip}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            logger.info(f"Analysis result forx IP {ip}: {data}")
            return data
        else:
            logger.warning(f"No analysis resultx available for IP {ip}")
            return None
