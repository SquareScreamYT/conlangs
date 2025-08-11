# Vilantic

## Introduction

Vilantic blah blah. Example: blah blah.

## Phonology

### Consonants

|             | Bilabial  | Alveolar       | Palatal        | Velar     |
|-------------|-----------|----------------|----------------|-----------|
| Nasals      | m         | n              |                | ŋ \<ń>    |
| Plosives    | p b       | t d            |                | k g       |
| Fricatives  | f v       | s z            | ʃ ʒ ç \<ś ź x> | h \<h>    |
| Affricates  |           | ts \<c>        | tʃ \<ć>        |           |
| Liquids     | w         | l ɾ ɬ \<l r ł> | j \<j>         |           |

### Vowels

|       | Front     | Central | Back  |
|-------|-----------|---------|-------|
| Close | i y       |         | u     |
| Mid   | e ø       | ə \<é>  | o     |
| Open  |           | a       |       |

### Phonotactics

Vilantic follows a (C)V(n) syllable structure, where:

* C can be any consonant.
* V can be any vowel.
* n is optional and is pronounced [n].
* final [n] may not occur before [n] or any vowel, unless part of a compund word, then is separated from the next letter by an apostrophe.
* [wu] and [ji] are invalid syllables.
* [y] can only occur after [ʃ ʒ tʃ j n l]

### Allophones

* [n] is pronounced [m] before [p b] and [ŋ] before [k g]

## Grammar

### Pronouns

Here is a chart of Vilantic's pronouns.

Pronouns follow a format of "PNC(N)", where P is person, N is number and C is case.

#### Person Chart

| 1 | 2 | 2FOR | 3 | 4 | PRX | MED | DIS |
|---|---|------|---|---|-----|-----|-----|
| a | i | é    | u | y | e   | o   | ø   |

The fourth person is used for indefinite referents:

```text
yźa     ćéźémøn         reźoni
4SG.NOM eat.PRS.NEC.NEG uranium.COLL.ACC
"one should not consume uranium"
```

#### Number Chart

| SG | DU | DU.DISTR | PAU | PAU.DISTR | PL | PL.DISTR | COL |
|----|----|----------|-----|-----------|----|----------|-----|
| ź  | ś  | ś...n    | l   | l...n     | ć  | ć...n    | n   |

Use the collective case when referring to uncountable or mass nouns.

#### Case Chart

Vilantic has 8 cases: Nominative, Accusative, Genitive, Dative, Locative, Vocative, Comitative and Instrumental:

| NOM | ACC | GEN | DAT | LOC | VOC | COM | INS |
|-----|-----|-----|-----|-----|-----|-----|-----|
| a   | i   | u   | e   | o   | é   | ø   | y   |

To make `3PAU.DISTR.ACC`, we must find the components of the pronoun.  
In this case, P is "u", N is "l...n" and C is "i".  
To make `3PAU.DISTR.ACC`, we combine them to make "ulin".

#### Chart of every possible pronoun

