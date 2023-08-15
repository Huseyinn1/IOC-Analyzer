# -*- coding: utf-8 -*-
import re
from fastapi import FastAPI
from utils.utils import search_and_analyze_Ip,search_and_domain,search_and_analyze_url

app = FastAPI()


@app.post("/search/")
async def check_and_get(ioc: str):
    if ioc.startswith("http://") or ioc.startswith("https://"):
        await search_and_analyze_url(ioc)
    elif is_valid_ip(ioc):
        await search_and_analyze_Ip(ioc)
    else:
        await search_and_domain(ioc)


def is_valid_ip(ioc: str) -> bool:
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    return re.match(ip_pattern, ioc) is not None


