import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-manufacture-reporting",
    description="Meta package for oca-manufacture-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-mrp_bom_matrix_report',
        'odoo11-addon-mrp_bom_structure_xlsx',
        'odoo11-addon-mrp_bom_structure_xlsx_level_1',
        'odoo11-addon-mrp_flattened_bom_xlsx',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