|               | NOM   | ACC   | GEN   | DAT   | LOC   | VOC   | COM   | INS   |
|---------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 1SG           | aźa   | aźi   | aźu   | aźe   | aźo   | aźé   | aźø   | aźy   |
| 1DU           | aśa   | aśi   | aśu   | aśe   | aśo   | aśé   | aśø   | aśy   |
| 1DU.DISTR     | aśan  | aśin  | aśun  | aśen  | aśon  | aśén  | aśøn  | aśyn  |
| 1PAU          | ala   | ali   | alu   | ale   | alo   | alé   | alø   | aly   |
| 1PAU.DISTR    | alan  | alin  | alun  | alen  | alon  | alén  | aløn  | alyn  |
| 1PL           | aća   | aći   | aću   | aće   | aćo   | aćé   | aćø   | aćy   |
| 1PL.DISTR     | aćan  | aćin  | aćun  | aćen  | aćon  | aćén  | aćøn  | aćyn  |
| 1COL          | ana   | ani   | anu   | ane   | ano   | ané   | anø   | any   |
| 2SG           | iźa   | iźi   | iźu   | iźe   | iźo   | iźé   | iźø   | iźy   |
| 2DU           | iśa   | iśi   | iśu   | iśe   | iśo   | iśé   | iśø   | iśy   |
| 2DU.DISTR     | iśan  | iśin  | iśun  | iśen  | iśon  | iśén  | iśøn  | iśyn  |
| 2PAU          | ila   | ili   | ilu   | ile   | ilo   | ilé   | ilø   | ily   |
| 2PAU.DISTR    | ilan  | ilin  | ilun  | ilen  | ilon  | ilén  | iløn  | ilyn  |
| 2PL           | ića   | ići   | iću   | iće   | ićo   | ićé   | ićø   | ićy   |
| 2PL.DISTR     | ićan  | ićin  | ićun  | ićen  | ićon  | ićén  | ićøn  | ićyn  |
| 2COL          | ina   | ini   | inu   | ine   | ino   | iné   | inø   | iny   |
| 2FOR.SG       | éźa   | éźi   | éźu   | éźe   | éźo   | éźé   | éźø   | éźy   |
| 2FOR.DU       | éśa   | éśi   | éśu   | éśe   | éśo   | éśé   | éśø   | éśy   |
| 2FOR.DU.DISTR | éśan  | éśin  | éśun  | éśen  | éśon  | éśén  | éśøn  | éśyn  |
| 2FOR.PAU      | éla   | éli   | élu   | éle   | élo   | élé   | élø   | ély   |
| 2FOR.PAU.DISTR| élan  | élin  | élun  | élen  | élon  | élén  | éløn  | élyn  |
| 2FOR.PL       | éća   | éći   | éću   | éće   | éćo   | éćé   | éćø   | éćy   |
| 2FOR.PL.DISTR | éćan  | éćin  | éćun  | éćen  | éćon  | éćén  | éćøn  | éćyn  |
| 2FOR.COL      | éna   | éni   | énu   | éne   | éno   | éné   | énø   | ény   |
| 3SG           | uźa   | uźi   | uźu   | uźe   | uźo   | uźé   | uźø   | uźy   |
| 3DU           | uśa   | uśi   | uśu   | uśe   | uśo   | uśé   | uśø   | uśy   |
| 3DU.DISTR     | uśan  | uśin  | uśun  | uśen  | uśon  | uśén  | uśøn  | uśyn  |
| 3PAU          | ula   | uli   | ulu   | ule   | ulo   | ulé   | ulø   | uly   |
| 3PAU.DISTR    | ulan  | ulin  | ulun  | ulen  | ulon  | ulén  | uløn  | ulyn  |
| 3PL           | uća   | ući   | uću   | uće   | ućo   | ućé   | ućø   | ućy   |
| 3PL.DISTR     | ućan  | ućin  | ućun  | ućen  | ućon  | ućén  | ućøn  | ućyn  |
| 3COL          | una   | uni   | unu   | une   | uno   | uné   | unø   | uny   |
| 4SG           | yźa   | yźi   | yźu   | yźe   | yźo   | yźé   | yźø   | yźy   |
| 4DU           | yśa   | yśi   | yśu   | yśe   | yśo   | yśé   | yśø   | yśy   |
| 4DU.DISTR     | yśan  | yśin  | yśun  | yśen  | yśon  | yśén  | yśøn  | yśyn  |
| 4PAU          | yla   | yli   | ylu   | yle   | ylo   | ylé   | ylø   | yly   |
| 4PAU.DISTR    | ylan  | ylin  | ylun  | ylen  | ylon  | ylén  | yløn  | ylyn  |
| 4PL           | yća   | yći   | yću   | yće   | yćo   | yćé   | yćø   | yćy   |
| 4PL.DISTR     | yćan  | yćin  | yćun  | yćen  | yćon  | yćén  | yćøn  | yćyn  |
| 4COL          | yna   | yni   | ynu   | yne   | yno   | yné   | ynø   | yny   |
| PRX.SG        | eźa   | eźi   | eźu   | eźe   | eźo   | eźé   | eźø   | eźy   |
| PRX.DU        | eśa   | eśi   | eśu   | eśe   | eśo   | eśé   | eśø   | eśy   |
| PRX.DU.DISTR  | eśan  | eśin  | eśun  | eśen  | eśon  | eśén  | eśøn  | eśyn  |
| PRX.PAU       | ela   | eli   | elu   | ele   | elo   | elé   | elø   | ely   |
| PRX.PAU.DISTR | elan  | elin  | elun  | elen  | elon  | elén  | eløn  | elyn  |
| PRX.PL        | eća   | eći   | eću   | eće   | ećo   | ećé   | ećø   | ećy   |
| PRX.PL.DISTR  | ećan  | ećin  | ećun  | ećen  | ećon  | ećén  | ećøn  | ećyn  |
| PRX.COL       | ena   | eni   | enu   | ene   | eno   | ené   | enø   | eny   |
| MED.SG        | oźa   | oźi   | oźu   | oźe   | oźo   | oźé   | oźø   | oźy   |
| MED.DU        | ośa   | ośi   | ośu   | ośe   | ośo   | ośé   | ośø   | ośy   |
| MED.DU.DISTR  | ośan  | ośin  | ośun  | ośen  | ośon  | ośén  | ośøn  | ośyn  |
| MED.PAU       | ola   | oli   | olu   | ole   | olo   | olé   | olø   | oly   |
| MED.PAU.DISTR | olan  | olin  | olun  | olen  | olon  | olén  | oløn  | olyn  |
| MED.PL        | oća   | oći   | oću   | oće   | oćo   | oćé   | oćø   | oćy   |
| MED.PL.DISTR  | oćan  | oćin  | oćun  | oćen  | oćon  | oćén  | oćøn  | oćyn  |
| MED.COL       | ona   | oni   | onu   | one   | ono   | oné   | onø   | ony   |
| DIS.SG        | øźa   | øźi   | øźu   | øźe   | øźo   | øźé   | øźø   | øźy   |
| DIS.DU        | øśa   | øśi   | øśu   | øśe   | øśo   | øśé   | øśø   | øśy   |
| DIS.DU.DISTR  | øśan  | øśin  | øśun  | øśen  | øśon  | øśén  | øśøn  | øśyn  |
| DIS.PAU       | øla   | øli   | ølu   | øle   | ølo   | ølé   | ølø   | øly   |
| DIS.PAU.DISTR | ølan  | ølin  | ølun  | ølen  | ølon  | ølén  | øløn  | ølyn  |
| DIS.PL        | øća   | øći   | øću   | øće   | øćo   | øćé   | øćø   | øćy   |
| DIS.PL.DISTR  | øćan  | øćin  | øćun  | øćen  | øćon  | øćén  | øćøn  | øćyn  |
| DIS.COL       | øna   | øni   | ønu   | øne   | øno   | øné   | ønø   | øny   |

