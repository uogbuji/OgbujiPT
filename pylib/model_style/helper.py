# SPDX-FileCopyrightText: 2023-present Uche Ogbuji <uche@ogbuji.net>
#
# SPDX-License-Identifier: Apache-2.0
# ogbujipt.model_style.helper

import os

__all__ = ['hosted_model_openai']


def hosted_model_openai():
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
