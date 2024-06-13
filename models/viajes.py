# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Viajes(models.Model):
    _name = 'ave.tren'
    _description = 'Modelo de los viajes'

    nombre = fields.Char(string='ID del Viaje', required=True)
    fecha_viaje = fields.Date(string='Fecha del Viaje', required=True, default=fields.Date.context_today)
    duracion_minutos = fields.Integer(string='Duración (minutos)', required=True)
    numero_asientos = fields.Integer(string='Número de Asientos', required=True, default=1)
    asientos_disponibles = fields.Integer(string='Asientos Disponibles', compute='_compute_asientos_disponibles', store=True)

    @api.depends('numero_asientos')
    def _compute_asientos_disponibles(self):
        for viaje in self:
            viaje.asientos_disponibles = viaje.numero_asientos

    @api.constrains('numero_asientos')
    def _check_numero_asientos(self):
        for viaje in self:
            if viaje.numero_asientos < 1:
                raise ValidationError('El número de asientos debe ser al menos 1.')
