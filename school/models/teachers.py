from odoo import fields, models


class TeacherInfo(models.Model):
    _name = "teacher.teacher"
    _description = "teachers Profile"

    name = fields.Char(string="Name", help="Enter the name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date_of_Birth")
    image = fields.Image(string="Image")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], 'Gender')
    status = fields.Selection([('temporary', 'Temporary'), ('permanent', 'Permanent')], 'Status', default='active')
    phone = fields.Char(string="Phone")
    note = fields.Text(string='Note')
    active = fields.Boolean(string="Active")
    in_active = fields.Boolean(string="In-Active")
    subject = fields.Selection([('english', 'English'), ('malayalam', 'Malayalam')], 'subject')
    english_qualification = fields.Char(string="English-Qualification")
    malayalam_qualification = fields.Char(string="Malayalam-Qualification")
    teacher_id = fields.Char(string="Teacher-ID")

