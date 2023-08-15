# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class AnalyzedDOMAIN(Base):
    __tablename__ = "analyzed_domains"

    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String, index=True)
    ip = Column(String)
    country = Column(String)
    region = Column(String)
    city = Column(String)
    whois_info = Column(JSON)
    googleSafe = Column(String)
    tlps = Column(String)
    tags = Column(String)
    blacklist = Column(String)
    virustotal = Column(JSON)

class AnalyzedIP(Base):
    __tablename__ = "analyzed_ips"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True)
    country = Column(String)
    region = Column(String)
    city = Column(String)
    whois_info = Column(JSON)
    googleSafe = Column(String)
    blacklist = Column(String)
    virustotal = Column(JSON)
    graynoise = Column(JSON)

class AnalyzedURL(Base):
    __tablename__ = "analyzed_urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    domain = Column(String)
    ip = Column(String)
    country = Column(String)
    region = Column(String)
    city = Column(String)
    whois_info = Column(JSON)
    googleSafe = Column(String)
    blacklist = Column(String)
    virustotal = Column(JSON)
