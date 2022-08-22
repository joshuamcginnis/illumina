#!/usr/bin/env python
import click
from os.path import exists
import xml.etree.ElementTree as ET

class F2C:
    def __init__(self, fhir_input_file):
        print('hi')
        if not exists(fhir_input_file):
            raise click.BadParameter('Input file not found. Check the path.')

        print(fhir_input_file)

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
