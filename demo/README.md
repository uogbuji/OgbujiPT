# Simplest

## alpaca_simple_fix_xml.py

Quick demo, sending an Alpaca-compatible LLm some bad XML & asking it to make corrections.

# Intermediate

## alpaca_multitask_fix_xml.py

Intermediate demo using an LLM to repair data (XML), like
alpaca_simple_fix_xml.py
but running a separate, progress indicator task in the background
while the LLm works, using asyncio. This should work even
if the LLM framework we're using doesn't suport asyncio,
thanks to ogbujipt.async_helper 

# Advanced

## alpaca_simple_qa_discord.py

<img width="555" alt="image" src="https://github.com/uogbuji/OgbujiPT/assets/279982/82121324-a930-4b2c-ab26-d8a3c6a50f54">

Demo of a Discord chatbot with an LLM back end

Demonstrates:
* Async processing via ogbujipt.async_helper
* Discord API integration
* Client-side serialization of requests to the server. An important
consideration until more sever-side LLM hosting frameworks reliablly
support multiprocessing

## chat_pdf_streamlit_ui.py

<img width="970" alt="image" src="https://github.com/uogbuji/OgbujiPT/assets/279982/57b479a9-2dbc-4d65-ac19-e954df2a21d0">

"Chat my PDF" demo, but using self-hosted LLM. Definitely a good idea for you to understand
demos/alpaca_multitask_fix_xml.py
before swapping this in.

UI: Streamlit - streamlit.io
Vector store: Qdrant - https://qdrant.tech/

Single-PDF support, for now, to keep the demo code simple, 
though you can easily extend it to e.g. work with multiple docs
dropped in a directory

Note: manual used for above demo downloaded from Hasbro via [Board Game Capital](https://www.boardgamecapital.com/monopoly-rules.htm).
