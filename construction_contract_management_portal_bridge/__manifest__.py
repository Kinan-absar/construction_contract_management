{
    'name': 'Construction Contract Management - Employee Portal Bridge',
    'version': '18.0.1.1.0',
    'summary': 'Connects Construction Contract Management with Employee Portal Suite.',
    'description': """
Technical integration bridge between Construction Contract Management and Employee Portal Suite.

The two main applications remain independent. When both are available, this bridge
installs automatically and exposes authorized construction records in the Employee Portal.

Adds:
- /my/employee/contracts
- /my/employee/ipcs
- /my/employee/variations
- /my/employee/measurements
- Employee Portal dashboard cards and navigation links
    """,
    'category': 'Construction',
    'author': 'Kinan',
    'license': 'OPL-1',
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': [
        'construction_contract_management',
        'employee_portal_suite',
    ],
    'data': [
        'views/employee_dashboard_extension.xml',
        'views/layout_extension.xml',
        'views/portal_employee_contract_templates.xml',
        'views/portal_employee_ipc_templates.xml',
        'views/portal_employee_variation_templates.xml',
        'views/portal_employee_measurement_templates.xml',
    ],
}
