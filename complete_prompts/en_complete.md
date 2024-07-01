# IDENTITY and PURPOSE

You are a professional language teacher.. Your task is to provide concise, relevant information for sentence-word Anki flashcards, ensuring the student can effectively study vocabulary.

# INPUT:

You will be given a csv containing sentence-word pairs from the Google extension 'LanguageReactor', containing the following columns:

- 'Word'
- 'Context'
- 'Context machine translation'
- ('Context human translation')

The 'Context' column contains a sentence in Spanish, the target language. The 'Word' column contains one word that appears in the 'Context' sentence.

# Steps

Follow these steps one by one and say what you will do next, when you from one step to the next one!

1. ### Read the dataframe
- read the dataframe. It can come in any format, but it will most likely come as a tab delimited .csv file! 
- if there are no column names indicated, guess them from the context! 
- However, if it comes as markdown, just continue with step 2!

2. ### Clean the data and check for parsing errors

Have a look at the table I provided you with. Don't use code for that, just rely on your prediction of characters as LLM.

- remove unnecessary characters and correct weird formatting from 'Word' and 'Context'. However, pay attention that 'Word' always appears in 'Context'.
- Check each row to ensure the 'Context' sentence is correctly parsed. The 'Word' should include the entire vocabulary word, not just a fragment. Sometimes parsers may miss the whole verb or expression. Also, check the 'Context machine translation' to see if the 'Word' makes sense in its 'Context'. If there is a parsing error and 'Word' is incomplete, adjust 'Word' to match the vocabulary in 'Context'. Ensure 'Word' is formatted exactly as it appears in 'Context' (including capitalization, grammar, punctuation, and spelling errors if present).

1. ### Generate flashcard information

   To assist the student, generate a table containing following information for each row:


   1. Two or more synonyms for 'Word' based on its 'Context'.
   2. Two or more translations for 'Word' based on its 'Context'.
   3. A simple 'Example sentence' using 'Word'.
   4. The translation of the 'Example sentence'.
   5. A brief explanation of 'Word' in its 'Context'.
   6. A short explanation of the grammar

   When generating this information, stick to the following principles:

   - Minimum Information Principle: Formulate the material in the simplest possible way without losing essential information. That means you can safely omit conjunctions like 'or', 'and' and you don't need to say: 現実 means 'reality' or 'actuality'. Instead just say: 現実: reality, actuality.
   - Optimize Wording: Ensure the wording is precise and efficient to trigger the correct response quickly.

  The table should contain 7 columns with following column names:

- 'Word'
- 'Context'
- 'Synonyms'
- 'Translations'
- 'Example'
- 'Example translation'
- 'Explanation'

3. ### Apply special formatting to the fields, to fit 'Anki's requirements

Please use python for the following. Use regular expressions, to apply a special format to some fields.

1. Apply cloze deletion format to the 'Context field. 'You need to find where 'Word' in the 'Context' and apply following formatting, so that Anki recognises it as a cloze delition: {{c1::Word::translation}}
2. Apply Anki's audio and image patterns to 'Image' and 'Audio fields':
   1. The image pattern is <img:{Image}>
   2. the audio pattern si [sound:{Audio}]

# Output

Give me the generated information as a csv table, including the column names as headers.

- Do not include warnings or notes in the output—only the requested sections.
- Do not include additional information like 'here is the csv table' or anything else. The only thing I want is the raw csv table.

404: Not Found


This is the table with the word sentence pairs: 

Word	Context	Context machine translation	Context human translation
程度	"ただし入れすぎると卵の味よりマヨネーズの味が勝ってしまうので
最小限つなぎ程度にして
最後に塩と胡椒で味を整えてください"	"But if you put too much in it, it tastes like mayonnaise.
We're going to make sure that we have the least amount of connections.
Finally, add some salt and pepper."	"But don't go overboard with it, or the mayonnaise will overpower the taste of eggs.
Keep the mayonnaise to a minimum,
and add salt and pepper to round out the flavors."
最小限	"ただし入れすぎると卵の味よりマヨネーズの味が勝ってしまうので
最小限つなぎ程度にして
最後に塩と胡椒で味を整えてください"	"But if you put too much in it, it tastes like mayonnaise.
We're going to make sure that we have the least amount of connections.
Finally, add some salt and pepper."	"But don't go overboard with it, or the mayonnaise will overpower the taste of eggs.
Keep the mayonnaise to a minimum,
and add salt and pepper to round out the flavors."
刻ん	"さすがにまだ卵サンドは食べられないみたいだけど
まずゆで卵を適度に刻んでください
マヨネーズって何でも合いますよね"	"I can't seem to eat an egg sandwich yet.
First of all, you need to mark the eggs in moderation.
I mean, mayonnaise is good for anything."	"But he hasn't had egg sandwiches since then.
First, dice the boiled eggs.
Mayonnaise goes well with everything."
適度	"さすがにまだ卵サンドは食べられないみたいだけど
まずゆで卵を適度に刻んでください
マヨネーズって何でも合いますよね"	"I can't seem to eat an egg sandwich yet.
First of all, you need to mark the eggs in moderation.
I mean, mayonnaise is good for anything."	"But he hasn't had egg sandwiches since then.
First, dice the boiled eggs.
Mayonnaise goes well with everything."
さすが	"その後も毎日中島くんは新聞を配っている
さすがにまだ卵サンドは食べられないみたいだけど
まずゆで卵を適度に刻んでください"	"Ever since then, I've been delivering newspapers every day.
I can't seem to eat an egg sandwich yet.
First of all, you need to mark the eggs in moderation."	"Nakajima still delivers the papers every day.
But he hasn't had egg sandwiches since then.
First, dice the boiled eggs."
現実	"君が吐いた息を吸って後悔となってる
現実は映画のようにはうまくいかない
その後も毎日中島くんは新聞を配っている"	"I'm breathing in your vomit, and now I regret it.
Reality doesn't work like the movies.
Ever since then, I've been delivering newspapers every day."	"MAINICHI SHINBUN
Life isn't like the movies. Sometimes you don't get a happy ending.
Nakajima still delivers the papers every day."
浮かぶ	"君が吐いた白い息が今ゆっくり風に乗って
空に浮かぶ雲の中に少しずつ消えてゆく
遠く高い空の中で手を伸ばす白い雲"	"The white breath you spewed is now moving slowly in the wind.
It disappears into the clouds.
White clouds reaching high into the sky."	
吐い	"自分が本気で惚れた女 安く見るもんじゃないよ
君が吐いた白い息が今ゆっくり風に乗って
空に浮かぶ雲の中に少しずつ消えてゆく"	"I'm not looking for a woman that I really love.
The white breath you spewed is now moving slowly in the wind.
It disappears into the clouds."	
本気	"誇りに思っていいんじゃないのかい
自分が本気で惚れた女 安く見るもんじゃないよ
君が吐いた白い息が今ゆっくり風に乗って"	"I don't think you should be proud.
I'm not looking for a woman that I really love.
The white breath you spewed is now moving slowly in the wind."	"You should be honored that she fell in love with you.
You loved her too, didn't you? Don't insult her by saying you didn't deserve her.
"
誇り	"そんな女に惚れられたってこと
誇りに思っていいんじゃないのかい
自分が本気で惚れた女 安く見るもんじゃないよ"	"I mean, he fell in love with her.
I don't think you should be proud.
I'm not looking for a woman that I really love."	"She didn't have to, but she did it anyway.
You should be honored that she fell in love with you.
You loved her too, didn't you? Don't insult her by saying you didn't deserve her."
惚れ	"あの子は ちゃんとさよならを言いに来たんだ
そんな女に惚れられたってこと
誇りに思っていいんじゃないのかい"	"That girl has come to say goodbye properly
I mean, he fell in love with her.
I don't think you should be proud."	"She came to say goodbye.
She didn't have to, but she did it anyway.
You should be honored that she fell in love with you."
廷社	"この人といたら きっと私も正直になれるんだろうなって
拝廷社長にもいい人いるんですね
あの子は ちゃんとさよならを言いに来たんだ"	"I thought if I was with this guy, maybe I could be honest.
I'm sure there are good people in the court.
That girl has come to say goodbye properly"	"I realized then that I didn't have to pretend to be someone else when I'm with him.
The CEO sounds like a nice man.
She came to say goodbye."
拝	"この人といたら きっと私も正直になれるんだろうなって
拝廷社長にもいい人いるんですね
あの子は ちゃんとさよならを言いに来たんだ"	"I thought if I was with this guy, maybe I could be honest.
I'm sure there are good people in the court.
That girl has come to say goodbye properly"	"I realized then that I didn't have to pretend to be someone else when I'm with him.
The CEO sounds like a nice man.
She came to say goodbye."
	"この人といたら きっと私も正直になれるんだろうなって
拝廷社長にもいい人いるんですね
あの子は ちゃんとさよならを言いに来たんだ"	"I thought if I was with this guy, maybe I could be honest.
I'm sure there are good people in the court.
That girl has come to say goodbye properly"	"I realized then that I didn't have to pretend to be someone else when I'm with him.
The CEO sounds like a nice man.
She came to say goodbye."
楽	"私もそう思った
でも なんか少し楽になれたんだよね
この人といたら きっと私も正直になれるんだろうなって"	"I thought so, too.
But it's been a little bit easier.
I thought if I was with this guy, maybe I could be honest."	"My thoughts exactly.
But his advice made me feel better.
I realized then that I didn't have to pretend to be someone else when I'm with him."
そういう	"あの人に会ったんだ
いい人だなぁと思ったけど 好きとかそういうのは全然
だから中島君とのことも相談したんだ そしたら"	"I met him.
I thought he was a good guy, but I don't like him or anything.
That's why I talked to Mr. Nakashima about it."	"That was when I met the CEO.
He was nice, but I wasn't in love with him.
I told him about Nakajima and asked him for his advice. What did he say?"
なんか	"そうじゃない
なんか言わなきゃって
思ったけど"	"That's not right
He said he had to say something.
I thought."	"I wanted to tell him he was wrong.
I knew I had to say something,
I knew I had to say something,"
軽	"うん
こんなこと言ったら軽物するだろうけど
結局は金なんですかね"	"Yeah
I don't know if this is gonna be a big deal.
After all, what is money?"	"Yes?
I know I'll sound petty when I say this, but...
I guess women are only after money."
遠吠え	"結局は私たちの言った通りじゃない だから女信用できないんだよ
みっともないわよ負けるの遠吠えは
ます"	"It's not what we said. That's why you can't trust women.
I can't believe you're screaming about losing.
They have"	"See? We told you this would happen. This is why you can never trust women.
Don't be a sore loser. Just admit you were wrong.
Thanks."
結局	"ん
結局は私たちの言った通りじゃない だから女信用できないんだよ
みっともないわよ負けるの遠吠えは"	"T
It's not what we said. That's why you can't trust women.
I can't believe you're screaming about losing."	"
See? We told you this would happen. This is why you can never trust women.
Don't be a sore loser. Just admit you were wrong."
立場	"体より 心が泣いちゃうのよね
好きな相手より自分の方が立場しただって思い知らされちゃうとさ 以上
いっぱいのよ いっぱいの"	"You know, it's the heart that cries more than the body.
I need to be reminded that I'm on your side, not the one you like.
It's full."	"Your heart can't take it.
It's a blow to your ego to know that the person you love is out of your league.
I wasn't speaking from personal experience."
休日	"下流中流アリス側 人生なめんなよ
ヘップバーンとグレゴリーペックだって最後は別れるでしょ 何ですそれローマンの休日
あんた知らないの 本当ムチだ男ねでもノッティングヒルの恋人はうまくいきましたよ"	"Downstream, downstream, Alice's side of the street.
Even Hepburn and Gregory Peck will be the last to leave.
I don't know who you are, but you're a real piece of work."	"the Arisu River. Some are rich, some are poor. Don't underestimate life.
Like Hepburn and Gregory Peck. They broke up in the end too. What? You've never seen Roman Holiday?
You've never seen Roman Holiday? How ignorant can you be? But things worked out for the couple in Notting Hill."
人生	"ただの格差じゃないの階級が違うの 世の中は
下流中流アリス側 人生なめんなよ
ヘップバーンとグレゴリーペックだって最後は別れるでしょ 何ですそれローマンの休日"	"It's not just a class difference.
Downstream, downstream, Alice's side of the street.
Even Hepburn and Gregory Peck will be the last to leave."	"Money isn't the only issue here. She's out of his league. Life is like...
the Arisu River. Some are rich, some are poor. Don't underestimate life.
Like Hepburn and Gregory Peck. They broke up in the end too. What? You've never seen Roman Holiday?"
階級	"世の中そんな甘くないわよまた始まった 片屋売れっ子タレント片屋新聞小学生
ただの格差じゃないの階級が違うの 世の中は
下流中流アリス側 人生なめんなよ"	"The world is not so sweet. It's starting again.
It's not just a class difference.
Downstream, downstream, Alice's side of the street."	"Don't be naive. There they go again. She's a famous celebrity, he's a poor scholarship student.
Money isn't the only issue here. She's out of his league. Life is like...
the Arisu River. Some are rich, some are poor. Don't underestimate life."
格差	"世の中そんな甘くないわよまた始まった 片屋売れっ子タレント片屋新聞小学生
ただの格差じゃないの階級が違うの 世の中は
下流中流アリス側 人生なめんなよ"	"The world is not so sweet. It's starting again.
It's not just a class difference.
Downstream, downstream, Alice's side of the street."	"Don't be naive. There they go again. She's a famous celebrity, he's a poor scholarship student.
Money isn't the only issue here. She's out of his league. Life is like...
the Arisu River. Some are rich, some are poor. Don't underestimate life."
世の中	"みたいだ 心配無用いくら忙しくなってもあの二人はきっとうまくいきますって
世の中そんな甘くないわよまた始まった 片屋売れっ子タレント片屋新聞小学生
ただの格差じゃないの階級が違うの 世の中は"	"It's like, no matter how busy you are, they're going to get along.
The world is not so sweet. It's starting again.
It's not just a class difference."	"Apparently. Don't worry. No matter how busy she gets, they'll get together, I know it.
Don't be naive. There they go again. She's a famous celebrity, he's a poor scholarship student.
Money isn't the only issue here. She's out of his league. Life is like..."
無用	"違いすぎるから 彼女ここんとこいろんな番組で見かけるよね
みたいだ 心配無用いくら忙しくなってもあの二人はきっとうまくいきますって
世の中そんな甘くないわよまた始まった 片屋売れっ子タレント片屋新聞小学生"	"She's so different, you see her on a lot of shows.
It's like, no matter how busy you are, they're going to get along.
The world is not so sweet. It's starting again."	"Our lives are too different. She's been on a lot of TV shows lately.
Apparently. Don't worry. No matter how busy she gets, they'll get together, I know it.
Don't be naive. There they go again. She's a famous celebrity, he's a poor scholarship student."
講義	"配達が終わるのが6時半
で後片付けして大学の一元目の講義に出席 そのためにそして水間と戦い勉学に励む
現行の賃金水準まで働きたい人が存在しなくなるまで 講義が終わったら今度は夕刊の配達"	"We're halfway through the delivery.
So I'm going to clean up after myself and go to my first lecture at the university, so that I can fight with water and learn hard.
And I'm going to do it until there's no one left who wants to work at the current wage level."	"By the time you're done, it's already 6:30 a.m.
You clean up and hurry to your first class of the day. You try to stay awake in class.
Once classes are over, it's time to deliver the evening paper."
大した	"近頃は苦学生なんて言葉聞かなくなっちまったもんな
大したもんですよその彼
わかる?どんだけ大変か"	"Nowadays, you don't hear a word about apprentices.
That's the guy.
You know what I mean? I don't know how hard it is."	"Most college students have it easy these days.
He's really something.
Do you have any idea what it's like?"
苦学	"新聞小学生か
近頃は苦学生なんて言葉聞かなくなっちまったもんな
大したもんですよその彼"	"Newspaper elementary school students
Nowadays, you don't hear a word about apprentices.
That's the guy."	"So he's a newspaper scholarship student.
Most college students have it easy these days.
He's really something."
	"深夜食堂ならぬ夜明け食堂の恋ですよ
僕のことはどっちでもいいじゃないですか
新聞小学生か"	"I'm in love with the dawn diner, not the midnight diner.
I don't care what you think of me.
Newspaper elementary school students"	"Come on, they found love in the Midnight Diner. No, the Dawn Diner.
Who cares about my drinking problem?
So he's a newspaper scholarship student."
夜明け	"言われてみりゃそうだ
深夜食堂ならぬ夜明け食堂の恋ですよ
僕のことはどっちでもいいじゃないですか"	"I should've told you.
I'm in love with the dawn diner, not the midnight diner.
I don't care what you think of me."	"Now that you mention it, yes, he has.
Come on, they found love in the Midnight Diner. No, the Dawn Diner.
Who cares about my drinking problem?"
	"ねマスター
