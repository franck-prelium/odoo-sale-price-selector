from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    price_special = fields.Float(
        string='Prix spécial',
        digits='Product Price',
        help='Prix spécial sélectionnable sur les lignes de devis.',
    )
