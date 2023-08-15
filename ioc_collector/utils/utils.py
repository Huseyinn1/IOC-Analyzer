# -*- coding: utf-8 -*-
from database.crud import add_analyzed_domain,add_analyzed_IP,add_analyzed_url
from modules.alienvault.alienvault import analyze_ioc_and_save
from modules.blacklist.blacklist import get_blacklist_links
from modules.geometricLocation.getgeolocation import (
    analyze_url,
    get_geometric_location,
)
from modules.IPAdresses.getIPadresses import get_domain_ips
from modules.googlesafe.googlesafe import google_safe_browsing_check
from modules.greynoise.greynoise import analyzed_ip
from modules.virustotal.virustotal import (
    analyzed_virustotal,
    analyzed_virustotal_url,
    virustotal_url,
)
from modules.whoisInfo.whoisInfo import get_whois_info


async def search_and_domain(domain: str):
    first_ip, ips = await get_domain_ips(domain)
    whois_info = await get_whois_info(domain)
    country, region, city = await get_geometric_location(first_ip)
    blacklist = await get_blacklist_links("domain", domain)
    virustotal = await analyzed_virustotal("domains", domain)
    googleSafe = await google_safe_browsing_check(domain)
    tlps, tags = await analyze_ioc_and_save(domain)
    add_analyzed_domain( [domain, ips, country, region, city, whois_info, googleSafe, tlps, tags, blacklist, virustotal])



async def search_and_analyze_Ip(ip):
    country, region, city =  await get_geometric_location(ip)
    blacklist = await get_blacklist_links("ipv4", ip)
    virustotal = await analyzed_virustotal("ip_addresses", ip)
    googleSafe = await google_safe_browsing_check(ip)
    whois_info = await get_whois_info(ip)
    graynoise = await analyzed_ip(ip)
    add_analyzed_IP( [ip, country, region, city, whois_info, googleSafe, blacklist, virustotal, graynoise])


async def search_and_analyze_url(url: str):
    googleSafe = await google_safe_browsing_check(url)
    domain = analyze_url(url)
    first_ip, ips = await get_domain_ips(domain)
    whois_info = await get_whois_info(domain)
    country, region, city = await get_geometric_location(first_ip)
    blacklist = await get_blacklist_links("domain", domain)
    virustotal = await analyzed_virustotal_url(await virustotal_url(url))
    url = url.replace(" ", "")
    add_analyzed_url( [url, domain, ips, country, region, city, whois_info, googleSafe, blacklist, virustotal])
