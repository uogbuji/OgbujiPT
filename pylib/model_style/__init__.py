# SPDX-FileCopyrightText: 2023-present Uche Ogbuji <uche@ogbuji.net>
#
# SPDX-License-Identifier: Apache-2.0
# ogbujipt.model_style

'''
>>> from ogbujipt.model_style import hosted_model_openai
>>> from ogbujipt.config import openai_emulation
>>> openai_emulation(host='http://127.0.0.1', port='8000')
>>> print(hosted_model_openai())
['/models/TheBloke_WizardLM-13B-V1.0-Uncensored-GGML/wizardlm-13b-v1.0-uncensored.ggmlv3.q6_K.bin']
'''

from enum import Enum


class style(Enum):
    '''
    Marker of different prompring styles. When LLMs are trained, they're tuned
    to expect prompts according to a specific convention, and can become very
    erratic if you use the wrong one
    '''
    ALPACA = 1
    ALPACA_INSTRUCT = 2
    VICUNA = 3
    WIZARD = 4

from ogbujipt.model_style.helper import hosted_model_openai, model_style_from_name  # noqa
