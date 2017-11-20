"""
    This scritp assembles and compile a new VCF file
"""

from time import gmtime, strftime

from imgprocessor import encodeImage

class ContactAssembler():
    def __init__(self):
        self.version = ''
        self.surname = ''
        self.name = ''
        self.treatment = ''
        self.final_name = ''
        self.phone_type = ''
        self.phone_num = ''
        self.adress_type = ''
        self.adress_adress = ''
        self.adress_city = ''
        self.adress_state = ''
        self.adress_zip = ''
        self.adress_country = ''
        self.photo = ''
        self.email = ''
        self.bday = ''
        self.work_org = ''
        self.work_title = ''
        self.rev = ''
        self.template = 'BEGIN:VCARD'
        self.template_end = 'END:VCARD'

    def addTemplate(self, string, br=True):
        if br is True:
            self.template += '\n'
        
        self.template += string
        
    def endTemplate(self):
        self.addTemplate(self.template_end)

    def addVer(self, version):
        self.version = version

        template_ver = f'VERSION:{version}'
        self.addTemplate(template_ver)
    
    def createRev(self):
        if self.version == '2.1':
            review = strftime("%Y%m%dT%H%M%SZ", gmtime())
        elif self.version == '3.0':
            review = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
        else:
            review = '00000000T000000Z'
        
        self.rev = review
        
        template_rev = f'REV:{review}'
        self.addTemplate(template_rev)

    def createName(self, name, surname, treatment):
        if treatment == '':
            treatment = 'Mr.'

        self.surname = surname
        self.name = name
        self.treatment = treatment

        template_n = f'N:{surname};{name};;{treatment}'
        template_fn = f'FN:{name} {surname}'
        self.addTemplate(template_n)
        self.addTemplate(template_fn)

    def createPhone(self, p_type, p_number):
        if p_type == '':
            p_type = 'HOME'
        
        self.phone_type == p_type
        self.phone_num == p_number

        if self.version == '2.1':
            template_phone = f'TEL;{p_type};VOICE:{p_number}'
        elif self.version == '3.0':
            template_phone = f'TEL;TYPE={p_type},VOICE:{p_number}'
        
        self.addTemplate(template_phone)

    def createAdress(self, a_type, a_adress, a_city, a_state, a_zipcode, a_country):
        if a_type == '':
            a_type = 'HOME'

        self.adress_type = a_type
        self.adress_adress = a_adress
        self.adress_city = a_city
        self.adress_state = a_state
        self.adress_zip = a_zipcode
        self.adress_country = a_country

        if self.version == '2.1':
            template_adress = f'ADR;{a_type}:;;{a_adress};{a_city};{a_state};{a_zipcode};{a_country}'
        elif self.version == '3.0':
            template_adress = f'ADR;TYPE={a_type}:;;{a_adress};{a_city};{a_state};{a_zipcode};{a_country}'
        
        self.addTemplate(template_adress)

    def createImg(self, img_location):
        data_b64 = encodeImage(img_location)

        template_photo = f'PHOTO;JPEG;ENCODING=BASE64:{data_b64}'

        self.addTemplate(template_photo)


#TESTS
if __name__ == '__main__':
    a = ContactAssembler()
    a.addVer('3.0')
    a.createName('Leonardo', 'Isso Blah', 'Dr.')
    a.createPhone('CELL', '04111912345678')
    a.createAdress('HOME', 'R. dos Bobos 0', 'Sao Paulo', 'SP', '22222-222', 'Brazil')
    a.createAdress('WORK', 'R. do Arouche 666', 'Sao Paulo', 'SP', '22222-666', 'Brazil')
    a.createImg('test_img.png')
    a.createRev()
    a.endTemplate()

    #GET ALL CLASS VARS
    #members = [getattr(a, attr) for attr in dir(a) if not callable(getattr(a,attr)) and not attr.startswith("__")]
    #for var in members:
    #    print('\n' + var) 

    with open('log.txt', 'w+') as file:
        file.write(a.template)
