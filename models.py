# -*- coding: utf-8 -*-

from datetime import timedelta

from openerp import models, fields, api

# class web_calc(models.Model):
#     _name = 'web_calc.web_calc'

#     name = fields.Char()

class SessionVisitor(models.Model):
    _name = 'web_calc.session_visitor'

    clientAddr = fields.Char(string="Client remote IP address", required=True)
    dateVisit = fields.Date(default=fields.Date.today)
    dateLastCheck = fields.Date(default=fields.Date.today)
    # в dateLastCheck находится время последнего ping со страницы. Время пребывания пользователя на сайте
    # высчитывается как дельта dateVisit и dateLastCheck
    session_first_visit_ids = fields.One2many(
        'web_calc.session_first_visit', 'session_id', string="Sessions")
    session_site_trip_ids = fields.One2many(
        'web_calc.session_site_trip', 'session_id', string="Sessions site trip")
    session_ping_result_ids = fields.One2many(
        'web_calc.session_site_trip', 'session_id', string="Sessions ping result")

class SessionTimeout(models.Model):
    _name = 'web_calc.session_timout'
    timeoutSession = fields.Integer(string="Timeout visitor session for cookie in minuetes")
    timeoutPing = fields.Integer(string="Timeout for ping activity in secounds")

class SessionFirstVisit(models.Model):
    _name = 'web_calc.session_first_visit'

    session_id = fields.One2one('web_calc.session_visitor', string="Session id")
    source_type_id = fields.Many2one('web_calc.session_source_type', string="Type source")
    source_url_id = fields.Many2one('web_calc.session_url_list', string="Source URL")
    courent_url_id = fields.Many2one('web_calc.session_url_list', string="Courent URL")

    _sql_constraints = [
        ('session_id_unique',
         'UNIQUE(session_id)',
         "The client session ID must be unique"),
    ]

class SessionSourceType(models.Model):
    _name = 'web_calc.session_source_type'
    source_type = fields.Char(string="Type source", required=True)
    session_first_visit_ids = fields.One2many(
        'web_calc.SessionFirstVisit', 'type_source_id', string="Type source first visit")

    _sql_constraints = [
        ('source_type_unique',
         'UNIQUE(source_type)',
         "The source type must be unique"),
    ]

class SessionUrlList(models.Model):
    _name = 'web_calc.session_url_list'

    url = fields.Char(string="URL", required=True)
    url_local  = fields.Boolean(default=False)
    session_first_vizit_source_url_id = fields.One2many('web_calc.session_first_visit', string="Source URL")
    session_first_vizit_courent_url_id = fields.One2many('web_calc.session_first_visit', string="Courent URL")

    _sql_constraints = [
        ('url_unique',
         'UNIQUE(url)',
         "The URL must be unique"),
    ]


class SessionSiteTrip(models.Model):
    _name= 'web_calc.session_site_trip'

    session_id = fields.Many2one('web_calc.session_source_type', string="Session id")
    time_start = fields.Date(default=fields.Date.today)
    time_finish = fields.Date(default=fields.Date.today)
    courent_url =

class SearchEngine(models.Model):
    _name = 'web_calc.search_engine'

    engine = url = fields.Char(string="URL", required=True)

    _sql_constraints = [
        ('engine_unique',
         'UNIQUE(engine)',
         "The engine must be unique"),
    ]

