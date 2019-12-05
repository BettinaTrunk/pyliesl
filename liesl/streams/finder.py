# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:35:12 2018

Robert Guggenberger
"""
import pylsl
from pylsl import StreamInlet, StreamInfo
from functools import wraps
from typing import Dict, List
from liesl.tools.convert import xml_to_dict

# %%
def recover_info(stream: StreamInlet) -> StreamInfo:
    "takes a StreamInlet and recovers the basic info"
    info = stream.info()
    return pylsl.StreamInfo(
        name=info.name(),
        type=info.type(),
        channel_count=info.channel_count(),
        nominal_srate=info.nominal_srate(),
        channel_format=info.channel_format(),
        source_id=info.source_id(),
    )


def print_available_streams():
    "print all available streams in their xml form"
    available_streams = pylsl.resolve_streams()
    for a in available_streams:
        print(a.as_xml())


def open_stream(**kwargs) -> StreamInlet:
    """get only a single streaminlets which matches kwargs

    raises a ConnectionError if more than one match is found

    args
    ----
    **kwargs:
        keyword arguments to identify the desired stream
        
    returns
    -------
    stream: StreamInlet
        a single StreamInlet matching the kwargs. 
    
    
    """
    infos = get_streaminfos_matching(**kwargs)
    if infos is None:
        return None
    elif len(infos) > 1:
        raise ConnectionError("Found too many streaminfos")
    else:
        return pylsl.StreamInlet(infos[0])


def open_streaminfo(**kwargs) -> StreamInfo:
    """get only a single StreamInfo which matches kwargs

    raises a ConnectionError if more than one match is found

    args
    ----
    **kwargs:
        keyword arguments to identify the desired stream
        
    returns
    -------
    sinfo: StreamInfo
        a single StreamInfo matching the kwargs. 
    
    
    """
    infos = get_streaminfos_matching(**kwargs)
    if infos is None:
        return None
    elif len(infos) > 1:
        raise ConnectionError("Found too many streaminfos")
    else:
        return infos[0]


def get_streams_matching(**kwargs) -> List[StreamInlet]:
    """get all streaminlets matching kwargs
    args
    ----
    **kwargs:
        keyword arguments to identify the desired stream
        
    returns
    -------
    varies: List[StreamInlet]
        a list of StreamInlets matching the kwargs
    
    """
    infos = get_streaminfos_matching(**kwargs)
    if infos is None:
        return None
    else:
        streams = []
        for info in infos:
            streams.append(pylsl.StreamInlet(info))
        return streams


def get_streaminfos_matching(**kwargs) -> List[StreamInfo]:
    """
    args
    ----
    **kwargs:
        keyword arguments to identify the desired stream
        
    returns
    -------
    varies: List[StreamInfo]
        a list of StreamInfo matching the kwargs
    
    """
    # find all available streams, check whether they are fitting with kwargs
    available_streams = pylsl.resolve_streams()
    if len(available_streams) == 0:
        return None
    fitting_streams = []
    for st in available_streams:
        for k, v in kwargs.items():
            if eval("st." + k + "()") != v:
                break
        else:
            fitting_streams.append(st)

    # either throws a timepout, returns a streaminfo or a list of streaminfos
    if len(fitting_streams) == 0:
        return None
    else:
        return fitting_streams

