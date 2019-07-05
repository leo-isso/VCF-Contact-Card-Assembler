# VCF Contact Card assembler

Create V-Cards content using Python.

Supports V-Cards `2.1` and `3.0`.

The V-Cards can be generated in its default versions `3.0` and `2.1`.

Creating an V-Card:
```python
name = {'name': 'John', 'surname': 'Wick', treatment='Mr.'}
phones = [
    {'type': 'WORK', 'number': '080012345678'},
    {'type': 'HOME', 'number': '12345678'},  
  ]
email = 'mr_john@email.com'

vcard = VCFAssembler2(name, phones, email).build_vcf_body()

print(vcard.vcf_body)
```

### Work in Progress (release 2.0.0):
- [ ] Code documentation
- [ ] CHANGELOG
- [ ] MD documentation


### TODO Features:
- [ ] Adresses 
- [ ] Birthdays 
- [ ] Work/Organization 
- [ ] Support V-Card 4.0
- [ ] Output .vcf file

### About the Project :
A long time ago I came up with this project because I wanted to make my mobile's agenda migration easier, and I also wanted to practice Python, after all I love programming and Python! I ended up with another unfinished project.

Now I'm reviving this Project, because I want to practice some soft and hard skills, such as unnit testing, OOP and resilience. And this project is kinda cool. 

I hope it inspires or helps someone!