### Declension of Nouns

Declining nouns is similar to making pronouns, except that the "person" part is replaced with the noun.

#### Declension Chart

|           | NOM | ACC | GEN | DAT | LOC | VOC | COM | INS |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|
| SG        | źa  | źi  | źu  | źe  | źo  | źé  | źø  | źy  |
| DU        | śa  | śi  | śu  | śe  | śo  | śé  | śø  | śy  |
| DU.DISTR  | śan | śin | śun | śen | śon | śén | śøn | śyn |
| PAU       | la  | li  | lu  | le  | lo  | lé  | lø  | ly  |
| PAU.DISTR | lan | lin | lun | len | lon | lén | løn | lyn |
| PL        | ća  | ći  | ću  | će  | ćo  | ćé  | ćø  | ćy  |
| PL.DISTR  | ćan | ćin | ćun | ćen | ćon | ćén | ćøn | ćyn |
| COL       | na  | ni  | nu  | ne  | no  | né  | nø  | ny  |

Examples:

```text
ringoni
apple.COL.ACC
"that group of apples"
```

### Word Order

Vilantic uses SVO word order:

```text
aźa     ćéźéma  ringoźi
1SG.NOM eat.PRS apple.SG.ACC
"I eat an apple"
```

Genitives and adjectives/adverbs come before the main noun/verb:

```text
iźu     ringoźa
1SG.GEN apple.SG.NOM
"my apple"
```

```text
jami      ringoźa
delicious apple.SG.NOM
"delicious apple"
```

### Tense and Conjugation

Vilantic has 5 tenses: Past, Near Past, Present, Near Future and Future.  
It also has 6 aspects: Perfective, Durative, Progressive, Experiential, Infinitive and Habitual.
It also has 3 moods: Ability, Possibility and Necessitative.

#### Conjugation Chart

|     | -   | POSB | ABIL | NEC |
|-----|-----|------|------|-----|
| PST | ra  | re   | ru   | rø  |
| NP  | ja  | je   | ju   | jø  |
| PRS | ma  | me   | mu   | mø  |
| IMM | pa  | pe   | pu   | pø  |
| FUT | za  | ze   | zu   | zø  |

Verbs can be negated by adding -n:

```text
aźa     ćéźéma    ringoźi
1SG.NOM eat.PRS apple.SG.ACC
"I eat an apple"
```

```text
aźa     ćéźéman       ringoźi
1SG.NOM eat.PRS.NEG apple.SG.ACC
"I am not eating an apple"
```

#### Aspects Chart

| PFV | DUR | PROG | EXP | INF | HAB |
|-----|-----|------|-----|-----|-----|
| lé  | źé  | ze   | go  | tu  | ju  |

Aspects can be added as particles before the verb:

```text
aźa     go  ćéźéma    ringoźi
1SG.NOM EXP eat.PRS apple.SG.ACC
"I have eaten apples before"
```

### Suffixes

#### Commands

The particle "da" is used before verbs to make it a command.

```text
da  ćéźéma    ringoźi
IMP eat.PRS apple.SG.ACC
"eat the apple"
```

### Evaluative Suffixes

Use "ha" for dimunitives and "vu" for augmentatives.

```text
wokéźavu       i   nysiźøha
cat.SG.NOM.AUG and mouse.SG.COM.DIM
"big cat and small mouse"
```

### Deriviational Suffixes

#### Nominalisers

| NMLZ | AGENT | INSTR | ABSTR | ABESS |
|------|-------|-------|-------|-------|
| ca   | cin   | cun   | ce    | cø    |

#### Verbalisers

| VBLZ | CAUS | INCH |
|------|------|------|
| ka   | ki   | ko   |

#### Adjectivisers and Adverbialisers

| ADJZ | PRIV | ADVZ |
|------|------|------|
| ńé   | ńan  | gø   |

### Questions

Vilantic forms questions by adding "śén" to the thing you want to find out:

```text
rasonśén
reason.WH
"why"
```

```text
iźa     ćéźéma    tingiźiśén
2SG.NOM eat.PRS thing.SG.ACC.WH
"what are you eating"
```

#### Yes/No Questions

For yes/no questions, add **-ba** to the verb:

```text
iźa     ćéźémaba      ringoźi
2SG.NOM eat.PRS.YNQ apple.SG.ACC
"do you eat apples?"
```

### Linking Words

To link words, Vilantic uses "x" + the last vowel of the previous word:

```text
libéxéźaliźa
libé-xé-źali -źa
book-LM-house-SG.NOM
"library"
```

### Expletives and Derogatory Suffixes

Vilantic has one suffix, "cen", to use as an expletive or pejorative:

```text
a cen
EXCLAM EXPL
"oh no"
```

```text
uźacen
3SG.NOM.PEJ
"that damn person"
```

### Numbers

Vilantic uses a seximal (base-6) number system. Here are the basic numerals:

**Basic Numerals (0-5):**

* 0: zero
* 1: hene
* 2: kera
* 3: sané
* 4: kanto
* 5: funfé

**Higher Numbers:**

