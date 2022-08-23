from eulxml import xmlmap

class ServiceRequestMap(xmlmap.XmlObject):
    ROOT_NS = 'http://hl7.org/fhir'
    ROOT_NAME = 'servicerequest'
    ROOT_NAMESPACES = {
        'sr': ROOT_NS,
        'xml': 'http://www.w3.org/XML/1998/namespace'
    }

    text = xmlmap.StringField('sr:text')

    request_id = xmlmap.StringField('sr:id/@value', required=True)
    intent = xmlmap.StringField('sr:intent/@value', required=True)
    priority = xmlmap.StringField('sr:priority/@value')

    coding_system = xmlmap.StringField('sr:code/sr:coding/sr:system/@value')
    code = xmlmap.StringField('sr:code/sr:coding/sr:code/@value')
    code_text = xmlmap.StringField('sr:code/sr:text/@value')
    code_display = xmlmap.StringField('sr:code/sr:coding/sr:display/@value')

    subject = xmlmap.StringField('sr:subject/sr:reference/@value')
    requester = xmlmap.StringField('sr:requester/sr:reference/@value')

    authored_on = xmlmap.fields.StringField('sr:authoredOn/@value')
    occurrence_date = xmlmap.fields.StringField('sr:occurrenceDateTime/@value')
