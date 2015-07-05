#Intellectual Property Government Open Data (IPGOD) Statistics

The IPGOD dataset provided by IP Australia [[1]] contains over 10 million entries detailing the life and states of Australian Patents. This dataset took over 2 hours to import and uses a staggering __20 gigabytes__ of disk space on our sever; the equivalent of 15,000 minutes of audio! Focusing on the __patents__ section of the dataset, we've crunched the numbers on some interesting statistics.

# Top Patent Filing Countries

Using the more recent IPGOD101 dataset [[2]], we've identified patents filed from as many as 162 different countries. The top 3 Australian patent filing counties are:

  1. The United States of America: 133,806 patents
  2. Australia: 115,572 patents
  3. Japan: 20498 patents

# Current Status of Australian Patents

There are many different states a patent application can be in. Using the IPGOD101 dataset [[2]] we've graphed the distribution of patent lifecycle stages.

![Distribution of Patent Applications in Database](/static/Statuscount.png)


# Time Series of "Open to Public Inspection" Publications

Finally we have generated a time series graph of OPI publications listed in the IPGOD datasets.

![Patent Publication Time Series](/static/OPpubcount.png)

[1]: https://data.gov.au/dataset/ntellectual-property-government-open-data-2015
[2]: https://data.gov.au/dataset/ntellectual-property-government-open-data-2015/resource/fb0078f3-c164-4d95-b1fd-e72d5d6d2324?inner_span=True
