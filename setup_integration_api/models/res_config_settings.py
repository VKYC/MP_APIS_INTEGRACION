
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    api_first_url = fields.Text(string='Url de API Rin de Gastos')
    api_first_key = fields.Text(string='Key de API Rin de Gastos')
    api_second_url = fields.Text(string='Url de API SII')
    api_second_key = fields.Text(string='Key de API SII')
