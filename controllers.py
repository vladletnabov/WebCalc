# -*- coding: utf-8 -*-
from openerp import http
import werkzeug
from openerp.http import request
#import os

class WebCalc(http.Controller):
    @http.route(['/webcalc/remoteaddr/'], type='json', auth='public', website=True)
    def return_map(self):
        '''For JSON you need restart odoo with - u module_name after all modify'''
        remoteAddr = request.httprequest.environ['REMOTE_ADDR']
        return {'remoteAddr': remoteAddr}

    @http.route(['/web_calc/register_session'], type='json', auth='public', website=True)
    def register_session(self, prevouseURL, currentURL):
        '''For JSON you need restart odoo with - u module_name after all modify'''
        # remoteAddr = request.httprequest.environ['REMOTE_ADDR']

        return {'remoteAddr': '192.12.122.34'}

    @http.route(['/web_calc/check_session'], type='json', auth='public', website=True)
    def check_session(self, sessionID, prevouseURL, currentURL):
        '''For JSON you need restart odoo with - u module_name after all modify'''
        remoteAddr = request.httprequest.environ['REMOTE_ADDR']
        return {'remoteAddr': '192.12.122.34'}

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