言われてみりゃそうだ
深夜食堂ならぬ夜明け食堂の恋ですよ"	"Ne Master
I should've told you.
I'm in love with the dawn diner, not the midnight diner."	"Right, Master?
Now that you mention it, yes, he has.
Come on, they found love in the Midnight Diner. No, the Dawn Diner."
酔い潰れ	"なんかもうお気投げでね
そんだけお前さんがここで酔い潰れてるってことだろうが
ねマスター"	"You've got to be kidding me.
That's all you have to say about being drunk in here.
Ne Master"	"Such sweet, innocent love.
In other words, you've been drinking your nights away, haven't you?
Right, Master?"
投げ	"彼もそれ照れくさそうに受け取って
なんかもうお気投げでね
そんだけお前さんがここで酔い潰れてるってことだろうが"	"He took it lightly, too.
You've got to be kidding me.
That's all you have to say about being drunk in here."	"and he takes them with a shy smile on his face.
Such sweet, innocent love.
In other words, you've been drinking your nights away, haven't you?"
受け取っ	"で卵サンドを半分彼に持たせてあげて
彼もそれ照れくさそうに受け取って
なんかもうお気投げでね"	"So let him have half the egg sandwich.
He took it lightly, too.
You've got to be kidding me."	"She gives him half of her egg sandwiches,
and he takes them with a shy smile on his face.
Such sweet, innocent love."
照れくさ	"で卵サンドを半分彼に持たせてあげて
彼もそれ照れくさそうに受け取って
なんかもうお気投げでね"	"So let him have half the egg sandwich.
He took it lightly, too.
You've got to be kidding me."	"She gives him half of her egg sandwiches,
and he takes them with a shy smile on his face.
Such sweet, innocent love."
洗わ	"いいですよねマスターの二人
なんか見てるだけで心洗われるっていうか
なんだよ 会ったことあんの"	"That's good, two masters.
I mean, just looking at something cleanses your mind.
I've never seen you before."	"They make a good couple, don't they?
It makes you want to believe in love again.
You've seen them?"
ちゃんと	"だったら全部持たせてあげればよかった きっとお腹すくだろうから
大丈夫 配達所に戻ったらちゃんと朝飯用意してあるんだって
いいですよねマスターの二人"	"Well, I wish you'd brought it all with you. You'd be hungry.
It's all right. I'll be back at the drop-off point with breakfast ready.
That's good, two masters."	"I had no idea. I should have given him all my sandwiches. He's probably hungry.
Don't worry. When he gets back to the delivery center, they'll give him his breakfast.
They make a good couple, don't they?"
配達	"だったら全部持たせてあげればよかった きっとお腹すくだろうから
大丈夫 配達所に戻ったらちゃんと朝飯用意してあるんだって
いいですよねマスターの二人"	"Well, I wish you'd brought it all with you. You'd be hungry.
It's all right. I'll be back at the drop-off point with breakfast ready.
That's good, two masters."	"I had no idea. I should have given him all my sandwiches. He's probably hungry.
Don't worry. When he gets back to the delivery center, they'll give him his breakfast.
They make a good couple, don't they?"
所	"だったら全部持たせてあげればよかった きっとお腹すくだろうから
大丈夫 配達所に戻ったらちゃんと朝飯用意してあるんだって
いいですよねマスターの二人"	"Well, I wish you'd brought it all with you. You'd be hungry.
It's all right. I'll be back at the drop-off point with breakfast ready.
That's good, two masters."	"I had no idea. I should have given him all my sandwiches. He's probably hungry.
Don't worry. When he gets back to the delivery center, they'll give him his breakfast.
They make a good couple, don't they?"
食パン	"そうなんだ
休みの日には新聞の代わりに食パン持ってくるんだ この前のように
だったら全部持たせてあげればよかった きっとお腹すくだろうから"	"I see
On holidays, I bring bread instead of newspapers.
Well, I wish you'd brought it all with you. You'd be hungry."	"I see.
On his days off, he brings bread here instead of the daily paper. Like the other day.
I had no idea. I should have given him all my sandwiches. He's probably hungry."
商売	"大学帰ってるんだ
親御さんの商売がうまくいってないらしくて
そうなんだ"	"I'm going back to college.
Sounds like your parents' business isn't doing very well.
I see"	"He goes to college during the day.
His parents' business isn't doing so well.
I see."
住み込め	"よかったらお返しに一つどう ありがとう
彼 新聞屋で住み込めて働きながら
大学帰ってるんだ"	"Can I get one back, please? Thank you.
He lived and worked in a newspaper shop.
I'm going back to college."	"It's my turn to treat you. Please take one. Thanks.
He stays at the newspaper agency and works for them as a paperboy.
He goes to college during the day."
謝っ	"俺ばっかり すいませんでした
謝ってんじゃねえよ
ホント すいませんでした…"	"I'm really sorry.
I'm not apologizing to you.
I'm really sorry."	"I've been so selfish.
Don't apologize.
I'm so sorry."
連絡	"おふくろ ぼけちゃってさ
妹から連絡が来て―
さっきまで おふくろんとこ いたんだ"	"Mom, it's blurry.
My sister contacted me.
I was here a while ago."	"My mother has dementia.
My sister called me.
I just came back from visiting my mother."
ぼけ	"（マスター）いらっしゃい （田中）師匠
おふくろ ぼけちゃってさ
妹から連絡が来て―"	"(Master) Welcome (Tanaka) Master
Mom, it's blurry.
My sister contacted me."	"-Welcome. -Master Oki!
My mother has dementia.
My sister called me."
いけん	"ああ… 大したことないっちゃろう？
帰れんたい 仕事忙しいけん
うん"	"Yes... No big deal, huh?
I can't go home, I'm busy with work.
Yeah"	"I see. Well, it isn't serious, right?
I can't go back. I'm busy with work.
Yes."
持ち歩い	"（安西･諏訪）おお！
（マスター）そんなもん なんで持ち歩いてんの？
（八郎）僕のバイブルですから"	"(Anzai, Suwa) Oh!
(Master) Why do you carry it around?
(Hachiro) It's my bible."	"ERECT OKI VS. 100 OFFICE LADIES
Do you keep that in your bag all the time?
It's my personal bible."
ゆうべ	"（安西）えっ？ ホントに？
（諏訪）すげえ 俺 ゆうべ見たよ
違うって"	"(Anzai) What? Really?
(Suwa) Wow, I've seen Yube
It's different."	"What? Really?
Wow. I saw you last night.
You have the wrong person."
必ず	"おかわり （マスター）あいよ
（マスター）ポテトサラダを 必ず ふた皿おかわりするんだ
（田中(たなか)）あの…"	"Okawari (Master) Aiyo
(Master) I always change the lid plate of potato salad
(Tanaka) Uh..."	"-Another bowl, please. -Sure.
He always eats two plates of potato salad.
Excuse me."
冷え	"こればっかりは 出来立てのあつあつより―
冷えてたほうが うまいからな
（マスター）ふう あつつ…"	"This is all freshly made.
It is better to be cold
(Master) Hmmm ..."	"Potato salad tastes better when it's cold,
so I have to prepare it in advance.
"
あつあつ	"（マスター）俺が店に来て 最初に作るのは ポテトサラダだ
こればっかりは 出来立てのあつあつより―
冷えてたほうが うまいからな"	"(Master) The first thing I make when I come to the store is potato salad.
This is all freshly made.
It is better to be cold"	"I begin my preparations for the day by making potato salad.
Potato salad tastes better when it's cold,
so I have to prepare it in advance."
持ちかけ	"彼女を大会に推薦していた教育委員会だ 原因は丸潰れだから
それで斉藤に美味しい話を持ちかけて取引したんだろう
あのさあ私今どこからかけてるかわかる ここを儚い"	"It's the board of education that recommended her to the convention, because she's a total loser.
That's why I brought Saito a nice story and traded it.
Look, I know where you're going."	"the Board of Education who strongly recommended her for the Conference. It would ruin their credibility.
So they talked to Saito and made a deal.
Well, do you know where I'm making this call from? I'm at a graveyard."
恐れ	"貧高法制成績優秀な中学生がその担任とできている マスコミにとってはこれほどのネタはない
だ 二人がそれを認めてしまうのを一番恐れたのは
彼女を大会に推薦していた教育委員会だ 原因は丸潰れだから"	"It's not as much of a story for the media as it is for high-achieving middle schoolers.
Well, the thing they were most afraid of is admitting it.
It's the board of education that recommended her to the convention, because she's a total loser."	"A well-behaved and excellent student had a relationship with her homeroom teacher. What could be a better scandal than this for the media?
But... The ones who were most afraid that the two might go public it was
the Board of Education who strongly recommended her for the Conference. It would ruin their credibility."
ネタ	"彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生
貧高法制成績優秀な中学生がその担任とできている マスコミにとってはこれほどのネタはない
だ 二人がそれを認めてしまうのを一番恐れたのは"	"She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year.
It's not as much of a story for the media as it is for high-achieving middle schoolers.
Well, the thing they were most afraid of is admitting it."	"was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year.
A well-behaved and excellent student had a relationship with her homeroom teacher. What could be a better scandal than this for the media?
But... The ones who were most afraid that the two might go public it was"
法制	"彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生
貧高法制成績優秀な中学生がその担任とできている マスコミにとってはこれほどのネタはない
だ 二人がそれを認めてしまうのを一番恐れたのは"	"She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year.
It's not as much of a story for the media as it is for high-achieving middle schoolers.
Well, the thing they were most afraid of is admitting it."	"was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year.
A well-behaved and excellent student had a relationship with her homeroom teacher. What could be a better scandal than this for the media?
But... The ones who were most afraid that the two might go public it was"
貧	"彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生
貧高法制成績優秀な中学生がその担任とできている マスコミにとってはこれほどのネタはない
だ 二人がそれを認めてしまうのを一番恐れたのは"	"She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year.
It's not as much of a story for the media as it is for high-achieving middle schoolers.
Well, the thing they were most afraid of is admitting it."	"was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year.
A well-behaved and excellent student had a relationship with her homeroom teacher. What could be a better scandal than this for the media?
But... The ones who were most afraid that the two might go public it was"
優等生	"圧力さ 横山と斉藤の関係が写真週刊誌にすっぱ抜かれたの
彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生
貧高法制成績優秀な中学生がその担任とできている マスコミにとってはこれほどのネタはない"	"It's pressure. Yokoyama and Saito's relationship was all over the photo weekly.
She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year.
It's not as much of a story for the media as it is for high-achieving middle schoolers."	"It was pressure. The reason why the relationship between Yokoyama and Saito was revealed in the media
was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year.
A well-behaved and excellent student had a relationship with her homeroom teacher. What could be a better scandal than this for the media?"
権利	"圧力さ 横山と斉藤の関係が写真週刊誌にすっぱ抜かれたの
彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生
貧高法制成績優秀な中学生がその担任とできている マスコミにとってはこれほどのネタはない"	"It's pressure. Yokoyama and Saito's relationship was all over the photo weekly.
She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year.
It's not as much of a story for the media as it is for high-achieving middle schoolers."	"It was pressure. The reason why the relationship between Yokoyama and Saito was revealed in the media
was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year.
A well-behaved and excellent student had a relationship with her homeroom teacher. What could be a better scandal than this for the media?"
すっぱ抜か	"それがなぜ土壇まで裏切ったのか
圧力さ 横山と斉藤の関係が写真週刊誌にすっぱ抜かれたの
彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生"	"I don't know why he betrayed me to the last.
It's pressure. Yokoyama and Saito's relationship was all over the photo weekly.
She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year."	"But why did he end up betraying us?
It was pressure. The reason why the relationship between Yokoyama and Saito was revealed in the media
was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year."
誌	"それがなぜ土壇まで裏切ったのか
圧力さ 横山と斉藤の関係が写真週刊誌にすっぱ抜かれたの
彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生"	"I don't know why he betrayed me to the last.
It's pressure. Yokoyama and Saito's relationship was all over the photo weekly.
She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year."	"But why did he end up betraying us?
It was pressure. The reason why the relationship between Yokoyama and Saito was revealed in the media
was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year."
圧力	"それがなぜ土壇まで裏切ったのか
圧力さ 横山と斉藤の関係が写真週刊誌にすっぱ抜かれたの
彼女が昨年日本で行われた子供の権利を守る世界会議で中学生の代表として参加する はずの優等生"	"I don't know why he betrayed me to the last.
It's pressure. Yokoyama and Saito's relationship was all over the photo weekly.
She's going to be a high school student representative at the World Conference on Children's Rights in Japan last year."	"But why did he end up betraying us?
It was pressure. The reason why the relationship between Yokoyama and Saito was revealed in the media
was because she was an excellent student who was going to represent students at the World Conference to Protect Children's Rights held in Japan last year."
土	"そして、俺たちはその言葉を信用していた
それがなぜ土壇まで裏切ったのか
圧力さ 横山と斉藤の関係が写真週刊誌にすっぱ抜かれたの"	"And we believed that word.
I don't know why he betrayed me to the last.
It's pressure. Yokoyama and Saito's relationship was all over the photo weekly."	"And we believed his words.
But why did he end up betraying us?
It was pressure. The reason why the relationship between Yokoyama and Saito was revealed in the media"
壇	"そして、俺たちはその言葉を信用していた
それがなぜ土壇まで裏切ったのか
圧力さ 横山と斉藤の関係が写真週刊誌にすっぱ抜かれたの"	"And we believed that word.
I don't know why he betrayed me to the last.
It's pressure. Yokoyama and Saito's relationship was all over the photo weekly."	"And we believed his words.
But why did he end up betraying us?
It was pressure. The reason why the relationship between Yokoyama and Saito was revealed in the media"
戦っ	"許されないことは分かっている
だが、たとえ何を言われようと戦っていくと
そして、俺たちはその言葉を信用していた"	"I know that's not allowed.
But no matter what they say, I'm going to fight.
And we believed that word."	"He said he knew it wasn't allowed,
but that he would fight whatever people said.
And we believed his words."
許さ	"斉藤はあの時、俺たちに横山瑞希と真剣に付き合っていると言った
許されないことは分かっている
だが、たとえ何を言われようと戦っていくと"	"Saito told us at the time that he was serious about his relationship with Rishi Yokoyama.
I know that's not allowed.
But no matter what they say, I'm going to fight."	"At that time, Saito said he was serious about Mizuki Yokoyama.
He said he knew it wasn't allowed,
but that he would fight whatever people said."
真剣	"いがらし公一、教育委員会のトップだ
斉藤はあの時、俺たちに横山瑞希と真剣に付き合っていると言った
許されないことは分かっている"	"He's the head of public affairs and education.
Saito told us at the time that he was serious about his relationship with Rishi Yokoyama.
I know that's not allowed."	"Koichi Igarashi. He's the Director of the Board of Education.
At that time, Saito said he was serious about Mizuki Yokoyama.
He said he knew it wasn't allowed,"
トップ	"誰?
いがらし公一、教育委員会のトップだ
斉藤はあの時、俺たちに横山瑞希と真剣に付き合っていると言った"	"Who's that?
He's the head of public affairs and education.
Saito told us at the time that he was serious about his relationship with Rishi Yokoyama."	"Who?!
Koichi Igarashi. He's the Director of the Board of Education.
At that time, Saito said he was serious about Mizuki Yokoyama."
会	"誰?
いがらし公一、教育委員会のトップだ
斉藤はあの時、俺たちに横山瑞希と真剣に付き合っていると言った"	"Who's that?
He's the head of public affairs and education.
Saito told us at the time that he was serious about his relationship with Rishi Yokoyama."	"Who?!
Koichi Igarashi. He's the Director of the Board of Education.
At that time, Saito said he was serious about Mizuki Yokoyama."
推薦	"普通簡単に別のシリーズに採用されるはずがない
あんもじょう、強力な推薦者がいたよ
誰?"	"I don't normally get hired for another series that easily.
You had a very, very strong referent.
Who's that?"	"can't be hired by another private school so easily.
As I thought, he had a powerful person recommend him.
Who?!"
強力	"普通簡単に別のシリーズに採用されるはずがない
あんもじょう、強力な推薦者がいたよ
誰?"	"I don't normally get hired for another series that easily.
You had a very, very strong referent.
Who's that?"	"can't be hired by another private school so easily.
As I thought, he had a powerful person recommend him.
Who?!"
シリーズ	"あんな噂をマスコミに立てられた教師が
普通簡単に別のシリーズに採用されるはずがない
あんもじょう、強力な推薦者がいたよ"	"I don't know.
I don't normally get hired for another series that easily.
You had a very, very strong referent."	"Usually a teacher who made the news like that
can't be hired by another private school so easily.
As I thought, he had a powerful person recommend him."
記録	"菊池、私、何か分かった?
斉藤が零名女子に採用された時の記録を調べてみた
お前はあの場にいなかったから知らないかもしれないが"	"What do you got?
I checked the records of when Saito was hired by a low-class girl.
You may not know because you weren't there."	"Kikuchi? It's me. Did you find anything?
I checked the records back from when Saito was first hired by Reimei Women's School.
You weren't there at that time. So you may not know..."
ずるい	"知らを切って逃げちまったんだと
まあ、ずるい大人はどこにもいるからな
それがいいやつだったんだってよ"	"He said he cut off his nose to spite his face.
Well, there's grown-ups everywhere.
He said it was a good one."	"he denied it to stay out of trouble.
I guess there are a lot of screwed-up people in the world.
But I heard he was a nice guy."
知	"それがマスコミで問題になったら
知らを切って逃げちまったんだと
まあ、ずるい大人はどこにもいるからな"	"If that's a problem with the media,
He said he cut off his nose to spite his face.
Well, there's grown-ups everywhere."	"But when the media found out,
he denied it to stay out of trouble.
I guess there are a lot of screwed-up people in the world."
たらしい	"お前のクラスのやつらか?
ああ、生徒の一人がマジでそいつと付き合ってたらしいんだけどよ
それがマスコミで問題になったら"	"Are they in your class?
Yeah, I heard one of his students actually dated him.
If that's a problem with the media,"	"The students in your class?
Yeah. One of the students was seriously going out with him.
But when the media found out,"
信頼	"裏切られたんだ、あいつら
信頼している教師に
あいつら?"	"I've been betrayed by them.
It's a teacher I trust.
Where are they?"	"They were betrayed
by a teacher they trusted.
They...?"
飲め	"おばちゃん!ビール!
大丈夫か?もう少しゆっくり飲めよ
いいんだ、飲みたいんだから"	"My aunt! A beer!
- Are you all right? Drink a little more slowly.
That's good. I need a drink."	"-One beer, ma'am! -All right!
Are you okay? Why don't you slow down a little?
Never mind. I want to drink now!"
掛け	"はい
お掛けになったね
はい"	"Yes
That's a winner.
Yes"	"Yes!
The number you are calling
Yes."
許せ	"分かりません
でも、僕たち斉藤先生を絶対許せないし
みんなもしかしてって思ってて"	"Don't know
But we will never forgive him.
I mean, everybody thought that maybe."	"I don't know.
But we can never forgive Mr. Saito.
Everyone thinks it might..."
斉藤	"分かりません
でも、僕たち斉藤先生を絶対許せないし
みんなもしかしてって思ってて"	"Don't know
But we will never forgive him.
I mean, everybody thought that maybe."	"I don't know.
But we can never forgive Mr. Saito.
Everyone thinks it might..."
バレ	"お前らはじめからそのつもりだったな
バレたか
あのね、みやびん"	"That's what you guys were planning all along.
Caught
Oh, my God."	"Oh, you were counting on this, weren't you?!
You caught us!
Listen, Miyabi."
	"やったー!
