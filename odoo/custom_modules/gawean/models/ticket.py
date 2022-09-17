# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date, datetime
# from email.policy import default
from odoo import models, fields # Mandatory
from dateutil.relativedelta import relativedelta
import re


class Ticket(models.Model):
    _name = 'gawean.ticket' # name_of_module.name_of_class 
    _description = 'Ticket Gawean' # Some note of table

    # Header
    name = fields.Char('Name', compute='_set_name', store=True)
    last_name = fields.Char('Last Name')
    first_name = fields.Char('First Name')
    in_crawl = fields.Boolean('In Crawl')
    out_of_office = fields.Boolean('Out of Office')
    lgbtq = fields.Boolean('LGBTQ')

    gender = fields.Selection([ ('m', 'Male'), ('f', 'Female') ], 'Gender')
    gender_pronouns = fields.Selection([('She/Her/Hers', 'She/Her/Hers'), ('He/Him/His', 'He/Him/His'), 
                                      ('They/Them/Theirs', 'They/Them/Theirs'), ('Not Listed', 'Not Listed')], 'Gender Pronouns')

    
    street = fields.Char('Street')
    apt_no = fields.Char('Apt/Suite No')
    city = fields.Char('City')
    zip_code = fields.Char('Zip')
    email = fields.Char('Email')
    cell_phone = fields.Char('Cell #')
    other = fields.Char('Other #')

    trained_for = fields.Selection([('WeCounsel', 'WeCounsel'), ('Couples/Family', 'Couples/Family'),
                                    ('Group', 'Group'), ('Psychiatry', 'Psychiatry')], 'Trained For')

    departments = fields.Selection([('Administration', 'Administration'), ('Counselors', 'Counselors'),
                                    ('Directors', 'Directors'), ('Front Desk', 'Front Desk'),
                                    ('Psychiatry', 'Psychiatry'), ('Coordinators', 'Coordinators')], 'Department')

    ethnicity = fields.Selection([('American Indian/Native American/Alaskan Native', 'American Indian/Native American/Alaskan Native'),
                                ('Asian', 'Asian'), ('Black', 'Black'), ('Latina/o/x', 'Latina/o/x'),
                                ('Middle Eastern or North African','Middle Eastern or North African'), ('Mixed','Mixed'), 
                                ('Native Hawaiian or Pacific Islander','Native Hawaiian or Pacific Islander'), 
                                ('White','White'), ('Other','Other'), ('Declines to Specify','Declines to Specify')], 'Ethnicity')

    language = fields.Char('Language')
    created_on = fields.Datetime("Date")
    

    @api.depends('last_name', 'first_name')
    def _set_name(self):
        last_name = ""
        if self.last_name:
            last_name = str(self.last_name)
        
        first_name = ""
        if self.first_name:
            first_name = str(self.first_name)

        self.name = first_name + ", " + last_name

    