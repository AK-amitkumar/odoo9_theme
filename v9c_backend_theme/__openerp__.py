# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "V9c Backend Material Theme",
    "summary": "Odoo 9.0 community Material backend theme"
               "web",
    "version": "9.0.1.0.0",
    "category": "Website",
    "website": "http://www.openworx.nl",
    "author": "Openworx, LasLabs, Tecnativa, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
}

/*!------------------------------------*\
    Left
\*!------------------------------------*/
.drawer--left .drawer-nav {
  left: -16.25rem;
  -webkit-transition: left .1s cubic-bezier(0.190, 1.000, 0.220, 1.000);
  transition: left .1s cubic-bezier(0.190, 1.000, 0.220, 1.000);
}
