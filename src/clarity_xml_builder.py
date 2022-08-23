import datetime

class ClarityXMLBuilder:
    def __init__(self, fhir_map):
        self.fhir_map = fhir_map

    def build_sample_xml(self):
        xml = []
        xml.append('<smp:samplecreation xmlns:smp="http://genologics.com/ri/sample" xmlns:udf="http://genologics.com/ri/userdefined">')
        xml.append("<name>%s</name>" % self.sample_name())
        xml.append(self.__static_project())
        xml.append(self.__static_location())
        xml.append("<date-received>%s</date-received>" % self.date_received())
        xml.append(self.__udf('request_id', self.fhir_map.request_id))
        xml.append(self.__udf('intent', self.fhir_map.intent))
        xml.append(self.__udf('subject', self.fhir_map.subject))
        xml.append(self.__udf('coding_system', self.fhir_map.coding_system))
        xml.append(self.__udf('code', self.fhir_map.code))

        xml.append('</smp:samplecreation>')

        return ''.join(xml)

    def __udf(self, name, value):
        return "<udf:field name=\"%s\">%s</udf:field>" % (name, value)

    def date_received(self):
        if self.fhir_map.authored_on is not None:
            return self.fhir_map.authored_on

        return datetime.datetime.now()

    def sample_name(self):
        if self.fhir_map.code_display is not None:
            return self.fhir_map.code_display

        return self.fhir_map.code_text

    def __static_location(self):
        """Returns a staticly set location for testing."""
        return '<location><container ' \
                'uri="http://localhost:8080/api/v2/containers/27-100001">' \
                '</container><value>1:1</value></location>'

    def __static_project(self):
        """Returns a staticly set project for testing."""
        return '<project uri="http://localhost:8080/api/v2/' \
                'projects/ADM243"></project>'

