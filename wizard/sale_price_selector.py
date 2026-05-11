from odoo import api, fields, models


class SalePriceSelector(models.TransientModel):
    _name = 'sale.price.selector'
    _description = 'Sélecteur de type de prix'

    sale_line_id = fields.Many2one('sale.order.line', required=True, ondelete='cascade')
    product_id = fields.Many2one(related='sale_line_id.product_id', string='Produit', readonly=True)

    price_catalogue = fields.Float(string='Prix catalogue', compute='_compute_prices', digits='Product Price')
    price_special = fields.Float(string='Prix spécial', compute='_compute_prices', digits='Product Price')
    price_standard = fields.Float(string='Prix standard', compute='_compute_prices', digits='Product Price')
    price_partner = fields.Float(string='Prix partenaire', compute='_compute_prices', digits='Product Price')

    price_type = fields.Selection(
        selection=[
            ('catalogue', 'Prix catalogue'),
            ('special', 'Prix spécial'),
            ('standard', 'Prix standard'),
            ('partner', 'Prix partenaire'),
            ('manual', 'Prix manuel'),
        ],
        string='Type de prix',
        default='partner',
        required=True,
    )
    manual_price = fields.Float(string='Prix manuel', digits='Product Price')

    @api.depends('sale_line_id')
    def _compute_prices(self):
        for rec in self:
            line = rec.sale_line_id
            product = line.product_id
            if not product:
                rec.price_catalogue = rec.price_special = rec.price_standard = rec.price_partner = 0.0
                continue

            rec.price_catalogue = product.lst_price
            rec.price_special = product.price_special
            rec.price_standard = product.standard_price

            order = line.order_id
            pricelist = order.pricelist_id
            if pricelist:
                rec.price_partner = pricelist._get_product_price(
                    product,
                    line.product_uom_qty or 1.0,
                    currency=order.currency_id,
                    date=order.date_order or fields.Date.today(),
                )
            else:
                rec.price_partner = product.lst_price

    def action_apply(self):
        self.ensure_one()
        price_map = {
            'catalogue': self.price_catalogue,
            'special': self.price_special,
            'standard': self.price_standard,
            'partner': self.price_partner,
            'manual': self.manual_price,
        }
        self.sale_line_id.price_unit = price_map[self.price_type]
        return {'type': 'ir.actions.act_window_close'}
