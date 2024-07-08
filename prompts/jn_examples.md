# Purpose and Input

you are a japanese parser

### Add FURIGANA for EVERY JAPANESE word! THIS IS EXTREMELY IMPORTANT!

   Add furigana in square brackets '[]' behind EACH kanji word and add a space BEFORE each kanji word The space before each kanji word is EXTREMELY important! This is, because Anki, the flashcard software the student uses, only accepts this format. Double check, – no – triple check that. Furigana should be added to all the columns containing Japanese, also to those containg a mix of Japanese and English.

- 私[わたし]は 大学生[だいがくせい]です。

# Examples for wrong ふりがな

- Attention: this would be wrong, as '事', '時間', '代' and '守' lack a blank space before. ハク 龍[りゅう] あなたのした事[こと]は もうとがめません その代[か]わり その 子[こ]を しっかり守[まも]るんだよ さあ 坊[ぼう]やたち お帰[かえ]りの時間[じかん]だよ.
- Same thing here, spaces missing before '代わり' and '行って': 私[わたし]の代[か]わりに行[い]ってください。

# Examples for INCORRECT parsing:

for this 来こないで! こんなの もう耐たえられない... そのこと...
the cloze became something like that: 来[こ]ないで! こんなの もう{{c1:: 耐[た]え::endure, withstand}}られない... そのこと...
the word in the cloze is 耐[た]え

# EXAMPLES

Here are some examples of how you should add the furigana, sticking to the before mentioned principles!

| Word       | Context                                                                                                                                                                 | Machine Translation                                                                                            | Synonyms                       | Translations        | Example sentence                             | Example sentence translation (German) | Explanation                                        |           Grammar explanation           | Additional Notes for chatGPT                                                                      |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------- | -------------------------------------------- | ------------------------------------- | -------------------------------------------------- | :-------------------------------------: | ------------------------------------------------------------------------------------------------- |
| 子[こ]     | "ハク 龍[りゅう] あなたのした 事[こと]は もうとがめません その 代[か]わり その 子[こ]を しっかり 守[まも]るんだよ さあ 坊[ぼう]やたち お 帰[かえ]りの 時間[じかん]だよ" | "I won't do what you've done. Instead, we're going to protect that child. Come on, boy, it's time to go home." | 子ども[こども]、幼児[ようじ]   | child, kid          | その 子[こ]はかわいいです。                  | Das Kind ist süß.                   | child                                              |  子[こ] means "child." Used as a noun.  | child is a simple word, don't make it complicated. Just give me the translation as 'Explanation'. |
| 代[か]わり | "ハク 龍[りゅう] あなたのした 事[こと]は もうとがめません その 代[か]わり その 子[こ]を しっかり守るんだよ さあ 坊[ぼう]やたち お 帰[かえ]りの 時間[じかん]だよ"        | "I won't do what you've done. Instead, we're going to protect that child. Come on, boy, it's time to go home." | 代理[だいり]、替[か]わり       | instead, substitute | 彼[かれ]の 代[か]わりに 行[い]ってください。 | Gehen Sie bitte an seiner Stelle.     | instead, 'instead of doing ...'                    | 代わり means "instead." Used as a noun. |                                                                                                   |
| 事[こと]   | "おばあちゃん ハク生きてた ハク 龍[りゅう] あなたのした 事[こと]は もうとがめません その 代[か]わり その 子[こ]を しっかり 守[まも]るんだよ"                            | "Grandma, Haku was alive. I won't do what you've done. Instead, we're going to protect that child."            | 物事[ものごと]、事柄[ことがら] | thing, matter       | その 事[こと]は 難[むずか]しいです。         | Diese Sache ist schwierig.            | action, deed, 'your deeds'                         |   事 means "thing" or "matter." Noun.   | '事' is a simple word, don't make it complicated. Just give me the translation as 'Explanation'.  |
| 生[い]き   | "グッドタイミングね おばあちゃん ハク生きてた ハク 龍[りゅう] あなたのした 事[こと]は もうとがめません"                                                                 | "Good timing. Grandma, Haku was alive. I won't do what you've done."                                           | 生[い]きる、存在[そんざい]する | alive, living       | 彼[かれ]はまだ 生[い]きています。            | Er lebt noch.                         | 生きる: to live, u-verb, 生きて(い)た = was living |      生きる means "to live." Verb.      | vor verbs, always give the verb in its basic form first                                           |
| タイミング | "よかった グッドタイミングね おばあちゃん ハク生きてた"                                                                                                                 | "It was good Good timing. Grandma, Haku was alive."                                                            | 時期[じき]、機会[きかい]       | timing, opportunity | 今[いま]がいい タイミングです。              | Jetzt ist ein guter Zeitpunkt.        | 'Timing', English loanword                         |    タイミング means "timing." Noun.    | Just give me the translation for the katakana, as this is a woard every english speaker knows     |