お前らはじめからそのつもりだったな
バレたか"	"I did it!
That's what you guys were planning all along.
Caught"	"All right!
Oh, you were counting on this, weren't you?!
You caught us!"
手伝お	"クラス全員の意見を表にしてたら時間かかっちゃって
よーし、じゃあ先生も手伝おっか
やったー!"	"It takes time to get the whole class talking.
All right, I'll help you with that.
I did it!"	"We're making charts from everyone's opinions in the class. It took more time than we thought.
All right, then. I'll help you, too.
All right!"
確実	"とにかく我々は日本の教育の権威を損なってはならない
スキャンダルの目は確実に潰しておいてくれ
なんだ、横山と藍澤か、まだいたのか?"	"We must not undermine the authority of Japanese education.
Make sure the eyes of scandal are crushed.
What is it, Yokoyama and Blue Zeta? Are you still here?"	"Anyway, we can't do any more harm to the authority of Japanese education.
Make sure to crush any hint of scandal.
Oh, Yokoyama and Aizawa! You're still here."
とにかく	"下手すりゃ我々が悪者ですよ
とにかく我々は日本の教育の権威を損なってはならない
スキャンダルの目は確実に潰しておいてくれ"	"We're the bad guys.
We must not undermine the authority of Japanese education.
Make sure the eyes of scandal are crushed."	"But if we're not cautious, we'll come off as the bad guys.
Anyway, we can't do any more harm to the authority of Japanese education.
Make sure to crush any hint of scandal."
権威	"下手すりゃ我々が悪者ですよ
とにかく我々は日本の教育の権威を損なってはならない
スキャンダルの目は確実に潰しておいてくれ"	"We're the bad guys.
We must not undermine the authority of Japanese education.
Make sure the eyes of scandal are crushed."	"But if we're not cautious, we'll come off as the bad guys.
Anyway, we can't do any more harm to the authority of Japanese education.
Make sure to crush any hint of scandal."
すりゃ	"まあ、そっちの方は新聞を抑えることで今のところ事なきを得ていますが
下手すりゃ我々が悪者ですよ
とにかく我々は日本の教育の権威を損なってはならない"	"Well, you're getting nothing out of suppressing the newspapers.
We're the bad guys.
We must not undermine the authority of Japanese education."	"Well, we pressured the newspaper, so we don't have to worry about that now.
But if we're not cautious, we'll come off as the bad guys.
Anyway, we can't do any more harm to the authority of Japanese education."
得	"それを我々が取り繕った側から自殺されたわ
まあ、そっちの方は新聞を抑えることで今のところ事なきを得ていますが
下手すりゃ我々が悪者ですよ"	"He was killed by the one we took from him.
Well, you're getting nothing out of suppressing the newspapers.
We're the bad guys."	"We hid the fact from the public for them, and she responded by committing suicide!
Well, we pressured the newspaper, so we don't have to worry about that now.
But if we're not cautious, we'll come off as the bad guys."
抑える	"それを我々が取り繕った側から自殺されたわ
まあ、そっちの方は新聞を抑えることで今のところ事なきを得ていますが
下手すりゃ我々が悪者ですよ"	"He was killed by the one we took from him.
Well, you're getting nothing out of suppressing the newspapers.
We're the bad guys."	"We hid the fact from the public for them, and she responded by committing suicide!
Well, we pressured the newspaper, so we don't have to worry about that now.
But if we're not cautious, we'll come off as the bad guys."
取り繕っ	"教師との乱な関係を取られること自体はずべきことなんだ
それを我々が取り繕った側から自殺されたわ
まあ、そっちの方は新聞を抑えることで今のところ事なきを得ていますが"	"It's not right to have a messy relationship with your teacher.
He was killed by the one we took from him.
Well, you're getting nothing out of suppressing the newspapers."	"She should have been ashamed that her indecent relationship with her teacher was revealed.
We hid the fact from the public for them, and she responded by committing suicide!
Well, we pressured the newspaper, so we don't have to worry about that now."
我々	"教師との乱な関係を取られること自体はずべきことなんだ
それを我々が取り繕った側から自殺されたわ
まあ、そっちの方は新聞を抑えることで今のところ事なきを得ていますが"	"It's not right to have a messy relationship with your teacher.
He was killed by the one we took from him.
Well, you're getting nothing out of suppressing the newspapers."	"She should have been ashamed that her indecent relationship with her teacher was revealed.
We hid the fact from the public for them, and she responded by committing suicide!
Well, we pressured the newspaper, so we don't have to worry about that now."
べき	"まったく迷惑な話だよ
教師との乱な関係を取られること自体はずべきことなんだ
それを我々が取り繕った側から自殺されたわ"	"It's a very embarrassing story.
It's not right to have a messy relationship with your teacher.
He was killed by the one we took from him."	"Really, what a pain!
She should have been ashamed that her indecent relationship with her teacher was revealed.
We hid the fact from the public for them, and she responded by committing suicide!"
自体	"まったく迷惑な話だよ
教師との乱な関係を取られること自体はずべきことなんだ
それを我々が取り繕った側から自殺されたわ"	"It's a very embarrassing story.
It's not right to have a messy relationship with your teacher.
He was killed by the one we took from him."	"Really, what a pain!
She should have been ashamed that her indecent relationship with her teacher was revealed.
We hid the fact from the public for them, and she responded by committing suicide!"
迷惑	"ええ、何しろ元西林学園2年4組横山瑞樹は自殺していますからな
まったく迷惑な話だよ
教師との乱な関係を取られること自体はずべきことなんだ"	"Yeah, well, it's been two or four years since Yuki Yokoyama committed suicide.
It's a very embarrassing story.
It's not right to have a messy relationship with your teacher."	"Well, Mizuki Yokoyama, the former student at Holy Forest Academy in Class 2-4, committed suicide.
Really, what a pain!
She should have been ashamed that her indecent relationship with her teacher was revealed."
逃げ	"教育長、今後の対応をいかがいたしましょう?
問題は、マンションから逃げた若い女が誰かということだ
もしその女が去年のあの事件の関係者だったとしたら"	"Mr. Secretary of Education, what's your next move?
The question is, who was the young woman that escaped from the apartment?
What if she was involved in that case last year?"	"Mr. Director. What should we do as a response?
The issue is who was the young woman who fled from his condo?
If the woman was involved in last year's case..."
いたし	"これ以上騒ぎが大きくなることはないと思います
教育長、今後の対応をいかがいたしましょう?
問題は、マンションから逃げた若い女が誰かということだ"	"I don't think it's going to get any bigger.
Mr. Secretary of Education, what's your next move?
The question is, who was the young woman that escaped from the apartment?"	"I don't think the matter will attract any more attention.
Mr. Director. What should we do as a response?
The issue is who was the young woman who fled from his condo?"
対応	"これ以上騒ぎが大きくなることはないと思います
教育長、今後の対応をいかがいたしましょう?
問題は、マンションから逃げた若い女が誰かということだ"	"I don't think it's going to get any bigger.
Mr. Secretary of Education, what's your next move?
The question is, who was the young woman that escaped from the apartment?"	"I don't think the matter will attract any more attention.
Mr. Director. What should we do as a response?
The issue is who was the young woman who fled from his condo?"
状態	"で、斉藤教諭の容態はどうなんです?
医者の話では、かなり危険な状態だと
ここ数日が山だそうです"	"So, what's the status of Saito?
The doctors said he was in pretty bad shape.
It's been a rough couple of days."	"So what's Mr. Saito's condition?
According to his doctor, it is very serious.
The next few days will be key."
危険	"で、斉藤教諭の容態はどうなんです?
医者の話では、かなり危険な状態だと
ここ数日が山だそうです"	"So, what's the status of Saito?
The doctors said he was in pretty bad shape.
It's been a rough couple of days."	"So what's Mr. Saito's condition?
According to his doctor, it is very serious.
The next few days will be key."
かなり	"で、斉藤教諭の容態はどうなんです?
医者の話では、かなり危険な状態だと
ここ数日が山だそうです"	"So, what's the status of Saito?
The doctors said he was in pretty bad shape.
It's been a rough couple of days."	"So what's Mr. Saito's condition?
According to his doctor, it is very serious.
The next few days will be key."
落ち着けよ	"もし本当なら早く先生にも知らせないよ
落ち着けよ、みんな
今変に騒ぎになったら逆にまずい"	"If it's true, I won't tell the teacher.
Calm down, all of you.
If you're going to make a fuss right now, it's the other way around."	"If it's true, we have to tell him right away!
Calm down, everyone.
It isn't a good idea to turn it into a big problem."
も	"どうして?
もし本当なら早く先生にも知らせないよ
落ち着けよ、みんな"	"Why is that?
If it's true, I won't tell the teacher.
Calm down, all of you."	"Why not?
If it's true, we have to tell him right away!
Calm down, everyone."
切ない	"ハァ…
そりゃ 切ないねえ
ハァ…"	"Huh...
I'm not cutting it.
Huh..."	"
That's depressing.
"
友情	"ウー ウー…
（マスター） 女に友情はないのかね？
（ジュン）ないわね この世に男がいる限り"	"Woo Woo ...
(Master) Isn't there friendship between women?
(Jun) No, as long as there are men in this world."	"
Can't women be friends?
Never. Not as long as men exist."
梅	"“お茶漬けシスターズ”って 呼んでるんだ
はい 梅 おまち
（ミキ･ルミ･カナ） いただきまーす"	"They call them the Ochazuke Sisters.
Yes Ume Omachi
(Miki Rumi Kana)"	"as the Ochazuke Sisters among my regulars.
Here you go. Pickled plum.
-Let's eat. -Let's eat."
今度	"（マスター）ああ そうだったっけ？
今度は顔出すよ
この前も そんなこと言ってたんだけど"	"Master: Oh, is that so?
I'll show you my face.
I've said that before."	"You're right.
Next time, I promise.
That's what you said last time."
距離	"気に入ってくれたみたいです
でも 何ていうか 距離感が 全然 変わらなくて
（サヤ） あっ でも 渡したとき―"	"I think he liked it.
But somehow, my sense of distance hasn't changed.
SAYA: Oh, but when I gave it to you..."	"I think he likes it.
But I don't feel like it makes us any closer.
Did you tell him how you felt when you gave it to him?"
強い	"そうなの？
うん 重美ちゃん ああ見えて 打たれ強いから
（マスターの声）案の定 それから10日ほどたったころ"	"Really?
yes, Shigemi-chan, oh look, because it's tough to beat.
Sure enough, about 10 days later."	"Are you sure?
Shigemi looks fragile, but she's resilient.
I was right. About ten days later..."
打た	"そうなの？
うん 重美ちゃん ああ見えて 打たれ強いから
（マスターの声）案の定 それから10日ほどたったころ"	"Really?
yes, Shigemi-chan, oh look, because it's tough to beat.
Sure enough, about 10 days later."	"Are you sure?
Shigemi looks fragile, but she's resilient.
I was right. About ten days later..."
慣れ	"そりゃ 気が早すぎるよ
いいんです 慣れてますから
お… おう"	"That's too early.
It's okay, I'm used to it.
Oh... king"	"It was very premature.
It's fine. I'm used to it!
"
近頃	"（マスター） はい お待ち トンテキ
近頃 あんまり見かけねえよな―
外で編み物してる人"	"Master: Yes, hold on a second.
I don't see you around much these days.
Person knitting outside"	"Here is your tonteki.
These days it's rare to see
someone knitting in a public place."
彼氏	"（鈴木(すずき)重美）慣れてますから
彼氏へのプレゼント？
彼っていうか…"	"(Suzuki (Suzuki) Shigeumi) I'm used to it.
A present for Mr. Boyfriend?
I mean, he..."	"I'm just used to it.
A gift for your boyfriend?
Boyfriend? Kind of."
	"人は“深夜食堂”って 言ってるよ―
