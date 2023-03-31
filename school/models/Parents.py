from odoo import fields, models


class ParentInfo(models.Model):
    _name = "parent.parent"
    _description = "Parent Profile"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date of Birth")
    image = fields.Image(string="Image")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], 'Gender')
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    meeting_start_date = fields.Datetime(string='Meeting Date')

