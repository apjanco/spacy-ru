#coding: utf-8
from spacy.lang.ru.examples import sentences

ss = ['Ты кто такой?', 'Давай досвидания!']
for s in sentences:
    s = s.strip()
    if not s[-1:] in '.!?':
        s = s + '.'
    ss.append(s)

sample_sentences = ' '.join(ss)
