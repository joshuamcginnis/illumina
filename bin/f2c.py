#!/usr/bin/env python
import click
from os.path import exists
from xml.dom.minidom import parse, parseString

class ClarityXMLBuilder:
    def __init__(self):
        pass

    def create_sample_xml(self, sample_dict):
        xml = []
        xml.append('<smp:samplecreation xmlns:smp="http://genologics.com/ri/sample">')
        xml.append("<name>%s</name>" % sample_dict)
        xml.append(self.__static_project())
        xml.append(self.__static_location())
        xml.append('</smp:samplecreation>')

        return ''.join(xml)

    def __static_location(self):
        """Returns a staticly set location for testing."""
        return '<location><container ' \
                'uri="http://localhost:8080/api/v2/containers/27-100001">' \
                '</container><value>1:1</value></location>'

    def __static_project(self):
        """Returns a staticly set project for testing."""
        return '<project uri="http://localhost:8080/api/v2/' \
                'projects/ADM243"></project>'

class F2C:
    def __init__(self, fhir_input_file):
        if not exists(fhir_input_file):
            raise click.BadParameter('Input file not found. Check the path.')

        sample_name = self.sample_name_from_fhir_order(fhir_input_file)

        clarity_xml_builder = ClarityXMLBuilder()
        sample_xml = clarity_xml_builder.create_sample_xml(sample_name)
        self.__pretty_print_xml(sample_xml)

    def __pretty_print_xml(self, xml):
        dom = parseString(xml)
        click.echo(dom.toprettyxml())

    def sample_name_from_fhir_order(self, fhir_input_file):
        with open(fhir_input_file, 'r', encoding='utf-8') as file:
            parsed_xml = parse(file)

        id_element = parsed_xml.getElementsByTagName('id')[0]
        id_value = id_element.getAttribute('value')

        detail_element = parsed_xml.getElementsByTagName('detail')[0]
        reference_element = detail_element.getElementsByTagName('reference')[0]
        reference_value = reference_element.getAttribute('value')

        return ''.join([id_value, ':', reference_value])

@click.group()
def f2c():
    """HL7 FHIR to Clarity Payload Utility"""

@f2c.command()
@click.option("--i", help="File path to the FHIR order payload.")
def convert(i):
    """Translate a FHIR order message to a Clarity LMS /service
    API POST payload."""
    F2C(i)

if __name__ == '__main__':
    f2c()
