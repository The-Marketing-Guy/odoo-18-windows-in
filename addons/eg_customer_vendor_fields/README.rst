Customer or Vendor Fields
=========================

This Odoo module restores the "Is Customer" and "Is Vendor" fields for contacts, a feature available in Odoo versions 
prior to version 13. It helps users identify whether a contact is a customer or a vendor, improving the management of 
sales and purchase orders.

Features
--------

- **Is Customer and Is Vendor Boolean Fields**: Adds fields to the contact form to configure whether the contact is a customer or a vendor.
- **Sales Order Filter**: Filters contacts by the "Is Customer" field, ensuring only contacts marked as customers appear in sales orders.
- **Purchase Order Filter**: Filters contacts by the "Is Vendor" field, ensuring only contacts marked as vendors appear in purchase orders.
- **Request for Quotation**: Only contacts marked as vendors are displayed when creating RFQs.

Installation
------------

1. Install the module from the Odoo apps menu.
2. Once installed, go to the Contacts view to see the new "Is Customer" and "Is Vendor" checkboxes.
3. Use these fields to configure contacts as customers or vendors in the sales and purchase modules.

Usage
-----

1. **Contacts view**: 
   - Navigate to Contacts → Contacts → Sales & Purchase to configure "Is Customer" and "Is Vendor" fields for each contact.
   
2. **Sales View**:
   - Navigate to Sales → Orders → Customers to see only contacts marked as customers.

3. **Quotations View**:
   - When creating a new quotation, only contacts with "Is Customer" checked will appear in the list of available contacts.

4. **Purchase View**:
   - Navigate to Purchase → Orders → Vendors to see only contacts marked as vendors.

5. **Request for Quotation**:
   - Only contacts marked as vendors will appear when creating RFQs.

Support
-------

For any demo or support, please contact us at: team@inkerp.com

Author: INKERP  
Website: https://inkerp.com
