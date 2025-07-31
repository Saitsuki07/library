from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Book Category'

    name = fields.Char('Category', required=True)

    @api.constrains('name')
    def _check_name_unique(self):
        for rec in self:
            if rec.name:
                # Normalize name for comparison
                normalized_name = rec.name.strip().lower()
                # Find existing categories with matching normalized names
                existing = self.search([]).filtered(
                    lambda r: r.id != rec.id and 
                    r.name.strip().lower() == normalized_name
                )
                if existing:
                    raise ValidationError(
                        "Category name must be unique (case-insensitive and ignoring spaces)."
                    )

    # Database constraint remains for direct SQL operations
    _sql_constraints = [
        ('name_unique_constraint', 'unique(name)', 'Category name must be unique.')
    ]