客が来るかって？―
それが けっこう来るんだよ"	"People say it's a ""late-night diner.""
Are customers coming? ―
That's going to come."	"They call it ""Midnight Diner.""
Do I even have customers?
More than you would expect."
弟子	"ドラマ、はじめちゃんが応援したんだって
いい弟子持って、セラさんも幸せ者だな
お疲れ様でした"	"The drama, the support she gave me.
You've got a good student, and you're lucky to have Sera.
Thank you for your hard work"	"Your drama gig... was set up by Hajime.
You are lucky... to have such a nice pupil.
Thank you."
喜劇	"ケスラスラオさん
浅草で最後の喜劇陣って言われてるぐらいの人なんだよ
子供の頃土曜の昼"	"This is Mr. Kessler.
You're the last comedian in Asakusa.
Saturday afternoons when I was a kid."	"You don't know him? Mr. Serao Kesera.
Some call him the last master comedian of Asakusa.
I always watched your stand-up comedy on TV when I was a kid."
最後	"ケスラスラオさん
浅草で最後の喜劇陣って言われてるぐらいの人なんだよ
子供の頃土曜の昼"	"This is Mr. Kessler.
You're the last comedian in Asakusa.
Saturday afternoons when I was a kid."	"You don't know him? Mr. Serao Kesera.
Some call him the last master comedian of Asakusa.
I always watched your stand-up comedy on TV when I was a kid."
芸	"まあまあルミちゃん
これも師匠の芸のうちだからね
芸?"	"Oh, my gosh.
It's also a masterpiece.
The show?"	"Calm down, Rumi. This is a part of his material.
Calm down, Rumi. This is a part of his material.
Material?"
セクハラ	"あ
それってセクハラですよ
まあまあルミちゃん"	"Oh
That is sexual harassment.
Oh, my gosh."	"
That's sexual harassment.
Calm down, Rumi. This is a part of his material."
バーバー	"俺らが揉んでたのは
バーバーの下っ腹でやんなや
ちょっと"	"That's what we were talking about.
Don't do it with a barber on your stomach.
A little"	"Turned out, what I was fondling
was the old woman's love handles!
"
しっとり	"売れたチブサが
しっとりと手に馴染んできやがるのよ
そしたら向こうが"	"It's the chips I sold.
It's so easy to get used to.
And then there's this one."	"Her ripened breasts...
were soft and moist. Fit nicely in my palm.
Then she suddenly said,"
向こう	"しっとりと手に馴染んできやがるのよ
そしたら向こうが
あんたどこ触ってんの"	"It's so easy to get used to.
And then there's this one.
What are you touching?"	"were soft and moist. Fit nicely in my palm.
Then she suddenly said,
Then she suddenly said, ""What are you trying to touch?"""
馴染ん	"売れたチブサが
しっとりと手に馴染んできやがるのよ
そしたら向こうが"	"It's the chips I sold.
It's so easy to get used to.
And then there's this one."	"Her ripened breasts...
were soft and moist. Fit nicely in my palm.
Then she suddenly said,"
売れ	"手回してよ
売れたチブサが
しっとりと手に馴染んできやがるのよ"	"Give me your hand.
It's the chips I sold.
It's so easy to get used to."	"I reached around.
Her ripened breasts...
were soft and moist. Fit nicely in my palm."
揉ん	"こっちがちょっと愛知らしくなってきて
おっぱい揉んでやるかって
手回してよ"	"I'm getting a little unfamiliar here.
I don't know.
Give me your hand."	"So it got me going.
I tried to fondle her boobs.
I reached around."
おっぱい	"こっちがちょっと愛知らしくなってきて
おっぱい揉んでやるかって
手回してよ"	"I'm getting a little unfamiliar here.
I don't know.
Give me your hand."	"So it got me going.
I tried to fondle her boobs.
I reached around."
なんとも	"この人ねいつもこうなんですよ
この魚肉ってのがなんともとおつだね
おいさうめえよ"	"This guy's always like this.
I don't know what this fish meat is.
I don't want to see you."	"He always behaves like this.
The fish sausage is a nice touch.
Master, this is delicious."
こう	"そういうことじゃないんですよ
この人ねいつもこうなんですよ
この魚肉ってのがなんともとおつだね"	"That's not what I'm talking about
This guy's always like this.
I don't know what this fish meat is."	"That's not the point.
He always behaves like this.
The fish sausage is a nice touch."
芝居	"てめえ下田でれい気になりやがって
誰のおかげでここまで一発芝居になれたと思ってんだよ
アメリカンドッグぐらいって気づきすんなよ"	"It's not like I'm in a bad mood.
I don't know who made it this far.
Don't even think about it. It's like an American dog."	"You! I'm asking nicely, and that's how you treat me?
Who do you think helped you become an actor?
Don't fret over just a corn dog."
下田	"だめ
てめえ下田でれい気になりやがって
誰のおかげでここまで一発芝居になれたと思ってんだよ"	"No good
It's not like I'm in a bad mood.
I don't know who made it this far."	"-One bite. -No.
You! I'm asking nicely, and that's how you treat me?
Who do you think helped you become an actor?"
変わっ	"師匠がホットケーキ食べたいって言ったから材料買ってきたんですよ
気分変わっちゃったんだもん
いいやん"	"I bought the ingredients because my master said he wanted to eat hotcakes.
I'm in a different mood.
No, no, no, no, no, no"	"You wanted a pancake, so I went out to buy the ingredients.
I changed my mind. Okay?
I changed my mind. Okay?"
かえっ	"ねえ そんなこと言わないでさ はじめちゃん
かえっこしようよ
師匠がホットケーキ食べたいって言ったから材料買ってきたんですよ"	"Hey, don't say that to me.
Let's go back
I bought the ingredients because my master said he wanted to eat hotcakes."	"Oh, come on, Hajime. Please.
Let's switch.
You wanted a pancake, so I went out to buy the ingredients."
生地	"普通のソーセージがなくて魚肉ソーセージなんだけど
生地が余ったから作ってみたんだよ
ありがとうございます"	"It's not a regular sausage, it's a fish sauce.
I made it because there was so much left over.
thank you"	"I didn't have a regular sausage, so I used fish sausage.
I had extra batter, so I made this for you.
Thank you. It looks delicious."
魚肉	"こいつははじめちゃんに
普通のソーセージがなくて魚肉ソーセージなんだけど
生地が余ったから作ってみたんだよ"	"This one's for you.
It's not a regular sausage, it's a fish sauce.
I made it because there was so much left over."	"This is for you, Hajime.
I didn't have a regular sausage, so I used fish sausage.
I had extra batter, so I made this for you."
行か	"突然ホットケーキが食べたいって言い出して
元月人のはじめちゃんに材料の買い出しに行かせたんだ
はじめちゃん 最近テレビタレントとして活躍し始めて"	"All of a sudden, he wants to eat hotcakes.
I had the first lady go shopping for supplies.
You know, I've just started working as a television personality."	"He suddenly requested pancakes,
so he made his ex-assistant Hajime go out to buy the ingredients.
Hajime has become popular as a TV actor."
買い出し	"突然ホットケーキが食べたいって言い出して
元月人のはじめちゃんに材料の買い出しに行かせたんだ
はじめちゃん 最近テレビタレントとして活躍し始めて"	"All of a sudden, he wants to eat hotcakes.
I had the first lady go shopping for supplies.
You know, I've just started working as a television personality."	"He suddenly requested pancakes,
so he made his ex-assistant Hajime go out to buy the ingredients.
Hajime has become popular as a TV actor."
師匠	"遅いよ
この人浅草芸人のケセラー・セラオ師匠で
突然ホットケーキが食べたいって言い出して"	"It's late
This is a man named Kessler Serao, an Ashanti master.
All of a sudden, he wants to eat hotcakes."	"What took you so long?
This is Serao Kesera, a master comedian in Asakusa.
He suddenly requested pancakes,"
突然	"この人浅草芸人のケセラー・セラオ師匠で
突然ホットケーキが食べたいって言い出して
元月人のはじめちゃんに材料の買い出しに行かせたんだ"	"This is a man named Kessler Serao, an Ashanti master.
All of a sudden, he wants to eat hotcakes.
I had the first lady go shopping for supplies."	"This is Serao Kesera, a master comedian in Asakusa.
He suddenly requested pancakes,
so he made his ex-assistant Hajime go out to buy the ingredients."
芸人	"遅いよ
この人浅草芸人のケセラー・セラオ師匠で
突然ホットケーキが食べたいって言い出して"	"It's late
This is a man named Kessler Serao, an Ashanti master.
All of a sudden, he wants to eat hotcakes."	"What took you so long?
This is Serao Kesera, a master comedian in Asakusa.
He suddenly requested pancakes,"
ご苦労さん	"マスター買ってきました
ご苦労さん
遅いよ"	"I bought a master.
Thank you for your hard work
It's late"	"Master, I got everything.
Thank you.
What took you so long?"
結構	"客が来るかって?
それが結構来るんだよ
マスター買ってきました"	"Are you expecting company?
That's a lot to take in.
I bought a master."	"Do I even have customers?
More than you would expect. MIDNIGHT DINER: TOKYO STORIES CORN DOG
Master, I got everything."
客	"人は深夜食堂って言ってるよ
客が来るかって?
それが結構来るんだよ"	"People say it's a late night diner.
Are you expecting company?
That's a lot to take in."	"They call it ""Midnight Diner.""
Do I even have customers?
More than you would expect. MIDNIGHT DINER: TOKYO STORIES CORN DOG"
深夜	"営業時間は夜12時から朝7時頃まで
人は深夜食堂って言ってるよ
客が来るかって?"	"Opening hours are from midnight to about 7:00 a.m.
People say it's a late night diner.
Are you expecting company?"	"My diner is open from midnight to seven in the morning.
They call it ""Midnight Diner.""
Do I even have customers?"
営業	"泡も飲めろ
営業時間は夜12時から朝7時頃まで
人は深夜食堂って言ってるよ"	"Give me some bubbles.
Opening hours are from midnight to about 7:00 a.m.
People say it's a late night diner."	"
My diner is open from midnight to seven in the morning.
They call it ""Midnight Diner."""
泡	"ずっと昔の 元のようだね
泡も飲めろ
営業時間は夜12時から朝7時頃まで"	"Looks like it's from a long time ago.
Give me some bubbles.
Opening hours are from midnight to about 7:00 a.m."	
ずっと	"俺の一日は始まる
ずっと昔の 元のようだね
泡も飲めろ"	"My day starts
Looks like it's from a long time ago.
Give me some bubbles."	
家路	"白い雲 君が入りたい
一日が終わり 人々が家路へと急ぐ頃
俺の一日は始まる"	"White clouds, you want in.
At the end of the day, people are rushing to their streets.
My day starts"	"
When people finish their day and hurry home,
my day starts."
伸ばす	"空に浮かぶ雲の中に少しずつ消えてゆく
遠く高い空の中で手を伸ばす
白い雲 君が入りたい"	"It disappears into the clouds.
I'm reaching out for you high in the sky.
White clouds, you want in."	
遠く	"空に浮かぶ雲の中に少しずつ消えてゆく
遠く高い空の中で手を伸ばす
白い雲 君が入りたい"	"It disappears into the clouds.
I'm reaching out for you high in the sky.
White clouds, you want in."	
抜け	"ママとジュリアさんの弱みにつけこんで結婚しようとしているのよ
しかしそのオヤジも抜け目のねえ野郎だぜ
村インチの事情を知りながら金でジュリアさんを吊ろうってんだからな"	"He's going to marry her because of her weakness.
But his dad's a stupid son of a bitch.
You know what's going on in the village, and you want to hang Julia with your money."	"took advantage of Julia's insecurity by trying to marry her.
But the guy is shrewd.
He knows about her circumstances and showers her with money."
つけこん	"つまりそのオヤジは
ママとジュリアさんの弱みにつけこんで結婚しようとしているのよ
しかしそのオヤジも抜け目のねえ野郎だぜ"	"I mean, the father.
He's going to marry her because of her weakness.
But his dad's a stupid son of a bitch."	"Therefore, the old guy
took advantage of Julia's insecurity by trying to marry her.
But the guy is shrewd."
弱み	"つまりそのオヤジは
ママとジュリアさんの弱みにつけこんで結婚しようとしているのよ
しかしそのオヤジも抜け目のねえ野郎だぜ"	"I mean, the father.
He's going to marry her because of her weakness.
But his dad's a stupid son of a bitch."	"Therefore, the old guy
took advantage of Julia's insecurity by trying to marry her.
But the guy is shrewd."
つまり	"たとえ好きでなくてもな
つまりそのオヤジは
ママとジュリアさんの弱みにつけこんで結婚しようとしているのよ"	"Even if you don't like it.
I mean, the father.
He's going to marry her because of her weakness."	"Even though she may not love him.
Therefore, the old guy
took advantage of Julia's insecurity by trying to marry her."
そういや	"うん 島田さん 来てる？
そういや ここんとこ 顔 出さないな
あたしね ようやく 誰にでも 胸張って言えるくらい⸺"	"Yes, Mr. Shimada, are you coming?
Oh no, I don't show my face.
I'm finally smart enough to be able to stand up for myself."	"Does Mr. Shimada still visit?
Speaking of... he hasn't in a while.
I... can finally tell everyone with pride..."
珍しい	"マスター お代わり
（マスター） 珍しいね うちで飲むなんて
うん 島田さん 来てる？"	"Master Substitute
(Master) It's unusual, I can't drink it at home.
Yes, Mr. Shimada, are you coming?"	"Master, another one.
What's the occasion? You've never had a drink here.
Does Mr. Shimada still visit?"
辞め	"あの後 何をやっても “コーガの楓”って言われた
それがイヤで 役者 辞めたようなもんなのに
そうだったんですか"	"After that, no matter what I did, they said ""Koga no Kaede""
I don't like that, and it's like I've quit as an actor.
Was that so?"	"No matter who I played, I was always Maple of Koga.
That's the main reason why I quit acting.
I didn't know that."
役者	"あの後 何をやっても “コーガの楓”って言われた
それがイヤで 役者 辞めたようなもんなのに
そうだったんですか"	"After that, no matter what I did, they said ""Koga no Kaede""
I don't like that, and it's like I've quit as an actor.
Was that so?"	"No matter who I played, I was always Maple of Koga.
That's the main reason why I quit acting.
I didn't know that."
過去	"ここで会って感じたんです 勘だけど
だから 自分の過去も 笑って 話せるんじゃないかって
そうですよ とっくに吹っ切ってますよ"	"I felt that I met you here
So I thought I could laugh and talk about my past.
That's right, it's already blowing up."	"I felt it when I met her. It's just a hunch, but...
I think she could even talk about her downs positively.
That's right. She must have moved on by now."
勘	"きちんと仕事している人 なんだろうなって⸺
ここで会って感じたんです 勘だけど
だから 自分の過去も 笑って 話せるんじゃないかって"	"I don't know what it's like to be a good worker.
I felt that I met you here
So I thought I could laugh and talk about my past."	"She's diligent, and loyal to her job.
I felt it when I met her. It's just a hunch, but...
I think she could even talk about her downs positively."
感じ	"きちんと仕事している人 なんだろうなって⸺
ここで会って感じたんです 勘だけど
だから 自分の過去も 笑って 話せるんじゃないかって"	"I don't know what it's like to be a good worker.
I felt that I met you here
So I thought I could laugh and talk about my past."	"She's diligent, and loyal to her job.
I felt it when I met her. It's just a hunch, but...
I think she could even talk about her downs positively."
豚汁	"（小寿々(こすず)）ガキねえ 男って
（マスター） お待たせ ジャンボ豚汁定食
（コウちゃん） はい いただきます"	"Hey brat, man?
(Master) Thank you for waiting Jumbo pork soup set meal
(Ko-chan) Yes, I will take it."	"Men... never grow up.
Here you go. Extra large pork and veggie soup combo.
Bon appétit."
待た	"（小寿々(こすず)）ガキねえ 男って
（マスター） お待たせ ジャンボ豚汁定食
（コウちゃん） はい いただきます"	"Hey brat, man?
(Master) Thank you for waiting Jumbo pork soup set meal
(Ko-chan) Yes, I will take it."	"Men... never grow up.
Here you go. Extra large pork and veggie soup combo.
Bon appétit."
ガキ	"（金本）ねえねえ あの… タスケとハヤテってさ…
（小寿々(こすず)）ガキねえ 男って
（マスター） お待たせ ジャンボ豚汁定食"	"(Kanemoto) Hey, hey... Tasuke and Hayate...
Hey brat, man?
(Master) Thank you for waiting Jumbo pork soup set meal"	"And Flying Squirrel and...
Men... never grow up.
Here you go. Extra large pork and veggie soup combo."
反響	"番組のホームページで 発表したんです
そしたら 反響が すごくて
僕が いちばん好きだったのは"	"I announced it on the show's website.
And the response was incredible.
What I liked most"	"I announced it on my website to see the listeners' reactions.
The feedback was amazing.
My favorite episode is when the leader welcomed Maple,"
様子見	"ええ
まずは 様子見で⸺
番組のホームページで 発表したんです"	"Yes
Let's start with the look.
I announced it on the show's website."	"That's right.
I announced it on my website to see the listeners' reactions.
I announced it on my website to see the listeners' reactions."
まずは	"ええ
まずは 様子見で⸺
番組のホームページで 発表したんです"	"Yes
Let's start with the look.
I announced it on the show's website."	"That's right.
I announced it on my website to see the listeners' reactions.
I announced it on my website to see the listeners' reactions."
コーガ	"（金本）へえ 懐かしいな
あのコーガの ファンクラブ作るんすか？
ええ"	"(Kanemoto) Hee, nostalgic
Are you going to make that Koga fan club?
Yes"	"That brings back so many memories.
Are you starting a fan club for that show?
That's right."
懐かしい	"「忍者戦隊コーガ」の主題歌 “刃の心で駆け抜けろ”です
（金本）へえ 懐かしいな
あのコーガの ファンクラブ作るんすか？"	"It's the theme song to ""Ninja Battalion Koga"".
(Kanemoto) Hee, nostalgic
Are you going to make that Koga fan club?"	"It's the main theme song from Super Ninja Squadron Koga.
That brings back so many memories.
Are you starting a fan club for that show?"
駆け抜けろ	"僕の頭に この曲が流れました⸺
「忍者戦隊コーガ」の主題歌 “刃の心で駆け抜けろ”です
（金本）へえ 懐かしいな"	"This song came into my head.
It's the theme song to ""Ninja Battalion Koga"".
(Kanemoto) Hee, nostalgic"	"this song started playing in my head.
It's the main theme song from Super Ninja Squadron Koga.
That brings back so many memories."
主題歌	"僕の頭に この曲が流れました⸺
「忍者戦隊コーガ」の主題歌 “刃の心で駆け抜けろ”です
（金本）へえ 懐かしいな"	"This song came into my head.
It's the theme song to ""Ninja Battalion Koga"".
(Kanemoto) Hee, nostalgic"	"this song started playing in my head.
It's the main theme song from Super Ninja Squadron Koga.
That brings back so many memories."
再会	"恋といえば 僕 最近 初恋の女性に
たまたま ある場所で 再会したんですよ⸺
再会っていっても⸺"	"Speaking of love, I've recently become my first love.
I just happened to meet you again somewhere.
I hope to see you again."	"Speaking of love... I recently ran into my first love at the most random place.
I recently ran into my first love at the most random place.
Unfortunately, it was an unrequited love."
女性	"相手の気持ちを 思いやんないと
恋といえば 僕 最近 初恋の女性に
たまたま ある場所で 再会したんですよ⸺"	"You have to be considerate of the other person's feelings.
Speaking of love, I've recently become my first love.
I just happened to meet you again somewhere."	"Please consider how your love interest feels.
Speaking of love... I recently ran into my first love at the most random place.
I recently ran into my first love at the most random place."
初恋	"相手の気持ちを 思いやんないと
恋といえば 僕 最近 初恋の女性に
たまたま ある場所で 再会したんですよ⸺"	"You have to be considerate of the other person's feelings.
Speaking of love, I've recently become my first love.
I just happened to meet you again somewhere."	"Please consider how your love interest feels.
Speaking of love... I recently ran into my first love at the most random place.
I recently ran into my first love at the most random place."
恋	"相手の気持ちを 思いやんないと
恋といえば 僕 最近 初恋の女性に
たまたま ある場所で 再会したんですよ⸺"	"You have to be considerate of the other person's feelings.
Speaking of love, I've recently become my first love.
I just happened to meet you again somewhere."	"Please consider how your love interest feels.
Speaking of love... I recently ran into my first love at the most random place.
I recently ran into my first love at the most random place."
思いやん	"ただ ストーカーは ダメですよ
相手の気持ちを 思いやんないと
恋といえば 僕 最近 初恋の女性に"	"But stalker is no good
You have to be considerate of the other person's feelings.
Speaking of love, I've recently become my first love."	"But don't be a stalker.
Please consider how your love interest feels.
Speaking of love... I recently ran into my first love at the most random place."
相手	"ただ ストーカーは ダメですよ
相手の気持ちを 思いやんないと
恋といえば 僕 最近 初恋の女性に"	"But stalker is no good
You have to be considerate of the other person's feelings.
Speaking of love, I've recently become my first love."	"But don't be a stalker.
Please consider how your love interest feels.
Speaking of love... I recently ran into my first love at the most random place."
恋し	"いくつになっても⸺
恋したって いいじゃないですか
ただ ストーカーは ダメですよ"	"No matter how much it costs.
I hope you are in love
But stalker is no good"	"there is no age limit for falling in love.
there is no age limit for falling in love.
But don't be a stalker."
届い	"楓さんに ファンレター 送ったんですよ
そしたら このブロマイドが 届いたんですよ
覚えてるかな？ 僕のこと"	"I sent a fan letter to Kaede.
And then this bromide arrived.
Do you remember? About Me"	"When I was a kid, I sent her a fan letter.
Then she sent me this photo.
I wonder if she remembers me."
悪	"〝紅の楓 〞
“五人の忍びが そろうとき 誰にも知られず悪を断つ！”
子供のときに⸺"	"It's an orange peach.
""When the five shinobi come together, they will cut off evil without anyone knowing!""
When I was a kid."	"and Crimson Maple.
Five super ninjas kill evildoers, leaving no trace!
When I was a kid, I sent her a fan letter."
そろう	"〝紅の楓 〞
“五人の忍びが そろうとき 誰にも知られず悪を断つ！”
子供のときに⸺"	"It's an orange peach.
""When the five shinobi come together, they will cut off evil without anyone knowing!""
When I was a kid."	"and Crimson Maple.
Five super ninjas kill evildoers, leaving no trace!
When I was a kid, I sent her a fan letter."
忍び	"〝紅の楓 〞
“五人の忍びが そろうとき 誰にも知られず悪を断つ！”
子供のときに⸺"	"It's an orange peach.
""When the five shinobi come together, they will cut off evil without anyone knowing!""
When I was a kid."	"and Crimson Maple.
Five super ninjas kill evildoers, leaving no trace!
When I was a kid, I sent her a fan letter."
楓	"〝橙(だいだい)のタスケ 〞⸺
〝紅の楓 〞
“五人の忍びが そろうとき 誰にも知られず悪を断つ！”"	"It's a lot of work.
It's an orange peach.
""When the five shinobi come together, they will cut off evil without anyone knowing!"""	"Ultramarine Gale, Light-green Yonezo, Orange Tasuke,
and Crimson Maple.
Five super ninjas kill evildoers, leaving no trace!"
紅	"〝橙(だいだい)のタスケ 〞⸺
〝紅の楓 〞
“五人の忍びが そろうとき 誰にも知られず悪を断つ！”"	"It's a lot of work.
It's an orange peach.
""When the five shinobi come together, they will cut off evil without anyone knowing!"""	"Ultramarine Gale, Light-green Yonezo, Orange Tasuke,
and Crimson Maple.
Five super ninjas kill evildoers, leaving no trace!"
伝説	"紅の楓じゃないですか
あの伝説の 「忍者戦隊コーガ」の
知ってっか？"	"Isn't it Crimson Kaede?
That legendary ""Ninja Sentai Koga""
Do you know that?"	"She's Crimson Maple.
From the legendary TV show, Super Ninja Squadron Koga.
Do you know it?"
確か	"絶対 間違いないですよ 〝紅の楓(かえで) 〞
（マスター）うーん… 確かに似てるけど⸺
これ 何だい？"	"I'm sure of it.
Master: Yes, I'm sure they look alike.
What is this?"	"Don't you think they look alike? I have no doubt. Crimson Maple.
They do look alike.
What is this anyway?"
似	"どっかで会ったような気が するんだよなあ
（島田） ねっ 似てるでしょ？⸺
絶対 間違いないですよ 〝紅の楓(かえで) 〞"	"I feel like we've met somewhere.
You look alike, don't you?
I'm sure of it."	"Why does she looks so familiar to me?
Right? Don't you think they look alike? I have no doubt.
Don't you think they look alike? I have no doubt. Crimson Maple."
勘定	"今日みたいに流しても お客さんがいないときに
マスター お勘定
ごちそうさま"	"Even if you play it like today, when there are no customers
Master Account
Thank you for the feast"	"It's not always easy finding customers just by driving around.
Master, check please.
-Thank you for the meal. -Thank you."
感じ	"ああ 独りぼっち じゃないんだって
分かるなあ その感じ
（携帯電話の着信音）"	"Oh, I'm not alone.
I don't know, that feeling.
(Mobile phone ringtone)"	"they helped me feel like I wasn't alone.
I know what you mean.
"
独りぼっち	"落ち込んで やりきれないとき
ああ 独りぼっち じゃないんだって
分かるなあ その感じ"	"When you're depressed and can't do it
Oh, I'm not alone.
I don't know, that feeling."	"and didn't know what to do,
they helped me feel like I wasn't alone.
I know what you mean."
悩ん	"憧れてたんです 深夜放送のＤＪに
つまんないことで悩んだり
落ち込んで やりきれないとき"	"I was longing to be a late-night DJ.
I'm worried about boring things.
When you're depressed and can't do it"	"I looked up to late-night radio jockeys.
When I got sad or stressed out,
and didn't know what to do,"
つまんない	"憧れてたんです 深夜放送のＤＪに
つまんないことで悩んだり
落ち込んで やりきれないとき"	"I was longing to be a late-night DJ.
I'm worried about boring things.
When you're depressed and can't do it"	"I looked up to late-night radio jockeys.
When I got sad or stressed out,
and didn't know what to do,"
放送	"目指してたんですか？ ＤＪ
憧れてたんです 深夜放送のＤＪに
つまんないことで悩んだり"	"Was that what you were aiming for? dj
I was longing to be a late-night DJ.
I'm worried about boring things."	"So, why a radio jockey?
I looked up to late-night radio jockeys.
When I got sad or stressed out,"
憧れ	"目指してたんですか？ ＤＪ
憧れてたんです 深夜放送のＤＪに
つまんないことで悩んだり"	"Was that what you were aiming for? dj
I was longing to be a late-night DJ.
I'm worried about boring things."	"So, why a radio jockey?
I looked up to late-night radio jockeys.
When I got sad or stressed out,"
目指し	"フフッ
目指してたんですか？ ＤＪ
憧れてたんです 深夜放送のＤＪに"	"Huh-huh
Was that what you were aiming for? dj
I was longing to be a late-night DJ."	"
So, why a radio jockey?
I looked up to late-night radio jockeys."
正義	"あとはてめえで片付けろ
くそ、正義のヒーロー気取ってるつもりかよ
女の子にこんなことして、タダで済むと思ってんの"	"If you don't, clean it up.
Shit, you care about heroes of justice?
You think you can do this to a girl and get away with it?"	"Take care of the rest on your own.
Shit. You think you're a hero of justice or something?
Do you think you'll get away with doing something like this to girls?"
ざけたまねするんじゃねえぞ	"ちょっと、聞いてんのに
いいな、俺に懲りたら二度といじめなんてふざけたまねするんじゃねえぞ
ほらよ、吉川"	"Wait a minute. I heard you.
Okay, if you're going to punish me again, don't make fun of me.
There you are, Kigawa."	"Hey! Are you listening, Onizuka? -No, stop it! -Please!
Listen to me. You've learned your lesson. Don't ever bully anyone again.
Here, Yoshikawa."
いじめ	"ちょっと、聞いてんのに
いいな、俺に懲りたら二度といじめなんてふざけたまねするんじゃねえぞ
ほらよ、吉川"	"Wait a minute. I heard you.
Okay, if you're going to punish me again, don't make fun of me.
There you are, Kigawa."	"Hey! Are you listening, Onizuka? -No, stop it! -Please!
Listen to me. You've learned your lesson. Don't ever bully anyone again.
Here, Yoshikawa."
二度と	"ちょっと、聞いてんのに
いいな、俺に懲りたら二度といじめなんてふざけたまねするんじゃねえぞ
ほらよ、吉川"	"Wait a minute. I heard you.
Okay, if you're going to punish me again, don't make fun of me.
There you are, Kigawa."	"Hey! Are you listening, Onizuka? -No, stop it! -Please!
Listen to me. You've learned your lesson. Don't ever bully anyone again.
Here, Yoshikawa."
懲り	"ちょっと、聞いてんのに
いいな、俺に懲りたら二度といじめなんてふざけたまねするんじゃねえぞ
ほらよ、吉川"	"Wait a minute. I heard you.
Okay, if you're going to punish me again, don't make fun of me.
There you are, Kigawa."	"Hey! Are you listening, Onizuka? -No, stop it! -Please!
Listen to me. You've learned your lesson. Don't ever bully anyone again.
Here, Yoshikawa."
霊	"さてと、ちょっと、記念写真撮っとこうと思ってよ
人権重霊よ、この変態キャッシュ
ちょっと、聞いてんのに"	"Well, wait a minute. I thought I'd take some souvenir photos.
It's the human spirit, this mutant cash.
Wait a minute. I heard you."	"-Now, next... -No, wait! What are you going to do? I'm gonna take a commemorative photo.
Stop it! You're violating our human rights, you pervert!
Hey! Are you listening, Onizuka? -No, stop it! -Please!"
人権	"さてと、ちょっと、記念写真撮っとこうと思ってよ
人権重霊よ、この変態キャッシュ
ちょっと、聞いてんのに"	"Well, wait a minute. I thought I'd take some souvenir photos.
It's the human spirit, this mutant cash.
Wait a minute. I heard you."	"-Now, next... -No, wait! What are you going to do? I'm gonna take a commemorative photo.
Stop it! You're violating our human rights, you pervert!
Hey! Are you listening, Onizuka? -No, stop it! -Please!"
記念	"いい眺めだね、吉川君
さてと、ちょっと、記念写真撮っとこうと思ってよ
人権重霊よ、この変態キャッシュ"	"That's a nice view you got there, Mr. Kigawa.
Well, wait a minute. I thought I'd take some souvenir photos.
It's the human spirit, this mutant cash."	"What a wonderful view, isn't it, Yoshikawa?
-Now, next... -No, wait! What are you going to do? I'm gonna take a commemorative photo.
Stop it! You're violating our human rights, you pervert!"
さてと	"その方が少しは動きやすいだろ
さてと
お前たちは何がいいかね"	"It's a little easier to move, isn't it?
Let's see
What do you like?"	"There, that gives you a little more freedom.
There, that gives you a little more freedom.
Let's see now... What shall we turn you into?"
眺め	"さて、仕上げといくか
いい眺めだね、吉川君
さてと、ちょっと、記念写真撮っとこうと思ってよ"	"Okay, let's get this over with.
That's a nice view you got there, Mr. Kigawa.
Well, wait a minute. I thought I'd take some souvenir photos."	"Now, to finish it off.
What a wonderful view, isn't it, Yoshikawa?
-Now, next... -No, wait! What are you going to do? I'm gonna take a commemorative photo."
仕上げ	"ちくしょう、吉川、てめえ、写真ばらまくだけじゃ済まねえからな
さて、仕上げといくか
いい眺めだね、吉川君"	"Damn it, Kichigawa, you can't just scatter the photos.
Okay, let's get this over with.
That's a nice view you got there, Mr. Kigawa."	"You bastard! Yoshikawa, don't think we'll be done with just scattering your photos!
Now, to finish it off.
What a wonderful view, isn't it, Yoshikawa?"
済ま	"こんなもん今まで吉川が味わった痛みに比べりゃ、へびてえなもんだ
ちくしょう、吉川、てめえ、写真ばらまくだけじゃ済まねえからな
さて、仕上げといくか"	"This is nothing compared to the pain Ji-Kawa's been through.
Damn it, Kichigawa, you can't just scatter the photos.
Okay, let's get this over with."	"This is nothing compared to what Yoshikawa felt.
You bastard! Yoshikawa, don't think we'll be done with just scattering your photos!
Now, to finish it off."
びてえなもんだ	"いてえだと、冗談こぐんじゃねえよ
こんなもん今まで吉川が味わった痛みに比べりゃ、へびてえなもんだ
ちくしょう、吉川、てめえ、写真ばらまくだけじゃ済まねえからな"	"If you are, I'm not kidding.
This is nothing compared to the pain Ji-Kawa's been through.
Damn it, Kichigawa, you can't just scatter the photos."	"Hurts? Look who's talking!
This is nothing compared to what Yoshikawa felt.
You bastard! Yoshikawa, don't think we'll be done with just scattering your photos!"
比べりゃ	"いてえだと、冗談こぐんじゃねえよ
こんなもん今まで吉川が味わった痛みに比べりゃ、へびてえなもんだ
ちくしょう、吉川、てめえ、写真ばらまくだけじゃ済まねえからな"	"If you are, I'm not kidding.
This is nothing compared to the pain Ji-Kawa's been through.
Damn it, Kichigawa, you can't just scatter the photos."	"Hurts? Look who's talking!
This is nothing compared to what Yoshikawa felt.
You bastard! Yoshikawa, don't think we'll be done with just scattering your photos!"
痛み	"いてえだと、冗談こぐんじゃねえよ
こんなもん今まで吉川が味わった痛みに比べりゃ、へびてえなもんだ
ちくしょう、吉川、てめえ、写真ばらまくだけじゃ済まねえからな"	"If you are, I'm not kidding.
This is nothing compared to the pain Ji-Kawa's been through.
Damn it, Kichigawa, you can't just scatter the photos."	"Hurts? Look who's talking!
This is nothing compared to what Yoshikawa felt.
You bastard! Yoshikawa, don't think we'll be done with just scattering your photos!"
味わっ	"いてえだと、冗談こぐんじゃねえよ
こんなもん今まで吉川が味わった痛みに比べりゃ、へびてえなもんだ
ちくしょう、吉川、てめえ、写真ばらまくだけじゃ済まねえからな"	"If you are, I'm not kidding.
This is nothing compared to the pain Ji-Kawa's been through.
Damn it, Kichigawa, you can't just scatter the photos."	"Hurts? Look who's talking!
This is nothing compared to what Yoshikawa felt.
You bastard! Yoshikawa, don't think we'll be done with just scattering your photos!"
こぐ	"てめえ
いてえだと、冗談こぐんじゃねえよ
こんなもん今まで吉川が味わった痛みに比べりゃ、へびてえなもんだ"	"Temee
If you are, I'm not kidding.
This is nothing compared to the pain Ji-Kawa's been through."	"Onizuka! You bastard!
Hurts? Look who's talking!
This is nothing compared to what Yoshikawa felt."
冗談	"てめえ
いてえだと、冗談こぐんじゃねえよ
こんなもん今まで吉川が味わった痛みに比べりゃ、へびてえなもんだ"	"Temee
If you are, I'm not kidding.
This is nothing compared to the pain Ji-Kawa's been through."	"Onizuka! You bastard!
Hurts? Look who's talking!
This is nothing compared to what Yoshikawa felt."
切っ	"リベンジの始まりです
押しを切ってんだよ
てめえ"	"This is the beginning of revenge.
I pushed him off.
Temee"	"Now, we begin the revenge!
-What the hell are you doing?! -Bad kids get a spanking!
Onizuka! You bastard!"
押し	"リベンジの始まりです
押しを切ってんだよ
てめえ"	"This is the beginning of revenge.
I pushed him off.
Temee"	"Now, we begin the revenge!
-What the hell are you doing?! -Bad kids get a spanking!
Onizuka! You bastard!"
脱がし	"どういう意味よ
バックレンじゃねえよ、男のパンツ脱がして生写真撮るなんてよ
知らないよ、そんなの、ねえ、そうよ、何言ってんのよ"	"What do you mean?
It's not like you can take a picture of a man with his pants off.
I don't know. That... hey, yeah, what did you say?"	"What do you mean?
Don't play innocent. You pulled down a man's pants and took pictures of him naked.
I have no idea what this is all about, right? Right. What are you talking about?"
レン	"どういう意味よ
バックレンじゃねえよ、男のパンツ脱がして生写真撮るなんてよ
知らないよ、そんなの、ねえ、そうよ、何言ってんのよ"	"What do you mean?
It's not like you can take a picture of a man with his pants off.
I don't know. That... hey, yeah, what did you say?"	"What do you mean?
Don't play innocent. You pulled down a man's pants and took pictures of him naked.
I have no idea what this is all about, right? Right. What are you talking about?"
曲	"せめてこれぐらいやんなきゃ気が晴れないよ
あんこ 曲入ったよ ほら
はい マイク"	"At least I'll be able to do this much.
You're in the song.
I know, Mike."	"This is the least I could do to be satisfied.
Anko, your song is ready.
-Here's your microphone. -Thank you!"
せめて	"ムライや鬼塚があんましだらしなさすぎるからさ
せめてこれぐらいやんなきゃ気が晴れないよ
あんこ 曲入ったよ ほら"	"Because you're too much of a Muay Thai or Goktsuka.
At least I'll be able to do this much.
You're in the song."	"It's because Murai and Kikuchi were so worthless.
This is the least I could do to be satisfied.
Anko, your song is ready."
しなさ	"しかしあんこもえぐいよね ここまでやるとはさ
ムライや鬼塚があんましだらしなさすぎるからさ
せめてこれぐらいやんなきゃ気が晴れないよ"	"But I know you're pretty good, too.
Because you're too much of a Muay Thai or Goktsuka.
At least I'll be able to do this much."	"But Anko, you're so harsh. I never imagined you'd go this far.
It's because Murai and Kikuchi were so worthless.
This is the least I could do to be satisfied."
握ら	"ま これであいつも鬼塚んとこには近づけないだろうね
何だってこんな恥ずかしい写真握られてんだからさ
しかしあんこもえぐいよね ここまでやるとはさ"	"That's why you can't always get close to him.
I'm always holding these embarrassing pictures.
But I know you're pretty good, too."	"He's not gonna approach Onizuka anymore.
Because we have such an embarrassing picture.
But Anko, you're so harsh. I never imagined you'd go this far."
近づけ	"あの時の吉川の顔 傑作じゃないこの写真!
ま これであいつも鬼塚んとこには近づけないだろうね
何だってこんな恥ずかしい写真握られてんだからさ"	"This isn't a masterpiece!
That's why you can't always get close to him.
I'm always holding these embarrassing pictures."	"Yoshikawa's face was priceless! This photo is just too funny.
He's not gonna approach Onizuka anymore.
Because we have such an embarrassing picture."
決め	"よーし 案内しろや
リベンジ決めんぞ
あの時の吉川の顔 傑作じゃないこの写真!"	"All right, let me show you around.
It's not about revenge.
This isn't a masterpiece!"	"Well, lead the way.
Revenge, let's do it.
Yoshikawa's face was priceless! This photo is just too funny."
リベンジ	"よーし 案内しろや
リベンジ決めんぞ
あの時の吉川の顔 傑作じゃないこの写真!"	"All right, let me show you around.
It's not about revenge.
This isn't a masterpiece!"	"Well, lead the way.
Revenge, let's do it.
Yoshikawa's face was priceless! This photo is just too funny."
上等	"悔しい…悔しいよ…悔しい…
それでいいんだよ 上等だ
よーし 案内しろや"	"I'm sorry about that.
That's good. That's great.
All right, let me show you around."	"I'm frustrated. Of course I'm frustrated! I am...
Good. That's good. Good job.
Well, lead the way."
晴れる	"悔しくねえのか このまま落ちんだよ
死んだって気持ちが晴れるわけじゃねえんだぜ
悔しい…悔しいよ…悔しい…"	"Don't you have any regrets?
It doesn't make you feel any better to be dead.
I'm sorry about that."	"Aren't you frustrated?
Even if you die, you won't feel better.
I'm frustrated. Of course I'm frustrated! I am..."
まま	"お前…
悔しくねえのか このまま落ちんだよ
死んだって気持ちが晴れるわけじゃねえんだぜ"	"My love...
Don't you have any regrets?
It doesn't make you feel any better to be dead."	"Yoshikawa, you...
Aren't you frustrated?
Even if you die, you won't feel better."
悔しく	"お前…
悔しくねえのか このまま落ちんだよ
死んだって気持ちが晴れるわけじゃねえんだぜ"	"My love...
Don't you have any regrets?
It doesn't make you feel any better to be dead."	"Yoshikawa, you...
Aren't you frustrated?
Even if you die, you won't feel better."
まね	"何回言や分かるんだよ!
あれほど自殺なんてバカなまねすんなって!
吉子…"	"How many times do I have to tell you?
It's so stupid to kill yourself!
It's all right."	"How many times do I have to tell you?
I told you so many times not to kill yourself!
Yoshikawa, you..."
言	"わ…わ…わたしのくれ…くれくれくれくれくれくれくれ…
何回言や分かるんだよ!
あれほど自殺なんてバカなまねすんなって!"	"Oh, my God.
How many times do I have to tell you?
It's so stupid to kill yourself!"	"My Cresta...
How many times do I have to tell you?
I told you so many times not to kill yourself!"
隠れ	"このクレスタさえあれば
なんで隠れてんだよ
てっはぁ!"	"If only I had this crest.
Why are you hiding?
Get out of here!"	"All I need is my Cresta!
Onizuka! Ouch... Here we are. Jeez. What the hell were you thinking? You idiot!
What the hell were you thinking? You idiot!"
家庭	"このクレスタが私に父としての威厳と
幸せな家庭を取り戻させてくれる
このクレスタさえあれば"	"This crest has given me the dignity of a father.
It'll bring you back to a happy home.
If only I had this crest."	"This Cresta will help me regain my dignity as a father
and my happy family.
All I need is my Cresta!"
威厳	"鬼塚
このクレスタが私に父としての威厳と
幸せな家庭を取り戻させてくれる"	"It's a ghost town.
This crest has given me the dignity of a father.
It'll bring you back to a happy home."	"Onizuka?
This Cresta will help me regain my dignity as a father
and my happy family."
帰宅	"よしか
このクレスタで帰宅した私を見たら
妻や娘はどんな顔をするだろう"	"Good to see you.
If you see me coming home in this crest,
What will your wife and daughter look like?"	"Yoshikawa?
When I come home in this Cresta,
how will my wife and daughter react?"
ニョタイコレクション	"楽しみだよな
これで鬼塚ニョタイコレクションの
新しい1ページが"	"I'm looking forward to it
I'm going to show you the Goktsuka Notai collection.
There's a new page."	"I can't wait!
This will be an additional page in the Onizuka Female Body Collection.
This will be an additional page in the Onizuka Female Body Collection."
商工	"ばれなきゃいいんだって
じゃあ30分後に商工口で待ってんぜ
じゃあな"	"He said he had to go.
Then meet me at the commercial entrance in 30 minutes.
Bye"	"Oh, hush. It's fine as long as no one knows.
I'll be waiting in 30 minutes at the front door.
See you then."
偽造	"なあ
それって偽造じゃねえか
教師のくせに学校に知れたら問題だぞ"	"Hey
That's not a fake.
It's a problem if the school finds out about you because of your teacher."	"I'll have them copied so well that no one will know they're fake!
Isn't that counterfeiting?
If the school finds out, you'll be in trouble."
ばれ	"本物の食券クリソツにコピーしてっから
絶対ばれねえぞ
なあ"	"I copied it from a real food stamp.
I'm not going anywhere.
Hey"	"I'll have them copied so well that no one will know they're fake!
I'll have them copied so well that no one will know they're fake!
I'll have them copied so well that no one will know they're fake!"
絶対	"本物の食券クリソツにコピーしてっから
絶対ばれねえぞ
なあ"	"I copied it from a real food stamp.
I'm not going anywhere.
Hey"	"I'll have them copied so well that no one will know they're fake!
I'll have them copied so well that no one will know they're fake!
I'll have them copied so well that no one will know they're fake!"
クリ	"10枚でどうだ
本物の食券クリソツにコピーしてっから
絶対ばれねえぞ"	"How about ten?
I copied it from a real food stamp.
I'm not going anywhere."	"I have an idea! What if I give you 10 combo-A lunch tickets?
I'll have them copied so well that no one will know they're fake!
I'll have them copied so well that no one will know they're fake!"
食券	"おぉそうだよ
学食の英定食ライス大盛りの食券
10枚でどうだ"	"Oh, my God.
School meals, English meals, rice food stamps.
How about ten?"	"I have an idea! What if I give you 10 combo-A lunch tickets?
I have an idea! What if I give you 10 combo-A lunch tickets?
I have an idea! What if I give you 10 combo-A lunch tickets?"
大盛り	"おぉそうだよ
学食の英定食ライス大盛りの食券
10枚でどうだ"	"Oh, my God.
School meals, English meals, rice food stamps.
How about ten?"	"I have an idea! What if I give you 10 combo-A lunch tickets?
I have an idea! What if I give you 10 combo-A lunch tickets?
I have an idea! What if I give you 10 combo-A lunch tickets?"
定食	"おぉそうだよ
学食の英定食ライス大盛りの食券
10枚でどうだ"	"Oh, my God.
School meals, English meals, rice food stamps.
How about ten?"	"I have an idea! What if I give you 10 combo-A lunch tickets?
I have an idea! What if I give you 10 combo-A lunch tickets?
I have an idea! What if I give you 10 combo-A lunch tickets?"
水	"おいおい
そんな水くせえこと言わずによ
おぉそうだよ"	"Hey, hey
Don't be such a dick about it.
Oh, my God."	"Come on.
Don't be so cold.
I have an idea! What if I give you 10 combo-A lunch tickets?"
待ちくたびれ	"まだできねえのかよ
こっちは待ちくたびれてんだぞ
約束なんかした覚えねえよ"	"I don't know if you can do it yet.
I can't wait to be here.
I don't remember promising you anything."	"Have you finished the photos you promised me? I'm tired of waiting.
Have you finished the photos you promised me? I'm tired of waiting.
I didn't promise you anything!"
約束	"鬼塚?
前に約束した合成写真
まだできねえのかよ"	"Where's the ghost?
I promised you a synthetic photo.
I don't know if you can do it yet."	"Onizuka?
Have you finished the photos you promised me? I'm tired of waiting.
Have you finished the photos you promised me? I'm tired of waiting."
歌お	"いいね いいね
何歌おうかな
やっぱラルクじゃない"	"Like Like
I don't know what to sing.
It's not Rack."	"Oh, I love it! What shall I sing?
Oh, I love it! What shall I sing?
-Definitely L'Arc. -No, it's got to be enka, enka!"
ほっぽっ	"それでも男かよ
さぁ こんなやつほっぽっといて
ボクシ行こう ボクシ"	"But he's still a man.
Now, leave this one alone.
Let's get out of here."	"-Oh, he's started to cry. -Are you really a man?
Leave him here. Let's go to karaoke!
Leave him here. Let's go to karaoke!"
清潔	"白描きなんかしちゃったりして
おぉ 清潔
あ 泣き出しちゃった"	"I'm going to do some white drawing.
Oh, cleanliness
I was crying."	"-What if we add some doodles? -How artistic!
-What if we add some doodles? -How artistic!
-Oh, he's started to cry. -Are you really a man?"
描き	"かわいい
白描きなんかしちゃったりして
おぉ 清潔"	"pitiable
I'm going to do some white drawing.
Oh, cleanliness"	"It's cute!
-What if we add some doodles? -How artistic!
-What if we add some doodles? -How artistic!"
帽子	"なさげね
でも素敵なお帽子よ よしかーくん
かわいい"	"Nagene
But it's a nice hat, Yoshishika-kun.
pitiable"	"That's pathetic! It's got on a nice hoodie, Yoshikawa.
That's pathetic! It's got on a nice hoodie, Yoshikawa.
It's cute!"
ちっ	"僕は女の子にすっぱだかの生写真撮られましたって書いてさ
こいつちっちぇー
なさげね"	"I wrote that I was photographed by a girl
This guy is a little bit
Nagene"	"With the caption, ""I had my naked picture taken by girls.""
He's so tiny!
That's pathetic! It's got on a nice hoodie, Yoshikawa."
撮ら	"この写真、街中にばらまくかんね
僕は女の子にすっぱだかの生写真撮られましたって書いてさ
こいつちっちぇー"	"I don't want to scatter this photo all over the city.
I wrote that I was photographed by a girl
This guy is a little bit"	"l'll scatter these photos all over town.
With the caption, ""I had my naked picture taken by girls.""
He's so tiny!"
生	"この写真、街中にばらまくかんね
僕は女の子にすっぱだかの生写真撮られましたって書いてさ
こいつちっちぇー"	"I don't want to scatter this photo all over the city.
I wrote that I was photographed by a girl
This guy is a little bit"	"l'll scatter these photos all over town.
With the caption, ""I had my naked picture taken by girls.""
He's so tiny!"
すっぱ	"この写真、街中にばらまくかんね
僕は女の子にすっぱだかの生写真撮られましたって書いてさ
こいつちっちぇー"	"I don't want to scatter this photo all over the city.
I wrote that I was photographed by a girl
This guy is a little bit"	"l'll scatter these photos all over town.
With the caption, ""I had my naked picture taken by girls.""
He's so tiny!"
ばらまく	"もし今度鬼塚と立ち越えてたら
この写真、街中にばらまくかんね
僕は女の子にすっぱだかの生写真撮られましたって書いてさ"	"If I had stood up to Onizuka next time
I don't want to scatter this photo all over the city.
I wrote that I was photographed by a girl"	"Understand? If I see you being friendly to Onizuka again,
l'll scatter these photos all over town.
With the caption, ""I had my naked picture taken by girls."""
街	"もし今度鬼塚と立ち越えてたら
この写真、街中にばらまくかんね
僕は女の子にすっぱだかの生写真撮られましたって書いてさ"	"If I had stood up to Onizuka next time
I don't want to scatter this photo all over the city.
I wrote that I was photographed by a girl"	"Understand? If I see you being friendly to Onizuka again,
l'll scatter these photos all over town.
With the caption, ""I had my naked picture taken by girls."""
越え	"いいね
もし今度鬼塚と立ち越えてたら
この写真、街中にばらまくかんね"	"Nice
If I had stood up to Onizuka next time
I don't want to scatter this photo all over the city."	"Understand? If I see you being friendly to Onizuka again,
Understand? If I see you being friendly to Onizuka again,
l'll scatter these photos all over town."
死刑	"クラスの決まり知ってんだろ?
死刑だよ、普通
いいね"	"You know the rules of the class, don't you?
It's the death penalty, usually
Nice"	"You know our class rules. You get the consequences.
You know our class rules. You get the consequences.
Understand? If I see you being friendly to Onizuka again,"
決まり	"鬼塚とつるんでんじゃねえよ
クラスの決まり知ってんだろ?
死刑だよ、普通"	"Don't hang out with Onizuka
You know the rules of the class, don't you?
It's the death penalty, usually"	"Idiot! You shouldn't hang out with Onizuka!
You know our class rules. You get the consequences.
You know our class rules. You get the consequences."
つるん	"よね
鬼塚とつるんでんじゃねえよ
クラスの決まり知ってんだろ?"	"Right
Don't hang out with Onizuka
You know the rules of the class, don't you?"	"I wanna talk to you. You'll come with me, won't you?
Idiot! You shouldn't hang out with Onizuka!
You know our class rules. You get the consequences."
付き合っ	"吉川くん
ちょっち話なんだけど、付き合ってくれる?
よね"	"Yoshikawa-kun
It's a little story, but will you go with me?
Right"	"Hey, Yoshikawa.
I wanna talk to you. You'll come with me, won't you?
I wanna talk to you. You'll come with me, won't you?"
ケチ	"僕がクリアしてからだけどね
ケチくせえ
吉川くん"	"After I cleared it, but only after I cleared it.
Stingy
Yoshikawa-kun"	"-Of course, it'll be after I clear it. -Gosh, you're so stingy.
-Of course, it'll be after I clear it. -Gosh, you're so stingy.
Hey, Yoshikawa."
手	"そこはさっき言ったでしょ
じゃあ、また新しいソフト手に入ったら来るから
頼むぜ、吉川"	"That's what I said.
Well, I'll come back when I get new software
Please, Yoshikawa"	"-I already told you about that. -What?
I'll come over again when I get new software.
I'm counting on you, Yoshikawa!"
氷	"違うよ、そこはそっち
なんでなんで、氷じゃねえのかよ
そこはさっき言ったでしょ"	"No, it's that way.
Why isn't it ice?
That's what I said."	"-Like this? This way? -No, no. Use this for that.
Oh, not this one?
-I already told you about that. -What?"
邪魔	"入れ入れ
い、いえ、お邪魔みたいだから
ちょうどよかったぜ"	"Get in there.
No, no. I'm in the way.
It was just right."	"Oh, Yoshikawa. What's the matter? Come in.
Oh, no. I don't want to intrude.
I have to ask you something."
匂い	"そうそう、簡単でしょこれ
いい匂いだ
この後はどうするの?"	"Yeah, yeah, that's easy.
It smells good.
What's next?"	"That's right. Isn't it easy?
She smells good...
What do I do next?"
かしら	"ほらほら
えっと、これでいいのかしら?
そうそう"	"Hey
Uh, is this all right?
I remember"	"Here, this is a really fun part. I'll teach you. See? There!
-Oh, is this how it goes? -Right, right.
-Oh, is this how it goes? -Right, right."
っけ	"何か心配事が?
来ました!新しいアイテムを見っけ!
もう"	"Are you worried about something?
It's here! Look at this new item!
already"	"You do have some concerns, right?
Great! I found new items!
"
頃	"そう でも先生方噂してるから
鬼塚先生もそろそろストレス溜まってくる頃じゃないかって
それに京都先生あなたのことあまり好きじゃないだろうし"	"Yeah, but the teacher's been rumouring.
It's time for Gokutsuka to get stressed out.
Besides, Mr. Kyoto probably doesn't like you very much."	"Is that so? But the other teachers are talking about you.
They say it's time Mr. Onizuka felt the stress accumulating.
Also, the vice principal doesn't seem to like you much."
溜まっ	"そう でも先生方噂してるから
鬼塚先生もそろそろストレス溜まってくる頃じゃないかって
それに京都先生あなたのことあまり好きじゃないだろうし"	"Yeah, but the teacher's been rumouring.
It's time for Gokutsuka to get stressed out.
Besides, Mr. Kyoto probably doesn't like you very much."	"Is that so? But the other teachers are talking about you.
They say it's time Mr. Onizuka felt the stress accumulating.
Also, the vice principal doesn't seem to like you much."
生徒	"嫌がらせとか受けてません 嫌がらせ?なんすかそれ
生徒たちとはわけあいあいつが楽しくやってますよ
俺の授業なんて生徒たちに受けちゃっても大変なんすから"	"I'm not being harassed. Oh, my God.
He's having fun with his students.
It's hard for my students to take my classes."	"Are you being harassed? Harassed? What the heck is that?
I'm doing fine. I'm having fun with my students.
My students seem to like my class so much, I don't know what to do."
嫌がらせ	"どうです3年4組 どうって
嫌がらせとか受けてません 嫌がらせ?なんすかそれ
生徒たちとはわけあいあいつが楽しくやってますよ"	"Thank you. Three, four pairs.
I'm not being harassed. Oh, my God.
He's having fun with his students."	"-How has it been in Class 3-4? -What do you mean?
Are you being harassed? Harassed? What the heck is that?
I'm doing fine. I'm having fun with my students."
裏切ら	"俺が外れたからって決して鬼塚を認めたわけじゃねえんだからな
選考なんか信じたら前みたいに裏切られるだけだ
どうです3年4組 どうって"	"Just because I'm out doesn't mean I'll ever admit to being a ghost.
If you believe in the selection, you'll be betrayed just like before.
Thank you. Three, four pairs."	"Just because I'm out doesn't mean I approve of Onizuka.
If we trust a teacher, we'll be betrayed again like before.
-How has it been in Class 3-4? -What do you mean?"
選考	"俺が外れたからって決して鬼塚を認めたわけじゃねえんだからな
選考なんか信じたら前みたいに裏切られるだけだ
どうです3年4組 どうって"	"Just because I'm out doesn't mean I'll ever admit to being a ghost.
If you believe in the selection, you'll be betrayed just like before.
Thank you. Three, four pairs."	"Just because I'm out doesn't mean I approve of Onizuka.
If we trust a teacher, we'll be betrayed again like before.
-How has it been in Class 3-4? -What do you mean?"
わけ	"何が言いたいんだよ お前
俺が外れたからって決して鬼塚を認めたわけじゃねえんだからな
選考なんか信じたら前みたいに裏切られるだけだ"	"What are you talking about?
Just because I'm out doesn't mean I'll ever admit to being a ghost.
If you believe in the selection, you'll be betrayed just like before."	"What are you saying?
Just because I'm out doesn't mean I approve of Onizuka.
If we trust a teacher, we'll be betrayed again like before."
認め	"何が言いたいんだよ お前
俺が外れたからって決して鬼塚を認めたわけじゃねえんだからな
選考なんか信じたら前みたいに裏切られるだけだ"	"What are you talking about?
Just because I'm out doesn't mean I'll ever admit to being a ghost.
If you believe in the selection, you'll be betrayed just like before."	"What are you saying?
Just because I'm out doesn't mean I approve of Onizuka.
If we trust a teacher, we'll be betrayed again like before."
決して	"何が言いたいんだよ お前
俺が外れたからって決して鬼塚を認めたわけじゃねえんだからな
選考なんか信じたら前みたいに裏切られるだけだ"	"What are you talking about?
Just because I'm out doesn't mean I'll ever admit to being a ghost.
If you believe in the selection, you'll be betrayed just like before."	"What are you saying?
Just because I'm out doesn't mean I approve of Onizuka.
If we trust a teacher, we'll be betrayed again like before."
外れ	"何が言いたいんだよ お前
俺が外れたからって決して鬼塚を認めたわけじゃねえんだからな
選考なんか信じたら前みたいに裏切られるだけだ"	"What are you talking about?
Just because I'm out doesn't mean I'll ever admit to being a ghost.
If you believe in the selection, you'll be betrayed just like before."	"What are you saying?
Just because I'm out doesn't mean I approve of Onizuka.
If we trust a teacher, we'll be betrayed again like before."
あっ	"でもそしたらね先生に友達を作るんじゃねえって叱られたんだ
それに先生ったら俺が学校を面白くしてやるって ほらでもあったりでもそんなことを言う先生って初めてだよ
菊池君も先生のことをもっとよく知ればきっと"	"But then my teacher told me not to make friends.
And it's the first time I've ever been told by a teacher or anyone else that I make school fun.
If only you knew more about him."	"Anyway, he scolded me and told me to not tell on my friends.
Also, he said that he'll make this school more interesting. Whether he was blowing smoke, I've never heard a teacher say that.
If you get to know him better, you'll probably..."
生っ	"でもそしたらね先生に友達を作るんじゃねえって叱られたんだ
それに先生ったら俺が学校を面白くしてやるって ほらでもあったりでもそんなことを言う先生って初めてだよ
菊池君も先生のことをもっとよく知ればきっと"	"But then my teacher told me not to make friends.
And it's the first time I've ever been told by a teacher or anyone else that I make school fun.
If only you knew more about him."	"Anyway, he scolded me and told me to not tell on my friends.
Also, he said that he'll make this school more interesting. Whether he was blowing smoke, I've never heard a teacher say that.
If you get to know him better, you'll probably..."
叱ら	"うん 僕が合成写真の犯人知ってるって言ったら
でもそしたらね先生に友達を作るんじゃねえって叱られたんだ
それに先生ったら俺が学校を面白くしてやるって ほらでもあったりでもそんなことを言う先生って初めてだよ"	"Yeah, if I told you that I knew who took the photos.
But then my teacher told me not to make friends.
And it's the first time I've ever been told by a teacher or anyone else that I make school fun."	"-You mean Onizuka? -Yeah. When I told him I knew who made the composite photo...
Anyway, he scolded me and told me to not tell on my friends.
Also, he said that he'll make this school more interesting. Whether he was blowing smoke, I've never heard a teacher say that."
そしたら	"うん 僕が合成写真の犯人知ってるって言ったら
でもそしたらね先生に友達を作るんじゃねえって叱られたんだ
それに先生ったら俺が学校を面白くしてやるって ほらでもあったりでもそんなことを言う先生って初めてだよ"	"Yeah, if I told you that I knew who took the photos.
But then my teacher told me not to make friends.
And it's the first time I've ever been told by a teacher or anyone else that I make school fun."	"-You mean Onizuka? -Yeah. When I told him I knew who made the composite photo...
Anyway, he scolded me and told me to not tell on my friends.
Also, he said that he'll make this school more interesting. Whether he was blowing smoke, I've never heard a teacher say that."
外さ	"しょうがねえだろう そんなに言うならお前として勝手にやれよ
悪いけど俺は今回外させてもらうぜ
ちょっと待ってよどういうことよそれ 何笑ってんだよ"	"If you're going to say that, do it on your own.
I'm sorry, but I'll let you out this time.
Wait a minute. What do you mean?"	"I can't help it. If you aren't happy, why don't you do it yourself?
Sorry, but I don't wanna participate this time.
Wait a minute! What do you mean by that? -What are you laughing at? -Nothing in particular."
しょうが	"あんたには期待してたのにさぁ 全然ダメージ受けてないじゃない鬼塚の奴
しょうがねえだろう そんなに言うならお前として勝手にやれよ
悪いけど俺は今回外させてもらうぜ"	"I was expecting you. You're not damaged at all, asshole.
If you're going to say that, do it on your own.
I'm sorry, but I'll let you out this time."	"What happened, Kikuchi? I expected you would do a better job. That bastard, Onizuka. He doesn't seem crushed at all.
I can't help it. If you aren't happy, why don't you do it yourself?
Sorry, but I don't wanna participate this time."
受け	"笑った奴は処刑するからなぁ どうしたのよ菊池
あんたには期待してたのにさぁ 全然ダメージ受けてないじゃない鬼塚の奴
しょうがねえだろう そんなに言うならお前として勝手にやれよ"	"I'm going to execute anyone who laughs.
I was expecting you. You're not damaged at all, asshole.
If you're going to say that, do it on your own."	"If you do, there will be consequences! What happened, Kikuchi? I expected you would do a better job.
What happened, Kikuchi? I expected you would do a better job. That bastard, Onizuka. He doesn't seem crushed at all.
I can't help it. If you aren't happy, why don't you do it yourself?"
処刑	"裏切り者がいいか 鬼塚の前で二度と笑うなよ
笑った奴は処刑するからなぁ どうしたのよ菊池
あんたには期待してたのにさぁ 全然ダメージ受けてないじゃない鬼塚の奴"	"Don't you ever laugh in front of a ghost again.
I'm going to execute anyone who laughs.
I was expecting you. You're not damaged at all, asshole."	"Traitors! Do you hear me? Never laugh in front of him again!
If you do, there will be consequences! What happened, Kikuchi? I expected you would do a better job.
What happened, Kikuchi? I expected you would do a better job. That bastard, Onizuka. He doesn't seem crushed at all."
裏切り者	"ねっ 鬼塚の授業で何喜んでんだよ
裏切り者がいいか 鬼塚の前で二度と笑うなよ
笑った奴は処刑するからなぁ どうしたのよ菊池"	"Hey, I'm so happy for you.
Don't you ever laugh in front of a ghost again.
I'm going to execute anyone who laughs."	"You guys! Why in the world are you having fun in Onizuka's class?
Traitors! Do you hear me? Never laugh in front of him again!
If you do, there will be consequences! What happened, Kikuchi? I expected you would do a better job."
喜ん	"じゃあなぁ
ねっ 鬼塚の授業で何喜んでんだよ
裏切り者がいいか 鬼塚の前で二度と笑うなよ"	"I'll see you.
Hey, I'm so happy for you.
Don't you ever laugh in front of a ghost again."	"So, look forward to it. See you!
You guys! Why in the world are you having fun in Onizuka's class?
Traitors! Do you hear me? Never laugh in front of him again!"
恐怖	"今日の授業はこれまでだ 面白かっただろう
今度は恐怖の白いジャムの話をしてやるからな 楽しみにしたらよ
じゃあなぁ"	"We've had lessons so far. It must have been fun.
I'll tell you about the white jelly of fear, if you're looking forward to it.
I'll see you."	"Okay, that's it for today. Wasn't it fun?
Next time, I'll tell you the story of Scary White Jam. So, look forward to it. See you!
So, look forward to it. See you!"
くだら	"なんだよそれ
くだらねえ
今日の授業はこれまでだ 面白かっただろう"	"What's that?
, hey
We've had lessons so far. It must have been fun."	"What the hell is that?
It's so dumb!
Okay, that's it for today. Wasn't it fun?"
くっつい	"すると
蓋の裏に全部くっついてたんだってよ
なんだよそれ"	"And then
He said it was all stuck behind the lid.
What's that?"	"Then, he saw...
All the dumplings were stuck on the back of the lid.
What the hell is that?"
裏	"すると
蓋の裏に全部くっついてたんだってよ
なんだよそれ"	"And then
He said it was all stuck behind the lid.
What's that?"	"Then, he saw...
All the dumplings were stuck on the back of the lid.
What the hell is that?"
覗き	"どうなってるんだ
恐ろしくなってもう一度よーく覗き込んだ
すると"	"What's going on?
I got scared, and I peeked again.
And then"	"There were no dumplings left! What was going on?
Though he was scared, he looked into the box carefully.
Then, he saw..."
恐ろしく	"どうなってるんだ
恐ろしくなってもう一度よーく覗き込んだ
すると"	"What's going on?
I got scared, and I peeked again.
And then"	"There were no dumplings left! What was going on?
Though he was scared, he looked into the box carefully.
Then, he saw..."
個	"そして一遍蓋を閉めて、もう一度ゆっくりと蓋を開けた
ない、一個もねえ
シュウマイが一個もなくなってるじゃねえか"	"And then I closed the lid again, and slowly opened it again.
No, not one.
You're running out of shumais."	"Then he put the lid back on. Once more, slowly, he opened the lid.
None! There was none left!
There were no dumplings left! What was going on?"
	"そして一遍蓋を閉めて、もう一度ゆっくりと蓋を開けた
