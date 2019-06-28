from abc import ABCMeta

class VCFAssembler(metaclass=ABCMeta):

    VCARD_START =  'BEGIN:VCARD'
    VCARD_END =  'END:VCARD'

    def __init__(self, version, name, **kwargs):
        self.vcf_card = ''
        self.vcf_body = ''
        self.version = version
        self.name = name
        self.phones = kwargs['phones']
        self.email = kwargs['email']
        self.photo = kwargs['photo']

    def add_to_body(self, line):
        self.vcf_body += f'\n{line}'
    
    @classmethod
    def set_review(self):
        pass

    @classmethod
    def set_phone(self):
        pass

    @classmethod
    def set_image(self):
        pass

    def set_version(self):
        if self.version == '2.1':
            self.add_to_body('VERSION:2.1')
        elif self.version == '3.0':
            self.add_to_body('VERSION:3.0')
        else:
            raise 'Invalid Version'

    def set_name(self):
        name = self.name['name']
        surname = self.name['surname']
        treatment = self.name['treatment']

        vcf_name = f'{name};'
        vcf_surname = f'{surname};'
        vcf_treatment = f';{treatment};'
        
        self.add_to_body(f'N:{vcf_surname}{vcf_name}{vcf_treatment}')
        self.add_to_body(f'FN:{surname} {name}')

    def build_vcf_body(self):
        self.set_version()
        self.set_name()
