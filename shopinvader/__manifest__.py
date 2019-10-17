# -*- coding: utf-8 -*-
# Copyright 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopinvader",
    "summary": "Shopinvader",
    "version": "10.0.2.3.6",
    "category": "e-commerce",
    "website": "https://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "external_dependencies": {
        "python": ["cerberus", "unidecode", "openupgradelib"],
        "bin": [],
    },
    "depends": [
        "base_rest",
        "auth_api_key",
        "base_jsonify",
        "base_sparse_field_list_support",
        "base_suspend_security",
        "base_url",
        "base_vat",
        "component_event",
        "sale",
        "sale_discount_display_amount",
        "onchange_helper",
        "queue_job",
    ],
    "data": [
        "security/shopinvader_security.xml",
        "security/ir.model.access.csv",
        "security/shopinvader_backend_security.xml",
        "security/shopinvader_partner_security.xml",
        "security/shopinvader_category_security.xml",
        "security/shopinvader_product_security.xml",
        "security/shopinvader_variant_security.xml",
        "wizards/shopinvader_variant_unbinding_wizard.xml",
        "wizards/shopinvader_variant_binding_wizard.xml",
        "wizards/shopinvader_category_binding_wizard.xml",
        "wizards/shopinvader_category_unbinding_wizard.xml",
        "wizards/shopinvader_partner_binding.xml",
        "views/shopinvader_menu.xml",
        "views/shopinvader_product_view.xml",
        "views/shopinvader_variant_view.xml",
        "views/shopinvader_category_view.xml",
        "views/shopinvader_cart_step_view.xml",
        "views/shopinvader_partner_view.xml",
        "views/shopinvader_backend_view.xml",
        "views/product_view.xml",
        "views/partner_view.xml",
        "views/product_category_view.xml",
        "views/sale_view.xml",
        "views/shopinvader_config_settings.xml",
        "data/res_partner.xml",
        "data/ir_export_product.xml",
        "data/ir_export_category.xml",
        "data/cart_step.xml",
    ],
    "demo": [
        "demo/account_demo.xml",
        "demo/pricelist_demo.xml",
        "demo/backend_demo.xml",
        "demo/partner_demo.xml",
        "demo/sale_demo.xml",
        "demo/email_demo.xml",
        "demo/notification_demo.xml",
        "demo/product_filter_demo.xml",
        "demo/product_category_demo.xml",
        "demo/product_attribute_value_demo.xml",
        "demo/product_product_demo.xml",
    ],
    "qweb": [],
}