ない、一個もねえ
シュウマイが一個もなくなってるじゃねえか"	"And then I closed the lid again, and slowly opened it again.
No, not one.
You're running out of shumais."	"Then he put the lid back on. Once more, slowly, he opened the lid.
None! There was none left!
There were no dumplings left! What was going on?"
遍	"その人は、怖くなって大声を上げた
そして一遍蓋を閉めて、もう一度ゆっくりと蓋を開けた
ない、一個もねえ"	"He was scared, and he screamed.
And then I closed the lid again, and slowly opened it again.
No, not one."	"The guy was so scared that he screamed!
Then he put the lid back on. Once more, slowly, he opened the lid.
None! There was none left!"
大声	"そしたら、なんと今度は三個も一遍に消えてやがった
その人は、怖くなって大声を上げた
そして一遍蓋を閉めて、もう一度ゆっくりと蓋を開けた"	"And then, this time, all three of them disappeared.
He was scared, and he screamed.
And then I closed the lid again, and slowly opened it again."	"This time... believe it or not, three more were missing all at once!
The guy was so scared that he screamed!
Then he put the lid back on. Once more, slowly, he opened the lid."
角	"きっと、きっと最初から一個足りなかったんだろうって
でも、やっぱり気になって次の角でまた蓋を開けた
すると、またシュウマイが一個減ってるじゃねえか"	"I'm sure there was one missing in the first place.
But then I got curious and opened the lid again at the next corner.
And then there's another one less shumai."	"he convinced himself that one was missing from the beginning.
But... He kept thinking about it, so he opened the box again at the next corner.
Another dumpling was missing."
最初	"その人は、ゾーッとしながらも自分に言い聞かせたんだ
きっと、きっと最初から一個足りなかったんだろうって
でも、やっぱり気になって次の角でまた蓋を開けた"	"He told himself that, even though he was terrified.
I'm sure there was one missing in the first place.
But then I got curious and opened the lid again at the next corner."	"Though this guy had a chill down his back,
he convinced himself that one was missing from the beginning.
But... He kept thinking about it, so he opened the box again at the next corner."
言い聞かせ	"ひとつ、シュウマイが減ってたんだよ
その人は、ゾーッとしながらも自分に言い聞かせたんだ
きっと、きっと最初から一個足りなかったんだろうって"	"One thing, I was losing my shumai.
He told himself that, even though he was terrified.
I'm sure there was one missing in the first place."	"One dumpling was missing.
Though this guy had a chill down his back,
he convinced himself that one was missing from the beginning."
ゾーッ	"ひとつ、シュウマイが減ってたんだよ
その人は、ゾーッとしながらも自分に言い聞かせたんだ
きっと、きっと最初から一個足りなかったんだろうって"	"One thing, I was losing my shumai.
He told himself that, even though he was terrified.
I'm sure there was one missing in the first place."	"One dumpling was missing.
Though this guy had a chill down his back,
he convinced himself that one was missing from the beginning."
減っ	"あ、開けると?
ひとつ、シュウマイが減ってたんだよ
その人は、ゾーッとしながらも自分に言い聞かせたんだ"	"What do you say we open it?
One thing, I was losing my shumai.
He told himself that, even though he was terrified."	"When he opened it...
One dumpling was missing.
Though this guy had a chill down his back,"
蓋	"振り返ってみると
無性に気になって、シュウマイの蓋を開けると
あ、開けると?"	"in retrospect
I'm just a little nervous, and then I open up my shoemaker.
What do you say we open it?"	"he felt uneasy for some reason, so he turned around...
He couldn't stop feeling uneasy, so he removed the lid of the box.
When he opened it..."
無性に	"振り返ってみると
無性に気になって、シュウマイの蓋を開けると
あ、開けると?"	"in retrospect
I'm just a little nervous, and then I open up my shoemaker.
What do you say we open it?"	"he felt uneasy for some reason, so he turned around...
He couldn't stop feeling uneasy, so he removed the lid of the box.
When he opened it..."
振り返っ	"なぜか胸騒ぎがして
振り返ってみると
無性に気になって、シュウマイの蓋を開けると"	"I don't know why.
in retrospect
I'm just a little nervous, and then I open up my shoemaker."	"he felt uneasy for some reason, so he turned around...
he felt uneasy for some reason, so he turned around...
He couldn't stop feeling uneasy, so he removed the lid of the box."
胸騒ぎ	"ところが、その帰り道
なぜか胸騒ぎがして
振り返ってみると"	"But that's the way home.
I don't know why.
in retrospect"	"But then... on his way home,
he felt uneasy for some reason, so he turned around...
he felt uneasy for some reason, so he turned around..."
関係	"ああ、その人は地元でも相当気合の入った人だったんで
関係ねえとかって、買って帰ることにしたらしいんだ
ところが、その帰り道"	"Yeah, he was a pretty decent guy in the neighborhood.
He said he didn't care, so he bought it and went home.
But that's the way home."	"This guy, who was known for his fearlessness,
ignored the rumor and decided to buy a box there.
But then... on his way home,"
らしい	"ああ、その人は地元でも相当気合の入った人だったんで
関係ねえとかって、買って帰ることにしたらしいんだ
ところが、その帰り道"	"Yeah, he was a pretty decent guy in the neighborhood.
He said he didn't care, so he bought it and went home.
But that's the way home."	"This guy, who was known for his fearlessness,
ignored the rumor and decided to buy a box there.
But then... on his way home,"
気合	"シュウマイ屋があったんだと
ああ、その人は地元でも相当気合の入った人だったんで
関係ねえとかって、買って帰ることにしたらしいんだ"	"He said there was a shoe store.
Yeah, he was a pretty decent guy in the neighborhood.
He said he didn't care, so he bought it and went home."	"a store was making dumplings with human flesh.
This guy, who was known for his fearlessness,
ignored the rumor and decided to buy a box there."
相当	"シュウマイ屋があったんだと
ああ、その人は地元でも相当気合の入った人だったんで
関係ねえとかって、買って帰ることにしたらしいんだ"	"He said there was a shoe store.
Yeah, he was a pretty decent guy in the neighborhood.
He said he didn't care, so he bought it and went home."	"a store was making dumplings with human flesh.
This guy, who was known for his fearlessness,
ignored the rumor and decided to buy a box there."
地元	"シュウマイ屋があったんだと
ああ、その人は地元でも相当気合の入った人だったんで
関係ねえとかって、買って帰ることにしたらしいんだ"	"He said there was a shoe store.
Yeah, he was a pretty decent guy in the neighborhood.
He said he didn't care, so he bought it and went home."	"a store was making dumplings with human flesh.
This guy, who was known for his fearlessness,
ignored the rumor and decided to buy a box there."
シュウマイ	"これは、昔、俗の先輩から聞いた話なんだが
ある町に、人肉でシュウマイ作ってるって噂のある
シュウマイ屋があったんだと"	"This is a story I've heard from the old folk.
There's a rumor going around town that they make shumai out of human flesh.
He said there was a shoe store."	"I heard this story from my senior when I was in a motorcycle gang.
In a certain town, there was a rumor that
a store was making dumplings with human flesh."
先輩	"センキュー!
これは、昔、俗の先輩から聞いた話なんだが
ある町に、人肉でシュウマイ作ってるって噂のある"	"The Senkyu!
This is a story I've heard from the old folk.
There's a rumor going around town that they make shumai out of human flesh."	"Thank you!
I heard this story from my senior when I was in a motorcycle gang.
In a certain town, there was a rumor that"
念願	"そしてこの真っ白なクレスタで
念願の家族旅行に行くんだよ!
センキュー!"	"And then there's this white crest.
I'm going on a family vacation!
The Senkyu!"	"In my Cresta, my white Cresta
I will go on a long-awaited family trip!
Thank you!"
真っ白	"私にはこのクレスタがある
そしてこの真っ白なクレスタで
念願の家族旅行に行くんだよ!"	"I have this crest.
And then there's this white crest.
I'm going on a family vacation!"	"In my Cresta, my white Cresta
In my Cresta, my white Cresta
I will go on a long-awaited family trip!"
関わる	"クレスタさえあれば、昔のように可愛かった娘と優しかった妻に囲まれた幸せな家族に戻れる。
もう、鬼塚なんかに関わるのはよそ!
私にはこのクレスタがある"	"With only Cresta, he can return to his happy family as before, surrounded by his lovely daughter and kind wife.
I don't want anything to do with the Ghosts anymore!
I have this crest."	"As long as I have my Cresta, I can have a happy family with my lovely daughter and loving wife back, just like before.
I won't get involved with Onizuka anymore.
In my Cresta, my white Cresta"
囲ま	"ね。分かった。
クレスタさえあれば、昔のように可愛かった娘と優しかった妻に囲まれた幸せな家族に戻れる。
もう、鬼塚なんかに関わるのはよそ!"	"That's right. I got it.
With only Cresta, he can return to his happy family as before, surrounded by his lovely daughter and kind wife.
I don't want anything to do with the Ghosts anymore!"	"No problem.
As long as I have my Cresta, I can have a happy family with my lovely daughter and loving wife back, just like before.
I won't get involved with Onizuka anymore."
優しかっ	"ね。分かった。
クレスタさえあれば、昔のように可愛かった娘と優しかった妻に囲まれた幸せな家族に戻れる。
もう、鬼塚なんかに関わるのはよそ!"	"That's right. I got it.
With only Cresta, he can return to his happy family as before, surrounded by his lovely daughter and kind wife.
I don't want anything to do with the Ghosts anymore!"	"No problem.
As long as I have my Cresta, I can have a happy family with my lovely daughter and loving wife back, just like before.
I won't get involved with Onizuka anymore."
可愛かっ	"ね。分かった。
クレスタさえあれば、昔のように可愛かった娘と優しかった妻に囲まれた幸せな家族に戻れる。
もう、鬼塚なんかに関わるのはよそ!"	"That's right. I got it.
With only Cresta, he can return to his happy family as before, surrounded by his lovely daughter and kind wife.
I don't want anything to do with the Ghosts anymore!"	"No problem.
As long as I have my Cresta, I can have a happy family with my lovely daughter and loving wife back, just like before.
I won't get involved with Onizuka anymore."
指輪	"本当?行く行く。ねえ。
私も指輪が欲しいんだけど。
ね。分かった。"	"Is that right? I'm on my way. Hey, whoa.
I want a ring, too.
That's right. I got it."	"Really? I'll go! I'll go! Mom, you're going too, right?
There's this ring that I want...
No problem."
欲し	"私いいよ。めんどくさいし、友達と遊んでる方がいいし。
お前が欲しがってたあのバッグ買ってやってもいいぞ。
本当?行く行く。ねえ。"	"I'm all right. It's better to be quiet and play with your friends.
I can buy that bag you wanted.
Is that right? I'm on my way. Hey, whoa."	"I wanna pass. I don't feel up to it. I'd rather hang out with my friends.
Well, I could buy you... that bag you always wanted.
Really? I'll go! I'll go! Mom, you're going too, right?"
めんどくさい	"クレスタで?
私いいよ。めんどくさいし、友達と遊んでる方がいいし。
お前が欲しがってたあのバッグ買ってやってもいいぞ。"	"In the Cresta?
I'm all right. It's better to be quiet and play with your friends.
I can buy that bag you wanted."	"to a hot spring in my Cresta.
I wanna pass. I don't feel up to it. I'd rather hang out with my friends.
Well, I could buy you... that bag you always wanted."
揃っ	"保険のおかげで新車になって戻ってくることになったんだよ。
そこで家族揃って温泉旅行にでも行かないかと思って。
クレスタで?"	"The insurance made it possible for me to come back with a new car.
So I decided to take my family on a trip to the hot springs.
In the Cresta?"	"Thanks to my insurance, my Cresta is coming back to me brand new.
So, I thought maybe we could go on a trip to a hot spring in my Cresta.
to a hot spring in my Cresta."
戻っ	"壊されたんじゃなかったの?鬼なんとか先生に潰されたって。
保険のおかげで新車になって戻ってくることになったんだよ。
そこで家族揃って温泉旅行にでも行かないかと思って。"	"I thought it was broken. The ghost somehow crushed him by the teacher.
The insurance made it possible for me to come back with a new car.
So I decided to take my family on a trip to the hot springs."	"Wasn't it destroyed? By a teacher named Oni-something?
Thanks to my insurance, my Cresta is coming back to me brand new.
So, I thought maybe we could go on a trip to a hot spring in my Cresta."
保険	"壊されたんじゃなかったの?鬼なんとか先生に潰されたって。
保険のおかげで新車になって戻ってくることになったんだよ。
そこで家族揃って温泉旅行にでも行かないかと思って。"	"I thought it was broken. The ghost somehow crushed him by the teacher.
The insurance made it possible for me to come back with a new car.
So I decided to take my family on a trip to the hot springs."	"Wasn't it destroyed? By a teacher named Oni-something?
Thanks to my insurance, my Cresta is coming back to me brand new.
So, I thought maybe we could go on a trip to a hot spring in my Cresta."
潰さ	"しかも、ホワイトパールの2.5エクシードだぞ。
壊されたんじゃなかったの?鬼なんとか先生に潰されたって。
保険のおかげで新車になって戻ってくることになったんだよ。"	"And that's two and a half exits of white pearls.
I thought it was broken. The ghost somehow crushed him by the teacher.
The insurance made it possible for me to come back with a new car."	"It's a Cresta. Not only that, it's the white-pearl 2.5 Exceed.
Wasn't it destroyed? By a teacher named Oni-something?
Thanks to my insurance, my Cresta is coming back to me brand new."
期待	"頼んだよ菊池くん
期待してるからな
3日間"	"Oh, please.
Because I expect it.
Three days."	"Kikuchi, don't disappoint me.
Kikuchi, don't disappoint me.
I'll give you three days. If that's too tight, one week."
サービス	"じゃあ2000円でどうだ?
出血代サービスで3000円だ
ジビデオも一本つけてやる"	"How about 2,000 yen?
It's 3,000 yen for the blood service.
I'll get you a video."	"No? What about 2,000 yen?
Okay. 3,000 yen, a sacrificial price...
And I'll throw in an X-rated, unedited video."
出血	"じゃあ2000円でどうだ?
出血代サービスで3000円だ
ジビデオも一本つけてやる"	"How about 2,000 yen?
It's 3,000 yen for the blood service.
I'll get you a video."	"No? What about 2,000 yen?
Okay. 3,000 yen, a sacrificial price...
And I'll throw in an X-rated, unedited video."
なんとか	"は?
早くなんとかしなければ
よかった"	"What's that?
We have to do something about it soon.
It was good"	"
I must do something quick...
I'm so relieved."
首	"作ってくんねえか?
あのその首のすげ替え写真
は?"	"Do you want to make some?
That photo of your neck being replaced.
What's that?"	"to make those composite photos where the faces are swapped?
to make those composite photos where the faces are swapped?
"
すげ替え	"作ってくんねえか?
あのその首のすげ替え写真
は?"	"Do you want to make some?
That photo of your neck being replaced.
What's that?"	"to make those composite photos where the faces are swapped?
to make those composite photos where the faces are swapped?
"
秘蔵	"何?
この写真と俺の秘蔵の雑誌でさ
作ってくんねえか?"	"what?
This photo and the magazine in my vault.
Do you want to make some?"	"What?
Could you use these photos and my magazines
to make those composite photos where the faces are swapped?"
放り出さ	"そんなことしたら
あんたが学園から放り出されるぜ
菊池よ"	"If you do that,
You're getting kicked off campus.
It's the pool."	"you will be kicked out of the school.
you will be kicked out of the school.
Hey, Kikuchi."
振るう	"退学か?
それとも暴力を振るう気か?
そんなことしたら"	"You dropped out of school?
Or are you going to use violence?
If you do that,"	"What are you gonna do? Expel me?
If you use violence,
you will be kicked out of the school."
暴力	"退学か?
それとも暴力を振るう気か?
そんなことしたら"	"You dropped out of school?
Or are you going to use violence?
If you do that,"	"What are you gonna do? Expel me?
If you use violence,
you will be kicked out of the school."
それとも	"退学か?
それとも暴力を振るう気か?
そんなことしたら"	"You dropped out of school?
Or are you going to use violence?
If you do that,"	"What are you gonna do? Expel me?
If you use violence,
you will be kicked out of the school."
退学	"どうする気だ?
退学か?
それとも暴力を振るう気か?"	"What are you gonna do?
You dropped out of school?
Or are you going to use violence?"	"What are you gonna do? Expel me?
What are you gonna do? Expel me?
If you use violence,"
落とし	"おい!何する気だよ
落とし目をつけるんだよ
てめえらついてきたな"	"Hey, whoa! What are you doing?
I'll drop it and close my eyes.
You've been following me."	"Hey, what are you gonna do?
I'm gonna make him pay.
You guys, if you follow us, I'll kill you."
気	"つらかせや
おい!何する気だよ
落とし目をつけるんだよ"	"Let it go.
Hey, whoa! What are you doing?
I'll drop it and close my eyes."	"Sorry to interrupt, but lend me your ear.
Hey, what are you gonna do?
I'm gonna make him pay."
	"ちょっといいがな
