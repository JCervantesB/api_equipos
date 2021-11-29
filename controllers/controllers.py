# -*- coding> UTF/8 -*-
from odoo import http
from odoo.http import Response
from odoo.http import request
import json


class EquiposApi(http.Controller):

    @http.route('/api/equipos', auth='public', method=['GET'], csrf=False, cors='*')
    def get_equipos(self, **kw):
        try:
            equipos = http.request.env['maintenance.equipment'].sudo().search_read(
                [], 
                ['id', 'code', 'name', 'category_id', 'employee_id', 'department_id', 'x_studio_marca', 'model', 'serial_no', 'x_studio_ubicacion', 'x_studio_selection_field_shlje']
                )
            res = json.dumps(equipos, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    @http.route('/api/equipos/marcas', auth='public', method=['GET'], csrf=False, cors='*')
    def get_marcas(self, **kw):
        try:
            marcas = http.request.env['product.brand'].sudo().search_read(
                [], 
                ['id', 'name']
                )
            res = json.dumps(marcas, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    @http.route('/api/equipos/categorias', auth='public', method=['GET'], csrf=False, cors='*')
    def get_categorias(self, **kw):
        try:
            categorias = http.request.env['maintenance.equipment.category'].sudo().search_read(
                [], 
                ['id', 'name']
                )
            res = json.dumps(categorias, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    @http.route('/api/departamentos', auth='public', method=['GET'], csrf=False, cors='*')
    def get_departamentos(self, **kw):
        try:
            departamentos = http.request.env['hr.department'].sudo().search_read(
                [], 
                ['id', 'name']
                )
            res = json.dumps(departamentos, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
