# Viszic

## Preface

## Background

## Phonology

### Consonants

|             | Labial | Coronal | Palatal      | Dorsal      |
|-------------|--------|---------|--------------|-------------|
| Nasal       | m      | n       | ɲ \<ny>      | ŋ \<ng>     |
| Stop        | p b    | t d     | c ɟ \<ty gy> | k g         |
| Fricative   | f v    | s z     | ɕ ʑ \<sz zs> | x ɣ \<ch r> |
| Affricate   |        | ts \<c> | tɕ \<cz>     |             |
| Approximant | w      | l       | ç j \<h/x y> |             |

* [ç] is written as ⟨x⟩ syllable-finally and ⟨h⟩ anywhere else.
* [ɣ] may be realised as [ʁ].

### Vowels

|       | Front   | Back |
|-------|---------|------|
| Close | i       | u    |
| Mid   | e       | o    |
| Open  | æ \<ea> | a    |

* All vowels except [æ] can be lengthened, which is written as ⟨◌́⟩.

### Diphthongs

|   | a  | i  | u  | e  | o  |
|---|----|----|----|----|----|
| a |    | ia | ua |    |    |
| i | ai |    | ui | ei | oi |
| u | au | iu |    | eu | ou |
| e |    | ie | ue |    |    |
| o |    | io | uo |    |    |

* Diphthongs cannot be lengthened.
* Long vowels and diphthongs count as 2 morae, while normal vowels count as 1.

### Phonotactics and Orthography

(C₁)V₁(V₂)(C₂) where:

* C₁ can be any consonant except [ŋ]
* V₁ can be any vowel
* V₂ can be the second vowel of an allowed diphthong
* C₂ can be any consonant except [w j ɲ c ɟ x ɣ]
* Syllables can be split with ⟨'⟩ if necessary, e.g. ⟨ac'ha⟩ [ats.ça] and ⟨acha⟩ [axa]
* CVCV structures are automatically assumed to be [CV.CV].
* ⟨CVC'V⟩ or can be used to explicitly state a [CVC.V] pattern.

## Grammar

### Structure

Morphemes are typically 2 morae long. Proper nouns may have some vowels lengthened or shortened to have an even number of morae.

### Cases And Number

Viszic has 8 cases: Nominative, Accusative, Genitive, Dative, Locative, Vocative, Comitative and Instrumental; as well as 5 numbers: Singular, Dual, Paucal, Plural (used for plural or collective) and Umbral (used for an unknown number or for none at all), which are stacked onto the noun as suffixes.

|     | NOM | ACC  | GEN | DAT | LOC  | VOC | COM | INSTR |
|-----|-----|------|-----|-----|------|-----|-----|-------|
| SG  | -rá | -sá  | -wá | -pá | -ná  | -ó  | -má | -bá   |
| DU  | -gí | -szí | -ví | -pí | -nyé | -ó  | -ní | -bí   |
| PAU | -rú | -sú  | -yú | -fú | -nú  | -ó  | -mó | -bó   |
| PL  | -ré | -sé  | -vé | -pé | -mé  | -ó  | -gé | -dé   |
| UMB | -ró | -só  | -yó | -pó | -nó  | -ó  | -gá | -dá   |

```text
viwará ít pinagí ít aretré
viwa -rá     ít    pina  -gí     ít    aret -ré
apple-NOM.SG COORD cherry-NOM.DU COORD grape-NOM.PL
"the apple, the cherries and the grapes"
```

### Pronouns

Pronouns are formed by attaching one of the person prefixes with the case and number suffix.

| 0 | 1 | 2 | 2.FOR | 3 |
|---|---|---|-------|---|
| á | í | é | ú     | ó |

```text
írá tulaneu tyég
í-rá     tula-neu     tyégsé
1-NOM.SG love-PRS.NEG egg-ACC.PL
"I don't like eggs"
```

```text
árá szecholmáneu nesibirug gayusé
á-rá     szechol   -má    -neu nesi        -birug gayu      -sé
0-NOM.SG protection-COM.SG-NEG PRS.NEC.NEG -use   pufferfish-ACC.PL
"one without protection should not handle pufferfish"
```

### Word Order

Viszic uses word SVO word order.

```text
érá marax donyasá zsetalná
é-rá     marax     donya-sá     zsetal-ná
2-NOM.SG take-PRS  item -ACC.SG table -LOC.SG
"you take the item on the table"
```

Genitives and descriptors (adjectives/adverbs) come before the main noun/verb.

```text
ówá miará pefret haxan
ó-wá     mia-rá     pefret haxan
3-GEN.SG cat-NOM.SG fast   sprint-PRS
"his cat runs quickly"
```

### Tense and Conjugation

Viszic has 5 tenses: Past, Near Past, Present, Near Future and Future.  
It also has 6 aspects: Perfective, Durative, Progressive, Experiential, Infinitive and Habitual.
It also has 3 moods: Ability, Possibility and Necessitative.
Non-negated forms are on the left, negated forms are on the right.

|     | -             | POSB         | ABIL           | NEC           |
|-----|---------------|--------------|----------------|---------------|
| PST | -sai -mai     | -ranya -tász | -luzse -asze   | -measze       |
| NP  | -zsablo -anye | -yelo -yela  | -lanzse -anzse | -alya -talya  |
| PRS | - -neu        | -meu -moi    | -nyeu -nyoi    | -nasi -nesi   |
| IMM | -pán -bán     | -tán -dán    | -czán -zsán    | -kán -gyán    |
| FUT | -reu -tiel    | -miel -riel  | -ciel -biel    | -zoig -lugesz |

## Lexicon

| Viszic  | Class      | Translation |
|---------|------------|-------------|
| amasz   | verb       | to eat      |
| tula    | verb       | to love     |
| birug   | verb       | to use      |
| marax   | verb       | to take     |
| haxan   | verb       | to sprint   |
| pefret  | descriptor | fast        |
| tyég    | noun       | egg         |
| donya   | noun       | item        |
| gayu    | noun       | pufferfish  |
| viwa    | noun       | apple       |
| pina    | noun       | cherry      |
| aret    | noun       | grape       |
| szechol | noun       | protection  |
| zsetal  | noun       | table       |
| meadif  | noun       | chair       |
| mia     | noun       | cat         |
