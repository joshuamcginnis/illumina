Illumina BaseSpace API Utils
=======
This repo contains some prototype utilities for various Illumina Basespace product APIs.

## Table of Contents
* **Utilities**
  * [FHIR to Clarity Sample XML Translator (F2C)](#fhir-to-clarity-sample-xml)
    * [Basic Usage](#basic-usage)
    * [Running the Examples](#running-the-examples)
    * [How it works](#how-it-works)
* [Project Setup](#project-setup)

# FHIR to Clarity Sample XML
This is the prototype for a utility that allows translation, translation and connection of raw HL7 data to third-party data sources such as Epic.

## Basic Usage
```sh
$ python f2c.py --help
Usage: f2c.py [OPTIONS] COMMAND [ARGS]...

  HL7 FHIR to Clarity Payload Utility

Options:
  --help  Show this message and exit.

Commands:
  convert  Translate a FHIR order message to a Clarity LMS /service API...
```

Save a local FHIR SampleRequest xml and pass it's path to the app.
```bash
python f2c.py convert -i path/to/file.xml
```

### Running the Examples
Several example ServiceRequest xml's are available for testing in [examples](/examples). You can run them like so:
```bash
$ python f2c.py convert -i examples/fhir/servicerequest-genetics.xml

<?xml version="1.0" ?>
<smp:samplecreation xmlns:smp="http://genologics.com/ri/sample"
                    xmlns:udf="http://genologics.com/ri/userdefined">
    <name>ABCB4 gene mutation analysis</name>
    <project uri="http://localhost:8080/api/v2/projects/ADM243"/>
    <location>
        <container uri="http://localhost:8080/api/v2/containers/27-100001"/>
        <value>1:1</value>
    </location>
    <date-received>2022-08-23 14:42:46.052753</date-received>
    <udf:field name="request_id">genetics-example-1</udf:field>
    <udf:field name="intent">original-order</udf:field>
    <udf:field name="subject">Patient/example</udf:field>
    <udf:field name="coding_system">http://loinc.org</udf:field>
    <udf:field name="code">49874-1</udf:field>
</smp:samplecreation>
```

### How it Works
Per the most current [Hl7 FHIR standards](http://hl7.org/fhir/), _orders_ are constructed primarily as `<ServiceRequest>` objects (with the exception of `<MedicationRequest>` not currently supported). Previous standards defined an `<Order>`, but this has since been removed and replaced.

> ServiceRequest is a record of a proposal/plan or order for a service to be performed that would result in a Procedure, Observation, DiagnosticReport, ImagingStudy or similar resource.

For now, this project only supports mapping `<ServiceRequests`> to Clarity Sample creation xml, but is designed to support future mappings between FHIR elements and Clarity LMS xml requests.

**FHIR Maps**

FHIR maps are python objects which map `<ServiceRequest>` objects to python objects via xpath.

See: [src\fhir_maps\service_request_map.py](src\fhir_maps\service_request_map.py)

These maps are composable and can be used to construct and confine mappings with strict types between FHIR elements to pythonic objects.

**Clarity XML Builder**

See: [src\clarity_xml_builder.py](src\clarity_xml_builder.py)
This is the main class for building the sample request xml by mapping the fields defined in FHIR Maps to the Clarity LMS Service creation fields.

## Project Setup
### Requirements
* [Conda](https://docs.conda.io/en/latest/miniconda.html) (or virtualenv)
* Python 3+

### Recreate the python environment and install deps:
  
  ```sh
  $ conda env create -f * environment.yml
  ```

## Helpful links
* [Clarity LMS Sample API documentation](https://d10e8rzir0haj8.cloudfront.net/6.0/data_smp.html#artifact)
* [HL7 FHIR Documentation](http://hl7.org/fhir/)
* [FHIR at EPIC](https://fhir.epic.com/)