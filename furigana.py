# -*- coding: utf-8 -*-

from sudachipy import tokenizer
from sudachipy import dictionary
from wanakana import to_hiragana, is_hiragana, is_japanese, is_katakana
import string

tokenizer_obj = dictionary.Dictionary(dict_type="small").create()

KANJI_READING_MAPPING = {
    '私': '私[わたし]',
    '貴女': '貴女[あなた]',
    '何': '何[なに]',
    '外宇宙': '外宇宙[がいうちゅう]',
    '異星人': '異星人[いせいじん]',
    '優那': '優那[ゆうな]',
    '菜々美': '菜々美[ななみ]'
}

JAPANESE_PUNCTUATION = '　〜！？。、（）：「」『』０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'

SPECIAL_CHARACTERS = '〜'

def is_japanese_extended(text):
    return is_japanese(text) and text not in string.punctuation and text not in JAPANESE_PUNCTUATION

def to_anki_format(index, kanji, reading):
    return '{}{}[{}]'.format(' ' if index > 0 else '', kanji, reading) 

def add_furigana(text):
    tokens = [m for m in tokenizer_obj.tokenize(text, tokenizer.Tokenizer.SplitMode.C)]
    parsed = ''
    token_indexes_to_skip = []
    for index, token in enumerate(tokens):   
        if index in token_indexes_to_skip:
          continue
        to_parse = is_japanese_extended(token.surface()) and not is_katakana(token.surface()) and not is_hiragana(token.surface())
        if to_parse:
            if token.surface()[-1] in SPECIAL_CHARACTERS:
                parsed += add_furigana(token.surface()[:-1]) + token.surface()[-1]
            else:
                if index > 0:
                    parsed += ' '
                reading = to_hiragana(token.reading_form())
                if token.surface() in KANJI_READING_MAPPING:
                    parsed += KANJI_READING_MAPPING[token.surface()]
                elif index < len(tokens)-1 and token.surface() + tokens[index+1].surface() in KANJI_READING_MAPPING:
                    parsed += KANJI_READING_MAPPING[tokens[index].surface() + tokens[index+1].surface()]
                    token_indexes_to_skip.append(index+1)
                else:
                    surface_index = 0
                    reading_index = 0
                    while len(token.surface()) > surface_index:
                        if is_hiragana(token.surface()[surface_index]) or is_katakana(token.surface()[surface_index]):
                            parsed += token.surface()[surface_index]
                            reading_index += 1
                            surface_index += 1
                        else:
                            next_index = -1
                            for token_index in range(surface_index, len(token.surface())):
                                if is_hiragana(token.surface()[token_index]) or is_katakana(token.surface()[token_index]):
                                    next_index = token_index
                                    break
                            if next_index < 0:
                                parsed += to_anki_format(
                                  index=surface_index, 
                                  kanji=token.surface()[surface_index:], reading=reading[reading_index:])
                                break
                            else:
                                reading_index_tail = reading_index
                                while reading[reading_index_tail] != token.surface()[next_index] or (reading_index_tail < len(reading)-1 and reading[reading_index_tail] == reading[reading_index_tail+1]):
                                    reading_index_tail += 1
                                parsed += to_anki_format(
                                  index=surface_index, 
                                  kanji=token.surface()[surface_index:next_index], reading=reading[reading_index:reading_index_tail])
                                reading_index = reading_index_tail
                            reading_length = next_index - surface_index
                            if reading_length > 0:
                                surface_index += reading_length
                            else:
                                break
        else:
            parsed += token.surface()
    return parsed

# test = ['私', 'このテキストは', 'Japanese', '可愛い','いい加減', '喧嘩', '咲く', '入り口', '兎に角', '取り逃す', 'とり戻す', '絞り込んだ', 'この先に多数の機械生命体反応を確認', '広いな……この廃墟。']
# for s in test:
#     print(add_furigana(s))

# 映画「千と千尋の神隠し」の一部のようです。この映画は、宮崎駿監督によるスタジオジブリのアニメーション映画で、2001年にリリースされました。物語は、10歳の少女千尋が不思議な世界に迷い込み、両親を救い出すために様々な試練に挑む様子を描いています。このテキストは、映画内のキャラクター間の対話や、特定のシーンの説明を含んでいるようです。それぞれのエントリーは、特定の言葉やフレーズに焦点を当て、それに関連する日本語と英語の対話を提供しています。映画では、主人公の千尋が魔女の湯婆婆によって「千」という名前に変えられ、本当の名前を忘れると二度と人間の世界に戻れなくなるという危険に直面します。千尋は、この新しい環境で働きながら、自分のアイデンティティを保持し、両親を救い出す方法を見つけ出さなければなりません。これらのテキストは、そのような物語の要素を反映したもので、キャラクターの成長、友情、勇気についての物語を伝えています。'
    
# df_anki = df_anki.map(lambda x: add_furigana(x) if isinstance(x, str) else x)
# df_anki.head



