norm_stop False

SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zwei | anlagen | so | nah | bei@@ | einander | : | absicht | oder | schil@@ | d@@ | bürger@@ | st@@ | reich | ?|
| waitk tgt |  |  | two | plants | so | close | to | each | other | : | intention | or | tur@@ | tle | ? | </s>|
| waitk prob |  |  | 0.63 | 0.58 | 0.30 | 0.87 | 0.53 | 0.68 | 0.92 | 0.85 | 0.42 | 0.80 | 0.51 | 0.75 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.93 | 0.41 | 0.09 | 0.80 | 0.16 | 0.64 | 0.89 | 0.61 | 0.33 | 0.83 | 0.06 | 0.61 | 0.55 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.06 | -3.24 | -3.19 | -1.55 | -1.51 | -2.05 | -1.65 | -2.50 | -3.33 | -1.90 | -4.97 | -1.87 | -2.78 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.95 | -2.54 | -3.27 | -1.32 | -2.64 | -1.22 | -1.35 | -1.71 | -3.19 | -1.97 | -2.69 | -1.45 | -1.32 | -1.73|
| full sent prob |  |  | 0.62 | 0.25 | 0.72 | 0.64 | 0.21 | 0.64 | 0.87 | 0.86 | 0.58 | 0.88 | 0.04 | 0.66 | 0.62 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.00 | -3.74 | -1.91 | -2.02 | -1.58 | -1.79 | -1.83 | -1.74 | -2.42 | -1.69 | -4.59 | -1.59 | -3.12 | -1.61|
| full sent KL (full->waitk) |  |  | -2.79 | -2.46 | -3.42 | -1.21 | -2.65 | -1.23 | -1.34 | -1.89 | -3.27 | -2.00 | -2.69 | -1.48 | -1.37 | -1.72|
| dec-waitktgt |  |  | two | plants | </s> | close | together | each | other | : | intention | or | the | tle | ? | </s>|
| full sent tgt |  |  | two | plants | so | close | together | each | other | : | intention | or | tor@@ | tle | ? | </s>|
| ref | two | sets | of | lights | so | close | to | one | another | : | inten@@ | tional | or | just | a | sil@@ | ly | error | ? | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | diese | frage | hat | gu@@ | ta@@ | chs | bürger@@ | meister | gestern | klar | beantwortet | .|
| waitk tgt |  |  | this | question | has | been | addressed | by | the | may@@ | or | of | the | city | yesterday | . | </s>|
| waitk prob |  |  | 0.45 | 0.44 | 0.67 | 0.74 | 0.12 | 0.78 | 0.27 | 0.31 | 0.88 | 0.74 | 0.17 | 0.27 | 0.45 | 0.85 | 0.91|
| dec-waitk prob |  |  | 0.56 | 0.40 | 0.64 | 0.51 | 0.02 | 0.71 | 0.07 | 0.84 | 0.81 | 0.72 | 0.01 | 0.17 | 0.00 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 77 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.00 | -2.00 | -2.62 | -3.18 | -2.43 | -1.67 | -4.43 | -1.43 | -1.95 | -2.49 | -4.12 | -4.14 | -2.36 | -1.75 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.03 | -2.40 | -2.06 | -2.09 | -3.97 | -1.92 | -3.75 | -4.63 | -1.48 | -2.14 | -4.68 | -3.80 | -2.73 | -1.90 | -1.67|
| full sent prob |  |  | 0.13 | 0.59 | 0.01 | 0.78 | 0.01 | 0.06 | 0.09 | 0.98 | 0.89 | 0.75 | 0.02 | 0.13 | 0.00 | 0.71 | 0.91|
| full sent rank |  |  | 1 | 0 | 2 | 0 | 6 | 2 | 2 | 0 | 0 | 0 | 1 | 1 | 28 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.31 | -1.93 | -0.95 | -2.20 | -2.55 | -2.42 | -4.33 | -0.44 | -1.48 | -2.09 | -4.37 | -4.07 | -2.19 | -2.35 | -1.60|
| full sent KL (full->waitk) |  |  | -2.85 | -2.44 | -1.80 | -2.25 | -3.93 | -1.50 | -3.75 | -4.66 | -1.54 | -2.16 | -4.67 | -3.79 | -2.74 | -1.78 | -1.67|
| dec-waitktgt |  |  | this | question | has | been | put | by | gu@@ | may@@ | or | of | gu@@ | city | of | . | </s>|
| full sent tgt |  |  | yesterday | question | was | been | answered | clearly | mr | may@@ | or | of | gu@@ | gu@@ | of | . | </s>|
| ref | yesterday | , | gu@@ | t@@ | ach@@ | t | &apos;s | may@@ | or | gave | a | clear | answer | to | this | question | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | klu@@ | ser@@ | -@@ | amp@@ | el | sichere | sowohl | rad@@ | fahrer | als | auch | bus@@ | fahr@@ | gäste | und | die | berg@@ | le-@@ | bewohner | .|
| waitk tgt |  |  | the | k@@ | lu@@ | ser@@ | -@@ | traffic | light | both | safe | cy@@ | cli@@ | sts | and | bus | passengers | and | the | mountain | inhabitants | . | </s>|
| waitk prob |  |  | 0.38 | 0.95 | 0.55 | 0.49 | 0.70 | 0.07 | 0.64 | 0.12 | 0.13 | 0.33 | 0.95 | 0.97 | 0.86 | 0.67 | 0.61 | 0.77 | 0.47 | 0.58 | 0.31 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.61 | 0.86 | 0.56 | 0.08 | 0.89 | 0.42 | 0.64 | 0.03 | 0.08 | 0.57 | 0.95 | 0.93 | 0.90 | 0.88 | 0.69 | 0.32 | 0.19 | 0.34 | 0.33 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.37 | -1.92 | -1.73 | -1.90 | -1.56 | -3.50 | -1.59 | -1.39 | -3.42 | -2.60 | -1.14 | -1.45 | -1.56 | -1.16 | -1.96 | -3.17 | -2.40 | -3.60 | -2.59 | -1.77 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.78 | -1.15 | -1.76 | -2.31 | -2.46 | -6.14 | -1.59 | -4.36 | -4.37 | -2.49 | -1.13 | -1.03 | -1.85 | -2.40 | -1.98 | -1.71 | -3.21 | -2.32 | -2.67 | -1.76 | -1.62|
| full sent prob |  |  | 0.54 | 0.88 | 0.74 | 0.53 | 0.92 | 0.69 | 0.45 | 0.01 | 0.05 | 0.57 | 0.99 | 0.95 | 0.42 | 0.81 | 0.69 | 0.80 | 0.45 | 0.48 | 0.40 | 0.90 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.86 | -1.73 | -1.55 | -1.86 | -1.33 | -2.00 | -2.48 | -2.13 | -2.54 | -2.46 | -0.88 | -1.26 | -2.33 | -1.27 | -2.21 | -1.93 | -2.75 | -2.89 | -2.33 | -1.71 | -1.55|
| full sent KL (full->waitk) |  |  | -3.75 | -1.16 | -1.80 | -2.39 | -2.48 | -6.15 | -1.50 | -4.35 | -4.37 | -2.49 | -1.16 | -1.05 | -1.51 | -2.36 | -1.98 | -2.01 | -3.27 | -2.39 | -2.70 | -1.76 | -1.62|
| dec-waitktgt |  |  | the | k@@ | lu@@ | ser | -@@ | traffic | light | sa@@ | sa@@ | cy@@ | cli@@ | sts | and | bus | passengers | . | mountain | mountain | inhabitants | . | </s>|
| full sent tgt |  |  | the | k@@ | lu@@ | ser@@ | -@@ | traffic | light | sa@@ | sa@@ | cy@@ | cli@@ | sts | and | bus | passengers | and | the | mountain | inhabitants | . | </s>|
| ref | the | kl@@ | user | lights | protect | cy@@ | cli@@ | sts | , | as | well | as | those | travelling | by | bus | and | the | residents | of | ber@@ | g@@ | le | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | gestern | offiziell | in | betrieb | genommen@@ | e | anlage | sei | wichtig | für | den | kreuz@@ | ungs@@ | bereich | sul@@ | z@@ | ba@@ | ch@@ | weg | / | kir@@ | ch@@ | straße | .|
| waitk tgt |  |  | the | official | start | of | the | plant | was | made | yesterday | important | for | the | crossing | area | of | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | / | kir@@ | ch@@ | stra@@ | ß@@ | e | . | </s>|
| waitk prob |  |  | 0.56 | 0.07 | 0.11 | 0.69 | 0.56 | 0.43 | 0.17 | 0.18 | 0.59 | 0.75 | 0.74 | 0.69 | 0.16 | 0.77 | 0.56 | 0.96 | 0.88 | 0.81 | 0.96 | 0.95 | 0.97 | 0.86 | 0.99 | 0.95 | 0.43 | 0.92 | 0.95 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.04 | 0.95 | 0.09 | 0.15 | 0.05 | 0.70 | 0.03 | 0.09 | 0.13 | 0.00 | 0.34 | 0.71 | 0.16 | 0.43 | 0.61 | 0.89 | 0.87 | 0.76 | 0.95 | 0.96 | 0.98 | 0.15 | 0.98 | 0.96 | 0.56 | 0.98 | 0.95 | 0.89 | 0.92|
| dec-waitk rank |  |  | 2 | 0 | 1 | 1 | 1 | 0 | 6 | 1 | 0 | 18 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.53 | -0.44 | -4.16 | -1.84 | -0.90 | -1.81 | -3.86 | -4.07 | -4.67 | -2.85 | -2.85 | -2.15 | -2.24 | -3.46 | -2.11 | -1.71 | -1.84 | -1.97 | -1.19 | -1.18 | -0.96 | -1.98 | -0.97 | -1.19 | -1.91 | -1.00 | -1.26 | -1.73 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.76 | -5.80 | -5.35 | -2.13 | -2.75 | -3.42 | -3.65 | -4.51 | -2.64 | -1.71 | -1.70 | -2.80 | -4.61 | -1.70 | -2.10 | -1.05 | -1.72 | -1.49 | -1.09 | -1.16 | -1.06 | -1.30 | -0.91 | -1.17 | -2.32 | -1.54 | -1.28 | -1.60 | -1.66|
| full sent prob |  |  | 0.51 | 0.00 | 0.01 | 0.44 | 0.44 | 0.50 | 0.27 | 0.02 | 0.00 | 0.54 | 0.71 | 0.85 | 0.05 | 0.64 | 0.37 | 0.88 | 0.91 | 0.84 | 0.96 | 0.97 | 0.97 | 0.87 | 0.99 | 0.95 | 0.56 | 0.96 | 0.95 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 34 | 9 | 0 | 0 | 0 | 0 | 3 | 29 | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.20 | -3.09 | -2.73 | -2.59 | -2.72 | -2.78 | -3.20 | -4.15 | -4.30 | -2.65 | -2.06 | -1.74 | -4.63 | -2.68 | -2.34 | -1.69 | -1.54 | -1.59 | -1.12 | -1.06 | -1.07 | -1.60 | -0.95 | -1.21 | -1.85 | -1.15 | -1.28 | -1.71 | -1.58|
| full sent KL (full->waitk) |  |  | -2.98 | -5.75 | -5.34 | -2.30 | -2.87 | -3.36 | -3.68 | -4.50 | -2.58 | -2.04 | -1.92 | -2.88 | -4.56 | -1.83 | -2.08 | -1.05 | -1.75 | -1.54 | -1.10 | -1.17 | -1.05 | -1.81 | -0.91 | -1.17 | -2.32 | -1.53 | -1.28 | -1.60 | -1.65|
| dec-waitktgt |  |  | officially | official | opening | yesterday | yesterday | plant | , | yesterday | yesterday | . | for | the | cros@@ | area | of | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | . | kir@@ | ch@@ | stra@@ | ß@@ | e | . | </s>|
| full sent tgt |  |  | the | plant | plant | of | the | plant | was | important | important | important | for | the | sul@@ | area | sul@@ | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | / | kir@@ | ch@@ | stra@@ | ß@@ | e | . | </s>|
| ref | the | system | , | which | officially | became | operational | yesterday | , | is | of | importance | to | the | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | / | kir@@ | ch@@ | stras@@ | se | junction | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dies | bestätigt | auch | peter | ar@@ | n@@ | old | vom | land@@ | rat@@ | sam@@ | t | offen@@ | burg | .|
| waitk tgt |  |  | this | is | confirmed | by | peter | ar@@ | no@@ | ld | of | the | council | of | land@@ | rat@@ | r@@ | at | off@@ | enburg | . | </s>|
| waitk prob |  |  | 0.59 | 0.44 | 0.42 | 0.65 | 0.74 | 0.92 | 0.98 | 0.95 | 0.36 | 0.85 | 0.20 | 0.41 | 0.22 | 0.84 | 0.21 | 0.75 | 0.89 | 0.92 | 0.83 | 0.90|
| dec-waitk prob |  |  | 0.63 | 0.49 | 0.19 | 0.56 | 0.57 | 0.95 | 0.99 | 0.77 | 0.25 | 0.89 | 0.16 | 0.62 | 0.00 | 0.65 | 0.00 | 0.55 | 0.54 | 0.97 | 0.86 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 21 | 0 | 266 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.05 | -2.33 | -2.40 | -2.71 | -2.48 | -1.23 | -0.89 | -1.95 | -3.05 | -1.74 | -3.61 | -2.38 | -0.63 | -1.61 | -4.53 | -2.89 | -2.72 | -0.96 | -1.84 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.66 | -2.76 | -2.14 | -2.28 | -2.16 | -1.47 | -1.01 | -1.03 | -2.64 | -2.00 | -3.85 | -2.70 | -3.55 | -1.51 | -3.20 | -1.55 | -1.40 | -1.43 | -1.98 | -1.68|
| full sent prob |  |  | 0.28 | 0.50 | 0.45 | 0.81 | 0.91 | 0.92 | 0.98 | 0.97 | 0.41 | 0.68 | 0.05 | 0.74 | 0.00 | 0.64 | 0.00 | 0.59 | 0.73 | 0.97 | 0.84 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 5 | 0 | 244 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.09 | -2.79 | -2.28 | -1.79 | -1.31 | -1.49 | -1.03 | -1.09 | -2.81 | -2.46 | -3.95 | -2.08 | -1.09 | -1.79 | -4.91 | -2.61 | -2.15 | -0.95 | -1.90 | -1.61|
| full sent KL (full->waitk) |  |  | -2.49 | -2.78 | -2.16 | -2.40 | -2.36 | -1.44 | -1.00 | -1.19 | -2.66 | -1.85 | -3.83 | -2.74 | -3.55 | -1.50 | -3.21 | -1.58 | -1.55 | -1.43 | -1.97 | -1.67|
| dec-waitktgt |  |  | this | is | also | by | peter | ar@@ | no@@ | ld | from | the | land | of | off@@ | rat@@ | t | at | off@@ | enburg | . | </s>|
| full sent tgt |  |  | this | is | confirmed | by | peter | ar@@ | no@@ | ld | of | the | district | of | off@@ | rat@@ | sam@@ | at | off@@ | enburg | . | </s>|
| ref | this | was | also | confirmed | by | peter | ar@@ | no@@ | ld | from | the | off@@ | enburg | district | office | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | und | spar@@ | sam | ist | sie | auch | : | die | älteren | lich@@ | tan@@ | lagen | verbrau@@ | chen | etwa | 100 | wa@@ | tt | , | die | neuen | gerade | mal | acht | wa@@ | tt | .|
| waitk tgt |  |  | and | econom@@ | ical | it | is | also | : | the | older | lighting | systems | use | about | 100 | wat@@ | ts | , | the | new | ones | only | eight | wat@@ | ts | . | </s>|
| waitk prob |  |  | 0.35 | 0.12 | 0.68 | 0.20 | 0.75 | 0.35 | 0.77 | 0.49 | 0.79 | 0.34 | 0.43 | 0.34 | 0.44 | 0.86 | 0.87 | 0.89 | 0.49 | 0.46 | 0.81 | 0.41 | 0.24 | 0.73 | 0.88 | 0.87 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.80 | 0.10 | 0.16 | 0.15 | 0.76 | 0.51 | 0.62 | 0.01 | 0.48 | 0.30 | 0.36 | 0.22 | 0.22 | 0.91 | 0.23 | 0.79 | 0.09 | 0.04 | 0.22 | 0.20 | 0.04 | 0.75 | 0.33 | 0.75 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.95 | -1.86 | -4.80 | -4.52 | -2.12 | -3.18 | -2.82 | -0.97 | -3.49 | -3.58 | -3.14 | -2.52 | -3.36 | -1.46 | -4.27 | -1.50 | -1.62 | -4.46 | -4.35 | -4.07 | -4.38 | -1.87 | -3.36 | -1.59 | -1.71 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.32 | -4.24 | -2.38 | -3.99 | -2.21 | -3.77 | -2.20 | -2.32 | -1.76 | -2.66 | -3.13 | -2.86 | -2.49 | -1.73 | -1.08 | -1.20 | -2.70 | -2.88 | -1.82 | -3.65 | -3.44 | -2.25 | -1.06 | -1.26 | -1.77 | -1.63|
| full sent prob |  |  | 0.40 | 0.00 | 0.78 | 0.15 | 0.70 | 0.44 | 0.86 | 0.55 | 0.76 | 0.36 | 0.58 | 0.37 | 0.58 | 0.88 | 0.94 | 0.83 | 0.65 | 0.72 | 0.80 | 0.06 | 0.06 | 0.82 | 0.92 | 0.87 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 15 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.60 | -2.82 | -1.99 | -3.36 | -2.35 | -2.85 | -1.69 | -2.58 | -2.08 | -2.77 | -2.57 | -2.49 | -1.87 | -1.58 | -1.14 | -1.39 | -2.25 | -2.06 | -2.14 | -3.05 | -3.97 | -1.59 | -1.33 | -1.34 | -1.71 | -1.59|
| full sent KL (full->waitk) |  |  | -4.20 | -4.22 | -2.72 | -4.00 | -2.17 | -3.76 | -2.35 | -2.58 | -1.94 | -2.69 | -3.20 | -2.88 | -2.64 | -1.71 | -1.60 | -1.23 | -2.93 | -3.10 | -2.21 | -3.60 | -3.45 | -2.29 | -1.48 | -1.35 | -1.76 | -1.62|
| dec-waitktgt |  |  | and | au@@ | ical | it | is | also | : | </s> | older | lighting | systems | con@@ | for | 100 | wat@@ | ts | . | which | new | ones | just | eight | wat@@ | ts | . | </s>|
| full sent tgt |  |  | and | it | ical | , | is | also | : | the | older | lighting | systems | use | about | 100 | wat@@ | ts | , | the | new | one | just | eight | wat@@ | ts | . | </s>|
| ref | and | they | are | also | ener@@ | g@@ | y-@@ | efficient | : | the | older | light | systems | con@@ | sume | around | 100 | wat@@ | ts | , | with | the | new | ones | consum@@ | ing | just | eight | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ar@@ | n@@ | old | erklärte | die | technik | der | neuen | anlage | : | diese | ist | mit | zwei | ra@@ | dar@@ | sen@@ | sor@@ | en | ausgestattet | .|
| waitk tgt |  |  | ar@@ | no@@ | ld | explained | the | technique | of | the | new | plant | : | it | is | equipped | with | two | rad@@ | ar | sen@@ | sors | . | </s>|
| waitk prob |  |  | 0.61 | 0.99 | 0.91 | 0.64 | 0.74 | 0.63 | 0.85 | 0.83 | 0.89 | 0.34 | 0.87 | 0.42 | 0.55 | 0.74 | 0.90 | 0.90 | 0.94 | 0.73 | 0.95 | 0.97 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.64 | 0.99 | 0.97 | 0.55 | 0.71 | 0.64 | 0.86 | 0.62 | 0.88 | 0.40 | 0.71 | 0.03 | 0.65 | 0.24 | 0.88 | 0.93 | 0.85 | 0.88 | 0.86 | 0.96 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.90 | -0.96 | -1.03 | -2.58 | -2.67 | -1.60 | -1.80 | -2.75 | -1.84 | -2.67 | -2.78 | -3.76 | -2.44 | -3.93 | -1.80 | -1.29 | -1.84 | -1.38 | -1.63 | -1.21 | -1.73 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.10 | -0.94 | -1.47 | -2.32 | -2.40 | -1.87 | -1.91 | -1.79 | -1.63 | -3.10 | -1.59 | -2.79 | -2.80 | -1.76 | -1.61 | -1.50 | -1.20 | -2.14 | -1.08 | -1.04 | -1.69 | -1.67|
| full sent prob |  |  | 0.70 | 0.98 | 0.96 | 0.87 | 0.80 | 0.36 | 0.83 | 0.79 | 0.89 | 0.15 | 0.83 | 0.22 | 0.62 | 0.92 | 0.89 | 0.93 | 0.88 | 0.89 | 0.86 | 0.96 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.49 | -0.99 | -1.11 | -1.40 | -2.00 | -2.39 | -1.92 | -2.07 | -1.70 | -3.42 | -2.02 | -2.43 | -2.24 | -1.09 | -1.72 | -1.29 | -1.71 | -1.31 | -1.54 | -1.15 | -1.76 | -1.61|
| full sent KL (full->waitk) |  |  | -3.13 | -0.94 | -1.46 | -2.48 | -2.46 | -1.74 | -1.89 | -1.91 | -1.64 | -3.04 | -1.67 | -2.93 | -2.79 | -2.18 | -1.62 | -1.50 | -1.22 | -2.15 | -1.09 | -1.05 | -1.68 | -1.67|
| dec-waitktgt |  |  | ar@@ | no@@ | ld | explained | the | technique | of | the | new | plant | : | </s> | is | equipped | with | two | rad@@ | ar | sen@@ | sors | . | </s>|
| full sent tgt |  |  | ar@@ | no@@ | ld | explained | the | technique | of | the | new | system | : | this | is | equipped | with | two | rad@@ | ar | sen@@ | sors | . | </s>|
| ref | ar@@ | no@@ | ld | explained | the | technology | used | by | the | new | system | : | it | is | fitted | with | two | rad@@ | ar | sen@@ | sors | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | drückt | der | fuß@@ | gän@@ | ger | den | amp@@ | el@@ | kno@@ | pf | , | te@@ | stet | der | ober@@ | e | ra@@ | dar@@ | sen@@ | sor | die | verkehrs@@ | lage | .|
| waitk tgt |  |  | press | the | pede@@ | strian | to | turn | the | light | button | , | the | driver | will | test | the | upper | rad@@ | ar | sensor | to | determine | the | traffic | situation | . | </s>|
| waitk prob |  |  | 0.34 | 0.72 | 0.46 | 0.74 | 0.24 | 0.10 | 0.58 | 0.28 | 0.77 | 0.69 | 0.21 | 0.09 | 0.20 | 0.73 | 0.78 | 0.30 | 0.70 | 0.87 | 0.86 | 0.18 | 0.28 | 0.64 | 0.68 | 0.49 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.01 | 0.49 | 0.80 | 0.79 | 0.00 | 0.00 | 0.17 | 0.04 | 0.71 | 0.72 | 0.01 | 0.03 | 0.20 | 0.50 | 0.56 | 0.12 | 0.82 | 0.94 | 0.95 | 0.00 | 0.06 | 0.68 | 0.30 | 0.62 | 0.88 | 0.92|
| dec-waitk rank |  |  | 11 | 0 | 0 | 0 | 44 | 32 | 1 | 2 | 0 | 0 | 12 | 3 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.94 | -2.27 | -1.80 | -1.25 | -4.74 | -4.33 | -3.91 | -2.31 | -2.10 | -2.25 | -4.21 | -5.52 | -3.54 | -3.34 | -2.33 | -3.37 | -1.89 | -1.18 | -1.06 | -2.26 | -5.06 | -2.40 | -4.04 | -2.09 | -1.81 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.82 | -2.31 | -3.94 | -2.41 | -4.29 | -4.23 | -2.35 | -3.57 | -2.29 | -2.48 | -3.84 | -5.14 | -4.11 | -2.07 | -2.00 | -4.38 | -2.64 | -1.48 | -1.73 | -3.84 | -3.57 | -2.34 | -2.23 | -2.27 | -1.64 | -1.65|
| full sent prob |  |  | 0.02 | 0.84 | 0.00 | 0.89 | 0.00 | 0.00 | 0.61 | 0.13 | 0.88 | 0.38 | 0.80 | 0.00 | 0.25 | 0.73 | 0.83 | 0.00 | 0.88 | 0.91 | 0.95 | 0.04 | 0.18 | 0.73 | 0.63 | 0.66 | 0.89 | 0.91|
| full sent rank |  |  | 5 | 0 | 56 | 0 | 41 | 44 | 0 | 1 | 0 | 0 | 0 | 50 | 1 | 0 | 0 | 154 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.43 | -1.89 | -2.53 | -1.28 | -2.97 | -4.36 | -2.78 | -2.70 | -1.41 | -2.41 | -1.66 | -1.99 | -2.70 | -2.20 | -1.82 | -1.75 | -1.44 | -1.36 | -1.06 | -3.27 | -4.38 | -2.12 | -2.72 | -2.09 | -1.74 | -1.60|
| full sent KL (full->waitk) |  |  | -3.82 | -2.52 | -3.64 | -2.47 | -4.32 | -4.24 | -2.56 | -3.56 | -2.40 | -2.31 | -3.96 | -5.13 | -4.13 | -2.21 | -2.18 | -4.34 | -2.67 | -1.46 | -1.73 | -3.85 | -3.60 | -2.37 | -2.42 | -2.28 | -1.65 | -1.65|
| dec-waitktgt |  |  | pus@@ | the | pede@@ | strian | path | press | </s> | traffic | button | , | </s> | pro@@ | tests | test | the | rad@@ | rad@@ | ar | sensor | . | determine | the | traffic | situation | . | </s>|
| full sent tgt |  |  | if | the | traffic | strian | button | set | the | traffic | button | , | the | upper | tests | test | the | traffic | rad@@ | ar | sensor | . | determine | the | traffic | situation | . | </s>|
| ref | if | the | pede@@ | strian | pres@@ | ses | the | button | at | the | traffic | lights | , | the | top | rad@@ | ar | sensor | checks | the | traffic | status | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ein | weiteres | ra@@ | dar@@ | sen@@ | sor | prüft | , | ob | die | grün@@ | phase | für | den | fuß@@ | gän@@ | ger | beendet | werden | kann | .|
| waitk tgt |  |  | another | rad@@ | ar | sensor | checks | whether | the | rad@@ | ar | phase | is | correct | for | the | pede@@ | strian | . | </s>|
| waitk prob |  |  | 0.55 | 0.91 | 0.91 | 0.93 | 0.43 | 0.33 | 0.46 | 0.04 | 0.89 | 0.79 | 0.47 | 0.10 | 0.77 | 0.53 | 0.89 | 0.65 | 0.56 | 0.91|
| dec-waitk prob |  |  | 0.73 | 0.97 | 0.88 | 0.98 | 0.01 | 0.00 | 0.16 | 0.61 | 0.94 | 0.06 | 0.46 | 0.00 | 0.08 | 0.21 | 0.50 | 0.77 | 0.64 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 2 | 18 | 0 | 0 | 0 | 1 | 0 | 61 | 1 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.06 | -1.01 | -1.46 | -0.96 | -2.65 | -3.79 | -4.25 | -2.61 | -1.06 | -5.22 | -2.82 | -4.94 | -1.89 | -1.83 | -3.83 | -1.70 | -3.02 | -1.48|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.90 | -1.55 | -1.23 | -1.28 | -3.00 | -2.54 | -3.26 | -6.08 | -1.40 | -1.43 | -2.53 | -4.31 | -1.56 | -2.16 | -1.27 | -3.10 | -2.89 | -1.67|
| full sent prob |  |  | 0.39 | 0.93 | 0.90 | 0.96 | 0.43 | 0.49 | 0.73 | 0.00 | 0.99 | 0.12 | 0.06 | 0.00 | 0.71 | 0.74 | 0.69 | 0.83 | 0.83 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 502 | 0 | 0 | 2 | 85 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.15 | -1.30 | -1.47 | -1.09 | -3.25 | -2.66 | -2.13 | -4.94 | -0.84 | -5.30 | -2.25 | -3.41 | -2.16 | -2.05 | -2.67 | -1.48 | -1.78 | -1.59|
| full sent KL (full->waitk) |  |  | -2.76 | -1.53 | -1.24 | -1.26 | -3.16 | -2.71 | -3.47 | -6.06 | -1.44 | -1.46 | -2.42 | -4.31 | -1.95 | -2.26 | -1.41 | -3.13 | -2.98 | -1.66|
| dec-waitktgt |  |  | another | rad@@ | ar | sensor | </s> | </s> | the | rad@@ | ar | sensor | is | in | . | pede@@ | pede@@ | strian | . | </s>|
| full sent tgt |  |  | another | rad@@ | ar | sensor | checks | whether | the | pede@@ | ar | phase | for | ready | for | the | pede@@ | strian | . | </s>|
| ref | an | additional | rad@@ | ar | sensor | checks | whether | the | green | phase | for | the | pede@@ | strian | can | be | ended | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | natürlich | mü@@ | sse | der | auto@@ | fahrer | hier | als | partner | mit@@ | denken | und | die | fahr@@ | bahn | beobachten | .|
| waitk tgt |  |  | of | course | , | drivers | must | be | a | partner | here | and | the | drivers | must | observe | the | track | . | </s>|
| waitk prob |  |  | 0.42 | 0.94 | 0.63 | 0.34 | 0.34 | 0.65 | 0.07 | 0.79 | 0.54 | 0.62 | 0.22 | 0.67 | 0.70 | 0.34 | 0.72 | 0.31 | 0.87 | 0.91|
| dec-waitk prob |  |  | 0.50 | 0.95 | 0.51 | 0.23 | 0.44 | 0.68 | 0.05 | 0.33 | 0.45 | 0.00 | 0.04 | 0.10 | 0.57 | 0.02 | 0.59 | 0.07 | 0.86 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 1 | 2 | 0 | 4 | 0 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.76 | -1.31 | -2.51 | -2.82 | -2.57 | -2.72 | -3.61 | -3.68 | -2.09 | -1.61 | -4.95 | -3.20 | -2.99 | -4.10 | -2.29 | -4.90 | -1.96 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.14 | -1.42 | -2.13 | -2.96 | -2.67 | -2.72 | -4.33 | -1.72 | -2.16 | -1.84 | -4.65 | -1.45 | -1.92 | -2.83 | -2.22 | -3.67 | -1.83 | -1.67|
| full sent prob |  |  | 0.37 | 0.93 | 0.49 | 0.23 | 0.42 | 0.12 | 0.09 | 0.53 | 0.38 | 0.70 | 0.00 | 0.00 | 0.75 | 0.46 | 0.80 | 0.11 | 0.87 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 29 | 53 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.40 | -1.46 | -2.71 | -3.21 | -2.50 | -3.61 | -4.07 | -3.22 | -2.27 | -2.10 | -2.24 | -3.84 | -1.78 | -2.87 | -2.01 | -5.01 | -1.90 | -1.56|
| full sent KL (full->waitk) |  |  | -3.09 | -1.41 | -2.11 | -2.98 | -2.67 | -2.42 | -4.34 | -1.85 | -2.12 | -2.21 | -4.64 | -1.37 | -2.03 | -2.95 | -2.33 | -3.68 | -1.83 | -1.66|
| dec-waitktgt |  |  | of | course | , | drivers | must | be | here | partner | here | . | </s> | driving | must | take | the | railways | . | </s>|
| full sent tgt |  |  | of | course | , | the | must | take | involved | partner | here | and | observe | road | must | observe | the | track | . | </s>|
| ref | of | course | , | drivers | must | also | play | their | part | and | keep | their | eyes | on | the | road | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dabei | scheint | regi@@ | ss@@ | eur | fre@@ | sa@@ | cher | dem | text | wenig | zu | vertrauen | .|
| waitk tgt |  |  | in | doing | so | , | director | fres@@ | ach@@ | er | seems | to | have | little | faith | in | the | text | . | </s>|
| waitk prob |  |  | 0.10 | 0.25 | 0.83 | 0.90 | 0.84 | 0.86 | 0.89 | 0.94 | 0.57 | 0.42 | 0.65 | 0.93 | 0.49 | 0.83 | 0.82 | 0.82 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.02 | 0.24 | 0.84 | 0.90 | 0.23 | 0.64 | 0.80 | 0.93 | 0.57 | 0.19 | 0.45 | 0.94 | 0.44 | 0.85 | 0.84 | 0.88 | 0.91 | 0.92|
| dec-waitk rank |  |  | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.84 | -2.71 | -1.49 | -1.58 | -4.25 | -2.80 | -2.03 | -1.43 | -2.41 | -2.70 | -2.56 | -1.18 | -1.49 | -1.80 | -1.86 | -1.72 | -1.61 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.48 | -3.04 | -1.52 | -1.55 | -1.18 | -1.52 | -1.37 | -1.28 | -1.92 | -2.61 | -2.21 | -1.21 | -1.35 | -1.88 | -2.00 | -2.06 | -1.70 | -1.63|
| full sent prob |  |  | 0.11 | 0.22 | 0.86 | 0.87 | 0.84 | 0.48 | 0.81 | 0.94 | 0.57 | 0.69 | 0.52 | 0.90 | 0.39 | 0.90 | 0.84 | 0.86 | 0.90 | 0.91|
| full sent rank |  |  | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.25 | -2.89 | -1.49 | -1.73 | -1.78 | -3.65 | -2.13 | -1.38 | -2.39 | -2.17 | -2.52 | -1.35 | -1.44 | -1.65 | -1.80 | -1.81 | -1.70 | -1.61|
| full sent KL (full->waitk) |  |  | -4.47 | -3.04 | -1.53 | -1.52 | -1.59 | -1.41 | -1.38 | -1.28 | -1.91 | -2.71 | -2.25 | -1.18 | -1.36 | -1.91 | -2.01 | -2.05 | -1.69 | -1.62|
| dec-waitktgt |  |  | but | this | so | , | director | fres@@ | ach@@ | er | seems | little | have | little | faith | in | the | text | . | </s>|
| full sent tgt |  |  | director | this | so | , | director | fres@@ | ach@@ | er | seems | to | have | little | confidence | in | the | text | . | </s>|
| ref | however | , | director | fres@@ | ach@@ | er | seems | to | have | little | trust | in | the | text | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | vor | allem | die | schau@@ | spiel@@ | erinnen | kommen | bei | den | mit@@ | unter | etwas | fra@@ | g@@ | würdigen | szen@@ | ischen | um@@ | setzungen | d@@ | ran | .|
| waitk tgt |  |  | the | fo@@ | cal | point | of | the | show | is | the | fact | that | the | actors | sometimes | find | themselves | in | a | rather | du@@ | bi@@ | ous | setting | . | </s>|
| waitk prob |  |  | 0.22 | 0.10 | 0.30 | 0.56 | 0.49 | 0.37 | 0.06 | 0.56 | 0.44 | 0.03 | 0.87 | 0.30 | 0.73 | 0.23 | 0.10 | 0.33 | 0.34 | 0.22 | 0.44 | 0.31 | 0.99 | 0.98 | 0.18 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.04 | 0.00 | 0.80 | 0.21 | 0.38 | 0.45 | 0.01 | 0.52 | 0.32 | 0.00 | 0.83 | 0.23 | 0.44 | 0.06 | 0.05 | 0.84 | 0.40 | 0.31 | 0.49 | 0.16 | 0.95 | 0.98 | 0.09 | 0.84 | 0.92|
| dec-waitk rank |  |  | 4 | 87 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 17 | 0 | 0 | 0 | 4 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.10 | -5.39 | -1.52 | -4.88 | -2.77 | -2.95 | -4.36 | -3.08 | -3.85 | -3.53 | -2.00 | -3.56 | -3.91 | -3.13 | -4.05 | -1.28 | -3.21 | -3.07 | -2.70 | -3.05 | -1.26 | -1.01 | -3.12 | -1.92 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.18 | -4.84 | -3.33 | -1.48 | -2.36 | -3.24 | -5.65 | -2.88 | -3.12 | -6.00 | -1.75 | -3.76 | -1.80 | -3.18 | -4.32 | -3.35 | -3.94 | -3.16 | -2.08 | -3.18 | -0.84 | -1.01 | -4.25 | -1.79 | -1.65|
| full sent prob |  |  | 0.16 | 0.00 | 0.32 | 0.33 | 0.29 | 0.27 | 0.03 | 0.59 | 0.43 | 0.00 | 0.83 | 0.23 | 0.66 | 0.06 | 0.04 | 0.54 | 0.53 | 0.18 | 0.43 | 0.15 | 0.95 | 0.97 | 0.15 | 0.82 | 0.92|
| full sent rank |  |  | 0 | 216 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 48 | 0 | 1 | 0 | 3 | 3 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.10 | -2.74 | -3.04 | -4.54 | -2.65 | -2.85 | -5.19 | -2.56 | -3.40 | -2.32 | -1.98 | -3.07 | -2.76 | -3.78 | -3.67 | -2.35 | -3.17 | -3.08 | -2.49 | -2.99 | -1.27 | -1.08 | -3.74 | -2.00 | -1.56|
| full sent KL (full->waitk) |  |  | -4.18 | -4.89 | -3.22 | -1.52 | -2.33 | -3.22 | -5.64 | -2.92 | -3.17 | -6.01 | -1.76 | -3.76 | -1.92 | -3.18 | -4.31 | -3.27 | -3.96 | -3.15 | -2.08 | -3.18 | -0.84 | -1.01 | -4.25 | -1.77 | -1.64|
| dec-waitktgt |  |  | above | most | cal | point | of | the | actors | is | the | actors | that | the | actors | in | have | themselves | in | a | rather | question@@ | bi@@ | ous | situation | . | </s>|
| full sent tgt |  |  | the | actors | cal | point | of | this | film | is | the | actors | that | some | actors | are | perform | themselves | in | rather | rather | question@@ | bi@@ | ous | setting | . | </s>|
| ref | in | particular | , | the | ac@@ | t@@ | res@@ | ses | play | a | major | role | in | the | sometimes | rather | du@@ | bi@@ | ous | st@@ | aging | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | werden | hart | ange@@ | fasst | , | mit | dem | kopf | unter | wasser | get@@ | au@@ | cht | , | mit | ihren | ab@@ | end@@ | ro@@ | ben | an | die | wand | ge@@ | ta@@ | ck@@ | ert | .|
| waitk tgt |  |  | they | are | har@@ | d-@@ | pressed | to | keep | their | heads | under | water | . | </s>|
| waitk prob |  |  | 0.52 | 0.56 | 0.39 | 0.55 | 0.26 | 0.37 | 0.07 | 0.68 | 0.74 | 0.39 | 0.51 | 0.34 | 0.89|
| dec-waitk prob |  |  | 0.16 | 0.17 | 0.05 | 0.33 | 0.06 | 0.02 | 0.01 | 0.70 | 0.77 | 0.62 | 0.86 | 0.16 | 0.93|
| dec-waitk rank |  |  | 1 | 1 | 4 | 1 | 3 | 7 | 8 | 0 | 0 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.17 | -2.86 | -3.30 | -1.88 | -2.66 | -4.60 | -4.79 | -2.33 | -1.40 | -2.78 | -1.40 | -1.53 | -1.41|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.48 | -2.24 | -3.28 | -1.82 | -3.76 | -2.44 | -4.78 | -2.13 | -1.45 | -2.89 | -2.38 | -2.37 | -1.79|
| full sent prob |  |  | 0.57 | 0.72 | 0.09 | 0.20 | 0.07 | 0.01 | 0.00 | 0.64 | 0.66 | 0.23 | 0.85 | 0.00 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 2 | 3 | 4 | 262 | 0 | 0 | 0 | 0 | 5 | 0|
| full sent KL (waitk->full) |  |  | -2.99 | -2.24 | -4.21 | -2.53 | -3.27 | -1.91 | -4.55 | -2.33 | -1.30 | -4.66 | -1.47 | -1.92 | -1.57|
| full sent KL (full->waitk) |  |  | -2.55 | -2.42 | -3.28 | -1.78 | -3.74 | -2.58 | -4.77 | -2.10 | -1.40 | -2.76 | -2.38 | -2.48 | -1.78|
| dec-waitktgt |  |  | you | will | hard | sh | hit@@ | , | face | their | heads | under | water | </s> | </s>|
| full sent tgt |  |  | they | are | se@@ | sh@@ | touch | , | the | their | heads | under | water | , | </s>|
| ref | they | are | man@@ | handled | , | their | heads | held | under | water | , | tack@@ | ed | to | the | wall | by | their | evening | go@@ | wn@@ | s | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | das | normalerweise | eher | lang@@ | wei@@ | lige | gebiet | der | straßen@@ | planung | hat | plötz@@ | lich | eine | intensi@@ | ve | debatte | mit | bun@@ | ten | allian@@ | zen | ent@@ | fa@@ | cht | .|
| waitk tgt |  |  | the | normally | rather | bor@@ | ing | area | of | road | planning | has | suddenly | reached | an | intensive | debate | with | bun@@ | t@@ | led | al@@ | li@@ | ances | . | </s>|
| waitk prob |  |  | 0.18 | 0.11 | 0.75 | 0.57 | 0.96 | 0.56 | 0.86 | 0.83 | 0.74 | 0.65 | 0.90 | 0.07 | 0.35 | 0.48 | 0.89 | 0.83 | 0.82 | 0.12 | 0.13 | 0.90 | 0.97 | 0.93 | 0.44 | 0.91|
| dec-waitk prob |  |  | 0.03 | 0.04 | 0.39 | 0.57 | 0.98 | 0.31 | 0.83 | 0.80 | 0.69 | 0.11 | 0.89 | 0.02 | 0.52 | 0.39 | 0.88 | 0.06 | 0.27 | 0.08 | 0.06 | 0.95 | 0.96 | 0.97 | 0.88 | 0.92|
| dec-waitk rank |  |  | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 8 | 0 | 1 | 0 | 1 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.33 | -3.68 | -2.59 | -1.62 | -0.99 | -3.71 | -2.01 | -1.64 | -2.62 | -2.44 | -1.52 | -4.35 | -2.25 | -1.67 | -1.76 | -1.41 | -3.95 | -4.58 | -2.01 | -1.13 | -1.13 | -1.00 | -1.49 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.99 | -5.49 | -1.67 | -2.06 | -1.19 | -2.51 | -1.85 | -1.43 | -2.26 | -1.59 | -1.44 | -4.33 | -2.46 | -2.42 | -1.54 | -1.43 | -1.39 | -5.26 | -4.98 | -1.58 | -1.08 | -1.41 | -2.69 | -1.67|
| full sent prob |  |  | 0.49 | 0.20 | 0.59 | 0.44 | 0.97 | 0.55 | 0.87 | 0.72 | 0.74 | 0.49 | 0.79 | 0.00 | 0.55 | 0.14 | 0.90 | 0.68 | 0.00 | 0.00 | 0.37 | 0.96 | 0.98 | 0.97 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 290 | 0 | 1 | 0 | 0 | 16 | 17 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.85 | -2.35 | -2.13 | -2.04 | -1.03 | -2.33 | -1.78 | -1.78 | -2.34 | -1.96 | -2.17 | -3.76 | -2.34 | -1.39 | -1.44 | -2.75 | -3.06 | -4.26 | -2.68 | -1.08 | -1.00 | -1.05 | -1.35 | -1.59|
| full sent KL (full->waitk) |  |  | -4.05 | -5.52 | -1.79 | -1.99 | -1.19 | -2.61 | -1.88 | -1.38 | -2.29 | -1.77 | -1.37 | -4.32 | -2.48 | -2.38 | -1.56 | -1.85 | -1.21 | -5.25 | -5.00 | -1.59 | -1.09 | -1.40 | -2.70 | -1.66|
| dec-waitktgt |  |  | usually | usual | rather | bor@@ | ing | area | of | road | planning | suddenly | suddenly | been | an | intense | debate | . | bun@@ | ch | les | al@@ | li@@ | ances | . | </s>|
| full sent tgt |  |  | the | usually | rather | bor@@ | ing | area | of | road | planning | has | suddenly | spar@@ | an | intense | debate | with | colour@@ | ch | led | al@@ | li@@ | ances | . | </s>|
| ref | the | usually | dul@@ | l | arena | of | highway | planning | has | suddenly | spa@@ | w@@ | ned | intense | debate | and | color@@ | ful | al@@ | li@@ | ances | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | amerikanische | bürger@@ | rechts@@ | vereinigung | ( | ac@@ | l@@ | u | ) | ist | ebenfalls | zu@@ | tief@@ | st | besorgt | und | äuß@@ | ert | eine | reihe | von | datenschutz@@ | bedenken | .|
| waitk tgt |  |  | the | american | civil | rights | association | ( | ac@@ | l@@ | u | ) | is | also | deeply | concerned | and | deeply | concerned | about | a | number | of | data | protection | concerns | . | </s>|
| waitk prob |  |  | 0.36 | 0.55 | 0.83 | 0.70 | 0.69 | 0.89 | 0.91 | 0.95 | 0.95 | 0.93 | 0.72 | 0.87 | 0.87 | 0.90 | 0.72 | 0.24 | 0.74 | 0.74 | 0.68 | 0.70 | 0.91 | 0.39 | 0.90 | 0.84 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.32 | 0.45 | 0.50 | 0.47 | 0.64 | 0.83 | 0.74 | 0.89 | 0.95 | 0.89 | 0.57 | 0.81 | 0.54 | 0.85 | 0.71 | 0.01 | 0.45 | 0.00 | 0.02 | 0.65 | 0.88 | 0.63 | 0.96 | 0.80 | 0.90 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 9 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.18 | -3.26 | -2.20 | -2.61 | -1.93 | -1.80 | -2.77 | -1.75 | -1.24 | -1.76 | -2.71 | -2.17 | -2.36 | -1.43 | -2.42 | -1.70 | -2.75 | -2.32 | -3.63 | -2.26 | -1.89 | -2.30 | -1.08 | -1.82 | -1.68 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.71 | -2.15 | -1.51 | -1.87 | -2.47 | -1.52 | -1.36 | -1.18 | -1.30 | -1.40 | -1.89 | -1.59 | -1.10 | -1.18 | -2.14 | -3.29 | -1.72 | -1.37 | -2.25 | -1.84 | -1.62 | -3.13 | -1.65 | -1.65 | -1.64 | -1.67|
| full sent prob |  |  | 0.76 | 0.46 | 0.81 | 0.54 | 0.73 | 0.84 | 0.84 | 0.86 | 0.93 | 0.92 | 0.83 | 0.83 | 0.84 | 0.87 | 0.84 | 0.00 | 0.21 | 0.53 | 0.70 | 0.61 | 0.92 | 0.63 | 0.96 | 0.91 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 267 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.12 | -3.30 | -1.56 | -2.67 | -1.86 | -1.81 | -2.09 | -1.97 | -1.41 | -1.57 | -1.80 | -1.99 | -1.32 | -1.47 | -1.69 | -1.10 | -1.96 | -2.32 | -2.48 | -1.99 | -1.55 | -2.25 | -1.06 | -1.35 | -1.65 | -1.60|
| full sent KL (full->waitk) |  |  | -2.73 | -2.17 | -1.72 | -1.91 | -2.52 | -1.53 | -1.43 | -1.15 | -1.28 | -1.42 | -2.05 | -1.61 | -1.32 | -1.19 | -2.22 | -3.27 | -1.58 | -1.71 | -2.63 | -1.82 | -1.65 | -3.12 | -1.66 | -1.73 | -1.65 | -1.66|
| dec-waitktgt |  |  | american | american | civil | rights | association | ( | ac@@ | l@@ | u | ) | is | also | deeply | concerned | and | ou@@ | concerned | . | it | number | of | data | protection | concerns | . | </s>|
| full sent tgt |  |  | the | american | civil | rights | association | ( | ac@@ | l@@ | u | ) | is | also | deeply | concerned | and | expres@@ | concerns | about | a | number | of | data | protection | concerns | . | </s>|
| ref | the | american | civil | liberties | union | is | deeply | concerned | , | too | , | raising | a | variety | of | privacy | issues | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | doch | während | man | sich | im | kongre@@ | ss | nicht | auf | ein | vorgehen | einigen | kann | , | warten | mehrere | bundes@@ | staaten | nicht | länger | .|
| waitk tgt |  |  | but | , | while | congress | has | not | agreed | on | a | course | of | action | , | several | federal | states | are | no | longer | waiting | . | </s>|
| waitk prob |  |  | 0.59 | 0.49 | 0.72 | 0.41 | 0.10 | 0.44 | 0.48 | 0.63 | 0.44 | 0.48 | 0.90 | 0.95 | 0.92 | 0.70 | 0.47 | 0.95 | 0.44 | 0.90 | 0.94 | 0.81 | 0.73 | 0.91|
| dec-waitk prob |  |  | 0.14 | 0.03 | 0.85 | 0.12 | 0.01 | 0.43 | 0.00 | 0.02 | 0.19 | 0.82 | 0.88 | 0.96 | 0.51 | 0.28 | 0.69 | 0.98 | 0.45 | 0.74 | 0.93 | 0.38 | 0.89 | 0.93|
| dec-waitk rank |  |  | 1 | 3 | 0 | 1 | 5 | 0 | 636 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.16 | -2.61 | -1.51 | -2.46 | -3.01 | -3.84 | -4.28 | -2.41 | -3.79 | -1.48 | -1.76 | -1.15 | -3.53 | -3.34 | -2.27 | -0.95 | -2.87 | -2.12 | -1.44 | -3.53 | -1.66 | -1.48|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.29 | -2.25 | -1.77 | -3.22 | -4.93 | -3.03 | -2.99 | -1.93 | -2.91 | -3.50 | -1.67 | -1.26 | -1.18 | -1.89 | -3.28 | -1.17 | -2.64 | -1.31 | -1.32 | -1.70 | -2.10 | -1.66|
| full sent prob |  |  | 0.64 | 0.57 | 0.81 | 0.40 | 0.01 | 0.07 | 0.49 | 0.49 | 0.17 | 0.61 | 0.88 | 0.97 | 0.89 | 0.79 | 0.05 | 0.91 | 0.34 | 0.74 | 0.93 | 0.59 | 0.89 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.37 | -2.34 | -1.58 | -2.17 | -1.84 | -1.92 | -2.33 | -2.74 | -3.52 | -2.52 | -1.80 | -1.03 | -1.75 | -1.71 | -1.09 | -1.43 | -3.03 | -1.87 | -1.39 | -2.96 | -1.57 | -1.55|
| full sent KL (full->waitk) |  |  | -2.54 | -2.40 | -1.75 | -3.32 | -4.93 | -2.98 | -3.18 | -2.18 | -2.91 | -3.42 | -1.67 | -1.27 | -1.48 | -2.17 | -3.07 | -1.12 | -2.58 | -1.30 | -1.32 | -1.84 | -2.10 | -1.66|
| dec-waitktgt |  |  | while | while | while | you | </s> | not | been | </s> | a | course | of | action | , | several | federal | states | are | no | longer | waiting | . | </s>|
| full sent tgt |  |  | but | , | while | congress | cannot | failed | agreed | on | a | course | of | action | , | several | states | states | are | no | longer | waiting | . | </s>|
| ref | and | while | congress | can | &apos;t | agree | on | whether | to | proceed | , | several | states | are | not | waiting | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | tausende | von | auto@@ | fahr@@ | ern | haben | die | fahr@@ | ten@@ | schrei@@ | ber | , | von | denen | einige | mit | g@@ | p@@ | s-@@ | überwachung | ausgestattet | sind | , | bereits | ge@@ | te@@ | stet | .|
| waitk tgt |  |  | thousands | of | drivers | have | lost | their | driving | lic@@ | ences | , | many | of | which | are | equipped | with | g@@ | ps | monitoring | . | </s>|
| waitk prob |  |  | 0.80 | 0.89 | 0.55 | 0.59 | 0.08 | 0.70 | 0.23 | 0.17 | 0.85 | 0.58 | 0.24 | 0.90 | 0.45 | 0.52 | 0.15 | 0.91 | 0.91 | 0.94 | 0.28 | 0.57 | 0.90|
| dec-waitk prob |  |  | 0.74 | 0.89 | 0.31 | 0.33 | 0.00 | 0.36 | 0.36 | 0.00 | 0.88 | 0.02 | 0.00 | 0.72 | 0.02 | 0.26 | 0.02 | 0.92 | 0.94 | 0.93 | 0.24 | 0.77 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 47 | 0 | 0 | 61 | 0 | 2 | 29 | 0 | 2 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.28 | -1.80 | -3.52 | -3.99 | -2.24 | -3.67 | -3.52 | -3.65 | -1.57 | -1.99 | -1.30 | -2.66 | -1.31 | -4.11 | -4.66 | -1.54 | -1.24 | -1.30 | -3.22 | -2.31 | -1.43|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.02 | -1.78 | -2.44 | -2.88 | -4.89 | -1.99 | -3.80 | -4.32 | -1.74 | -2.30 | -3.27 | -1.55 | -2.01 | -2.57 | -4.73 | -1.59 | -1.49 | -1.22 | -3.17 | -2.33 | -1.70|
| full sent prob |  |  | 0.83 | 0.90 | 0.51 | 0.83 | 0.00 | 0.39 | 0.00 | 0.06 | 0.87 | 0.74 | 0.03 | 0.85 | 0.41 | 0.37 | 0.87 | 0.91 | 0.90 | 0.92 | 0.45 | 0.73 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 5699 | 0 | 33 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.71 | -1.65 | -2.89 | -1.81 | -1.75 | -3.08 | -4.75 | -3.31 | -1.69 | -2.06 | -1.13 | -1.89 | -2.46 | -2.60 | -1.05 | -1.55 | -1.54 | -1.36 | -2.50 | -2.11 | -1.59|
| full sent KL (full->waitk) |  |  | -2.08 | -1.79 | -2.53 | -3.12 | -4.90 | -2.01 | -3.73 | -4.33 | -1.73 | -2.65 | -3.43 | -1.64 | -2.08 | -2.65 | -4.82 | -1.59 | -1.46 | -1.22 | -3.23 | -2.32 | -1.68|
| dec-waitktgt |  |  | thousands | of | drivers | have | </s> | their | driving | tac@@ | ences | </s> | </s> | of | them | are | g@@ | with | g@@ | ps | monitoring | . | </s>|
| full sent tgt |  |  | thousands | of | drivers | have | already | their | test | tac@@ | ences | , | some | of | which | have | equipped | with | g@@ | ps | monitoring | . | </s>|
| ref | thousands | of | mo@@ | tori@@ | sts | have | already | taken | the | black | boxes | , | some | of | which | have | g@@ | ps | monitoring | , | for | a | test | drive | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | art | und | weise | , | wie | wir | diese | steuern | zahlen | , | wird | sich | verändern | .|
| waitk tgt |  |  | the | way | in | which | we | are | going | to | pay | these | taxes | will | change | . | </s>|
| waitk prob |  |  | 0.64 | 0.84 | 0.57 | 0.92 | 0.91 | 0.20 | 0.16 | 0.90 | 0.60 | 0.77 | 0.94 | 0.87 | 0.76 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.80 | 0.75 | 0.03 | 0.78 | 0.86 | 0.02 | 0.01 | 0.88 | 0.97 | 0.37 | 0.97 | 0.75 | 0.68 | 0.90 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 4 | 0 | 0 | 3 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.91 | -1.77 | -2.76 | -2.53 | -1.98 | -3.40 | -2.65 | -1.84 | -0.76 | -2.75 | -1.01 | -2.36 | -2.28 | -1.65 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.95 | -1.74 | -2.39 | -1.46 | -1.52 | -4.00 | -4.23 | -1.68 | -3.10 | -1.48 | -1.18 | -1.55 | -1.89 | -1.68 | -1.65|
| full sent prob |  |  | 0.78 | 0.86 | 0.39 | 0.89 | 0.89 | 0.03 | 0.03 | 0.90 | 0.92 | 0.47 | 0.95 | 0.76 | 0.66 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.12 | -1.55 | -2.05 | -1.81 | -1.69 | -1.08 | -1.69 | -1.71 | -1.13 | -2.43 | -1.12 | -1.96 | -2.12 | -1.67 | -1.61|
| full sent KL (full->waitk) |  |  | -2.94 | -1.82 | -2.57 | -1.53 | -1.54 | -3.99 | -4.22 | -1.69 | -3.08 | -1.54 | -1.17 | -1.57 | -1.87 | -1.68 | -1.65|
| dec-waitktgt |  |  | the | way | , | which | we | do | tax@@ | to | pay | these | taxes | will | change | . | </s>|
| full sent tgt |  |  | the | way | we | which | we | pay | paying | to | pay | these | taxes | will | change | . | </s>|
| ref | there | is | going | to | be | a | change | in | how | we | pay | these | taxes | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | doch | in | amerika | wird | nicht | mehr | so | viel | get@@ | an@@ | kt | wie | früher | .|
| waitk tgt |  |  | but | in | america | , | it | is | not | so | much | tan@@ | g@@ | led | as | it | was | before | . | </s>|
| waitk prob |  |  | 0.63 | 0.52 | 0.93 | 0.53 | 0.11 | 0.46 | 0.49 | 0.13 | 0.95 | 0.11 | 0.39 | 0.93 | 0.83 | 0.37 | 0.44 | 0.60 | 0.92 | 0.91|
| dec-waitk prob |  |  | 0.68 | 0.34 | 0.98 | 0.02 | 0.09 | 0.18 | 0.63 | 0.26 | 0.95 | 0.20 | 0.01 | 0.90 | 0.03 | 0.28 | 0.33 | 0.64 | 0.90 | 0.93|
| dec-waitk rank |  |  | 0 | 1 | 0 | 4 | 1 | 1 | 0 | 1 | 0 | 0 | 7 | 0 | 1 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.07 | -2.06 | -0.92 | -2.64 | -3.72 | -2.71 | -1.91 | -2.69 | -1.18 | -4.23 | -2.43 | -1.14 | -1.83 | -1.85 | -2.15 | -2.12 | -1.70 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.33 | -2.63 | -1.35 | -2.74 | -4.38 | -2.61 | -2.94 | -4.05 | -1.20 | -4.75 | -3.65 | -1.18 | -1.40 | -2.21 | -2.27 | -1.91 | -1.52 | -1.62|
| full sent prob |  |  | 0.59 | 0.18 | 0.91 | 0.47 | 0.09 | 0.38 | 0.28 | 0.01 | 0.94 | 0.37 | 0.01 | 0.96 | 0.67 | 0.40 | 0.45 | 0.61 | 0.91 | 0.92|
| full sent rank |  |  | 0 | 1 | 0 | 0 | 3 | 0 | 1 | 19 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.65 | -2.98 | -1.45 | -2.80 | -3.94 | -3.06 | -2.21 | -3.92 | -1.27 | -3.27 | -2.24 | -1.02 | -2.39 | -1.89 | -2.08 | -2.03 | -1.63 | -1.58|
| full sent KL (full->waitk) |  |  | -2.29 | -2.56 | -1.29 | -2.92 | -4.38 | -2.65 | -2.85 | -4.01 | -1.19 | -4.76 | -3.66 | -1.22 | -1.83 | -2.25 | -2.30 | -1.91 | -1.53 | -1.61|
| dec-waitktgt |  |  | but | america | america | will | no | will | not | that | much | tan@@ | k | led | . | before | was | before | . | </s>|
| full sent tgt |  |  | but | america | america | , | the | is | no | getting | much | tan@@ | ked | led | as | it | was | before | . | </s>|
| ref | americans | don | &apos;t | buy | as | much | gas | as | they | used | to | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | politiker | wagen | bei | hohen | sp@@ | rit@@ | preisen | nicht | , | die | steuer | auch | nur | um | einen | c@@ | ent | anzu@@ | heben | .|
| waitk tgt |  |  | politicians | d@@ | are | to | take | the | risk | of | driving | the | tax | even | by | a | pen@@ | ny | , | at | high | prices | . | </s>|
| waitk prob |  |  | 0.86 | 0.41 | 0.97 | 0.60 | 0.03 | 0.14 | 0.21 | 0.78 | 0.08 | 0.54 | 0.74 | 0.47 | 0.31 | 0.47 | 0.37 | 0.85 | 0.22 | 0.40 | 0.85 | 0.40 | 0.78 | 0.91|
| dec-waitk prob |  |  | 0.66 | 0.40 | 0.96 | 0.59 | 0.02 | 0.02 | 0.02 | 0.67 | 0.00 | 0.01 | 0.52 | 0.04 | 0.07 | 0.69 | 0.09 | 0.85 | 0.06 | 0.70 | 0.83 | 0.63 | 0.88 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 6 | 3 | 4 | 0 | 20 | 5 | 0 | 2 | 2 | 0 | 2 | 0 | 4 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.44 | -3.47 | -1.11 | -2.81 | -5.26 | -1.88 | -4.09 | -2.56 | -3.17 | -2.92 | -3.27 | -2.77 | -4.51 | -2.52 | -1.70 | -1.33 | -3.64 | -1.96 | -1.84 | -2.70 | -1.74 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -1.36 | -2.89 | -1.10 | -3.11 | -5.50 | -4.65 | -4.63 | -2.02 | -4.69 | -2.99 | -2.33 | -2.29 | -3.76 | -3.35 | -2.41 | -1.26 | -2.74 | -3.01 | -1.57 | -3.26 | -2.02 | -1.65|
| full sent prob |  |  | 0.54 | 0.12 | 0.97 | 0.08 | 0.02 | 0.38 | 0.00 | 0.57 | 0.08 | 0.05 | 0.72 | 0.06 | 0.04 | 0.09 | 0.39 | 0.86 | 0.04 | 0.76 | 0.78 | 0.58 | 0.79 | 0.91|
| full sent rank |  |  | 0 | 2 | 0 | 2 | 10 | 0 | 87 | 0 | 0 | 3 | 0 | 1 | 4 | 2 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.67 | -2.73 | -1.05 | -1.43 | -4.39 | -2.76 | -2.96 | -2.38 | -4.38 | -3.11 | -2.41 | -2.13 | -2.85 | -3.46 | -1.58 | -1.41 | -1.98 | -1.74 | -2.03 | -2.98 | -1.96 | -1.62|
| full sent KL (full->waitk) |  |  | -1.27 | -2.80 | -1.11 | -2.88 | -5.50 | -4.69 | -4.63 | -1.95 | -4.70 | -3.01 | -2.45 | -2.31 | -3.76 | -3.12 | -2.46 | -1.27 | -2.79 | -3.03 | -1.54 | -3.24 | -1.97 | -1.64|
| dec-waitktgt |  |  | politicians | d@@ | are | to | high | high | pl@@ | of | high | at | tax | at | for | a | cent | ny | at | at | high | prices | . | </s>|
| full sent tgt |  |  | politicians | do | are | not | raise | the | tax | of | driving | at | tax | at | to | raising | cent | ny | at | at | high | prices | . | </s>|
| ref | politicians | are | lo@@ | ath | to | raise | the | tax | even | one | pen@@ | ny | when | gas | prices | are | high | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | „ | das | stellt | die | langfristig | sinn@@ | voll@@ | ste | alternative | dar | \“ | , | sagte | er | .|
| waitk tgt |  |  | \“ | this | is | the | most | sensible | alternative | in | the | long | term | , | \” | he | said | . | </s>|
| waitk prob |  |  | 0.43 | 0.51 | 0.31 | 0.69 | 0.32 | 0.25 | 0.37 | 0.47 | 0.89 | 0.86 | 0.58 | 0.77 | 0.86 | 0.88 | 0.66 | 0.93 | 0.90|
| dec-waitk prob |  |  | 0.33 | 0.11 | 0.18 | 0.11 | 0.02 | 0.62 | 0.36 | 0.70 | 0.91 | 0.85 | 0.56 | 0.75 | 0.93 | 0.91 | 0.80 | 0.92 | 0.92|
| dec-waitk rank |  |  | 0 | 3 | 0 | 1 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.67 | -3.65 | -3.34 | -2.74 | -3.72 | -1.85 | -2.36 | -1.89 | -1.51 | -1.51 | -1.71 | -1.93 | -1.36 | -1.45 | -1.89 | -1.54 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.77 | -2.39 | -3.49 | -2.00 | -4.11 | -3.63 | -3.23 | -2.49 | -1.75 | -1.59 | -1.75 | -1.67 | -1.76 | -1.68 | -2.81 | -1.40 | -1.69|
| full sent prob |  |  | 0.58 | 0.58 | 0.74 | 0.87 | 0.53 | 0.31 | 0.12 | 0.71 | 0.90 | 0.85 | 0.54 | 0.81 | 0.89 | 0.93 | 0.83 | 0.92 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.22 | -1.88 | -1.89 | -1.73 | -2.12 | -2.78 | -2.61 | -1.93 | -1.63 | -1.58 | -1.75 | -1.74 | -1.62 | -1.30 | -1.72 | -1.55 | -1.61|
| full sent KL (full->waitk) |  |  | -2.84 | -2.60 | -3.61 | -2.39 | -4.25 | -3.58 | -3.17 | -2.49 | -1.74 | -1.59 | -1.74 | -1.71 | -1.74 | -1.70 | -2.83 | -1.40 | -1.68|
| dec-waitktgt |  |  | \“ | the | is | what | sensible | sensible | alternative | in | the | long | term | , | \” | he | said | . | </s>|
| full sent tgt |  |  | \“ | this | is | the | most | sensible | long-term | in | the | long | term | , | \” | he | said | . | </s>|
| ref | &quot; | this | works | out | as | the | most | logical | alternative | over | the | long | term | , | &quot; | he | said | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | büro@@ | kraten | be@@ | zeichnen | es | als | mei@@ | len@@ | basi@@ | erte | benutz@@ | ergeb@@ | ü@@ | hr | .|
| waitk tgt |  |  | bureaucr@@ | ats | call | it | the | mil@@ | est@@ | one | based | user | benefit | . | </s>|
| waitk prob |  |  | 0.83 | 0.96 | 0.40 | 0.94 | 0.30 | 0.78 | 0.36 | 0.43 | 0.43 | 0.51 | 0.16 | 0.33 | 0.91|
| dec-waitk prob |  |  | 0.33 | 0.89 | 0.40 | 0.85 | 0.04 | 0.36 | 0.02 | 0.45 | 0.00 | 0.62 | 0.00 | 0.06 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 74 | 0 | 69 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.76 | -1.59 | -3.55 | -1.73 | -3.14 | -4.32 | -2.30 | -3.55 | -1.02 | -2.47 | -5.28 | -1.91 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -1.53 | -1.07 | -3.46 | -1.20 | -3.08 | -1.69 | -2.76 | -2.91 | -4.03 | -3.03 | -4.19 | -2.88 | -1.64|
| full sent prob |  |  | 0.68 | 0.94 | 0.68 | 0.84 | 0.07 | 0.40 | 0.10 | 0.58 | 0.00 | 0.76 | 0.01 | 0.75 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 16 | 0 | 9 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.84 | -1.29 | -2.28 | -1.62 | -2.34 | -2.74 | -3.30 | -3.43 | -2.88 | -2.19 | -4.74 | -2.09 | -1.58|
| full sent KL (full->waitk) |  |  | -1.77 | -1.11 | -3.55 | -1.20 | -3.15 | -1.72 | -2.75 | -2.94 | -4.04 | -3.08 | -4.19 | -3.07 | -1.63|
| dec-waitktgt |  |  | bureaucr@@ | ats | call | it | me@@ | mil@@ | e@@ | one | </s> | user | </s> | </s> | </s>|
| full sent tgt |  |  | bureaucr@@ | ats | call | it | mil@@ | mil@@ | e@@ | one | in | user | charge | . | </s>|
| ref | won@@ | ks | call | it | a | mil@@ | e@@ | ag@@ | e-@@ | based | user | fee | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | us-@@ | sen@@ | at | genehmi@@ | gte | letz@@ | tes | jahr | ein | 90 | millionen | dollar | teu@@ | res | pi@@ | lot@@ | projekt | , | das | 10@@ | .000 | autos | umfasst | hätte | .|
| waitk tgt |  |  | the | us | sen@@ | ate | approved | a | new | law | on | the | subject | of | the | death | penalty | last | year | , | which | was | $ | 90 | million | expensive | . | </s>|
| waitk prob |  |  | 0.67 | 0.73 | 0.93 | 0.96 | 0.44 | 0.29 | 0.07 | 0.03 | 0.16 | 0.12 | 0.07 | 0.32 | 0.05 | 0.06 | 0.74 | 0.22 | 0.93 | 0.55 | 0.50 | 0.11 | 0.32 | 0.86 | 0.88 | 0.25 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.82 | 0.78 | 0.99 | 0.97 | 0.72 | 0.02 | 0.05 | 0.00 | 0.01 | 0.17 | 0.02 | 0.01 | 0.11 | 0.00 | 0.80 | 0.15 | 0.89 | 0.07 | 0.04 | 0.13 | 0.85 | 0.81 | 0.85 | 0.00 | 0.84 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 178 | 8 | 1 | 3 | 1 | 0 | 25 | 0 | 1 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 151 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.92 | -1.69 | -0.84 | -1.06 | -1.67 | -2.88 | -1.74 | -0.14 | -3.29 | -4.34 | -4.60 | -1.25 | -5.33 | -5.27 | -1.70 | -2.91 | -1.79 | -3.42 | -3.93 | -5.03 | -1.36 | -2.01 | -1.93 | -1.52 | -1.87 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.93 | -2.04 | -1.39 | -1.15 | -2.90 | -3.25 | -5.39 | -5.71 | -4.31 | -5.52 | -5.07 | -3.30 | -5.74 | -5.83 | -1.75 | -3.17 | -1.43 | -2.49 | -2.85 | -4.39 | -2.84 | -1.50 | -1.66 | -3.32 | -1.67 | -1.65|
| full sent prob |  |  | 0.55 | 0.85 | 0.97 | 0.95 | 0.78 | 0.76 | 0.00 | 0.00 | 0.01 | 0.14 | 0.00 | 0.42 | 0.11 | 0.00 | 0.63 | 0.02 | 0.90 | 0.36 | 0.27 | 0.01 | 0.85 | 0.87 | 0.86 | 0.02 | 0.02 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 5725 | 12 | 1 | 60 | 0 | 1 | 261 | 0 | 6 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 5 | 3 | 0|
| full sent KL (waitk->full) |  |  | -1.86 | -1.56 | -1.03 | -1.27 | -1.65 | -1.74 | -0.12 | -0.22 | -4.51 | -2.59 | -3.03 | -2.42 | -2.47 | -2.42 | -2.27 | -4.06 | -1.68 | -2.76 | -3.69 | -1.61 | -1.24 | -1.60 | -1.82 | -2.48 | -2.43 | -1.70|
| full sent KL (full->waitk) |  |  | -2.78 | -2.08 | -1.37 | -1.14 | -2.93 | -3.30 | -5.40 | -5.71 | -4.31 | -5.52 | -5.07 | -3.31 | -5.74 | -5.83 | -1.65 | -3.17 | -1.44 | -2.63 | -2.95 | -4.41 | -2.85 | -1.54 | -1.67 | -3.29 | -1.07 | -1.64|
| dec-waitktgt |  |  | the | us | sen@@ | ate | approved | the | year | year | last | 90 | year | last | the | dollar | penalty | </s> | year | . | </s> | was | $ | 90 | million | . | . | </s>|
| full sent tgt |  |  | the | us | sen@@ | ate | approved | a | $ | $ | pilot | $ | $ | of | $ | $ | penalty | of | year | , | which | would | $ | 90 | million | , | , | </s>|
| ref | the | u.s. | sen@@ | ate | approved | a | $ | 9@@ | 0-@@ | million | pilot | project | last | year | that | would | have | involved | about | 10@@ | ,000 | cars | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | mehrere | bundes@@ | staaten | und | groß@@ | städte | bewegen | sich | nicht@@ | s@@ | de@@ | st@@ | ot@@ | ro@@ | tz | auf | eigene | fau@@ | st | in | diese | richtung | .|
| waitk tgt |  |  | several | states | and | large | cities | are | moving | in | the | right | direction | , | however | . | </s>|
| waitk prob |  |  | 0.51 | 0.58 | 0.87 | 0.30 | 0.86 | 0.59 | 0.35 | 0.22 | 0.32 | 0.29 | 0.98 | 0.41 | 0.41 | 0.64 | 0.91|
| dec-waitk prob |  |  | 0.89 | 0.79 | 0.42 | 0.06 | 0.95 | 0.22 | 0.30 | 0.02 | 0.27 | 0.01 | 0.94 | 0.13 | 0.39 | 0.80 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 5 | 0 | 14 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.17 | -1.38 | -2.81 | -1.86 | -1.05 | -3.40 | -4.12 | -4.57 | -3.78 | -4.78 | -1.25 | -2.07 | -3.78 | -2.13 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.15 | -2.56 | -1.45 | -2.71 | -1.35 | -2.46 | -3.76 | -3.85 | -2.97 | -1.90 | -0.97 | -2.59 | -3.04 | -2.21 | -1.68|
| full sent prob |  |  | 0.18 | 0.84 | 0.87 | 0.27 | 0.89 | 0.38 | 0.02 | 0.65 | 0.02 | 0.06 | 0.93 | 0.39 | 0.58 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.11 | -1.46 | -1.90 | -2.32 | -1.44 | -2.20 | -1.25 | -2.37 | -1.52 | -1.56 | -1.41 | -2.33 | -2.31 | -1.48 | -1.63|
| full sent KL (full->waitk) |  |  | -2.86 | -2.57 | -1.77 | -2.75 | -1.31 | -2.50 | -3.68 | -3.96 | -2.97 | -2.06 | -0.96 | -2.66 | -3.11 | -2.26 | -1.67|
| dec-waitktgt |  |  | several | states | and | cities | cities | move | moving | . | the | same | direction | . | however | . | </s>|
| full sent tgt |  |  | several | states | and | large | cities | are | nevertheless | in | this | same | direction | , | however | . | </s>|
| ref | several | states | and | cities | are | nonetheless | moving | ahead | on | their | own | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | am | enga@@ | gi@@ | er@@ | testen | ist | ore@@ | g@@ | on | , | das | derzeit | 5@@ | .000 | fahrer | für | das | größte | experi@@ | ment | des | landes | an@@ | wir@@ | bt | .|
| waitk tgt |  |  | the | most | dedicated | is | o@@ | reg@@ | on | , | the | current | 5@@ | ,000 | driver | for | the | largest | experim@@ | ent | of | the | country | . | </s>|
| waitk prob |  |  | 0.22 | 0.27 | 0.32 | 0.09 | 0.60 | 0.99 | 0.95 | 0.80 | 0.44 | 0.12 | 0.33 | 0.77 | 0.38 | 0.60 | 0.73 | 0.38 | 0.72 | 0.86 | 0.39 | 0.82 | 0.88 | 0.73 | 0.91|
| dec-waitk prob |  |  | 0.07 | 0.00 | 0.05 | 0.28 | 0.47 | 0.95 | 0.94 | 0.01 | 0.01 | 0.19 | 0.06 | 0.88 | 0.02 | 0.00 | 0.37 | 0.00 | 0.28 | 0.92 | 0.01 | 0.47 | 0.72 | 0.89 | 0.93|
| dec-waitk rank |  |  | 4 | 84 | 2 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 3 | 8 | 0 | 214 | 0 | 0 | 2 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.81 | -1.60 | -1.95 | -3.61 | -3.10 | -1.15 | -1.39 | -3.12 | -1.62 | -4.40 | -5.11 | -1.41 | -2.22 | -1.58 | -4.75 | -6.09 | -4.97 | -1.30 | -1.50 | -3.57 | -2.46 | -1.67 | -1.46|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.36 | -5.03 | -3.30 | -5.11 | -2.19 | -0.84 | -1.26 | -1.53 | -2.69 | -4.68 | -4.11 | -1.85 | -2.84 | -2.30 | -2.51 | -2.53 | -2.47 | -1.64 | -2.34 | -1.87 | -1.46 | -2.20 | -1.67|
| full sent prob |  |  | 0.15 | 0.50 | 0.07 | 0.31 | 0.82 | 0.98 | 0.93 | 0.83 | 0.01 | 0.33 | 0.30 | 0.91 | 0.25 | 0.24 | 0.79 | 0.08 | 0.83 | 0.95 | 0.05 | 0.76 | 0.89 | 0.90 | 0.91|
| full sent rank |  |  | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.94 | -3.35 | -4.27 | -3.70 | -1.64 | -1.02 | -1.44 | -1.77 | -2.11 | -3.22 | -4.37 | -1.23 | -2.70 | -2.89 | -2.20 | -1.28 | -1.97 | -1.08 | -1.51 | -2.21 | -1.63 | -1.56 | -1.62|
| full sent KL (full->waitk) |  |  | -4.37 | -5.14 | -3.20 | -5.11 | -2.34 | -0.86 | -1.26 | -2.07 | -2.73 | -4.70 | -4.18 | -1.86 | -2.92 | -2.42 | -2.76 | -2.56 | -2.79 | -1.66 | -2.57 | -2.07 | -1.58 | -2.21 | -1.66|
| dec-waitktgt |  |  | am | eng@@ | committed | is | o@@ | reg@@ | on | . | </s> | current | figure | ,000 | . | . | the | car | experim@@ | ent | . | the | country | . | </s>|
| full sent tgt |  |  | o@@ | most | committed | is | o@@ | reg@@ | on | , | who | current | 5@@ | ,000 | drivers | recru@@ | the | country | experim@@ | ent | in | the | country | . | </s>|
| ref | the | most | e@@ | ager | is | o@@ | reg@@ | on | , | which | is | en@@ | li@@ | sting | 5@@ | ,000 | drivers | in | the | country | &apos;s | biggest | experim@@ | ent | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | diese | fahrer | werden | bald | die | mei@@ | len@@ | gebühren | statt | der | miner@@ | al@@ | öl@@ | steuer | an | den | bundes@@ | staat | zahlen | .|
| waitk tgt |  |  | these | drivers | will | soon | be | charged | mil@@ | e@@ | age | instead | of | the | oil | tax | to | the | federal | state | . | </s>|
| waitk prob |  |  | 0.42 | 0.57 | 0.78 | 0.22 | 0.37 | 0.16 | 0.53 | 0.94 | 0.99 | 0.27 | 0.91 | 0.26 | 0.23 | 0.81 | 0.43 | 0.86 | 0.42 | 0.84 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.54 | 0.75 | 0.75 | 0.86 | 0.67 | 0.01 | 0.09 | 0.97 | 0.99 | 0.51 | 0.89 | 0.25 | 0.35 | 0.91 | 0.10 | 0.73 | 0.23 | 0.65 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.99 | -2.16 | -2.14 | -1.08 | -2.38 | -4.70 | -4.23 | -0.99 | -0.88 | -2.81 | -1.76 | -2.57 | -1.82 | -1.32 | -3.63 | -2.54 | -2.19 | -2.52 | -1.76 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.47 | -1.55 | -2.02 | -4.27 | -3.71 | -3.78 | -1.62 | -1.19 | -0.95 | -3.38 | -1.59 | -2.83 | -3.28 | -1.99 | -2.20 | -1.77 | -2.07 | -1.63 | -1.73 | -1.62|
| full sent prob |  |  | 0.53 | 0.70 | 0.85 | 0.76 | 0.19 | 0.04 | 0.39 | 0.94 | 0.99 | 0.03 | 0.91 | 0.19 | 0.11 | 0.90 | 0.71 | 0.87 | 0.36 | 0.76 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 1 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.88 | -2.55 | -1.73 | -1.64 | -1.59 | -1.07 | -2.51 | -1.23 | -0.89 | -2.64 | -1.65 | -2.97 | -2.65 | -1.23 | -2.23 | -1.79 | -2.14 | -2.23 | -1.71 | -1.60|
| full sent KL (full->waitk) |  |  | -3.46 | -1.53 | -2.08 | -4.25 | -3.57 | -3.83 | -1.81 | -1.17 | -0.95 | -3.29 | -1.60 | -2.80 | -3.23 | -1.99 | -2.42 | -1.87 | -2.08 | -1.70 | -1.73 | -1.62|
| dec-waitktgt |  |  | these | drivers | will | soon | be | mil@@ | </s> | e@@ | age | instead | of | petro@@ | petro@@ | tax | . | the | state | state | . | </s>|
| full sent tgt |  |  | these | drivers | will | soon | pay | paying | mil@@ | e@@ | age | charges | of | petro@@ | petro@@ | tax | to | the | state | state | . | </s>|
| ref | those | drivers | will | soon | pay | the | mil@@ | e@@ | age | fees | instead | of | gas | taxes | to | the | state | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | il@@ | lin@@ | o@@ | is | te@@ | stet | es | in | eingeschrän@@ | k@@ | tem | maße | mit | l@@ | k@@ | ws | .|
| waitk tgt |  |  | il@@ | lin@@ | o@@ | is | tests | it | in | restricted | mode | and | uses | l@@ | k@@ | ws | . | </s>|
| waitk prob |  |  | 0.72 | 0.97 | 0.97 | 0.94 | 0.27 | 0.75 | 0.63 | 0.26 | 0.04 | 0.23 | 0.07 | 0.59 | 0.23 | 0.60 | 0.76 | 0.91|
| dec-waitk prob |  |  | 0.87 | 0.97 | 0.94 | 0.94 | 0.33 | 0.64 | 0.09 | 0.10 | 0.09 | 0.00 | 0.00 | 0.06 | 0.41 | 0.00 | 0.38 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 8 | 43 | 3 | 0 | 4 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.70 | -1.12 | -1.30 | -1.37 | -3.65 | -2.75 | -4.76 | -4.13 | -2.90 | -1.62 | -3.01 | -4.83 | -3.94 | -1.08 | -3.42 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.54 | -1.11 | -1.11 | -1.37 | -3.40 | -2.02 | -2.10 | -2.77 | -5.35 | -3.08 | -4.96 | -2.76 | -4.37 | -2.07 | -2.15 | -1.68|
| full sent prob |  |  | 0.88 | 0.97 | 0.92 | 0.91 | 0.21 | 0.45 | 0.03 | 0.15 | 0.00 | 0.00 | 0.29 | 0.00 | 0.01 | 0.11 | 0.80 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 24 | 9 | 0 | 45 | 16 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.46 | -1.14 | -1.50 | -1.59 | -3.56 | -3.29 | -2.83 | -2.17 | -3.94 | -1.39 | -3.32 | -1.27 | -3.89 | -1.88 | -2.02 | -1.57|
| full sent KL (full->waitk) |  |  | -2.55 | -1.10 | -1.10 | -1.35 | -3.40 | -1.90 | -2.09 | -2.87 | -5.34 | -3.10 | -4.98 | -2.72 | -4.28 | -2.10 | -2.41 | -1.67|
| dec-waitktgt |  |  | il@@ | lin@@ | o@@ | is | tests | it | </s> | a | areas | </s> | </s> | the | k@@ | w | . | </s>|
| full sent tgt |  |  | il@@ | lin@@ | o@@ | is | tests | it | with | limited | measure | with | uses | tr@@ | cars | w | . | </s>|
| ref | il@@ | lin@@ | o@@ | is | is | trying | it | on | a | limited | basis | with | tr@@ | uc@@ | ks | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | damit | , | so | k@@ | h@@ | an | , | wäre | auch | die | öffentlichkeit | beru@@ | hi@@ | gter | .|
| waitk tgt |  |  | i | am | not | saying | that | this | would | mean | that | the | public | would | be | more | reas@@ | su@@ | red | . | </s>|
| waitk prob |  |  | 0.16 | 0.16 | 0.21 | 0.07 | 0.43 | 0.27 | 0.46 | 0.20 | 0.64 | 0.64 | 0.84 | 0.58 | 0.62 | 0.36 | 0.45 | 0.99 | 0.95 | 0.80 | 0.91|
| dec-waitk prob |  |  | 0.02 | 0.04 | 0.06 | 0.07 | 0.27 | 0.01 | 0.20 | 0.12 | 0.32 | 0.57 | 0.77 | 0.53 | 0.59 | 0.27 | 0.29 | 0.99 | 0.95 | 0.75 | 0.92|
| dec-waitk rank |  |  | 6 | 5 | 2 | 2 | 0 | 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.00 | -4.45 | -4.15 | -4.21 | -3.22 | -2.52 | -3.20 | -2.46 | -3.50 | -2.83 | -1.96 | -2.66 | -2.66 | -3.73 | -2.90 | -0.89 | -1.13 | -2.17 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.38 | -4.26 | -4.31 | -4.52 | -2.85 | -3.42 | -2.74 | -4.15 | -2.61 | -2.37 | -1.80 | -2.34 | -2.21 | -3.49 | -2.90 | -0.93 | -1.22 | -1.96 | -1.65|
| full sent prob |  |  | 0.00 | 0.03 | 0.04 | 0.16 | 0.72 | 0.11 | 0.50 | 0.01 | 0.57 | 0.68 | 0.82 | 0.60 | 0.61 | 0.31 | 0.41 | 1.00 | 0.96 | 0.48 | 0.91|
| full sent rank |  |  | 28 | 8 | 6 | 1 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.31 | -3.77 | -3.63 | -3.64 | -2.17 | -4.07 | -2.50 | -3.73 | -2.84 | -2.49 | -1.63 | -2.50 | -2.58 | -3.64 | -2.77 | -0.86 | -1.12 | -2.52 | -1.59|
| full sent KL (full->waitk) |  |  | -3.39 | -4.27 | -4.31 | -4.53 | -2.99 | -3.44 | -2.85 | -4.11 | -2.74 | -2.43 | -1.83 | -2.38 | -2.22 | -3.50 | -2.94 | -0.94 | -1.22 | -1.79 | -1.64|
| dec-waitktgt |  |  | so | say | saying | happy | that | , | , | be | that | the | public | would | be | more | reas@@ | su@@ | red | . | </s>|
| full sent tgt |  |  | that | think | sure | convinced | that | this | would | make | that | the | public | would | be | more | reas@@ | su@@ | red | . | </s>|
| ref | if | you | can | do | that | , | kh@@ | an | said | , | the | public | gets | more | comfortable | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | jag@@ | d | nach | dieser | technologie | hat | einige | behörden | zu | einem | kleinen | star@@ | tu@@ | p-@@ | unternehmen | namens | tru@@ | e | mi@@ | le@@ | age | in | kali@@ | for@@ | nien | geführt | .|
| waitk tgt |  |  | hun@@ | ting | for | this | technology | has | led | to | a | small | star@@ | tup | bo@@ | om | company | called | true | mic@@ | key | mouse | in | california | . | </s>|
| waitk prob |  |  | 0.53 | 0.83 | 0.60 | 0.71 | 0.89 | 0.83 | 0.17 | 0.47 | 0.36 | 0.52 | 0.12 | 0.49 | 0.05 | 0.56 | 0.55 | 0.78 | 0.83 | 0.23 | 0.42 | 0.18 | 0.45 | 0.78 | 0.51 | 0.91|
| dec-waitk prob |  |  | 0.84 | 0.71 | 0.73 | 0.65 | 0.93 | 0.03 | 0.00 | 0.02 | 0.34 | 0.66 | 0.16 | 0.25 | 0.00 | 0.35 | 0.00 | 0.35 | 0.92 | 0.00 | 0.01 | 0.00 | 0.10 | 0.02 | 0.39 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 12 | 4 | 0 | 0 | 0 | 1 | 3148 | 0 | 18 | 0 | 0 | 4 | 13 | 723 | 2 | 5 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.20 | -1.88 | -2.20 | -2.56 | -1.31 | -1.71 | -3.95 | -1.33 | -3.48 | -2.80 | -4.07 | -3.10 | -2.45 | -2.60 | -2.64 | -3.97 | -1.31 | -1.48 | -4.37 | -3.73 | -2.69 | -3.56 | -2.81 | -1.44|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.13 | -1.53 | -2.41 | -2.20 | -1.64 | -1.35 | -4.33 | -2.15 | -4.07 | -3.41 | -4.21 | -1.71 | -5.13 | -2.31 | -2.45 | -1.13 | -1.73 | -3.29 | -2.12 | -4.91 | -2.93 | -1.51 | -2.23 | -1.68|
| full sent prob |  |  | 0.12 | 0.86 | 0.74 | 0.67 | 0.94 | 0.77 | 0.70 | 0.01 | 0.74 | 0.89 | 0.86 | 0.64 | 0.00 | 0.16 | 0.23 | 0.65 | 0.95 | 0.00 | 0.00 | 0.00 | 0.86 | 0.92 | 0.90 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 649 | 0 | 1 | 0 | 0 | 26 | 85 | 355 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.13 | -1.58 | -2.17 | -2.47 | -1.26 | -1.76 | -1.97 | -1.21 | -2.02 | -1.35 | -1.08 | -1.62 | -1.80 | -3.63 | -2.91 | -2.00 | -1.08 | -0.25 | -2.39 | -3.16 | -1.58 | -1.32 | -1.40 | -1.61|
| full sent KL (full->waitk) |  |  | -2.85 | -1.62 | -2.41 | -2.21 | -1.65 | -1.86 | -4.43 | -2.15 | -4.18 | -3.51 | -4.26 | -1.84 | -5.13 | -2.22 | -2.58 | -1.33 | -1.75 | -3.23 | -2.10 | -4.89 | -3.15 | -2.07 | -2.44 | -1.67|
| dec-waitktgt |  |  | hun@@ | ting | for | this | technology | </s> | </s> | some | a | small | star@@ | t-@@ | </s> | om | . | called | true | mi@@ | hel | . | . | kal@@ | . | </s>|
| full sent tgt |  |  | the | ting | for | this | technology | has | led | some | a | small | star@@ | tup | company | om | called | called | true | mil@@ | e@@ | in | in | california | . | </s>|
| ref | the | hun@@ | t | for | that | technology | has | led | some | state | agencies | to | a | small | california | star@@ | tup | called | true | mil@@ | e@@ | age | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | firma | ist | ursprünglich | nicht | ange@@ | treten | , | um | bundes@@ | staaten | bei | der | besteuerung | von | auto@@ | fahr@@ | ern | zu | helfen | .|
| waitk tgt |  |  | the | company | was | not | originally | established | to | provide | state | states | with | a | tax | on | car | drivers | . | </s>|
| waitk prob |  |  | 0.58 | 0.74 | 0.51 | 0.44 | 0.51 | 0.37 | 0.74 | 0.22 | 0.07 | 0.38 | 0.86 | 0.17 | 0.35 | 0.75 | 0.32 | 0.81 | 0.43 | 0.91|
| dec-waitk prob |  |  | 0.81 | 0.79 | 0.15 | 0.66 | 0.67 | 0.08 | 0.62 | 0.00 | 0.23 | 0.09 | 0.07 | 0.02 | 0.92 | 0.40 | 0.19 | 0.69 | 0.72 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 121 | 2 | 0 | 2 | 5 | 0 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.86 | -2.16 | -2.74 | -2.21 | -1.87 | -4.49 | -3.25 | -3.19 | -1.65 | -4.88 | -3.71 | -3.17 | -0.87 | -3.44 | -3.75 | -2.37 | -2.33 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.28 | -2.36 | -2.74 | -2.75 | -2.38 | -3.04 | -2.03 | -4.06 | -5.21 | -4.09 | -1.22 | -4.32 | -4.42 | -1.97 | -2.91 | -1.76 | -2.44 | -1.68|
| full sent prob |  |  | 0.55 | 0.84 | 0.22 | 0.56 | 0.63 | 0.07 | 0.81 | 0.01 | 0.10 | 0.00 | 0.91 | 0.07 | 0.42 | 0.23 | 0.11 | 0.93 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 | 3 | 45 | 0 | 5 | 0 | 0 | 2 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.86 | -1.76 | -3.02 | -2.25 | -1.61 | -4.56 | -1.86 | -1.62 | -3.00 | -3.89 | -1.53 | -2.77 | -3.32 | -4.56 | -2.42 | -1.14 | -1.34 | -1.59|
| full sent KL (full->waitk) |  |  | -3.15 | -2.39 | -2.74 | -2.73 | -2.38 | -3.04 | -2.15 | -4.08 | -5.18 | -4.06 | -1.82 | -4.30 | -4.28 | -1.87 | -2.90 | -1.92 | -2.50 | -1.67|
| dec-waitktgt |  |  | the | company | is | not | originally | launched | to | federal | federal | states | in | tax | tax | on | cars | drivers | . | </s>|
| full sent tgt |  |  | the | company | was | not | originally | set | to | help | assistance | assistance | with | assistance | tax | on | drivers | drivers | . | </s>|
| ref | the | firm | was | not | originally | in | the | business | of | helping | states | tax | drivers | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | einigen | dieser | öffentlichen | pi@@ | lot@@ | programme | wurden | große | fehler | gemacht | .|
| waitk tgt |  |  | in | some | of | these | public | pilot | programmes | , | major | mistakes | have | been | made | . | </s>|
| waitk prob |  |  | 0.44 | 0.78 | 0.86 | 0.78 | 0.91 | 0.88 | 0.59 | 0.56 | 0.21 | 0.54 | 0.59 | 0.90 | 0.89 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.06 | 0.92 | 0.44 | 0.71 | 0.86 | 0.85 | 0.50 | 0.78 | 0.30 | 0.58 | 0.61 | 0.89 | 0.86 | 0.91 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.43 | -1.22 | -3.07 | -1.69 | -1.68 | -1.75 | -2.84 | -2.00 | -2.88 | -2.31 | -1.82 | -1.68 | -1.96 | -1.64 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.93 | -2.15 | -1.65 | -1.79 | -1.34 | -1.57 | -2.17 | -2.69 | -3.11 | -1.96 | -1.70 | -1.62 | -1.63 | -1.59 | -1.66|
| full sent prob |  |  | 0.07 | 0.92 | 0.88 | 0.72 | 0.84 | 0.87 | 0.65 | 0.50 | 0.19 | 0.56 | 0.67 | 0.89 | 0.90 | 0.91 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.42 | -1.22 | -1.79 | -1.90 | -1.97 | -1.68 | -1.87 | -2.87 | -3.19 | -2.32 | -1.67 | -1.71 | -1.64 | -1.62 | -1.59|
| full sent KL (full->waitk) |  |  | -2.92 | -2.15 | -1.95 | -1.80 | -1.33 | -1.59 | -2.24 | -2.57 | -3.09 | -1.96 | -1.72 | -1.62 | -1.66 | -1.59 | -1.66|
| dec-waitktgt |  |  | some | some | of | these | public | pilot | programmes | , | major | mistakes | have | been | made | . | </s>|
| full sent tgt |  |  | some | some | of | these | public | pilot | programmes | , | major | mistakes | have | been | made | . | </s>|
| ref | there | have | been | some | big | mistakes | in | some | of | these | state | pilot | programs | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | es | gibt | wesentlich | billi@@ | gere | und | weniger | in@@ | tru@@ | sive | möglichkeiten | , | dies | umzusetzen | .|
| waitk tgt |  |  | there | are | much | cheaper | and | less | in@@ | tru@@ | sive | ways | to | implement | this | . | </s>|
| waitk prob |  |  | 0.68 | 0.58 | 0.42 | 0.91 | 0.79 | 0.90 | 0.94 | 0.97 | 0.96 | 0.72 | 0.54 | 0.23 | 0.57 | 0.87 | 0.91|
| dec-waitk prob |  |  | 0.82 | 0.48 | 0.45 | 0.85 | 0.63 | 0.56 | 0.92 | 0.98 | 0.98 | 0.10 | 0.20 | 0.06 | 0.14 | 0.87 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.98 | -1.90 | -2.88 | -1.58 | -2.69 | -3.32 | -1.48 | -0.94 | -0.93 | -2.77 | -2.55 | -2.32 | -2.24 | -1.86 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.69 | -1.94 | -3.10 | -1.29 | -2.10 | -1.18 | -1.25 | -1.04 | -1.10 | -1.73 | -1.69 | -3.42 | -2.25 | -1.91 | -1.65|
| full sent prob |  |  | 0.86 | 0.87 | 0.44 | 0.86 | 0.73 | 0.79 | 0.82 | 0.95 | 0.97 | 0.92 | 0.30 | 0.28 | 0.44 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.61 | -1.51 | -2.31 | -1.64 | -2.04 | -2.12 | -2.19 | -1.18 | -1.06 | -0.97 | -1.93 | -3.39 | -2.25 | -1.74 | -1.61|
| full sent KL (full->waitk) |  |  | -2.72 | -2.03 | -3.10 | -1.31 | -2.17 | -1.34 | -1.18 | -1.01 | -1.09 | -2.20 | -1.84 | -3.41 | -2.38 | -1.93 | -1.64|
| dec-waitktgt |  |  | there | are | much | cheaper | and | less | in@@ | tru@@ | sive | options | . | do | it | . | </s>|
| full sent tgt |  |  | there | are | much | cheaper | and | less | in@@ | tru@@ | sive | ways | of | implement | this | . | </s>|
| ref | there | are | a | lot | less | expensive | and | less | in@@ | tru@@ | sive | ways | to | do | this | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | ore@@ | g@@ | on | experi@@ | men@@ | tieren | die | plan@@ | er | damit | , | auto@@ | fahr@@ | ern | eine | reihe | von | aus@@ | wahl@@ | möglichkeiten | zu | geben | .|
| waitk tgt |  |  | in | o@@ | reg@@ | on | , | the | plan@@ | ner | experim@@ | ents | with | using | car | drivers | to | create | a | series | of | choices | . | </s>|
| waitk prob |  |  | 0.31 | 0.94 | 0.95 | 0.94 | 0.54 | 0.53 | 0.47 | 0.22 | 0.49 | 0.96 | 0.54 | 0.05 | 0.30 | 0.84 | 0.60 | 0.08 | 0.74 | 0.25 | 0.91 | 0.77 | 0.33 | 0.90|
| dec-waitk prob |  |  | 0.78 | 0.79 | 0.97 | 0.92 | 0.16 | 0.23 | 0.40 | 0.36 | 0.61 | 0.95 | 0.65 | 0.00 | 0.04 | 0.72 | 0.01 | 0.08 | 0.76 | 0.36 | 0.90 | 0.49 | 0.85 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 5 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.97 | -1.92 | -1.01 | -1.55 | -3.41 | -4.31 | -3.56 | -4.53 | -2.72 | -1.05 | -2.61 | -3.65 | -3.70 | -1.87 | -3.62 | -5.53 | -2.38 | -2.86 | -1.73 | -3.34 | -1.66 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.64 | -1.08 | -1.20 | -1.29 | -2.89 | -3.60 | -3.28 | -4.55 | -3.11 | -1.05 | -2.96 | -5.32 | -3.27 | -1.68 | -2.17 | -4.82 | -2.59 | -2.90 | -1.61 | -1.46 | -2.98 | -1.70|
| full sent prob |  |  | 0.77 | 0.86 | 0.95 | 0.93 | 0.65 | 0.49 | 0.07 | 0.21 | 0.53 | 0.94 | 0.62 | 0.00 | 0.09 | 0.90 | 0.67 | 0.04 | 0.82 | 0.11 | 0.90 | 0.56 | 0.87 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 32 | 1 | 0 | 0 | 4 | 0 | 3 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.96 | -1.54 | -1.16 | -1.42 | -1.99 | -2.48 | -1.68 | -3.96 | -2.46 | -1.13 | -1.90 | -2.73 | -3.27 | -1.32 | -2.14 | -3.75 | -2.08 | -2.92 | -1.70 | -2.89 | -1.38 | -1.59|
| full sent KL (full->waitk) |  |  | -3.64 | -1.13 | -1.19 | -1.30 | -3.12 | -3.71 | -3.18 | -4.54 | -3.09 | -1.05 | -2.96 | -5.32 | -3.29 | -1.80 | -2.51 | -4.82 | -2.62 | -2.87 | -1.62 | -1.50 | -2.99 | -1.70|
| dec-waitktgt |  |  | in | o@@ | reg@@ | on | experim@@ | the | plan@@ | ner | experim@@ | ents | with | it | it | drivers | . | create | a | series | of | choices | . | </s>|
| full sent tgt |  |  | in | o@@ | reg@@ | on | , | the | pl@@ | ner | experim@@ | ents | with | giving | a | drivers | to | give | a | range | of | choices | . | </s>|
| ref | in | o@@ | reg@@ | on | , | pl@@ | ann@@ | ers | are | experim@@ | enting | with | giving | drivers | different | choices | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | können | sich | für | ein | gerät | mit | oder | ohne | g@@ | ps | entscheiden | .|
| waitk tgt |  |  | you | can | register | for | a | device | with | or | without | g@@ | ps | . | </s>|
| waitk prob |  |  | 0.50 | 0.77 | 0.23 | 0.66 | 0.72 | 0.83 | 0.78 | 0.95 | 0.97 | 0.79 | 0.97 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.41 | 0.83 | 0.00 | 0.73 | 0.82 | 0.85 | 0.79 | 0.83 | 0.91 | 0.92 | 0.94 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 37 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.78 | -1.79 | -4.04 | -2.11 | -1.92 | -1.65 | -2.16 | -1.95 | -1.58 | -1.21 | -1.33 | -1.75 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.47 | -1.99 | -3.39 | -2.54 | -2.32 | -1.88 | -2.17 | -1.18 | -1.02 | -1.95 | -1.01 | -1.84 | -1.64|
| full sent prob |  |  | 0.71 | 0.81 | 0.00 | 0.33 | 0.68 | 0.58 | 0.76 | 0.77 | 0.90 | 0.78 | 0.94 | 0.89 | 0.92|
| full sent rank |  |  | 0 | 0 | 69 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.43 | -1.81 | -1.73 | -3.28 | -2.53 | -2.15 | -2.11 | -2.34 | -1.68 | -1.67 | -1.32 | -1.75 | -1.56|
| full sent KL (full->waitk) |  |  | -3.59 | -1.98 | -3.41 | -2.33 | -2.24 | -1.69 | -2.15 | -1.13 | -1.01 | -1.86 | -1.01 | -1.84 | -1.64|
| dec-waitktgt |  |  | you | can | choose | for | a | device | with | or | without | g@@ | ps | . | </s>|
| full sent tgt |  |  | you | can | choose | for | a | device | with | or | without | g@@ | ps | . | </s>|
| ref | they | can | choose | a | device | with | or | without | g@@ | ps | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | wenn | wir | das | tun | , | machen | sich | hunder@@ | te | millionen | von | auto@@ | fahr@@ | ern | sorgen | über | ihre | privat@@ | sphäre | und | zahlreiche | andere | dinge | .|
| waitk tgt |  |  | if | we | do | that | , | hundreds | of | millions | of | car | drivers | will | worry | about | their | privacy | . | </s>|
| waitk prob |  |  | 0.68 | 0.88 | 0.84 | 0.32 | 0.78 | 0.81 | 0.85 | 0.89 | 0.86 | 0.28 | 0.67 | 0.62 | 0.46 | 0.92 | 0.82 | 0.64 | 0.36 | 0.90|
| dec-waitk prob |  |  | 0.77 | 0.72 | 0.84 | 0.39 | 0.75 | 0.52 | 0.55 | 0.96 | 0.36 | 0.03 | 0.39 | 0.78 | 0.22 | 0.15 | 0.12 | 0.28 | 0.85 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.84 | -2.23 | -1.85 | -2.44 | -2.15 | -2.33 | -2.32 | -1.08 | -2.44 | -1.68 | -3.40 | -1.97 | -2.09 | -2.45 | -4.41 | -2.79 | -1.62 | -1.44|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.62 | -1.57 | -1.71 | -2.41 | -1.95 | -1.71 | -1.70 | -1.57 | -1.50 | -3.89 | -1.73 | -2.53 | -2.06 | -0.87 | -1.44 | -1.77 | -2.23 | -1.76|
| full sent prob |  |  | 0.67 | 0.90 | 0.87 | 0.32 | 0.86 | 0.70 | 0.89 | 0.91 | 0.90 | 0.13 | 0.93 | 0.28 | 0.23 | 0.94 | 0.85 | 0.95 | 0.00 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 4 | 0|
| full sent KL (waitk->full) |  |  | -2.37 | -1.64 | -1.64 | -2.44 | -1.77 | -2.10 | -1.68 | -1.40 | -1.68 | -2.92 | -1.00 | -2.38 | -2.01 | -1.36 | -1.58 | -0.92 | -1.39 | -1.64|
| full sent KL (full->waitk) |  |  | -2.57 | -1.69 | -1.74 | -2.41 | -2.02 | -1.83 | -1.94 | -1.54 | -1.87 | -3.89 | -2.03 | -2.30 | -2.06 | -1.46 | -1.93 | -2.07 | -2.20 | -1.74|
| dec-waitktgt |  |  | if | we | do | that | , | hundreds | of | millions | will | cars | drivers | will | be | . | it | private | . | </s>|
| full sent tgt |  |  | if | we | do | that | , | hundreds | of | millions | of | drivers | drivers | are | be | about | their | privacy | and | </s>|
| ref | if | we | do | this | , | hundreds | of | millions | of | drivers | will | be | concerned | about | their | privacy | and | a | host | of | other | things | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | köni@@ | gs@@ | feld | : | kleine | mann@@ | schaft | schlägt | sich | wa@@ | cker|
| waitk tgt |  |  | the | royal | field | : | small | team | be@@ | ats | w@@ | ack@@ | er | and | the | team | is | w@@ | ack@@ | er | . | </s>|
| waitk prob |  |  | 0.17 | 0.12 | 0.50 | 0.69 | 0.41 | 0.56 | 0.11 | 0.98 | 0.92 | 0.96 | 0.92 | 0.07 | 0.04 | 0.11 | 0.07 | 0.22 | 0.96 | 0.91 | 0.14 | 0.90|
| dec-waitk prob |  |  | 0.02 | 0.52 | 0.84 | 0.72 | 0.69 | 0.67 | 0.00 | 0.86 | 0.36 | 0.97 | 0.93 | 0.00 | 0.05 | 0.02 | 0.13 | 0.00 | 0.97 | 0.92 | 0.63 | 0.92|
| dec-waitk rank |  |  | 5 | 0 | 0 | 0 | 0 | 0 | 68 | 0 | 0 | 0 | 0 | 20 | 1 | 1 | 0 | 125 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.82 | -2.47 | -1.18 | -2.09 | -2.18 | -2.22 | -0.97 | -1.39 | -3.56 | -1.09 | -1.33 | -3.04 | -5.56 | -6.21 | -5.36 | -5.78 | -1.08 | -1.37 | -2.35 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.41 | -5.23 | -3.07 | -2.40 | -3.37 | -3.43 | -4.98 | -0.88 | -1.02 | -1.16 | -1.46 | -4.88 | -5.78 | -5.63 | -5.05 | -4.84 | -1.17 | -1.50 | -5.09 | -1.74|
| full sent prob |  |  | 0.02 | 0.02 | 0.66 | 0.84 | 0.38 | 0.78 | 0.11 | 0.96 | 0.91 | 0.97 | 0.95 | 0.00 | 0.08 | 0.02 | 0.15 | 0.00 | 0.98 | 0.92 | 0.66 | 0.92|
| full sent rank |  |  | 4 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 38 | 0 | 0 | 0 | 75 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.29 | -5.64 | -2.02 | -1.77 | -3.54 | -1.99 | -3.10 | -1.03 | -1.43 | -1.10 | -1.24 | -3.31 | -5.61 | -6.25 | -5.05 | -5.94 | -0.96 | -1.41 | -2.19 | -1.54|
| full sent KL (full->waitk) |  |  | -4.41 | -5.17 | -3.00 | -2.47 | -3.27 | -3.48 | -5.00 | -0.96 | -1.43 | -1.16 | -1.47 | -4.89 | -5.78 | -5.63 | -5.05 | -4.84 | -1.18 | -1.50 | -5.09 | -1.73|
| dec-waitktgt |  |  | royal | royal | field | : | small | team | </s> | ats | w@@ | ack@@ | er | </s> | </s> | world | is | not | ack@@ | er | . | </s>|
| full sent tgt |  |  | king | king | field | : | small | team | w@@ | ats | w@@ | ack@@ | er | . | the | team | is | not | ack@@ | er | . | </s>|
| ref | kö@@ | ni@@ | gs@@ | fel@@ | d | : | small | team | gives | a | spi@@ | ri@@ | ted | performance | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | freiwilli@@ | ge | feuer@@ | w@@ | ehr | be@@ | wä@@ | lti@@ | gte | ihre | her@@ | b@@ | st@@ | haupt@@ | pro@@ | be | trotz | personal@@ | mangel@@ | s | mit | bra@@ | vo@@ | ur | .|
| waitk tgt |  |  | voluntary | fire@@ | figh@@ | ters | are | ir@@ | ri@@ | g@@ | ated | by | their | autumn | main | pro@@ | be | despite | personnel | short@@ | ages | with | brown | and | white | . | </s>|
| waitk prob |  |  | 0.36 | 0.48 | 0.43 | 0.44 | 0.19 | 0.10 | 0.12 | 0.73 | 0.97 | 0.48 | 0.42 | 0.32 | 0.44 | 0.42 | 0.45 | 0.38 | 0.41 | 0.84 | 0.92 | 0.50 | 0.20 | 0.04 | 0.06 | 0.08 | 0.91|
| dec-waitk prob |  |  | 0.47 | 0.31 | 0.02 | 0.80 | 0.00 | 0.61 | 0.04 | 0.71 | 0.45 | 0.00 | 0.00 | 0.48 | 0.06 | 0.94 | 0.33 | 0.00 | 0.09 | 0.95 | 0.98 | 0.00 | 0.01 | 0.00 | 0.09 | 0.17 | 0.92|
| dec-waitk rank |  |  | 0 | 1 | 6 | 0 | 12 | 0 | 5 | 0 | 1 | 9 | 6 | 0 | 1 | 0 | 1 | 18 | 1 | 0 | 0 | 20 | 16 | 120 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.72 | -1.39 | -3.16 | -1.61 | -0.93 | -2.56 | -4.11 | -1.35 | -1.18 | -1.39 | -1.95 | -2.91 | -4.69 | -0.87 | -2.22 | -2.58 | -4.54 | -1.05 | -0.91 | -2.52 | -4.99 | -4.92 | -5.01 | -4.58 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.96 | -2.20 | -2.24 | -2.82 | -4.24 | -4.90 | -3.97 | -1.62 | -0.54 | -2.62 | -2.73 | -3.96 | -3.59 | -3.62 | -3.68 | -2.21 | -2.53 | -1.70 | -1.17 | -2.46 | -3.98 | -5.39 | -5.44 | -5.13 | -1.66|
| full sent prob |  |  | 0.00 | 0.05 | 0.17 | 0.85 | 0.00 | 0.00 | 0.01 | 0.54 | 0.17 | 0.12 | 0.26 | 0.14 | 0.48 | 0.08 | 0.89 | 0.52 | 0.05 | 0.88 | 0.93 | 0.00 | 0.00 | 0.00 | 0.01 | 0.22 | 0.91|
| full sent rank |  |  | 10 | 1 | 1 | 0 | 172 | 1023 | 14 | 0 | 1 | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 3 | 741 | 45 | 30 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.87 | -0.79 | -2.60 | -1.42 | -3.92 | -4.02 | -2.31 | -2.02 | -0.75 | -3.37 | -3.38 | -3.23 | -3.26 | -4.91 | -1.17 | -2.07 | -3.24 | -1.51 | -1.08 | -1.26 | -1.84 | -3.94 | -5.15 | -3.98 | -1.59|
| full sent KL (full->waitk) |  |  | -2.92 | -2.18 | -2.33 | -2.83 | -4.24 | -4.85 | -3.97 | -1.52 | -0.32 | -2.69 | -2.87 | -3.87 | -3.74 | -3.33 | -3.89 | -2.43 | -2.52 | -1.65 | -1.14 | -2.47 | -3.97 | -5.40 | -5.44 | -5.13 | -1.65|
| dec-waitktgt |  |  | voluntary | fire | men | ters | </s> | ir@@ | responsible | g@@ | ating | </s> | </s> | autumn | </s> | pro@@ | tests | </s> | </s> | short@@ | ages | . | a | lights | white | . | </s>|
| full sent tgt |  |  | the | fire | men | ters | bra@@ | bra@@ | rit@@ | g@@ | ating | in | their | main | main | test | be | despite | a | short@@ | ages | . | flying | air | heavy | . | </s>|
| ref | the | voluntary | fire | service | bra@@ | vely | came | through | the | main | autumn | test | run | in | spite | of | a | lack | of | personnel | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | durch | den | ent@@ | stehenden | bran@@ | d | und | die | rau@@ | ch@@ | entwicklung | wurden | zwei | menschen | verletzt | , | einer | davon | konnte | aber | noch | einen | not@@ | ruf | ab@@ | senden | .|
| waitk tgt |  |  | the | resulting | industry | has | created | a | new | and | growing | trend | for | smo@@ | ke | , | one | of | which | has | not | yet | been | able | to | send | an | emergency | call | . | </s>|
| waitk prob |  |  | 0.27 | 0.50 | 0.13 | 0.16 | 0.13 | 0.23 | 0.09 | 0.04 | 0.06 | 0.04 | 0.16 | 0.36 | 0.50 | 0.14 | 0.24 | 0.78 | 0.86 | 0.24 | 0.33 | 0.41 | 0.38 | 0.54 | 0.90 | 0.72 | 0.30 | 0.94 | 0.72 | 0.87 | 0.91|
| dec-waitk prob |  |  | 0.22 | 0.40 | 0.00 | 0.00 | 0.01 | 0.22 | 0.02 | 0.03 | 0.03 | 0.02 | 0.21 | 0.30 | 0.49 | 0.22 | 0.47 | 0.83 | 0.69 | 0.15 | 0.06 | 0.26 | 0.62 | 0.05 | 0.90 | 0.52 | 0.42 | 0.90 | 0.85 | 0.87 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 95 | 657 | 16 | 0 | 5 | 1 | 2 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.24 | -3.99 | -1.70 | -3.56 | -5.00 | -4.09 | -5.13 | -4.96 | -5.27 | -5.03 | -2.78 | -1.94 | -2.03 | -2.62 | -3.01 | -1.99 | -1.95 | -3.16 | -3.22 | -3.19 | -2.35 | -5.34 | -1.69 | -3.28 | -2.47 | -1.54 | -1.40 | -1.82 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.06 | -3.70 | -4.70 | -4.18 | -4.43 | -4.17 | -5.21 | -5.45 | -5.31 | -5.26 | -3.14 | -3.05 | -1.86 | -3.62 | -3.18 | -2.18 | -1.43 | -3.44 | -3.62 | -3.17 | -3.94 | -2.94 | -1.66 | -2.33 | -2.84 | -1.17 | -2.38 | -1.80 | -1.66|
| full sent prob |  |  | 0.24 | 0.07 | 0.00 | 0.00 | 0.01 | 0.35 | 0.03 | 0.03 | 0.05 | 0.02 | 0.10 | 0.25 | 0.54 | 0.29 | 0.01 | 0.65 | 0.80 | 0.40 | 0.00 | 0.34 | 0.54 | 0.44 | 0.90 | 0.49 | 0.47 | 0.89 | 0.84 | 0.85 | 0.91|
| full sent rank |  |  | 0 | 1 | 274 | 7 | 14 | 0 | 1 | 1 | 1 | 6 | 3 | 1 | 0 | 0 | 7 | 0 | 0 | 0 | 49 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.78 | -3.02 | -0.95 | -2.02 | -3.48 | -3.76 | -5.12 | -5.39 | -5.32 | -4.77 | -2.78 | -2.92 | -1.82 | -2.86 | -3.85 | -2.80 | -1.75 | -2.90 | -3.21 | -3.57 | -3.11 | -3.98 | -1.66 | -3.33 | -2.55 | -1.58 | -1.57 | -1.90 | -1.60|
| full sent KL (full->waitk) |  |  | -4.03 | -3.57 | -4.69 | -4.20 | -4.43 | -4.19 | -5.21 | -5.45 | -5.31 | -5.26 | -3.13 | -3.01 | -1.86 | -3.61 | -3.10 | -2.07 | -1.51 | -3.47 | -3.61 | -3.18 | -3.91 | -3.11 | -1.66 | -2.31 | -2.85 | -1.17 | -2.37 | -1.78 | -1.65|
| dec-waitktgt |  |  | by | resulting | bran@@ | </s> | </s> | a | ra@@ | fire | more | smo@@ | for | smoking | ke | . | one | of | which | was | been | been | been | able | to | send | an | emergency | call | . | </s>|
| full sent tgt |  |  | the | fire | fire | fire | in@@ | a | fire | fire | in@@ | smo@@ | in | smoking | ke | , | which | of | which | has | been | yet | been | able | to | send | an | emergency | call | . | </s>|
| ref | two | people | were | in@@ | ju@@ | red | by | the | resulting | fire | and | the | spread | of | smo@@ | ke | , | however | , | one | was | able | to | make | an | emergency | call | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | nach | kurzer | zeit | ge@@ | lang | es | , | die | erste | person | zu | finden | und | ins | freie | zu | ge@@ | leiten | .|
| waitk tgt |  |  | after | a | short | time | , | the | first | person | was | able | to | find | and | enter | the | open | . | </s>|
| waitk prob |  |  | 0.24 | 0.79 | 0.90 | 0.49 | 0.49 | 0.39 | 0.75 | 0.90 | 0.35 | 0.78 | 0.91 | 0.63 | 0.43 | 0.16 | 0.64 | 0.15 | 0.31 | 0.90|
| dec-waitk prob |  |  | 0.48 | 0.45 | 0.94 | 0.29 | 0.46 | 0.09 | 0.83 | 0.94 | 0.16 | 0.29 | 0.59 | 0.21 | 0.04 | 0.03 | 0.76 | 0.85 | 0.80 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 6 | 5 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.25 | -3.12 | -1.23 | -3.26 | -2.59 | -2.65 | -2.08 | -1.20 | -3.65 | -4.17 | -3.44 | -5.25 | -4.28 | -4.59 | -2.17 | -1.15 | -1.82 | -1.47|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.08 | -1.98 | -1.38 | -2.21 | -2.86 | -3.74 | -2.63 | -1.59 | -3.80 | -1.65 | -1.38 | -2.60 | -3.12 | -4.33 | -2.70 | -5.07 | -3.32 | -1.68|
| full sent prob |  |  | 0.33 | 0.72 | 0.86 | 0.43 | 0.42 | 0.23 | 0.73 | 0.85 | 0.38 | 0.26 | 0.90 | 0.69 | 0.52 | 0.00 | 0.82 | 0.72 | 0.66 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 220 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.65 | -2.51 | -1.54 | -2.62 | -2.71 | -2.86 | -2.71 | -1.78 | -3.05 | -2.71 | -1.68 | -2.61 | -2.59 | -3.74 | -1.84 | -1.66 | -2.09 | -1.58|
| full sent KL (full->waitk) |  |  | -4.05 | -2.16 | -1.32 | -2.27 | -2.86 | -3.81 | -2.57 | -1.52 | -3.86 | -1.65 | -1.62 | -2.84 | -3.29 | -4.32 | -2.73 | -5.05 | -3.30 | -1.68|
| dec-waitktgt |  |  | after | a | short | period | , | </s> | first | person | succeeded | able | to | find | him | open | the | open | . | </s>|
| full sent tgt |  |  | after | a | short | time | , | it | first | person | was | found | to | find | and | lead | the | open | . | </s>|
| ref | after | a | short | time | they | managed | to | find | the | first | person | and | direct | them | out | of | the | building | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dies | war | nicht | so | einfach | , | da | auch | eine | enge | tre@@ | ppe | zu | überwinden | war | .|
| waitk tgt |  |  | this | was | not | so | easy | , | as | a | close | sta@@ | ir@@ | case | was | to | be | overcome | . | </s>|
| waitk prob |  |  | 0.51 | 0.72 | 0.87 | 0.42 | 0.54 | 0.47 | 0.40 | 0.25 | 0.40 | 0.64 | 0.71 | 0.69 | 0.52 | 0.35 | 0.82 | 0.74 | 0.70 | 0.90|
| dec-waitk prob |  |  | 0.05 | 0.76 | 0.90 | 0.64 | 0.78 | 0.30 | 0.33 | 0.05 | 0.25 | 0.81 | 0.46 | 0.85 | 0.37 | 0.07 | 0.94 | 0.46 | 0.81 | 0.92|
| dec-waitk rank |  |  | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.44 | -2.12 | -1.58 | -2.27 | -1.31 | -2.98 | -2.73 | -3.79 | -4.40 | -1.88 | -2.00 | -1.09 | -2.72 | -2.99 | -1.27 | -3.83 | -1.85 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.28 | -2.05 | -1.76 | -2.64 | -1.45 | -2.09 | -2.34 | -3.38 | -2.71 | -3.20 | -1.71 | -1.47 | -2.45 | -2.84 | -1.94 | -2.17 | -2.19 | -1.69|
| full sent prob |  |  | 0.28 | 0.69 | 0.82 | 0.62 | 0.79 | 0.39 | 0.42 | 0.29 | 0.02 | 0.88 | 0.84 | 0.89 | 0.27 | 0.17 | 0.94 | 0.53 | 0.66 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.43 | -2.36 | -2.04 | -2.23 | -1.42 | -2.48 | -2.59 | -2.91 | -3.36 | -1.48 | -1.19 | -1.11 | -2.21 | -3.00 | -1.25 | -3.51 | -2.09 | -1.59|
| full sent KL (full->waitk) |  |  | -2.37 | -2.00 | -1.70 | -2.64 | -1.45 | -2.18 | -2.36 | -3.42 | -2.68 | -3.24 | -1.90 | -1.47 | -2.42 | -2.85 | -1.94 | -2.22 | -2.11 | -1.69|
| dec-waitktgt |  |  | not | was | not | so | easy | . | as | it | close | sta@@ | ir@@ | case | was | also | be | overcome | . | </s>|
| full sent tgt |  |  | this | was | not | so | easy | , | as | a | narrow | sta@@ | ir@@ | case | could | also | be | overcome | . | </s>|
| ref | this | was | not | so | simple | as | they | also | had | to | negotiate | a | narrow | sta@@ | ir@@ | well | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | das | gebäude | , | eine | werk@@ | statt | mit | integri@@ | erter | st@@ | all@@ | ung | für | zwei | pfer@@ | de | , | war | nicht | einfach | zu | sichern | .|
| waitk tgt |  |  | the | building | , | a | workshop | with | integrated | stone | and | a | small | bar@@ | n | for | two | horses | , | was | not | easy | to | secure | . | </s>|
| waitk prob |  |  | 0.60 | 0.61 | 0.76 | 0.80 | 0.72 | 0.77 | 0.79 | 0.13 | 0.06 | 0.19 | 0.03 | 0.06 | 0.75 | 0.64 | 0.87 | 0.95 | 0.85 | 0.72 | 0.79 | 0.76 | 0.86 | 0.15 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.49 | 0.91 | 0.68 | 0.44 | 0.66 | 0.60 | 0.53 | 0.04 | 0.00 | 0.05 | 0.00 | 0.00 | 0.38 | 0.10 | 0.79 | 0.79 | 0.80 | 0.65 | 0.83 | 0.59 | 0.86 | 0.35 | 0.88 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 1 | 25 | 59 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.81 | -1.20 | -2.57 | -3.26 | -2.24 | -2.62 | -2.20 | -3.05 | -0.66 | -5.52 | -5.98 | -5.28 | -2.41 | -2.98 | -1.96 | -2.21 | -2.08 | -2.67 | -2.06 | -2.72 | -1.89 | -3.73 | -1.80 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.00 | -2.98 | -1.99 | -1.80 | -2.25 | -2.10 | -1.55 | -4.09 | -5.16 | -4.92 | -5.82 | -5.36 | -1.65 | -2.28 | -1.67 | -1.04 | -1.86 | -2.13 | -2.32 | -1.83 | -1.87 | -4.22 | -1.68 | -1.66|
| full sent prob |  |  | 0.65 | 0.81 | 0.76 | 0.55 | 0.58 | 0.78 | 0.53 | 0.00 | 0.00 | 0.16 | 0.00 | 0.05 | 0.56 | 0.74 | 0.88 | 0.93 | 0.85 | 0.74 | 0.84 | 0.65 | 0.90 | 0.47 | 0.89 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 16 | 1 | 38 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.65 | -1.80 | -2.05 | -2.39 | -2.57 | -2.17 | -2.15 | -2.63 | -2.32 | -4.36 | -4.82 | -5.27 | -2.42 | -2.07 | -1.59 | -1.37 | -1.83 | -2.20 | -1.85 | -2.49 | -1.68 | -3.27 | -1.72 | -1.57|
| full sent KL (full->waitk) |  |  | -3.08 | -2.94 | -2.04 | -1.88 | -2.20 | -2.21 | -1.55 | -4.05 | -5.16 | -4.94 | -5.82 | -5.36 | -1.76 | -2.58 | -1.74 | -1.15 | -1.90 | -2.19 | -2.33 | -1.87 | -1.90 | -4.23 | -1.69 | -1.66|
| dec-waitktgt |  |  | the | building | , | a | workshop | with | integrated | st@@ | </s> | </s> | roof | por@@ | n | , | two | horses | , | was | not | easy | to | secure | . | </s>|
| full sent tgt |  |  | the | building | , | a | workshop | with | integrated | stab@@ | for | two | horse | bar@@ | n | for | two | horses | , | was | not | easy | to | secure | . | </s>|
| ref | the | building | , | a | workshop | with | integrated | stab@@ | ling | for | two | horses | , | was | not | easy | to | secure | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | es | lager@@ | te | viel | holz | und | auch | stro@@ | h@@ | b@@ | allen | darin | .|
| waitk tgt |  |  | it | was | a | lot | of | wood | and | also | stra@@ | w | bal@@ | es | in | it | . | </s>|
| waitk prob |  |  | 0.39 | 0.32 | 0.12 | 0.89 | 0.90 | 0.76 | 0.63 | 0.49 | 0.47 | 0.87 | 0.73 | 0.84 | 0.36 | 0.54 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.64 | 0.24 | 0.08 | 0.34 | 0.91 | 0.76 | 0.57 | 0.39 | 0.13 | 0.77 | 0.32 | 0.83 | 0.21 | 0.83 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.39 | -4.24 | -4.24 | -3.80 | -1.61 | -1.70 | -2.48 | -2.72 | -4.01 | -2.03 | -3.51 | -1.73 | -2.86 | -1.53 | -1.65 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.77 | -3.35 | -4.79 | -1.11 | -1.66 | -2.19 | -2.16 | -2.28 | -3.06 | -1.09 | -2.07 | -1.81 | -2.85 | -2.30 | -1.61 | -1.65|
| full sent prob |  |  | 0.25 | 0.10 | 0.07 | 0.08 | 0.91 | 0.86 | 0.62 | 0.63 | 0.10 | 0.93 | 0.37 | 0.87 | 0.25 | 0.83 | 0.91 | 0.92|
| full sent rank |  |  | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.54 | -3.93 | -4.83 | -4.28 | -1.64 | -1.42 | -2.27 | -2.56 | -4.39 | -1.06 | -3.77 | -1.53 | -2.73 | -1.59 | -1.64 | -1.56|
| full sent KL (full->waitk) |  |  | -3.65 | -3.33 | -4.79 | -0.92 | -1.66 | -2.25 | -2.20 | -2.34 | -3.05 | -1.21 | -2.10 | -1.84 | -2.87 | -2.30 | -1.61 | -1.64|
| dec-waitktgt |  |  | it | was | stor@@ | lot | of | wood | and | also | stal@@ | w | bal@@ | es | . | it | . | </s>|
| full sent tgt |  |  | it | had | a | place | of | wood | and | also | stal@@ | w | bal@@ | es | . | it | . | </s>|
| ref | there | were | large | quantities | of | wood | and | bal@@ | es | of | stra@@ | w | stored | inside | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | erste | lö@@ | sch@@ | angriff | erfol@@ | gte | über | den | tan@@ | k | im | fahrzeug | .|
| waitk tgt |  |  | the | first | ext@@ | ingu@@ | ishing | attack | was | made | via | the | tan@@ | k | in | the | vehicle | . | </s>|
| waitk prob |  |  | 0.71 | 0.85 | 0.52 | 0.82 | 0.76 | 0.81 | 0.49 | 0.20 | 0.18 | 0.81 | 0.61 | 0.91 | 0.74 | 0.90 | 0.76 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.73 | 0.90 | 0.75 | 0.94 | 0.81 | 0.73 | 0.14 | 0.03 | 0.36 | 0.83 | 0.82 | 0.94 | 0.78 | 0.89 | 0.82 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.40 | -1.59 | -1.92 | -1.17 | -1.52 | -2.15 | -3.82 | -3.74 | -3.02 | -2.00 | -1.63 | -1.28 | -1.88 | -1.69 | -1.33 | -1.74 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.69 | -1.96 | -3.09 | -1.56 | -1.60 | -1.93 | -2.43 | -3.86 | -3.39 | -1.84 | -2.56 | -1.49 | -2.10 | -1.57 | -1.90 | -1.69 | -1.66|
| full sent prob |  |  | 0.71 | 0.93 | 0.63 | 0.90 | 0.77 | 0.80 | 0.29 | 0.06 | 0.37 | 0.87 | 0.93 | 0.94 | 0.78 | 0.89 | 0.82 | 0.90 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.65 | -1.28 | -2.64 | -1.27 | -1.57 | -1.91 | -2.68 | -3.18 | -2.88 | -1.73 | -1.05 | -1.23 | -1.93 | -1.67 | -1.36 | -1.71 | -1.58|
| full sent KL (full->waitk) |  |  | -2.68 | -1.99 | -3.04 | -1.54 | -1.58 | -1.97 | -2.50 | -3.87 | -3.39 | -1.86 | -2.61 | -1.49 | -2.10 | -1.57 | -1.90 | -1.70 | -1.66|
| dec-waitktgt |  |  | the | first | ext@@ | ingu@@ | ishing | attack | took | done | via | the | tan@@ | k | in | the | vehicle | . | </s>|
| full sent tgt |  |  | the | first | ext@@ | ingu@@ | ishing | attack | was | carried | via | the | tan@@ | k | in | the | vehicle | . | </s>|
| ref | the | first | attempt | to | ext@@ | ingu@@ | ish | the | fire | was | made | using | the | tan@@ | k | on | the | fire | engine | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | eine | weitere | leitung | erfol@@ | gte | über | einen | über@@ | fl@@ | ur@@ | - | hy@@ | d@@ | ran@@ | ten | in | rund | 100 | meter | entfernung | .|
| waitk tgt |  |  | another | management | was | the | creation | of | a | large | over@@ | hau@@ | l | and | hy@@ | dr@@ | ant | in | about | 100 | metres | distance | . | </s>|
| waitk prob |  |  | 0.50 | 0.19 | 0.54 | 0.11 | 0.03 | 0.85 | 0.53 | 0.02 | 0.05 | 0.14 | 0.97 | 0.08 | 0.61 | 0.67 | 0.40 | 0.45 | 0.45 | 0.92 | 0.42 | 0.38 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.55 | 0.02 | 0.01 | 0.01 | 0.00 | 0.67 | 0.45 | 0.00 | 0.08 | 0.01 | 0.95 | 0.01 | 0.08 | 0.16 | 0.39 | 0.28 | 0.27 | 0.90 | 0.39 | 0.02 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 8 | 7 | 18 | 46 | 0 | 0 | 31 | 1 | 9 | 0 | 9 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.62 | -3.73 | -3.83 | -3.29 | -6.12 | -3.07 | -2.67 | -5.09 | -5.47 | -2.73 | -1.28 | -3.54 | -3.45 | -1.55 | -3.79 | -3.71 | -3.20 | -1.49 | -1.55 | -1.69 | -1.74 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.02 | -3.96 | -2.63 | -4.74 | -6.28 | -1.75 | -2.49 | -5.84 | -5.52 | -4.02 | -1.05 | -4.95 | -2.30 | -1.73 | -3.76 | -3.67 | -2.73 | -1.31 | -2.14 | -2.26 | -1.75 | -1.63|
| full sent prob |  |  | 0.21 | 0.01 | 0.34 | 0.02 | 0.00 | 0.88 | 0.29 | 0.00 | 0.19 | 0.01 | 0.97 | 0.00 | 0.46 | 0.34 | 0.69 | 0.12 | 0.48 | 0.89 | 0.39 | 0.29 | 0.89 | 0.92|
| full sent rank |  |  | 1 | 1 | 0 | 8 | 369 | 0 | 1 | 51 | 0 | 10 | 0 | 6 | 0 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.42 | -2.55 | -3.99 | -4.13 | -4.37 | -1.77 | -2.16 | -3.75 | -4.05 | -3.18 | -1.04 | -1.07 | -3.19 | -1.64 | -2.29 | -3.51 | -2.57 | -1.51 | -1.72 | -2.86 | -1.74 | -1.56|
| full sent KL (full->waitk) |  |  | -2.90 | -3.99 | -2.78 | -4.73 | -6.28 | -1.89 | -2.46 | -5.84 | -5.53 | -4.02 | -1.07 | -4.98 | -2.48 | -1.80 | -3.85 | -3.61 | -2.80 | -1.31 | -2.13 | -2.31 | -1.75 | -1.62|
| dec-waitktgt |  |  | another | line | </s> | done | one | of | a | super@@ | super@@ | floor | l | . | a | d@@ | ant | in | about | 100 | meters | . | . | </s>|
| full sent tgt |  |  | the | line | was | carried | over@@ | of | an | hy@@ | over@@ | floor | l | hy@@ | hy@@ | d@@ | ant | at | about | 100 | meters | distance | . | </s>|
| ref | another | line | was | taken | from | the | surface | hy@@ | dr@@ | ant | around | 100 | metres | away | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zum | einsatz | kam | auch | im | gebäude | ein | ho@@ | hl@@ | strahl@@ | ro@@ | hr | .|
| waitk tgt |  |  | the | new | version | of | the | new | version | of | the | new | version | of | the | original | version | of | the | original | version | of | the | original | version | was | released | . | </s>|
| waitk prob |  |  | 0.21 | 0.04 | 0.03 | 0.34 | 0.55 | 0.05 | 0.03 | 0.25 | 0.50 | 0.04 | 0.08 | 0.21 | 0.45 | 0.04 | 0.11 | 0.18 | 0.47 | 0.07 | 0.14 | 0.19 | 0.51 | 0.09 | 0.15 | 0.18 | 0.12 | 0.31 | 0.90|
| dec-waitk prob |  |  | 0.23 | 0.00 | 0.03 | 0.07 | 0.60 | 0.00 | 0.01 | 0.08 | 0.63 | 0.01 | 0.04 | 0.10 | 0.48 | 0.01 | 0.09 | 0.14 | 0.46 | 0.01 | 0.13 | 0.14 | 0.47 | 0.02 | 0.16 | 0.25 | 0.07 | 0.53 | 0.91|
| dec-waitk rank |  |  | 0 | 203 | 0 | 3 | 0 | 10 | 12 | 2 | 0 | 16 | 0 | 2 | 0 | 15 | 0 | 2 | 0 | 7 | 0 | 1 | 0 | 5 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.52 | -4.81 | -6.18 | -3.11 | -3.13 | -4.55 | -5.33 | -3.01 | -2.52 | -5.69 | -5.68 | -3.74 | -3.83 | -5.59 | -5.42 | -3.54 | -3.94 | -5.41 | -5.24 | -3.44 | -3.90 | -5.30 | -5.07 | -3.36 | -4.93 | -2.70 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.76 | -6.37 | -6.28 | -3.61 | -3.62 | -6.05 | -6.07 | -3.88 | -3.96 | -6.01 | -5.84 | -3.89 | -4.16 | -5.93 | -5.65 | -3.70 | -4.04 | -5.77 | -5.44 | -3.66 | -3.82 | -5.67 | -5.28 | -3.67 | -4.52 | -3.01 | -1.72|
| full sent prob |  |  | 0.15 | 0.00 | 0.01 | 0.13 | 0.50 | 0.03 | 0.04 | 0.12 | 0.48 | 0.06 | 0.07 | 0.12 | 0.48 | 0.01 | 0.10 | 0.15 | 0.49 | 0.01 | 0.13 | 0.16 | 0.51 | 0.02 | 0.15 | 0.19 | 0.09 | 0.47 | 0.91|
| full sent rank |  |  | 1 | 16 | 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 14 | 0 | 1 | 0 | 8 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.68 | -6.01 | -6.10 | -3.96 | -3.64 | -6.00 | -5.86 | -3.91 | -3.82 | -5.73 | -5.72 | -3.89 | -3.76 | -5.56 | -5.44 | -3.71 | -3.74 | -5.42 | -5.32 | -3.66 | -3.70 | -5.27 | -5.22 | -3.64 | -4.96 | -2.89 | -1.64|
| full sent KL (full->waitk) |  |  | -4.75 | -6.37 | -6.28 | -3.61 | -3.57 | -6.05 | -6.07 | -3.87 | -3.90 | -6.02 | -5.84 | -3.88 | -4.16 | -5.93 | -5.65 | -3.70 | -4.05 | -5.77 | -5.44 | -3.66 | -3.84 | -5.67 | -5.27 | -3.67 | -4.52 | -3.00 | -1.71|
| dec-waitktgt |  |  | the | use | version | was | the | ho@@ | building | was | the | building | version | is | the | system | version | is | the | new | version | was | the | new | version | was | released | . | </s>|
| full sent tgt |  |  | a | building | model | of | the | new | version | is | the | new | version | is | the | new | version | is | the | new | version | of | the | new | version | was | released | . | </s>|
| ref | a | hol@@ | low-@@ | stream | no@@ | zz@@ | le | in | the | building | was | also | used | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | im | ernst@@ | fall | erfolgt | eine | unterstützung | über | die | tages@@ | einsatz@@ | gruppe | köni@@ | gs@@ | feld | .|
| waitk tgt |  |  | in | case | of | emergency | , | support | is | provided | via | the | kö@@ | ni@@ | gs@@ | fel@@ | d | daily | operation | group | . | </s>|
| waitk prob |  |  | 0.55 | 0.35 | 0.84 | 0.24 | 0.58 | 0.36 | 0.61 | 0.66 | 0.36 | 0.83 | 0.50 | 0.96 | 0.93 | 0.96 | 0.90 | 0.54 | 0.22 | 0.84 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.50 | 0.77 | 0.87 | 0.29 | 0.35 | 0.23 | 0.48 | 0.54 | 0.31 | 0.84 | 0.62 | 0.90 | 0.62 | 0.95 | 0.96 | 0.10 | 0.09 | 0.70 | 0.90 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.59 | -1.29 | -1.74 | -2.32 | -3.55 | -3.21 | -2.83 | -2.87 | -2.50 | -1.97 | -2.40 | -1.61 | -1.44 | -1.21 | -1.10 | -2.83 | -3.49 | -2.26 | -1.64 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.85 | -3.05 | -1.88 | -3.58 | -2.64 | -3.41 | -2.52 | -2.39 | -2.56 | -2.01 | -2.16 | -1.11 | -0.87 | -1.11 | -1.72 | -2.28 | -3.64 | -1.59 | -1.67 | -1.66|
| full sent prob |  |  | 0.57 | 0.32 | 0.90 | 0.36 | 0.59 | 0.48 | 0.42 | 0.64 | 0.39 | 0.86 | 0.57 | 0.92 | 0.60 | 0.96 | 0.96 | 0.10 | 0.09 | 0.76 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.90 | -3.08 | -1.60 | -2.75 | -2.43 | -2.21 | -2.64 | -2.39 | -2.19 | -1.82 | -2.47 | -1.43 | -1.50 | -1.18 | -1.08 | -2.12 | -3.47 | -2.23 | -1.66 | -1.60|
| full sent KL (full->waitk) |  |  | -2.88 | -2.92 | -1.90 | -3.59 | -2.75 | -3.48 | -2.50 | -2.44 | -2.59 | -2.03 | -2.13 | -1.13 | -0.86 | -1.12 | -1.72 | -2.29 | -3.65 | -1.63 | -1.67 | -1.65|
| dec-waitktgt |  |  | in | case | of | an | , | support | is | provided | via | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | operations | group | . | </s>|
| full sent tgt |  |  | in | case | of | emergency | , | support | is | provided | via | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | operations | group | . | </s>|
| ref | in | case | of | emergency | , | support | is | provided | by | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | time | task | force | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | komman@@ | dan@@ | t | zeigte | sich | mit | dem | ablauf | der | ü@@ | bung | zufrieden | .|
| waitk tgt |  |  | the | comm@@ | ander | was | very | familiar | with | the | course | of | the | exercise | . | </s>|
| waitk prob |  |  | 0.45 | 0.63 | 0.91 | 0.36 | 0.10 | 0.24 | 0.87 | 0.76 | 0.16 | 0.89 | 0.76 | 0.69 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.35 | 0.92 | 0.58 | 0.00 | 0.00 | 0.01 | 0.72 | 0.43 | 0.04 | 0.89 | 0.70 | 0.87 | 0.87 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 2 | 43 | 12 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.81 | -1.00 | -1.41 | -1.83 | -4.62 | -4.92 | -2.49 | -3.58 | -5.12 | -1.71 | -2.39 | -1.36 | -1.87 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.70 | -3.11 | -1.00 | -3.63 | -5.18 | -3.69 | -1.63 | -2.17 | -4.13 | -1.80 | -2.18 | -2.39 | -1.72 | -1.66|
| full sent prob |  |  | 0.59 | 0.87 | 0.80 | 0.46 | 0.01 | 0.00 | 0.91 | 0.77 | 0.12 | 0.88 | 0.80 | 0.83 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 4 | 47 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.02 | -1.40 | -1.55 | -3.36 | -1.67 | -1.61 | -1.60 | -2.14 | -4.22 | -1.79 | -2.00 | -1.57 | -1.76 | -1.60|
| full sent KL (full->waitk) |  |  | -3.78 | -3.08 | -1.15 | -3.77 | -5.18 | -3.73 | -1.77 | -2.38 | -4.15 | -1.79 | -2.24 | -2.37 | -1.73 | -1.65|
| dec-waitktgt |  |  | the | comm@@ | ander | </s> | with | happy | with | the | way | of | the | exercise | . | </s>|
| full sent tgt |  |  | the | comm@@ | ander | was | satisfied | satisfied | with | the | course | of | the | exercise | . | </s>|
| ref | the | comm@@ | ander | expressed | his | satisfaction | following | the | exercise | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dabei | zeigte | sich | wol@@ | f | beein@@ | druckt | über | die | modell@@ | projekte | zur | ausbildung | .|
| waitk tgt |  |  | the | first | of | these | was | the | first | model | of | the | new | generation | of | the | german | model | . | </s>|
| waitk prob |  |  | 0.16 | 0.03 | 0.03 | 0.36 | 0.33 | 0.34 | 0.02 | 0.02 | 0.05 | 0.45 | 0.03 | 0.03 | 0.40 | 0.13 | 0.05 | 0.03 | 0.15 | 0.90|
| dec-waitk prob |  |  | 0.08 | 0.00 | 0.01 | 0.68 | 0.48 | 0.13 | 0.02 | 0.03 | 0.00 | 0.46 | 0.01 | 0.02 | 0.27 | 0.05 | 0.02 | 0.07 | 0.20 | 0.91|
| dec-waitk rank |  |  | 3 | 20 | 7 | 0 | 0 | 1 | 0 | 0 | 14 | 0 | 3 | 2 | 0 | 0 | 3 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.19 | -5.05 | -5.40 | -1.97 | -3.57 | -4.01 | -6.42 | -6.12 | -2.96 | -2.48 | -5.41 | -5.65 | -4.11 | -5.97 | -6.16 | -5.72 | -4.74 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.88 | -6.34 | -6.03 | -2.67 | -4.33 | -4.08 | -6.42 | -6.17 | -5.70 | -4.04 | -6.30 | -6.09 | -3.86 | -5.85 | -6.10 | -5.99 | -4.91 | -1.72|
| full sent prob |  |  | 0.01 | 0.03 | 0.01 | 0.39 | 0.16 | 0.26 | 0.02 | 0.01 | 0.01 | 0.42 | 0.02 | 0.02 | 0.34 | 0.06 | 0.02 | 0.08 | 0.07 | 0.91|
| full sent rank |  |  | 2 | 3 | 7 | 0 | 0 | 0 | 1 | 3 | 10 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -1.08 | -5.88 | -5.87 | -3.13 | -5.06 | -4.54 | -6.33 | -6.06 | -4.01 | -3.40 | -6.09 | -5.85 | -4.09 | -5.99 | -6.22 | -5.74 | -4.59 | -1.65|
| full sent KL (full->waitk) |  |  | -3.83 | -6.35 | -6.02 | -2.61 | -4.25 | -4.10 | -6.42 | -6.17 | -5.70 | -4.03 | -6.30 | -6.09 | -3.88 | -5.85 | -6.10 | -5.99 | -4.90 | -1.72|
| dec-waitktgt |  |  | that | cl@@ | time | these | was | wol@@ | first | model | projects | the | training | model | of | the | model | model | . | </s>|
| full sent tgt |  |  | wol@@ | film | time | these | was | the | german | german | training | the | training | model | of | the | german | model | series | </s>|
| ref | during | the | presentation | , | wol@@ | f | seemed | impres@@ | sed | by | the | educational | pilot | project | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | außerdem | lob@@ | te | er | die | familien@@ | freundlichkeit | im | land@@ | kreis | .|
| waitk tgt |  |  | i | also | p@@ | raised | the | family | friend@@ | liness | of | the | district | . | </s>|
| waitk prob |  |  | 0.36 | 0.52 | 0.52 | 0.80 | 0.71 | 0.42 | 0.53 | 0.91 | 0.49 | 0.79 | 0.38 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.00 | 0.58 | 0.79 | 0.79 | 0.67 | 0.12 | 0.82 | 0.86 | 0.48 | 0.85 | 0.26 | 0.86 | 0.92|
| dec-waitk rank |  |  | 21 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.76 | -2.78 | -1.85 | -1.41 | -2.40 | -4.02 | -1.40 | -1.59 | -2.22 | -1.86 | -2.78 | -1.91 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.86 | -2.86 | -2.10 | -1.17 | -2.43 | -2.55 | -3.29 | -1.34 | -2.12 | -2.22 | -2.31 | -1.80 | -1.66|
| full sent prob |  |  | 0.00 | 0.31 | 0.72 | 0.83 | 0.77 | 0.13 | 0.83 | 0.92 | 0.40 | 0.84 | 0.25 | 0.84 | 0.91|
| full sent rank |  |  | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.79 | -3.94 | -1.98 | -1.50 | -2.09 | -4.83 | -1.44 | -1.32 | -2.14 | -1.89 | -2.87 | -2.02 | -1.60|
| full sent KL (full->waitk) |  |  | -2.85 | -2.75 | -2.09 | -1.19 | -2.49 | -2.55 | -3.29 | -1.38 | -2.12 | -2.22 | -2.31 | -1.78 | -1.66|
| dec-waitktgt |  |  | moreover | also | p@@ | raised | the | kin@@ | friend@@ | liness | of | the | county | . | </s>|
| full sent tgt |  |  | he | also | p@@ | raised | the | family | friend@@ | liness | in | the | county | . | </s>|
| ref | he | also | p@@ | raised | the | family-@@ | friendly | approach | within | the | district | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | außerdem | führte | er | an | , | dass | sich | immer | mehr | beschäfti@@ | gte | um | die | pflege | und | betreuung | ihrer | an@@ | gehörigen | kü@@ | mm@@ | erten | .|
| waitk tgt |  |  | he | also | said | that | the | situation | is | becoming | more | and | more | concerned | with | care | for | and | care | for | their | families | . | </s>|
| waitk prob |  |  | 0.38 | 0.70 | 0.12 | 0.83 | 0.34 | 0.04 | 0.33 | 0.13 | 0.45 | 0.82 | 0.92 | 0.10 | 0.80 | 0.29 | 0.43 | 0.54 | 0.84 | 0.65 | 0.73 | 0.25 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.53 | 0.51 | 0.03 | 0.73 | 0.10 | 0.24 | 0.62 | 0.03 | 0.56 | 0.81 | 0.90 | 0.01 | 0.16 | 0.64 | 0.04 | 0.46 | 0.77 | 0.68 | 0.66 | 0.17 | 0.92 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 8 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.45 | -3.18 | -3.00 | -2.54 | -5.19 | -5.08 | -2.50 | -2.37 | -2.71 | -2.10 | -1.67 | -4.93 | -2.76 | -2.31 | -1.69 | -3.03 | -2.02 | -2.15 | -2.64 | -2.44 | -1.55 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.34 | -2.22 | -3.56 | -1.95 | -4.13 | -6.13 | -3.29 | -3.95 | -2.82 | -2.03 | -1.45 | -5.15 | -1.36 | -3.22 | -2.25 | -2.96 | -1.67 | -1.85 | -2.23 | -3.19 | -1.67 | -1.67|
| full sent prob |  |  | 0.43 | 0.64 | 0.05 | 0.86 | 0.05 | 0.00 | 0.05 | 0.03 | 0.44 | 0.72 | 0.92 | 0.00 | 0.52 | 0.22 | 0.27 | 0.08 | 0.71 | 0.76 | 0.68 | 0.18 | 0.91 | 0.92|
| full sent rank |  |  | 0 | 0 | 5 | 0 | 3 | 88 | 5 | 3 | 0 | 0 | 0 | 100 | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.30 | -2.78 | -3.99 | -1.88 | -3.06 | -2.83 | -3.33 | -3.58 | -2.66 | -2.41 | -1.51 | -4.30 | -2.54 | -2.91 | -1.96 | -2.61 | -2.19 | -1.89 | -2.39 | -2.50 | -1.61 | -1.56|
| full sent KL (full->waitk) |  |  | -3.31 | -2.29 | -3.58 | -2.04 | -4.11 | -6.12 | -3.16 | -3.94 | -2.79 | -1.96 | -1.46 | -5.16 | -1.60 | -3.17 | -2.29 | -2.82 | -1.63 | -1.88 | -2.25 | -3.20 | -1.66 | -1.67|
| dec-waitktgt |  |  | he | also | mentioned | that | the | situation | is | increasing | more | and | more | . | . | care | and | and | care | for | their | loved | . | </s>|
| full sent tgt |  |  | he | also | mentioned | that | more | care | was | increasing | more | and | more | important | with | the | and | their | care | for | their | rela@@ | . | </s>|
| ref | he | also | stated | that | an | increasing | number | of | employed | persons | are | looking | after | the | long-term | care | and | support | of | rela@@ | tives | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | aber | niemand | könne | es | sich | leisten | , | qualifizi@@ | erte | arbeitskrä@@ | fte | zu | verlieren | , | sagte | er | weiter | .|
| waitk tgt |  |  | but | no | one | can | afford | to | buy | skilled | workers | . | </s>|
| waitk prob |  |  | 0.61 | 0.54 | 0.92 | 0.81 | 0.98 | 0.88 | 0.05 | 0.41 | 0.33 | 0.29 | 0.91|
| dec-waitk prob |  |  | 0.55 | 0.48 | 0.93 | 0.73 | 0.96 | 0.13 | 0.02 | 0.13 | 0.26 | 0.03 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 1 | 2 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.76 | -1.90 | -1.38 | -1.70 | -1.18 | -1.85 | -5.06 | -3.34 | -2.28 | -1.25 | -1.46|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.58 | -1.79 | -1.46 | -1.67 | -0.93 | -1.18 | -4.80 | -2.85 | -2.56 | -2.72 | -1.66|
| full sent prob |  |  | 0.74 | 0.73 | 0.92 | 0.61 | 0.97 | 0.87 | 0.00 | 0.31 | 0.32 | 0.00 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 19 | 0 | 0 | 16 | 0|
| full sent KL (waitk->full) |  |  | -2.04 | -1.61 | -1.45 | -1.87 | -1.08 | -1.86 | -1.32 | -2.93 | -2.34 | -2.25 | -1.58|
| full sent KL (full->waitk) |  |  | -2.67 | -1.85 | -1.46 | -1.60 | -0.94 | -1.72 | -4.80 | -2.94 | -2.56 | -2.85 | -1.65|
| dec-waitktgt |  |  | but | no | one | can | afford | it | do | a | labor | </s> | </s>|
| full sent tgt |  |  | but | no | one | can | afford | to | lose | skilled | workers | , | </s>|
| ref | however | , | nobody | can | afford | to | lose | qualified | workers | , | &quot; | he | added | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ein | weiterer | , | besonders | wichtiger | faktor | sei | die | ver@@ | ne@@ | tzung | von | hoch@@ | schulen | und | unternehmen | .|
| waitk tgt |  |  | another | aspect | of | the | report | is | the | net@@ | working | of | high-@@ | level | and | enterprise | . | </s>|
| waitk prob |  |  | 0.63 | 0.11 | 0.21 | 0.32 | 0.15 | 0.27 | 0.48 | 0.16 | 0.93 | 0.85 | 0.38 | 0.16 | 0.21 | 0.18 | 0.71 | 0.91|
| dec-waitk prob |  |  | 0.59 | 0.00 | 0.05 | 0.03 | 0.02 | 0.05 | 0.02 | 0.05 | 0.93 | 0.39 | 0.04 | 0.26 | 0.06 | 0.02 | 0.82 | 0.92|
| dec-waitk rank |  |  | 0 | 16 | 4 | 3 | 8 | 3 | 6 | 3 | 0 | 0 | 4 | 0 | 1 | 6 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.42 | -2.43 | -2.57 | -2.63 | -3.34 | -2.47 | -2.33 | -3.55 | -1.09 | -2.66 | -3.59 | -3.15 | -3.25 | -3.74 | -1.81 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.58 | -4.09 | -2.56 | -3.78 | -4.48 | -2.79 | -3.03 | -4.60 | -1.20 | -1.44 | -2.77 | -3.99 | -3.68 | -4.10 | -2.62 | -1.66|
| full sent prob |  |  | 0.68 | 0.04 | 0.31 | 0.02 | 0.00 | 0.03 | 0.47 | 0.29 | 0.91 | 0.86 | 0.00 | 0.09 | 0.20 | 0.04 | 0.66 | 0.92|
| full sent rank |  |  | 0 | 4 | 0 | 2 | 49 | 3 | 0 | 0 | 0 | 0 | 40 | 2 | 1 | 3 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.19 | -2.77 | -2.36 | -1.91 | -3.16 | -2.64 | -2.68 | -3.63 | -1.38 | -1.79 | -1.89 | -3.72 | -2.91 | -3.74 | -2.65 | -1.57|
| full sent KL (full->waitk) |  |  | -2.62 | -4.09 | -2.58 | -3.78 | -4.46 | -2.76 | -3.21 | -4.63 | -1.19 | -1.76 | -2.83 | -3.97 | -3.71 | -4.11 | -2.52 | -1.65|
| dec-waitktgt |  |  | another | , | , | particular | greatest | , | particularly | importance | working | of | the | level | schools | corporate | . | </s>|
| full sent tgt |  |  | another | factor | of | particular | greatest | , | the | net@@ | working | of | universities | schools | schools | corporate | . | </s>|
| ref | another | , | particularly | important | factor | is | that | of | net@@ | working | between | universities | and | companies | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | denn | nur | wenn | ausreichend | aus@@ | bild@@ | ungsp@@ | lätze | angeboten | würden | , | könne | auch | der | fach@@ | kräf@@ | te@@ | bedarf | ge@@ | deckt | werden | .|
| waitk tgt |  |  | only | if | there | is | sufficient | training | places | available | can | the | european | court | of | justice | be | able | to | cover | the | needs | of | skilled | workers | . | </s>|
| waitk prob |  |  | 0.33 | 0.48 | 0.29 | 0.67 | 0.61 | 0.78 | 0.47 | 0.45 | 0.17 | 0.24 | 0.07 | 0.08 | 0.89 | 0.40 | 0.19 | 0.58 | 0.89 | 0.69 | 0.50 | 0.30 | 0.73 | 0.20 | 0.67 | 0.82 | 0.91|
| dec-waitk prob |  |  | 0.84 | 0.57 | 0.01 | 0.78 | 0.41 | 0.74 | 0.06 | 0.20 | 0.00 | 0.02 | 0.00 | 0.00 | 0.36 | 0.00 | 0.27 | 0.09 | 0.83 | 0.04 | 0.65 | 0.13 | 0.75 | 0.28 | 0.86 | 0.84 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 4 | 0 | 0 | 0 | 1 | 1 | 42 | 7 | 16 | 23 | 0 | 36 | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.31 | -2.49 | -1.51 | -1.85 | -1.72 | -2.19 | -3.14 | -2.18 | -1.99 | -4.66 | -6.29 | -4.81 | -3.70 | -5.16 | -4.43 | -4.43 | -2.21 | -2.62 | -2.52 | -3.90 | -2.04 | -3.36 | -1.27 | -1.95 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.42 | -2.33 | -2.73 | -1.92 | -1.84 | -1.93 | -2.92 | -2.82 | -3.03 | -3.66 | -5.86 | -4.84 | -1.32 | -2.59 | -4.14 | -2.51 | -1.72 | -1.49 | -2.85 | -2.36 | -1.98 | -3.74 | -2.06 | -1.92 | -1.63|
| full sent prob |  |  | 0.42 | 0.57 | 0.10 | 0.09 | 0.46 | 0.74 | 0.08 | 0.76 | 0.57 | 0.55 | 0.00 | 0.00 | 0.53 | 0.16 | 0.08 | 0.48 | 0.90 | 0.15 | 0.79 | 0.10 | 0.71 | 0.40 | 0.70 | 0.81 | 0.92|
| full sent rank |  |  | 0 | 0 | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 2309 | 100 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.07 | -2.39 | -2.81 | -2.16 | -1.95 | -2.27 | -3.77 | -1.49 | -2.04 | -2.62 | -3.15 | -4.72 | -3.26 | -2.97 | -3.40 | -3.06 | -1.68 | -3.18 | -1.93 | -3.36 | -1.88 | -2.77 | -1.90 | -2.01 | -1.56|
| full sent KL (full->waitk) |  |  | -3.32 | -2.33 | -2.73 | -1.57 | -1.85 | -1.93 | -2.92 | -3.02 | -3.14 | -3.75 | -5.86 | -4.84 | -1.44 | -2.71 | -4.12 | -2.69 | -1.77 | -1.54 | -2.91 | -2.39 | -1.97 | -3.76 | -1.97 | -1.89 | -1.63|
| dec-waitktgt |  |  | only | if | enough | is | sufficient | training | place | . | </s> | we | </s> | training | of | health | be | able | to | meet | the | demand | of | skilled | workers | . | </s>|
| full sent tgt |  |  | only | if | adequate | were | sufficient | training | place | available | can | the | need | skilled | of | auditors | also | able | to | meet | the | need | of | skilled | workers | . | </s>|
| ref | for | it | is | only | if | a | sufficient | number | of | educational | places | can | be | provided | that | the | need | for | skilled | workers | can | be | covered | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | früher | wurden | die | älteren | mit@@ | bürger | in | der | ra@@ | st@@ | stä@@ | tte | be@@ | wir@@ | tet | .|
| waitk tgt |  |  | in | the | past | , | the | elderly | were | often | left | in | the | re@@ | sting | place | . | </s>|
| waitk prob |  |  | 0.24 | 0.73 | 0.61 | 0.75 | 0.47 | 0.63 | 0.45 | 0.05 | 0.05 | 0.42 | 0.58 | 0.22 | 0.77 | 0.52 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.08 | 0.79 | 0.73 | 0.69 | 0.31 | 0.64 | 0.17 | 0.00 | 0.04 | 0.71 | 0.68 | 0.12 | 0.95 | 0.52 | 0.89 | 0.92|
| dec-waitk rank |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 94 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.31 | -2.04 | -2.03 | -2.56 | -3.18 | -1.79 | -3.15 | -4.82 | -4.83 | -1.93 | -2.20 | -4.79 | -0.96 | -2.95 | -1.76 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.68 | -2.27 | -2.47 | -2.11 | -3.19 | -2.65 | -2.91 | -5.30 | -5.27 | -3.14 | -2.84 | -4.53 | -1.65 | -2.66 | -1.74 | -1.65|
| full sent prob |  |  | 0.35 | 0.72 | 0.86 | 0.53 | 0.55 | 0.62 | 0.43 | 0.00 | 0.00 | 0.39 | 0.79 | 0.27 | 0.90 | 0.49 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 83 | 162 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.36 | -2.37 | -1.39 | -2.42 | -2.66 | -2.24 | -3.44 | -4.50 | -4.43 | -3.20 | -2.02 | -4.00 | -1.24 | -3.15 | -1.84 | -1.58|
| full sent KL (full->waitk) |  |  | -3.74 | -2.22 | -2.53 | -2.03 | -3.28 | -2.64 | -2.99 | -5.30 | -5.27 | -3.04 | -2.89 | -4.56 | -1.62 | -2.65 | -1.73 | -1.65|
| dec-waitktgt |  |  | the | the | past | , | the | elderly | became | the | the | in | the | re@@ | sting | place | . | </s>|
| full sent tgt |  |  | in | the | past | , | the | elderly | were | treated | treated | in | the | re@@ | sting | place | . | </s>|
| ref | previously | , | the | elderly | citizens | were | ho@@ | sted | in | the | service | station | can@@ | teen | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | mittlerweile | findet | dieser | nachmittag | im | pf@@ | le@@ | gehei@@ | m | st. | jo@@ | se@@ | f | statt | .|
| waitk tgt |  |  | in | the | meantime | , | this | afternoon | is | taking | place | in | the | fo@@ | ster | home | of | st. | jo@@ | se@@ | f | . | </s>|
| waitk prob |  |  | 0.11 | 0.74 | 0.91 | 0.53 | 0.49 | 0.91 | 0.20 | 0.24 | 0.92 | 0.64 | 0.78 | 0.18 | 0.76 | 0.15 | 0.63 | 0.75 | 0.53 | 0.94 | 0.94 | 0.86 | 0.91|
| dec-waitk prob |  |  | 0.05 | 0.83 | 0.93 | 0.50 | 0.56 | 0.90 | 0.30 | 0.27 | 0.93 | 0.70 | 0.80 | 0.03 | 0.93 | 0.10 | 0.61 | 0.82 | 0.59 | 0.95 | 0.97 | 0.89 | 0.92|
| dec-waitk rank |  |  | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.33 | -1.77 | -1.15 | -2.40 | -2.72 | -1.55 | -2.81 | -3.80 | -1.29 | -2.11 | -1.95 | -4.63 | -1.18 | -4.64 | -2.19 | -1.39 | -2.27 | -1.23 | -1.11 | -1.70 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.98 | -2.27 | -1.28 | -2.77 | -2.88 | -1.45 | -3.52 | -3.27 | -1.51 | -1.79 | -1.98 | -3.79 | -2.41 | -4.49 | -2.49 | -1.51 | -2.23 | -1.29 | -1.37 | -1.99 | -1.66|
| full sent prob |  |  | 0.10 | 0.86 | 0.79 | 0.29 | 0.41 | 0.88 | 0.29 | 0.32 | 0.91 | 0.70 | 0.78 | 0.03 | 0.94 | 0.10 | 0.57 | 0.82 | 0.62 | 0.95 | 0.96 | 0.89 | 0.92|
| full sent rank |  |  | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.72 | -1.77 | -1.83 | -2.74 | -2.68 | -1.66 | -2.53 | -3.19 | -1.55 | -1.79 | -1.91 | -4.44 | -1.13 | -4.49 | -2.29 | -1.38 | -2.23 | -1.23 | -1.16 | -1.74 | -1.57|
| full sent KL (full->waitk) |  |  | -3.99 | -2.29 | -1.18 | -2.69 | -2.84 | -1.43 | -3.52 | -3.28 | -1.50 | -1.81 | -1.98 | -3.78 | -2.42 | -4.49 | -2.47 | -1.51 | -2.23 | -1.29 | -1.36 | -1.98 | -1.65|
| dec-waitktgt |  |  | meanwhile | the | meantime | , | this | afternoon | is | taking | place | in | the | st. | ster | \’ | of | st. | jo@@ | se@@ | f | . | </s>|
| full sent tgt |  |  | this | the | meantime | , | this | afternoon | is | taking | place | in | the | st. | ster | \’ | of | st. | jo@@ | se@@ | f | . | </s>|
| ref | the | coffee | afternoon | is | now | held | in | the | st. | jo@@ | se@@ | f | nur@@ | sing | home | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | heim@@ | bewohner | freu@@ | ten | sich | auf | die | le@@ | ck@@ | eren | ku@@ | chen | und | tor@@ | ten | .|
| waitk tgt |  |  | the | home | residents | were | happy | with | the | delicious | meals | of | the | ca@@ | kes | and | ca@@ | kes | . | </s>|
| waitk prob |  |  | 0.44 | 0.20 | 0.45 | 0.31 | 0.18 | 0.41 | 0.75 | 0.54 | 0.09 | 0.16 | 0.49 | 0.30 | 0.78 | 0.85 | 0.71 | 0.97 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.74 | 0.00 | 0.16 | 0.50 | 0.33 | 0.13 | 0.67 | 0.02 | 0.01 | 0.01 | 0.62 | 0.02 | 0.26 | 0.07 | 0.59 | 0.95 | 0.87 | 0.92|
| dec-waitk rank |  |  | 0 | 17 | 0 | 0 | 0 | 1 | 0 | 5 | 6 | 7 | 0 | 7 | 1 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.19 | -3.91 | -4.18 | -2.95 | -3.48 | -4.34 | -2.47 | -4.70 | -5.02 | -2.09 | -2.52 | -5.66 | -0.91 | -2.23 | -2.63 | -1.16 | -1.86 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.00 | -4.32 | -3.03 | -3.80 | -3.45 | -2.40 | -2.24 | -1.73 | -4.68 | -3.47 | -3.40 | -3.92 | -1.02 | -1.27 | -2.21 | -1.01 | -1.72 | -1.64|
| full sent prob |  |  | 0.58 | 0.01 | 0.51 | 0.32 | 0.16 | 0.33 | 0.75 | 0.57 | 0.00 | 0.00 | 0.52 | 0.85 | 0.61 | 0.81 | 0.60 | 0.95 | 0.89 | 0.92|
| full sent rank |  |  | 0 | 13 | 0 | 0 | 1 | 1 | 0 | 0 | 36 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.04 | -3.88 | -2.67 | -3.76 | -3.43 | -2.39 | -2.12 | -2.30 | -0.17 | -1.33 | -2.67 | -1.31 | -1.28 | -1.81 | -2.62 | -1.13 | -1.74 | -1.57|
| full sent KL (full->waitk) |  |  | -3.94 | -4.33 | -3.16 | -3.77 | -3.45 | -2.50 | -2.29 | -2.00 | -4.68 | -3.52 | -3.36 | -4.12 | -1.18 | -1.79 | -2.22 | -1.01 | -1.73 | -1.64|
| dec-waitktgt |  |  | the | inhabitants | residents | were | happy | to | the | lea@@ | food | . | the | day | ke | . | ca@@ | kes | . | </s>|
| full sent tgt |  |  | the | residents | residents | were | looking | to | the | delicious | ca@@ | and | the | ca@@ | kes | and | ca@@ | kes | . | </s>|
| ref | the | residents | of | the | home | were | delighted | with | the | delicious | ca@@ | kes | and | tar@@ | ts | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | eine | entscheidung | darüber | wird | voraus@@ | sichtlich | bereits | im | kommenden | jahr | fallen | .|
| waitk tgt |  |  | a | decision | on | this | is | expected | to | be | taken | as | early | as | next | year | . | </s>|
| waitk prob |  |  | 0.36 | 0.86 | 0.59 | 0.67 | 0.55 | 0.74 | 0.63 | 0.76 | 0.40 | 0.45 | 0.60 | 0.91 | 0.96 | 0.96 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.67 | 0.93 | 0.75 | 0.48 | 0.55 | 0.48 | 0.83 | 0.73 | 0.61 | 0.04 | 0.94 | 0.93 | 0.91 | 0.94 | 0.90 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.13 | -1.28 | -1.98 | -2.54 | -3.22 | -2.60 | -1.83 | -2.30 | -1.87 | -1.87 | -0.92 | -1.45 | -1.19 | -1.37 | -1.66 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.44 | -1.76 | -2.32 | -2.20 | -2.50 | -1.56 | -2.32 | -2.02 | -2.40 | -2.52 | -1.96 | -1.57 | -1.03 | -1.21 | -1.64 | -1.63|
| full sent prob |  |  | 0.41 | 0.92 | 0.70 | 0.71 | 0.46 | 0.67 | 0.88 | 0.62 | 0.56 | 0.05 | 0.93 | 0.93 | 0.93 | 0.95 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.76 | -1.43 | -2.07 | -2.14 | -2.86 | -1.92 | -1.62 | -2.54 | -2.12 | -2.01 | -0.98 | -1.44 | -1.14 | -1.31 | -1.68 | -1.59|
| full sent KL (full->waitk) |  |  | -3.39 | -1.75 | -2.30 | -2.32 | -2.50 | -1.67 | -2.34 | -1.95 | -2.39 | -2.52 | -1.95 | -1.57 | -1.04 | -1.21 | -1.64 | -1.62|
| dec-waitktgt |  |  | a | decision | on | this | is | expected | to | be | taken | next | early | as | next | year | . | </s>|
| full sent tgt |  |  | a | decision | on | this | is | expected | to | be | taken | next | early | as | next | year | . | </s>|
| ref | a | decision | is | expected | to | be | made | in | the | coming | year | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | tiefe | ri@@ | sse | in | einzelnen | st@@ | einen | zeugen | von | wi@@ | tter@@ | ungs@@ | schäden | , | jedoch | ist | die | mauer | derzeit | nicht | ein@@ | stur@@ | z@@ | gefährdet | .|
| waitk tgt |  |  | deep | cr@@ | acks | in | individual | br@@ | ic@@ | ks | bear | witness | to | weather | damage | , | but | the | wall | is | not | collap@@ | sing | at | the | moment | . | </s>|
| waitk prob |  |  | 0.83 | 0.72 | 0.97 | 0.72 | 0.48 | 0.41 | 0.92 | 0.98 | 0.18 | 0.97 | 0.90 | 0.34 | 0.55 | 0.78 | 0.48 | 0.78 | 0.91 | 0.79 | 0.63 | 0.11 | 0.89 | 0.66 | 0.45 | 0.68 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.91 | 0.51 | 0.90 | 0.43 | 0.42 | 0.01 | 0.85 | 0.96 | 0.00 | 0.98 | 0.90 | 0.60 | 0.79 | 0.29 | 0.65 | 0.80 | 0.89 | 0.79 | 0.83 | 0.09 | 0.94 | 0.52 | 0.41 | 0.78 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.24 | -2.08 | -1.36 | -3.21 | -3.12 | -2.91 | -1.42 | -1.21 | -1.14 | -0.93 | -1.70 | -2.62 | -1.87 | -3.00 | -2.37 | -2.10 | -1.64 | -2.04 | -1.76 | -3.27 | -1.08 | -2.42 | -1.98 | -1.55 | -1.64 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -1.88 | -2.14 | -0.95 | -2.26 | -2.91 | -2.12 | -1.13 | -0.95 | -3.64 | -1.01 | -1.64 | -2.93 | -3.33 | -1.75 | -2.51 | -2.36 | -1.41 | -2.09 | -2.77 | -4.47 | -1.36 | -2.24 | -1.97 | -1.79 | -1.64 | -1.65|
| full sent prob |  |  | 0.43 | 0.90 | 0.93 | 0.64 | 0.37 | 0.03 | 0.88 | 0.93 | 0.08 | 0.82 | 0.89 | 0.43 | 0.70 | 0.73 | 0.69 | 0.74 | 0.92 | 0.73 | 0.71 | 0.00 | 0.54 | 0.62 | 0.40 | 0.77 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 19 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.77 | -1.25 | -1.30 | -2.60 | -3.56 | -2.57 | -1.48 | -1.41 | -3.93 | -1.91 | -1.71 | -3.19 | -2.38 | -1.97 | -2.05 | -2.29 | -1.36 | -2.27 | -2.18 | -3.52 | -1.88 | -2.42 | -1.94 | -1.55 | -1.65 | -1.60|
| full sent KL (full->waitk) |  |  | -1.55 | -2.36 | -0.97 | -2.38 | -2.88 | -2.15 | -1.15 | -0.93 | -3.69 | -0.89 | -1.64 | -2.89 | -3.30 | -2.04 | -2.53 | -2.32 | -1.44 | -2.05 | -2.71 | -4.45 | -1.08 | -2.29 | -1.97 | -1.79 | -1.64 | -1.64|
| dec-waitktgt |  |  | deep | cr@@ | acks | in | individual | stones | ic@@ | ks | </s> | witness | to | weather | damage | . | but | the | wall | is | not | cr@@ | sing | at | the | moment | . | </s>|
| full sent tgt |  |  | deep | cr@@ | acks | in | individual | stones | ic@@ | ks | are | witness | to | weather | damage | , | but | the | wall | is | not | in | sing | at | the | moment | . | </s>|
| ref | deep | cr@@ | acks | in | a | number | of | individual | stones | testi@@ | fy | to | the | weather | damage | , | however | , | at | present | the | wall | is | not | in | danger | of | collapse | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ö@@ | z@@ | de@@ | mir | will | ja@@ | zz@@ | ausbildung | in | st@@ | utt@@ | gar@@ | t | erhalten|
| waitk tgt |  |  | ö@@ | z@@ | dem@@ | ir | wants | to | train | jazz | in | stutt@@ | gart | . | </s>|
| waitk prob |  |  | 0.77 | 0.94 | 0.95 | 0.99 | 0.38 | 0.75 | 0.30 | 0.72 | 0.80 | 0.95 | 0.93 | 0.33 | 0.90|
| dec-waitk prob |  |  | 0.35 | 0.96 | 0.96 | 0.92 | 0.00 | 0.77 | 0.04 | 0.36 | 0.41 | 0.99 | 0.97 | 0.03 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 8 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.83 | -1.07 | -1.06 | -1.46 | -2.18 | -2.01 | -4.79 | -3.54 | -3.48 | -0.89 | -1.02 | -1.43 | -1.47|
| dec-waitk KL (dec-waitk->waitk) |  |  | -1.93 | -1.35 | -1.21 | -0.87 | -2.89 | -2.06 | -3.70 | -2.03 | -1.67 | -1.25 | -1.40 | -2.42 | -1.69|
| full sent prob |  |  | 0.86 | 0.96 | 0.95 | 0.97 | 0.40 | 0.91 | 0.00 | 0.84 | 0.79 | 1.00 | 0.96 | 0.01 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -1.69 | -1.18 | -1.23 | -1.07 | -2.89 | -1.47 | -2.41 | -1.53 | -2.19 | -0.84 | -1.13 | -1.66 | -1.52|
| full sent KL (full->waitk) |  |  | -2.25 | -1.34 | -1.19 | -0.92 | -3.04 | -2.14 | -3.69 | -2.31 | -1.93 | -1.25 | -1.39 | -2.42 | -1.69|
| dec-waitktgt |  |  | ö@@ | z@@ | dem@@ | ir | </s> | to | be | jazz | in | stutt@@ | gart | </s> | </s>|
| full sent tgt |  |  | ö@@ | z@@ | dem@@ | ir | wants | to | receive | jazz | in | stutt@@ | gart | </s> | </s>|
| ref | ö@@ | z@@ | dem@@ | ir | wants | jazz | training | in | stutt@@ | gart | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ja@@ | z@@ | z | und | klassi@@ | k | gehören | gerade | am | ja@@ | zz@@ | standort | st@@ | utt@@ | gar@@ | t | zusammen | .|
| waitk tgt |  |  | jazz | and | classical | music | are | just | at | the | jazz | site | in | stutt@@ | gart | . | </s>|
| waitk prob |  |  | 0.70 | 0.86 | 0.72 | 0.54 | 0.49 | 0.42 | 0.15 | 0.61 | 0.39 | 0.17 | 0.55 | 0.98 | 0.85 | 0.50 | 0.91|
| dec-waitk prob |  |  | 0.96 | 0.70 | 0.61 | 0.01 | 0.02 | 0.44 | 0.07 | 0.46 | 0.25 | 0.06 | 0.20 | 0.98 | 0.12 | 0.43 | 0.94|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -0.81 | -2.29 | -1.68 | -1.09 | -2.29 | -2.72 | -2.22 | -3.69 | -4.65 | -3.16 | -2.92 | -0.96 | -2.05 | -3.59 | -1.31|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.62 | -1.72 | -1.64 | -2.56 | -2.40 | -3.52 | -3.94 | -2.35 | -3.41 | -4.40 | -1.79 | -1.00 | -1.07 | -2.38 | -1.67|
| full sent prob |  |  | 0.86 | 0.87 | 0.58 | 0.32 | 0.56 | 0.04 | 0.01 | 0.85 | 0.62 | 0.18 | 0.13 | 0.99 | 0.96 | 0.76 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 4 | 9 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.46 | -1.84 | -2.06 | -3.20 | -2.59 | -3.28 | -3.96 | -1.52 | -2.63 | -3.25 | -1.38 | -0.95 | -1.07 | -2.21 | -1.57|
| full sent KL (full->waitk) |  |  | -2.56 | -1.84 | -1.62 | -2.72 | -2.62 | -3.39 | -3.93 | -2.55 | -3.53 | -4.43 | -1.81 | -1.00 | -1.61 | -2.52 | -1.65|
| dec-waitktgt |  |  | jazz | and | classical | </s> | </s> | just | right | the | jazz | scene | at | stutt@@ | gar@@ | . | </s>|
| full sent tgt |  |  | jazz | and | classical | music | are | currently | part | the | jazz | location | stutt@@ | stutt@@ | gart | . | </s>|
| ref | jazz | and | classical | music | belong | together | at | the | jazz | location | of | stutt@@ | gart | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | tun@@ | nel | war | den | angaben | zufolge | noch | nicht | in | gebrauch | genommen | worden | .|
| waitk tgt |  |  | the | tunnel | was | not | , | according | to | the | data | , | yet | in | use | . | </s>|
| waitk prob |  |  | 0.64 | 0.90 | 0.68 | 0.08 | 0.12 | 0.61 | 0.90 | 0.29 | 0.32 | 0.86 | 0.23 | 0.58 | 0.79 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.86 | 0.94 | 0.81 | 0.00 | 0.05 | 0.65 | 0.92 | 0.60 | 0.10 | 0.88 | 0.06 | 0.33 | 0.93 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 80 | 4 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.73 | -1.14 | -2.07 | -2.93 | -4.53 | -2.42 | -1.52 | -2.86 | -3.47 | -1.73 | -3.74 | -2.92 | -1.19 | -1.73 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.07 | -1.51 | -2.45 | -4.99 | -4.66 | -1.79 | -1.71 | -3.47 | -3.21 | -1.89 | -3.31 | -2.20 | -1.99 | -1.66 | -1.68|
| full sent prob |  |  | 0.28 | 0.75 | 0.20 | 0.21 | 0.07 | 0.57 | 0.91 | 0.64 | 0.18 | 0.89 | 0.05 | 0.25 | 0.95 | 0.90 | 0.92|
| full sent rank |  |  | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.50 | -2.49 | -2.62 | -3.80 | -2.87 | -2.29 | -1.65 | -2.45 | -2.71 | -1.71 | -2.41 | -2.14 | -1.08 | -1.70 | -1.57|
| full sent KL (full->waitk) |  |  | -2.77 | -1.37 | -2.14 | -5.00 | -4.66 | -1.77 | -1.70 | -3.48 | -3.25 | -1.90 | -3.35 | -2.20 | -2.00 | -1.66 | -1.67|
| dec-waitktgt |  |  | the | tunnel | was | the | in | according | to | the | figures | , | in | in | use | . | </s>|
| full sent tgt |  |  | according | tunnel | has | not | used | according | to | the | information | , | used | used | use | . | </s>|
| ref | according | to | the | details | provided | , | the | tunnel | had | not | yet | been | put | into | use | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sowohl | die | us-@@ | behörden | als | auch | die | mexi@@ | kanischen | sicherheit@@ | skrä@@ | fte | befinden | sich | in | einem | dauer@@ | -@@ | kampf | gegen | die | drogen@@ | kar@@ | t@@ | elle | .|
| waitk tgt |  |  | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | are | in | a | permanent | state | of | war | against | drug | car@@ | te@@ | ls | . | </s>|
| waitk prob |  |  | 0.78 | 0.77 | 0.89 | 0.72 | 0.90 | 0.76 | 0.86 | 0.96 | 0.90 | 0.90 | 0.91 | 0.80 | 0.55 | 0.61 | 0.51 | 0.78 | 0.40 | 0.30 | 0.45 | 0.60 | 0.91 | 0.96 | 0.98 | 0.92 | 0.91|
| dec-waitk prob |  |  | 0.72 | 0.76 | 0.90 | 0.91 | 0.91 | 0.43 | 0.96 | 0.97 | 0.79 | 0.94 | 0.79 | 0.16 | 0.72 | 0.09 | 0.75 | 0.19 | 0.76 | 0.45 | 0.00 | 0.24 | 0.55 | 0.24 | 0.98 | 0.88 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 9 | 1 | 0 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.39 | -1.78 | -1.46 | -1.23 | -1.63 | -1.99 | -0.95 | -1.08 | -1.93 | -1.24 | -1.96 | -3.33 | -2.44 | -1.58 | -1.77 | -2.86 | -2.08 | -2.57 | -1.54 | -3.35 | -3.16 | -2.28 | -0.97 | -1.85 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  | -1.96 | -1.99 | -1.56 | -2.49 | -1.63 | -1.90 | -1.72 | -1.17 | -1.51 | -1.55 | -1.29 | -1.47 | -3.08 | -2.51 | -2.94 | -1.68 | -3.27 | -3.60 | -2.31 | -1.59 | -1.14 | -0.55 | -0.98 | -1.54 | -1.64|
| full sent prob |  |  | 0.81 | 0.83 | 0.87 | 0.82 | 0.90 | 0.47 | 0.95 | 0.96 | 0.92 | 0.95 | 0.82 | 0.87 | 0.60 | 0.66 | 0.35 | 0.00 | 0.72 | 0.35 | 0.70 | 0.11 | 0.98 | 0.98 | 0.96 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 78 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.78 | -1.78 | -1.66 | -1.75 | -1.69 | -1.77 | -1.09 | -1.16 | -1.49 | -1.23 | -1.86 | -1.57 | -2.61 | -2.16 | -3.41 | -1.79 | -1.94 | -2.53 | -2.04 | -1.53 | -0.94 | -0.97 | -1.18 | -1.64 | -1.59|
| full sent KL (full->waitk) |  |  | -2.02 | -2.03 | -1.54 | -2.44 | -1.62 | -1.92 | -1.72 | -1.16 | -1.60 | -1.55 | -1.32 | -1.94 | -3.03 | -2.80 | -2.77 | -1.57 | -3.26 | -3.58 | -2.59 | -1.53 | -1.46 | -1.13 | -0.96 | -1.56 | -1.64|
| dec-waitktgt |  |  | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | </s> | in | one | permanent | one | of | war | </s> | drugs | car@@ | ts | ls | . | </s>|
| full sent tgt |  |  | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | are | in | a | permanent | fight | of | war | against | the | car@@ | te@@ | ls | . | </s>|
| ref | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | are | engaged | in | an | ongoing | battle | against | the | drug | car@@ | te@@ | ls | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | seit | 2006 | wurden | in | mexiko | mehr | als | 7@@ | 7. | 000 | menschen | im | zusammenhang | mit | der | drogen@@ | kriminalität | get@@ | ö@@ | tet | .|
| waitk tgt |  |  | since | 2006 | , | more | than | 7@@ | 7@@ | ,000 | people | have | been | killed | in | mexico | in | connection | with | drug | crime | . | </s>|
| waitk prob |  |  | 0.55 | 0.92 | 0.78 | 0.48 | 0.92 | 0.78 | 0.91 | 0.55 | 0.76 | 0.66 | 0.87 | 0.20 | 0.77 | 0.91 | 0.55 | 0.43 | 0.92 | 0.60 | 0.53 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.87 | 0.96 | 0.64 | 0.18 | 0.77 | 0.96 | 0.82 | 0.16 | 0.81 | 0.73 | 0.83 | 0.01 | 0.86 | 0.95 | 0.00 | 0.18 | 0.91 | 0.45 | 0.64 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 10 | 0 | 0 | 15 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.57 | -1.14 | -2.50 | -2.19 | -2.45 | -0.97 | -1.57 | -2.67 | -1.96 | -1.88 | -2.07 | -3.86 | -1.78 | -1.15 | -2.95 | -3.20 | -1.64 | -1.91 | -2.50 | -1.79 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.25 | -1.48 | -1.99 | -3.06 | -1.39 | -1.92 | -1.31 | -2.75 | -2.40 | -2.14 | -1.76 | -3.92 | -2.12 | -1.39 | -2.69 | -2.28 | -1.54 | -1.74 | -3.61 | -1.63 | -1.67|
| full sent prob |  |  | 0.49 | 0.87 | 0.66 | 0.51 | 0.93 | 0.82 | 0.90 | 0.84 | 0.88 | 0.91 | 0.89 | 0.91 | 0.88 | 0.92 | 0.63 | 0.54 | 0.92 | 0.33 | 0.69 | 0.91 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.21 | -1.83 | -2.04 | -1.61 | -1.47 | -1.51 | -1.33 | -1.52 | -1.50 | -1.27 | -1.58 | -0.84 | -1.68 | -1.42 | -2.58 | -1.98 | -1.50 | -1.87 | -2.26 | -1.64 | -1.56|
| full sent KL (full->waitk) |  |  | -3.07 | -1.41 | -1.99 | -3.13 | -1.51 | -1.84 | -1.38 | -3.03 | -2.44 | -2.23 | -1.80 | -4.07 | -2.13 | -1.37 | -2.98 | -2.37 | -1.55 | -1.71 | -3.63 | -1.65 | -1.66|
| dec-waitktgt |  |  | since | 2006 | , | mexico | than | 7@@ | 7@@ | 7@@ | people | have | been | living | in | mexico | . | the | with | drug | crime | . | </s>|
| full sent tgt |  |  | since | 2006 | , | more | than | 7@@ | 7@@ | ,000 | people | have | been | killed | in | mexico | in | connection | with | dru@@ | crime | . | </s>|
| ref | since | 2006 | , | more | than | 7@@ | 7@@ | ,000 | people | have | been | killed | in | conjunction | with | drug | crime | in | mexico | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | glei@@ | san@@ | lage | war | so | ausgestattet | , | dass | dort | elektri@@ | sch | betrie@@ | bene | wagen | eingesetzt | werden | konnten | .|
| waitk tgt |  |  | the | track | system | was | equipped | to | allow | the | installation | of | electr@@ | ically | operated | cars | . | </s>|
| waitk prob |  |  | 0.50 | 0.37 | 0.28 | 0.65 | 0.36 | 0.57 | 0.12 | 0.17 | 0.06 | 0.86 | 0.54 | 0.70 | 0.55 | 0.47 | 0.60 | 0.91|
| dec-waitk prob |  |  | 0.66 | 0.21 | 0.20 | 0.60 | 0.19 | 0.02 | 0.00 | 0.13 | 0.01 | 0.49 | 0.04 | 0.30 | 0.23 | 0.51 | 0.78 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 1 | 9 | 48 | 1 | 7 | 0 | 5 | 1 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.74 | -3.08 | -4.06 | -3.14 | -3.96 | -4.82 | -5.31 | -4.07 | -5.69 | -2.24 | -3.20 | -2.42 | -1.82 | -2.25 | -1.97 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.70 | -3.20 | -3.36 | -2.34 | -3.13 | -1.97 | -4.18 | -4.74 | -5.03 | -1.55 | -2.09 | -1.27 | -1.48 | -2.74 | -2.63 | -1.65|
| full sent prob |  |  | 0.60 | 0.32 | 0.37 | 0.79 | 0.63 | 0.44 | 0.05 | 0.14 | 0.01 | 0.88 | 0.26 | 0.70 | 0.55 | 0.55 | 0.85 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.00 | -2.88 | -2.96 | -1.94 | -2.13 | -2.56 | -4.18 | -3.34 | -1.32 | -1.77 | -1.86 | -1.84 | -1.49 | -2.25 | -1.68 | -1.59|
| full sent KL (full->waitk) |  |  | -3.68 | -3.22 | -3.40 | -2.45 | -3.26 | -2.19 | -4.19 | -4.75 | -5.07 | -1.83 | -2.21 | -1.45 | -1.57 | -2.75 | -2.66 | -1.65|
| dec-waitktgt |  |  | the | track | was | was | so | . | do | it | electric | of | electricity | ic@@ | powered | cars | . | </s>|
| full sent tgt |  |  | the | track | system | was | equipped | to | operate | electric | use | of | electric | ically | operated | cars | . | </s>|
| ref | the | railway | system | was | equipped | in | such | a | way | that | electr@@ | ically | powered | car@@ | ts | could | be | used | on | it | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | auf | mexi@@ | kan@@ | ischer | seite | liegt | der | zugang | in | einem | gebäude | , | das | 80 | meter | von | der | grenze | entfernt | ist | .|
| waitk tgt |  |  | on | mex@@ | ic@@ | an | side | , | access | is | in | a | building | that | is | 80 | meters | from | the | border | . | </s>|
| waitk prob |  |  | 0.11 | 0.40 | 0.97 | 0.89 | 0.68 | 0.51 | 0.59 | 0.70 | 0.46 | 0.80 | 0.82 | 0.30 | 0.38 | 0.87 | 0.46 | 0.65 | 0.87 | 0.77 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.06 | 0.66 | 0.97 | 0.85 | 0.36 | 0.01 | 0.01 | 0.19 | 0.09 | 0.62 | 0.86 | 0.29 | 0.32 | 0.81 | 0.47 | 0.49 | 0.81 | 0.83 | 0.90 | 0.93|
| dec-waitk rank |  |  | 2 | 0 | 0 | 0 | 0 | 2 | 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.45 | -1.30 | -1.09 | -1.68 | -3.80 | -1.57 | -3.21 | -3.24 | -4.98 | -2.71 | -1.71 | -3.82 | -4.02 | -1.92 | -1.56 | -2.67 | -1.93 | -1.81 | -1.71 | -1.47|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.73 | -2.58 | -1.08 | -1.55 | -2.60 | -2.37 | -2.84 | -1.99 | -3.41 | -1.91 | -2.02 | -3.68 | -3.47 | -1.50 | -1.80 | -2.02 | -1.78 | -2.12 | -1.68 | -1.65|
| full sent prob |  |  | 0.43 | 0.01 | 0.91 | 0.89 | 0.83 | 0.55 | 0.61 | 0.79 | 0.42 | 0.78 | 0.91 | 0.22 | 0.89 | 0.74 | 0.49 | 0.58 | 0.88 | 0.88 | 0.90 | 0.92|
| full sent rank |  |  | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.15 | -1.35 | -1.62 | -1.63 | -1.92 | -2.45 | -2.22 | -1.99 | -3.21 | -2.03 | -1.38 | -2.53 | -1.29 | -2.20 | -1.59 | -2.13 | -1.78 | -1.47 | -1.70 | -1.57|
| full sent KL (full->waitk) |  |  | -4.74 | -2.50 | -1.03 | -1.58 | -2.86 | -2.60 | -3.14 | -2.33 | -3.54 | -2.01 | -2.05 | -3.67 | -3.64 | -1.46 | -1.81 | -2.07 | -1.82 | -2.16 | -1.68 | -1.64|
| dec-waitktgt |  |  | mexico | mex@@ | ic@@ | an | side | </s> | </s> | </s> | </s> | a | building | that | is | 80 | meters | from | the | border | . | </s>|
| full sent tgt |  |  | on | the | ic@@ | an | side | , | access | is | in | a | building | 80 | is | 80 | meters | from | the | border | . | </s>|
| ref | on | the | mex@@ | ic@@ | an | side | , | the | entrance | is | located | in | a | building | located | 80 | metres | from | the | border | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | laut | behörden | führt | eine | leiter | 20 | meter | in | die | tiefe | zum | eigent@@ | lichen | tun@@ | n@@ | el@@ | eingang | .|
| waitk tgt |  |  | according | to | the | authorities | , | a | lad@@ | der | leads | 20 | metres | deep | to | the | actual | entrance | of | the | tunnel | . | </s>|
| waitk prob |  |  | 0.70 | 0.90 | 0.42 | 0.80 | 0.74 | 0.80 | 0.61 | 0.99 | 0.43 | 0.48 | 0.59 | 0.24 | 0.42 | 0.86 | 0.38 | 0.58 | 0.51 | 0.88 | 0.93 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.65 | 0.86 | 0.50 | 0.84 | 0.81 | 0.73 | 0.26 | 0.98 | 0.13 | 0.60 | 0.26 | 0.31 | 0.71 | 0.74 | 0.29 | 0.02 | 0.52 | 0.74 | 0.96 | 0.91 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.47 | -1.86 | -2.43 | -1.64 | -2.08 | -2.30 | -3.31 | -0.95 | -3.17 | -2.29 | -1.61 | -3.02 | -1.85 | -2.32 | -3.14 | -1.01 | -2.01 | -2.05 | -1.02 | -1.64 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.33 | -1.69 | -2.57 | -2.04 | -2.10 | -2.00 | -2.23 | -0.88 | -3.20 | -2.94 | -1.65 | -3.42 | -2.04 | -1.74 | -2.63 | -1.68 | -2.13 | -1.52 | -1.16 | -1.68 | -1.67|
| full sent prob |  |  | 0.68 | 0.91 | 0.59 | 0.81 | 0.73 | 0.78 | 0.36 | 0.99 | 0.12 | 0.63 | 0.28 | 0.25 | 0.49 | 0.80 | 0.39 | 0.03 | 0.55 | 0.77 | 0.96 | 0.90 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.46 | -1.62 | -2.31 | -1.90 | -2.08 | -2.01 | -3.28 | -0.92 | -3.23 | -2.14 | -1.49 | -3.04 | -1.87 | -2.14 | -2.90 | -1.14 | -2.10 | -1.98 | -1.00 | -1.66 | -1.57|
| full sent KL (full->waitk) |  |  | -2.35 | -1.72 | -2.60 | -2.02 | -2.06 | -2.03 | -2.28 | -0.89 | -3.20 | -2.95 | -1.66 | -3.42 | -2.03 | -1.78 | -2.66 | -1.68 | -2.16 | -1.54 | -1.17 | -1.68 | -1.66|
| dec-waitktgt |  |  | according | to | the | authorities | , | a | lad@@ | der | takes | 20 | meters | deep | to | the | tunnel | tunnel | of | the | tunnel | . | </s>|
| full sent tgt |  |  | according | to | the | authorities | , | a | lad@@ | der | takes | 20 | meters | deep | to | the | actual | tunnel | of | the | tunnel | . | </s>|
| ref | according | to | the | authorities | , | a | lad@@ | der | runs | 20 | metres | underground | to | the | actual | entrance | of | the | tunnel | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | tun@@ | nel | hat | einen | quer@@ | schnitt | von | 1,@@ | 20 | meter | höhe | und | 90 | z@@ | enti@@ | meter | breite | .|
| waitk tgt |  |  | the | tunnel | has | a | cross-@@ | section | of | 1.@@ | 20 | metres | and | 90 | in@@ | ches | of | width | . | </s>|
| waitk prob |  |  | 0.64 | 0.92 | 0.68 | 0.77 | 0.43 | 0.98 | 0.86 | 0.78 | 0.73 | 0.33 | 0.20 | 0.77 | 0.52 | 0.80 | 0.22 | 0.82 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.86 | 0.93 | 0.69 | 0.81 | 0.63 | 0.90 | 0.22 | 0.73 | 0.91 | 0.49 | 0.03 | 0.52 | 0.13 | 0.96 | 0.03 | 0.34 | 0.88 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 4 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.73 | -1.19 | -2.74 | -1.93 | -1.89 | -1.45 | -3.99 | -2.15 | -1.28 | -2.07 | -3.31 | -3.71 | -5.44 | -0.82 | -3.40 | -3.83 | -1.81 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.07 | -1.37 | -2.53 | -2.08 | -2.98 | -0.87 | -1.39 | -1.72 | -2.46 | -2.07 | -2.82 | -1.99 | -2.62 | -1.37 | -3.24 | -1.35 | -1.66 | -1.70|
| full sent prob |  |  | 0.70 | 0.86 | 0.67 | 0.83 | 0.39 | 0.98 | 0.88 | 0.84 | 0.88 | 0.31 | 0.17 | 0.06 | 0.04 | 0.96 | 0.07 | 0.64 | 0.91 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.50 | -1.82 | -2.35 | -1.86 | -3.05 | -0.90 | -1.74 | -1.35 | -1.50 | -2.19 | -3.13 | -2.02 | -1.86 | -0.87 | -1.68 | -2.48 | -1.65 | -1.56|
| full sent KL (full->waitk) |  |  | -2.99 | -1.32 | -2.53 | -2.09 | -2.90 | -0.95 | -1.86 | -1.80 | -2.44 | -2.06 | -2.87 | -1.72 | -2.64 | -1.36 | -3.20 | -1.55 | -1.67 | -1.69|
| dec-waitktgt |  |  | the | tunnel | has | a | cross-@@ | section | </s> | 1.@@ | 20 | metres | . | 90 | in@@ | ches | . | width | . | </s>|
| full sent tgt |  |  | the | tunnel | has | a | cross-@@ | section | of | 1.@@ | 20 | metres | and | a | cen@@ | ches | wide | width | . | </s>|
| ref | the | tunnel | has | a | cross-@@ | section | measuring | 1.@@ | 20 | metres | high | and | 90 | cen@@ | ti@@ | metres | across | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | er | wäre | damit | auch | geeignet | gewesen | , | um | die | illegale | einwanderung | richtung | usa | zu | fördern | .|
| waitk tgt |  |  | it | would | also | have | been | a | good | way | of | combating | illegal | immigration | to | the | united | states | . | </s>|
| waitk prob |  |  | 0.31 | 0.72 | 0.45 | 0.76 | 0.50 | 0.22 | 0.55 | 0.50 | 0.70 | 0.07 | 0.88 | 0.87 | 0.32 | 0.90 | 0.38 | 0.93 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.03 | 0.67 | 0.17 | 0.89 | 0.67 | 0.07 | 0.47 | 0.02 | 0.58 | 0.00 | 0.92 | 0.89 | 0.55 | 0.90 | 0.50 | 0.93 | 0.88 | 0.92|
| dec-waitk rank |  |  | 2 | 0 | 1 | 0 | 0 | 1 | 0 | 4 | 0 | 103 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.01 | -2.54 | -3.46 | -1.39 | -2.55 | -3.54 | -2.66 | -2.85 | -1.90 | -4.30 | -1.24 | -1.37 | -2.25 | -1.66 | -2.04 | -1.43 | -1.73 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.16 | -2.13 | -2.39 | -2.10 | -3.54 | -3.90 | -2.50 | -2.54 | -1.73 | -4.37 | -1.65 | -1.47 | -2.88 | -1.64 | -2.09 | -1.46 | -1.70 | -1.66|
| full sent prob |  |  | 0.46 | 0.79 | 0.30 | 0.89 | 0.36 | 0.21 | 0.47 | 0.44 | 0.62 | 0.00 | 0.90 | 0.89 | 0.55 | 0.90 | 0.47 | 0.93 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 211 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.60 | -1.87 | -2.27 | -1.44 | -3.51 | -3.91 | -3.20 | -3.31 | -1.91 | -1.83 | -1.39 | -1.36 | -2.38 | -1.66 | -2.04 | -1.47 | -1.73 | -1.62|
| full sent KL (full->waitk) |  |  | -3.20 | -2.20 | -2.41 | -2.09 | -3.41 | -3.91 | -2.49 | -2.68 | -1.74 | -4.38 | -1.63 | -1.47 | -2.88 | -1.64 | -2.09 | -1.46 | -1.70 | -1.65|
| dec-waitktgt |  |  | he | would | be | have | been | appropriate | good | idea | of | moving | illegal | immigration | to | the | united | states | . | </s>|
| full sent tgt |  |  | it | would | have | have | been | a | good | way | of | encouraging | illegal | immigration | to | the | united | states | . | </s>|
| ref | it | would | thus | be | suitable | to | assist | illegal | immigration | into | the | usa | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zwei | der | ver@@ | dä@@ | chtigen | wurden | in | zusammenhang | mit | dem | ko@@ | ka@@ | in-@@ | f@@ | und | fest@@ | genommen | .|
| waitk tgt |  |  | two | of | the | susp@@ | ects | were | arrested | in | connection | with | the | co@@ | ca@@ | ine | fund | . | </s>|
| waitk prob |  |  | 0.58 | 0.69 | 0.81 | 0.87 | 0.92 | 0.57 | 0.41 | 0.59 | 0.91 | 0.92 | 0.78 | 0.66 | 0.92 | 0.80 | 0.57 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.93 | 0.81 | 0.84 | 0.87 | 0.88 | 0.47 | 0.00 | 0.32 | 0.63 | 0.91 | 0.04 | 0.84 | 0.92 | 0.93 | 0.88 | 0.88 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 85 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -0.99 | -1.97 | -1.94 | -1.74 | -1.53 | -3.51 | -3.40 | -2.42 | -2.05 | -1.62 | -0.53 | -1.28 | -1.16 | -1.22 | -1.34 | -1.83 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.34 | -2.26 | -2.03 | -1.67 | -1.27 | -1.96 | -3.13 | -2.45 | -1.00 | -1.53 | -1.67 | -2.39 | -1.18 | -1.57 | -3.35 | -1.59 | -1.65|
| full sent prob |  |  | 0.89 | 0.78 | 0.81 | 0.94 | 0.85 | 0.67 | 0.90 | 0.70 | 0.83 | 0.91 | 0.87 | 0.84 | 0.87 | 0.91 | 0.86 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.42 | -1.94 | -1.97 | -1.20 | -1.71 | -1.86 | -0.95 | -2.32 | -1.52 | -1.58 | -1.72 | -1.35 | -1.42 | -1.34 | -1.45 | -1.68 | -1.59|
| full sent KL (full->waitk) |  |  | -3.32 | -2.25 | -2.01 | -1.72 | -1.25 | -2.08 | -3.44 | -2.64 | -1.15 | -1.54 | -2.16 | -2.39 | -1.14 | -1.56 | -3.34 | -1.60 | -1.64|
| dec-waitktgt |  |  | two | of | the | susp@@ | ects | were | involved | </s> | connection | with | co@@ | co@@ | ca@@ | ine | fund | . | </s>|
| full sent tgt |  |  | two | of | the | susp@@ | ects | were | arrested | in | connection | with | the | co@@ | ca@@ | ine | fund | . | </s>|
| ref | two | of | the | susp@@ | ects | were | de@@ | tained | in | conjunction | with | the | co@@ | ca@@ | ine | find | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | dritte | , | ein | mexi@@ | kan@@ | er | , | wurde | wegen | des | besch@@ | lag@@ | nah@@ | m@@ | ten | mar@@ | ih@@ | u@@ | an@@ | as | gefasst | .|
| waitk tgt |  |  | the | third | , | a | mex@@ | ic@@ | an | , | was | sent@@ | enced | to | death | for | se@@ | iz@@ | ure | of | mari@@ | ju@@ | ana | . | </s>|
| waitk prob |  |  | 0.71 | 0.91 | 0.55 | 0.59 | 0.93 | 0.94 | 0.87 | 0.88 | 0.73 | 0.36 | 0.95 | 0.65 | 0.43 | 0.63 | 0.44 | 0.85 | 0.60 | 0.79 | 0.96 | 0.57 | 0.99 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.57 | 0.94 | 0.44 | 0.47 | 0.94 | 0.93 | 0.90 | 0.84 | 0.44 | 0.00 | 0.86 | 0.13 | 0.03 | 0.00 | 0.07 | 0.33 | 0.63 | 0.00 | 0.93 | 0.86 | 0.92 | 0.86 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 110 | 0 | 1 | 4 | 5 | 2 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.07 | -1.31 | -2.71 | -2.25 | -1.13 | -1.43 | -1.49 | -1.97 | -3.10 | -3.95 | -1.84 | -5.19 | -3.85 | -1.56 | -4.84 | -2.44 | -3.09 | -1.72 | -1.26 | -0.97 | -1.26 | -1.98 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.20 | -1.56 | -3.05 | -2.35 | -1.37 | -1.31 | -1.82 | -1.75 | -1.65 | -2.88 | -1.14 | -1.99 | -3.12 | -1.95 | -1.75 | -0.86 | -1.98 | -1.38 | -1.05 | -1.65 | -0.84 | -1.63 | -1.66|
| full sent prob |  |  | 0.81 | 0.90 | 0.88 | 0.78 | 0.97 | 0.96 | 0.91 | 0.90 | 0.83 | 0.00 | 0.95 | 0.19 | 0.00 | 0.45 | 0.13 | 0.34 | 0.84 | 0.05 | 0.96 | 0.95 | 0.89 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 314 | 0 | 1 | 17 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.12 | -1.65 | -1.42 | -1.90 | -1.00 | -1.14 | -1.51 | -1.63 | -1.73 | -3.46 | -1.25 | -2.62 | -3.76 | -2.41 | -2.89 | -1.83 | -1.54 | -1.14 | -1.09 | -0.70 | -1.39 | -1.78 | -1.58|
| full sent KL (full->waitk) |  |  | -2.33 | -1.53 | -3.24 | -2.49 | -1.39 | -1.33 | -1.82 | -1.79 | -1.88 | -2.89 | -1.21 | -2.07 | -3.12 | -2.20 | -1.79 | -0.88 | -2.09 | -1.46 | -1.08 | -1.67 | -0.82 | -1.65 | -1.66|
| dec-waitktgt |  |  | the | third | , | a | mex@@ | ic@@ | an | , | was | accused | enced | </s> | se@@ | </s> | the | ized | ure | </s> | mari@@ | ju@@ | ana | . | </s>|
| full sent tgt |  |  | the | third | , | a | mex@@ | ic@@ | an | , | was | arrested | enced | for | the | for | the | ized | ure | mari@@ | mari@@ | ju@@ | ana | . | </s>|
| ref | the | third | , | a | mex@@ | ic@@ | an | , | was | de@@ | tained | due | to | the | se@@ | iz@@ | ure | of | the | mari@@ | ju@@ | ana | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | allen | drei@@ | en | dro@@ | ht | als | höchst@@ | strafe | lebens@@ | langer | frei@@ | heits@@ | ent@@ | zug | , | wie | beam@@ | te | sagten | .|
| waitk tgt |  |  | all | three | face | the | threat | of | a | maximum | penalty | of | life@@ | -@@ | long | de@@ | priv@@ | ation | , | as | officials | have | said | . | </s>|
| waitk prob |  |  | 0.35 | 0.91 | 0.26 | 0.61 | 0.69 | 0.87 | 0.24 | 0.35 | 0.38 | 0.62 | 0.36 | 0.83 | 0.95 | 0.51 | 0.64 | 0.94 | 0.56 | 0.91 | 0.76 | 0.67 | 0.73 | 0.93 | 0.91|
| dec-waitk prob |  |  | 0.83 | 0.94 | 0.02 | 0.79 | 0.85 | 0.84 | 0.34 | 0.25 | 0.09 | 0.11 | 0.09 | 0.66 | 0.99 | 0.16 | 0.74 | 0.96 | 0.00 | 0.91 | 0.66 | 0.78 | 0.80 | 0.92 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.52 | -1.24 | -3.98 | -2.01 | -1.39 | -1.92 | -3.04 | -2.86 | -2.47 | -2.35 | -3.56 | -2.07 | -0.87 | -2.77 | -1.36 | -1.13 | -2.33 | -1.56 | -1.88 | -1.61 | -1.91 | -1.58 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.79 | -1.43 | -3.13 | -2.84 | -1.91 | -1.64 | -3.69 | -3.92 | -2.06 | -2.06 | -1.88 | -1.37 | -1.21 | -2.96 | -2.05 | -1.31 | -1.78 | -1.54 | -1.81 | -2.24 | -2.38 | -1.48 | -1.64|
| full sent prob |  |  | 0.55 | 0.86 | 0.10 | 0.66 | 0.64 | 0.80 | 0.15 | 0.28 | 0.06 | 0.33 | 0.20 | 0.63 | 0.99 | 0.14 | 0.84 | 0.96 | 0.12 | 0.91 | 0.66 | 0.71 | 0.80 | 0.91 | 0.92|
| full sent rank |  |  | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.81 | -1.84 | -2.45 | -2.07 | -2.40 | -1.93 | -2.73 | -3.26 | -2.27 | -2.34 | -2.66 | -2.14 | -0.91 | -2.72 | -1.26 | -1.15 | -2.08 | -1.58 | -1.82 | -1.73 | -1.87 | -1.63 | -1.55|
| full sent KL (full->waitk) |  |  | -3.71 | -1.37 | -3.20 | -2.79 | -1.79 | -1.61 | -3.69 | -3.92 | -2.06 | -2.14 | -1.92 | -1.36 | -1.21 | -2.95 | -2.09 | -1.31 | -1.87 | -1.54 | -1.81 | -2.20 | -2.38 | -1.48 | -1.63|
| dec-waitktgt |  |  | all | three | are | the | threat | of | a | maximum | sentence | for | li@@ | -@@ | long | imprison@@ | priv@@ | ation | of | as | officials | have | said | . | </s>|
| full sent tgt |  |  | all | three | are | the | threat | of | life | maximum | sentence | for | life | -@@ | long | imprison@@ | priv@@ | ation | of | as | officials | have | said | . | </s>|
| ref | all | three | face | a | maximum | penalty | of | life | imprison@@ | ment | , | according | to | the | authorities | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | seit | 2006 | seien | acht | derartige | tun@@ | nel | entdeckt | worden | , | hi@@ | e@@ | ß | es | auf | der | presse@@ | konferenz | in | san | die@@ | go | weiter | .|
| waitk tgt |  |  | since | 2006 | , | eight | such | tun@@ | nels | have | been | discovered | , | but | they | were | reported | to | have | been | on | the | press | conference | in | san | di@@ | e@@ | go | . | </s>|
| waitk prob |  |  | 0.54 | 0.94 | 0.81 | 0.83 | 0.68 | 0.95 | 0.95 | 0.87 | 0.94 | 0.73 | 0.74 | 0.28 | 0.20 | 0.32 | 0.13 | 0.41 | 0.57 | 0.74 | 0.11 | 0.61 | 0.08 | 0.60 | 0.89 | 0.90 | 0.93 | 0.97 | 0.95 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.76 | 0.93 | 0.84 | 0.79 | 0.69 | 0.74 | 0.73 | 0.90 | 0.95 | 0.39 | 0.17 | 0.01 | 0.10 | 0.47 | 0.06 | 0.22 | 0.49 | 0.86 | 0.01 | 0.70 | 0.79 | 0.79 | 0.87 | 0.92 | 0.95 | 0.94 | 0.91 | 0.88 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 9 | 2 | 0 | 2 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.01 | -1.44 | -1.99 | -1.78 | -2.12 | -1.86 | -2.81 | -1.47 | -1.24 | -2.74 | -2.77 | -4.51 | -4.65 | -2.76 | -4.86 | -2.31 | -2.60 | -1.59 | -3.40 | -2.39 | -1.36 | -2.06 | -1.71 | -1.44 | -1.22 | -1.30 | -1.54 | -1.80 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.31 | -1.32 | -1.96 | -1.81 | -1.96 | -0.95 | -1.00 | -1.56 | -1.35 | -1.83 | -1.71 | -3.75 | -3.67 | -3.92 | -4.00 | -2.52 | -1.89 | -2.30 | -4.96 | -2.79 | -5.12 | -3.30 | -1.65 | -1.66 | -1.39 | -1.09 | -1.18 | -1.65 | -1.66|
| full sent prob |  |  | 0.25 | 0.91 | 0.68 | 0.87 | 0.82 | 0.91 | 0.95 | 0.58 | 0.94 | 0.47 | 0.70 | 0.01 | 0.23 | 0.26 | 0.01 | 0.27 | 0.57 | 0.58 | 0.02 | 0.49 | 0.62 | 0.86 | 0.89 | 0.94 | 0.96 | 0.94 | 0.91 | 0.88 | 0.92|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 10 | 1 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.78 | -1.59 | -2.07 | -1.54 | -1.72 | -1.41 | -1.28 | -2.18 | -1.36 | -2.63 | -2.11 | -3.04 | -3.28 | -3.04 | -4.10 | -2.60 | -1.96 | -2.37 | -3.95 | -2.87 | -2.01 | -1.65 | -1.69 | -1.35 | -1.18 | -1.34 | -1.59 | -1.79 | -1.57|
| full sent KL (full->waitk) |  |  | -3.08 | -1.30 | -1.86 | -1.86 | -2.03 | -1.08 | -1.17 | -1.34 | -1.34 | -1.88 | -2.04 | -3.77 | -3.71 | -3.86 | -4.00 | -2.52 | -1.91 | -2.13 | -4.94 | -2.69 | -5.11 | -3.34 | -1.66 | -1.67 | -1.40 | -1.09 | -1.18 | -1.65 | -1.66|
| dec-waitktgt |  |  | since | 2006 | , | eight | such | tun@@ | nels | have | been | discovered | . | </s> | </s> | were | referred | at | have | been | in | the | press | conference | in | san | di@@ | e@@ | go | . | </s>|
| full sent tgt |  |  | eight | 2006 | , | eight | such | tun@@ | nels | have | been | discovered | , | it | they | were | still | at | have | been | re@@ | the | press | conference | in | san | di@@ | e@@ | go | . | </s>|
| ref | since | 2006 | , | eight | tun@@ | nels | of | this | type | have | been | discovered | , | the | press | conference | in | san | di@@ | e@@ | go | continued | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | es | sei | aber | das | erste | mal | , | dass | in | einem | solchen | tun@@ | n@@ | el@@ | bau | ko@@ | ka@@ | in | gefunden | wurde | .|
| waitk tgt |  |  | it | is | the | first | time | that | the | european | parliament | has | had | a | debate | on | co@@ | ca@@ | ine | in | this | way | . | </s>|
| waitk prob |  |  | 0.32 | 0.44 | 0.42 | 0.91 | 0.88 | 0.40 | 0.20 | 0.05 | 0.65 | 0.66 | 0.13 | 0.19 | 0.18 | 0.68 | 0.77 | 0.95 | 0.98 | 0.41 | 0.60 | 0.40 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.02 | 0.34 | 0.50 | 0.92 | 0.94 | 0.37 | 0.02 | 0.00 | 0.07 | 0.77 | 0.08 | 0.32 | 0.00 | 0.71 | 0.74 | 0.92 | 0.96 | 0.06 | 0.43 | 0.16 | 0.88 | 0.92|
| dec-waitk rank |  |  | 7 | 0 | 0 | 0 | 0 | 0 | 6 | 587 | 1 | 0 | 1 | 0 | 818 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.55 | -3.04 | -2.96 | -1.46 | -1.29 | -2.85 | -3.50 | -5.83 | -5.32 | -2.03 | -4.45 | -3.01 | -1.15 | -2.27 | -1.74 | -1.30 | -1.09 | -3.43 | -2.85 | -3.83 | -1.76 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.90 | -2.17 | -2.87 | -1.56 | -1.84 | -2.47 | -4.11 | -5.93 | -1.92 | -2.63 | -4.66 | -3.43 | -4.93 | -2.21 | -2.04 | -1.12 | -1.02 | -3.02 | -2.31 | -3.06 | -1.66 | -1.65|
| full sent prob |  |  | 0.24 | 0.38 | 0.65 | 0.91 | 0.92 | 0.26 | 0.02 | 0.00 | 0.01 | 0.70 | 0.02 | 0.09 | 0.00 | 0.63 | 0.58 | 0.95 | 0.97 | 0.34 | 0.23 | 0.02 | 0.87 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 670 | 4 | 0 | 2 | 2 | 272 | 0 | 0 | 0 | 0 | 0 | 1 | 6 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.28 | -2.36 | -2.33 | -1.57 | -1.47 | -2.30 | -1.39 | -4.77 | -2.07 | -2.43 | -3.42 | -1.73 | -4.51 | -2.28 | -2.09 | -1.15 | -1.01 | -3.81 | -2.39 | -3.12 | -1.86 | -1.57|
| full sent KL (full->waitk) |  |  | -2.98 | -2.17 | -2.92 | -1.55 | -1.82 | -2.39 | -4.09 | -5.93 | -1.88 | -2.59 | -4.65 | -3.36 | -4.93 | -2.17 | -1.94 | -1.14 | -1.03 | -3.09 | -2.23 | -3.02 | -1.65 | -1.65|
| dec-waitktgt |  |  | but | is | the | first | time | that | in | event | union | has | been | a | tunnel | on | co@@ | ca@@ | ine | . | this | way | . | </s>|
| full sent tgt |  |  | it | is | the | first | time | co@@ | co@@ | co@@ | tunnel | has | found | co@@ | co@@ | on | co@@ | ca@@ | ine | in | such | tunnel | . | </s>|
| ref | however | , | this | was | the | first | time | that | co@@ | ca@@ | ine | was | found | in | such | a | tunnel | construction | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | normalerweise | wird | ko@@ | ka@@ | in | in | klein@@ | eren | mengen | und | nicht | durch | tun@@ | nel | gesch@@ | mu@@ | g@@ | gelt | .|
| waitk tgt |  |  | usually | co@@ | ca@@ | ine | is | used | in | smaller | quantities | and | not | through | tun@@ | nels | . | </s>|
| waitk prob |  |  | 0.20 | 0.74 | 0.96 | 0.97 | 0.75 | 0.10 | 0.81 | 0.55 | 0.85 | 0.44 | 0.86 | 0.56 | 0.74 | 0.97 | 0.77 | 0.91|
| dec-waitk prob |  |  | 0.17 | 0.79 | 0.97 | 0.80 | 0.47 | 0.00 | 0.49 | 0.69 | 0.83 | 0.15 | 0.89 | 0.45 | 0.57 | 0.48 | 0.48 | 0.94|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 30 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.92 | -1.36 | -0.99 | -1.67 | -3.44 | -3.26 | -3.65 | -1.70 | -1.32 | -3.33 | -1.66 | -2.33 | -2.21 | -4.08 | -2.47 | -1.38|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.94 | -2.00 | -1.10 | -0.93 | -2.08 | -4.66 | -1.75 | -1.88 | -1.25 | -2.21 | -1.86 | -1.88 | -1.78 | -0.69 | -1.82 | -1.64|
| full sent prob |  |  | 0.11 | 0.57 | 0.98 | 0.97 | 0.86 | 0.00 | 0.74 | 0.51 | 0.74 | 0.33 | 0.78 | 0.10 | 0.61 | 0.96 | 0.91 | 0.92|
| full sent rank |  |  | 2 | 0 | 0 | 0 | 0 | 92 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.03 | -1.88 | -0.92 | -0.99 | -1.73 | -0.63 | -2.18 | -1.98 | -1.55 | -2.36 | -1.85 | -2.61 | -2.24 | -1.14 | -1.54 | -1.57|
| full sent KL (full->waitk) |  |  | -3.90 | -1.88 | -1.10 | -1.07 | -2.32 | -4.66 | -1.93 | -1.83 | -1.20 | -2.27 | -1.79 | -1.70 | -1.80 | -1.07 | -2.09 | -1.62|
| dec-waitktgt |  |  | normally | co@@ | ca@@ | ine | is | smaller | in | smaller | quantities | , | not | through | tun@@ | nels | . | </s>|
| full sent tgt |  |  | normally | co@@ | ca@@ | ine | is | s@@ | in | smaller | quantities | and | not | s@@ | tun@@ | nels | . | </s>|
| ref | normally | co@@ | ca@@ | ine | is | s@@ | mu@@ | gg@@ | led | in | smaller | quantities | and | not | through | tun@@ | nels | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | würden | alles | tun | , | um | in | die | usa | zu | gelangen | .|
| waitk tgt |  |  | they | would | do | everything | they | can | to | go | to | the | us | . | </s>|
| waitk prob |  |  | 0.47 | 0.77 | 0.88 | 0.52 | 0.35 | 0.63 | 0.89 | 0.26 | 0.85 | 0.88 | 0.51 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.15 | 0.71 | 0.84 | 0.76 | 0.37 | 0.22 | 0.70 | 0.18 | 0.80 | 0.88 | 0.42 | 0.87 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.87 | -2.34 | -1.94 | -1.61 | -2.02 | -2.29 | -2.13 | -3.62 | -1.97 | -1.71 | -2.48 | -1.88 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.47 | -2.07 | -1.55 | -2.32 | -2.19 | -1.52 | -1.49 | -3.18 | -1.77 | -1.79 | -1.68 | -1.61 | -1.68|
| full sent prob |  |  | 0.69 | 0.81 | 0.82 | 0.69 | 0.35 | 0.70 | 0.89 | 0.03 | 0.75 | 0.89 | 0.56 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.93 | -1.90 | -2.02 | -1.81 | -2.20 | -1.65 | -1.70 | -2.13 | -1.97 | -1.63 | -2.23 | -1.69 | -1.62|
| full sent KL (full->waitk) |  |  | -2.61 | -2.14 | -1.54 | -2.30 | -2.18 | -1.69 | -1.62 | -3.19 | -1.74 | -1.80 | -1.72 | -1.64 | -1.67|
| dec-waitktgt |  |  | you | would | do | everything | they | could | to | go | to | the | us | . | </s>|
| full sent tgt |  |  | they | would | do | everything | they | can | to | get | to | the | us | . | </s>|
| ref | they | will | do | anything | to | make | it | to | the | usa | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zu | den | fest@@ | genommenen | wurden | keine | einzelheiten | bekannt | gegeben | , | zumindest | einer | sei | mexi@@ | kan@@ | er | , | hi@@ | e@@ | ß | es | .|
| waitk tgt |  |  | the | de@@ | tain@@ | e@@ | es | were | not | given | any | details | , | at | least | one | of | them | was | mex@@ | ic@@ | ans | . | </s>|
| waitk prob |  |  | 0.11 | 0.30 | 0.92 | 0.93 | 0.95 | 0.41 | 0.80 | 0.15 | 0.38 | 0.81 | 0.78 | 0.78 | 0.92 | 0.78 | 0.31 | 0.92 | 0.50 | 0.83 | 0.95 | 0.73 | 0.80 | 0.91|
| dec-waitk prob |  |  | 0.09 | 0.56 | 0.73 | 0.89 | 0.96 | 0.17 | 0.69 | 0.15 | 0.37 | 0.88 | 0.40 | 0.78 | 0.92 | 0.54 | 0.21 | 0.84 | 0.21 | 0.93 | 0.98 | 0.68 | 0.84 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.51 | -2.07 | -1.59 | -1.59 | -1.20 | -2.40 | -2.47 | -3.50 | -2.21 | -1.48 | -3.27 | -2.03 | -1.37 | -3.38 | -3.51 | -1.67 | -3.35 | -1.20 | -0.99 | -2.07 | -1.86 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.56 | -3.55 | -0.95 | -1.28 | -1.24 | -2.34 | -1.94 | -4.06 | -2.75 | -1.88 | -1.88 | -1.98 | -1.37 | -1.85 | -2.89 | -1.23 | -2.40 | -1.91 | -1.27 | -1.57 | -1.97 | -1.66|
| full sent prob |  |  | 0.18 | 0.54 | 0.88 | 0.97 | 0.94 | 0.57 | 0.74 | 0.28 | 0.34 | 0.81 | 0.75 | 0.52 | 0.92 | 0.59 | 0.26 | 0.68 | 0.39 | 0.90 | 0.97 | 0.69 | 0.13 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -2.82 | -2.32 | -1.32 | -1.04 | -1.32 | -2.27 | -2.26 | -3.58 | -2.67 | -1.88 | -2.19 | -2.35 | -1.33 | -3.06 | -3.26 | -2.15 | -2.80 | -1.34 | -1.12 | -2.05 | -1.97 | -1.61|
| full sent KL (full->waitk) |  |  | -4.56 | -3.54 | -1.05 | -1.34 | -1.22 | -2.39 | -1.97 | -4.07 | -2.73 | -1.84 | -2.11 | -1.82 | -1.37 | -1.88 | -2.90 | -1.11 | -2.47 | -1.89 | -1.25 | -1.58 | -1.54 | -1.65|
| dec-waitktgt |  |  | to | de@@ | tain@@ | e@@ | es | have | not | informed | details | details | , | at | least | one | of | them | was | mex@@ | ic@@ | ans | . | </s>|
| full sent tgt |  |  | no | de@@ | tain@@ | e@@ | es | were | not | given | any | details | , | at | least | one | of | them | was | mex@@ | ic@@ | ans | , | </s>|
| ref | no | specific | details | were | given | regarding | those | de@@ | tained | , | but | it | is | reported | that | at | least | one | is | mex@@ | ic@@ | an | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | müssen | mit | haft@@ | stra@@ | fen | bis | zu | zehn | jahren | rechnen | .|
| waitk tgt |  |  | they | must | be | pun@@ | ished | with | prison | sent@@ | ences | of | up | to | ten | years | . | </s>|
| waitk prob |  |  | 0.36 | 0.60 | 0.55 | 0.27 | 0.94 | 0.21 | 0.56 | 0.92 | 0.97 | 0.51 | 0.94 | 0.91 | 0.84 | 0.93 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.07 | 0.67 | 0.27 | 0.02 | 0.91 | 0.34 | 0.51 | 0.95 | 0.92 | 0.55 | 0.90 | 0.91 | 0.74 | 0.93 | 0.89 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.02 | -1.95 | -4.35 | -3.75 | -1.40 | -2.60 | -1.70 | -1.04 | -1.45 | -2.55 | -1.45 | -1.63 | -1.64 | -1.41 | -1.76 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.78 | -2.17 | -3.07 | -3.79 | -1.23 | -3.16 | -2.58 | -1.14 | -1.09 | -2.08 | -1.12 | -1.58 | -1.32 | -1.41 | -1.68 | -1.70|
| full sent prob |  |  | 0.73 | 0.11 | 0.08 | 0.00 | 0.82 | 0.01 | 0.62 | 0.88 | 0.95 | 0.52 | 0.90 | 0.92 | 0.77 | 0.93 | 0.89 | 0.92|
| full sent rank |  |  | 0 | 3 | 1 | 26 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.09 | -3.14 | -1.72 | -3.35 | -1.85 | -1.33 | -2.16 | -1.31 | -1.21 | -2.63 | -1.40 | -1.57 | -1.53 | -1.41 | -1.77 | -1.58|
| full sent KL (full->waitk) |  |  | -2.79 | -1.90 | -2.98 | -3.77 | -1.16 | -3.14 | -2.62 | -1.09 | -1.11 | -2.07 | -1.12 | -1.58 | -1.33 | -1.42 | -1.68 | -1.69|
| dec-waitktgt |  |  | you | must | be | given | ished | with | prison | sent@@ | ences | of | up | to | ten | years | . | </s>|
| full sent tgt |  |  | they | have | expect | expected | ished | for | prison | sent@@ | ences | of | up | to | ten | years | . | </s>|
| ref | they | can | expect | prison | terms | of | up | to | ten | years | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | wieder@@ | kehr | der | ersten | ur@@ | kund@@ | lichen | erwähn@@ | ung | rück@@ | t | immer | näher | .|
| waitk tgt |  |  | the | re@@ | vers@@ | al | of | the | first | docum@@ | entary | mention | is | getting | closer | and | closer | . | </s>|
| waitk prob |  |  | 0.18 | 0.17 | 0.50 | 0.97 | 0.88 | 0.81 | 0.79 | 0.46 | 0.92 | 0.39 | 0.60 | 0.27 | 0.62 | 0.47 | 0.83 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.08 | 0.02 | 0.01 | 0.93 | 0.90 | 0.84 | 0.88 | 0.50 | 0.88 | 0.44 | 0.72 | 0.17 | 0.79 | 0.38 | 0.84 | 0.90 | 0.93|
| dec-waitk rank |  |  | 3 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.15 | -1.31 | -2.93 | -1.37 | -1.69 | -1.90 | -1.60 | -2.32 | -1.33 | -2.75 | -2.31 | -3.12 | -1.85 | -1.84 | -1.55 | -1.64 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.88 | -4.31 | -2.83 | -1.00 | -1.80 | -2.18 | -2.14 | -3.35 | -1.18 | -2.89 | -2.91 | -3.48 | -2.48 | -2.24 | -1.48 | -1.73 | -1.63|
| full sent prob |  |  | 0.39 | 0.08 | 0.01 | 0.97 | 0.90 | 0.81 | 0.88 | 0.54 | 0.83 | 0.48 | 0.82 | 0.20 | 0.80 | 0.45 | 0.83 | 0.90 | 0.92|
| full sent rank |  |  | 0 | 2 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.49 | -2.16 | -3.96 | -1.08 | -1.71 | -2.10 | -1.51 | -2.46 | -1.49 | -3.07 | -1.70 | -3.35 | -1.78 | -1.94 | -1.60 | -1.66 | -1.54|
| full sent KL (full->waitk) |  |  | -3.90 | -4.32 | -2.82 | -1.03 | -1.80 | -2.16 | -2.14 | -3.36 | -1.14 | -2.89 | -2.96 | -3.48 | -2.49 | -2.24 | -1.48 | -1.73 | -1.63|
| dec-waitktgt |  |  | re@@ | first | sumption | al | of | the | first | docum@@ | entary | mention | is | appro@@ | closer | . | closer | . | </s>|
| full sent tgt |  |  | the | return | sumption | al | of | the | first | docum@@ | entary | mention | is | getting | closer | and | closer | . | </s>|
| ref | anniversary | of | the | first | docum@@ | ented | mention | of | the | town | , | are | drawing | closer | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | wenn | in | gut | acht | wochen | das | jahr | zu | ende | geht | , | steht | das | ju@@ | bi@@ | lä@@ | ums@@ | jahr | an | .|
| waitk tgt |  |  | if | in | more | than | eight | weeks | the | year | is | over | , | the | anniversary | of | the | year | is | over | . | </s>|
| waitk prob |  |  | 0.49 | 0.16 | 0.15 | 0.89 | 0.90 | 0.96 | 0.77 | 0.88 | 0.21 | 0.50 | 0.75 | 0.54 | 0.50 | 0.22 | 0.59 | 0.03 | 0.38 | 0.17 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.42 | 0.08 | 0.04 | 0.92 | 0.84 | 0.92 | 0.44 | 0.79 | 0.23 | 0.68 | 0.09 | 0.18 | 0.00 | 0.02 | 0.41 | 0.26 | 0.29 | 0.04 | 0.90 | 0.92|
| dec-waitk rank |  |  | 1 | 2 | 6 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 2 | 4 | 0 | 0 | 1 | 5 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.67 | -3.71 | -3.83 | -1.35 | -1.60 | -1.47 | -2.97 | -2.50 | -2.74 | -1.75 | -2.01 | -3.52 | -1.03 | -2.50 | -4.17 | -4.67 | -2.80 | -3.15 | -1.63 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.90 | -3.89 | -3.50 | -1.74 | -1.37 | -1.11 | -1.82 | -1.72 | -3.18 | -2.95 | -1.67 | -2.57 | -2.60 | -3.31 | -3.03 | -5.72 | -2.91 | -3.77 | -1.67 | -1.67|
| full sent prob |  |  | 0.17 | 0.10 | 0.08 | 0.93 | 0.88 | 0.94 | 0.77 | 0.83 | 0.25 | 0.80 | 0.84 | 0.70 | 0.47 | 0.01 | 0.57 | 0.19 | 0.29 | 0.06 | 0.91 | 0.91|
| full sent rank |  |  | 2 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 3 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.27 | -2.84 | -3.87 | -1.36 | -1.45 | -1.34 | -2.11 | -2.22 | -2.51 | -1.57 | -1.77 | -2.21 | -2.53 | -0.96 | -2.96 | -4.96 | -2.79 | -2.57 | -1.58 | -1.59|
| full sent KL (full->waitk) |  |  | -2.77 | -3.91 | -3.51 | -1.75 | -1.40 | -1.12 | -2.02 | -1.75 | -3.20 | -2.99 | -2.14 | -2.80 | -2.67 | -3.20 | -3.11 | -5.71 | -2.91 | -3.77 | -1.68 | -1.67|
| dec-waitktgt |  |  | when | you | over | than | eight | weeks | the | year | ends | over | </s> | </s> | ju@@ | will | the | year | will | due | . | </s>|
| full sent tgt |  |  | when | the | a | than | eight | weeks | the | year | ends | over | , | the | anniversary | year | the | year | will | due | . | </s>|
| ref | when | the | year | comes | to | an | end | in | just | eight | weeks | , | the | anniversary | year | will | be | upon | us | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | gei@@ | sin@@ | gen | und | kir@@ | chen@@ | -@@ | haus@@ | en | wurden | 7@@ | 9@@ | 4 | erstmals | ur@@ | kund@@ | lich | zusammen | erwähnt | .|
| waitk tgt |  |  | ho@@ | stag@@ | e-@@ | sing@@ | ing | and | church | house@@ | holds | were | born | in | 7@@ | 94 | for | the | first | time | together | . | </s>|
| waitk prob |  |  | 0.09 | 0.13 | 0.22 | 0.51 | 0.95 | 0.83 | 0.72 | 0.54 | 0.32 | 0.86 | 0.06 | 0.40 | 0.56 | 0.93 | 0.58 | 0.91 | 0.92 | 0.96 | 0.84 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.03 | 0.06 | 0.05 | 0.04 | 0.87 | 0.82 | 0.43 | 0.03 | 0.94 | 0.53 | 0.00 | 0.89 | 0.96 | 0.96 | 0.01 | 0.90 | 0.97 | 0.97 | 0.00 | 0.90 | 0.92|
| dec-waitk rank |  |  | 7 | 3 | 2 | 3 | 0 | 0 | 0 | 5 | 0 | 0 | 10 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 15 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.95 | -3.57 | -4.91 | -4.77 | -1.57 | -2.03 | -2.71 | -3.11 | -0.74 | -2.79 | -1.86 | -1.08 | -0.86 | -1.10 | -2.17 | -1.65 | -1.05 | -1.13 | -1.61 | -1.68 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.83 | -4.96 | -4.50 | -3.08 | -1.09 | -1.95 | -2.14 | -2.12 | -4.60 | -1.34 | -4.90 | -2.96 | -3.51 | -1.30 | -2.12 | -1.61 | -1.46 | -1.19 | -0.95 | -1.74 | -1.67|
| full sent prob |  |  | 0.01 | 0.00 | 0.00 | 0.00 | 0.65 | 0.80 | 0.42 | 0.02 | 0.08 | 0.80 | 0.00 | 0.69 | 0.82 | 0.96 | 0.06 | 0.85 | 0.96 | 0.95 | 0.02 | 0.54 | 0.91|
| full sent rank |  |  | 8 | 19 | 36 | 30 | 0 | 0 | 0 | 8 | 2 | 0 | 72 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 5 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.45 | -3.72 | -5.04 | -4.82 | -2.06 | -2.19 | -2.86 | -3.66 | -5.05 | -1.92 | -0.90 | -2.12 | -1.71 | -1.13 | -3.28 | -1.93 | -1.12 | -1.22 | -2.16 | -2.74 | -1.59|
| full sent KL (full->waitk) |  |  | -4.85 | -4.95 | -4.49 | -3.06 | -0.92 | -1.94 | -2.13 | -2.14 | -4.38 | -1.54 | -4.90 | -2.90 | -3.45 | -1.30 | -2.15 | -1.57 | -1.45 | -1.18 | -0.96 | -1.47 | -1.66|
| dec-waitktgt |  |  | vul@@ | sti@@ | ings | based | ing | and | church | sha@@ | holds | were | 7@@ | in | 7@@ | 94 | . | the | first | time | . | . | </s>|
| full sent tgt |  |  | ge@@ | is@@ | n@@ | like | ing | and | church | houses | en | were | first | in | 7@@ | 94 | . | the | first | time | in | . | </s>|
| ref | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | were | first | docum@@ | ented | together | in | the | year | 7@@ | 94 | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | kirchen | wurde | eine | ur@@ | kunde | ge@@ | fertigt | , | in | der | beide | orte | erwähnt | sind | .|
| waitk tgt |  |  | in | churches | , | a | certificate | was | produced | , | in | which | both | places | are | mentioned | . | </s>|
| waitk prob |  |  | 0.39 | 0.81 | 0.38 | 0.70 | 0.41 | 0.58 | 0.30 | 0.23 | 0.22 | 0.88 | 0.75 | 0.72 | 0.59 | 0.77 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.56 | 0.78 | 0.16 | 0.41 | 0.34 | 0.50 | 0.27 | 0.23 | 0.00 | 0.50 | 0.28 | 0.61 | 0.58 | 0.90 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.90 | -2.17 | -3.61 | -3.01 | -2.72 | -2.29 | -3.72 | -3.40 | -1.23 | -3.75 | -4.22 | -2.75 | -2.17 | -1.33 | -1.77 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.49 | -1.67 | -2.54 | -2.18 | -2.64 | -2.07 | -3.73 | -3.30 | -4.07 | -1.49 | -1.72 | -2.08 | -2.35 | -2.23 | -1.63 | -1.67|
| full sent prob |  |  | 0.27 | 0.31 | 0.37 | 0.73 | 0.12 | 0.47 | 0.37 | 0.24 | 0.16 | 0.95 | 0.77 | 0.59 | 0.64 | 0.91 | 0.91 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.58 | -3.89 | -2.34 | -2.17 | -1.15 | -2.16 | -3.21 | -3.27 | -3.11 | -1.18 | -2.02 | -2.65 | -1.85 | -1.26 | -1.64 | -1.58|
| full sent KL (full->waitk) |  |  | -3.40 | -1.35 | -2.68 | -2.36 | -2.69 | -2.07 | -3.74 | -3.34 | -4.12 | -1.82 | -2.01 | -2.07 | -2.37 | -2.24 | -1.64 | -1.66|
| dec-waitktgt |  |  | in | churches | , | a | document | was | produced | , | </s> | which | both | places | are | mentioned | . | </s>|
| full sent tgt |  |  | a | churches | , | a | document | was | produced | , | men@@ | which | both | places | are | mentioned | . | </s>|
| ref | a | de@@ | ed | was | drafted | in | kir@@ | chen | , | in | which | both | towns | are | mentioned | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | im | rahmen | des | ju@@ | bi@@ | lä@@ | ums | sind | et@@ | liche | veranstaltungen | sowohl | in | gei@@ | sin@@ | gen | , | als | auch | in | kir@@ | chen@@ | -@@ | haus@@ | en | geplant | .|
| waitk tgt |  |  | in | the | context | of | the | anniversary | , | several | events | are | being | held | both | in | ge@@ | is@@ | ingen | and | in | kir@@ | ch@@ | en-@@ | haus@@ | en | . | </s>|
| waitk prob |  |  | 0.13 | 0.65 | 0.55 | 0.90 | 0.79 | 0.69 | 0.60 | 0.45 | 0.87 | 0.36 | 0.17 | 0.56 | 0.46 | 0.82 | 0.28 | 0.76 | 0.73 | 0.73 | 0.86 | 0.35 | 0.89 | 0.99 | 0.88 | 0.92 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.07 | 0.62 | 0.55 | 0.92 | 0.69 | 0.46 | 0.08 | 0.03 | 0.78 | 0.48 | 0.01 | 0.94 | 0.07 | 0.85 | 0.19 | 0.96 | 0.32 | 0.82 | 0.62 | 0.02 | 0.77 | 0.97 | 0.72 | 0.92 | 0.89 | 0.93|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 8 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.80 | -2.73 | -1.51 | -1.52 | -2.43 | -1.63 | -2.65 | -2.45 | -2.29 | -2.60 | -3.00 | -0.86 | -2.90 | -1.67 | -2.71 | -0.90 | -3.92 | -2.00 | -1.66 | -2.19 | -1.43 | -1.06 | -1.85 | -1.48 | -1.73 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.02 | -2.81 | -2.79 | -1.71 | -2.01 | -2.47 | -2.38 | -2.27 | -1.67 | -2.92 | -3.42 | -2.42 | -1.96 | -1.80 | -3.51 | -2.22 | -1.47 | -2.29 | -1.60 | -2.72 | -1.07 | -0.89 | -1.30 | -1.47 | -1.67 | -1.65|
| full sent prob |  |  | 0.08 | 0.73 | 0.35 | 0.91 | 0.76 | 0.53 | 0.42 | 0.19 | 0.66 | 0.72 | 0.04 | 0.07 | 0.20 | 0.89 | 0.77 | 0.97 | 0.43 | 0.85 | 0.85 | 0.94 | 0.78 | 0.98 | 0.70 | 0.93 | 0.87 | 0.92|
| full sent rank |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.86 | -2.34 | -3.60 | -1.59 | -2.04 | -2.68 | -2.93 | -2.86 | -2.98 | -1.96 | -1.59 | -2.53 | -2.07 | -1.51 | -1.65 | -0.82 | -3.40 | -1.77 | -1.63 | -0.74 | -1.50 | -0.97 | -1.97 | -1.43 | -1.82 | -1.57|
| full sent KL (full->waitk) |  |  | -3.99 | -2.87 | -2.70 | -1.70 | -2.05 | -2.51 | -2.55 | -2.34 | -1.59 | -2.96 | -3.45 | -2.04 | -2.09 | -1.83 | -3.64 | -2.23 | -1.54 | -2.31 | -1.76 | -2.84 | -1.07 | -0.90 | -1.29 | -1.47 | -1.66 | -1.65|
| dec-waitktgt |  |  | within | the | context | of | the | anniversary | of | there | events | are | held | held | . | in | g@@ | is@@ | ingen | and | in | church | ch@@ | en-@@ | haus@@ | en | . | </s>|
| full sent tgt |  |  | the | the | context | of | the | anniversary | , | a | events | are | planned | planned | in | in | ge@@ | is@@ | ingen | and | in | kir@@ | ch@@ | en-@@ | haus@@ | en | . | </s>|
| ref | as | part | of | the | anniversary | celebra@@ | tions | , | a | number | of | events | are | planned | both | in | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | am | freitag | mit | einem | fe@@ | sta@@ | kt | , | am | samstag | und | sonntag | mit | einem | fest | rund | um | die | kir@@ | cht@@ | al@@ | halle | .|
| waitk tgt |  |  | on | friday | with | a | fe@@ | st@@ | act | , | on | saturday | and | sunday | with | a | festival | around | the | church | al@@ | ley | . | </s>|
| waitk prob |  |  | 0.43 | 0.87 | 0.37 | 0.80 | 0.36 | 0.36 | 0.45 | 0.81 | 0.60 | 0.93 | 0.89 | 0.94 | 0.82 | 0.88 | 0.40 | 0.59 | 0.87 | 0.86 | 0.23 | 0.22 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.18 | 0.96 | 0.55 | 0.80 | 0.18 | 0.93 | 0.85 | 0.38 | 0.18 | 0.90 | 0.91 | 0.94 | 0.61 | 0.69 | 0.04 | 0.26 | 0.80 | 0.73 | 0.02 | 0.02 | 0.61 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 4 | 6 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.73 | -1.06 | -2.50 | -1.87 | -3.98 | -0.88 | -1.47 | -3.58 | -1.53 | -1.35 | -1.54 | -1.22 | -2.66 | -2.76 | -3.49 | -3.32 | -2.09 | -2.29 | -2.74 | -5.64 | -2.33 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.67 | -1.62 | -2.88 | -1.95 | -2.93 | -2.30 | -4.06 | -1.74 | -1.81 | -1.16 | -1.72 | -1.23 | -1.79 | -1.51 | -2.34 | -2.32 | -1.74 | -1.48 | -4.35 | -4.92 | -1.51 | -1.69|
| full sent prob |  |  | 0.37 | 0.86 | 0.56 | 0.81 | 0.18 | 0.65 | 0.85 | 0.76 | 0.34 | 0.85 | 0.90 | 0.89 | 0.80 | 0.87 | 0.15 | 0.56 | 0.90 | 0.58 | 0.00 | 0.03 | 0.31 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 12 | 3 | 1 | 0|
| full sent KL (waitk->full) |  |  | -3.24 | -1.56 | -2.28 | -1.90 | -2.21 | -2.31 | -1.55 | -2.13 | -1.80 | -1.60 | -1.63 | -1.55 | -1.81 | -1.78 | -2.92 | -2.74 | -1.64 | -3.07 | -0.59 | -5.19 | -1.68 | -1.58|
| full sent KL (full->waitk) |  |  | -3.73 | -1.55 | -2.88 | -1.96 | -2.97 | -2.23 | -4.06 | -1.99 | -1.86 | -1.12 | -1.71 | -1.18 | -1.91 | -1.64 | -2.39 | -2.46 | -1.81 | -1.37 | -4.40 | -4.92 | -1.29 | -1.69|
| dec-waitktgt |  |  | friday | friday | with | a | cere@@ | st@@ | act | , | saturday | saturday | and | sunday | with | a | party | around | the | church | . | ta | . | </s>|
| full sent tgt |  |  | on | friday | with | a | cere@@ | st@@ | act | , | saturday | saturday | and | sunday | with | a | party | around | the | church | hall | hall | hall | </s>|
| ref | on | the | friday | there | will | be | a | cere@@ | mony | , | and | on | the | saturday | and | sunday | a | party | will | be | held | at | the | kir@@ | ch@@ | tal@@ | hal@@ | le | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | an | diesem | fest@@ | wochenende | ist | außerdem | noch | das | kir@@ | chen@@ | -@@ | haus@@ | ener | kir@@ | chen@@ | fest | .|
| waitk tgt |  |  | at | this | weekend | , | there | is | also | the | church | house | piano | festival | , | which | takes | place | in | the | town | of | k@@ | ap@@ | run | . | </s>|
| waitk prob |  |  | 0.12 | 0.69 | 0.28 | 0.20 | 0.16 | 0.64 | 0.60 | 0.67 | 0.47 | 0.67 | 0.12 | 0.21 | 0.21 | 0.29 | 0.26 | 0.94 | 0.28 | 0.38 | 0.05 | 0.55 | 0.04 | 0.06 | 0.35 | 0.76 | 0.91|
| dec-waitk prob |  |  | 0.06 | 0.13 | 0.69 | 0.06 | 0.09 | 0.53 | 0.53 | 0.49 | 0.66 | 0.69 | 0.00 | 0.00 | 0.06 | 0.12 | 0.16 | 0.97 | 0.28 | 0.35 | 0.02 | 0.11 | 0.02 | 0.03 | 0.32 | 0.59 | 0.92|
| dec-waitk rank |  |  | 3 | 1 | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 818 | 27 | 2 | 1 | 1 | 0 | 0 | 0 | 4 | 3 | 1 | 3 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.17 | -3.19 | -1.81 | -2.56 | -3.82 | -2.31 | -2.61 | -2.29 | -2.38 | -2.50 | -2.98 | -4.81 | -3.12 | -4.13 | -3.28 | -1.09 | -3.00 | -4.36 | -5.37 | -2.53 | -5.58 | -4.53 | -3.32 | -2.62 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.91 | -1.80 | -3.56 | -3.59 | -3.67 | -2.00 | -2.05 | -2.07 | -3.81 | -2.21 | -3.93 | -3.40 | -3.27 | -3.63 | -2.88 | -1.39 | -3.05 | -4.05 | -5.23 | -2.08 | -5.45 | -4.37 | -3.28 | -1.98 | -1.66|
| full sent prob |  |  | 0.02 | 0.41 | 0.39 | 0.09 | 0.05 | 0.55 | 0.68 | 0.66 | 0.62 | 0.12 | 0.00 | 0.40 | 0.01 | 0.34 | 0.17 | 0.95 | 0.22 | 0.38 | 0.02 | 0.12 | 0.02 | 0.02 | 0.45 | 0.59 | 0.92|
| full sent rank |  |  | 7 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 349 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 9 | 2 | 1 | 7 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.56 | -2.48 | -2.98 | -2.84 | -2.87 | -2.29 | -1.84 | -2.07 | -2.63 | -4.20 | -3.14 | -3.03 | -1.48 | -3.69 | -3.06 | -1.19 | -2.92 | -4.14 | -5.25 | -2.45 | -5.60 | -4.32 | -2.84 | -2.73 | -1.57|
| full sent KL (full->waitk) |  |  | -3.90 | -1.96 | -3.49 | -3.61 | -3.69 | -2.03 | -2.13 | -2.15 | -3.79 | -1.90 | -3.93 | -3.47 | -3.31 | -3.66 | -2.89 | -1.38 | -3.04 | -4.05 | -5.23 | -2.09 | -5.45 | -4.37 | -3.32 | -1.98 | -1.66|
| dec-waitktgt |  |  | this | the | weekend | &apos;s | the | is | also | the | church | house | of | and | . | the | is | place | in | the | city | centre | st. | ran@@ | run | . | </s>|
| full sent tgt |  |  | this | this | weekend | the | the | is | also | the | church | and | of | festival | . | which | is | place | in | the | middle | centre | st. | ran@@ | run | . | </s>|
| ref | the | kir@@ | ch@@ | en-@@ | haus@@ | en | kir@@ | chen@@ | fest | festival | will | also | be | held | on | this | celebr@@ | atory | weekend | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | an@@ | lässlich | des | gei@@ | sin@@ | ger | stadt@@ | ju@@ | bi@@ | lä@@ | ums | wird | auch | noch | eine | neue | ch@@ | roni@@ | k | heraus@@ | gebracht | .|
| waitk tgt |  |  | on | the | occasion | of | the | ge@@ | is@@ | inger | city | anniversary | , | the | exhibition | will | be | accompanied | by | a | new | chron@@ | ic@@ | le | . | </s>|
| waitk prob |  |  | 0.25 | 0.82 | 0.83 | 0.90 | 0.79 | 0.66 | 0.80 | 0.52 | 0.61 | 0.58 | 0.53 | 0.20 | 0.03 | 0.31 | 0.34 | 0.11 | 0.91 | 0.72 | 0.75 | 0.88 | 0.83 | 0.82 | 0.85 | 0.91|
| dec-waitk prob |  |  | 0.39 | 0.86 | 0.97 | 0.92 | 0.65 | 0.48 | 0.91 | 0.83 | 0.77 | 0.56 | 0.45 | 0.17 | 0.01 | 0.39 | 0.15 | 0.01 | 0.89 | 0.50 | 0.87 | 0.85 | 0.95 | 0.90 | 0.87 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 1 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.00 | -1.69 | -0.96 | -1.49 | -2.16 | -3.05 | -1.33 | -1.63 | -1.87 | -2.73 | -3.35 | -4.06 | -5.39 | -3.07 | -3.20 | -4.08 | -1.78 | -2.57 | -1.67 | -1.59 | -1.11 | -1.36 | -1.84 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.82 | -2.19 | -1.99 | -1.69 | -2.11 | -2.63 | -2.09 | -3.07 | -2.26 | -2.57 | -2.86 | -3.91 | -6.19 | -3.51 | -2.89 | -4.56 | -1.45 | -1.95 | -2.64 | -1.62 | -1.94 | -1.78 | -1.92 | -1.64|
| full sent prob |  |  | 0.11 | 0.82 | 0.96 | 0.92 | 0.83 | 0.77 | 0.95 | 0.85 | 0.59 | 0.39 | 0.28 | 0.02 | 0.00 | 0.31 | 0.19 | 0.01 | 0.86 | 0.58 | 0.88 | 0.88 | 0.92 | 0.88 | 0.85 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 43 | 0 | 1 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.76 | -2.06 | -0.97 | -1.51 | -1.93 | -2.00 | -1.06 | -1.41 | -2.95 | -2.84 | -2.76 | -2.43 | -4.64 | -2.93 | -2.73 | -5.05 | -1.90 | -2.46 | -1.60 | -1.43 | -1.28 | -1.49 | -1.94 | -1.59|
| full sent KL (full->waitk) |  |  | -3.77 | -2.16 | -1.98 | -1.69 | -2.23 | -2.78 | -2.12 | -3.08 | -2.17 | -2.50 | -2.80 | -3.96 | -6.19 | -3.49 | -2.92 | -4.55 | -1.44 | -2.00 | -2.64 | -1.65 | -1.92 | -1.76 | -1.90 | -1.63|
| dec-waitktgt |  |  | on | the | occasion | of | the | ge@@ | is@@ | inger | city | anniversary | , | the | event | will | also | held | by | a | new | chron@@ | ic@@ | le | . | </s>|
| full sent tgt |  |  | a | the | occasion | of | the | ge@@ | is@@ | inger | city | anniversary | , | a | new | will | also | presented | by | a | new | chron@@ | ic@@ | le | . | </s>|
| ref | on | the | occasion | of | the | ge@@ | is@@ | ingen | town | anniversary | , | a | new | chron@@ | ic@@ | le | will | also | be | published | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | neue | ch@@ | roni@@ | k | soll | dann | am | 21. | oder | 22. | november | in | der | neuen | fest@@ | halle | in | gei@@ | sin@@ | gen | vorgestellt | werden | .|
| waitk tgt |  |  | the | new | chron@@ | ic@@ | le | will | be | published | on | 21 | or | 22 | november | in | the | new | f@@ | es@@ | th@@ | al@@ | le | in | ge@@ | is@@ | ingen | . | </s>|
| waitk prob |  |  | 0.57 | 0.65 | 0.85 | 0.80 | 0.75 | 0.30 | 0.59 | 0.26 | 0.78 | 0.47 | 0.70 | 0.91 | 0.96 | 0.69 | 0.81 | 0.75 | 0.35 | 0.99 | 0.99 | 0.93 | 0.97 | 0.87 | 0.84 | 0.81 | 0.84 | 0.82 | 0.91|
| dec-waitk prob |  |  | 0.78 | 0.85 | 0.95 | 0.80 | 0.91 | 0.13 | 0.19 | 0.01 | 0.27 | 0.36 | 0.72 | 0.96 | 0.95 | 0.08 | 0.78 | 0.34 | 0.14 | 0.98 | 0.95 | 0.94 | 1.00 | 0.79 | 0.91 | 0.99 | 0.60 | 0.85 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 7 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.01 | -1.85 | -1.12 | -2.15 | -1.23 | -3.99 | -3.03 | -2.70 | -3.56 | -1.98 | -2.06 | -1.08 | -1.27 | -2.63 | -2.31 | -2.84 | -4.10 | -0.99 | -1.11 | -1.05 | -0.83 | -2.02 | -1.30 | -0.76 | -2.75 | -1.79 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.39 | -3.32 | -1.90 | -1.89 | -1.69 | -2.74 | -2.28 | -3.17 | -1.70 | -2.00 | -1.98 | -1.46 | -1.19 | -1.95 | -2.15 | -2.13 | -2.70 | -0.86 | -0.84 | -1.28 | -1.10 | -1.76 | -1.82 | -2.08 | -1.32 | -1.96 | -1.67|
| full sent prob |  |  | 0.62 | 0.86 | 0.94 | 0.83 | 0.79 | 0.45 | 0.73 | 0.01 | 0.53 | 0.45 | 0.62 | 0.95 | 0.94 | 0.45 | 0.86 | 0.58 | 0.25 | 0.99 | 0.92 | 0.95 | 1.00 | 0.85 | 0.94 | 0.99 | 0.54 | 0.84 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.91 | -1.70 | -1.15 | -1.96 | -1.75 | -2.27 | -1.88 | -2.30 | -2.61 | -2.03 | -2.42 | -1.13 | -1.31 | -2.21 | -1.82 | -2.07 | -3.35 | -0.91 | -1.31 | -1.08 | -0.83 | -1.82 | -1.17 | -0.76 | -3.00 | -1.87 | -1.63|
| full sent KL (full->waitk) |  |  | -3.31 | -3.32 | -1.89 | -1.91 | -1.62 | -2.82 | -2.51 | -3.15 | -1.86 | -2.02 | -1.92 | -1.45 | -1.18 | -2.17 | -2.20 | -2.28 | -2.74 | -0.87 | -0.81 | -1.29 | -1.10 | -1.80 | -1.84 | -2.08 | -1.28 | -1.95 | -1.66|
| dec-waitktgt |  |  | the | new | chron@@ | ic@@ | le | should | then | on | on | november | or | 22 | november | . | the | ne@@ | fe@@ | es@@ | th@@ | al@@ | le | in | ge@@ | is@@ | ingen | . | </s>|
| full sent tgt |  |  | the | new | chron@@ | ic@@ | le | will | be | presented | on | 21 | or | 22 | november | in | the | new | fe@@ | es@@ | th@@ | al@@ | le | in | ge@@ | is@@ | ingen | . | </s>|
| ref | the | new | chron@@ | ic@@ | le | is | to | be | presented | on | 21 | or | 22 | november | in | the | new | festival | hall | in | ge@@ | is@@ | ingen | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | 20@@ | 14 | ist | aber | auch | sonst | ein | jahr | mit | vielen | ju@@ | bi@@ | lä@@ | en | .|
| waitk tgt |  |  | in | 20@@ | 14 | , | however | , | another | year | with | many | anniversary | celebra@@ | tions | . | </s>|
| waitk prob |  |  | 0.30 | 0.94 | 0.93 | 0.73 | 0.49 | 0.91 | 0.21 | 0.87 | 0.30 | 0.82 | 0.26 | 0.09 | 0.93 | 0.47 | 0.91|
| dec-waitk prob |  |  | 0.00 | 0.98 | 0.97 | 0.76 | 0.49 | 0.91 | 0.10 | 0.92 | 0.05 | 0.43 | 0.06 | 0.21 | 0.88 | 0.23 | 0.92|
| dec-waitk rank |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 2 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -0.58 | -0.97 | -1.08 | -2.18 | -2.35 | -1.58 | -3.45 | -1.41 | -3.02 | -3.02 | -1.67 | -4.16 | -1.76 | -3.01 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.47 | -1.38 | -1.41 | -2.40 | -2.69 | -1.60 | -3.51 | -1.85 | -3.11 | -1.43 | -3.81 | -4.87 | -1.31 | -2.84 | -1.65|
| full sent prob |  |  | 0.06 | 0.49 | 0.94 | 0.56 | 0.47 | 0.91 | 0.03 | 0.90 | 0.15 | 0.68 | 0.05 | 0.11 | 0.88 | 0.22 | 0.91|
| full sent rank |  |  | 3 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 2 | 0 | 2 | 1 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -3.56 | -3.28 | -1.28 | -2.88 | -3.03 | -1.64 | -3.73 | -1.63 | -3.06 | -2.23 | -3.03 | -4.44 | -1.75 | -2.83 | -1.58|
| full sent KL (full->waitk) |  |  | -3.36 | -1.00 | -1.39 | -2.28 | -2.66 | -1.59 | -3.50 | -1.83 | -3.14 | -1.59 | -3.77 | -4.86 | -1.32 | -2.84 | -1.65|
| dec-waitktgt |  |  | 20@@ | 20@@ | 14 | , | however | , | it | year | is | many | ju@@ | celebra@@ | tions | is | </s>|
| full sent tgt |  |  | 20@@ | 20@@ | 14 | , | however | , | it | year | is | many | ju@@ | . | tions | is | </s>|
| ref | however | , | 20@@ | 14 | is | also | a | year | of | many | anni@@ | vers@@ | aries | in | other | respects | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | ur@@ | kunde | wurde | in | kirchen | ( | haus@@ | en | ) | ge@@ | fertigt | , | das | damals | gericht@@ | splatz | war | .|
| waitk tgt |  |  | the | certificate | was | issued | in | churches | ( | houses | ) | . | </s>|
| waitk prob |  |  | 0.54 | 0.38 | 0.69 | 0.24 | 0.79 | 0.69 | 0.62 | 0.24 | 0.91 | 0.26 | 0.55|
| dec-waitk prob |  |  | 0.62 | 0.13 | 0.70 | 0.05 | 0.89 | 0.72 | 0.88 | 0.00 | 0.91 | 0.03 | 0.92|
| dec-waitk rank |  |  | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 6 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.57 | -3.46 | -2.05 | -2.94 | -1.54 | -2.60 | -1.63 | -1.13 | -1.61 | -1.36 | -1.22|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.47 | -3.00 | -2.02 | -3.76 | -2.12 | -2.60 | -2.93 | -3.49 | -1.60 | -2.85 | -2.98|
| full sent prob |  |  | 0.59 | 0.16 | 0.83 | 0.07 | 0.83 | 0.39 | 0.82 | 0.00 | 0.91 | 0.01 | 0.64|
| full sent rank |  |  | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 4 | 0 | 5 | 0|
| full sent KL (waitk->full) |  |  | -2.91 | -3.06 | -1.68 | -4.13 | -1.81 | -2.47 | -1.79 | -1.04 | -1.62 | -2.22 | -2.11|
| full sent KL (full->waitk) |  |  | -3.46 | -3.03 | -2.10 | -3.75 | -2.08 | -2.42 | -2.90 | -3.49 | -1.60 | -2.96 | -2.86|
| dec-waitktgt |  |  | the | document | was | given | in | churches | ( | haus@@ | ) | </s> | </s>|
| full sent tgt |  |  | the | document | was | produced | in | churches | ( | haus@@ | ) | , | </s>|
| ref | the | de@@ | ed | was | drawn | up | in | kir@@ | chen | ( | haus@@ | en | ) | , | which | at | the | time | was | the | location | of | the | cour@@ | thouse | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | soll | der | bahn@@ | übergang | &quot; | am | hir@@ | schen | &quot; | auf@@ | w@@ | än@@ | dig | um@@ | gebaut | werden | , | um | die | verkehr@@ | ssicherheit | zu | erhöhen | ?|
| waitk tgt |  |  | if | the | railway | crossing | is | to | be | opened | &quot; | at | h@@ | ir@@ | sch@@ | en | &quot; | in | a | complex | way | to | increase | traffic | safety | ? | </s>|
| waitk prob |  |  | 0.22 | 0.53 | 0.23 | 0.21 | 0.51 | 0.58 | 0.69 | 0.28 | 0.31 | 0.46 | 0.66 | 0.96 | 0.95 | 0.97 | 0.91 | 0.13 | 0.50 | 0.27 | 0.59 | 0.43 | 0.58 | 0.44 | 0.76 | 0.73 | 0.90|
| dec-waitk prob |  |  | 0.01 | 0.31 | 0.13 | 0.07 | 0.65 | 0.82 | 0.40 | 0.02 | 0.21 | 0.43 | 0.04 | 0.88 | 0.88 | 0.98 | 0.82 | 0.01 | 0.17 | 0.26 | 0.52 | 0.07 | 0.50 | 0.15 | 0.85 | 0.29 | 0.92|
| dec-waitk rank |  |  | 7 | 0 | 0 | 2 | 0 | 0 | 0 | 6 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.21 | -3.54 | -4.65 | -4.07 | -2.45 | -1.82 | -2.74 | -4.09 | -3.34 | -3.01 | -3.22 | -1.53 | -1.16 | -0.93 | -2.16 | -2.07 | -3.11 | -3.00 | -2.62 | -2.00 | -2.62 | -1.85 | -1.62 | -3.41 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.45 | -2.74 | -4.29 | -4.68 | -3.06 | -3.22 | -2.46 | -3.87 | -3.06 | -2.87 | -1.51 | -1.09 | -0.92 | -1.03 | -1.53 | -4.58 | -2.64 | -4.01 | -1.64 | -2.43 | -2.02 | -1.94 | -1.65 | -2.38 | -1.72|
| full sent prob |  |  | 0.01 | 0.24 | 0.04 | 0.10 | 0.21 | 0.71 | 0.57 | 0.00 | 0.19 | 0.40 | 0.07 | 0.92 | 0.90 | 0.98 | 0.85 | 0.08 | 0.03 | 0.12 | 0.59 | 0.23 | 0.49 | 0.16 | 0.83 | 0.05 | 0.91|
| full sent rank |  |  | 10 | 0 | 5 | 1 | 1 | 0 | 0 | 88 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -2.62 | -3.36 | -4.18 | -4.15 | -2.78 | -2.38 | -2.74 | -4.28 | -3.27 | -3.04 | -3.02 | -1.29 | -1.07 | -0.97 | -1.97 | -2.51 | -1.87 | -3.83 | -2.79 | -2.49 | -2.65 | -1.86 | -1.74 | -1.58 | -1.64|
| full sent KL (full->waitk) |  |  | -3.49 | -2.72 | -4.28 | -4.68 | -2.90 | -3.16 | -2.55 | -3.86 | -3.05 | -2.86 | -1.53 | -1.12 | -0.93 | -1.03 | -1.56 | -4.58 | -2.57 | -3.98 | -1.65 | -2.46 | -2.01 | -1.94 | -1.63 | -2.23 | -1.71|
| dec-waitktgt |  |  | should | the | railway | is | is | to | be | carried | &quot; | at | the | ir@@ | sch@@ | en | &quot; | , | order | lab@@ | way | , | increase | road | safety | , | </s>|
| full sent tgt |  |  | should | the | train | transition | &quot; | to | be | &quot; | &quot; | at | the | ir@@ | sch@@ | en | &quot; | , | order | lab@@ | way | , | increase | road | safety | , | </s>|
| ref | should | the | &quot; | am | h@@ | ir@@ | sch@@ | en | &quot; | railway | crossing | be | re@@ | constructed | at | great | cost | , | in | order | to | increase | traffic | safety | ? | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | schil@@ | ta@@ | ch | muss | dafür | 2@@ | 20 | 000 | euro | in | die | hand | nehmen | .|
| waitk tgt |  |  | sch@@ | il@@ | t@@ | ach | must | be | eur | 2@@ | 20 | 000 | for | this | . | </s>|
| waitk prob |  |  | 0.56 | 0.78 | 0.97 | 0.79 | 0.39 | 0.29 | 0.10 | 0.96 | 0.90 | 0.94 | 0.49 | 0.58 | 0.81 | 0.90|
| dec-waitk prob |  |  | 0.36 | 0.83 | 0.82 | 0.06 | 0.69 | 0.13 | 0.37 | 0.94 | 0.90 | 0.96 | 0.50 | 0.69 | 0.41 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.33 | -1.17 | -1.88 | -4.03 | -2.08 | -3.89 | -3.07 | -1.35 | -1.36 | -1.15 | -2.27 | -1.88 | -1.91 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.96 | -1.55 | -0.94 | -1.00 | -2.76 | -3.38 | -4.72 | -1.11 | -1.48 | -1.36 | -2.35 | -2.17 | -1.89 | -1.69|
| full sent prob |  |  | 0.20 | 0.84 | 0.89 | 0.93 | 0.33 | 0.03 | 0.13 | 0.94 | 0.86 | 0.95 | 0.35 | 0.67 | 0.50 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.77 | -1.24 | -1.60 | -1.21 | -2.77 | -4.37 | -3.71 | -1.34 | -1.53 | -1.25 | -2.54 | -1.92 | -1.97 | -1.60|
| full sent KL (full->waitk) |  |  | -2.89 | -1.55 | -1.00 | -1.57 | -2.69 | -3.35 | -4.70 | -1.11 | -1.45 | -1.35 | -2.32 | -2.16 | -1.95 | -1.69|
| dec-waitktgt |  |  | sch@@ | il@@ | t@@ | ta@@ | must | do | eur | 2@@ | 20 | 000 | for | this | purpose | </s>|
| full sent tgt |  |  | sch@@ | il@@ | t@@ | ach | must | therefore | in | 2@@ | 20 | 000 | for | this | . | </s>|
| ref | sch@@ | il@@ | t@@ | ach | will | have | to | contribute | up | to | eur | 2@@ | 20@@ | ,000 | to | the | project | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | deutsche | bahn | will | im | kommenden | jahr | die | kin@@ | zi@@ | g@@ | tal@@ | -@@ | bahn@@ | strecke | verbessern | .|
| waitk tgt |  |  | deutsche | bahn | wants | to | make | the | cinema | show | a | success | this | coming | year | . | </s>|
| waitk prob |  |  | 0.66 | 0.86 | 0.30 | 0.82 | 0.05 | 0.38 | 0.21 | 0.30 | 0.11 | 0.15 | 0.32 | 0.40 | 0.88 | 0.66 | 0.91|
| dec-waitk prob |  |  | 0.40 | 0.97 | 0.88 | 0.57 | 0.02 | 0.17 | 0.03 | 0.00 | 0.04 | 0.11 | 0.06 | 0.51 | 0.94 | 0.79 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 9 | 1 | 2 | 2664 | 5 | 1 | 5 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.31 | -1.01 | -1.11 | -2.53 | -3.90 | -2.96 | -5.07 | -4.31 | -3.37 | -3.08 | -3.34 | -1.73 | -1.25 | -2.16 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.19 | -1.96 | -3.33 | -1.90 | -5.00 | -3.63 | -4.28 | -3.84 | -4.19 | -4.41 | -2.97 | -2.75 | -1.79 | -2.19 | -1.67|
| full sent prob |  |  | 0.09 | 0.97 | 0.30 | 0.88 | 0.01 | 0.50 | 0.00 | 0.00 | 0.11 | 0.00 | 0.07 | 0.57 | 0.92 | 0.89 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 5 | 0 | 10 | 1546 | 1 | 17 | 4 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.06 | -0.99 | -2.73 | -1.72 | -1.49 | -2.86 | -3.99 | -3.60 | -2.66 | -0.67 | -2.82 | -1.91 | -1.38 | -1.53 | -1.58|
| full sent KL (full->waitk) |  |  | -2.04 | -1.96 | -3.21 | -2.11 | -5.00 | -3.71 | -4.30 | -3.84 | -4.19 | -4.37 | -2.98 | -2.74 | -1.77 | -2.24 | -1.67|
| dec-waitktgt |  |  | deutsche | bahn | wants | to | see | its | kin@@ | available | up | reality | in | coming | year | . | </s>|
| full sent tgt |  |  | the | bahn | wants | to | improve | the | kin@@ | line | better | better | in | coming | year | . | </s>|
| ref | the | deutsche | bahn | hopes | to | improve | the | kin@@ | zi@@ | g@@ | tal | railway | line | in | the | coming | year | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dort | plan@@ | t | die | stadt | , | in | höhe | des | dor@@ | tigen | tun@@ | n@@ | el@@ | m@@ | un@@ | des | west@@ | lich | der | bahn@@ | glei@@ | se | eine | aus@@ | bu@@ | chtung | zu | bauen | .|
| waitk tgt |  |  | the | commission | is | planning | to | invest | in | the | amount | of | the | tunnel | m@@ | ill | there | in | the | west | of | the | railway | track | . | </s>|
| waitk prob |  |  | 0.14 | 0.22 | 0.15 | 0.60 | 0.69 | 0.10 | 0.19 | 0.32 | 0.12 | 0.90 | 0.47 | 0.77 | 0.14 | 0.57 | 0.40 | 0.27 | 0.61 | 0.68 | 0.80 | 0.85 | 0.82 | 0.60 | 0.56 | 0.91|
| dec-waitk prob |  |  | 0.07 | 0.00 | 0.09 | 0.61 | 0.55 | 0.01 | 0.49 | 0.35 | 0.00 | 0.79 | 0.19 | 0.65 | 0.00 | 0.00 | 0.75 | 0.05 | 0.77 | 0.63 | 0.20 | 0.80 | 0.49 | 0.05 | 0.89 | 0.93|
| dec-waitk rank |  |  | 4 | 64 | 1 | 0 | 0 | 15 | 0 | 0 | 21 | 0 | 0 | 0 | 713 | 20 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.13 | -3.95 | -4.43 | -2.80 | -2.93 | -4.61 | -3.11 | -3.83 | -5.18 | -2.19 | -4.26 | -2.35 | -2.16 | -4.58 | -1.60 | -1.60 | -1.95 | -2.70 | -1.83 | -2.17 | -2.67 | -2.60 | -1.53 | -1.47|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.37 | -5.01 | -4.27 | -2.80 | -2.26 | -4.53 | -3.77 | -4.52 | -5.02 | -1.60 | -2.53 | -1.36 | -4.74 | -2.00 | -3.23 | -2.77 | -2.17 | -1.52 | -1.74 | -1.95 | -1.40 | -1.71 | -2.64 | -1.68|
| full sent prob |  |  | 0.20 | 0.00 | 0.06 | 0.03 | 0.67 | 0.00 | 0.15 | 0.26 | 0.00 | 0.86 | 0.53 | 0.38 | 0.00 | 0.00 | 0.24 | 0.02 | 0.13 | 0.81 | 0.56 | 0.86 | 0.42 | 0.44 | 0.81 | 0.91|
| full sent rank |  |  | 0 | 4205 | 2 | 4 | 0 | 45 | 1 | 0 | 24 | 0 | 0 | 1 | 240 | 25 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.83 | -3.69 | -4.61 | -4.73 | -2.51 | -3.58 | -3.42 | -4.43 | -5.10 | -1.99 | -2.98 | -2.13 | -4.99 | -3.18 | -3.42 | -2.07 | -3.20 | -1.43 | -2.94 | -1.81 | -2.21 | -2.56 | -1.87 | -1.59|
| full sent KL (full->waitk) |  |  | -4.39 | -5.02 | -4.27 | -2.51 | -2.32 | -4.54 | -3.73 | -4.50 | -5.02 | -1.65 | -2.67 | -1.24 | -4.74 | -2.02 | -3.07 | -2.84 | -1.88 | -1.64 | -1.97 | -1.99 | -1.35 | -1.91 | -2.60 | -1.67|
| dec-waitktgt |  |  | planning | plan | has | planning | to | make | in | the | city | of | the | tunnel | there | ound | there | . | the | west | . | the | railway | . | . | </s>|
| full sent tgt |  |  | the | city | has | currently | to | build | a | the | construction | of | the | tun@@ | to | ound | there | west | western | west | of | the | railway | track | . | </s>|
| ref | at | the | crossing | , | the | town | is | planning | to | increase | the | height | of | the | mouth | of | the | tunnel | to | the | west | of | the | railway | line | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | bürger@@ | meister | thomas | ha@@ | as | wider@@ | sprach | : | der | bahn@@ | übergang | &quot; | hir@@ | schen | &quot; | werde | regelmäßig | für | lang@@ | holz@@ | transpor@@ | te | genutzt | .|
| waitk tgt |  |  | may@@ | or | thomas | ha@@ | as | dis@@ | agreed | : | the | railway | crossing | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | was | regularly | used | for | long-@@ | distance | transport | . | </s>|
| waitk prob |  |  | 0.71 | 0.95 | 0.90 | 0.94 | 0.94 | 0.48 | 0.55 | 0.85 | 0.83 | 0.32 | 0.49 | 0.82 | 0.86 | 0.99 | 0.95 | 0.98 | 0.92 | 0.33 | 0.16 | 0.56 | 0.85 | 0.43 | 0.38 | 0.42 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.67 | 0.82 | 0.33 | 0.89 | 0.93 | 0.01 | 0.50 | 0.37 | 0.00 | 0.10 | 0.12 | 0.23 | 0.84 | 0.96 | 0.88 | 0.92 | 0.88 | 0.00 | 0.35 | 0.12 | 0.66 | 0.62 | 0.29 | 0.22 | 0.85 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 15 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.79 | -2.24 | -2.07 | -1.66 | -1.38 | -3.86 | -2.38 | -1.95 | -0.97 | -4.41 | -4.63 | -3.46 | -1.92 | -1.13 | -1.34 | -1.39 | -1.75 | -1.07 | -3.81 | -4.65 | -2.30 | -2.04 | -4.31 | -3.22 | -1.94 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.25 | -1.09 | -0.98 | -1.26 | -1.38 | -2.40 | -3.11 | -1.45 | -1.49 | -3.52 | -3.25 | -1.29 | -1.67 | -0.86 | -0.96 | -0.93 | -1.52 | -2.54 | -4.25 | -2.81 | -1.66 | -2.44 | -2.98 | -2.74 | -1.78 | -1.63|
| full sent prob |  |  | 0.91 | 0.92 | 0.96 | 0.94 | 0.92 | 0.05 | 0.85 | 0.54 | 0.75 | 0.24 | 0.20 | 0.64 | 0.92 | 0.99 | 0.92 | 0.98 | 0.92 | 0.12 | 0.46 | 0.92 | 0.79 | 0.64 | 0.25 | 0.16 | 0.85 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.22 | -1.49 | -1.09 | -1.35 | -1.53 | -3.46 | -1.35 | -2.42 | -2.41 | -2.70 | -4.03 | -2.72 | -1.36 | -0.94 | -1.23 | -1.01 | -1.51 | -2.44 | -1.99 | -1.13 | -1.99 | -1.97 | -4.33 | -3.30 | -1.89 | -1.58|
| full sent KL (full->waitk) |  |  | -2.40 | -1.17 | -1.44 | -1.29 | -1.37 | -2.44 | -3.26 | -1.57 | -2.00 | -3.57 | -3.29 | -1.56 | -1.73 | -0.89 | -0.99 | -0.97 | -1.54 | -2.71 | -4.30 | -3.18 | -1.75 | -2.44 | -2.97 | -2.73 | -1.78 | -1.62|
| dec-waitktgt |  |  | may@@ | or | of | ha@@ | as | </s> | agreed | </s> | </s> | train | transition | </s> | h@@ | ir@@ | sch@@ | en | &quot; | </s> | regularly | used | for | long-@@ | distance | trans@@ | . | </s>|
| full sent tgt |  |  | may@@ | or | thomas | ha@@ | as | contradic@@ | agreed | : | the | train | transition | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | is | regularly | used | for | long-@@ | distance | trans@@ | . | </s>|
| ref | may@@ | or | thomas | ha@@ | as | re@@ | tor@@ | ted | : | the | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | railway | crossing | is | used | regularly | for | the | transportation | of | long | log@@ | s | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | rä@@ | te | kamen | überein | , | untersuchen | zu | lassen | , | welche | kosten | die | ange@@ | da@@ | chte | verbrei@@ | ter@@ | ung | der | straße | verursachen | würde | .|
| waitk tgt |  |  | the | counc@@ | ils | agreed | to | investigate | how | the | eu | &apos;s | financial | resources | are | to | be | used | to | spread | the | road | . | </s>|
| waitk prob |  |  | 0.54 | 0.73 | 0.91 | 0.95 | 0.46 | 0.36 | 0.21 | 0.29 | 0.04 | 0.22 | 0.04 | 0.29 | 0.19 | 0.30 | 0.85 | 0.19 | 0.53 | 0.21 | 0.56 | 0.37 | 0.45 | 0.90|
| dec-waitk prob |  |  | 0.65 | 0.82 | 0.97 | 0.71 | 0.48 | 0.48 | 0.00 | 0.03 | 0.01 | 0.03 | 0.03 | 0.02 | 0.08 | 0.15 | 0.86 | 0.03 | 0.01 | 0.01 | 0.52 | 0.29 | 0.00 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 23 | 7 | 5 | 6 | 1 | 8 | 2 | 0 | 0 | 6 | 5 | 9 | 0 | 0 | 5 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.35 | -1.97 | -1.03 | -2.13 | -2.39 | -2.42 | -1.41 | -3.85 | -5.16 | -5.09 | -5.54 | -3.97 | -3.22 | -4.47 | -1.87 | -4.76 | -2.86 | -5.12 | -3.29 | -4.33 | -1.16 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.16 | -2.51 | -1.56 | -0.98 | -2.20 | -2.11 | -2.70 | -4.14 | -5.72 | -3.82 | -5.02 | -3.35 | -3.40 | -3.31 | -1.98 | -3.18 | -2.00 | -3.19 | -3.05 | -3.11 | -2.11 | -1.70|
| full sent prob |  |  | 0.66 | 0.89 | 0.92 | 0.96 | 0.85 | 0.14 | 0.07 | 0.00 | 0.00 | 0.34 | 0.00 | 0.01 | 0.02 | 0.07 | 0.67 | 0.01 | 0.33 | 0.09 | 0.71 | 0.44 | 0.45 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 6 | 476 | 0 | 1812 | 10 | 4 | 3 | 0 | 29 | 0 | 3 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.40 | -1.20 | -1.47 | -1.07 | -1.61 | -2.89 | -2.03 | -0.63 | -2.48 | -3.08 | -2.49 | -4.76 | -2.34 | -4.08 | -2.64 | -4.36 | -2.59 | -3.20 | -2.33 | -3.13 | -3.44 | -1.58|
| full sent KL (full->waitk) |  |  | -3.16 | -2.56 | -1.53 | -1.17 | -2.30 | -1.97 | -2.79 | -4.14 | -5.72 | -3.87 | -5.02 | -3.35 | -3.38 | -3.31 | -1.85 | -3.19 | -2.15 | -3.25 | -3.14 | -3.17 | -2.28 | -1.69|
| dec-waitktgt |  |  | the | counc@@ | ils | agreed | to | investigate | </s> | to | council | should | budget | situation | were | to | be | spent | . | fund | the | road | </s> | </s>|
| full sent tgt |  |  | the | counc@@ | ils | agreed | to | have | the | much | planned | &apos;s | planned | interests | would | being | be | increased | to | increase | the | road | . | </s>|
| ref | the | counc@@ | ill@@ | ors | agreed | to | have | an | investigation | conducted | as | to | what | costs | the | planned | wid@@ | ening | of | the | road | would | inc@@ | ur | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | verantwortung | hierfür | tra@@ | ge | wiederum | die | stadt | als | straßen@@ | bau@@ | last@@ | trä@@ | ger@@ | in | .|
| waitk tgt |  |  | the | responsibility | for | this | lies | with | the | city | as | a | road | load | carrier | . | </s>|
| waitk prob |  |  | 0.36 | 0.60 | 0.69 | 0.72 | 0.38 | 0.76 | 0.85 | 0.80 | 0.64 | 0.63 | 0.60 | 0.33 | 0.66 | 0.87 | 0.91|
| dec-waitk prob |  |  | 0.12 | 0.94 | 0.57 | 0.56 | 0.40 | 0.41 | 0.82 | 0.74 | 0.27 | 0.64 | 0.18 | 0.01 | 0.49 | 0.80 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 18 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.45 | -1.00 | -2.31 | -2.67 | -2.84 | -2.57 | -2.16 | -2.23 | -2.43 | -2.90 | -4.92 | -3.13 | -2.84 | -2.11 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.21 | -3.47 | -2.08 | -2.34 | -2.35 | -1.78 | -1.96 | -1.51 | -1.97 | -2.32 | -2.32 | -2.68 | -2.32 | -1.81 | -1.63|
| full sent prob |  |  | 0.47 | 0.14 | 0.74 | 0.70 | 0.29 | 0.55 | 0.83 | 0.76 | 0.51 | 0.73 | 0.39 | 0.01 | 0.83 | 0.76 | 0.92|
| full sent rank |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.25 | -3.68 | -2.07 | -2.36 | -3.10 | -2.52 | -2.08 | -1.84 | -2.33 | -2.19 | -3.65 | -3.62 | -1.47 | -2.23 | -1.57|
| full sent KL (full->waitk) |  |  | -3.19 | -3.08 | -2.17 | -2.41 | -2.32 | -1.87 | -1.97 | -1.53 | -2.10 | -2.37 | -2.42 | -2.72 | -2.50 | -1.79 | -1.62|
| dec-waitktgt |  |  | responsibility | responsibility | for | this | lies | with | the | city | itself | a | road | ha@@ | carrier | . | </s>|
| full sent tgt |  |  | the | city | for | this | lies | with | the | city | as | a | road | lo@@ | carrier | . | </s>|
| ref | the | town | , | as | the | authority | responsible | for | road | construction | , | would | then | bear | responsibility | for | this | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | selbst | züge | vom | hauptbahnhof | her | müssten | an | dieser | stelle | schon | soweit | ab@@ | geb@@ | re@@ | m@@ | st | sein | , | dass | keine | kol@@ | li@@ | sion | dro@@ | he | .|
| waitk tgt |  |  | even | trains | from | the | main | station | would | have | to | be | dro@@ | pped | here | so | far | that | the | train | station | is | not | in | danger | of | col@@ | li@@ | sion | . | </s>|
| waitk prob |  |  | 0.52 | 0.75 | 0.70 | 0.75 | 0.47 | 0.40 | 0.59 | 0.51 | 0.91 | 0.38 | 0.16 | 0.93 | 0.14 | 0.14 | 0.46 | 0.59 | 0.22 | 0.05 | 0.33 | 0.18 | 0.73 | 0.15 | 0.79 | 0.90 | 0.32 | 0.98 | 0.55 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.30 | 0.89 | 0.41 | 0.57 | 0.40 | 0.54 | 0.35 | 0.55 | 0.85 | 0.33 | 0.01 | 0.97 | 0.02 | 0.03 | 0.88 | 0.00 | 0.05 | 0.02 | 0.27 | 0.26 | 0.75 | 0.09 | 0.87 | 0.82 | 0.49 | 0.96 | 0.72 | 0.89 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 9 | 4 | 0 | 72 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.54 | -1.22 | -2.69 | -2.41 | -2.40 | -1.72 | -3.50 | -2.51 | -1.79 | -3.30 | -5.54 | -0.98 | -3.75 | -3.17 | -1.08 | -1.50 | -4.55 | -5.84 | -4.08 | -3.92 | -2.27 | -5.10 | -1.28 | -1.76 | -2.78 | -1.20 | -1.92 | -1.70 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.28 | -1.89 | -2.31 | -2.14 | -2.20 | -1.89 | -2.39 | -3.03 | -1.54 | -2.99 | -4.52 | -1.35 | -3.51 | -3.40 | -2.72 | -1.85 | -3.91 | -5.87 | -3.70 | -3.67 | -2.38 | -4.74 | -1.74 | -1.56 | -3.57 | -0.95 | -2.60 | -1.75 | -1.66|
| full sent prob |  |  | 0.24 | 0.89 | 0.63 | 0.66 | 0.45 | 0.53 | 0.39 | 0.80 | 0.84 | 0.74 | 0.00 | 0.82 | 0.03 | 0.09 | 0.85 | 0.69 | 0.01 | 0.01 | 0.01 | 0.09 | 0.42 | 0.46 | 0.96 | 0.90 | 0.56 | 0.97 | 0.69 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 151 | 0 | 5 | 1 | 0 | 0 | 5 | 9 | 12 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.55 | -1.24 | -2.74 | -2.29 | -2.34 | -1.83 | -2.77 | -1.67 | -1.89 | -1.90 | -4.29 | -2.10 | -3.32 | -3.73 | -1.30 | -2.25 | -1.68 | -3.53 | -3.44 | -3.16 | -3.58 | -2.48 | -0.92 | -1.59 | -2.50 | -1.13 | -2.03 | -1.69 | -1.59|
| full sent KL (full->waitk) |  |  | -3.25 | -1.89 | -2.43 | -2.19 | -2.22 | -1.88 | -2.42 | -3.14 | -1.54 | -3.11 | -4.52 | -1.23 | -3.52 | -3.38 | -2.71 | -2.20 | -3.88 | -5.87 | -3.63 | -3.65 | -2.19 | -4.79 | -1.79 | -1.63 | -3.59 | -0.96 | -2.59 | -1.76 | -1.66|
| dec-waitktgt |  |  | even | trains | from | the | main | station | would | have | to | be | replaced | pped | to | . | far | . | they | hotel | station | is | not | in | danger | of | col@@ | li@@ | sion | . | </s>|
| full sent tgt |  |  | even | trains | from | the | main | station | would | have | to | be | bra@@ | pped | to | to | far | that | no | col@@ | would | would | not | in | danger | of | col@@ | li@@ | sion | . | </s>|
| ref | the | trains | themselves | , | coming | from | the | central | station | , | must | also | be | sufficiently | slow@@ | ed | down | so | that | there | is | no | threat | of | col@@ | li@@ | sion | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | 30 | vorschläge | standen | zur | auswahl | , | fünf | sind | noch | im | rennen | .|
| waitk tgt |  |  | 30 | proposals | were | selected | , | five | are | still | in | the | race | . | </s>|
| waitk prob |  |  | 0.46 | 0.87 | 0.76 | 0.18 | 0.69 | 0.78 | 0.50 | 0.79 | 0.64 | 0.68 | 0.78 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.68 | 0.90 | 0.69 | 0.02 | 0.10 | 0.71 | 0.10 | 0.91 | 0.76 | 0.76 | 0.82 | 0.88 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 7 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.38 | -1.40 | -2.56 | -4.14 | -3.18 | -2.28 | -3.98 | -1.21 | -2.12 | -2.26 | -1.75 | -1.80 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.33 | -1.59 | -2.01 | -3.95 | -1.90 | -1.93 | -2.25 | -1.86 | -2.37 | -2.48 | -1.99 | -1.67 | -1.64|
| full sent prob |  |  | 0.20 | 0.28 | 0.66 | 0.01 | 0.41 | 0.61 | 0.64 | 0.89 | 0.74 | 0.78 | 0.77 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.83 | -4.23 | -2.43 | -3.09 | -2.36 | -2.59 | -2.15 | -1.29 | -2.15 | -2.16 | -2.04 | -1.84 | -1.59|
| full sent KL (full->waitk) |  |  | -2.12 | -1.15 | -1.99 | -3.95 | -2.08 | -1.87 | -2.45 | -1.84 | -2.36 | -2.49 | -1.95 | -1.67 | -1.63|
| dec-waitktgt |  |  | 30 | proposals | were | available | </s> | five | were | still | in | the | race | . | </s>|
| full sent tgt |  |  | 30 | proposals | were | available | , | five | are | still | in | the | race | . | </s>|
| ref | there | were | 30 | proposals | to | choose | from | , | five | of | which | are | still | in | the | running | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | mehr | als | 1000 | planeten | bei | anderen | ster@@ | nen | haben | ast@@ | ron@@ | omen | bereits | gefunden | .|
| waitk tgt |  |  | more | than | 1000 | plan@@ | ets | on | other | stars | have | a@@ | stronom@@ | ers | already | found | . | </s>|
| waitk prob |  |  | 0.52 | 0.92 | 0.51 | 0.81 | 0.97 | 0.40 | 0.72 | 0.80 | 0.82 | 0.74 | 0.95 | 0.85 | 0.46 | 0.67 | 0.86 | 0.91|
| dec-waitk prob |  |  | 0.52 | 0.92 | 0.35 | 0.92 | 0.90 | 0.13 | 0.83 | 0.64 | 0.00 | 0.73 | 0.98 | 0.97 | 0.20 | 0.39 | 0.83 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.59 | -1.55 | -2.72 | -1.33 | -1.55 | -2.97 | -1.78 | -3.03 | -2.30 | -2.33 | -0.94 | -1.02 | -2.14 | -3.06 | -1.95 | -1.48|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.11 | -1.49 | -2.23 | -1.88 | -1.00 | -2.98 | -2.37 | -1.55 | -1.44 | -2.32 | -1.22 | -1.86 | -2.88 | -2.07 | -1.86 | -1.67|
| full sent prob |  |  | 0.28 | 0.91 | 0.47 | 0.92 | 0.98 | 0.08 | 0.86 | 0.71 | 0.82 | 0.00 | 0.94 | 0.89 | 0.65 | 0.58 | 0.65 | 0.92|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.44 | -1.56 | -2.57 | -1.37 | -0.97 | -3.03 | -1.62 | -2.43 | -1.94 | -2.73 | -1.32 | -1.59 | -2.42 | -2.82 | -2.56 | -1.56|
| full sent KL (full->waitk) |  |  | -2.99 | -1.49 | -2.28 | -1.88 | -1.06 | -2.96 | -2.38 | -1.60 | -1.99 | -1.88 | -1.18 | -1.80 | -2.97 | -2.18 | -1.74 | -1.66|
| dec-waitktgt |  |  | more | than | 1000 | plan@@ | ets | in | other | stars | </s> | a@@ | stronom@@ | ers | . | found | . | </s>|
| full sent tgt |  |  | more | than | 1000 | plan@@ | ets | in | other | stars | have | already | stronom@@ | ers | already | found | . | </s>|
| ref | a@@ | stronom@@ | ers | have | already | found | more | than | 1@@ | ,000 | plan@@ | ets | near | other | stars | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ob | es | zumindest | auf | einigen | davon | leben | gibt | , | weiß | keiner | .|
| waitk tgt |  |  | whether | it | is | at | least | some | of | them | , | nobody | knows | . | </s>|
| waitk prob |  |  | 0.45 | 0.36 | 0.41 | 0.22 | 0.93 | 0.19 | 0.81 | 0.69 | 0.17 | 0.44 | 0.86 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.15 | 0.08 | 0.48 | 0.70 | 0.95 | 0.23 | 0.69 | 0.85 | 0.05 | 0.11 | 0.83 | 0.77 | 0.92|
| dec-waitk rank |  |  | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.61 | -1.69 | -2.80 | -1.85 | -1.24 | -3.37 | -2.43 | -1.36 | -3.01 | -2.36 | -1.66 | -2.26 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.11 | -2.83 | -2.94 | -4.21 | -1.38 | -3.76 | -2.00 | -1.62 | -3.79 | -1.96 | -1.63 | -1.56 | -1.65|
| full sent prob |  |  | 0.40 | 0.01 | 0.43 | 0.05 | 0.94 | 0.37 | 0.63 | 0.72 | 0.07 | 0.12 | 0.85 | 0.10 | 0.92|
| full sent rank |  |  | 0 | 4 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -3.09 | -1.45 | -2.80 | -3.42 | -1.32 | -3.09 | -2.41 | -1.71 | -3.14 | -2.99 | -1.58 | -2.49 | -1.58|
| full sent KL (full->waitk) |  |  | -3.19 | -2.77 | -2.93 | -4.09 | -1.37 | -3.78 | -1.96 | -1.56 | -3.79 | -1.92 | -1.65 | -1.07 | -1.64|
| dec-waitktgt |  |  | at | or | is | at | least | some | of | them | living | no | knows | . | </s>|
| full sent tgt |  |  | whether | there | is | alive | least | some | of | them | that | no | knows | , | </s>|
| ref | whether | or | not | life | exists | on | at | least | some | of | these | , | no-@@ | one | knows | . | </s>|


