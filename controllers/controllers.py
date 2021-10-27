# -*- coding> UTF/8 -*-
from odoo import http
from odoo.http import Response
from odoo.http import request
import json


class EquiposApi(http.Controller):

    @http.route('/api/equipos', auth='public', method=['GET'], csrf=False)
    def get_equipos(self, **kw):
        try:
            equipos = http.request.env['maintenance.equipment'].sudo().search_read(
                [], 
                ['id', 'code', 'name', 'category_id'],
                offset=0,
                limit=50
                )
            res = json.dumps(equipos, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    @http.route('/api/equipos/<id>', auth='public', method=['GET'], csrf=False)
    def get_equipo_id(self, id, **kw):
        try:
            rec = http.request.env['maintenance.equipment'].sudo().search([('id', '=', int(id))], limit=1)
            equipo = {
                'responsable': {
                    'empleado': rec.employee_id.name,
                    'puesto': rec.x_studio_puesto,
                    'departamento': rec.department_id.name,
                    'fecha_asignacion': rec.assign_date,
                },
                'equipo': {
                    'codigo': rec.code,
                    'nombre': rec.name,
                    'categoria': rec.category_id.name,
                    'marca': rec.x_studio_marca.name,
                    'modelo': rec.model,
                    'numero_serie': rec.serial_no,
                },
                'caracteristicas': {
                    'procesador': rec.x_studio_procesador,
                    'memoria': rec.x_studio_memoria,
                    'almacenamiento': rec.x_studio_almacenamiento,
                    'garantia': rec.warranty_date,
                }
            }
            res = json.dumps(equipo, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
