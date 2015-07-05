__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

import requests
from .ExternalAdapter import ExternalAdapter
from ..models import PatentApplication
from requests import Response
from bs4 import BeautifulSoup

AUSPAT_ROOT = "http://pericles.ipaustralia.gov.au/ols/auspat/"

class AusPatAdapter(ExternalAdapter):
    """
    Things I want:
    Invention Title: "title="The Title of the Application""
    Inventor: "title="The person(s) named on the Application as the Inventor""
    Applicant: title="The name of the person(s) or organisation(s) making Application for grant of patent"
    Link to specifications: "li class="publication""
    Link to Extract: "td class="eregister"
    """

    def __init__(self, parent_patent):
        """

        :param parent_patent: parent patent model
        :type parent_patent: PatentApplication
        :return:
        """
        super(AusPatAdapter, self).__init__(parent_patent)
        self.cookies = {"hasAccepted": "true"}
        self.auspat_response = None
        self.fields = None

    def get_response(self):
        #TODO implement caching here
        if self.auspat_response is None:
            self.auspat_response = self.__load_page__()
        return self.auspat_response

    def get_items(self):
        #TODO implement caching here
        if self.fields is None:
            self.fields = AusPatAdapter.__scrape_auspat_response(self.get_response())
        return [self.fields]

    def __load_page__(self):
        """
        Load and cache the webpage to the AusPatAdapter instance
        Page will 200 regardless of whether patent exists, need to check page title.
        :return: Page response or None
        :rtype: str
        """

        if self.patent.australian_appl_no is None:
            return

        req_params={"applicationNo": self.patent.australian_appl_no}

        response = requests.get(AUSPAT_ROOT + "applicationDetails.do", params=req_params, cookies=self.cookies)
        if AusPatAdapter.__check_title_matches__(response, "IP Australia: AusPat Application Details"):
            self.auspat_response = response.text
        else:
            self.auspat_response = None
        return self.auspat_response

    @staticmethod
    def __check_title_matches__(response, expected):
        """
        Check if the title of the page matches the expected value
        :param response: response object
        :type response: Response
        :param expected: expected page title
        :type expected: str
        :return: if response is patent record page
        :rtype: bool
        """
        if not response.ok:
            return False

        # Check for "error" in page title
        resp_root = BeautifulSoup(response.text, "html.parser")
        if resp_root.title.text is None or resp_root.title.text != expected:
            return False

        return True

    @staticmethod
    def __scrape_auspat_response(auspat_response_text):
        """
        Scrape the auspat response for a series of useful fields
        :param auspat_response_text: html text of the auspat patent application page
        :type auspat_response_text: str
        :return: dictionary of fields
        :rtype: dict
        """
        fields = {}

        bs = BeautifulSoup(auspat_response_text, "html.parser")

        # Title of Patent
        title_elem = bs.find(title="The Title of the Application")
        if title_elem is not None:
            fields["title"] = title_elem.parent()[1].text

        # Inventor of Patent
        inventors_elem = bs.find(title="The person(s) named on the Application as the Inventor")
        if inventors_elem is not None:
            fields["inventor"] = []
            #go up a level to find inventor list, skip title elem
            for inventor_elem in inventors_elem.parent()[1:]:
                # Make name more "intimate"
                inventor_name = inventor_elem.text.strip()
                inventor_name = " ".join(reversed(inventor_name.split(", ")))

                fields["inventor"].append(inventor_name)

        # Patent Applicant
        applicant_title_elem = bs.find(
            title="The name of the person(s) or organisation(s) making Application for grant of patent")
        if applicant_title_elem is not None:
            applicant_index = applicant_title_elem.parent().index(applicant_title_elem) + 1
            fields["applicant"] = applicant_title_elem.parent()[applicant_index].text

        # Specifications
        spec_elems = bs.find_all("li", "publication")
        if spec_elems is not None and len(spec_elems) is not 0:
            fields["specifications"] = {}
            for spec_elem in spec_elems:
                url = AUSPAT_ROOT + spec_elem.a["href"][2:]
                fields["specifications"][spec_elem.a.text] = url

        # Extract
        extract_elem = bs.find("td", "eregister")
        if extract_elem is not None:
            fields["extract"] = AUSPAT_ROOT + extract_elem.a["href"][2:]

        return fields