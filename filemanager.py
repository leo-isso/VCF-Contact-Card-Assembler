"""
    This script manage saving and reading files
"""

import os

import template

FILELOCATION = 'vcf_files'
FILENAME = 'contacts'
FILEEXT = '.vcf'

def checkFileLocation(vcf_filelocation):
    if os.path.exists(vcf_filelocation):
        return True
    else:
        return False

def createFileLocation(vcf_filelocation=None):
    if vcf_filelocation is None:
        vcf_filelocation = FILELOCATION

    if checkFileLocation(vcf_filelocation) is True:
        pass
    elif checkFileLocation(vcf_filelocation) is False:
        os.makedirs(vcf_filelocation)

def genFileString(vcf_filelocation=None, vcf_filename=None):
    if vcf_filelocation is None:
        vcf_filelocation = FILELOCATION
    
    if vcf_filename is None:
        vcf_filename = FILENAME
    
    if vcf_filelocation == '':
        file_string = vcf_filename + FILEEXT
        return file_string
    else:
        file_string = vcf_filelocation + '/' + vcf_filename + FILEEXT
        return file_string

def saveVCF(vcf_filelocation=None, vcf_filename=None):

    file_string = genFileString(vcf_filelocation, vcf_filename)
    createFileLocation(vcf_filelocation)
    
    file_manage = open(file_string, 'w')
    file_manage.write(template.TEMPLATE_TESTE)
    file_manage.close()

def readStringVCF(vcf_filelocation=None, vcf_filename=None):
    
    file_string = genFileString(vcf_filelocation, vcf_filename)

    try:
        file_manage = open(file_string, 'r')
    except FileNotFoundError as e:
        print('Something went wrong, check if file exists')
        pass

    file_string = file_manage.read()
    file_manage.close()
    
    return file_string

if __name__ == '__main__':
    readStringVCF()
