#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:33:54 2018

@author: braulinho
"""
personal=['Sirve alcohol','Bar completo','Vino y cerveza','Comida local','Reuniones de negocios','Ocasiones especiales','Romántico','Vistas'] 
amigos=['Sirve alcohol','Bar completo','Vino y cerveza','Comida local','Grupos grandes','Bar con música en vivo'] 
familiar=['Niños', 'Familias con niños', 'Comida local']

def planes (propiedades):
    salida=[]
    caracs=[]
    if len(propiedades['features']) > 0:
        caracs.extend([x.strip() for x in propiedades['features'][0].split(',')])
    if len(propiedades['events']) > 0:
        caracs.extend([y.strip() for y in propiedades['events'][0].split(',')])
    #personal
    for p in personal:
        if p in caracs:
            salida.append('personal')
            break
    #amigos
    for a in amigos:
        if a in caracs:
            salida.append('amigos')
            break
    #familiar
    for f in familiar:
        if f in caracs:
            salida.append('familiar')
            break
    if len(salida) == 0:
        salida.extend(['personal','amigos'])
    return salida