# lexicon
Method for extracting lexical samples for further annotation.

We extract the most frequent lexemes of Croatian from the hrLex v1.2 lexicon (http://hdl.handle.net/11356/1072) which is

1. built by maximizing the coverage of the hrWaC corpus (http://hdl.handle.net/11356/1064, http://nl.ijs.si/noske/all.cgi/first_form?corpname=hrwac;align=)

2. enriched with frequencies from the hrWaC corpus

The extraction process is defined in ```sample.py```. To run it, simply give the script as an argument to your python (2.*) interpreter:

```
python sample.py
```
