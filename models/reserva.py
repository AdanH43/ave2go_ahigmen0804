# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Reserva(models.Model):
    _name = 'ave.reserva'
    _description = 'Reserva de Viaje en Tren'

    fecha_reserva = fields.Date(string='Fecha de la Reserva', required=True, default=fields.Date.context_today)
    asientos_reservados = fields.Integer(string='Asientos Reservados', required=True, default=1)
    cliente_ids = fields.Many2one('cliente', string='Cliente', required=True)
    viaje_id = fields.Many2one('viaje.tren', string='Viaje', required=True)

    @api.constrains('fecha_reserva', 'viaje_id')
    def _check_fechas(self):
        for reserva in self:
            if reserva.fecha_reserva < fields.Date.today():
                raise ValidationError('La fecha de la reserva no puede ser en el pasado.')
            if reserva.viaje_id.fecha_viaje < fields.Date.today():
                raise ValidationError('La fecha del viaje no puede ser en el pasado.')
            if reserva.fecha_reserva > reserva.viaje_id.fecha_viaje:
                raise ValidationError('La fecha de la reserva no puede ser después de la fecha del viaje.')

    @api.constrains('cliente_ids')
    def _check_asientos_reservados(self):
        for reserva in self:
            if not reserva.cliente_ids:
                raise ValidationError('La reserva debe tener al menos un cliente.')
            if len(reserva.cliente_ids) > reserva.viaje_id.asientos_disponibles:
                raise ValidationError('No hay suficientes asientos disponibles para esta reserva.')

    @api.model
    def create(self, vals):
        reserva = super(Reserva, self).create(vals)
        if reserva.viaje_id:
            reserva.viaje_id.asientos_disponibles -= reserva.asientos_reservados
        return reserva

    def unlink(self):
        for reserva in self:
            if reserva.viaje_id:
                reserva.viaje_id.asientos_disponibles += reserva.asientos_reservados
        return super(Reserva, self).unlink()