つらかせや
おい!何する気だよ"	"It's a little good.
Let it go.
Hey, whoa! What are you doing?"	"Sorry to interrupt, but lend me your ear.
Sorry to interrupt, but lend me your ear.
Hey, what are you gonna do?"
ゴキブリ	"ど どっから湧いて出やがった
ゴキブリ並だな
菊池よ"	"It came out of nowhere.
You look like a cockroach.
It's the pool."	"-Onizuka. -Where did you sneak in from?
Just like a cockroach.
Hey, Kikuchi."
湧い	"兄塚
ど どっから湧いて出やがった
ゴキブリ並だな"	"It's my brother.
It came out of nowhere.
You look like a cockroach."	"-Onizuka. -Where did you sneak in from?
-Onizuka. -Where did you sneak in from?
Just like a cockroach."
流せ	"気が散る
これを職員室のネットに流せば
もうあいつはおしまいだぜ"	"They are distracted
You can stream this to the staff room.
He's already dead."	"Shut up. You're distracting me.
When we put this on the intranet, that will be it for him!
When we put this on the intranet, that will be it for him!"
職員	"気が散る
これを職員室のネットに流せば
もうあいつはおしまいだぜ"	"They are distracted
You can stream this to the staff room.
He's already dead."	"Shut up. You're distracting me.
When we put this on the intranet, that will be it for him!
When we put this on the intranet, that will be it for him!"
散る	"黙っとろよ
気が散る
これを職員室のネットに流せば"	"Shut the fuck up.
They are distracted
You can stream this to the staff room."	"Shut up. You're distracting me.
Shut up. You're distracting me.
When we put this on the intranet, that will be it for him!"
黙っ	"菊池の合成写真ますます磨きがかかってんな
黙っとろよ
気が散る"	"The synthetic photos of the pool are getting more and more polished.
Shut the fuck up.
They are distracted"	"Kikuchi's skill is getting better. Awesome!
Shut up. You're distracting me.
Shut up. You're distracting me."
かかっ	"こいつがとどめだ、これであいつも学校にいられなくなるぜ
菊池の合成写真ますます磨きがかかってんな
黙っとろよ"	"He's not gonna be able to make it to school.
The synthetic photos of the pool are getting more and more polished.
Shut the fuck up."	"This is the final blow. This will make him leave.
Kikuchi's skill is getting better. Awesome!
Shut up. You're distracting me."
磨き	"こいつがとどめだ、これであいつも学校にいられなくなるぜ
菊池の合成写真ますます磨きがかかってんな
黙っとろよ"	"He's not gonna be able to make it to school.
The synthetic photos of the pool are getting more and more polished.
Shut the fuck up."	"This is the final blow. This will make him leave.
Kikuchi's skill is getting better. Awesome!
Shut up. You're distracting me."
ますます	"こいつがとどめだ、これであいつも学校にいられなくなるぜ
菊池の合成写真ますます磨きがかかってんな
黙っとろよ"	"He's not gonna be able to make it to school.
The synthetic photos of the pool are getting more and more polished.
Shut the fuck up."	"This is the final blow. This will make him leave.
Kikuchi's skill is getting better. Awesome!
Shut up. You're distracting me."
とどめ	"冬月先生
こいつがとどめだ、これであいつも学校にいられなくなるぜ
菊池の合成写真ますます磨きがかかってんな"	"Dr. Fuyuzuki
He's not gonna be able to make it to school.
The synthetic photos of the pool are getting more and more polished."	"Mr. Onizuka...
This is the final blow. This will make him leave.
Kikuchi's skill is getting better. Awesome!"
ビシッ	"あ、俺、ちょっと、野暮用があるので、行ってきます
優待離脱の落とし前、ビシッとつけてきますよ
冬月先生"	"Oh, I'm just going to take a nap.
I'm going to have a lot of fun with you before the discount goes down.
Dr. Fuyuzuki"	"I have some business to take care of. I'll be going.
I will make sure they will pay dearly for making my spirit leave my body.
Mr. Onizuka..."
優待	"あ、俺、ちょっと、野暮用があるので、行ってきます
優待離脱の落とし前、ビシッとつけてきますよ
冬月先生"	"Oh, I'm just going to take a nap.
I'm going to have a lot of fun with you before the discount goes down.
Dr. Fuyuzuki"	"I have some business to take care of. I'll be going.
I will make sure they will pay dearly for making my spirit leave my body.
Mr. Onizuka..."
任せ	"あ、本当っすか?
うん、任せてください
あ、何笑ってるんですか?"	"Oh, really?
Yes, please.
What are you laughing at?"	"-Really? -Yes. Just leave it to me.
-Really? -Yes. Just leave it to me.
What are you laughing about?"
おごり	"あ、でも、なんかお詫びさせてください
そうだ!今夜、夕食をおごりますよ、ね?
あ、本当っすか?"	"Oh, I'm sorry about that.
That's right! I'll buy you dinner tonight, all right?
Oh, really?"	"Really? Oh, I'm relieved! But I want to make up for it.
I know! I'll treat you to dinner tonight.
-Really? -Yes. Just leave it to me."
夕食	"あ、でも、なんかお詫びさせてください
そうだ!今夜、夕食をおごりますよ、ね?
あ、本当っすか?"	"Oh, I'm sorry about that.
That's right! I'll buy you dinner tonight, all right?
Oh, really?"	"Really? Oh, I'm relieved! But I want to make up for it.
I know! I'll treat you to dinner tonight.
-Really? -Yes. Just leave it to me."
お詫び	"本当?よかった
あ、でも、なんかお詫びさせてください
そうだ!今夜、夕食をおごりますよ、ね?"	"Is that right? That's good.
Oh, I'm sorry about that.
That's right! I'll buy you dinner tonight, all right?"	"Really? Oh, I'm relieved! But I want to make up for it.
Really? Oh, I'm relieved! But I want to make up for it.
I know! I'll treat you to dinner tonight."
もらえれ	"ハッピー!
いいっすよ、分かってもらえれば
本当?よかった"	"Happy!
That's fine, if you can understand me.
Is that right? That's good."	"
It's okay. As long as you understand.
Really? Oh, I'm relieved! But I want to make up for it."
殴っ	"あの、鬼塚先生、私、ごめんなさい
私、先生のこと信じようとしないで、殴っちゃって
本当にごめんなさい"	"I'm sorry about that.
Don't try to believe me or the teacher.
I'm really sorry"	"Mr. Onizuka... I... I'm sorry.
I didn't believe you and I even slapped you. I am so sorry.
and I even slapped you. I am so sorry."
とけ	"この落とし前は俺がつける
お前は何も知らなかったことにしとけ、いいな
あ、冬月、じゃあ"	"I'll get you before this one drops.
Let's just say you didn't know anything.
Oh, the winter months."	"I will make them pay for this. You pretend you don't know anything.
I will make them pay for this. You pretend you don't know anything. Got it?
Fuyutsuki..."
落とし前	"先生
この落とし前は俺がつける
お前は何も知らなかったことにしとけ、いいな"	"teacher
I'll get you before this one drops.
Let's just say you didn't know anything."	"Teacher...
I will make them pay for this. You pretend you don't know anything.
I will make them pay for this. You pretend you don't know anything. Got it?"
信用	"同じクラスのやつだろ
同じクラスのだちをちくろうなんてやつは、俺は信用しねえぜ
先生"	"We're in the same class.
I don't trust a guy who's in the same class as you.
teacher"	"Someone in your class?
I don't wanna trust someone... who would tell on a classmate.
Teacher..."
ちく	"同じクラスのやつだろ
同じクラスのだちをちくろうなんてやつは、俺は信用しねえぜ
先生"	"We're in the same class.
I don't trust a guy who's in the same class as you.
teacher"	"Someone in your class?
I don't wanna trust someone... who would tell on a classmate.
Teacher..."
先	"おい、よしかわ
よしかわよ、その先を言うんじゃねえぞ
え?"	"Hey, how are you?
All right, well, you can't talk about that.
Oh, my God."	"Hey, Yoshikawa.
Yoshikawa, don't say anything else.
"
犯人	"くっ、合成写真!?
僕、犯人知ってるんだ
あ、あの写真作ったのは、うちのクラスの"	"Oh, my God!
I know who did it.
Oh, that photo was taken in my class."	"Composite?
I know who did it.
The person who made those photos is in our class."
載っ	"うん、アイコラだよ
雑誌なんかによく載ってるやつ
くっ、合成写真!?"	"Yes, it is Icola.
It's all over the magazines.
Oh, my God!"	"Yeah. You see them in magazines.
Yeah. You see them in magazines.
Composite?"
人格	"よしか
先生は二重人格なんかじゃないし、雄大離脱もしてないよ
あれ、全部パソコンで作った合成写真なんだ"	"Good to see you.
You're not a double personality, and you've never had an orgasm.
They're all computer-generated photos."	"Yoshikawa.
You don't have a split personality and your spirit isn't leaving your body.
They're composite photos created on a computer."
重	"よしか
先生は二重人格なんかじゃないし、雄大離脱もしてないよ
あれ、全部パソコンで作った合成写真なんだ"	"Good to see you.
You're not a double personality, and you've never had an orgasm.
They're all computer-generated photos."	"Yoshikawa.
You don't have a split personality and your spirit isn't leaving your body.
They're composite photos created on a computer."
離脱	"ううううう、そんなこと考えて遊んでる場合じゃねえ
先生、雄大離脱なんかしてないよ
あ?"	"Yeah, well, not when you're thinking about it.
Sir, I'm not going through withdrawal.
Oh, my God."	"Now's not the time for these stupid ideas.
Teacher, your spirit isn't leaving your body.
"
雄大	"ううううう、そんなこと考えて遊んでる場合じゃねえ
先生、雄大離脱なんかしてないよ
あ?"	"Yeah, well, not when you're thinking about it.
Sir, I'm not going through withdrawal.
Oh, my God."	"Now's not the time for these stupid ideas.
Teacher, your spirit isn't leaving your body.
"
場合	"なんちゃって、いやいや
ううううう、そんなこと考えて遊んでる場合じゃねえ
先生、雄大離脱なんかしてないよ"	"Oh, my God.
Yeah, well, not when you're thinking about it.
Sir, I'm not going through withdrawal."	"Wouldn't that be nice?
Now's not the time for these stupid ideas.
Teacher, your spirit isn't leaving your body."
過ごそ	"うふふふ
もちろんさ、さあ、限りなく透明に近い時を過ごそうぜ、ベイビー
なんちゃって、いやいや"	"Ufufufu
Of course. Well, let's spend some time near the infinite transparency, baby.
Oh, my God."	"
Of course. Let's spend an infinitely transparent time together, baby!
Wouldn't that be nice?"
透明	"うふふふ
もちろんさ、さあ、限りなく透明に近い時を過ごそうぜ、ベイビー
なんちゃって、いやいや"	"Ufufufu
Of course. Well, let's spend some time near the infinite transparency, baby.
Oh, my God."	"
Of course. Let's spend an infinitely transparent time together, baby!
Wouldn't that be nice?"
限り	"うふふふ
もちろんさ、さあ、限りなく透明に近い時を過ごそうぜ、ベイビー
なんちゃって、いやいや"	"Ufufufu
Of course. Well, let's spend some time near the infinite transparency, baby.
Oh, my God."	"
Of course. Let's spend an infinitely transparent time together, baby!
Wouldn't that be nice?"
たくましい	"うひひひひひひ
体は透けていても、すごくたくましいのね
うふふふ"	"Oh, my God.
It's very attractive, even though it's translucent.
Ufufufu"	"
Even when you're transparent, it's still very impressive.
"
透け	"うひひひひひひ
体は透けていても、すごくたくましいのね
うふふふ"	"Oh, my God.
It's very attractive, even though it's translucent.
Ufufufu"	"
Even when you're transparent, it's still very impressive.
"
ちくしょう	"悪魔め
ちくしょう
俺ってもしかして二重人格なのかな"	"Devil.
Chikushō
I don't know if I have a double personality."	"This devil!
Damn it! I wonder if I have a split personality.
Damn it! I wonder if I have a split personality."
微妙	"元二年四組の奴らのよく使う手なんですよ
ほらよく見ると頭のところと体の解像度が微妙に違うでしょ
そんな"	"It's a hand they used in their last two or four years.
If you look closely, there's a subtle difference in resolution between the head and the body.
That kind of"	"The students from the former Class 2-4 use this trick often.
If you look closely, the head and the body have a different resolution.
That's unbelievable."
解像度	"元二年四組の奴らのよく使う手なんですよ
ほらよく見ると頭のところと体の解像度が微妙に違うでしょ
そんな"	"It's a hand they used in their last two or four years.
If you look closely, there's a subtle difference in resolution between the head and the body.
That kind of"	"The students from the former Class 2-4 use this trick often.
If you look closely, the head and the body have a different resolution.
That's unbelievable."
組	"知らなかったんですか
元二年四組の奴らのよく使う手なんですよ
ほらよく見ると頭のところと体の解像度が微妙に違うでしょ"	"Didn't you know that?
It's a hand they used in their last two or four years.
If you look closely, there's a subtle difference in resolution between the head and the body."	"Didn't you know?
The students from the former Class 2-4 use this trick often.
If you look closely, the head and the body have a different resolution."
元	"知らなかったんですか
元二年四組の奴らのよく使う手なんですよ
ほらよく見ると頭のところと体の解像度が微妙に違うでしょ"	"Didn't you know that?
It's a hand they used in their last two or four years.
If you look closely, there's a subtle difference in resolution between the head and the body."	"Didn't you know?
The students from the former Class 2-4 use this trick often.
If you look closely, the head and the body have a different resolution."
上手	"そうじゃなくてですね
合成写真と見抜くのも難しいくらい上手にできてるって話してたんですよ
えそれ合成って"	"No, it's not.
I was talking about how they're so good at synthetic photography that it's hard to tell.
Yeah, that's synthetic."	"That's not what it is.
We were talking about how good it is. It's hard to tell it's a composite.
A composite?"
難しい	"そうじゃなくてですね
合成写真と見抜くのも難しいくらい上手にできてるって話してたんですよ
えそれ合成って"	"No, it's not.
I was talking about how they're so good at synthetic photography that it's hard to tell.
Yeah, that's synthetic."	"That's not what it is.
We were talking about how good it is. It's hard to tell it's a composite.
A composite?"
見抜く	"そうじゃなくてですね
合成写真と見抜くのも難しいくらい上手にできてるって話してたんですよ
えそれ合成って"	"No, it's not.
I was talking about how they're so good at synthetic photography that it's hard to tell.
Yeah, that's synthetic."	"That's not what it is.
We were talking about how good it is. It's hard to tell it's a composite.
A composite?"
合成	"そうじゃなくてですね
合成写真と見抜くのも難しいくらい上手にできてるって話してたんですよ
えそれ合成って"	"No, it's not.
I was talking about how they're so good at synthetic photography that it's hard to tell.
Yeah, that's synthetic."	"That's not what it is.
We were talking about how good it is. It's hard to tell it's a composite.
A composite?"
いたずら	"えいえ
いや今先生とこのいたずらを見ていたんですけどね
すみませんそういう変な写真はちょっと"	"Yes, you are.
No, I was just watching this with the teacher.
I'm sorry about the weird pictures."	"W-What?
We were just looking at this product of mischief.
Sorry, but I don't want to look at those pictures."
うまく	"奴の本性を暴くにはもっと接近にしなければ
ほうほんとだうまくできてる
冬月先生見ましたかこれ"	"We have to get closer to reveal his true nature.
It's really, really good.
Mr. Winter Moon, have you seen this?"	"In order to expose his true nature, I need to get closer.
Yeah, it really is well done.
Ms. Fuyutsuki, did you see this?"
接近	"まいったなあ
もっと接近するのだ
奴の本性を暴くにはもっと接近にしなければ"	"I'm not.
Get a little closer.
We have to get closer to reveal his true nature."	"I don't know what to do.
I need to get closer.
In order to expose his true nature, I need to get closer."
まいっ	"相変わらずえぐいなお前は
まいったなあ
もっと接近するのだ"	"You're as fast as you've ever been.
I'm not.
Get a little closer."	"You're so harsh, as usual.
I don't know what to do.
I need to get closer."
えぐい	"いや念には念を入れてもう一押ししとくか
相変わらずえぐいなお前は
まいったなあ"	"No, it's not. I mean, if you think about it, maybe you can push it a little bit more.
You're as fast as you've ever been.
I'm not."	"No. We wanna make extra sure with one more push.
You're so harsh, as usual.
I don't know what to do."
相変わらず	"いや念には念を入れてもう一押ししとくか
相変わらずえぐいなお前は
まいったなあ"	"No, it's not. I mean, if you think about it, maybe you can push it a little bit more.
You're as fast as you've ever been.
I'm not."	"No. We wanna make extra sure with one more push.
You're so harsh, as usual.
I don't know what to do."
念	"なあ菊池
いや念には念を入れてもう一押ししとくか
相変わらずえぐいなお前は"	"Hey, what's up?
No, it's not. I mean, if you think about it, maybe you can push it a little bit more.
You're as fast as you've ever been."	"We can leave him be and let him crumble on his own. Right, Kikuchi?
No. We wanna make extra sure with one more push.
You're so harsh, as usual."
押し	"なあ菊池
いや念には念を入れてもう一押ししとくか
相変わらずえぐいなお前は"	"Hey, what's up?
No, it's not. I mean, if you think about it, maybe you can push it a little bit more.
You're as fast as you've ever been."	"We can leave him be and let him crumble on his own. Right, Kikuchi?
No. We wanna make extra sure with one more push.
You're so harsh, as usual."
へこん	"ざまあみろっつーの
あとはほっといても勝手にへこんじまうさ
なあ菊池"	"It's not like I don't know what to do.
If you let him go, he'll do it on his own.
Hey, what's up?"	"He deserved it.
We can leave him be and let him crumble on his own. Right, Kikuchi?
We can leave him be and let him crumble on his own. Right, Kikuchi?"
ほっとい	"ざまあみろっつーの
あとはほっといても勝手にへこんじまうさ
なあ菊池"	"It's not like I don't know what to do.
If you let him go, he'll do it on his own.
Hey, what's up?"	"He deserved it.
We can leave him be and let him crumble on his own. Right, Kikuchi?
We can leave him be and let him crumble on his own. Right, Kikuchi?"
勝手	"ざまあみろっつーの
あとはほっといても勝手にへこんじまうさ
なあ菊池"	"It's not like I don't know what to do.
If you let him go, he'll do it on his own.
Hey, what's up?"	"He deserved it.
We can leave him be and let him crumble on his own. Right, Kikuchi?
We can leave him be and let him crumble on his own. Right, Kikuchi?"
	"ラブホカラ?
