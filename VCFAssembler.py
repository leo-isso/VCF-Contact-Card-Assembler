"""
    This scritp assembles and compile a new VCF file
"""

import datetime

class VCF():
    def __init__(self):
        self.version = ''
        self.surname = ''
        self.name = ''
        self.treatment = ''
        self.final_name = ''
        self.phone_type = ''
        self.phone_num = ''
        self.adress_type = ''
        self.adress_local = ''
        self.photo = ''
        self.email = ''
        self.bday = ''
        self.work_org = ''
        self.work_title = ''
        self.rev = ''

    def createRev(self):
        review = datetime.datetime.now()
        self.rev = review
        return review