* 6 (10₆): zesé
* 7 (11₆): vené
* 8 (12₆): ake
* 9 (13₆): nyné
* 10 (14₆): cené
* 11 (15₆): lefé
* 12 (20₆): keraløfo (2×6)

**Forming Larger Numbers:**

For multiples of 6, add the suffix "-lof":

* 12 (20₆): keraløfo (2×6)
* 18 (30₆): sanéløfo (3×6)
* 24 (40₆): kantoløfo (4×6)
* 30 (50₆): funféløfo (5×6)
* 36 (100₆): zeséløfo (6×6)

For numbers between multiples of 6, combine the multiple with the additional units:

* 20 (32₆): sanéløfo-ni (3×6 + 2)
* 25 (41₆): kantoløfo-en (4×6 + 1)

Here are the suffixes for bigger numbers:

* -løfo (6¹)
* -heli (6²)
* -reni (6³)
* -døla (6⁴)
* -vepe (6⁵)
* -bøne (6⁶)
* -gaći (6⁷)
* -źuru (6⁸)
* -were (6⁹)
* -śynbun (6¹⁰)

Example:

* 4025₆ = 881₁₀ = kantodøla-keraløfo-funfé

**Negative Numbers:**

Negative numbers are formed with the prefix "kén-":

* -3: kénsané
* -10: kéncené

**Decimal Numbers:**

Decimals are expressed by saying each digit after the word "piki" (meaning "dot"):

* 1.234: hene piki kera-sané-kanto

### Locative Case

Vilantic has particles you can use before nouns with the locative case to use as prepositions:

```text
śan libéźo
on  book.SG.LOC
"on the book"
```

#### Prepositions

| Word   | Meaning         |
|--------|-----------------|
| śan    | on              |
| awen   | away from (ABL) |

[reference (esperanto :\[)](https://en.wikiversity.org/wiki/Esperanto/Root_chart)

### Proper Nouns

Proper nouns are usually made by compounding words that describe the person/place:

```text
śéncińéxésolaxakøkéźa
śénci-ńé-xé-sola-xa-køké-źa
rise.ADJZ.LM.sun.LM.country.SG.NOM
"Japan (lit. country of the rising sun)"
```

### Sentence coordinators

#### "and"

| COORD | ADD | SEQ | SIM | COMP |
|-------|-----|-----|-----|------|
| i     | pu  | nø  | sin | ka   |

#### Other Conjunctions

| Word    | Meaning         |
|---------|-----------------|
| la...du | if...then       |

add more conjuctions here later

## Example Translations

translate the sentence at the beginning too

[other clong](https://sq.is-a.dev/conlangs/toporic)

## Lexicon (TEMP)

```text
aka    cup
aké    know
apo    help
beka   common
bili   become
bići   shore
dagé   day
daje   bring
daman  serve
danén  to curse
døré   animal
elø    to greet
even   ceramic
gakan  to ingest
guśé   story
hanśo  hand, arm
hono   fire
huła   basic
høré   hear
jami   delicious
janran person
keme   turtle
kené   joint
kepen  use
kindé  child
køké   country
langé  language
laćo   to schematise, to make a transit diagram
latø   old
lawa   fish
lego   brick
libé   book
lita   pretentious
lyte   pull
mado   window
mama   mother
meteré meter (loan)
mezi   grain, maize
mono   only
nysi   mouse, rodent
paso   learn
pili   beg
pini   finish
rason  reason
reźo   uranium
rijé   river, stream
ringo  apple
saba   curse
sanwi  cold
sehe   see
siba   self
sini   ski
sipi   game
sola   sun
suwi   water
sødu   south
tada   celebrate
tele   phone
tewin  drink
tingi  thing
viran  Vilantic
wacé   sock
wapa   hot
wara   get
weto   land
woké   cat, feline
zagi   rice
ćéźé   to eat
łaxa   (of something inedible) to ingest accidentally
łesa   appear
łese   to present
łéla   gemstone
śije   blood
śinu   to sleep
śénci  rise
źali   house
źonzé  seed
```

this clong is very incomplete