誰だこの女は 誰か知らねえかこの女
おい"	"What's that?
Who is this woman? I don't know.
Hey"	"I'm leaving a love hotel.
Who the hell is this woman? Does anyone know?
Who the hell is this woman? Does anyone know?"
	"考えてみれば、鬼塚先生のプライベートな趣味を私が咎める筋合いではありませんし。
だ、だから、それじゃ困るんだってば、椎月ちゃん。
どうして困るんです?"	"If you think about it, I don't blame Mr. Gokutsuka for his personal hobbies.
That's why you're in trouble.
What's the big deal?"	"I don't have any right to make an issue of your private hobbies.
No, it's important that we clear this up, Fuyutsuki!
Why is that?"
	"まあ、あの先生ならやりそうなことかもしれないけど、
話が出来すぎてて、あたしは面白くないね。
そんなに単純な話なのかねこの事件は"	"Well, maybe that's what he would have done.
I'm too good to talk. I'm not funny.
I don't know if it's that simple."	"Well, he might be the kind of person to do such a thing,
but I'm not convinced. The story is a little too perfect.
I wonder if this incident is as simple as it looks."
	"そうよ。あたしたちに担任なんていらないってことを、学園に思い知らせてやるのよ。
専攻なんて、みんな自殺でもしちゃえばいいんだわ。
来たぞ!"	"That's right. I want you to let the school know that we don't need your help.
I mean, if you're going to major in any of these subjects, you should kill yourself.
It's here!"	"That's right. We'll let the school know that we don't need a teacher.
All these teachers should kill themselves!
Hey, he's coming!"
	"先生よ! 信じてたのに!
