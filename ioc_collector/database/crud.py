# -*- coding: utf-8 -*-
from database.database import SessionLocal
from models.models import AnalyzedDOMAIN,AnalyzedIP,AnalyzedURL


def add_analyzed_domain(domain_data):
    session = SessionLocal()
    domain = AnalyzedDOMAIN(
        domain=domain_data[0],
        ip=domain_data[1],
        country=domain_data[2],
        region=domain_data[3],
        city=domain_data[4],
        whois_info=domain_data[5],
        googleSafe=domain_data[6],
        tlps=domain_data[7],
        tags=domain_data[8],
        blacklist=domain_data[9],
        virustotal=domain_data[10],
    )
    session.add(domain)
    session.commit()
    session.close()


def add_analyzed_IP(ip_data):
    session = SessionLocal()
    ip = AnalyzedIP(
        ip=ip_data[0],
        country=ip_data[1],
        region=ip_data[2],
        city=ip_data[3],
        whois_info=ip_data[4],
        googleSafe=ip_data[5],
        blacklist=ip_data[6],
        virustotal=ip_data[7],
        graynoise=ip_data[8],
    )
    session.add(ip)
    session.commit()
    session.close()

def add_analyzed_url(url_data):
    session = SessionLocal()
    url = AnalyzedURL(
        url=url_data[0],
        domain=url_data[1],
        ip=url_data[2],
        country=url_data[3],
        region=url_data[4],
        city=url_data[5],
        whois_info=url_data[6],
        googleSafe=url_data[7],
        blacklist=url_data[8],
        virustotal=url_data[9],
    )
    session.add(url)
    session.commit()
    session.close()
