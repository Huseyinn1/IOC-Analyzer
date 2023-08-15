from pydantic import BaseModel

class AnalyzedDomainSchema(BaseModel):
    domain: str
    ip: str
    country: str
    region: str
    city: str
    whois_info: dict
    googleSafe: str
    tlps: str
    tags: str
    blacklist: str
    virustotal: str

class AnalyzedIPSchema(BaseModel):
    ip: str
    country: str
    region: str
    city: str
    whois_info: dict
    googleSafe: str
    blacklist: str
    virustotal: str
    graynoise: str

class AnalyzedURLSchema(BaseModel):
    url: str
    domain: str
    ip: str
    country: str
    region: str
    city: str
    whois_info: dict
    googleSafe: str
    blacklist: str
    virustotal: str
