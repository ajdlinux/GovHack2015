__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .IPGOD101 import IPGOD101Adapter
from .IPGOD107 import IPGOD107Adapter
from .IPGOD108 import IPGOD108Adapter
from .IPGOD109 import IPGOD109Adapter
from .IPGOD121 import IPGOD121Adapter
from .IPGOD122 import IPGOD122Adapter
from .IPGOD125 import IPGOD125Adapter
from .IPGOD127 import IPGOD127Adapter

# Iterable list of event adapters
MONGO_PATENT_EVENT_ADAPTERS = [
    IPGOD101Adapter,
    IPGOD107Adapter,
    IPGOD108Adapter,
    IPGOD109Adapter,
    IPGOD121Adapter,
    IPGOD122Adapter,
    IPGOD125Adapter,
    IPGOD127Adapter,
]