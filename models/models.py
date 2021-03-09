# -*- coding: utf-8 -*-

from odoo import models, fields, api


class projectInherit(models.Model):
    _inherit = "project.project"

    # project_contracts = fields.Many2many('ir.attachment', relation="ir_attachment_project_project_relation", column1="project_project_id", column2="ir_attachment_id", string="Contracts")
    # project_contracts = fields.Many2many('ir.attachment', string="Contracts")
    @api.model
    def _calculate_percentage(self):
        for rec in self:
            rec.complete_percentage_progress = rec.complete_percentage * 100;

    complete_percentage = fields.Float(string="Completed %")

    complete_percentage_progress = fields.Char(string="Completed %", compute="_calculate_percentage", Store=False)

# class add_project_contract(models.Model):
#     _name = 'add_project_contract.add_project_contract'
#     _description = 'add_project_contract.add_project_contract'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
