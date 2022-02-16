from odoo import models, fields, api, tools
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError
from odoo import tools
import string
from odoo.tools import float_compare


class Accounting (models.Model):
    _name = "accounting.odoo"
    _description = "Accounting info"


name = fields.Char(sting='Title', required=True)
description = fields.Text(string='Description')
level = fields.Selection(string='Level',
                         selection=[('beginner', 'Beginner'),
                                    ('intermediate', 'Intermediate'),
                                    ('advanced', 'Advanced')],
                         copy=False)

active = fields.Boolean(string='active', default=True)
