from abc import ABCMeta

class VCFAssembler(metaclass=ABCMeta):

    VCARD_START =  'BEGIN:VCARD'
    VCARD_END =  'END:VCARD'

    def __init__(self, version, name, **kwargs):
        self.vcf_card = ''
        self.vcf_body = ''
        self.version = version
        self.name = name
        self.treatment = kwargs['treatment']
        self.phones = kwargs['phones']
        self.email = kwargs['email']
        self.photo = kwargs['photo']

    def add_to_body(self, line):
        self.vcf_body += f'\n{line}'

    def set_version(self):
        if self.version == '2.1':
            self.add_to_body('VERSION:2.1')
        elif self.version == '3.0':
            self.add_to_body('VERSION:3.0')
        else:
          raise 'Invalid Version'