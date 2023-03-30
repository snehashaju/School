from odoo import fields, models


class StaffInfo(models.Model):
    _name = "student.student"
    _description = "Staff Profile"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date of Birth")
    image = fields.Image(string="Image")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], 'Gender')
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')

