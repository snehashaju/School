from odoo import fields, models


class StaffInfo(models.Model):
    _name = "staff.staff"
    _description = "Staff Profile"

    name = fields.Char(string="Name", help="Enter the name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date_of_Birth")
    image = fields.Image(string="Image")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], 'Gender')
    position = fields.Selection([('office-staff', 'Office-Staff'), ('management-staff', 'Management-Staff')], 'Position')
    status = fields.Selection([('temporary', 'Temporary'), ('permanent', 'Permanent')], 'Status', defult="active")
    phone = fields.Char(string="Phone")
    note = fields.Text(string='Note')
