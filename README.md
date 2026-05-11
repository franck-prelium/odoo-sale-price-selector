# Odoo Sale Price Selector

**Odoo 19 module** — Adds a price type selector on each sale order line, allowing salespeople to choose between catalogue price, special price, standard cost, partner pricelist price, or a manual price.

## Features

- 🏷️ **Tag icon** on each sale order line opens a price selector dialog
- **4 pre-configured price types** displayed with their computed values:

| # | Type | Source |
|---|------|--------|
| 1 | **Prix catalogue** | Public sales price (`lst_price`) |
| 2 | **Prix spécial** | Special negotiated price set on the product form |
| 3 | **Prix standard** | Cost price (`standard_price`) |
| 4 | **Prix partenaire** | Price computed from the customer's pricelist |
| 5 | **Prix manuel** | Free manual input |

- Price is applied **per line** — not globally on the whole order
- New **Prix spécial** field on the product form (General Information tab)

## Installation

### From GitHub
1. Copy the `sale_price_selector` folder into your Odoo addons path
2. Restart Odoo server
3. Go to **Apps → Update Apps List**
4. Search for `sale_price_selector` → **Install**

### On Odoo SH
1. Add the `sale_price_selector` folder to your SH GitHub repository
2. Push to your branch — wait for the green build
3. Install via Apps UI or shell:
```bash
odoo-bin -i sale_price_selector
```

## Configuration

1. **Product form** → set **Prix spécial** field (appears under list price on General Information tab)
2. **Quotation** → add a product line → click the 🏷️ icon next to the unit price
3. Select a price type → click **Apply**

## Dependencies

- `sale` (standard Odoo Sales module)

## Compatibility

| Odoo Version | Status |
|---|---|
| 19.0 | ✅ Tested |
| 18.0 | ⚠️ Should work (not tested) |

## Author

**[Prelium](https://prelium.fr)** — Odoo integrator & consultant

## License

LGPL-3
