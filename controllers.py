# -*- coding: utf-8 -*-
from openerp import http

class WebCalc(http.Controller):
    @http.route(['/webcalc/jsonrpc/'], type='json', auth='none', website=True)
    def return_map(self, **post):
        return {'x': 12345, 'y': 2222}
#     @http.route('/web_calc/web_calc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_calc/web_calc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_calc.listing', {
#             'root': '/web_calc/web_calc',
#             'objects': http.request.env['web_calc.web_calc'].search([]),
#         })

#     @http.route('/web_calc/web_calc/objects/<model("web_calc.web_calc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_calc.object', {
#             'object': obj
#         })