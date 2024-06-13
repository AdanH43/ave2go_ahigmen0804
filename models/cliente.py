# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'ave.cliente'
    _description = 'Modelo del cliente'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    identificacion = fields.Char(string='Identificación (DNI o Pasaporte)', required=True, copy=False)

    _sql_constraints = [
        ('name_uniq','UNIQUE (idenificacion)', 'la identificacion del cliente ya existe')
    ]

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nombre} {record.apellidos}"
            result.append((record.id, name))
        return result

    