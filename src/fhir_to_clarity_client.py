from os import path
from xml.dom.minidom import parse, parseString
from eulxml import xmlmap
from .fhir_maps import ServiceRequestMap
from .clarity_xml_builder import ClarityXMLBuilder

class FhirToClarityClient:
    def __init__(self):
        pass

    def generate_sample_xml_from_fhir_file(self, fhir_input_file):
        if not path.exists(fhir_input_file):
            raise FileNotFoundError

        service_request_map = self.__map_file_to_fhir_map(fhir_input_file)

        clarity_lms_client = ClarityXMLBuilder(service_request_map)
        sample_request_xml = clarity_lms_client.build_sample_xml()

        return self.__pretty_print_xml(sample_request_xml)

    def __map_file_to_fhir_map(self, fhir_input_file):
        return xmlmap.load_xmlobject_from_file(
                fhir_input_file, xmlclass=ServiceRequestMap)

    def __pretty_print_xml(self, xml):
        dom = parseString(xml)
        return dom.toprettyxml()

    def sample_name_from_fhir_order(self, fhir_input_file):
        with open(fhir_input_file, 'r', encoding='utf-8') as file:
            parsed_xml = parse(file)

        id_element = parsed_xml.getElementsByTagName('id')[0]
        id_value = id_element.getAttribute('value')

        detail_element = parsed_xml.getElementsByTagName('detail')[0]
        reference_element = detail_element.getElementsByTagName('reference')[0]
        reference_value = reference_element.getAttribute('value')

        return ''.join([id_value, ':', reference_value])
