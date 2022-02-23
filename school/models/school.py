from odoo import models, fields, api


class SchoolProfile (models.Model):
    _name = "school.profile"
    _description = "Showing users profile"

    name = fields.Char(string="School Name")
    email = fields.Char(string="Email")
    phone = fields.Char("Phone")
