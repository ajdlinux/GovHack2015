__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .AusPat import AusPatAdapter
from .Trove import TroveAdapter

EXTERNAL_PATENT_EVENT_ADAPTERS = {
    "auspat": AusPatAdapter,
    "trove": TroveAdapter,
}