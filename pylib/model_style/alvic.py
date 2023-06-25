# SPDX-FileCopyrightText: 2023-present Uche Ogbuji <uche@ogbuji.net>
#
# SPDX-License-Identifier: Apache-2.0
# ogbujipt.model_styles.alvic

'''
Model style for Alpaca (instruction based) or Vicuña (Q&A).

Plain Alpaca style, e.g.:

* WizardLM

Alpaca-instruct style, e.g.

* Nous-Hermes

Vicuña style, e.g.

* Robin

Useful collection of Alpaca demo prompts: https://huggingface.co/datasets/tatsu-lab/alpaca
'''

import warnings

from ogbujipt.model_style import style

ALPACA_PROMPT_TMPL = '''\
{preamble}

{instru_marker}{instru_inputs}

### Response:
'''


VICUNA_PROMPT_TMPL = '''\
{preamble}

### USER:

{query}

### ASSISTANT:
'''


def make_prompt(msg: str, sub=style.ALPACA, preamble='', inputs='') -> str:
    '''
    Build a string prompt based on Alpaca, Alpaca Instruct or Vicuña
    '''
    if sub in (style.ALPACA, style.ALPACA_INSTRUCT):
        # Roundabout method needed pre Python 3.12 because of escaping limitations
        cr = '\n'
        instru_inputs = f'{msg}\n{"### Inputs:" + cr + inputs if inputs else "" }\n'
        instru_marker = '### Instruction:\n\n' if sub == style.ALPACA_INSTRUCT else ''
        return ALPACA_PROMPT_TMPL.format(
            preamble=preamble,
            instru_marker=instru_marker,
            instru_inputs=instru_inputs
            )
    elif sub == style.VICUNA:
        if inputs:
            warnings.warn('inputs are not defined for Vicuña style, and will be ignored')
        return VICUNA_PROMPT_TMPL.format(
            preamble=preamble,
            query=msg
            )
    else:
        raise ValueError('Prompt substyle should be Alpaca or Vicuna, not ', sub)
