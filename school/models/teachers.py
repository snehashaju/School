from odoo import fields, models


class TeacherInfo(models.Model):
    _name = "teacher.teacher"
    _description = "teachers Profile"

    name = fields.Char(string="Name", help="Enter the name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date_of_Birth")
    image = fields.Image(string="Image")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], 'Gender')
    status = fields.Selection([
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent')],
        'Status', default='temporary')
    phone = fields.Char(string="Phone")
    note = fields.Text(string='Note')
    present = fields.Boolean(string="Present")
    absent = fields.Boolean(string="Absent")
    subject = fields.Selection(
        [('english', 'English'),
         ('malayalam', 'Malayalam')],
        'subject'
    )
    color = fields.Integer(string="Color")
    english_qualification = fields.Char(string="English Qualification")
    malayalam_qualification = fields.Char(string="Malayalam Qualification")
    teacher_emp_id = fields.Char(string="Teacher ID")
    student_ids = fields.One2many('student.details', 'teachers_id', string='Student ID')
    subject_teacher = fields.One2many("subject.teacher", 'teacher_id', string='Subject Id')


class StudentDetails(models.Model):
    _name = "student.details"

    student_id = fields.Many2one('student.student', string='Student', domain="[('teacher_id','=', teachers_id)]")
    teachers_id = fields.Many2one('teacher.teacher', string='Teacher')


class SubjectDetails(models.Model):
    _name = "subject.teacher"

    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    subject_ids = fields.Many2many('subject.subject', string='Subject', domain="[('teacher_id', '=', teacher_id)]")
    age = fields.Integer(related='teacher_id.age', string='Age')
