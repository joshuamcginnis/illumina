#!/usr/bin/env python
import click
from src import FhirToClarityClient

@click.group()
def f2c():
    """HL7 FHIR to Clarity Payload Utility"""

@f2c.command()
@click.option("-i", help="File path to the FHIR order payload.")
def convert(i):
    """Translate a FHIR order message to a Clarity LMS /service
    API POST payload."""
    client = FhirToClarityClient()

    try:
        sample_xml = client.generate_sample_xml_from_fhir_file(i)
        click.echo(sample_xml)
    except FileNotFoundError as e:
        raise click.BadParameter('Input file not found.')

if __name__ == '__main__':
    f2c()
