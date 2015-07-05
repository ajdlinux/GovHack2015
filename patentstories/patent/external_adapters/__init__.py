__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .AusPat import AusPatAdapter

EXTERNAL_PATENT_EVENT_ADAPTERS = {
    "auspat": AusPatAdapter,
}