# -*- coding: utf-8 -*-
{
    'name': "School",
    'author': "Sneha",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/teacher_view.xml',
        'views/staff_views.xml',
        'views/student_view.xml',
        'views/subject_view.xml',
        'views/parent_view.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}