違うって! 誤解だって! 冬月ちゃん!
俺じゃねえって!"	"It's the teacher! I thought you did!
I said no! It was a misunderstanding. It's the winter moon!
It wasn't me!"	"You're the worst, Onizuka! I never imagined you had such a hobby! -I trusted you! -No, it's a misunderstanding!
-I trusted you! -No, it's a misunderstanding!
It's not me. I've never even seen a wooden horse like this!"
	"え、まだ乾杯してなかったんですか?
気にしない、気にしない
教頭先生、挨拶長いから"	"Yeah, haven't you had a toast yet?
It doesn't matter.
Principal, I've been waiting a long time."	"What? We haven't toasted yet?
Don't worry, don't worry.
The vice principal's speech always lasts a while. Here, I'm Sannomaru."
	"俺の予定じゃ、ピチピチの女子高生に囲まれて、バランドの学園生活のはずだったのに。
それがしょうべんくせい、ちゅーぼう泣いてたよ。
さっきちょっと小耳に挟んだんですけど、先生が担任になられた三年四組って、"	"My plan was to be surrounded by a bunch of high school girls and live in Ballarat.
That's why I was crying so hard.
And I've heard a little bit about it before, but in the last three or four years of my teaching career"	"My plan was to be surrounded by high school girls. My life was going to be so rosy.
But I'm in charge of immature junior high kids.
I heard a little earlier that your homeroom, Class 3-4..."
	"だいたい教師としての自覚が足りないんだ!
なんだその金髪は!ピアスは!
こういうような奴が私の下につくかと思った!"	"I don't know much about being a teacher!
What's with the blond hair? Pierce, please!
I thought a guy like that would get under me!"	"You are a teacher! You aren't even aware you're a teacher!
What's with your blond hair and pierced ears?
The thought of someone like you reporting to me"
	"説明してくれよ、ザビ野郎!
お前たち、静かにせんか!
マイク!"	"Explain it to me, you bastard!
You guys, shut up!
The mic!"	"I was told I'd be teaching high school. I demand an explanation, Xavier!
Hey, all of you. Be quiet!
Mr. Onizuka, the microphone!"
	"ちょちょちょ、ちょっと、聞いてねえよ!
俺は理事長から高校教師って聞いたからこうやって。
説明してくれよ、ザビ野郎!"	"Whoa, whoa, whoa, listen!
I was told by the school board that I'm a high-school teacher.
Explain it to me, you bastard!"	"W-Wait a minute!
I was told I'd be teaching high school. I demand an explanation, Xavier!
I was told I'd be teaching high school. I demand an explanation, Xavier!"
	"へへへ、冬月先生はぜひ遊びに来てくださいね。
いい気でいられるのも今のうちだぞ、鬼塚英吉。
へぇ、続きまして森林の先生方をご紹介します。"	"Hey, Mr. Winter Moon, please come and visit.
It's only now that you can be in a good mood.
Hey, I'd like to introduce you to my forest teacher."	"Yes. Please come visit me.
You can be happy for just a little while, Eikichi Onizuka.
Next, I will introduce our new teachers."
	"まもなく修行式が始まります。
へぇ、じゃあ学校に住むことになったんですか。
へへへ、冬月先生はぜひ遊びに来てくださいね。"	"The ceremony will begin soon.
Hey, so you're living at the school?
Hey, Mr. Winter Moon, please come and visit."	"The ceremony will commence.
So you're going to live on campus?
Yes. Please come visit me."
	"よし、よしかわのぼる
よしかわ様ですか?これからよろしく頼みますな
理事長!あんな男をうちの教員に迎えるなんて、私にはどうしても理解できません!"	"All right, I got it.
Are you all right? I'll see you later.
Chairman! I can't believe we have a guy like that in our class!"	"Noboru Yoshikawa.
Honorable Yoshikawa! I beg for your instruction.
Mrs. Chairwoman! I don't understand why we need to welcome him as a faculty member!"
	"あ、ぼ、ぼく、その…
来いって言ってんだろうが
はい"	"Oh, my God.
I thought you said you were coming.
Yes"	"I...
I'm telling you to come here.
Yes, sir."
	"ええ 鬼塚君は今日から
この学校に住むことになったんすよ
それが採用の条件だったんす"	"Yes, Gokutsuka. You started today.
I'm sorry you have to live in this school.
That was a condition of employment."	"Starting today, Onizuka will...
Live on campus. That was the requirement for employment.
Live on campus. That was the requirement for employment. What?"
	"ティワナかあそこの牛は
うまいわな
ゲートを通過しましたら"	"I don't know about Tiwana or the cows there.
Umaiwana
If you go through the gate,"	"Tijuana... The beef there is really tasty.
Tijuana... The beef there is really tasty.
Attention, please. We will soon arrive at the gate."
	"話が奪すぎると思ったんだよな。
採用してくれる上に、家まで用意してくれるなんてよ。
完全に騙されたぜ。"	"I thought it was too much to talk about.
They'll hire you, and they'll give you a place to live.
You've been completely fooled."	"I knew it was too good to be true.
They were gonna hire me and provide housing.
I was completely cheated."
	"じゃあ、修行式には遅れないようにね。
話が奪すぎると思ったんだよな。
採用してくれる上に、家まで用意してくれるなんてよ。"	"Well, don't be late for the rehearsal.
I thought it was too much to talk about.
They'll hire you, and they'll give you a place to live."	"Don't be late for the opening ceremony.
I knew it was too good to be true.
They were gonna hire me and provide housing."
	"引き受けてもらえますね
どうするトロッコ 決めるのはおめえだ
私は先生を信じてますから"	"I'd like you to accept it.
It's up to you, Troko.
I believe in my teachers."	"We want her to compete.
What do you want to do? It's up to you to make the decision.
I trust you, Teacher."
	"私(わたし) 小さい時 川に落ちたことがあるの
その川は もうマンションになって 埋(う)められちゃったんだって
でも いま思い出したの"	"I once fell into a river when I was little.
The river has already become an apartment and it's been buried.
But I just remembered."	"Once, when I was little, I fell into a river.
She said they'd drained it and built things on top.
But I've just remembered."
	"いえ でも とっても 大事なものだって
ハクの代わりに謝(あやま)りに来ました
ごめんなさい"	"No, but it's very important.
I came to apologize instead of Haku.
I am sorry"	"No, but I know it's very precious.
I'm here to apologize for Haku. I'm sorry.
I'm here to apologize for Haku. I'm sorry."
