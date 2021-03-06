# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_login()
def aluno():
    form = SQLFORM(Aluno)
    if form.process().accepted:
        session.flash = 'Novo Aluno cadastrado: %s' % form.vars.nome
        redirect(URL('aluno'))
    elif form.errors:
        response.flash = 'Erros encontrados no formulário'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def professor():
    form = SQLFORM(Professor)
    if form.process().accepted:
        session.flash = 'Novo Professor cadastrado: %s' % form.vars.nome
        redirect(URL('professor'))
    elif form.errors:
        response.flash = 'Erros encontrados no formulário'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def empresa():
    form = SQLFORM(Empresa)
    if form.process().accepted:
        session.flash = 'Nova empresa cadastrada: %s' % form.vars.nome
        redirect(URL('empresa'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def estagio():
    form = SQLFORM(Estagio)
    if form.process().accepted:
        session.flash = 'Novo Estagio cadastrado'
        redirect(URL('estagio'))
    elif form.errors:
        response.flash = 'Erros encontrados no formulário'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário'
    return dict(form=form)

# READ

@auth.requires_login()
def ver_aluno():
    grid = SQLFORM.grid(Aluno)
    return dict(grid=grid)

@auth.requires_login()
def ver_professor():
    grid = SQLFORM.grid(Professor)
    return dict(grid=grid)

@auth.requires_login()
def ver_empresa():
    grid = SQLFORM.grid(Empresa)
    return dict(grid=grid)

@auth.requires_login()
def ver_estagio():
    grid = SQLFORM.grid(Estagio)
    return dict(grid=grid)
