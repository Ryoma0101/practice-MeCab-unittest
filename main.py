import MeCab


def mecab_parse(text):
    tagger = MeCab.Tagger()
    parsed_text = tagger.parse(text)
    return parsed_text
