from assembler.VCFAssembler import VCFAssembler
from image_encoder.image_encoder import encode_image_file

from time import gmtime, strftime

class VCFAssembler2(VCFAssembler):

    def __init__(self, name, phones=None, email=None, image=None):
      super().__init__(name, phones, email, image)
      self.version = '3.0'

    def set_review(self):
        self.revision = strftime("%Y%m%dT%H%M%SZ", gmtime())
        vcf_revision = f'REV:{self.revision}'
        self.add_to_body(vcf_revision)

    def set_phones(self):
        for phone in self.phones:
            phone_type = phone['type']
            phone_number = phone['number']
            vcf_phone = f'TEL;{phone_type};VOICE:{phone_number}'
            self.add_to_body(vcf_phone)

    def set_image(self):
        image = encode_image_file(self.image)
        vcf_image = f'PHOTO;JPEG;ENCODING=BASE64:{image}'
        self.add_to_body(vcf_image)
