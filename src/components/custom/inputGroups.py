# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:33:41 2023

@author: jim
"""

from dash import html,dcc
import dash_bootstrap_components as dbc

from . import textScripting as ts

def stripKeys(dictIn,keys):
    """Generic function which returns a copy of a dictionary with the specified keys removed"""
    dictOut = dictIn.copy()
    for key in keys:
        if key in dictOut:
            dictOut.pop(key,None)
    return dictOut

def inputGroup(name:str, unit:str, component_id:str, value=None) -> dbc.InputGroup:
    """ A template function for a standard number input group with units. For pattern matching ids, component_id should be a dictionary"""

    # parse for sub and super-scripting
    name = ts.parseAll(name)
    unit = ts.parseAll(unit)

    
    # build input group
    return dbc.InputGroup(
                [
                    dbc.InputGroupText(name,className='input-group-label'),
                    dbc.Input(placeholder="-", type="number",id=component_id,value=value),
                    dbc.InputGroupText(unit),
                ],
                className="mb-3",
            )

def inputGroupList(title:str, inputDicts:[dict], index:int=None, className:str=None,equalPadding=True)->html.Div:
    """A template function for creating a vertical column/list of input groups given lists of dicts each having keys: 'name', 'unit', 'value' (optional) and any keys 
    associated with the component id. Any keys beyond name, unit, and value are specified will be used in the component id dictionary.  If only
    one key besides name, unit, and value are specified, the component id will be a string (no pattern matching)."""
    names = [inputDict['name'] for inputDict in inputDicts]
    
    units = [inputDict['unit'] for inputDict in inputDicts]
    values = [inputDict['value'] if ('value' in inputDict) else None for inputDict in inputDicts]
    ids = [stripKeys(inputDict,['name','unit','value']) for inputDict in inputDicts]
    # allow for non-str title types
    if isinstance(title,str):
        titleObj = html.H4(title)
    else:
        titleObj = title
        
    # create list of inputGroups   
    inDiv = []
    for name, unit, cid, value in zip(names,units,ids,values):
        # if component id dict is length one, assume id is intended to be string (i.e. no pattern matching)
        if len(cid)==1:
            cid = list(cid.values())[0]
            
        inDiv.append(inputGroup(name,unit,cid,value=value))
        
    return html.Div(
        className=className,
        children=[
            titleObj,
            html.Hr(),
            html.Div(inDiv),            
            ]
        )