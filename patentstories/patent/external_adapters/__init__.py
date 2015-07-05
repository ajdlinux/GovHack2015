__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from collections import OrderedDict
from .AusPat import AusPatAdapter
from .Trove import TroveAdapter

EXTERNAL_PATENT_EVENT_ADAPTERS = OrderedDict([
    ('auspat', AusPatAdapter),
    ('trove', TroveAdapter),
])
