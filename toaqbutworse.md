# Acorn

## Table of Contents

## Phonology

### Consonants

|           | Labial    | Alveolar  | Dorsal    |
|-----------|-----------|-----------|-----------|
| Nasal     | m ⟨m⟩     | n ⟨n⟩     |           |
| Plosive   | p b ⟨p b⟩ | t d ⟨t d⟩ | k g ⟨k g⟩ |
| Fricative | v ⟨v⟩     | s ⟨s⟩     | h ⟨h⟩     |
| Sonorant  |           | l r ⟨l r⟩ | j ⟨j⟩     |

### Vowels

|       | Front     |
|-------|-----------|
| Close | i y ⟨i y⟩ |
| Mid   | e ⟨e⟩     |
| Open  | a ⟨a⟩     |

### Allophony

* [s] becomes [ɕ] before [i y j]
* [k] becomes [c] before [i y j]
* [g] becomes [ɟ] before [i y j]
* [h] becomes [ç] before [i y j]
* [n] becomes [ɲ] before [i y j]
* [l] becomes [ʎ] before [i y j]
* [t] becomes [tɕ] before [i y j]
* [d] becomes [dʑ] before [i y j]
* [s] becomes [z] after [b d g]
* [ng] and [nk] become [ŋ] and [ŋk]
* [b d g v] become [p t k f] word-finally
* [ay] and [ey] become [au] and [eu]
* [i] can be dropped after any palatalised consonant word-finally

### Phonotactics

* **Syllable structure:** (C)V(C)
* **Onset:** any consonant
* **Nucleus:** any vowel
* **Coda:** any consonant except [j]

* [i y] cannot occur after [j]
* 2 identical consonants may not occur in hiatus

## Script

## Syntax

### Declaring Variables

```text
lari  ti may te ryn   lari  gil    mai   ta
larry := cat (  name: larry color: white )
```

Where:

* `lari` is the variable name
* `ti` defines the variable to something
* `may` is a cat
* `te` opens the attributes section
* `ryn lari` adds a value `lari` "Larry" to attribute `ryn` "name"
* `gil mai` adds a value `mai` "white" to attribute `gil` "color"
* `ta` closes the attributes section

As many attributes can be added as long as it has an even number and follows the pattern `[property] [value]`.

Values or attributes with more than 2 words should be enclosed with `ri` and `ra`.

```text
ena      ti jan    te ryn   ri ea natsir ra ta
ea-nasir := person (  name: "  ea-nasir  "  )
```

### Calling Variables

```text
ip     la       lari
sleep( variable larry )
```

which calls the variable `lari` which was previously defined as Larry the white cat.

### Time and Tense

The current time is expressed in gloss as τₑ and the time in which the event occured as τ. Similarly, the world is defined as wₑ and the world in which the events occur in as w. τ is compared using the symbols < ≤ = ≥ > while w is compared using the symbols = ≠.

```text
va say ve
wₑ =   w
"in this world"
```

```text
va sey ve
wₑ ≠   w
"not in this world"
```

```text
da sa/si/se/sy de
τₑ </≤/≥/> τ
"in the past/in the past or present/in the future or present/in the future"
```

### Existence

```text
la  pelemva sat va sey ve da say de 
var pelemva ⊆   wₑ ≠   w  τₑ =   τ
"pelemva does not exist in this world at the moment"
```
