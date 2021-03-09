# -*- coding: utf-8 -*-

from odoo import models, fields, api


class taskInherit(models.Model):
    _inherit = "project.task"

    @api.model
    def _calculate_percentage(self):
        for rec in self:
            rec.complete_task_percentage_progress = rec.complete_task_percentage * 100;

    complete_task_percentage = fields.Float(string="Completed %")

    complete_task_percentage_progress = fields.Char(string="Completed %", compute="_calculate_percentage", Store=False)

