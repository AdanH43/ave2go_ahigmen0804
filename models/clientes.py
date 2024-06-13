# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'ave.cliente'
    _description = 'Modelo del cliente'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    identificacion = fields.Char(string='Identificación (DNI o Pasaporte)', required=True, copy=False)

    