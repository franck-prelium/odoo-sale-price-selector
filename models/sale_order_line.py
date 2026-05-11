from odoo import models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def action_open_price_selector(self):
        self.ensure_one()
        wizard = self.env['sale.price.selector'].create({
            'sale_line_id': self.id,
        })
        return {
            'name': 'Sélectionner le type de prix',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.price.selector',
            'res_id': wizard.id,
            'view_mode': 'form',
            'target': 'new',
        }
