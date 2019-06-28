from abc import ABCMeta

class VCFAssembler(metaclass=ABCMeta):

    VCARD_START =  'BEGIN:VCARD'
    VCARD_END =  'END:VCARD'

    def __init__(self, name, **kwargs):
        self.vcf_card = ''
        self.vcf_body = ''
        self.name = name
        self.treatment = kwargs['treatment']
        self.phones = kwargs['phones']
        self.email = kwargs['email']
        self.photo = kwargs['photo']

    def add_to_body(self, line):
        self.vcf_body += f'\n{line}'

    def set_name(self):
        vcf_name = ''
        pass