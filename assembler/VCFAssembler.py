from abc import ABCMeta

class VCFAssembler(metaclass=ABCMeta):

    VCARD_START =  'BEGIN:VCARD'
    VCARD_END =  'END:VCARD'

    def __init__(self, name, phones=None, email=None, image=None):
        self.vcf_card = ''
        self.vcf_body = ''
        self.name = name
        self.phones = phones
        self.email = email
        self.image = image
        self.version = '3.0'
        self.revision = None

    def add_to_body(self, line, break_line=True):
        if break_line:
            self.vcf_body += '\n'
        self.vcf_body += f'{line}'
    
    @classmethod
    def set_review(self):
        pass

    @classmethod
    def set_phones(self):
        pass

    @classmethod
    def set_image(self):
        pass

    def set_version(self):
        vcf_version = f'VERSION:{self.version}'
        self.add_to_body(vcf_version)

    def set_name(self):
        name = self.name['name']
        surname = self.name['surname']
        treatment = self.name['treatment']

        vcf_name = f'{name};'
        vcf_surname = f'{surname};'
        vcf_treatment = f';{treatment};'
        
        self.add_to_body(f'N:{vcf_surname}{vcf_name}{vcf_treatment}')
        self.add_to_body(f'FN:{surname} {name}')

    def set_email(self):
        email = self.email
        self.add_to_body(f'EMAIL:{email}')

    def build_vcf_body(self):
        self.add_to_body(self.VCARD_START, False)
        self.set_version()
        self.set_name()

        if self.email:
            self.set_email()
        
        if self.phones:
            self.set_phones()
        
        if self.image:
            self.set_image()
        
        self.set_review()
        self.add_to_body(self.VCARD_END)
        