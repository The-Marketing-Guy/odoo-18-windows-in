{
   "name": "Customer Vendor Fields",
    "version": "18.0",
    "category": "Sale, purchase",
    'summary': "Add dedicated fields to distinguish between customers and vendors in Odoo. Streamline contact management and enhance clarity in business transactions. , Customer Vendor Fields in Odoo, Odoo Contact Customization, Manage Customers and Vendors, Contact Classification in Odoo, Streamlined Business Transactions, Enhanced Contact Management. Odoo, Customer Fields, Vendor Fields, Sales, Purchase, Contacts, Is Customer, Is Vendor, Sales Order, Purchase Order, RFQ, CRM, Contact Management, Odoo Module.",
    'description': """
        This Odoo module restores the "Is Customer" and "Is Vendor" fields for contacts, a feature available in Odoo versions 
        prior to version 13. It helps users identify whether a contact is a customer or a vendor, improving the management of 
        sales and purchase orders. The module adds Boolean fields to the contact form and filters for customers and vendors 
        in the respective views.
    """,
    "author": "INKERP",
    'website': 'https://www.inkerp.com/',
    "depends": ["contacts", "purchase", "sale_management"],
    "data": [
        "views/res_partner_view.xml",
        "views/sale_order_view.xml",
        "views/purchase_order_view.xml"],
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}

