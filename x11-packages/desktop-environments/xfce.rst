.. -*- coding: utf-8 -*-

%%%%
XFCE
%%%%


**Installation**
----------------
XFCE component are listed here

.. code-block:: shell

        desktop.xfce                       - This is the root component that contains the xfce4  desktop environment. 
        desktop.xfce.addon                 - Component that includes extra programs (addons) desktop software and desktop environments 
        desktop.xfce.admin                 - That component includes xfce administration tools. 
        desktop.xfce.base                  - Component that includes base packages of xfce desktop environment. 
        desktop.xfce.lookandfeel           - Includes appearance and palettes for xfce 
        desktop.xfce.plugin                - Component that includes desktop software and desktop environments 

For full installation `inary it -c desktop.xfce`

**Starting xfce session**
------------
- run *startxfce4* start a new xfce session. You can add **.xinitrc** file


**Resetting to defaults**
^^^^^^^^^^^^^^^^^^^^^^^^^
Try running: 

.. code-block::

        mv ~/.config/xfce4-session/ ~/.config/xfce4-session-bak
        mv ~/.config/xfce4/ ~/.config/xfce4-bakThese


**Debugging**
-------------

**TroubleShooting**
-------------------
