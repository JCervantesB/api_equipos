# -*- coding> UTF/8 -*-
from odoo import http
from odoo.http import Response
import json


class EquiposApi(http.Controller):

    @http.route('/api/equipos', auth='public', method=['GET'], csrf=False)
    def get_equipos(self, **kw):
        try:
            equipos = http.request.env['maintenance.equipment'].sudo().search_read([], ['id', 'name', 'employee_id'])
            res = json.dumps(equipos, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
