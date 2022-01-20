import spacy


def analyze(doc, lang):
    if lang == 'en':
        model_name = f"{lang}_core_web_sm"
    else:
        model_name = f"{lang}_core_news_sm"

    nlp = spacy.load(model_name)
    doc = nlp(doc)

    olist = list()
    if doc.ents:
        for ent in doc.ents:
            odict = dict()
            odict['text'] = ent.text
            odict['type'] = ent.label
            odict['start_pos'] = ent.start
            odict['end_pos'] = ent.end
            olist.append(odict)
    return olist


if __name__ == '__main__':
    language = 'en'
    txt = 'I think I would like to go to New York and Amsterdam and eat a hamburger with John.'
    output = analyze(txt, language)
    print(output)
