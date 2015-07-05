# Patents - a vital tool for innovation, or a way to unfairly crush competitors?
patentstori.es is an exploration tool for exploring the complex and interesting history of the patents behind Australian innovations.

The patent system has a huge impact on Australia's technology industry - it protects some of our best-known inventors and inventions - like the cochlear implant and the cervical cancer vaccine - while sometimes allowing patent trolls to crush new businesses. Given its economic significance, it's important that the Australian public understand their patent system - which isn't easy! The patent process is complex and few people appreciate just how involved it can be. Our aim is to combine the timeline of the patent process with the broader story and history of a particular patent.

patentstori.es aims to change this by visualising the patent process, helping ordinary people to explore the patents that lie behind many inventions. Using the IP Australia Intellectual Property Government Open Data set and the AusPat database, patentstori.es converts masses of patent process data into easily-understood timelines, allowing users to search for patents and see the patent's story.

On top of the patent process data, patentstori.es integrates external sources, such as news articles and images, to present patents in their full context. Relevant articles are automatically retrieved from the National Library of Australia's [Trove database][3]. Users can also add their own annotations - text, links and images - to tell the full story of an invention and inventor.

# Datasets
Our primary source is the [Intellectual Property Government Open Data (IPGOD)][1] dataset, produced by IP Australia. This dataset is one of the most comprehensive datasets ever released by an intellectual property regulator. IPGOD is used to identify patent applications and generate the visual timeline of the patent's application process and history. IPGOD was also used to produce our [statistical analysis][5].

Further information about a particular patent, including its supporting documentation and extract, is extracted from IP Australia's [AusPat database][6].

[Trove][3], a service of the [National Library of Australia](http://nla.gov.au), is used to request images, articles and publications relevant to the patent application, providing the opportunity for users to further explore the particular innovation.

# Future work
patentstori.es can be used as an educational tool to explain the patent system. patentstori.es could also be extended to create an application for coordinating community efforts to strike down invalid patents.

# Who are we?
patentstori.es was developed by [Andrew Donnellan](https://github.com/ajdlinux), [Benjamin Roberts](https://github.com/tsujamin) and Peter Schmidli as part of [GovHack 2015](http://govhack2015.org) Canberra.

# Acknowledgements
patentstori.es is built on a Free Software/Open Source stack:

* [Django](https://djangoproject.com)
* [Python](https://python.org)
* [PostgreSQL](http://www.postgresql.org)
* [MongoDB](https://mongodb.org)
* [nginx](http://nginx.org)
* [CentOS](https://centos.org)
* [Sentry](https://getsentry.com)



[1]: https://data.gov.au/dataset/ntellectual-property-government-open-data-2015
[2]: http://www.ipaustralia.gov.au/uploaded-files/reports/IP_Government_Open_Data_Paper_-_Final.pdf
[3]: http://trove.nla.gov.au/
[4]: http://pericles.ipaustralia.gov.au/ols/auspat/
[5]: /statistics/
[6]: http://pericles.ipaustralia.gov.au/ols/auspat/