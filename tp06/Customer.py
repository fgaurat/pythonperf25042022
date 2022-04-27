

from dataclasses import dataclass
from xml.sax.handler import property_dom_node


@dataclass
class Customer:
    id:int=0
    first_name:str=""
    last_name:str=""
    email:str=""
    gender:str=""
    ip_address:str=""
    done:str=""

