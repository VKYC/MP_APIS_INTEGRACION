
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    api_first_url = fields.Text(string='Url la url de API 1')
    api_first_key = fields.Text(string='Url la key de API 1')
    api_second_url = fields.Text(string='Url la url de API 2')
    api_second_key = fields.Text(string='Url la key de API 2')
