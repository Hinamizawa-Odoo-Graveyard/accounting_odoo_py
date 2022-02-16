from odoo import models, fields, api


class Accounting (models.Model):
    _name = "accounting.odoo"
    _description = 'Accounting info'


name = fields.Char(sting='Title', required=True)
description = fields.Text(string='Description')
level = fields.Selection(string='Level',
                         selection=[('beginner', 'Beginner'),
                                    ('intermediate', 'Intermediate'),
                                    ('advanced', 'Advanced')],
                         copy=False)

active = fields.Boolean(string='active', default=True)
