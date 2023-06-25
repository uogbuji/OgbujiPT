# SPDX-FileCopyrightText: 2023-present Uche Ogbuji <uche@ogbuji.net>
#
# SPDX-License-Identifier: Apache-2.0
# ogbujipt.model_style.helper


import os
import re
from typing import List

from ogbujipt.model_style import style

__all__ = ['hosted_model_openai']

# Quick cheat sheet:
# Alpaca style = [A…] \n ### Response:
# Alpaca/Instruct style = ### Instruction:\n [A…] ### Response:
# Alpaca/Instruct style, with input = ### Instruction:\n [A…] ### Input:\n ### Response:
# Vicuña style = ### Human:\n [A…] ### Assistant:
# Wizard style = USER:\n [A…] ### ASSISTANT:

MODEL_NAME_SEARCH_PATTERNS = {
    re.compile('nous-hermes'): [style.ALPACA_INSTRUCT],
    re.compile('wizardlm'): [style.WIZARD],
    # re.compile(''): [style.ALPACA_INSTRUCT],
}


def hosted_model_openai() -> List[str]:
    '''
    Query the OpenAI-compatible API set up via openai_emulation()
    (or even the real deal)
    to find what model is being run for APi calls
    '''
    try:
        import httpx  # noqa
    except ImportError:
        raise RuntimeError('Needs httpx installed. Try pip install httpx')

    api_base = os.environ['OPENAI_API_BASE']
    resp = httpx.get(f'{api_base}/models').json()
    # print(resp)
    model_fullname = [i['id'] for i in resp['data']]
    return model_fullname


def model_style_from_name(mname: str) -> List[str]:
    '''
    Uses heuristics to figure out the prompting/model style from its name

    >>> from ogbujipt.model_style import model_style_from_name
    >>> model_style_from_name('path/wizardlm-13b-v1.0-uncensored.ggmlv3.q6_K.bin')
    [<style.WIZARD: 4>]
    '''
    # Use the final slash portion, in case it's a full path
    mname = mname.split('/')[-1]
    for pat, styles in MODEL_NAME_SEARCH_PATTERNS.items():
        if pat.search(mname):
            mstyles = styles
            break
    else:
        # XXX: Come up with a default/unknown style?
        mstyles = []
    return mstyles
