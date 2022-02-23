from odoo import models, fields, api
from odoo.exceptions import UserError


class SchoolProfile (models.Model):
    _name = "school.profile"
    _description = "Showing users profile"

    name = fields.Char(string="school name")
    email = fields.Char(string="email")
    phone = fields.Char("phone")