SENT

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | auswahl | fällt | schwer | : | soll | man | nach | gra@@ | vi@@ | ta@@ | tions@@ | w@@ | ellen | suchen | ?|
| waitk tgt |  |  | the | choice | is | difficult | : | should | you | go | to | gra@@ | vit@@ | ational | waves | ? | </s>|
| waitk prob |  |  | 0.41 | 0.49 | 0.69 | 0.67 | 0.83 | 0.19 | 0.55 | 0.16 | 0.62 | 0.92 | 0.76 | 0.89 | 0.72 | 0.88 | 0.90|
| dec-waitk prob |  |  | 0.65 | 0.76 | 0.84 | 0.38 | 0.83 | 0.00 | 0.32 | 0.41 | 0.70 | 0.67 | 0.50 | 0.94 | 0.95 | 0.85 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.28 | -1.62 | -1.83 | -2.87 | -2.00 | -2.29 | -3.08 | -3.21 | -2.34 | -2.48 | -2.13 | -1.10 | -0.90 | -1.80 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.87 | -2.13 | -2.74 | -1.99 | -1.90 | -3.73 | -2.58 | -3.70 | -2.51 | -1.17 | -1.20 | -1.31 | -2.43 | -1.79 | -1.73|
| full sent prob |  |  | 0.29 | 0.66 | 0.83 | 0.37 | 0.83 | 0.36 | 0.31 | 0.01 | 0.07 | 0.04 | 0.37 | 0.94 | 0.90 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 1 | 2 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.35 | -1.96 | -1.94 | -3.04 | -1.89 | -3.12 | -2.40 | -2.27 | -1.80 | -2.72 | -2.32 | -1.03 | -1.13 | -1.80 | -1.64|
| full sent KL (full->waitk) |  |  | -3.76 | -2.11 | -2.73 | -1.99 | -1.90 | -3.80 | -2.59 | -3.71 | -2.22 | -0.69 | -1.13 | -1.32 | -2.40 | -1.81 | -1.73|
| dec-waitktgt |  |  | the | choice | is | difficult | : | </s> | you | go | to | gra@@ | vit@@ | ational | waves | ? | </s>|
| full sent tgt |  |  | the | choice | is | difficult | : | should | one | search | for | search | vity | ational | waves | ? | </s>|
| ref | the | choice | is | a | difficult | one | : | should | we | search | for | gra@@ | vit@@ | ational | waves | ? | </s>|

PRED AVG SCORE: -0.7473, PRED PPL: 2.1113
GOLD AVG SCORE: 0.0000, GOLD PPL: 1.0000
