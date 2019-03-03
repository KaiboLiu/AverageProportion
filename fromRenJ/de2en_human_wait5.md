norm_stop False

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zwei | anlagen | so | nah | bei@@ | einander | : | absicht | oder | schil@@ | d@@ | bürger@@ | st@@ | reich | ?|
| waitk tgt |  |  |  |  | two | plants | so | close | together | : | intention | or | tor@@ | to@@ | ise | ? | </s>|
| waitk prob |  |  |  |  | 0.61 | 0.35 | 0.63 | 0.90 | 0.38 | 0.81 | 0.30 | 0.79 | 0.62 | 0.81 | 0.76 | 0.86 | 0.90|
| dec-waitk prob |  |  |  |  | 0.90 | 0.22 | 0.74 | 0.41 | 0.74 | 0.80 | 0.42 | 0.82 | 0.07 | 0.32 | 0.29 | 0.72 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.30 | -3.90 | -2.08 | -2.38 | -1.68 | -1.98 | -3.08 | -1.93 | -4.92 | -2.54 | -1.21 | -2.46 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.12 | -3.23 | -2.48 | -0.88 | -2.84 | -2.13 | -3.68 | -2.07 | -1.88 | -1.11 | -1.04 | -1.79 | -1.73|
| full sent prob |  |  |  |  | 0.62 | 0.25 | 0.72 | 0.64 | 0.67 | 0.85 | 0.55 | 0.88 | 0.13 | 0.43 | 0.26 | 0.88 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.99 | -3.70 | -2.11 | -2.03 | -1.66 | -1.77 | -2.64 | -1.67 | -4.52 | -2.60 | -1.23 | -1.76 | -1.65|
| full sent KL (full->waitk) |  |  |  |  | -2.98 | -3.23 | -2.47 | -1.04 | -2.84 | -2.17 | -3.71 | -2.11 | -1.90 | -1.18 | -1.03 | -1.90 | -1.73|
| dec-waitktgt |  |  |  |  | two | plants | so | close | together | : | intention | or | the | to@@ | is@@ | ? | </s>|
| full sent tgt |  |  |  |  | two | plants | so | close | together | : | intention | or | a | to@@ | is@@ | ? | </s>|
| ref | two | sets | of | lights | so | close | to | one | another | : | inten@@ | tional | or | just | a | sil@@ | ly | error | ? | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | diese | frage | hat | gu@@ | ta@@ | chs | bürger@@ | meister | gestern | klar | beantwortet | .|
| waitk tgt |  |  |  |  | this | question | was | raised | yesterday | by | the | may@@ | or | of | gu@@ | t@@ | á@@ | n | . | </s>|
| waitk prob |  |  |  |  | 0.37 | 0.33 | 0.39 | 0.24 | 0.44 | 0.82 | 0.46 | 0.82 | 0.86 | 0.55 | 0.11 | 0.72 | 0.10 | 0.07 | 0.61 | 0.91|
| dec-waitk prob |  |  |  |  | 0.42 | 0.36 | 0.07 | 0.32 | 0.21 | 0.93 | 0.05 | 0.98 | 0.89 | 0.75 | 0.36 | 0.41 | 0.01 | 0.02 | 0.82 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 1 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.52 | -1.76 | -2.36 | -2.27 | -1.73 | -1.23 | -4.54 | -0.81 | -1.45 | -2.09 | -4.49 | -2.98 | -1.21 | -3.14 | -1.91 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.69 | -2.57 | -2.01 | -3.83 | -2.02 | -2.00 | -3.25 | -2.00 | -1.64 | -2.49 | -4.97 | -2.40 | -5.79 | -4.97 | -2.87 | -1.60|
| full sent prob |  |  |  |  | 0.13 | 0.59 | 0.89 | 0.00 | 0.21 | 0.89 | 0.10 | 0.99 | 0.89 | 0.76 | 0.31 | 0.42 | 0.01 | 0.01 | 0.50 | 0.91|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 41 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.30 | -1.87 | -1.14 | -2.55 | -3.31 | -1.58 | -4.10 | -0.80 | -1.49 | -1.93 | -4.71 | -2.90 | -1.28 | -3.07 | -3.01 | -1.63|
| full sent KL (full->waitk) |  |  |  |  | -3.59 | -2.56 | -2.08 | -3.76 | -1.88 | -1.97 | -3.27 | -2.00 | -1.63 | -2.49 | -4.97 | -2.40 | -5.79 | -4.97 | -2.72 | -1.59|
| dec-waitktgt |  |  |  |  | this | issue | has | put | by | by | expert | may@@ | or | of | gu@@ | t@@ | ach@@ | ch@@ | . | </s>|
| full sent tgt |  |  |  |  | yesterday | question | was | clearly | by | by | mr | may@@ | or | of | gu@@ | t@@ | ach@@ | ch@@ | . | </s>|
| ref | yesterday | , | gu@@ | t@@ | ach@@ | t | &apos;s | may@@ | or | gave | a | clear | answer | to | this | question | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | klu@@ | ser@@ | -@@ | amp@@ | el | sichere | sowohl | rad@@ | fahrer | als | auch | bus@@ | fahr@@ | gäste | und | die | berg@@ | le-@@ | bewohner | .|
| waitk tgt |  |  |  |  | k@@ | lu@@ | ser@@ | -@@ | traffic | lights | secure | both | cy@@ | cli@@ | sts | and | bus | passengers | and | mountain | residents | . | </s>|
| waitk prob |  |  |  |  | 0.37 | 0.79 | 0.39 | 0.97 | 0.20 | 0.45 | 0.24 | 0.36 | 0.76 | 0.90 | 0.97 | 0.80 | 0.62 | 0.40 | 0.76 | 0.43 | 0.70 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.28 | 0.44 | 0.15 | 0.90 | 0.55 | 0.73 | 0.22 | 0.67 | 0.79 | 0.95 | 0.95 | 0.76 | 0.87 | 0.62 | 0.52 | 0.19 | 0.61 | 0.88 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.96 | -1.92 | -1.75 | -1.67 | -2.85 | -1.58 | -3.32 | -1.93 | -1.85 | -1.15 | -1.30 | -2.11 | -1.13 | -2.24 | -2.99 | -3.14 | -2.05 | -1.81 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.85 | -1.52 | -2.55 | -1.01 | -4.45 | -3.10 | -3.71 | -3.64 | -1.91 | -1.26 | -1.05 | -1.86 | -2.49 | -3.23 | -1.94 | -2.12 | -1.64 | -1.76 | -1.64|
| full sent prob |  |  |  |  | 0.16 | 0.69 | 0.52 | 0.91 | 0.75 | 0.75 | 0.14 | 0.56 | 0.80 | 0.99 | 0.96 | 0.44 | 0.81 | 0.69 | 0.79 | 0.22 | 0.53 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.87 | -1.72 | -1.77 | -1.64 | -1.79 | -1.64 | -3.24 | -2.19 | -1.86 | -0.84 | -1.15 | -2.29 | -1.26 | -2.09 | -1.92 | -2.69 | -2.18 | -1.70 | -1.55|
| full sent KL (full->waitk) |  |  |  |  | -2.81 | -1.67 | -2.57 | -1.01 | -4.48 | -3.11 | -3.70 | -3.61 | -1.91 | -1.29 | -1.06 | -1.66 | -2.47 | -3.25 | -2.10 | -2.15 | -1.60 | -1.78 | -1.64|
| dec-waitktgt |  |  |  |  | the | lu@@ | ser | -@@ | traffic | lights | secure | both | cy@@ | cli@@ | sts | and | bus | passengers | and | the | residents | . | </s>|
| full sent tgt |  |  |  |  | the | lu@@ | ser@@ | -@@ | traffic | lights | secure | both | cy@@ | cli@@ | sts | and | bus | passengers | and | the | residents | . | </s>|
| ref | the | kl@@ | user | lights | protect | cy@@ | cli@@ | sts | , | as | well | as | those | travelling | by | bus | and | the | residents | of | ber@@ | g@@ | le | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | gestern | offiziell | in | betrieb | genommen@@ | e | anlage | sei | wichtig | für | den | kreuz@@ | ungs@@ | bereich | sul@@ | z@@ | ba@@ | ch@@ | weg | / | kir@@ | ch@@ | straße | .|
| waitk tgt |  |  |  |  | the | agreement | officially | launched | yesterday | is | important | for | the | crossing | area | of | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | / | kir@@ | ch@@ | stra@@ | ß@@ | e | . | </s>|
| waitk prob |  |  |  |  | 0.60 | 0.03 | 0.68 | 0.22 | 0.95 | 0.44 | 0.65 | 0.68 | 0.64 | 0.13 | 0.51 | 0.62 | 0.93 | 0.96 | 0.53 | 0.96 | 0.99 | 0.94 | 0.84 | 0.98 | 0.96 | 0.57 | 0.93 | 0.92 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.04 | 0.00 | 0.69 | 0.38 | 0.90 | 0.43 | 0.72 | 0.43 | 0.47 | 0.19 | 0.20 | 0.02 | 0.84 | 0.85 | 0.63 | 0.92 | 0.94 | 0.98 | 0.01 | 0.98 | 0.96 | 0.53 | 0.97 | 0.94 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 2 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.15 | -1.36 | -2.05 | -3.05 | -1.57 | -3.11 | -2.03 | -3.09 | -2.30 | -3.50 | -4.27 | -1.20 | -1.95 | -2.10 | -2.26 | -1.30 | -1.38 | -0.97 | -1.26 | -0.99 | -1.19 | -2.11 | -1.07 | -1.32 | -1.73 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.05 | -6.24 | -2.10 | -3.87 | -1.19 | -2.22 | -2.36 | -1.79 | -2.52 | -4.04 | -3.17 | -1.77 | -1.22 | -1.07 | -1.67 | -1.08 | -0.91 | -1.34 | -1.21 | -0.98 | -1.11 | -1.61 | -1.43 | -1.42 | -1.67 | -1.63|
| full sent prob |  |  |  |  | 0.51 | 0.00 | 0.00 | 0.19 | 0.89 | 0.29 | 0.66 | 0.77 | 0.83 | 0.03 | 0.58 | 0.38 | 0.90 | 0.91 | 0.86 | 0.96 | 0.97 | 0.97 | 0.86 | 0.99 | 0.95 | 0.55 | 0.95 | 0.94 | 0.89 | 0.92|
| full sent rank |  |  |  |  | 0 | 591 | 25 | 1 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.22 | -3.09 | -3.36 | -2.94 | -1.72 | -2.45 | -2.42 | -1.93 | -1.79 | -4.22 | -2.87 | -2.32 | -1.57 | -1.59 | -1.32 | -1.11 | -1.11 | -1.05 | -1.63 | -0.94 | -1.24 | -1.96 | -1.23 | -1.32 | -1.71 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.28 | -6.24 | -1.72 | -3.86 | -1.19 | -2.29 | -2.32 | -1.98 | -2.70 | -4.00 | -3.33 | -2.02 | -1.27 | -1.12 | -1.76 | -1.12 | -0.93 | -1.33 | -1.80 | -0.99 | -1.10 | -1.62 | -1.42 | -1.42 | -1.67 | -1.63|
| dec-waitktgt |  |  |  |  | officially | official | officially | launched | yesterday | is | important | for | the | cros@@ | area | . | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | . | kir@@ | ch@@ | stra@@ | ß@@ | e | . | </s>|
| full sent tgt |  |  |  |  | the | plant | was | opened | yesterday | was | important | for | the | sul@@ | area | sul@@ | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | / | kir@@ | ch@@ | stra@@ | ß@@ | e | . | </s>|
| ref | the | system | , | which | officially | became | operational | yesterday | , | is | of | importance | to | the | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | / | kir@@ | ch@@ | stras@@ | se | junction | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dies | bestätigt | auch | peter | ar@@ | n@@ | old | vom | land@@ | rat@@ | sam@@ | t | offen@@ | burg | .|
| waitk tgt |  |  |  |  | peter | ar@@ | no@@ | ld | from | the | council | of | the | off@@ | enburg | region | confir@@ | ms | this | . | </s>|
| waitk prob |  |  |  |  | 0.57 | 0.93 | 0.98 | 0.97 | 0.30 | 0.79 | 0.09 | 0.48 | 0.16 | 0.42 | 0.91 | 0.19 | 0.28 | 0.98 | 0.73 | 0.61 | 0.91|
| dec-waitk prob |  |  |  |  | 0.33 | 0.95 | 1.00 | 0.77 | 0.07 | 0.71 | 0.48 | 0.38 | 0.02 | 0.08 | 0.97 | 0.00 | 0.48 | 0.98 | 0.71 | 0.51 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 5 | 3 | 0 | 42 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.11 | -1.26 | -0.86 | -1.86 | -3.39 | -2.31 | -2.87 | -3.34 | -3.98 | -3.84 | -0.98 | -2.31 | -2.73 | -1.02 | -2.04 | -2.40 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.52 | -1.41 | -1.02 | -0.89 | -2.97 | -2.29 | -4.82 | -2.69 | -4.65 | -2.65 | -1.47 | -2.99 | -3.00 | -1.03 | -1.88 | -2.54 | -1.66|
| full sent prob |  |  |  |  | 0.08 | 0.93 | 0.98 | 0.96 | 0.21 | 0.65 | 0.05 | 0.70 | 0.02 | 0.13 | 0.96 | 0.01 | 0.47 | 0.97 | 0.74 | 0.49 | 0.91|
| full sent rank |  |  |  |  | 2 | 0 | 0 | 0 | 1 | 0 | 4 | 0 | 1 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -4.02 | -1.44 | -1.04 | -1.12 | -3.26 | -2.67 | -3.99 | -2.25 | -1.03 | -3.45 | -1.01 | -2.74 | -2.90 | -1.14 | -1.96 | -2.56 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.41 | -1.40 | -1.01 | -1.05 | -3.02 | -2.25 | -4.79 | -2.81 | -4.63 | -2.67 | -1.47 | -2.99 | -2.99 | -1.02 | -1.89 | -2.53 | -1.65|
| dec-waitktgt |  |  |  |  | peter | ar@@ | no@@ | ld | von | the | council | of | state | republic | enburg | confir@@ | confir@@ | ms | this | . | </s>|
| full sent tgt |  |  |  |  | this | ar@@ | no@@ | ld | of | the | land | of | off@@ | off@@ | enburg | confir@@ | confir@@ | ms | this | . | </s>|
| ref | this | was | also | confirmed | by | peter | ar@@ | no@@ | ld | from | the | off@@ | enburg | district | office | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | und | spar@@ | sam | ist | sie | auch | : | die | älteren | lich@@ | tan@@ | lagen | verbrau@@ | chen | etwa | 100 | wa@@ | tt | , | die | neuen | gerade | mal | acht | wa@@ | tt | .|
| waitk tgt |  |  |  |  | and | it | is | also | econom@@ | ical | : | the | older | lighting | systems | use | up | to | 100 | wat@@ | ts | , | the | new | just | eight | wat@@ | ts | . | </s>|
| waitk prob |  |  |  |  | 0.59 | 0.47 | 0.78 | 0.57 | 0.46 | 0.89 | 0.83 | 0.70 | 0.62 | 0.46 | 0.76 | 0.45 | 0.37 | 0.64 | 0.68 | 0.96 | 0.89 | 0.71 | 0.63 | 0.85 | 0.19 | 0.87 | 0.96 | 0.83 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.82 | 0.27 | 0.79 | 0.38 | 0.11 | 0.64 | 0.85 | 0.49 | 0.62 | 0.49 | 0.46 | 0.22 | 0.00 | 0.03 | 0.88 | 0.91 | 0.88 | 0.47 | 0.56 | 0.59 | 0.10 | 0.85 | 0.86 | 0.89 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 11 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.95 | -3.35 | -2.11 | -2.15 | -2.54 | -2.95 | -1.92 | -3.11 | -2.61 | -2.64 | -2.80 | -1.87 | -2.13 | -2.45 | -1.39 | -1.46 | -1.35 | -2.19 | -2.71 | -3.26 | -3.91 | -1.39 | -1.76 | -1.33 | -1.72 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.00 | -3.34 | -2.00 | -2.34 | -2.92 | -1.47 | -1.97 | -2.41 | -2.85 | -2.88 | -1.40 | -2.47 | -2.53 | -2.41 | -2.67 | -1.09 | -1.41 | -2.16 | -2.33 | -1.74 | -3.88 | -1.29 | -0.99 | -1.79 | -1.72 | -1.63|
| full sent prob |  |  |  |  | 0.40 | 0.57 | 0.44 | 0.57 | 0.54 | 0.92 | 0.86 | 0.53 | 0.75 | 0.37 | 0.59 | 0.40 | 0.00 | 0.14 | 0.90 | 0.94 | 0.87 | 0.64 | 0.67 | 0.79 | 0.09 | 0.89 | 0.88 | 0.86 | 0.83 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.68 | -3.02 | -2.56 | -2.51 | -2.88 | -1.40 | -1.82 | -2.64 | -1.98 | -2.79 | -2.71 | -2.48 | -1.78 | -2.37 | -1.25 | -1.22 | -1.33 | -2.35 | -2.33 | -2.22 | -3.09 | -1.19 | -1.61 | -1.30 | -1.93 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.80 | -3.46 | -1.79 | -2.43 | -3.03 | -1.68 | -1.97 | -2.44 | -2.91 | -2.85 | -1.47 | -2.48 | -2.54 | -2.47 | -2.68 | -1.12 | -1.40 | -2.27 | -2.39 | -1.88 | -3.92 | -1.32 | -1.02 | -1.77 | -1.68 | -1.63|
| dec-waitktgt |  |  |  |  | and | it | is | th@@ | th@@ | ical | : | the | older | lighting | systems | con@@ | about | about | 100 | wat@@ | ts | , | the | new | only | eight | wat@@ | ts | . | </s>|
| full sent tgt |  |  |  |  | and | it | is | also | econom@@ | ical | : | the | older | lighting | systems | use | about | about | 100 | wat@@ | ts | , | the | new | one | eight | wat@@ | ts | . | </s>|
| ref | and | they | are | also | ener@@ | g@@ | y-@@ | efficient | : | the | older | light | systems | con@@ | sume | around | 100 | wat@@ | ts | , | with | the | new | ones | consum@@ | ing | just | eight | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ar@@ | n@@ | old | erklärte | die | technik | der | neuen | anlage | : | diese | ist | mit | zwei | ra@@ | dar@@ | sen@@ | sor@@ | en | ausgestattet | .|
| waitk tgt |  |  |  |  | ar@@ | no@@ | ld | explained | the | new | equipment | technology | : | it | is | equipped | with | two | rad@@ | ar | sen@@ | sors | . | </s>|
| waitk prob |  |  |  |  | 0.75 | 0.98 | 0.98 | 0.60 | 0.81 | 0.33 | 0.15 | 0.30 | 0.71 | 0.30 | 0.53 | 0.83 | 0.90 | 0.88 | 0.82 | 0.91 | 0.82 | 0.95 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.90 | 0.99 | 0.94 | 0.88 | 0.76 | 0.02 | 0.07 | 0.27 | 0.87 | 0.10 | 0.52 | 0.54 | 0.89 | 0.93 | 0.85 | 0.88 | 0.86 | 0.95 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 4 | 3 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.41 | -0.90 | -1.30 | -1.16 | -2.16 | -1.82 | -2.94 | -2.78 | -1.68 | -3.38 | -2.77 | -2.90 | -1.76 | -1.27 | -1.76 | -1.55 | -1.57 | -1.20 | -1.73 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.36 | -1.02 | -0.98 | -2.60 | -1.96 | -2.82 | -3.65 | -3.18 | -2.55 | -3.11 | -2.58 | -1.50 | -1.68 | -1.67 | -2.02 | -1.22 | -1.79 | -1.24 | -1.73 | -1.65|
| full sent prob |  |  |  |  | 0.70 | 0.98 | 0.96 | 0.87 | 0.80 | 0.07 | 0.09 | 0.17 | 0.81 | 0.24 | 0.57 | 0.89 | 0.90 | 0.94 | 0.86 | 0.89 | 0.85 | 0.96 | 0.88 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.57 | -0.98 | -1.17 | -1.37 | -2.05 | -2.29 | -3.99 | -3.44 | -1.99 | -2.63 | -2.36 | -1.33 | -1.70 | -1.26 | -1.73 | -1.46 | -1.50 | -1.15 | -1.80 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -2.23 | -1.01 | -0.99 | -2.59 | -1.99 | -2.82 | -3.64 | -3.14 | -2.52 | -3.13 | -2.61 | -1.74 | -1.69 | -1.68 | -2.03 | -1.23 | -1.79 | -1.24 | -1.72 | -1.64|
| dec-waitktgt |  |  |  |  | ar@@ | no@@ | ld | explained | the | technique | plant | technique | : | this | is | equipped | with | two | rad@@ | ar | sen@@ | sors | . | </s>|
| full sent tgt |  |  |  |  | ar@@ | no@@ | ld | explained | the | technique | system | technique | : | this | is | equipped | with | two | rad@@ | ar | sen@@ | sors | . | </s>|
| ref | ar@@ | no@@ | ld | explained | the | technology | used | by | the | new | system | : | it | is | fitted | with | two | rad@@ | ar | sen@@ | sors | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | drückt | der | fuß@@ | gän@@ | ger | den | amp@@ | el@@ | kno@@ | pf | , | te@@ | stet | der | ober@@ | e | ra@@ | dar@@ | sen@@ | sor | die | verkehrs@@ | lage | .|
| waitk tgt |  |  |  |  | if | the | pede@@ | strian | pus@@ | hes | the | traffic | light | button | , | the | upper | rad@@ | ar | sensor | tests | the | traffic | situation | . | </s>|
| waitk prob |  |  |  |  | 0.34 | 0.77 | 0.76 | 0.76 | 0.19 | 0.89 | 0.88 | 0.79 | 0.86 | 0.91 | 0.85 | 0.85 | 0.52 | 0.95 | 0.90 | 0.89 | 0.54 | 0.70 | 0.90 | 0.66 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.00 | 0.36 | 0.54 | 0.77 | 0.15 | 0.85 | 0.74 | 0.27 | 0.83 | 0.84 | 0.80 | 0.80 | 0.56 | 0.96 | 0.80 | 0.99 | 0.33 | 0.59 | 0.87 | 0.75 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 47 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -4.20 | -2.85 | -3.15 | -1.50 | -4.54 | -1.64 | -2.12 | -4.12 | -1.52 | -1.54 | -2.10 | -2.06 | -2.52 | -1.15 | -1.52 | -0.85 | -3.16 | -2.17 | -1.62 | -1.66 | -1.67 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.33 | -1.95 | -1.82 | -2.04 | -4.05 | -1.44 | -1.59 | -1.69 | -1.20 | -1.15 | -1.84 | -1.90 | -2.13 | -1.21 | -1.37 | -1.68 | -2.82 | -1.99 | -1.37 | -2.09 | -1.71 | -1.66|
| full sent prob |  |  |  |  | 0.27 | 0.75 | 0.84 | 0.80 | 0.43 | 0.91 | 0.84 | 0.52 | 0.78 | 0.87 | 0.71 | 0.86 | 0.68 | 0.92 | 0.89 | 0.98 | 0.30 | 0.84 | 0.87 | 0.72 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.49 | -2.09 | -1.75 | -1.84 | -2.68 | -1.34 | -1.93 | -3.11 | -1.81 | -1.43 | -2.26 | -1.87 | -2.09 | -1.35 | -1.52 | -0.88 | -3.38 | -1.76 | -1.58 | -2.15 | -1.68 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -3.42 | -2.20 | -2.01 | -2.05 | -4.10 | -1.48 | -1.67 | -1.86 | -1.17 | -1.17 | -1.78 | -1.95 | -2.16 | -1.18 | -1.44 | -1.68 | -2.80 | -2.13 | -1.37 | -2.07 | -1.71 | -1.66|
| dec-waitktgt |  |  |  |  | pus@@ | the | pede@@ | strian | pus@@ | hes | the | traffic | light | button | , | the | upper | rad@@ | ar | sensor | tests | the | traffic | situation | . | </s>|
| full sent tgt |  |  |  |  | if | the | pede@@ | strian | pus@@ | hes | the | traffic | light | button | , | the | upper | rad@@ | ar | sensor | tests | the | traffic | situation | . | </s>|
| ref | if | the | pede@@ | strian | pres@@ | ses | the | button | at | the | traffic | lights | , | the | top | rad@@ | ar | sensor | checks | the | traffic | status | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ein | weiteres | ra@@ | dar@@ | sen@@ | sor | prüft | , | ob | die | grün@@ | phase | für | den | fuß@@ | gän@@ | ger | beendet | werden | kann | .|
| waitk tgt |  |  |  |  | another | rad@@ | ar | sensor | checks | whether | the | green | phase | for | the | pede@@ | strian | has | been | finished | . | </s>|
| waitk prob |  |  |  |  | 0.42 | 0.29 | 0.93 | 0.76 | 0.49 | 0.42 | 0.78 | 0.27 | 0.80 | 0.51 | 0.76 | 0.83 | 0.81 | 0.31 | 0.45 | 0.29 | 0.88 | 0.91|
| dec-waitk prob |  |  |  |  | 0.57 | 0.95 | 0.94 | 0.98 | 0.39 | 0.47 | 0.58 | 0.42 | 0.84 | 0.21 | 0.83 | 0.46 | 0.81 | 0.11 | 0.62 | 0.03 | 0.88 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 4 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.73 | -0.65 | -1.20 | -0.79 | -3.30 | -2.62 | -2.75 | -4.06 | -1.74 | -2.88 | -1.93 | -3.82 | -1.53 | -4.11 | -2.27 | -2.42 | -1.83 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.18 | -4.47 | -1.27 | -2.52 | -2.76 | -2.63 | -2.17 | -4.44 | -2.09 | -2.49 | -2.39 | -1.55 | -1.93 | -2.88 | -2.55 | -2.54 | -1.78 | -1.63|
| full sent prob |  |  |  |  | 0.39 | 0.93 | 0.90 | 0.96 | 0.43 | 0.49 | 0.73 | 0.05 | 0.73 | 0.59 | 0.82 | 0.80 | 0.81 | 0.00 | 0.57 | 0.04 | 0.87 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 4 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.12 | -0.83 | -1.49 | -0.95 | -3.27 | -2.70 | -2.32 | -4.96 | -2.29 | -2.25 | -1.87 | -2.06 | -1.71 | -0.85 | -2.62 | -2.72 | -1.87 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -3.13 | -4.47 | -1.23 | -2.51 | -2.78 | -2.63 | -2.27 | -4.35 | -2.02 | -2.60 | -2.38 | -1.78 | -1.93 | -2.81 | -2.54 | -2.53 | -1.77 | -1.63|
| dec-waitktgt |  |  |  |  | another | rad@@ | ar | sensor | checks | whether | the | green | phase | is | the | pede@@ | strian | is | been | completed | . | </s>|
| full sent tgt |  |  |  |  | another | rad@@ | ar | sensor | checks | whether | the | pede@@ | phase | for | the | pede@@ | strian | can | been | completed | . | </s>|
| ref | an | additional | rad@@ | ar | sensor | checks | whether | the | green | phase | for | the | pede@@ | strian | can | be | ended | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | natürlich | mü@@ | sse | der | auto@@ | fahrer | hier | als | partner | mit@@ | denken | und | die | fahr@@ | bahn | beobachten | .|
| waitk tgt |  |  |  |  | of | course | , | drivers | must | be | considered | partners | here | and | the | track | monitored | . | </s>|
| waitk prob |  |  |  |  | 0.38 | 0.92 | 0.58 | 0.26 | 0.44 | 0.56 | 0.17 | 0.36 | 0.36 | 0.66 | 0.46 | 0.44 | 0.11 | 0.87 | 0.91|
| dec-waitk prob |  |  |  |  | 0.56 | 0.94 | 0.58 | 0.14 | 0.51 | 0.29 | 0.06 | 0.00 | 0.31 | 0.73 | 0.41 | 0.07 | 0.10 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 11 | 1 | 0 | 0 | 1 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.70 | -1.37 | -2.46 | -3.13 | -2.27 | -3.29 | -3.96 | -2.24 | -2.28 | -1.98 | -3.74 | -4.57 | -3.37 | -1.70 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.32 | -1.53 | -2.39 | -3.02 | -2.63 | -2.85 | -3.67 | -2.25 | -2.29 | -1.94 | -3.66 | -3.08 | -4.24 | -1.84 | -1.65|
| full sent prob |  |  |  |  | 0.37 | 0.93 | 0.49 | 0.23 | 0.42 | 0.12 | 0.04 | 0.03 | 0.22 | 0.78 | 0.00 | 0.14 | 0.03 | 0.88 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 1 | 2 | 3 | 1 | 0 | 14 | 1 | 4 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.39 | -1.45 | -2.69 | -3.20 | -2.53 | -3.60 | -4.09 | -2.81 | -2.20 | -1.93 | -2.66 | -4.15 | -2.65 | -1.72 | -1.54|
| full sent KL (full->waitk) |  |  |  |  | -3.27 | -1.52 | -2.35 | -3.02 | -2.60 | -2.77 | -3.67 | -2.31 | -2.29 | -1.95 | -3.51 | -3.11 | -4.24 | -1.83 | -1.65|
| dec-waitktgt |  |  |  |  | of | course | , | the | must | be | involved | and | and | and | the | road | must | . | </s>|
| full sent tgt |  |  |  |  | of | course | , | the | must | take | involved | as | and | and | observe | road | must | . | </s>|
| ref | of | course | , | drivers | must | also | play | their | part | and | keep | their | eyes | on | the | road | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dabei | scheint | regi@@ | ss@@ | eur | fre@@ | sa@@ | cher | dem | text | wenig | zu | vertrauen | .|
| waitk tgt |  |  |  |  | the | director | seems | to | have | been | rather | slow | to | trust | the | text | . | </s>|
| waitk prob |  |  |  |  | 0.16 | 0.74 | 0.26 | 0.79 | 0.32 | 0.11 | 0.05 | 0.08 | 0.67 | 0.63 | 0.84 | 0.77 | 0.84 | 0.91|
| dec-waitk prob |  |  |  |  | 0.22 | 0.89 | 0.01 | 0.70 | 0.09 | 0.07 | 0.01 | 0.00 | 0.44 | 0.86 | 0.77 | 0.84 | 0.84 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 7 | 0 | 1 | 2 | 16 | 52 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -4.01 | -1.41 | -2.81 | -2.40 | -3.05 | -4.20 | -3.77 | -1.62 | -2.42 | -1.54 | -2.17 | -1.96 | -1.95 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.16 | -2.36 | -3.27 | -2.07 | -3.14 | -5.13 | -5.12 | -4.91 | -2.14 | -2.80 | -1.84 | -2.37 | -1.95 | -1.66|
| full sent prob |  |  |  |  | 0.05 | 0.24 | 0.00 | 0.64 | 0.28 | 0.00 | 0.03 | 0.01 | 0.23 | 0.78 | 0.76 | 0.83 | 0.79 | 0.91|
| full sent rank |  |  |  |  | 2 | 0 | 76 | 0 | 1 | 4 | 5 | 8 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.29 | -4.32 | -2.97 | -2.49 | -2.86 | -0.82 | -3.62 | -2.42 | -2.23 | -1.99 | -2.26 | -1.96 | -2.11 | -1.62|
| full sent KL (full->waitk) |  |  |  |  | -4.17 | -1.97 | -3.28 | -2.04 | -3.13 | -5.12 | -5.12 | -4.90 | -2.05 | -2.77 | -1.83 | -2.37 | -1.92 | -1.65|
| dec-waitktgt |  |  |  |  | the | director | , | to | be | the | little | too | to | trust | the | text | . | </s>|
| full sent tgt |  |  |  |  | director | director | , | to | be | little | very | un@@ | in | trust | the | text | . | </s>|
| ref | however | , | director | fres@@ | ach@@ | er | seems | to | have | little | trust | in | the | text | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | vor | allem | die | schau@@ | spiel@@ | erinnen | kommen | bei | den | mit@@ | unter | etwas | fra@@ | g@@ | würdigen | szen@@ | ischen | um@@ | setzungen | d@@ | ran | .|
| waitk tgt |  |  |  |  | the | ac@@ | t@@ | res@@ | ses | in | particular | are | sometimes | somewhat | question@@ | able | scen@@ | ic | trans@@ | positions | . | </s>|
| waitk prob |  |  |  |  | 0.19 | 0.12 | 0.50 | 0.97 | 0.95 | 0.19 | 0.92 | 0.17 | 0.50 | 0.25 | 0.55 | 0.94 | 0.35 | 0.87 | 0.11 | 0.38 | 0.55 | 0.91|
| dec-waitk prob |  |  |  |  | 0.10 | 0.26 | 0.92 | 0.84 | 0.90 | 0.06 | 0.83 | 0.08 | 0.31 | 0.16 | 0.51 | 0.90 | 0.57 | 0.75 | 0.13 | 0.78 | 0.87 | 0.92|
| dec-waitk rank |  |  |  |  | 3 | 1 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.48 | -2.59 | -0.88 | -1.78 | -1.50 | -2.32 | -2.14 | -2.80 | -3.74 | -3.94 | -2.20 | -1.63 | -2.29 | -2.29 | -4.13 | -1.35 | -1.63 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.58 | -5.42 | -1.71 | -0.95 | -1.19 | -3.77 | -1.36 | -3.97 | -2.89 | -3.69 | -2.22 | -1.29 | -3.29 | -1.26 | -4.97 | -2.50 | -2.69 | -1.66|
| full sent prob |  |  |  |  | 0.16 | 0.17 | 0.87 | 0.94 | 0.98 | 0.14 | 0.73 | 0.20 | 0.06 | 0.19 | 0.56 | 0.91 | 0.45 | 0.89 | 0.12 | 0.63 | 0.87 | 0.91|
| full sent rank |  |  |  |  | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -4.09 | -2.73 | -0.99 | -1.29 | -0.95 | -3.57 | -2.36 | -4.04 | -4.94 | -4.09 | -2.47 | -1.63 | -3.10 | -1.62 | -4.50 | -1.54 | -1.62 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -4.58 | -5.41 | -1.71 | -1.03 | -1.25 | -3.78 | -1.28 | -3.95 | -2.78 | -3.69 | -2.22 | -1.29 | -3.26 | -1.35 | -4.97 | -2.49 | -2.69 | -1.66|
| dec-waitktgt |  |  |  |  | above | actors | t@@ | res@@ | ses | come | particular | sometimes | sometimes | rather | question@@ | able | scen@@ | ic | trans@@ | positions | . | </s>|
| full sent tgt |  |  |  |  | the | actors | t@@ | res@@ | ses | are | particular | are | often | somewhat | question@@ | able | scen@@ | ic | trans@@ | positions | . | </s>|
| ref | in | particular | , | the | ac@@ | t@@ | res@@ | ses | play | a | major | role | in | the | sometimes | rather | du@@ | bi@@ | ous | st@@ | aging | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | werden | hart | ange@@ | fasst | , | mit | dem | kopf | unter | wasser | get@@ | au@@ | cht | , | mit | ihren | ab@@ | end@@ | ro@@ | ben | an | die | wand | ge@@ | ta@@ | ck@@ | ert | .|
| waitk tgt |  |  |  |  | they | are | har@@ | d-@@ | pressed | , | with | their | head | under | water | , | with | their | evening | ra@@ | ys | at | the | wall | , | and | with | their | heads | . | </s>|
| waitk prob |  |  |  |  | 0.68 | 0.77 | 0.39 | 0.59 | 0.23 | 0.51 | 0.43 | 0.42 | 0.65 | 0.20 | 0.79 | 0.79 | 0.80 | 0.89 | 0.70 | 0.40 | 0.75 | 0.40 | 0.68 | 0.81 | 0.37 | 0.54 | 0.16 | 0.63 | 0.04 | 0.07 | 0.91|
| dec-waitk prob |  |  |  |  | 0.26 | 0.57 | 0.05 | 0.21 | 0.03 | 0.30 | 0.74 | 0.49 | 0.46 | 0.01 | 0.88 | 0.44 | 0.59 | 0.82 | 0.66 | 0.00 | 0.32 | 0.17 | 0.56 | 0.83 | 0.00 | 0.01 | 0.00 | 0.42 | 0.01 | 0.07 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 2 | 2 | 5 | 1 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 1 | 0 | 0 | 2 | 1 | 15 | 0 | 7 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.83 | -2.62 | -2.47 | -2.24 | -3.06 | -3.46 | -2.33 | -2.74 | -1.94 | -4.88 | -1.58 | -3.34 | -3.23 | -2.18 | -2.26 | -3.07 | -3.19 | -2.11 | -2.81 | -1.77 | -1.28 | -1.36 | -2.17 | -3.82 | -6.46 | -5.09 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.24 | -1.90 | -3.40 | -2.20 | -2.93 | -2.18 | -3.97 | -2.38 | -1.27 | -3.55 | -1.88 | -1.75 | -1.92 | -1.59 | -2.32 | -2.50 | -1.51 | -2.82 | -2.38 | -1.73 | -2.63 | -2.78 | -4.62 | -2.67 | -5.81 | -4.96 | -1.65|
| full sent prob |  |  |  |  | 0.57 | 0.72 | 0.09 | 0.20 | 0.07 | 0.75 | 0.02 | 0.76 | 0.74 | 0.00 | 0.85 | 0.53 | 0.04 | 0.88 | 0.04 | 0.15 | 0.78 | 0.00 | 0.73 | 0.64 | 0.02 | 0.03 | 0.00 | 0.44 | 0.01 | 0.03 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 1 | 2 | 3 | 0 | 7 | 0 | 0 | 26 | 0 | 0 | 3 | 0 | 3 | 1 | 0 | 172 | 0 | 0 | 4 | 3 | 94 | 0 | 8 | 2 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.06 | -2.37 | -4.20 | -2.50 | -3.28 | -2.04 | -4.64 | -1.73 | -1.32 | -4.15 | -1.75 | -3.20 | -4.92 | -1.71 | -5.14 | -2.55 | -1.66 | -4.63 | -2.25 | -2.43 | -4.08 | -4.98 | -5.09 | -3.40 | -5.66 | -4.82 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -2.41 | -1.99 | -3.37 | -2.21 | -2.93 | -2.35 | -3.71 | -2.44 | -1.37 | -3.56 | -1.86 | -1.81 | -1.55 | -1.64 | -1.95 | -2.55 | -1.79 | -2.74 | -2.46 | -1.61 | -2.60 | -2.79 | -4.64 | -2.68 | -5.81 | -4.96 | -1.65|
| dec-waitktgt |  |  |  |  | they | are | being | sh@@ | touch | with | with | their | head | being | water | , | with | their | evening | ro@@ | ys | . | the | wall | . | </s> | </s> | their | own | . | </s>|
| full sent tgt |  |  |  |  | they | are | se@@ | sh@@ | touch | , | di@@ | their | head | dro@@ | water | , | t@@ | their | after@@ | ro@@ | ys | t@@ | the | wall | . | t@@ | they | their | ch@@ | cut | </s>|
| ref | they | are | man@@ | handled | , | their | heads | held | under | water | , | tack@@ | ed | to | the | wall | by | their | evening | go@@ | wn@@ | s | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | das | normalerweise | eher | lang@@ | wei@@ | lige | gebiet | der | straßen@@ | planung | hat | plötz@@ | lich | eine | intensi@@ | ve | debatte | mit | bun@@ | ten | allian@@ | zen | ent@@ | fa@@ | cht | .|
| waitk tgt |  |  |  |  | the | normally | rather | bor@@ | ing | area | of | road | planning | has | suddenly | caused | an | intense | debate | with | colour@@ | ful | al@@ | li@@ | ances | . | </s>|
| waitk prob |  |  |  |  | 0.27 | 0.22 | 0.35 | 0.68 | 0.97 | 0.67 | 0.87 | 0.82 | 0.67 | 0.49 | 0.85 | 0.07 | 0.64 | 0.47 | 0.94 | 0.77 | 0.35 | 0.95 | 0.89 | 0.97 | 0.96 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.09 | 0.16 | 0.55 | 0.52 | 0.97 | 0.37 | 0.85 | 0.80 | 0.72 | 0.09 | 0.89 | 0.00 | 0.55 | 0.56 | 0.87 | 0.79 | 0.44 | 0.95 | 0.91 | 0.97 | 0.98 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.09 | -2.16 | -1.99 | -1.71 | -1.07 | -3.11 | -1.93 | -1.56 | -2.36 | -1.52 | -1.43 | -2.76 | -1.98 | -1.40 | -1.61 | -2.21 | -2.69 | -1.23 | -1.28 | -1.03 | -0.92 | -1.63 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.82 | -4.33 | -2.71 | -1.71 | -1.07 | -2.09 | -1.79 | -1.31 | -2.64 | -1.91 | -1.78 | -4.47 | -2.12 | -1.73 | -1.24 | -2.05 | -2.58 | -1.22 | -1.65 | -1.06 | -1.17 | -1.64 | -1.66|
| full sent prob |  |  |  |  | 0.49 | 0.20 | 0.59 | 0.44 | 0.97 | 0.55 | 0.87 | 0.72 | 0.74 | 0.49 | 0.79 | 0.01 | 0.56 | 0.63 | 0.92 | 0.70 | 0.37 | 0.95 | 0.95 | 0.98 | 0.98 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.89 | -2.40 | -1.97 | -2.06 | -1.04 | -2.38 | -1.79 | -1.78 | -2.30 | -1.94 | -2.14 | -3.76 | -2.17 | -1.47 | -1.39 | -2.73 | -3.48 | -1.22 | -1.09 | -0.95 | -0.98 | -1.67 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -3.91 | -4.32 | -2.72 | -1.66 | -1.07 | -2.19 | -1.81 | -1.26 | -2.65 | -1.95 | -1.72 | -4.46 | -2.13 | -1.73 | -1.27 | -2.00 | -2.54 | -1.23 | -1.69 | -1.06 | -1.16 | -1.64 | -1.65|
| dec-waitktgt |  |  |  |  | usually | usually | rather | bor@@ | ing | area | of | road | planning | suddenly | suddenly | become | an | intense | debate | with | colour@@ | ful | al@@ | li@@ | ances | . | </s>|
| full sent tgt |  |  |  |  | the | usually | rather | bor@@ | ing | area | of | road | planning | has | suddenly | spar@@ | an | intense | debate | with | colour@@ | ful | al@@ | li@@ | ances | . | </s>|
| ref | the | usually | dul@@ | l | arena | of | highway | planning | has | suddenly | spa@@ | w@@ | ned | intense | debate | and | color@@ | ful | al@@ | li@@ | ances | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | amerikanische | bürger@@ | rechts@@ | vereinigung | ( | ac@@ | l@@ | u | ) | ist | ebenfalls | zu@@ | tief@@ | st | besorgt | und | äuß@@ | ert | eine | reihe | von | datenschutz@@ | bedenken | .|
| waitk tgt |  |  |  |  | the | american | civil | rights | association | ( | ac@@ | l@@ | u | ) | is | also | deeply | concerned | and | expres@@ | ses | a | series | of | data | protection | concerns | . | </s>|
| waitk prob |  |  |  |  | 0.50 | 0.32 | 0.92 | 0.55 | 0.69 | 0.88 | 0.91 | 0.88 | 0.89 | 0.90 | 0.78 | 0.87 | 0.91 | 0.90 | 0.70 | 0.32 | 0.98 | 0.78 | 0.45 | 0.90 | 0.45 | 0.92 | 0.88 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.42 | 0.46 | 0.72 | 0.47 | 0.67 | 0.90 | 0.76 | 0.88 | 0.96 | 0.93 | 0.74 | 0.84 | 0.83 | 0.80 | 0.88 | 0.68 | 0.90 | 0.86 | 0.32 | 0.89 | 0.18 | 0.96 | 0.93 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.18 | -2.81 | -2.02 | -2.63 | -1.85 | -1.55 | -2.60 | -1.77 | -1.13 | -1.47 | -2.30 | -1.92 | -1.33 | -1.54 | -1.64 | -1.49 | -1.44 | -1.70 | -2.45 | -1.80 | -2.34 | -1.10 | -1.24 | -1.66 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.21 | -3.99 | -1.07 | -3.25 | -2.21 | -1.60 | -1.43 | -1.72 | -1.76 | -1.75 | -1.92 | -1.57 | -1.22 | -1.27 | -1.98 | -3.66 | -0.98 | -2.24 | -2.11 | -1.67 | -2.59 | -1.42 | -1.55 | -1.58 | -1.65|
| full sent prob |  |  |  |  | 0.76 | 0.46 | 0.81 | 0.54 | 0.73 | 0.84 | 0.84 | 0.86 | 0.93 | 0.92 | 0.83 | 0.83 | 0.84 | 0.87 | 0.84 | 0.79 | 0.97 | 0.83 | 0.17 | 0.91 | 0.55 | 0.96 | 0.94 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.20 | -3.19 | -1.62 | -2.60 | -1.86 | -1.80 | -2.09 | -1.92 | -1.37 | -1.54 | -1.84 | -1.99 | -1.34 | -1.48 | -1.68 | -1.30 | -1.06 | -1.94 | -1.75 | -1.63 | -2.35 | -1.12 | -1.15 | -1.65 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -3.32 | -3.98 | -1.14 | -3.28 | -2.24 | -1.56 | -1.49 | -1.70 | -1.74 | -1.74 | -1.98 | -1.56 | -1.23 | -1.32 | -1.97 | -3.69 | -1.04 | -2.21 | -2.12 | -1.69 | -2.66 | -1.42 | -1.56 | -1.58 | -1.65|
| dec-waitktgt |  |  |  |  | the | american | civil | rights | association | ( | ac@@ | l@@ | u | ) | is | also | deeply | concerned | and | expres@@ | ses | a | number | of | concerns | protection | concerns | . | </s>|
| full sent tgt |  |  |  |  | the | american | civil | rights | association | ( | ac@@ | l@@ | u | ) | is | also | deeply | concerned | and | expres@@ | ses | a | number | of | data | protection | concerns | . | </s>|
| ref | the | american | civil | liberties | union | is | deeply | concerned | , | too | , | raising | a | variety | of | privacy | issues | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | doch | während | man | sich | im | kongre@@ | ss | nicht | auf | ein | vorgehen | einigen | kann | , | warten | mehrere | bundes@@ | staaten | nicht | länger | .|
| waitk tgt |  |  |  |  | but | , | while | congress | does | not | agree | on | a | course | of | action | , | several | states | no | longer | wait | . | </s>|
| waitk prob |  |  |  |  | 0.52 | 0.50 | 0.78 | 0.57 | 0.24 | 0.89 | 0.85 | 0.72 | 0.31 | 0.15 | 0.90 | 0.95 | 0.91 | 0.74 | 0.83 | 0.49 | 0.94 | 0.79 | 0.84 | 0.91|
| dec-waitk prob |  |  |  |  | 0.46 | 0.01 | 0.77 | 0.18 | 0.11 | 0.87 | 0.00 | 0.52 | 0.11 | 0.81 | 0.88 | 0.97 | 0.59 | 0.75 | 0.89 | 0.29 | 0.95 | 0.59 | 0.90 | 0.93|
| dec-waitk rank |  |  |  |  | 0 | 4 | 0 | 1 | 1 | 0 | 75 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.15 | -1.19 | -1.86 | -2.65 | -3.13 | -1.92 | -4.06 | -2.62 | -3.27 | -1.34 | -1.76 | -1.04 | -3.62 | -1.98 | -1.31 | -2.78 | -1.24 | -3.18 | -1.60 | -1.48|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.94 | -2.45 | -1.69 | -2.45 | -3.27 | -1.72 | -0.99 | -1.90 | -3.32 | -4.27 | -1.63 | -1.21 | -1.38 | -2.04 | -1.71 | -2.21 | -1.36 | -1.75 | -1.92 | -1.66|
| full sent prob |  |  |  |  | 0.64 | 0.57 | 0.81 | 0.40 | 0.01 | 0.90 | 0.88 | 0.58 | 0.13 | 0.59 | 0.88 | 0.98 | 0.90 | 0.80 | 0.85 | 0.17 | 0.95 | 0.70 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.33 | -2.34 | -1.61 | -2.23 | -1.90 | -1.63 | -1.52 | -2.20 | -3.56 | -2.47 | -1.81 | -1.01 | -1.72 | -1.69 | -1.56 | -3.05 | -1.26 | -2.70 | -1.59 | -1.56|
| full sent KL (full->waitk) |  |  |  |  | -3.01 | -2.57 | -1.71 | -2.56 | -3.27 | -1.74 | -1.61 | -1.93 | -3.32 | -4.25 | -1.63 | -1.21 | -1.61 | -2.07 | -1.69 | -2.17 | -1.36 | -1.82 | -1.92 | -1.65|
| dec-waitktgt |  |  |  |  | but | while | while | you | is | not | seek | on | action | course | of | action | , | several | states | no | longer | wait | . | </s>|
| full sent tgt |  |  |  |  | but | , | while | congress | cannot | not | agree | on | what | course | of | action | , | several | states | are | longer | wait | . | </s>|
| ref | and | while | congress | can | &apos;t | agree | on | whether | to | proceed | , | several | states | are | not | waiting | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | tausende | von | auto@@ | fahr@@ | ern | haben | die | fahr@@ | ten@@ | schrei@@ | ber | , | von | denen | einige | mit | g@@ | p@@ | s-@@ | überwachung | ausgestattet | sind | , | bereits | ge@@ | te@@ | stet | .|
| waitk tgt |  |  |  |  | thousands | of | car | drivers | have | been | using | the | tac@@ | ho@@ | graph | , | some | of | which | are | equipped | with | g@@ | ps | surveillance | , | and | have | already | been | tested | . | </s>|
| waitk prob |  |  |  |  | 0.78 | 0.91 | 0.38 | 0.92 | 0.69 | 0.07 | 0.27 | 0.53 | 0.82 | 0.99 | 0.69 | 0.76 | 0.90 | 0.83 | 0.72 | 0.36 | 0.90 | 0.89 | 0.92 | 0.93 | 0.43 | 0.43 | 0.41 | 0.17 | 0.17 | 0.29 | 0.69 | 0.83 | 0.91|
| dec-waitk prob |  |  |  |  | 0.86 | 0.90 | 0.09 | 0.93 | 0.36 | 0.01 | 0.05 | 0.23 | 0.96 | 0.99 | 0.48 | 0.67 | 0.77 | 0.68 | 0.13 | 0.19 | 0.77 | 0.92 | 0.91 | 0.89 | 0.24 | 0.00 | 0.03 | 0.04 | 0.36 | 0.27 | 0.83 | 0.82 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 1 | 0 | 0 | 6 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 4 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.58 | -1.67 | -3.24 | -1.19 | -4.27 | -3.16 | -5.02 | -2.24 | -1.02 | -0.89 | -1.12 | -2.32 | -2.01 | -2.49 | -1.88 | -3.48 | -2.06 | -1.48 | -1.50 | -1.58 | -2.50 | -1.51 | -2.11 | -4.76 | -3.59 | -4.12 | -1.74 | -1.95 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.17 | -1.66 | -2.24 | -1.36 | -2.48 | -5.03 | -4.39 | -1.97 | -1.94 | -0.88 | -1.09 | -2.33 | -1.31 | -1.80 | -1.75 | -2.63 | -1.28 | -1.69 | -1.40 | -1.32 | -2.10 | -2.27 | -2.43 | -3.89 | -4.14 | -3.86 | -2.59 | -2.02 | -1.62|
| full sent prob |  |  |  |  | 0.83 | 0.90 | 0.05 | 0.92 | 0.84 | 0.01 | 0.01 | 0.58 | 0.78 | 0.99 | 0.56 | 0.71 | 0.86 | 0.79 | 0.30 | 0.35 | 0.90 | 0.92 | 0.90 | 0.92 | 0.22 | 0.05 | 0.10 | 0.51 | 0.72 | 0.12 | 0.49 | 0.87 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 2 | 0 | 0 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.70 | -1.67 | -2.77 | -1.30 | -1.80 | -1.73 | -1.63 | -3.10 | -2.12 | -0.93 | -1.09 | -2.41 | -1.57 | -2.01 | -2.70 | -2.56 | -1.39 | -1.52 | -1.54 | -1.35 | -2.45 | -1.76 | -2.54 | -2.65 | -1.97 | -3.38 | -2.13 | -1.76 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -2.15 | -1.66 | -2.24 | -1.36 | -2.74 | -5.06 | -4.38 | -1.97 | -1.82 | -0.88 | -1.12 | -2.36 | -1.37 | -1.87 | -1.85 | -2.69 | -1.38 | -1.68 | -1.40 | -1.35 | -2.11 | -2.27 | -2.46 | -3.95 | -4.18 | -3.83 | -2.41 | -2.06 | -1.61|
| dec-waitktgt |  |  |  |  | thousands | of | drivers | drivers | have | the | tac@@ | tac@@ | tac@@ | ho@@ | graph@@ | , | some | of | them | have | equipped | with | g@@ | ps | monitoring | . | </s> | others | already | been | tested | . | </s>|
| full sent tgt |  |  |  |  | thousands | of | drivers | drivers | have | already | testing | the | tac@@ | ho@@ | graph | , | some | of | them | have | equipped | with | g@@ | ps | monitoring | . | for | have | already | tested | tested | . | </s>|
| ref | thousands | of | mo@@ | tori@@ | sts | have | already | taken | the | black | boxes | , | some | of | which | have | g@@ | ps | monitoring | , | for | a | test | drive | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | art | und | weise | , | wie | wir | diese | steuern | zahlen | , | wird | sich | verändern | .|
| waitk tgt |  |  |  |  | the | way | we | have | managed | to | pay | these | taxes | will | change | . | </s>|
| waitk prob |  |  |  |  | 0.66 | 0.72 | 0.47 | 0.10 | 0.11 | 0.89 | 0.77 | 0.68 | 0.93 | 0.84 | 0.77 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.89 | 0.68 | 0.77 | 0.07 | 0.00 | 0.90 | 0.94 | 0.42 | 0.97 | 0.79 | 0.64 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 2 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.56 | -1.94 | -1.96 | -2.87 | -4.15 | -1.69 | -1.11 | -2.52 | -1.01 | -2.11 | -2.46 | -1.66 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.84 | -2.49 | -1.95 | -3.97 | -4.57 | -1.72 | -2.25 | -1.91 | -1.30 | -1.78 | -1.92 | -1.65 | -1.65|
| full sent prob |  |  |  |  | 0.78 | 0.86 | 0.43 | 0.00 | 0.00 | 0.90 | 0.86 | 0.43 | 0.94 | 0.80 | 0.63 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 20 | 53 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.13 | -1.46 | -2.14 | -0.93 | -2.24 | -1.66 | -1.61 | -2.49 | -1.15 | -1.89 | -2.32 | -1.73 | -1.61|
| full sent KL (full->waitk) |  |  |  |  | -2.78 | -2.59 | -1.92 | -3.95 | -4.58 | -1.73 | -2.20 | -1.91 | -1.29 | -1.79 | -1.91 | -1.64 | -1.65|
| dec-waitktgt |  |  |  |  | the | way | we | do | these | to | pay | these | taxes | will | change | . | </s>|
| full sent tgt |  |  |  |  | the | way | we | pay | paid | to | pay | these | taxes | will | change | . | </s>|
| ref | there | is | going | to | be | a | change | in | how | we | pay | these | taxes | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | doch | in | amerika | wird | nicht | mehr | so | viel | get@@ | an@@ | kt | wie | früher | .|
| waitk tgt |  |  |  |  | but | america | is | not | getting | as | much | fuel | as | it | used | to | . | </s>|
| waitk prob |  |  |  |  | 0.77 | 0.66 | 0.21 | 0.43 | 0.11 | 0.45 | 0.96 | 0.43 | 0.81 | 0.82 | 0.50 | 0.93 | 0.42 | 0.91|
| dec-waitk prob |  |  |  |  | 0.75 | 0.28 | 0.26 | 0.58 | 0.20 | 0.17 | 0.88 | 0.02 | 0.37 | 0.54 | 0.28 | 0.91 | 0.35 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 6 | 0 | 0 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.07 | -2.57 | -2.93 | -2.39 | -3.11 | -2.89 | -1.69 | -3.97 | -4.04 | -1.91 | -2.06 | -1.58 | -1.72 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -1.89 | -2.05 | -2.84 | -2.68 | -4.34 | -2.59 | -1.08 | -1.93 | -1.95 | -1.51 | -2.02 | -1.46 | -2.11 | -1.62|
| full sent prob |  |  |  |  | 0.59 | 0.36 | 0.31 | 0.34 | 0.23 | 0.70 | 0.96 | 0.02 | 0.78 | 0.65 | 0.42 | 0.91 | 0.40 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.71 | -3.09 | -2.77 | -2.59 | -3.52 | -2.20 | -1.12 | -2.91 | -2.41 | -1.98 | -1.96 | -1.58 | -1.85 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -1.79 | -2.09 | -2.83 | -2.65 | -4.32 | -2.73 | -1.14 | -1.99 | -2.22 | -1.58 | -2.06 | -1.46 | -2.11 | -1.61|
| dec-waitktgt |  |  |  |  | but | in | is | not | getting | so | much | tan@@ | as | it | used | to | be | </s>|
| full sent tgt |  |  |  |  | but | america | is | no | getting | as | much | tan@@ | as | it | used | to | be | </s>|
| ref | americans | don | &apos;t | buy | as | much | gas | as | they | used | to | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | politiker | wagen | bei | hohen | sp@@ | rit@@ | preisen | nicht | , | die | steuer | auch | nur | um | einen | c@@ | ent | anzu@@ | heben | .|
| waitk tgt |  |  |  |  | politicians | d@@ | are | not | d@@ | are | to | tax | even | at | a | cr@@ | un@@ | ch | . | </s>|
| waitk prob |  |  |  |  | 0.90 | 0.33 | 0.98 | 0.59 | 0.09 | 0.95 | 0.72 | 0.05 | 0.17 | 0.30 | 0.72 | 0.19 | 0.31 | 0.80 | 0.12 | 0.91|
| dec-waitk prob |  |  |  |  | 0.45 | 0.39 | 0.98 | 0.64 | 0.02 | 0.98 | 0.16 | 0.00 | 0.00 | 0.25 | 0.05 | 0.00 | 0.04 | 0.56 | 0.07 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 99 | 14 | 0 | 1 | 36 | 1 | 0 | 3 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.18 | -3.45 | -0.99 | -2.42 | -4.32 | -0.93 | -1.96 | -4.99 | -2.25 | -3.69 | -1.13 | -1.52 | -5.60 | -3.07 | -3.80 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -1.02 | -3.45 | -1.03 | -1.86 | -4.95 | -1.21 | -2.19 | -4.64 | -4.11 | -3.54 | -1.95 | -4.48 | -3.31 | -1.35 | -3.46 | -1.67|
| full sent prob |  |  |  |  | 0.54 | 0.12 | 0.97 | 0.64 | 0.01 | 0.96 | 0.49 | 0.21 | 0.02 | 0.06 | 0.03 | 0.00 | 0.52 | 0.84 | 0.30 | 0.91|
| full sent rank |  |  |  |  | 0 | 2 | 0 | 0 | 19 | 0 | 0 | 1 | 2 | 2 | 1 | 213 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.69 | -2.72 | -1.06 | -1.71 | -3.94 | -1.12 | -2.66 | -2.78 | -2.08 | -2.62 | -1.25 | -2.19 | -3.05 | -1.38 | -2.76 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -1.07 | -3.38 | -1.02 | -1.84 | -4.95 | -1.19 | -2.39 | -4.65 | -4.12 | -3.51 | -1.94 | -4.48 | -3.44 | -1.53 | -3.48 | -1.66|
| dec-waitktgt |  |  |  |  | politicians | d@@ | are | not | at | are | at | high | at | at | high | high | ent | ch | of | </s>|
| full sent tgt |  |  |  |  | politicians | do | are | not | to | are | to | raise | at | to | high | high | un@@ | ch | . | </s>|
| ref | politicians | are | lo@@ | ath | to | raise | the | tax | even | one | pen@@ | ny | when | gas | prices | are | high | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | „ | das | stellt | die | langfristig | sinn@@ | voll@@ | ste | alternative | dar | \“ | , | sagte | er | .|
| waitk tgt |  |  |  |  | \“ | this | is | the | most | sensible | alternative | in | the | long | term | , | \” | he | said | . | </s>|
| waitk prob |  |  |  |  | 0.48 | 0.54 | 0.22 | 0.82 | 0.50 | 0.28 | 0.32 | 0.73 | 0.91 | 0.81 | 0.59 | 0.84 | 0.87 | 0.94 | 0.84 | 0.92 | 0.91|
| dec-waitk prob |  |  |  |  | 0.64 | 0.44 | 0.13 | 0.68 | 0.23 | 0.44 | 0.25 | 0.73 | 0.91 | 0.87 | 0.46 | 0.76 | 0.89 | 0.91 | 0.80 | 0.92 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.91 | -2.20 | -2.73 | -2.45 | -2.76 | -2.35 | -2.37 | -1.96 | -1.52 | -1.42 | -1.67 | -2.00 | -1.61 | -1.50 | -2.05 | -1.54 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.42 | -2.44 | -3.88 | -1.92 | -2.86 | -2.68 | -2.90 | -2.21 | -1.59 | -1.82 | -1.59 | -1.62 | -1.70 | -1.25 | -1.74 | -1.54 | -1.66|
| full sent prob |  |  |  |  | 0.58 | 0.58 | 0.74 | 0.87 | 0.53 | 0.31 | 0.12 | 0.71 | 0.90 | 0.85 | 0.54 | 0.81 | 0.89 | 0.93 | 0.83 | 0.92 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.25 | -1.90 | -1.83 | -1.83 | -2.21 | -2.81 | -2.66 | -2.07 | -1.65 | -1.55 | -1.76 | -1.78 | -1.62 | -1.34 | -1.85 | -1.54 | -1.61|
| full sent KL (full->waitk) |  |  |  |  | -2.40 | -2.49 | -3.98 | -2.05 | -2.97 | -2.66 | -2.89 | -2.20 | -1.58 | -1.80 | -1.60 | -1.66 | -1.70 | -1.26 | -1.76 | -1.53 | -1.65|
| dec-waitktgt |  |  |  |  | \“ | this | makes | the | best | sensible | option | in | the | long | run | , | \” | he | said | . | </s>|
| full sent tgt |  |  |  |  | \“ | this | is | the | most | sensible | long-term | in | the | long | term | , | \” | he | said | . | </s>|
| ref | &quot; | this | works | out | as | the | most | logical | alternative | over | the | long | term | , | &quot; | he | said | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | büro@@ | kraten | be@@ | zeichnen | es | als | mei@@ | len@@ | basi@@ | erte | benutz@@ | ergeb@@ | ü@@ | hr | .|
| waitk tgt |  |  |  |  | bureaucr@@ | ats | call | it | mil@@ | e-@@ | based | user | charges | . | </s>|
| waitk prob |  |  |  |  | 0.92 | 0.94 | 0.35 | 0.90 | 0.98 | 0.44 | 0.78 | 0.39 | 0.19 | 0.34 | 0.91|
| dec-waitk prob |  |  |  |  | 0.40 | 0.85 | 0.53 | 0.79 | 0.72 | 0.25 | 0.85 | 0.40 | 0.00 | 0.32 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 90 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -4.16 | -1.95 | -2.83 | -1.73 | -2.47 | -3.63 | -1.87 | -3.43 | -5.38 | -2.11 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -0.89 | -1.26 | -3.26 | -1.35 | -0.74 | -2.73 | -2.44 | -3.54 | -4.59 | -2.92 | -1.66|
| full sent prob |  |  |  |  | 0.68 | 0.94 | 0.68 | 0.84 | 0.36 | 0.17 | 0.89 | 0.77 | 0.01 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 8 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.88 | -1.27 | -2.25 | -1.59 | -2.53 | -3.60 | -1.57 | -1.99 | -4.69 | -1.21 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -1.10 | -1.34 | -3.29 | -1.38 | -0.45 | -2.71 | -2.47 | -3.65 | -4.59 | -3.09 | -1.65|
| dec-waitktgt |  |  |  |  | bureaucr@@ | ats | call | it | mil@@ | e@@ | based | user | re@@ | </s> | </s>|
| full sent tgt |  |  |  |  | bureaucr@@ | ats | call | it | mil@@ | e@@ | based | user | charge | . | </s>|
| ref | won@@ | ks | call | it | a | mil@@ | e@@ | ag@@ | e-@@ | based | user | fee | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | us-@@ | sen@@ | at | genehmi@@ | gte | letz@@ | tes | jahr | ein | 90 | millionen | dollar | teu@@ | res | pi@@ | lot@@ | projekt | , | das | 10@@ | .000 | autos | umfasst | hätte | .|
| waitk tgt |  |  |  |  | the | us | sen@@ | ate | approved | a | 90 | million | dollars | expensive | program | last | year | , | which | would | cost | $ | 10@@ | ,000 | cars | . | </s>|
| waitk prob |  |  |  |  | 0.68 | 0.72 | 0.95 | 0.95 | 0.75 | 0.57 | 0.58 | 0.87 | 0.55 | 0.65 | 0.03 | 0.68 | 0.94 | 0.30 | 0.19 | 0.15 | 0.40 | 0.77 | 0.48 | 0.92 | 0.47 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.56 | 0.77 | 0.99 | 0.95 | 0.87 | 0.26 | 0.72 | 0.89 | 0.32 | 0.00 | 0.00 | 0.96 | 0.93 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.02 | 0.94 | 0.00 | 0.55 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1054 | 46 | 0 | 0 | 4 | 10 | 8 | 10 | 4 | 7 | 0 | 19 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.74 | -1.71 | -0.88 | -1.23 | -1.41 | -2.38 | -2.03 | -1.73 | -2.15 | -0.29 | -0.29 | -0.89 | -1.44 | -3.26 | -1.26 | -4.14 | -5.19 | -4.85 | -4.66 | -1.22 | -4.25 | -2.94 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.66 | -2.32 | -1.28 | -1.25 | -2.11 | -2.17 | -2.50 | -1.89 | -2.06 | -2.16 | -5.68 | -2.40 | -1.33 | -2.54 | -3.97 | -4.34 | -3.25 | -1.26 | -1.28 | -1.42 | -3.05 | -1.45 | -1.61|
| full sent prob |  |  |  |  | 0.55 | 0.85 | 0.97 | 0.95 | 0.78 | 0.76 | 0.00 | 0.88 | 0.41 | 0.08 | 0.00 | 0.94 | 0.93 | 0.52 | 0.31 | 0.88 | 0.01 | 0.01 | 0.80 | 0.97 | 0.63 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 1 | 3 | 447 | 0 | 0 | 0 | 0 | 0 | 8 | 6 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.86 | -1.55 | -1.04 | -1.26 | -1.84 | -1.91 | -0.18 | -1.75 | -1.73 | -4.01 | -2.02 | -1.01 | -1.40 | -2.20 | -3.01 | -1.02 | -2.48 | -2.28 | -1.29 | -1.03 | -2.50 | -1.73 | -1.62|
| full sent KL (full->waitk) |  |  |  |  | -2.65 | -2.37 | -1.27 | -1.25 | -2.05 | -2.41 | -2.21 | -1.89 | -2.10 | -2.21 | -5.68 | -2.38 | -1.33 | -2.63 | -4.02 | -4.44 | -3.26 | -1.27 | -1.62 | -1.44 | -3.28 | -1.70 | -1.61|
| dec-waitktgt |  |  |  |  | the | us | sen@@ | ate | approved | one | 90 | million | dollar | last | last | last | year | . | </s> | </s> | be | the | 1 | ,000 | . | . | </s>|
| full sent tgt |  |  |  |  | the | us | sen@@ | ate | approved | a | $ | million | dollar | of | pilot | last | year | , | which | would | have | 10@@ | 10@@ | ,000 | cars | . | </s>|
| ref | the | u.s. | sen@@ | ate | approved | a | $ | 9@@ | 0-@@ | million | pilot | project | last | year | that | would | have | involved | about | 10@@ | ,000 | cars | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | mehrere | bundes@@ | staaten | und | groß@@ | städte | bewegen | sich | nicht@@ | s@@ | de@@ | st@@ | ot@@ | ro@@ | tz | auf | eigene | fau@@ | st | in | diese | richtung | .|
| waitk tgt |  |  |  |  | several | states | and | major | cities | are | nevertheless | moving | in | the | right | direction | at | their | own | pace | . | </s>|
| waitk prob |  |  |  |  | 0.62 | 0.84 | 0.88 | 0.24 | 0.89 | 0.48 | 0.31 | 0.58 | 0.18 | 0.33 | 0.44 | 0.96 | 0.34 | 0.65 | 0.93 | 0.26 | 0.73 | 0.91|
| dec-waitk prob |  |  |  |  | 0.83 | 0.72 | 0.80 | 0.17 | 0.94 | 0.39 | 0.33 | 0.42 | 0.05 | 0.17 | 0.03 | 0.97 | 0.00 | 0.35 | 0.89 | 0.41 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 4 | 0 | 7 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.53 | -1.76 | -2.20 | -2.04 | -1.14 | -2.78 | -2.76 | -3.48 | -3.40 | -4.15 | -3.40 | -1.02 | -1.55 | -3.93 | -1.67 | -2.92 | -1.52 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.79 | -1.69 | -1.76 | -2.78 | -1.41 | -2.51 | -2.17 | -2.96 | -3.76 | -3.17 | -1.63 | -1.07 | -2.50 | -2.58 | -1.32 | -2.88 | -2.10 | -1.63|
| full sent prob |  |  |  |  | 0.18 | 0.84 | 0.87 | 0.21 | 0.88 | 0.38 | 0.66 | 0.67 | 0.68 | 0.02 | 0.10 | 0.92 | 0.04 | 0.76 | 0.91 | 0.60 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -4.12 | -1.63 | -1.90 | -2.32 | -1.52 | -2.22 | -1.45 | -2.01 | -2.04 | -1.46 | -1.78 | -1.46 | -2.27 | -2.27 | -1.55 | -2.45 | -1.46 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.46 | -1.77 | -1.80 | -2.79 | -1.37 | -2.52 | -2.25 | -3.07 | -3.85 | -3.14 | -1.69 | -1.02 | -2.43 | -2.79 | -1.33 | -2.91 | -2.11 | -1.62|
| dec-waitktgt |  |  |  |  | several | states | and | cities | cities | are | nevertheless | moving | . | the | same | direction | . | their | own | pace | . | </s>|
| full sent tgt |  |  |  |  | several | states | and | large | cities | are | nevertheless | moving | in | this | same | direction | . | their | own | pace | . | </s>|
| ref | several | states | and | cities | are | nonetheless | moving | ahead | on | their | own | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | am | enga@@ | gi@@ | er@@ | testen | ist | ore@@ | g@@ | on | , | das | derzeit | 5@@ | .000 | fahrer | für | das | größte | experi@@ | ment | des | landes | an@@ | wir@@ | bt | .|
| waitk tgt |  |  |  |  | the | most | committed | is | o@@ | reg@@ | on | , | which | currently | has | 5@@ | ,000 | ri@@ | ders | for | the | country | \’ | s | largest | experim@@ | ent | . | </s>|
| waitk prob |  |  |  |  | 0.35 | 0.65 | 0.42 | 0.22 | 0.85 | 0.96 | 0.92 | 0.81 | 0.43 | 0.72 | 0.17 | 0.80 | 0.81 | 0.45 | 0.94 | 0.68 | 0.87 | 0.62 | 0.55 | 0.92 | 0.58 | 0.95 | 0.90 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.75 | 0.80 | 0.43 | 0.59 | 0.87 | 0.96 | 0.93 | 0.84 | 0.20 | 0.25 | 0.46 | 0.51 | 0.89 | 0.13 | 0.99 | 0.01 | 0.73 | 0.60 | 0.48 | 0.94 | 0.66 | 0.88 | 0.94 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.08 | -2.02 | -3.25 | -2.86 | -1.59 | -1.12 | -1.41 | -1.86 | -2.59 | -2.27 | -3.17 | -2.70 | -1.30 | -1.24 | -0.88 | -1.21 | -2.64 | -2.12 | -2.22 | -1.38 | -1.90 | -1.80 | -1.20 | -1.66 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.18 | -3.05 | -3.43 | -4.09 | -1.62 | -1.07 | -1.49 | -2.00 | -2.40 | -1.69 | -4.22 | -1.23 | -1.57 | -2.44 | -1.34 | -1.87 | -1.75 | -1.90 | -1.65 | -1.52 | -1.81 | -1.13 | -1.44 | -1.67 | -1.64|
| full sent prob |  |  |  |  | 0.15 | 0.50 | 0.17 | 0.35 | 0.81 | 0.98 | 0.93 | 0.83 | 0.24 | 0.69 | 0.02 | 0.78 | 0.91 | 0.25 | 0.98 | 0.21 | 0.80 | 0.70 | 0.48 | 0.94 | 0.67 | 0.86 | 0.92 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.96 | -3.50 | -4.28 | -3.47 | -1.87 | -0.99 | -1.42 | -1.77 | -2.30 | -1.91 | -3.29 | -1.84 | -1.16 | -2.39 | -0.92 | -3.25 | -2.12 | -1.79 | -1.79 | -1.34 | -1.72 | -1.96 | -1.32 | -1.72 | -1.61|
| full sent KL (full->waitk) |  |  |  |  | -4.01 | -2.89 | -3.34 | -4.05 | -1.58 | -1.09 | -1.49 | -2.00 | -2.44 | -1.93 | -4.16 | -1.40 | -1.58 | -2.43 | -1.34 | -1.99 | -1.80 | -1.95 | -1.67 | -1.52 | -1.82 | -1.11 | -1.43 | -1.66 | -1.64|
| dec-waitktgt |  |  |  |  | the | most | committed | is | o@@ | reg@@ | on | , | the | is | has | 5@@ | ,000 | drivers | ders | . | the | country | \’ | s | largest | experim@@ | ent | . | </s>|
| full sent tgt |  |  |  |  | o@@ | most | committed | is | o@@ | reg@@ | on | , | who | currently | recru@@ | 5@@ | ,000 | drivers | ders | recru@@ | the | country | \’ | s | largest | experim@@ | ent | . | </s>|
| ref | the | most | e@@ | ager | is | o@@ | reg@@ | on | , | which | is | en@@ | li@@ | sting | 5@@ | ,000 | drivers | in | the | country | &apos;s | biggest | experim@@ | ent | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | diese | fahrer | werden | bald | die | mei@@ | len@@ | gebühren | statt | der | miner@@ | al@@ | öl@@ | steuer | an | den | bundes@@ | staat | zahlen | .|
| waitk tgt |  |  |  |  | these | drivers | will | soon | be | able | to | pay | mil@@ | e@@ | age | fees | instead | of | min@@ | eral | oil | taxes | to | the | state | . | </s>|
| waitk prob |  |  |  |  | 0.51 | 0.68 | 0.86 | 0.74 | 0.41 | 0.20 | 0.90 | 0.20 | 0.64 | 0.96 | 0.99 | 0.26 | 0.47 | 0.92 | 0.25 | 0.66 | 0.88 | 0.43 | 0.74 | 0.88 | 0.45 | 0.88 | 0.91|
| dec-waitk prob |  |  |  |  | 0.73 | 0.80 | 0.81 | 0.86 | 0.57 | 0.00 | 0.90 | 0.04 | 0.47 | 0.95 | 0.99 | 0.01 | 0.70 | 0.91 | 0.14 | 0.95 | 0.87 | 0.71 | 0.75 | 0.86 | 0.51 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 64 | 0 | 4 | 0 | 0 | 0 | 5 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.90 | -1.77 | -1.99 | -1.45 | -2.85 | -3.89 | -1.69 | -4.47 | -2.62 | -1.20 | -0.93 | -1.69 | -1.54 | -1.62 | -2.58 | -0.85 | -1.17 | -1.68 | -2.16 | -1.82 | -2.08 | -1.77 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.94 | -2.51 | -1.68 | -2.23 | -3.36 | -4.19 | -1.69 | -3.67 | -1.86 | -1.02 | -0.88 | -3.17 | -2.30 | -1.56 | -2.99 | -3.21 | -1.32 | -1.89 | -2.18 | -1.75 | -2.31 | -1.77 | -1.64|
| full sent prob |  |  |  |  | 0.53 | 0.70 | 0.85 | 0.76 | 0.19 | 0.00 | 0.90 | 0.85 | 0.31 | 0.93 | 0.99 | 0.30 | 0.19 | 0.91 | 0.07 | 0.94 | 0.85 | 0.75 | 0.82 | 0.85 | 0.42 | 0.87 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.93 | -2.61 | -1.79 | -1.96 | -1.65 | -1.05 | -1.68 | -1.31 | -2.33 | -1.29 | -0.94 | -2.80 | -2.13 | -1.65 | -2.95 | -0.90 | -1.22 | -1.60 | -1.91 | -1.89 | -2.22 | -1.84 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -2.86 | -2.45 | -1.71 | -2.17 | -3.28 | -4.22 | -1.69 | -3.79 | -1.82 | -1.01 | -0.88 | -3.27 | -2.20 | -1.56 | -2.97 | -3.21 | -1.30 | -1.89 | -2.23 | -1.74 | -2.30 | -1.76 | -1.64|
| dec-waitktgt |  |  |  |  | these | drivers | will | soon | be | mil@@ | to | earn | mil@@ | e@@ | age | instead | instead | of | petro@@ | eral | oil | taxes | to | the | state | . | </s>|
| full sent tgt |  |  |  |  | these | drivers | will | soon | pay | paying | to | pay | the | e@@ | age | charges | to | of | the | eral | oil | taxes | to | the | state | . | </s>|
| ref | those | drivers | will | soon | pay | the | mil@@ | e@@ | age | fees | instead | of | gas | taxes | to | the | state | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | il@@ | lin@@ | o@@ | is | te@@ | stet | es | in | eingeschrän@@ | k@@ | tem | maße | mit | l@@ | k@@ | ws | .|
| waitk tgt |  |  |  |  | il@@ | lin@@ | o@@ | is | tests | it | in | a | limited | way | with | tr@@ | uc@@ | ks | . | </s>|
| waitk prob |  |  |  |  | 0.83 | 0.97 | 0.96 | 0.94 | 0.32 | 0.63 | 0.55 | 0.52 | 0.72 | 0.63 | 0.69 | 0.74 | 0.94 | 0.96 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.96 | 0.97 | 0.94 | 0.90 | 0.59 | 0.55 | 0.81 | 0.67 | 0.50 | 0.43 | 0.73 | 0.42 | 0.93 | 0.92 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.05 | -1.08 | -1.32 | -1.65 | -2.25 | -2.98 | -1.76 | -2.14 | -1.92 | -3.50 | -2.14 | -2.36 | -1.10 | -1.47 | -1.67 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -1.97 | -1.08 | -1.12 | -1.37 | -3.67 | -2.58 | -2.64 | -3.10 | -2.17 | -2.47 | -2.04 | -1.49 | -1.17 | -1.12 | -1.77 | -1.61|
| full sent prob |  |  |  |  | 0.88 | 0.97 | 0.92 | 0.91 | 0.21 | 0.45 | 0.03 | 0.14 | 0.62 | 0.38 | 0.81 | 0.73 | 0.94 | 0.92 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.54 | -1.14 | -1.50 | -1.59 | -3.55 | -3.24 | -2.84 | -2.14 | -1.68 | -3.72 | -1.72 | -1.71 | -1.10 | -1.44 | -1.75 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -1.92 | -1.07 | -1.10 | -1.37 | -3.59 | -2.53 | -2.33 | -2.91 | -2.24 | -2.45 | -2.08 | -1.66 | -1.18 | -1.13 | -1.77 | -1.60|
| dec-waitktgt |  |  |  |  | il@@ | lin@@ | o@@ | is | tests | it | in | a | limited | way | with | tr@@ | uc@@ | ks | . | </s>|
| full sent tgt |  |  |  |  | il@@ | lin@@ | o@@ | is | tests | it | with | limited | limited | way | with | tr@@ | uc@@ | ks | . | </s>|
| ref | il@@ | lin@@ | o@@ | is | is | trying | it | on | a | limited | basis | with | tr@@ | uc@@ | ks | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | damit | , | so | k@@ | h@@ | an | , | wäre | auch | die | öffentlichkeit | beru@@ | hi@@ | gter | .|
| waitk tgt |  |  |  |  | so | , | kh@@ | an | argu@@ | ed | , | the | public | would | be | more | reas@@ | su@@ | red | . | </s>|
| waitk prob |  |  |  |  | 0.14 | 0.63 | 0.50 | 0.93 | 0.26 | 0.56 | 0.92 | 0.42 | 0.87 | 0.83 | 0.45 | 0.79 | 0.58 | 0.98 | 0.97 | 0.68 | 0.91|
| dec-waitk prob |  |  |  |  | 0.39 | 0.45 | 0.08 | 0.93 | 0.05 | 0.56 | 0.81 | 0.22 | 0.87 | 0.59 | 0.58 | 0.45 | 0.51 | 0.99 | 0.96 | 0.75 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.43 | -3.32 | -4.20 | -1.37 | -2.30 | -2.00 | -2.05 | -3.77 | -1.72 | -2.94 | -2.33 | -3.34 | -2.60 | -0.86 | -1.10 | -2.04 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.37 | -2.84 | -2.46 | -1.45 | -3.11 | -1.60 | -1.42 | -2.86 | -1.72 | -1.58 | -2.75 | -1.70 | -1.92 | -1.03 | -1.03 | -2.09 | -1.63|
| full sent prob |  |  |  |  | 0.07 | 0.65 | 0.48 | 0.92 | 0.26 | 0.56 | 0.92 | 0.47 | 0.84 | 0.64 | 0.54 | 0.45 | 0.49 | 1.00 | 0.96 | 0.70 | 0.92|
| full sent rank |  |  |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.28 | -2.60 | -2.48 | -1.49 | -2.70 | -2.08 | -1.55 | -2.45 | -1.90 | -2.72 | -2.29 | -3.35 | -2.61 | -0.85 | -1.12 | -2.07 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -4.34 | -2.95 | -2.62 | -1.45 | -3.12 | -1.60 | -1.50 | -2.95 | -1.70 | -1.62 | -2.75 | -1.70 | -1.91 | -1.03 | -1.02 | -2.07 | -1.62|
| dec-waitktgt |  |  |  |  | so | , | say | an | says | ed | , | the | public | would | be | more | reas@@ | su@@ | red | . | </s>|
| full sent tgt |  |  |  |  | that | , | kh@@ | an | argu@@ | ed | , | the | public | would | be | more | reas@@ | su@@ | red | . | </s>|
| ref | if | you | can | do | that | , | kh@@ | an | said | , | the | public | gets | more | comfortable | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | jag@@ | d | nach | dieser | technologie | hat | einige | behörden | zu | einem | kleinen | star@@ | tu@@ | p-@@ | unternehmen | namens | tru@@ | e | mi@@ | le@@ | age | in | kali@@ | for@@ | nien | geführt | .|
| waitk tgt |  |  |  |  | the | hun@@ | t | for | this | technology | has | led | some | authorities | to | become | a | small | star@@ | tup | company | called | true | mil@@ | e@@ | age | in | california | . | </s>|
| waitk prob |  |  |  |  | 0.38 | 0.28 | 0.81 | 0.87 | 0.72 | 0.88 | 0.82 | 0.61 | 0.76 | 0.75 | 0.87 | 0.16 | 0.88 | 0.92 | 0.97 | 0.54 | 0.64 | 0.65 | 0.95 | 0.99 | 0.99 | 0.97 | 0.87 | 0.92 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.55 | 0.83 | 0.91 | 0.89 | 0.72 | 0.93 | 0.87 | 0.05 | 0.89 | 0.77 | 0.84 | 0.75 | 0.90 | 0.89 | 0.93 | 0.55 | 0.72 | 0.64 | 0.94 | 0.98 | 0.92 | 0.99 | 0.91 | 0.91 | 0.92 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.16 | -1.28 | -1.34 | -1.70 | -2.25 | -1.30 | -1.66 | -3.71 | -1.29 | -2.21 | -1.94 | -1.46 | -1.61 | -1.53 | -1.24 | -1.66 | -1.82 | -1.88 | -1.25 | -1.03 | -1.40 | -0.91 | -1.59 | -1.55 | -1.55 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.63 | -3.89 | -1.63 | -1.75 | -2.23 | -1.71 | -1.60 | -2.30 | -1.97 | -2.40 | -1.73 | -4.04 | -1.76 | -1.38 | -0.95 | -1.66 | -1.97 | -2.05 | -1.12 | -0.87 | -0.88 | -1.12 | -1.85 | -1.39 | -1.67 | -1.64|
| full sent prob |  |  |  |  | 0.45 | 0.58 | 0.81 | 0.89 | 0.72 | 0.93 | 0.61 | 0.75 | 0.82 | 0.76 | 0.83 | 0.01 | 0.88 | 0.89 | 0.86 | 0.55 | 0.70 | 0.59 | 0.95 | 0.98 | 0.90 | 0.99 | 0.90 | 0.90 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.18 | -2.92 | -1.56 | -1.73 | -2.33 | -1.32 | -1.90 | -1.90 | -1.62 | -2.11 | -1.83 | -2.64 | -1.76 | -1.58 | -1.69 | -1.68 | -1.87 | -2.09 | -1.18 | -1.03 | -1.61 | -0.93 | -1.64 | -1.60 | -1.60 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -3.59 | -3.84 | -1.57 | -1.74 | -2.23 | -1.71 | -1.45 | -2.65 | -1.93 | -2.40 | -1.73 | -3.99 | -1.75 | -1.38 | -0.90 | -1.66 | -1.96 | -2.02 | -1.13 | -0.87 | -0.86 | -1.12 | -1.85 | -1.39 | -1.67 | -1.63|
| dec-waitktgt |  |  |  |  | the | hun@@ | t | for | this | technology | has | turned | some | authorities | to | become | a | small | star@@ | tup | company | called | true | mil@@ | e@@ | age | in | california | . | </s>|
| full sent tgt |  |  |  |  | the | hun@@ | t | for | this | technology | has | led | some | authorities | to | a | a | small | star@@ | tup | company | called | true | mil@@ | e@@ | age | in | california | . | </s>|
| ref | the | hun@@ | t | for | that | technology | has | led | some | state | agencies | to | a | small | california | star@@ | tup | called | true | mil@@ | e@@ | age | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | firma | ist | ursprünglich | nicht | ange@@ | treten | , | um | bundes@@ | staaten | bei | der | besteuerung | von | auto@@ | fahr@@ | ern | zu | helfen | .|
| waitk tgt |  |  |  |  | the | company | was | not | originally | registered | to | help | states | with | the | taxation | of | car | drivers | . | </s>|
| waitk prob |  |  |  |  | 0.55 | 0.82 | 0.32 | 0.53 | 0.49 | 0.07 | 0.71 | 0.19 | 0.64 | 0.23 | 0.30 | 0.70 | 0.89 | 0.46 | 0.95 | 0.45 | 0.91|
| dec-waitk prob |  |  |  |  | 0.80 | 0.81 | 0.23 | 0.59 | 0.73 | 0.01 | 0.76 | 0.00 | 0.71 | 0.11 | 0.11 | 0.44 | 0.90 | 0.27 | 0.66 | 0.69 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 24 | 0 | 221 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.90 | -2.10 | -3.39 | -2.47 | -1.49 | -4.66 | -2.16 | -2.65 | -1.56 | -2.73 | -2.08 | -3.21 | -1.67 | -3.20 | -2.08 | -2.55 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.15 | -1.79 | -3.19 | -2.29 | -2.06 | -4.88 | -2.10 | -3.44 | -2.44 | -3.15 | -2.75 | -1.59 | -1.80 | -1.96 | -0.91 | -2.72 | -1.65|
| full sent prob |  |  |  |  | 0.55 | 0.84 | 0.22 | 0.56 | 0.63 | 0.00 | 0.73 | 0.73 | 0.74 | 0.08 | 0.19 | 0.66 | 0.89 | 0.20 | 0.90 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 41 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.85 | -1.81 | -3.01 | -2.29 | -1.62 | -4.53 | -2.16 | -1.46 | -1.58 | -2.75 | -2.85 | -2.32 | -1.71 | -2.92 | -1.38 | -1.36 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.04 | -1.81 | -3.19 | -2.28 | -2.04 | -4.88 | -2.09 | -3.57 | -2.45 | -3.14 | -2.67 | -1.70 | -1.80 | -1.97 | -1.10 | -2.80 | -1.64|
| dec-waitktgt |  |  |  |  | the | company | was | not | originally | launched | to | state | states | in | taxation | taxation | of | car | drivers | . | </s>|
| full sent tgt |  |  |  |  | the | company | was | not | originally | set | to | help | states | tax | car | taxation | of | drivers | drivers | . | </s>|
| ref | the | firm | was | not | originally | in | the | business | of | helping | states | tax | drivers | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | einigen | dieser | öffentlichen | pi@@ | lot@@ | programme | wurden | große | fehler | gemacht | .|
| waitk tgt |  |  |  |  | some | of | these | public | pilot | programs | have | made | major | mistakes | . | </s>|
| waitk prob |  |  |  |  | 0.39 | 0.86 | 0.76 | 0.92 | 0.91 | 0.28 | 0.41 | 0.74 | 0.32 | 0.79 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.78 | 0.78 | 0.78 | 0.80 | 0.80 | 0.23 | 0.52 | 0.57 | 0.09 | 0.69 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.61 | -2.31 | -1.63 | -2.04 | -2.07 | -2.33 | -2.46 | -2.97 | -2.88 | -2.24 | -1.63 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.90 | -1.83 | -1.83 | -1.38 | -1.38 | -2.98 | -2.71 | -1.96 | -2.36 | -1.72 | -1.59 | -1.65|
| full sent prob |  |  |  |  | 0.54 | 0.88 | 0.69 | 0.84 | 0.88 | 0.01 | 0.60 | 0.58 | 0.11 | 0.68 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.51 | -1.77 | -2.06 | -1.97 | -1.68 | -1.72 | -2.29 | -3.03 | -2.76 | -2.27 | -1.65 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -2.82 | -1.91 | -1.78 | -1.41 | -1.44 | -2.98 | -2.73 | -1.97 | -2.37 | -1.72 | -1.59 | -1.65|
| dec-waitktgt |  |  |  |  | some | of | these | public | pilot | programmes | have | made | big | mistakes | . | </s>|
| full sent tgt |  |  |  |  | some | of | these | public | pilot | programmes | have | made | great | mistakes | . | </s>|
| ref | there | have | been | some | big | mistakes | in | some | of | these | state | pilot | programs | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | es | gibt | wesentlich | billi@@ | gere | und | weniger | in@@ | tru@@ | sive | möglichkeiten | , | dies | umzusetzen | .|
| waitk tgt |  |  |  |  | there | are | much | cheaper | and | less | in@@ | tru@@ | sive | ways | of | doing | this | . | </s>|
| waitk prob |  |  |  |  | 0.74 | 0.73 | 0.48 | 0.89 | 0.73 | 0.84 | 0.98 | 0.92 | 0.97 | 0.91 | 0.51 | 0.53 | 0.42 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.86 | 0.84 | 0.55 | 0.88 | 0.69 | 0.77 | 0.90 | 0.98 | 0.99 | 0.94 | 0.40 | 0.62 | 0.39 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.73 | -1.64 | -2.56 | -1.45 | -1.77 | -2.26 | -1.64 | -0.92 | -0.85 | -1.07 | -2.04 | -2.32 | -2.41 | -1.60 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.43 | -2.01 | -2.77 | -1.34 | -2.25 | -1.83 | -0.93 | -1.44 | -1.02 | -1.26 | -1.93 | -2.56 | -2.54 | -1.69 | -1.64|
| full sent prob |  |  |  |  | 0.86 | 0.87 | 0.44 | 0.86 | 0.73 | 0.79 | 0.82 | 0.95 | 0.97 | 0.92 | 0.56 | 0.32 | 0.47 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.65 | -1.61 | -2.34 | -1.62 | -2.01 | -2.08 | -2.22 | -1.14 | -1.07 | -1.11 | -1.96 | -3.01 | -2.15 | -1.67 | -1.61|
| full sent KL (full->waitk) |  |  |  |  | -2.43 | -2.03 | -2.74 | -1.33 | -2.29 | -1.84 | -0.87 | -1.42 | -1.00 | -1.25 | -1.97 | -2.44 | -2.57 | -1.68 | -1.63|
| dec-waitktgt |  |  |  |  | there | are | much | cheaper | and | less | in@@ | tru@@ | sive | ways | to | doing | this | . | </s>|
| full sent tgt |  |  |  |  | there | are | much | cheaper | and | less | in@@ | tru@@ | sive | ways | of | doing | this | . | </s>|
| ref | there | are | a | lot | less | expensive | and | less | in@@ | tru@@ | sive | ways | to | do | this | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | ore@@ | g@@ | on | experi@@ | men@@ | tieren | die | plan@@ | er | damit | , | auto@@ | fahr@@ | ern | eine | reihe | von | aus@@ | wahl@@ | möglichkeiten | zu | geben | .|
| waitk tgt |  |  |  |  | in | o@@ | reg@@ | on | , | the | plan@@ | ters | experim@@ | ent | with | making | car | drivers | perform | a | series | of | choices | . | </s>|
| waitk prob |  |  |  |  | 0.45 | 0.95 | 0.96 | 0.94 | 0.48 | 0.42 | 0.49 | 0.28 | 0.66 | 0.94 | 0.62 | 0.10 | 0.33 | 0.97 | 0.08 | 0.84 | 0.26 | 0.91 | 0.52 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.30 | 0.83 | 0.93 | 0.93 | 0.53 | 0.53 | 0.24 | 0.09 | 0.71 | 0.83 | 0.85 | 0.02 | 0.03 | 0.81 | 0.01 | 0.81 | 0.22 | 0.90 | 0.47 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 7 | 4 | 0 | 14 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.65 | -1.68 | -1.34 | -1.43 | -2.67 | -2.33 | -1.83 | -4.92 | -2.01 | -1.85 | -1.63 | -2.81 | -2.36 | -1.50 | -5.01 | -2.19 | -2.45 | -1.71 | -2.95 | -1.66 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.44 | -1.02 | -1.07 | -1.35 | -2.30 | -2.84 | -2.37 | -3.88 | -2.25 | -1.07 | -2.74 | -4.44 | -2.63 | -0.90 | -4.89 | -1.95 | -2.42 | -1.59 | -2.50 | -1.70 | -1.65|
| full sent prob |  |  |  |  | 0.77 | 0.86 | 0.95 | 0.93 | 0.65 | 0.49 | 0.07 | 0.21 | 0.41 | 0.95 | 0.79 | 0.01 | 0.15 | 0.90 | 0.00 | 0.78 | 0.14 | 0.90 | 0.47 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 6 | 1 | 0 | 77 | 0 | 3 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.04 | -1.55 | -1.17 | -1.41 | -2.01 | -2.47 | -1.82 | -3.98 | -2.39 | -1.15 | -1.72 | -2.54 | -3.05 | -1.38 | -4.55 | -2.34 | -2.62 | -1.69 | -2.82 | -1.74 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.59 | -1.04 | -1.09 | -1.35 | -2.36 | -2.82 | -2.33 | -3.91 | -2.12 | -1.17 | -2.72 | -4.47 | -2.68 | -0.97 | -4.89 | -1.93 | -2.41 | -1.59 | -2.50 | -1.69 | -1.65|
| dec-waitktgt |  |  |  |  | o@@ | o@@ | reg@@ | on | , | the | pl@@ | ner | experim@@ | ent | with | driving | a | drivers | a | a | range | of | choices | . | </s>|
| full sent tgt |  |  |  |  | in | o@@ | reg@@ | on | , | the | pl@@ | ner | experim@@ | ent | with | giving | drivers | drivers | choose | a | range | of | choices | . | </s>|
| ref | in | o@@ | reg@@ | on | , | pl@@ | ann@@ | ers | are | experim@@ | enting | with | giving | drivers | different | choices | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | können | sich | für | ein | gerät | mit | oder | ohne | g@@ | ps | entscheiden | .|
| waitk tgt |  |  |  |  | you | can | register | for | a | device | with | or | without | g@@ | ps | . | </s>|
| waitk prob |  |  |  |  | 0.58 | 0.77 | 0.35 | 0.65 | 0.56 | 0.49 | 0.72 | 0.88 | 0.92 | 0.54 | 0.95 | 0.88 | 0.91|
| dec-waitk prob |  |  |  |  | 0.85 | 0.86 | 0.01 | 0.68 | 0.78 | 0.81 | 0.76 | 0.76 | 0.90 | 0.86 | 0.94 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.47 | -1.69 | -3.87 | -2.40 | -2.00 | -1.36 | -2.09 | -2.01 | -1.60 | -1.29 | -1.28 | -1.75 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.23 | -1.86 | -2.56 | -2.46 | -2.70 | -3.54 | -2.45 | -1.66 | -1.51 | -2.07 | -1.28 | -1.84 | -1.59|
| full sent prob |  |  |  |  | 0.71 | 0.81 | 0.00 | 0.33 | 0.68 | 0.58 | 0.76 | 0.77 | 0.90 | 0.78 | 0.94 | 0.89 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 69 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.48 | -1.81 | -1.77 | -3.28 | -2.44 | -2.00 | -2.07 | -2.29 | -1.64 | -1.53 | -1.30 | -1.75 | -1.56|
| full sent KL (full->waitk) |  |  |  |  | -3.16 | -1.83 | -2.62 | -2.28 | -2.65 | -3.46 | -2.45 | -1.67 | -1.51 | -2.05 | -1.28 | -1.84 | -1.59|
| dec-waitktgt |  |  |  |  | you | can | choose | for | a | device | with | or | without | g@@ | ps | . | </s>|
| full sent tgt |  |  |  |  | you | can | choose | for | a | device | with | or | without | g@@ | ps | . | </s>|
| ref | they | can | choose | a | device | with | or | without | g@@ | ps | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | wenn | wir | das | tun | , | machen | sich | hunder@@ | te | millionen | von | auto@@ | fahr@@ | ern | sorgen | über | ihre | privat@@ | sphäre | und | zahlreiche | andere | dinge | .|
| waitk tgt |  |  |  |  | if | we | do | that | , | hundreds | of | millions | of | drivers | are | wor@@ | ried | about | their | privacy | and | many | other | things | . | </s>|
| waitk prob |  |  |  |  | 0.70 | 0.86 | 0.87 | 0.44 | 0.85 | 0.80 | 0.90 | 0.91 | 0.90 | 0.37 | 0.46 | 0.57 | 0.97 | 0.76 | 0.85 | 0.86 | 0.82 | 0.44 | 0.80 | 0.80 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.82 | 0.88 | 0.83 | 0.38 | 0.80 | 0.76 | 0.90 | 0.95 | 0.82 | 0.31 | 0.24 | 0.68 | 0.95 | 0.73 | 0.82 | 0.96 | 0.76 | 0.54 | 0.58 | 0.69 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.79 | -1.70 | -1.95 | -2.30 | -1.97 | -1.68 | -1.70 | -1.16 | -2.04 | -3.38 | -2.25 | -1.55 | -1.23 | -2.32 | -1.89 | -1.00 | -2.09 | -2.53 | -2.59 | -2.28 | -1.69 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.43 | -1.74 | -1.56 | -2.28 | -1.75 | -1.77 | -1.72 | -1.44 | -1.58 | -2.13 | -2.52 | -1.77 | -1.06 | -1.96 | -1.57 | -1.85 | -1.75 | -3.00 | -1.78 | -1.78 | -1.71 | -1.65|
| full sent prob |  |  |  |  | 0.67 | 0.90 | 0.87 | 0.32 | 0.86 | 0.70 | 0.89 | 0.91 | 0.90 | 0.39 | 0.41 | 0.37 | 0.94 | 0.86 | 0.84 | 0.94 | 0.87 | 0.40 | 0.75 | 0.56 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.39 | -1.63 | -1.67 | -2.45 | -1.81 | -2.09 | -1.71 | -1.42 | -1.71 | -3.04 | -2.48 | -1.79 | -1.35 | -1.65 | -1.70 | -1.12 | -1.74 | -2.87 | -2.19 | -2.50 | -1.66 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -2.35 | -1.75 | -1.59 | -2.27 | -1.79 | -1.73 | -1.72 | -1.41 | -1.64 | -2.16 | -2.53 | -1.69 | -1.05 | -2.04 | -1.59 | -1.83 | -1.81 | -2.96 | -1.89 | -1.71 | -1.72 | -1.64|
| dec-waitktgt |  |  |  |  | if | we | do | that | , | hundreds | of | millions | of | drivers | will | wor@@ | ried | about | their | privacy | and | many | other | things | . | </s>|
| full sent tgt |  |  |  |  | if | we | do | that | , | hundreds | of | millions | of | drivers | are | concerned | ried | about | their | privacy | and | many | other | things | . | </s>|
| ref | if | we | do | this | , | hundreds | of | millions | of | drivers | will | be | concerned | about | their | privacy | and | a | host | of | other | things | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | köni@@ | gs@@ | feld | : | kleine | mann@@ | schaft | schlägt | sich | wa@@ | cker|
| waitk tgt |  |  |  |  | kö@@ | ni@@ | gs@@ | fel@@ | d | : | small | team | be@@ | ats | w@@ | ack@@ | er | </s>|
| waitk prob |  |  |  |  | 0.39 | 0.98 | 0.72 | 0.90 | 0.84 | 0.80 | 0.32 | 0.69 | 0.21 | 0.96 | 0.96 | 0.96 | 0.91 | 0.68|
| dec-waitk prob |  |  |  |  | 0.02 | 0.91 | 0.42 | 0.98 | 0.91 | 0.87 | 0.68 | 0.75 | 0.66 | 0.89 | 0.96 | 0.98 | 0.96 | 0.02|
| dec-waitk rank |  |  |  |  | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.66 | -1.46 | -1.85 | -0.96 | -1.48 | -1.67 | -2.12 | -2.02 | -1.92 | -1.36 | -1.13 | -0.98 | -1.15 | -2.92|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.68 | -0.99 | -1.07 | -1.64 | -2.01 | -2.11 | -3.69 | -2.49 | -4.03 | -0.99 | -1.10 | -1.17 | -1.53 | -2.48|
| full sent prob |  |  |  |  | 0.01 | 0.70 | 0.35 | 0.98 | 0.92 | 0.85 | 0.66 | 0.77 | 0.55 | 0.86 | 0.96 | 0.98 | 0.96 | 0.01|
| full sent rank |  |  |  |  | 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5|
| full sent KL (waitk->full) |  |  |  |  | -3.27 | -2.57 | -2.08 | -0.93 | -1.45 | -1.76 | -2.30 | -1.96 | -2.37 | -1.45 | -1.14 | -1.00 | -1.16 | -2.92|
| full sent KL (full->waitk) |  |  |  |  | -3.68 | -0.81 | -1.03 | -1.65 | -2.02 | -2.10 | -3.68 | -2.50 | -4.02 | -0.97 | -1.10 | -1.17 | -1.53 | -2.48|
| dec-waitktgt |  |  |  |  | king | ni@@ | gs@@ | fel@@ | d | : | small | team | be@@ | ats | w@@ | ack@@ | er | .|
| full sent tgt |  |  |  |  | king | ni@@ | g@@ | fel@@ | d | : | small | team | be@@ | ats | w@@ | ack@@ | er | .|
| ref | kö@@ | ni@@ | gs@@ | fel@@ | d | : | small | team | gives | a | spi@@ | ri@@ | ted | performance | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | freiwilli@@ | ge | feuer@@ | w@@ | ehr | be@@ | wä@@ | lti@@ | gte | ihre | her@@ | b@@ | st@@ | haupt@@ | pro@@ | be | trotz | personal@@ | mangel@@ | s | mit | bra@@ | vo@@ | ur | .|
| waitk tgt |  |  |  |  | the | voluntary | fire | bri@@ | g@@ | ade | managed | its | autumn | di@@ | ap@@ | hr@@ | ag@@ | m | despite | lack | of | personnel | with | bra@@ | v@@ | our | . | </s>|
| waitk prob |  |  |  |  | 0.44 | 0.42 | 0.70 | 0.56 | 1.00 | 0.94 | 0.08 | 0.54 | 0.82 | 0.15 | 0.26 | 0.84 | 0.98 | 0.89 | 0.66 | 0.17 | 0.91 | 0.65 | 0.45 | 0.33 | 0.80 | 0.54 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.35 | 0.82 | 0.76 | 0.95 | 0.92 | 0.97 | 0.00 | 0.08 | 0.40 | 0.00 | 0.00 | 0.72 | 0.78 | 0.95 | 0.00 | 0.05 | 0.90 | 0.30 | 0.00 | 0.35 | 0.91 | 0.88 | 0.89 | 0.93|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 9 | 3 | 0 | 121 | 46 | 0 | 0 | 0 | 14 | 6 | 0 | 1 | 13 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.02 | -1.56 | -1.21 | -0.77 | -1.44 | -0.90 | -1.58 | -4.22 | -3.96 | -1.37 | -3.77 | -2.29 | -1.79 | -0.96 | -1.20 | -3.47 | -1.68 | -2.25 | -1.55 | -4.44 | -1.20 | -1.20 | -1.80 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.26 | -4.34 | -1.63 | -2.10 | -0.80 | -1.08 | -4.86 | -2.09 | -1.63 | -4.39 | -3.61 | -1.33 | -0.82 | -1.14 | -1.78 | -3.34 | -1.57 | -1.76 | -2.99 | -3.73 | -1.98 | -3.18 | -1.69 | -1.64|
| full sent prob |  |  |  |  | 0.61 | 0.18 | 0.90 | 0.65 | 0.99 | 0.98 | 0.10 | 0.62 | 0.30 | 0.00 | 0.02 | 0.85 | 0.96 | 0.94 | 0.30 | 0.11 | 0.91 | 0.32 | 0.51 | 0.00 | 0.87 | 0.91 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1692 | 7 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 10 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.94 | -4.86 | -1.02 | -1.77 | -0.93 | -0.87 | -4.82 | -2.14 | -3.02 | -2.26 | -2.30 | -1.42 | -1.06 | -1.02 | -3.61 | -3.12 | -1.61 | -1.87 | -2.13 | -1.00 | -1.43 | -1.05 | -1.63 | -1.56|
| full sent KL (full->waitk) |  |  |  |  | -3.29 | -4.12 | -1.69 | -1.99 | -0.86 | -1.09 | -4.87 | -2.31 | -1.57 | -4.39 | -3.61 | -1.42 | -0.95 | -1.13 | -1.96 | -3.36 | -1.58 | -1.78 | -3.15 | -3.73 | -1.95 | -3.19 | -1.70 | -1.64|
| dec-waitktgt |  |  |  |  | voluntary | voluntary | fire | bri@@ | g@@ | ade | </s> | </s> | autumn | </s> | re | hr@@ | ag@@ | m | </s> | a | of | staff | . | bra@@ | v@@ | our | . | </s>|
| full sent tgt |  |  |  |  | the | volunte@@ | fire | bri@@ | g@@ | ade | managed | its | main | main | ary | hr@@ | ag@@ | m | despite | a | of | staff | with | flying | v@@ | our | . | </s>|
| ref | the | voluntary | fire | service | bra@@ | vely | came | through | the | main | autumn | test | run | in | spite | of | a | lack | of | personnel | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | durch | den | ent@@ | stehenden | bran@@ | d | und | die | rau@@ | ch@@ | entwicklung | wurden | zwei | menschen | verletzt | , | einer | davon | konnte | aber | noch | einen | not@@ | ruf | ab@@ | senden | .|
| waitk tgt |  |  |  |  | the | fire | and | the | smo@@ | ke | development | have | led | to | two | in@@ | jur@@ | ies | , | one | of | which | could | have | an | emergency | call | . | </s>|
| waitk prob |  |  |  |  | 0.34 | 0.28 | 0.70 | 0.53 | 0.26 | 0.67 | 0.29 | 0.29 | 0.09 | 0.67 | 0.30 | 0.48 | 0.83 | 0.92 | 0.60 | 0.41 | 0.69 | 0.61 | 0.40 | 0.18 | 0.25 | 0.94 | 0.81 | 0.86 | 0.91|
| dec-waitk prob |  |  |  |  | 0.24 | 0.36 | 0.51 | 0.74 | 0.04 | 0.90 | 0.02 | 0.07 | 0.03 | 0.75 | 0.38 | 0.52 | 0.74 | 0.96 | 0.28 | 0.58 | 0.70 | 0.47 | 0.28 | 0.05 | 0.22 | 0.96 | 0.81 | 0.88 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 2 | 0 | 9 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.36 | -3.28 | -3.20 | -2.40 | -3.80 | -1.11 | -4.44 | -3.31 | -3.67 | -2.12 | -3.17 | -2.99 | -1.47 | -1.03 | -2.12 | -2.51 | -2.61 | -1.71 | -3.03 | -2.52 | -3.31 | -1.12 | -1.45 | -1.75 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.84 | -4.54 | -2.46 | -3.90 | -4.11 | -1.56 | -4.58 | -3.86 | -4.23 | -2.03 | -3.19 | -2.81 | -1.11 | -1.41 | -2.34 | -2.52 | -2.57 | -2.06 | -2.83 | -3.69 | -3.96 | -1.27 | -1.73 | -1.85 | -1.64|
| full sent prob |  |  |  |  | 0.24 | 0.51 | 0.57 | 0.40 | 0.44 | 0.94 | 0.08 | 0.08 | 0.01 | 0.89 | 0.35 | 0.74 | 0.54 | 0.88 | 0.66 | 0.63 | 0.72 | 0.55 | 0.17 | 0.02 | 0.17 | 0.96 | 0.89 | 0.76 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.79 | -3.11 | -2.99 | -2.51 | -3.31 | -0.85 | -4.81 | -3.18 | -3.32 | -1.55 | -3.15 | -1.98 | -1.48 | -1.46 | -2.25 | -2.32 | -2.57 | -1.96 | -3.03 | -2.72 | -3.55 | -1.12 | -1.31 | -2.43 | -1.62|
| full sent KL (full->waitk) |  |  |  |  | -3.84 | -4.57 | -2.49 | -3.75 | -4.17 | -1.59 | -4.59 | -3.88 | -4.22 | -2.10 | -3.18 | -2.89 | -0.98 | -1.35 | -2.53 | -2.53 | -2.58 | -2.07 | -2.82 | -3.65 | -3.94 | -1.28 | -1.78 | -1.76 | -1.64|
| dec-waitktgt |  |  |  |  | the | fire | and | the | r@@ | ke | that | that | caused | to | two | in@@ | jur@@ | ies | . | one | of | which | could | still | an | emergency | call | . | </s>|
| full sent tgt |  |  |  |  | the | fire | and | the | smo@@ | ke | that | caused | caused | to | two | in@@ | jur@@ | ies | , | one | of | which | was | send | sent | emergency | call | . | </s>|
| ref | two | people | were | in@@ | ju@@ | red | by | the | resulting | fire | and | the | spread | of | smo@@ | ke | , | however | , | one | was | able | to | make | an | emergency | call | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | nach | kurzer | zeit | ge@@ | lang | es | , | die | erste | person | zu | finden | und | ins | freie | zu | ge@@ | leiten | .|
| waitk tgt |  |  |  |  | after | a | short | time | , | the | first | person | was | found | and | moved | to | the | out@@ | doors | . | </s>|
| waitk prob |  |  |  |  | 0.24 | 0.77 | 0.85 | 0.43 | 0.35 | 0.50 | 0.72 | 0.87 | 0.37 | 0.67 | 0.80 | 0.20 | 0.26 | 0.68 | 0.49 | 0.72 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.87 | 0.53 | 0.92 | 0.28 | 0.39 | 0.02 | 0.83 | 0.92 | 0.21 | 0.16 | 0.20 | 0.00 | 0.32 | 0.73 | 0.04 | 0.62 | 0.89 | 0.93|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 4 | 0 | 0 | 1 | 1 | 1 | 164 | 1 | 0 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.09 | -2.68 | -1.22 | -2.27 | -2.38 | -3.15 | -1.88 | -1.25 | -3.38 | -3.64 | -3.40 | -4.62 | -2.36 | -2.32 | -1.61 | -2.53 | -1.76 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.16 | -2.00 | -1.67 | -2.48 | -2.73 | -2.83 | -2.90 | -1.83 | -2.82 | -2.45 | -1.61 | -4.07 | -3.25 | -2.36 | -2.42 | -2.04 | -1.72 | -1.65|
| full sent prob |  |  |  |  | 0.33 | 0.72 | 0.86 | 0.43 | 0.42 | 0.23 | 0.73 | 0.85 | 0.38 | 0.47 | 0.74 | 0.01 | 0.27 | 0.71 | 0.05 | 0.69 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 20 | 1 | 0 | 2 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.65 | -2.49 | -1.50 | -2.61 | -2.69 | -2.88 | -2.69 | -1.76 | -3.07 | -2.79 | -2.00 | -4.10 | -2.07 | -2.31 | -1.60 | -2.37 | -1.76 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -4.06 | -2.12 | -1.63 | -2.49 | -2.73 | -2.91 | -2.84 | -1.78 | -2.88 | -2.62 | -1.97 | -4.07 | -3.25 | -2.34 | -2.41 | -2.07 | -1.71 | -1.64|
| dec-waitktgt |  |  |  |  | after | a | short | period | , | it | first | person | succeeded | able | . | succeeded | into | the | open | doors | . | </s>|
| full sent tgt |  |  |  |  | after | a | short | time | , | it | first | person | was | found | and | led | into | the | open | doors | . | </s>|
| ref | after | a | short | time | they | managed | to | find | the | first | person | and | direct | them | out | of | the | building | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dies | war | nicht | so | einfach | , | da | auch | eine | enge | tre@@ | ppe | zu | überwinden | war | .|
| waitk tgt |  |  |  |  | this | was | not | so | easy | , | as | a | narrow | sta@@ | ir@@ | case | had | to | be | overcome | . | </s>|
| waitk prob |  |  |  |  | 0.42 | 0.67 | 0.86 | 0.42 | 0.75 | 0.61 | 0.35 | 0.21 | 0.38 | 0.93 | 0.86 | 0.70 | 0.34 | 0.89 | 0.92 | 0.72 | 0.79 | 0.91|
| dec-waitk prob |  |  |  |  | 0.18 | 0.72 | 0.89 | 0.60 | 0.76 | 0.55 | 0.40 | 0.13 | 0.32 | 0.96 | 0.51 | 0.83 | 0.16 | 0.78 | 0.93 | 0.56 | 0.79 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.40 | -2.27 | -1.66 | -2.32 | -1.46 | -2.69 | -2.55 | -3.46 | -3.98 | -1.04 | -2.08 | -1.23 | -2.31 | -2.09 | -1.39 | -3.26 | -1.95 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.58 | -2.25 | -1.87 | -2.88 | -1.69 | -2.19 | -2.28 | -3.60 | -3.38 | -1.40 | -1.17 | -1.21 | -2.65 | -1.61 | -1.49 | -2.13 | -1.93 | -1.65|
| full sent prob |  |  |  |  | 0.28 | 0.69 | 0.82 | 0.62 | 0.79 | 0.39 | 0.42 | 0.29 | 0.42 | 0.97 | 0.89 | 0.84 | 0.19 | 0.78 | 0.94 | 0.46 | 0.70 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.43 | -2.33 | -2.03 | -2.22 | -1.53 | -2.50 | -2.59 | -2.90 | -3.43 | -1.03 | -1.21 | -1.19 | -2.24 | -2.09 | -1.35 | -3.69 | -2.09 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -2.57 | -2.23 | -1.82 | -2.89 | -1.70 | -2.13 | -2.28 | -3.62 | -3.41 | -1.40 | -1.43 | -1.21 | -2.65 | -1.61 | -1.49 | -2.08 | -1.88 | -1.64|
| dec-waitktgt |  |  |  |  | it | was | not | so | easy | , | as | it | narrow | sta@@ | ir@@ | case | could | to | be | overcome | . | </s>|
| full sent tgt |  |  |  |  | this | was | not | so | easy | , | as | a | narrow | sta@@ | ir@@ | case | could | to | be | overcome | . | </s>|
| ref | this | was | not | so | simple | as | they | also | had | to | negotiate | a | narrow | sta@@ | ir@@ | well | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | das | gebäude | , | eine | werk@@ | statt | mit | integri@@ | erter | st@@ | all@@ | ung | für | zwei | pfer@@ | de | , | war | nicht | einfach | zu | sichern | .|
| waitk tgt |  |  |  |  | the | building | , | a | workshop | with | integrated | st@@ | all@@ | ing | for | two | horses | , | was | not | easy | to | secure | . | </s>|
| waitk prob |  |  |  |  | 0.59 | 0.67 | 0.69 | 0.66 | 0.73 | 0.81 | 0.70 | 0.39 | 0.64 | 0.23 | 0.86 | 0.87 | 0.97 | 0.88 | 0.81 | 0.88 | 0.87 | 0.89 | 0.74 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.66 | 0.88 | 0.49 | 0.51 | 0.64 | 0.80 | 0.43 | 0.01 | 0.10 | 0.03 | 0.37 | 0.91 | 0.90 | 0.41 | 0.76 | 0.89 | 0.27 | 0.85 | 0.47 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.11 | -1.46 | -3.06 | -2.90 | -2.05 | -2.00 | -2.53 | -2.86 | -3.21 | -5.27 | -2.70 | -1.48 | -1.53 | -3.16 | -2.33 | -1.73 | -3.22 | -2.03 | -3.42 | -1.71 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.05 | -2.89 | -2.15 | -2.28 | -2.04 | -2.06 | -1.86 | -3.58 | -2.18 | -4.28 | -1.49 | -1.71 | -0.96 | -1.44 | -1.85 | -1.78 | -1.17 | -1.70 | -1.97 | -1.68 | -1.65|
| full sent prob |  |  |  |  | 0.65 | 0.81 | 0.76 | 0.55 | 0.58 | 0.78 | 0.53 | 0.02 | 0.19 | 0.16 | 0.85 | 0.90 | 0.95 | 0.87 | 0.78 | 0.87 | 0.75 | 0.90 | 0.54 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.64 | -1.83 | -2.00 | -2.35 | -2.58 | -2.19 | -2.12 | -2.66 | -4.19 | -3.70 | -1.91 | -1.55 | -1.19 | -1.76 | -2.04 | -1.82 | -2.16 | -1.70 | -3.14 | -1.69 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -3.05 | -2.86 | -2.29 | -2.31 | -2.00 | -2.04 | -1.91 | -3.59 | -2.22 | -4.32 | -1.83 | -1.70 | -1.00 | -1.77 | -1.86 | -1.77 | -1.51 | -1.73 | -2.02 | -1.68 | -1.65|
| dec-waitktgt |  |  |  |  | the | building | , | a | workshop | with | integrated | stab@@ | all | n@@ | , | two | horses | , | was | not | too | to | secure | . | </s>|
| full sent tgt |  |  |  |  | the | building | , | a | workshop | with | integrated | stab@@ | all | ung | for | two | horses | , | was | not | easy | to | secure | . | </s>|
| ref | the | building | , | a | workshop | with | integrated | stab@@ | ling | for | two | horses | , | was | not | easy | to | secure | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | es | lager@@ | te | viel | holz | und | auch | stro@@ | h@@ | b@@ | allen | darin | .|
| waitk tgt |  |  |  |  | it | stored | a | lot | of | wood | and | also | stra@@ | w | bal@@ | es | in | it | . | </s>|
| waitk prob |  |  |  |  | 0.56 | 0.16 | 0.51 | 0.88 | 0.91 | 0.73 | 0.75 | 0.48 | 0.29 | 0.96 | 0.71 | 0.98 | 0.48 | 0.86 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.21 | 0.20 | 0.58 | 0.82 | 0.91 | 0.75 | 0.67 | 0.74 | 0.30 | 0.96 | 0.40 | 0.87 | 0.06 | 0.88 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.34 | -4.18 | -2.39 | -1.51 | -1.61 | -1.80 | -2.06 | -2.10 | -3.90 | -1.02 | -3.40 | -1.69 | -1.78 | -1.67 | -1.59 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.83 | -3.70 | -2.77 | -1.28 | -1.59 | -2.09 | -1.87 | -3.38 | -3.93 | -1.06 | -2.21 | -0.90 | -2.47 | -1.63 | -1.65 | -1.64|
| full sent prob |  |  |  |  | 0.25 | 0.04 | 0.52 | 0.86 | 0.90 | 0.85 | 0.68 | 0.79 | 0.19 | 0.94 | 0.45 | 0.89 | 0.21 | 0.88 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.57 | -3.90 | -2.70 | -1.50 | -1.66 | -1.49 | -2.18 | -1.82 | -4.27 | -1.11 | -3.54 | -1.61 | -2.21 | -1.67 | -1.61 | -1.56|
| full sent KL (full->waitk) |  |  |  |  | -2.85 | -3.68 | -2.74 | -1.30 | -1.59 | -2.14 | -1.87 | -3.40 | -3.91 | -1.04 | -2.24 | -0.91 | -2.50 | -1.63 | -1.64 | -1.63|
| dec-waitktgt |  |  |  |  | it | stored | a | lot | of | wood | and | also | stra@@ | w | bal@@ | es | . | it | . | </s>|
| full sent tgt |  |  |  |  | it | had | a | lot | of | wood | and | also | stra@@ | w | bal@@ | es | . | it | . | </s>|
| ref | there | were | large | quantities | of | wood | and | bal@@ | es | of | stra@@ | w | stored | inside | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | erste | lö@@ | sch@@ | angriff | erfol@@ | gte | über | den | tan@@ | k | im | fahrzeug | .|
| waitk tgt |  |  |  |  | the | first | ext@@ | inc@@ | tion | took | place | via | the | tan@@ | k | in | the | vehicle | . | </s>|
| waitk prob |  |  |  |  | 0.71 | 0.86 | 0.23 | 0.70 | 0.97 | 0.32 | 0.92 | 0.29 | 0.85 | 0.53 | 0.93 | 0.76 | 0.89 | 0.80 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.86 | 0.92 | 0.63 | 0.03 | 0.92 | 0.00 | 0.92 | 0.49 | 0.83 | 0.93 | 0.95 | 0.78 | 0.89 | 0.85 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 67 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.61 | -1.46 | -2.31 | -0.84 | -1.26 | -2.03 | -1.48 | -2.31 | -1.92 | -0.94 | -1.25 | -1.93 | -1.67 | -1.26 | -1.71 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.79 | -1.85 | -4.05 | -1.12 | -1.02 | -2.58 | -1.50 | -3.21 | -1.81 | -3.56 | -1.32 | -2.18 | -1.65 | -1.74 | -1.76 | -1.63|
| full sent prob |  |  |  |  | 0.71 | 0.93 | 0.63 | 0.05 | 0.90 | 0.00 | 0.92 | 0.50 | 0.85 | 0.94 | 0.94 | 0.76 | 0.89 | 0.85 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 53 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.65 | -1.29 | -2.49 | -0.88 | -1.35 | -2.32 | -1.50 | -2.31 | -1.81 | -0.91 | -1.26 | -2.03 | -1.67 | -1.29 | -1.71 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.70 | -1.86 | -4.05 | -1.13 | -1.00 | -2.58 | -1.50 | -3.22 | -1.83 | -3.56 | -1.32 | -2.17 | -1.64 | -1.73 | -1.76 | -1.62|
| dec-waitktgt |  |  |  |  | the | first | ext@@ | ingu@@ | tion | attack | place | via | the | tan@@ | k | in | the | vehicle | . | </s>|
| full sent tgt |  |  |  |  | the | first | ext@@ | ingu@@ | tion | attack | place | via | the | tan@@ | k | in | the | vehicle | . | </s>|
| ref | the | first | attempt | to | ext@@ | ingu@@ | ish | the | fire | was | made | using | the | tan@@ | k | on | the | fire | engine | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | eine | weitere | leitung | erfol@@ | gte | über | einen | über@@ | fl@@ | ur@@ | - | hy@@ | d@@ | ran@@ | ten | in | rund | 100 | meter | entfernung | .|
| waitk tgt |  |  |  |  | another | line | was | given | by | a | over@@ | floor | hy@@ | d@@ | ran@@ | t | in | about | 100 | meters | away | . | </s>|
| waitk prob |  |  |  |  | 0.23 | 0.13 | 0.53 | 0.09 | 0.53 | 0.41 | 0.12 | 0.10 | 0.69 | 0.49 | 0.89 | 0.38 | 0.54 | 0.43 | 0.86 | 0.56 | 0.35 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.59 | 0.37 | 0.38 | 0.01 | 0.09 | 0.21 | 0.01 | 0.35 | 0.95 | 0.37 | 0.97 | 0.10 | 0.46 | 0.27 | 0.92 | 0.46 | 0.21 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 11 | 2 | 1 | 10 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.28 | -3.67 | -3.29 | -4.05 | -3.03 | -2.91 | -4.57 | -3.36 | -0.98 | -1.71 | -0.93 | -4.56 | -2.92 | -2.57 | -1.33 | -1.47 | -2.16 | -1.67 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.83 | -4.11 | -2.80 | -4.56 | -2.52 | -2.43 | -5.51 | -4.25 | -1.68 | -1.56 | -1.55 | -2.60 | -3.51 | -2.73 | -1.78 | -1.92 | -2.23 | -1.71 | -1.63|
| full sent prob |  |  |  |  | 0.21 | 0.62 | 0.55 | 0.02 | 0.13 | 0.24 | 0.01 | 0.22 | 0.87 | 0.62 | 0.84 | 0.48 | 0.10 | 0.59 | 0.91 | 0.51 | 0.16 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 9 | 2 | 1 | 8 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.39 | -2.55 | -2.92 | -4.53 | -3.24 | -2.33 | -3.98 | -3.75 | -1.27 | -1.59 | -1.58 | -3.71 | -3.25 | -2.13 | -1.37 | -1.72 | -2.88 | -1.64 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.78 | -4.13 | -2.87 | -4.56 | -2.53 | -2.50 | -5.51 | -4.25 | -1.65 | -1.57 | -1.46 | -2.71 | -3.36 | -2.82 | -1.77 | -1.93 | -2.27 | -1.72 | -1.62|
| dec-waitktgt |  |  |  |  | another | line | was | taken | over | an | super@@ | floor | hy@@ | dr@@ | ran@@ | ts | in | around | 100 | meters | . | . | </s>|
| full sent tgt |  |  |  |  | the | line | was | made | via | an | super@@ | floor | hy@@ | d@@ | ran@@ | t | about | about | 100 | meters | distance | . | </s>|
| ref | another | line | was | taken | from | the | surface | hy@@ | dr@@ | ant | around | 100 | metres | away | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zum | einsatz | kam | auch | im | gebäude | ein | ho@@ | hl@@ | strahl@@ | ro@@ | hr | .|
| waitk tgt |  |  |  |  | the | building | also | used | a | hol@@ | low | be@@ | am | pi@@ | pe | . | </s>|
| waitk prob |  |  |  |  | 0.26 | 0.17 | 0.45 | 0.26 | 0.69 | 0.48 | 0.99 | 0.38 | 0.99 | 0.43 | 0.88 | 0.87 | 0.91|
| dec-waitk prob |  |  |  |  | 0.21 | 0.25 | 0.45 | 0.38 | 0.62 | 0.11 | 0.62 | 0.40 | 0.94 | 0.19 | 0.94 | 0.83 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.92 | -4.66 | -2.63 | -3.33 | -2.31 | -3.37 | -2.95 | -3.17 | -1.21 | -1.47 | -1.20 | -1.99 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.35 | -5.53 | -2.66 | -3.70 | -2.22 | -3.03 | -0.60 | -3.06 | -0.87 | -1.98 | -1.57 | -1.80 | -1.64|
| full sent prob |  |  |  |  | 0.15 | 0.05 | 0.43 | 0.15 | 0.68 | 0.41 | 0.86 | 0.25 | 0.92 | 0.19 | 0.95 | 0.86 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.69 | -6.02 | -2.89 | -4.09 | -2.02 | -3.03 | -1.48 | -3.62 | -1.28 | -1.25 | -1.13 | -1.88 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -4.34 | -5.50 | -2.65 | -3.66 | -2.25 | -3.13 | -0.79 | -3.01 | -0.86 | -1.99 | -1.58 | -1.82 | -1.64|
| dec-waitktgt |  |  |  |  | the | building | also | used | a | ca@@ | low | be@@ | am | tube | pe | . | </s>|
| full sent tgt |  |  |  |  | a | building | also | used | a | hol@@ | low | be@@ | am | tube | pe | . | </s>|
| ref | a | hol@@ | low-@@ | stream | no@@ | zz@@ | le | in | the | building | was | also | used | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | im | ernst@@ | fall | erfolgt | eine | unterstützung | über | die | tages@@ | einsatz@@ | gruppe | köni@@ | gs@@ | feld | .|
| waitk tgt |  |  |  |  | in | case | of | emergency | , | support | is | provided | through | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | care | group | . | </s>|
| waitk prob |  |  |  |  | 0.36 | 0.19 | 0.85 | 0.45 | 0.74 | 0.15 | 0.63 | 0.39 | 0.36 | 0.82 | 0.61 | 0.97 | 0.92 | 0.96 | 0.88 | 0.17 | 0.33 | 0.72 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.49 | 0.62 | 0.90 | 0.25 | 0.58 | 0.30 | 0.45 | 0.65 | 0.24 | 0.79 | 0.61 | 0.92 | 0.62 | 0.96 | 0.97 | 0.47 | 0.04 | 0.43 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.69 | -1.62 | -1.58 | -2.49 | -2.75 | -2.64 | -2.74 | -2.22 | -1.96 | -2.11 | -2.48 | -1.49 | -1.45 | -1.14 | -1.04 | -2.32 | -2.94 | -2.99 | -1.68 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.32 | -4.31 | -1.87 | -2.99 | -2.19 | -3.93 | -2.40 | -3.10 | -2.02 | -2.08 | -3.07 | -1.04 | -1.01 | -1.14 | -1.82 | -3.61 | -2.32 | -2.07 | -1.72 | -1.63|
| full sent prob |  |  |  |  | 0.57 | 0.32 | 0.90 | 0.36 | 0.59 | 0.48 | 0.42 | 0.64 | 0.22 | 0.83 | 0.49 | 0.92 | 0.61 | 0.96 | 0.96 | 0.51 | 0.02 | 0.44 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.81 | -3.03 | -1.61 | -2.81 | -2.50 | -2.12 | -2.66 | -2.25 | -2.19 | -1.94 | -2.68 | -1.48 | -1.50 | -1.19 | -1.07 | -2.15 | -2.56 | -3.22 | -1.71 | -1.62|
| full sent KL (full->waitk) |  |  |  |  | -3.34 | -4.26 | -1.87 | -3.02 | -2.19 | -3.94 | -2.39 | -3.10 | -2.01 | -2.11 | -3.01 | -1.04 | -1.00 | -1.14 | -1.82 | -3.61 | -2.32 | -2.07 | -1.71 | -1.63|
| dec-waitktgt |  |  |  |  | in | case | of | an | , | support | is | provided | via | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | -@@ | group | . | </s>|
| full sent tgt |  |  |  |  | in | case | of | emergency | , | support | is | provided | via | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | -@@ | group | . | </s>|
| ref | in | case | of | emergency | , | support | is | provided | by | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | time | task | force | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | komman@@ | dan@@ | t | zeigte | sich | mit | dem | ablauf | der | ü@@ | bung | zufrieden | .|
| waitk tgt |  |  |  |  | the | comm@@ | ander | was | shown | to | be | in | good | hands | with | the | procedure | . | </s>|
| waitk prob |  |  |  |  | 0.52 | 0.68 | 0.92 | 0.18 | 0.05 | 0.36 | 0.43 | 0.08 | 0.21 | 0.24 | 0.68 | 0.77 | 0.09 | 0.60 | 0.91|
| dec-waitk prob |  |  |  |  | 0.84 | 0.92 | 0.79 | 0.13 | 0.02 | 0.01 | 0.11 | 0.09 | 0.08 | 0.05 | 0.60 | 0.79 | 0.04 | 0.65 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 8 | 11 | 2 | 1 | 2 | 3 | 0 | 0 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.80 | -1.07 | -1.36 | -3.75 | -5.09 | -3.45 | -4.07 | -4.53 | -3.69 | -2.95 | -2.11 | -2.14 | -3.42 | -2.41 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.54 | -2.82 | -1.15 | -4.52 | -5.37 | -3.36 | -2.55 | -5.23 | -3.68 | -2.76 | -2.32 | -2.31 | -4.45 | -2.34 | -1.66|
| full sent prob |  |  |  |  | 0.59 | 0.87 | 0.80 | 0.46 | 0.00 | 0.09 | 0.87 | 0.00 | 0.19 | 0.07 | 0.85 | 0.86 | 0.06 | 0.62 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 280 | 2 | 0 | 16 | 0 | 2 | 0 | 0 | 2 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.05 | -1.43 | -1.55 | -3.30 | -1.66 | -2.75 | -1.42 | -1.60 | -3.81 | -4.30 | -1.71 | -1.81 | -3.72 | -2.39 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.44 | -2.80 | -1.15 | -4.56 | -5.37 | -3.36 | -2.79 | -5.22 | -3.70 | -2.72 | -2.46 | -2.36 | -4.44 | -2.33 | -1.65|
| dec-waitktgt |  |  |  |  | the | comm@@ | ander | showed | dis@@ | in | run | the | the | shape | with | the | exercise | . | </s>|
| full sent tgt |  |  |  |  | the | comm@@ | ander | was | satisfied | satisfied | be | satisfied | good | condition | with | the | exercise | . | </s>|
| ref | the | comm@@ | ander | expressed | his | satisfaction | following | the | exercise | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dabei | zeigte | sich | wol@@ | f | beein@@ | druckt | über | die | modell@@ | projekte | zur | ausbildung | .|
| waitk tgt |  |  |  |  | wol@@ | f | was | impres@@ | sed | by | the | model | projects | for | training | . | </s>|
| waitk prob |  |  |  |  | 0.45 | 0.93 | 0.54 | 0.77 | 0.95 | 0.52 | 0.81 | 0.39 | 0.70 | 0.49 | 0.41 | 0.85 | 0.91|
| dec-waitk prob |  |  |  |  | 0.92 | 0.97 | 0.51 | 0.83 | 0.96 | 0.57 | 0.25 | 0.25 | 0.11 | 0.66 | 0.49 | 0.82 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -0.98 | -1.01 | -2.67 | -1.62 | -1.12 | -2.24 | -2.76 | -4.73 | -3.16 | -2.47 | -2.50 | -1.98 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.48 | -1.46 | -3.23 | -2.22 | -1.24 | -2.39 | -1.68 | -4.12 | -2.34 | -2.87 | -2.07 | -1.90 | -1.65|
| full sent prob |  |  |  |  | 0.84 | 0.95 | 0.70 | 0.88 | 0.95 | 0.46 | 0.70 | 0.34 | 0.36 | 0.68 | 0.54 | 0.81 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.39 | -1.27 | -2.22 | -1.50 | -1.22 | -2.39 | -2.41 | -4.20 | -3.01 | -2.47 | -2.37 | -2.00 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -3.45 | -1.44 | -3.32 | -2.25 | -1.23 | -2.36 | -1.97 | -4.15 | -2.47 | -2.88 | -2.07 | -1.89 | -1.65|
| dec-waitktgt |  |  |  |  | wol@@ | f | was | impres@@ | sed | by | this | model | training | for | training | . | </s>|
| full sent tgt |  |  |  |  | wol@@ | f | was | impres@@ | sed | by | the | model | projects | for | training | . | </s>|
| ref | during | the | presentation | , | wol@@ | f | seemed | impres@@ | sed | by | the | educational | pilot | project | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | außerdem | lob@@ | te | er | die | familien@@ | freundlichkeit | im | land@@ | kreis | .|
| waitk tgt |  |  |  |  | he | also | p@@ | raised | the | family-@@ | friendly | atmosphere | in | the | district | . | </s>|
| waitk prob |  |  |  |  | 0.47 | 0.68 | 0.73 | 0.97 | 0.70 | 0.49 | 0.83 | 0.26 | 0.52 | 0.73 | 0.41 | 0.88 | 0.91|
| dec-waitk prob |  |  |  |  | 0.60 | 0.75 | 0.91 | 0.96 | 0.60 | 0.26 | 0.54 | 0.04 | 0.55 | 0.79 | 0.29 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.61 | -2.07 | -1.12 | -1.10 | -2.39 | -4.12 | -2.00 | -4.87 | -2.07 | -2.08 | -2.01 | -1.73 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.19 | -2.40 | -2.28 | -0.99 | -2.32 | -2.08 | -1.21 | -3.60 | -2.42 | -2.21 | -2.51 | -1.83 | -1.63|
| full sent prob |  |  |  |  | 0.33 | 0.66 | 0.81 | 0.95 | 0.76 | 0.17 | 0.55 | 0.04 | 0.58 | 0.80 | 0.32 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.90 | -2.68 | -1.62 | -1.13 | -2.15 | -4.60 | -2.06 | -4.82 | -2.05 | -2.04 | -2.18 | -1.74 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.09 | -2.36 | -2.23 | -0.98 | -2.40 | -2.05 | -1.21 | -3.60 | -2.43 | -2.22 | -2.51 | -1.83 | -1.62|
| dec-waitktgt |  |  |  |  | he | also | p@@ | raised | the | family-@@ | friendly | surroundings | in | the | county | . | </s>|
| full sent tgt |  |  |  |  | he | also | p@@ | raised | the | family-@@ | friendly | surroundings | in | the | county | . | </s>|
| ref | he | also | p@@ | raised | the | family-@@ | friendly | approach | within | the | district | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | außerdem | führte | er | an | , | dass | sich | immer | mehr | beschäfti@@ | gte | um | die | pflege | und | betreuung | ihrer | an@@ | gehörigen | kü@@ | mm@@ | erten | .|
| waitk tgt |  |  |  |  | he | also | stated | that | more | and | more | employees | are | concerned | about | the | care | and | care | of | their | families | . | </s>|
| waitk prob |  |  |  |  | 0.47 | 0.80 | 0.25 | 0.89 | 0.31 | 0.83 | 0.93 | 0.50 | 0.44 | 0.25 | 0.58 | 0.35 | 0.56 | 0.79 | 0.64 | 0.84 | 0.91 | 0.37 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.51 | 0.84 | 0.12 | 0.85 | 0.16 | 0.83 | 0.87 | 0.31 | 0.41 | 0.05 | 0.41 | 0.05 | 0.77 | 0.88 | 0.79 | 0.85 | 0.91 | 0.11 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.63 | -1.75 | -3.45 | -1.99 | -4.18 | -1.92 | -1.91 | -3.62 | -2.58 | -3.95 | -2.66 | -1.89 | -1.75 | -1.69 | -1.72 | -1.88 | -1.51 | -2.44 | -1.57 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.02 | -2.06 | -3.41 | -1.67 | -3.81 | -1.92 | -1.38 | -2.16 | -3.25 | -3.51 | -1.76 | -3.11 | -2.76 | -2.00 | -2.53 | -1.92 | -1.52 | -2.21 | -1.69 | -1.66|
| full sent prob |  |  |  |  | 0.43 | 0.64 | 0.05 | 0.89 | 0.40 | 0.87 | 0.94 | 0.25 | 0.05 | 0.03 | 0.37 | 0.32 | 0.86 | 0.87 | 0.70 | 0.86 | 0.90 | 0.11 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 1 | 5 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.33 | -2.83 | -3.99 | -1.76 | -3.10 | -1.73 | -1.32 | -3.18 | -3.25 | -2.59 | -2.35 | -2.85 | -1.35 | -1.75 | -2.12 | -1.82 | -1.55 | -2.27 | -1.62 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.99 | -1.93 | -3.38 | -1.69 | -3.87 | -1.95 | -1.43 | -2.16 | -3.11 | -3.55 | -1.78 | -3.12 | -2.80 | -2.00 | -2.48 | -1.92 | -1.52 | -2.21 | -1.69 | -1.66|
| dec-waitktgt |  |  |  |  | he | also | said | that | more | and | more | employees | are | taking | about | care | care | and | care | of | their | loved | . | </s>|
| full sent tgt |  |  |  |  | he | also | mentioned | that | more | and | more | people | were | looking | with | the | care | and | care | of | their | rela@@ | . | </s>|
| ref | he | also | stated | that | an | increasing | number | of | employed | persons | are | looking | after | the | long-term | care | and | support | of | rela@@ | tives | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | aber | niemand | könne | es | sich | leisten | , | qualifizi@@ | erte | arbeitskrä@@ | fte | zu | verlieren | , | sagte | er | weiter | .|
| waitk tgt |  |  |  |  | but | no | one | can | afford | to | emplo@@ | y | skilled | workers | , | he | said | . | </s>|
| waitk prob |  |  |  |  | 0.66 | 0.57 | 0.90 | 0.80 | 0.96 | 0.85 | 0.04 | 0.97 | 0.37 | 0.68 | 0.84 | 0.84 | 0.55 | 0.64 | 0.91|
| dec-waitk prob |  |  |  |  | 0.62 | 0.57 | 0.93 | 0.80 | 0.92 | 0.15 | 0.04 | 0.95 | 0.43 | 0.66 | 0.34 | 0.78 | 0.48 | 0.40 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.48 | -2.15 | -1.32 | -1.64 | -1.41 | -1.72 | -3.35 | -1.33 | -2.27 | -2.04 | -3.18 | -2.14 | -2.89 | -3.30 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.29 | -1.81 | -1.68 | -1.67 | -1.15 | -1.45 | -4.73 | -1.09 | -3.11 | -1.89 | -1.57 | -1.77 | -2.48 | -2.72 | -1.66|
| full sent prob |  |  |  |  | 0.74 | 0.73 | 0.92 | 0.61 | 0.97 | 0.87 | 0.00 | 0.96 | 0.37 | 0.70 | 0.73 | 0.88 | 0.26 | 0.26 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 222 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.07 | -1.62 | -1.43 | -1.87 | -1.06 | -1.83 | -1.33 | -1.20 | -2.59 | -1.95 | -2.37 | -1.63 | -3.35 | -3.72 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.36 | -1.87 | -1.67 | -1.56 | -1.18 | -1.95 | -4.73 | -1.10 | -3.09 | -1.91 | -1.84 | -1.84 | -2.40 | -2.65 | -1.66|
| dec-waitktgt |  |  |  |  | but | no | one | can | afford | it | have | y | skilled | workers | , | he | said | . | </s>|
| full sent tgt |  |  |  |  | but | no | one | can | afford | to | lose | y | skilled | workers | , | he | said | . | </s>|
| ref | however | , | nobody | can | afford | to | lose | qualified | workers | , | &quot; | he | added | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ein | weiterer | , | besonders | wichtiger | faktor | sei | die | ver@@ | ne@@ | tzung | von | hoch@@ | schulen | und | unternehmen | .|
| waitk tgt |  |  |  |  | another | factor | , | particularly | important | , | is | the | net@@ | working | of | universities | and | businesses | . | </s>|
| waitk prob |  |  |  |  | 0.73 | 0.36 | 0.30 | 0.25 | 0.84 | 0.91 | 0.84 | 0.62 | 0.33 | 0.92 | 0.88 | 0.64 | 0.91 | 0.34 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.60 | 0.58 | 0.04 | 0.16 | 0.87 | 0.64 | 0.71 | 0.56 | 0.07 | 0.88 | 0.89 | 0.69 | 0.90 | 0.21 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.81 | -2.22 | -2.31 | -2.40 | -1.63 | -2.70 | -2.68 | -2.51 | -3.50 | -1.54 | -1.69 | -2.12 | -1.68 | -2.56 | -1.67 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.05 | -3.24 | -2.60 | -2.97 | -1.81 | -1.35 | -1.76 | -2.45 | -3.22 | -1.42 | -1.78 | -2.05 | -1.62 | -2.19 | -1.60 | -1.63|
| full sent prob |  |  |  |  | 0.68 | 0.39 | 0.06 | 0.17 | 0.87 | 0.72 | 0.80 | 0.79 | 0.23 | 0.89 | 0.87 | 0.72 | 0.90 | 0.22 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.24 | -2.87 | -2.43 | -2.20 | -1.59 | -2.44 | -2.20 | -1.97 | -3.78 | -1.58 | -1.74 | -1.96 | -1.65 | -2.53 | -1.66 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.10 | -3.19 | -2.59 | -2.98 | -1.82 | -1.41 | -1.81 | -2.56 | -3.26 | -1.43 | -1.76 | -2.06 | -1.63 | -2.19 | -1.60 | -1.62|
| dec-waitktgt |  |  |  |  | another | factor | that | which | important | , | is | the | lin@@ | working | of | universities | and | companies | . | </s>|
| full sent tgt |  |  |  |  | another | factor | of | which | important | , | is | the | net@@ | working | of | universities | and | companies | . | </s>|
| ref | another | , | particularly | important | factor | is | that | of | net@@ | working | between | universities | and | companies | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | denn | nur | wenn | ausreichend | aus@@ | bild@@ | ungsp@@ | lätze | angeboten | würden | , | könne | auch | der | fach@@ | kräf@@ | te@@ | bedarf | ge@@ | deckt | werden | .|
| waitk tgt |  |  |  |  | only | if | there | is | sufficient | training | place | available | can | the | professional | person | be | able | to | cover | the | needs | of | the | skilled | . | </s>|
| waitk prob |  |  |  |  | 0.29 | 0.48 | 0.20 | 0.51 | 0.62 | 0.85 | 0.17 | 0.57 | 0.58 | 0.62 | 0.16 | 0.10 | 0.14 | 0.29 | 0.89 | 0.36 | 0.56 | 0.26 | 0.79 | 0.41 | 0.31 | 0.28 | 0.91|
| dec-waitk prob |  |  |  |  | 0.70 | 0.60 | 0.12 | 0.63 | 0.54 | 0.76 | 0.21 | 0.29 | 0.00 | 0.02 | 0.11 | 0.00 | 0.37 | 0.07 | 0.89 | 0.02 | 0.49 | 0.12 | 0.54 | 0.45 | 0.12 | 0.06 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 12 | 5 | 1 | 32 | 0 | 1 | 0 | 5 | 0 | 2 | 0 | 0 | 0 | 3 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.00 | -2.50 | -2.22 | -1.66 | -1.69 | -2.17 | -4.12 | -3.19 | -3.64 | -2.51 | -3.69 | -4.51 | -3.18 | -4.50 | -1.76 | -2.76 | -2.70 | -3.86 | -2.41 | -3.35 | -4.77 | -1.60 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.36 | -2.57 | -3.03 | -1.96 | -1.59 | -1.59 | -4.28 | -2.42 | -1.93 | -2.65 | -4.73 | -4.88 | -4.62 | -3.66 | -1.78 | -2.52 | -2.50 | -3.27 | -2.12 | -3.33 | -3.83 | -3.19 | -1.64|
| full sent prob |  |  |  |  | 0.42 | 0.57 | 0.10 | 0.09 | 0.46 | 0.74 | 0.27 | 0.63 | 0.55 | 0.55 | 0.02 | 0.00 | 0.02 | 0.02 | 0.91 | 0.03 | 0.49 | 0.10 | 0.42 | 0.54 | 0.23 | 0.02 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 79 | 8 | 5 | 0 | 5 | 0 | 3 | 0 | 0 | 0 | 4 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.06 | -2.39 | -2.81 | -2.18 | -1.97 | -2.30 | -3.77 | -2.21 | -2.25 | -2.79 | -3.18 | -3.62 | -2.78 | -4.01 | -1.62 | -3.02 | -2.80 | -3.46 | -2.63 | -2.95 | -4.14 | -1.63 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.31 | -2.57 | -3.08 | -1.73 | -1.55 | -1.58 | -4.29 | -2.57 | -2.21 | -2.91 | -4.70 | -4.88 | -4.57 | -3.65 | -1.79 | -2.50 | -2.51 | -3.28 | -2.04 | -3.35 | -3.86 | -3.19 | -1.63|
| dec-waitktgt |  |  |  |  | only | if | training | is | sufficient | training | place | available | </s> | that | specialist | staff | be | provided | to | meet | the | demand | of | the | skilled | labour | </s>|
| full sent tgt |  |  |  |  | only | if | adequate | were | sufficient | training | place | available | can | the | need | needs | &apos;s | met | to | meet | the | demand | of | the | skilled | labour | </s>|
| ref | for | it | is | only | if | a | sufficient | number | of | educational | places | can | be | provided | that | the | need | for | skilled | workers | can | be | covered | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | früher | wurden | die | älteren | mit@@ | bürger | in | der | ra@@ | st@@ | stä@@ | tte | be@@ | wir@@ | tet | .|
| waitk tgt |  |  |  |  | in | the | past | , | the | elderly | were | forced | to | rest | in | the | re@@ | sting | place | . | </s>|
| waitk prob |  |  |  |  | 0.33 | 0.70 | 0.73 | 0.80 | 0.35 | 0.86 | 0.40 | 0.07 | 0.46 | 0.15 | 0.42 | 0.73 | 0.13 | 0.90 | 0.21 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.18 | 0.84 | 0.79 | 0.67 | 0.32 | 0.70 | 0.14 | 0.00 | 0.72 | 0.02 | 0.51 | 0.75 | 0.23 | 0.87 | 0.52 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 57 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.80 | -1.80 | -1.87 | -2.59 | -3.05 | -2.06 | -3.31 | -4.79 | -1.66 | -4.11 | -2.97 | -2.23 | -4.13 | -1.50 | -2.91 | -1.71 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.55 | -2.34 | -1.93 | -1.84 | -3.07 | -1.35 | -3.18 | -4.62 | -2.16 | -3.85 | -2.91 | -2.26 | -5.16 | -1.07 | -4.25 | -1.73 | -1.63|
| full sent prob |  |  |  |  | 0.35 | 0.72 | 0.86 | 0.53 | 0.55 | 0.62 | 0.43 | 0.00 | 0.52 | 0.04 | 0.64 | 0.77 | 0.19 | 0.88 | 0.46 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 368 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.38 | -2.35 | -1.47 | -2.44 | -2.62 | -2.36 | -3.42 | -4.51 | -1.68 | -4.08 | -2.01 | -2.11 | -4.09 | -1.43 | -3.14 | -1.76 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.59 | -2.27 | -1.97 | -1.76 | -3.11 | -1.30 | -3.24 | -4.63 | -2.14 | -3.85 | -2.96 | -2.28 | -5.16 | -1.08 | -4.25 | -1.72 | -1.63|
| dec-waitktgt |  |  |  |  | in | the | past | , | the | elderly | became | the | to | re@@ | in | the | re@@ | sting | place | . | </s>|
| full sent tgt |  |  |  |  | in | the | past | , | the | elderly | were | treated | to | stay | in | the | re@@ | sting | place | . | </s>|
| ref | previously | , | the | elderly | citizens | were | ho@@ | sted | in | the | service | station | can@@ | teen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | mittlerweile | findet | dieser | nachmittag | im | pf@@ | le@@ | gehei@@ | m | st. | jo@@ | se@@ | f | statt | .|
| waitk tgt |  |  |  |  | meanwhile | , | this | afternoon | , | the | st. | jo@@ | se@@ | f | nur@@ | sing | home | is | being | held | . | </s>|
| waitk prob |  |  |  |  | 0.19 | 0.44 | 0.51 | 0.91 | 0.17 | 0.22 | 0.20 | 0.80 | 0.92 | 0.96 | 0.78 | 0.94 | 0.68 | 0.64 | 0.22 | 0.48 | 0.86 | 0.91|
| dec-waitk prob |  |  |  |  | 0.27 | 0.53 | 0.58 | 0.90 | 0.01 | 0.13 | 0.04 | 0.37 | 0.93 | 0.96 | 0.46 | 0.93 | 0.71 | 0.17 | 0.04 | 0.84 | 0.84 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 9 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.16 | -2.45 | -2.46 | -1.50 | -2.83 | -4.03 | -5.40 | -3.08 | -1.36 | -1.20 | -3.26 | -1.22 | -2.50 | -2.70 | -4.33 | -1.43 | -1.92 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.84 | -2.36 | -2.79 | -1.52 | -3.59 | -3.52 | -5.12 | -1.38 | -1.47 | -1.20 | -1.57 | -1.09 | -2.65 | -2.42 | -3.62 | -3.54 | -1.83 | -1.65|
| full sent prob |  |  |  |  | 0.11 | 0.30 | 0.36 | 0.87 | 0.01 | 0.17 | 0.15 | 0.55 | 0.94 | 0.96 | 0.46 | 0.92 | 0.69 | 0.36 | 0.05 | 0.71 | 0.80 | 0.91|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.73 | -2.90 | -2.71 | -1.75 | -2.65 | -3.78 | -4.88 | -2.68 | -1.27 | -1.19 | -3.30 | -1.24 | -2.58 | -3.07 | -4.62 | -2.07 | -2.03 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.83 | -2.29 | -2.72 | -1.50 | -3.60 | -3.52 | -5.14 | -1.49 | -1.48 | -1.20 | -1.56 | -1.09 | -2.64 | -2.51 | -3.61 | -3.49 | -1.81 | -1.65|
| dec-waitktgt |  |  |  |  | meanwhile | , | this | afternoon | is | in | nur@@ | jo@@ | se@@ | f | nur@@ | sing | home | , | taking | held | . | </s>|
| full sent tgt |  |  |  |  | this | , | this | afternoon | is | the | st. | jo@@ | se@@ | f | nur@@ | sing | home | is | taking | held | . | </s>|
| ref | the | coffee | afternoon | is | now | held | in | the | st. | jo@@ | se@@ | f | nur@@ | sing | home | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | heim@@ | bewohner | freu@@ | ten | sich | auf | die | le@@ | ck@@ | eren | ku@@ | chen | und | tor@@ | ten | .|
| waitk tgt |  |  |  |  | the | residents | were | looking | forward | to | the | delicious | ca@@ | kes | and | ca@@ | kes | . | </s>|
| waitk prob |  |  |  |  | 0.33 | 0.19 | 0.29 | 0.49 | 0.94 | 0.88 | 0.43 | 0.53 | 0.79 | 0.78 | 0.88 | 0.71 | 0.90 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.74 | 0.09 | 0.53 | 0.17 | 0.87 | 0.87 | 0.50 | 0.44 | 0.97 | 0.72 | 0.87 | 0.68 | 0.94 | 0.87 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.17 | -3.82 | -3.00 | -3.38 | -1.72 | -1.81 | -3.07 | -2.43 | -0.91 | -1.15 | -1.76 | -2.37 | -1.09 | -1.84 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.22 | -3.69 | -3.70 | -2.90 | -1.10 | -1.77 | -2.96 | -1.74 | -2.13 | -1.33 | -1.77 | -2.05 | -1.10 | -1.73 | -1.63|
| full sent prob |  |  |  |  | 0.58 | 0.18 | 0.30 | 0.25 | 0.90 | 0.89 | 0.62 | 0.50 | 0.98 | 0.87 | 0.90 | 0.69 | 0.96 | 0.89 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.98 | -3.91 | -3.85 | -3.47 | -1.50 | -1.68 | -2.68 | -2.24 | -0.81 | -1.06 | -1.67 | -2.50 | -1.02 | -1.75 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -4.18 | -3.70 | -3.65 | -2.93 | -1.13 | -1.79 | -3.00 | -1.76 | -2.14 | -1.41 | -1.79 | -2.06 | -1.12 | -1.74 | -1.63|
| dec-waitktgt |  |  |  |  | the | inhabitants | were | happy | forward | to | the | delicious | ca@@ | kes | and | ca@@ | kes | . | </s>|
| full sent tgt |  |  |  |  | the | residents | were | looking | forward | to | the | delicious | ca@@ | kes | and | ca@@ | kes | . | </s>|
| ref | the | residents | of | the | home | were | delighted | with | the | delicious | ca@@ | kes | and | tar@@ | ts | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | eine | entscheidung | darüber | wird | voraus@@ | sichtlich | bereits | im | kommenden | jahr | fallen | .|
| waitk tgt |  |  |  |  | a | decision | on | this | is | expected | to | be | taken | next | year | . | </s>|
| waitk prob |  |  |  |  | 0.42 | 0.91 | 0.59 | 0.69 | 0.48 | 0.82 | 0.86 | 0.53 | 0.58 | 0.42 | 0.91 | 0.85 | 0.91|
| dec-waitk prob |  |  |  |  | 0.57 | 0.92 | 0.61 | 0.58 | 0.60 | 0.61 | 0.88 | 0.59 | 0.59 | 0.66 | 0.93 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.66 | -1.39 | -2.30 | -2.45 | -2.61 | -2.15 | -1.73 | -2.57 | -2.17 | -2.07 | -1.43 | -1.66 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.11 | -1.52 | -2.20 | -2.11 | -2.87 | -1.48 | -1.89 | -2.77 | -2.16 | -2.87 | -1.57 | -1.92 | -1.65|
| full sent prob |  |  |  |  | 0.41 | 0.92 | 0.70 | 0.71 | 0.46 | 0.67 | 0.88 | 0.62 | 0.56 | 0.63 | 0.94 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.79 | -1.46 | -2.06 | -2.15 | -2.83 | -1.96 | -1.78 | -2.44 | -2.17 | -2.12 | -1.34 | -1.69 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.08 | -1.52 | -2.23 | -2.18 | -2.84 | -1.52 | -1.89 | -2.78 | -2.15 | -2.87 | -1.58 | -1.91 | -1.64|
| dec-waitktgt |  |  |  |  | a | decision | on | this | is | expected | to | be | taken | next | year | . | </s>|
| full sent tgt |  |  |  |  | a | decision | on | this | is | expected | to | be | taken | next | year | . | </s>|
| ref | a | decision | is | expected | to | be | made | in | the | coming | year | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | tiefe | ri@@ | sse | in | einzelnen | st@@ | einen | zeugen | von | wi@@ | tter@@ | ungs@@ | schäden | , | jedoch | ist | die | mauer | derzeit | nicht | ein@@ | stur@@ | z@@ | gefährdet | .|
| waitk tgt |  |  |  |  | deep | cr@@ | acks | in | individual | stones | bear | witness | to | the | damage | caused | by | weather | , | but | the | wall | is | not | at | present | at | risk | of | collapse | . | </s>|
| waitk prob |  |  |  |  | 0.46 | 0.69 | 0.93 | 0.78 | 0.48 | 0.74 | 0.15 | 0.96 | 0.86 | 0.13 | 0.50 | 0.43 | 0.82 | 0.39 | 0.42 | 0.70 | 0.64 | 0.86 | 0.58 | 0.69 | 0.32 | 0.85 | 0.31 | 0.94 | 0.86 | 0.72 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.68 | 0.68 | 0.92 | 0.68 | 0.52 | 0.47 | 0.18 | 0.98 | 0.90 | 0.08 | 0.46 | 0.30 | 0.81 | 0.54 | 0.49 | 0.74 | 0.66 | 0.87 | 0.65 | 0.77 | 0.14 | 0.84 | 0.09 | 0.95 | 0.86 | 0.66 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.37 | -1.88 | -1.30 | -2.54 | -2.82 | -3.10 | -3.61 | -0.96 | -1.63 | -2.54 | -2.23 | -2.89 | -1.68 | -1.89 | -2.44 | -2.12 | -2.46 | -1.69 | -2.25 | -2.00 | -3.68 | -1.52 | -3.26 | -1.20 | -1.79 | -1.82 | -1.60 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.69 | -2.32 | -1.15 | -2.07 | -2.24 | -1.48 | -3.67 | -1.01 | -1.89 | -3.98 | -3.20 | -2.53 | -1.72 | -2.70 | -2.16 | -2.33 | -2.34 | -1.77 | -2.68 | -2.27 | -2.68 | -1.60 | -2.48 | -1.20 | -1.75 | -1.85 | -1.69 | -1.65|
| full sent prob |  |  |  |  | 0.43 | 0.90 | 0.93 | 0.64 | 0.37 | 0.56 | 0.10 | 0.76 | 0.89 | 0.06 | 0.59 | 0.35 | 0.80 | 0.49 | 0.50 | 0.69 | 0.73 | 0.92 | 0.71 | 0.70 | 0.15 | 0.77 | 0.08 | 0.95 | 0.88 | 0.57 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.64 | -1.23 | -1.27 | -2.64 | -3.57 | -2.77 | -3.87 | -2.23 | -1.68 | -3.13 | -2.33 | -2.52 | -1.68 | -1.96 | -2.49 | -2.22 | -2.22 | -1.37 | -2.19 | -2.24 | -3.59 | -1.62 | -3.33 | -1.17 | -1.76 | -2.03 | -1.65 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.60 | -2.44 | -1.16 | -2.05 | -2.18 | -1.53 | -3.65 | -0.84 | -1.89 | -3.97 | -3.25 | -2.55 | -1.71 | -2.69 | -2.19 | -2.31 | -2.37 | -1.80 | -2.71 | -2.23 | -2.68 | -1.56 | -2.48 | -1.21 | -1.76 | -1.80 | -1.68 | -1.65|
| dec-waitktgt |  |  |  |  | deep | cr@@ | acks | in | individual | stones | testi@@ | witness | to | weather | damage | caused | by | weather | , | but | the | wall | is | not | in | present | in | risk | of | collapse | . | </s>|
| full sent tgt |  |  |  |  | deep | cr@@ | acks | in | individual | stones | are | witness | to | weather | damage | caused | by | weather | , | but | the | wall | is | not | in | present | in | risk | of | collapse | . | </s>|
| ref | deep | cr@@ | acks | in | a | number | of | individual | stones | testi@@ | fy | to | the | weather | damage | , | however | , | at | present | the | wall | is | not | in | danger | of | collapse | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ö@@ | z@@ | de@@ | mir | will | ja@@ | zz@@ | ausbildung | in | st@@ | utt@@ | gar@@ | t | erhalten|
| waitk tgt |  |  |  |  | ö@@ | z@@ | dem@@ | ir | wants | to | train | jazz | in | stutt@@ | gart | . | </s>|
| waitk prob |  |  |  |  | 0.29 | 0.93 | 0.97 | 0.98 | 0.60 | 0.84 | 0.37 | 0.88 | 0.23 | 0.94 | 0.95 | 0.42 | 0.91|
| dec-waitk prob |  |  |  |  | 0.70 | 0.95 | 0.95 | 0.95 | 0.66 | 0.76 | 0.08 | 0.61 | 0.82 | 0.99 | 0.97 | 0.02 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.23 | -1.15 | -1.14 | -1.22 | -2.26 | -2.05 | -4.53 | -2.37 | -1.59 | -0.84 | -1.02 | -1.50 | -1.49|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.45 | -1.48 | -1.01 | -0.93 | -2.41 | -1.61 | -3.08 | -1.26 | -4.02 | -1.33 | -1.31 | -2.44 | -1.64|
| full sent prob |  |  |  |  | 0.86 | 0.96 | 0.95 | 0.97 | 0.40 | 0.91 | 0.00 | 0.84 | 0.79 | 1.00 | 0.96 | 0.01 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.35 | -1.16 | -1.25 | -1.07 | -2.95 | -1.54 | -2.43 | -1.64 | -1.82 | -0.83 | -1.14 | -1.66 | -1.52|
| full sent KL (full->waitk) |  |  |  |  | -4.49 | -1.49 | -1.00 | -0.95 | -2.28 | -1.71 | -3.08 | -1.42 | -4.02 | -1.33 | -1.30 | -2.44 | -1.64|
| dec-waitktgt |  |  |  |  | ö@@ | z@@ | dem@@ | ir | wants | to | train | jazz | in | stutt@@ | gart | </s> | </s>|
| full sent tgt |  |  |  |  | ö@@ | z@@ | dem@@ | ir | wants | to | receive | jazz | in | stutt@@ | gart | </s> | </s>|
| ref | ö@@ | z@@ | dem@@ | ir | wants | jazz | training | in | stutt@@ | gart | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ja@@ | z@@ | z | und | klassi@@ | k | gehören | gerade | am | ja@@ | zz@@ | standort | st@@ | utt@@ | gar@@ | t | zusammen | .|
| waitk tgt |  |  |  |  | jazz | and | classical | music | are | part | of | the | festival | at | the | jazz | location | in | stutt@@ | gart | . | </s>|
| waitk prob |  |  |  |  | 0.79 | 0.82 | 0.75 | 0.76 | 0.53 | 0.09 | 0.89 | 0.45 | 0.03 | 0.19 | 0.63 | 0.62 | 0.39 | 0.36 | 0.96 | 0.95 | 0.75 | 0.91|
| dec-waitk prob |  |  |  |  | 0.93 | 0.88 | 0.66 | 0.04 | 0.48 | 0.05 | 0.89 | 0.63 | 0.00 | 0.27 | 0.83 | 0.14 | 0.42 | 0.12 | 0.98 | 0.97 | 0.87 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 0 | 16 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.15 | -1.71 | -1.73 | -3.47 | -2.67 | -2.81 | -1.69 | -2.43 | -4.50 | -4.11 | -1.73 | -3.83 | -3.31 | -1.50 | -0.97 | -1.12 | -1.65 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.21 | -2.03 | -1.42 | -1.37 | -2.95 | -4.36 | -1.73 | -3.05 | -5.57 | -4.62 | -2.40 | -2.03 | -3.46 | -2.19 | -1.20 | -1.27 | -2.26 | -1.62|
| full sent prob |  |  |  |  | 0.86 | 0.87 | 0.58 | 0.32 | 0.56 | 0.06 | 0.91 | 0.73 | 0.02 | 0.36 | 0.79 | 0.53 | 0.37 | 0.08 | 0.98 | 0.96 | 0.87 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.52 | -1.82 | -2.08 | -3.25 | -2.61 | -3.27 | -1.51 | -1.85 | -4.72 | -3.60 | -2.01 | -3.13 | -3.56 | -1.12 | -0.95 | -1.16 | -1.69 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.17 | -2.03 | -1.38 | -1.55 | -2.98 | -4.34 | -1.75 | -3.09 | -5.57 | -4.63 | -2.38 | -2.22 | -3.44 | -2.18 | -1.20 | -1.27 | -2.26 | -1.61|
| dec-waitktgt |  |  |  |  | jazz | and | classical | are | are | just | of | the | jazz | at | the | stutt@@ | location | stutt@@ | stutt@@ | gart | . | </s>|
| full sent tgt |  |  |  |  | jazz | and | classical | music | are | currently | of | the | jazz | at | the | jazz | location | stutt@@ | stutt@@ | gart | . | </s>|
| ref | jazz | and | classical | music | belong | together | at | the | jazz | location | of | stutt@@ | gart | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | tun@@ | nel | war | den | angaben | zufolge | noch | nicht | in | gebrauch | genommen | worden | .|
| waitk tgt |  |  |  |  | the | tunnel | was | still | not | in | use | , | according | to | the | information | . | </s>|
| waitk prob |  |  |  |  | 0.68 | 0.94 | 0.25 | 0.15 | 0.44 | 0.23 | 0.72 | 0.53 | 0.48 | 0.90 | 0.53 | 0.59 | 0.25 | 0.91|
| dec-waitk prob |  |  |  |  | 0.80 | 0.92 | 0.56 | 0.26 | 0.38 | 0.53 | 0.94 | 0.62 | 0.78 | 0.91 | 0.55 | 0.21 | 0.23 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.02 | -1.31 | -2.62 | -3.67 | -3.40 | -2.91 | -0.98 | -2.65 | -1.61 | -1.65 | -2.97 | -3.19 | -2.54 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.81 | -1.23 | -3.59 | -4.23 | -3.26 | -4.28 | -1.96 | -2.82 | -2.54 | -1.70 | -2.83 | -2.13 | -2.85 | -1.64|
| full sent prob |  |  |  |  | 0.28 | 0.75 | 0.20 | 0.01 | 0.52 | 0.13 | 0.97 | 0.64 | 0.81 | 0.91 | 0.61 | 0.21 | 0.21 | 0.91|
| full sent rank |  |  |  |  | 1 | 0 | 1 | 13 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.51 | -2.52 | -2.58 | -3.82 | -2.72 | -1.84 | -0.82 | -2.31 | -1.49 | -1.62 | -2.67 | -2.74 | -2.58 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.52 | -1.10 | -3.56 | -4.21 | -3.31 | -4.20 | -1.98 | -2.83 | -2.55 | -1.70 | -2.86 | -2.14 | -2.84 | -1.64|
| dec-waitktgt |  |  |  |  | the | tunnel | was | still | not | in | use | , | according | to | the | figures | provided | </s>|
| full sent tgt |  |  |  |  | according | tunnel | has | not | not | used | use | , | according | to | the | figures | provided | </s>|
| ref | according | to | the | details | provided | , | the | tunnel | had | not | yet | been | put | into | use | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sowohl | die | us-@@ | behörden | als | auch | die | mexi@@ | kanischen | sicherheit@@ | skrä@@ | fte | befinden | sich | in | einem | dauer@@ | -@@ | kampf | gegen | die | drogen@@ | kar@@ | t@@ | elle | .|
| waitk tgt |  |  |  |  | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | are | in | a | permanent | struggle | against | drug | car@@ | te@@ | ls | . | </s>|
| waitk prob |  |  |  |  | 0.80 | 0.79 | 0.87 | 0.65 | 0.84 | 0.74 | 0.90 | 0.93 | 0.94 | 0.95 | 0.72 | 0.82 | 0.70 | 0.70 | 0.25 | 0.28 | 0.86 | 0.54 | 0.80 | 0.98 | 0.96 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.88 | 0.83 | 0.90 | 0.81 | 0.91 | 0.15 | 0.90 | 0.98 | 0.90 | 0.95 | 0.78 | 0.84 | 0.80 | 0.77 | 0.29 | 0.51 | 0.03 | 0.25 | 0.80 | 0.16 | 0.98 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.57 | -1.69 | -1.45 | -1.59 | -1.58 | -1.60 | -1.24 | -1.02 | -1.60 | -1.22 | -1.89 | -1.82 | -1.98 | -1.67 | -3.36 | -1.90 | -3.63 | -2.28 | -1.87 | -2.09 | -0.95 | -1.78 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -1.94 | -1.98 | -1.54 | -2.39 | -1.93 | -1.68 | -1.48 | -1.44 | -1.32 | -1.25 | -2.06 | -1.72 | -2.32 | -1.87 | -3.20 | -2.80 | -1.09 | -1.77 | -1.86 | -0.29 | -1.20 | -1.61 | -1.64|
| full sent prob |  |  |  |  | 0.81 | 0.83 | 0.87 | 0.82 | 0.90 | 0.47 | 0.95 | 0.96 | 0.92 | 0.95 | 0.82 | 0.87 | 0.60 | 0.66 | 0.35 | 0.27 | 0.85 | 0.13 | 0.98 | 0.97 | 0.96 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.79 | -1.79 | -1.64 | -1.71 | -1.65 | -1.77 | -1.12 | -1.14 | -1.52 | -1.26 | -1.74 | -1.58 | -2.68 | -2.22 | -3.34 | -1.94 | -1.86 | -1.70 | -0.83 | -1.00 | -1.13 | -1.64 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -1.89 | -1.98 | -1.52 | -2.39 | -1.92 | -1.85 | -1.52 | -1.43 | -1.34 | -1.24 | -2.09 | -1.73 | -2.21 | -1.80 | -3.21 | -2.78 | -1.67 | -1.77 | -1.97 | -0.94 | -1.18 | -1.63 | -1.64|
| dec-waitktgt |  |  |  |  | both | the | us | authorities | and | mexico | mex@@ | ic@@ | an | security | forces | are | in | a | permanent | struggle | </s> | drugs | car@@ | t | ls | . | </s>|
| full sent tgt |  |  |  |  | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | are | in | a | permanent | fight | against | the | car@@ | te@@ | ls | . | </s>|
| ref | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | are | engaged | in | an | ongoing | battle | against | the | drug | car@@ | te@@ | ls | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | seit | 2006 | wurden | in | mexiko | mehr | als | 7@@ | 7. | 000 | menschen | im | zusammenhang | mit | der | drogen@@ | kriminalität | get@@ | ö@@ | tet | .|
| waitk tgt |  |  |  |  | since | 2006 | , | more | than | 7@@ | 7@@ | ,000 | people | have | been | killed | in | mexico | in | connection | with | dru@@ | g-@@ | related | crime | . | </s>|
| waitk prob |  |  |  |  | 0.47 | 0.91 | 0.85 | 0.43 | 0.92 | 0.90 | 0.95 | 0.36 | 0.87 | 0.71 | 0.86 | 0.14 | 0.81 | 0.97 | 0.64 | 0.76 | 0.90 | 0.48 | 0.85 | 0.97 | 0.90 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.18 | 0.87 | 0.83 | 0.02 | 0.90 | 0.91 | 0.75 | 0.35 | 0.74 | 0.79 | 0.86 | 0.01 | 0.86 | 0.96 | 0.05 | 0.23 | 0.91 | 0.36 | 0.94 | 0.97 | 0.71 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.36 | -1.86 | -1.88 | -1.07 | -1.66 | -1.18 | -1.96 | -2.74 | -2.52 | -1.95 | -1.83 | -3.25 | -1.81 | -1.11 | -4.49 | -2.73 | -1.58 | -1.83 | -0.96 | -1.01 | -2.24 | -1.77 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.26 | -1.52 | -1.79 | -2.53 | -1.47 | -1.33 | -1.00 | -3.88 | -1.60 | -1.95 | -1.63 | -4.06 | -1.95 | -1.05 | -2.38 | -1.24 | -1.68 | -1.71 | -1.36 | -0.98 | -1.32 | -1.66 | -1.64|
| full sent prob |  |  |  |  | 0.49 | 0.87 | 0.66 | 0.51 | 0.93 | 0.82 | 0.90 | 0.84 | 0.88 | 0.91 | 0.89 | 0.91 | 0.88 | 0.92 | 0.63 | 0.54 | 0.92 | 0.46 | 0.83 | 0.96 | 0.81 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.18 | -1.82 | -2.08 | -1.62 | -1.47 | -1.59 | -1.36 | -1.39 | -1.58 | -1.31 | -1.58 | -0.80 | -1.71 | -1.46 | -2.62 | -2.10 | -1.48 | -1.91 | -1.21 | -1.12 | -2.00 | -1.69 | -1.56|
| full sent KL (full->waitk) |  |  |  |  | -3.36 | -1.52 | -1.67 | -2.60 | -1.49 | -1.27 | -1.12 | -4.00 | -1.70 | -2.02 | -1.65 | -4.16 | -1.96 | -1.01 | -2.69 | -1.42 | -1.68 | -1.72 | -1.29 | -0.97 | -1.39 | -1.67 | -1.64|
| dec-waitktgt |  |  |  |  | mexico | 2006 | , | mexico | than | 7@@ | 7@@ | ,000 | people | have | been | living | in | mexico | . | the | with | drug | g-@@ | related | crime | . | </s>|
| full sent tgt |  |  |  |  | since | 2006 | , | more | than | 7@@ | 7@@ | ,000 | people | have | been | killed | in | mexico | in | connection | with | dru@@ | g-@@ | related | crime | . | </s>|
| ref | since | 2006 | , | more | than | 7@@ | 7@@ | ,000 | people | have | been | killed | in | conjunction | with | drug | crime | in | mexico | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | glei@@ | san@@ | lage | war | so | ausgestattet | , | dass | dort | elektri@@ | sch | betrie@@ | bene | wagen | eingesetzt | werden | konnten | .|
| waitk tgt |  |  |  |  | the | track | system | was | equipped | to | allow | electrical | connections | to | the | vehicle | . | </s>|
| waitk prob |  |  |  |  | 0.42 | 0.67 | 0.50 | 0.77 | 0.27 | 0.30 | 0.11 | 0.16 | 0.09 | 0.33 | 0.39 | 0.13 | 0.41 | 0.91|
| dec-waitk prob |  |  |  |  | 0.62 | 0.20 | 0.05 | 0.75 | 0.46 | 0.29 | 0.00 | 0.03 | 0.05 | 0.32 | 0.02 | 0.02 | 0.63 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 63 | 8 | 2 | 1 | 3 | 5 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.82 | -4.12 | -2.87 | -2.25 | -2.69 | -3.07 | -4.54 | -3.41 | -3.85 | -2.28 | -2.64 | -4.83 | -2.75 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.93 | -1.89 | -2.81 | -1.96 | -3.15 | -2.46 | -4.09 | -3.32 | -4.57 | -3.06 | -2.91 | -4.69 | -3.38 | -1.65|
| full sent prob |  |  |  |  | 0.60 | 0.32 | 0.37 | 0.79 | 0.63 | 0.44 | 0.05 | 0.02 | 0.00 | 0.59 | 0.00 | 0.03 | 0.71 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 13 | 101 | 0 | 6 | 3 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.96 | -2.95 | -2.99 | -2.01 | -2.09 | -2.48 | -4.18 | -3.36 | -2.52 | -2.36 | -1.14 | -4.51 | -2.26 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.93 | -1.96 | -2.92 | -1.98 | -3.18 | -2.48 | -4.09 | -3.32 | -4.54 | -3.10 | -2.97 | -4.69 | -3.40 | -1.64|
| dec-waitktgt |  |  |  |  | the | track | was | was | equipped | to | provide | the | power | . | be | track | . | </s>|
| full sent tgt |  |  |  |  | the | track | system | was | equipped | to | operate | electric | cars | to | be | track | . | </s>|
| ref | the | railway | system | was | equipped | in | such | a | way | that | electr@@ | ically | powered | car@@ | ts | could | be | used | on | it | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | auf | mexi@@ | kan@@ | ischer | seite | liegt | der | zugang | in | einem | gebäude | , | das | 80 | meter | von | der | grenze | entfernt | ist | .|
| waitk tgt |  |  |  |  | on | the | mex@@ | ic@@ | an | side | , | there | is | access | in | a | building | that | is | 80 | meters | from | the | border | . | </s>|
| waitk prob |  |  |  |  | 0.43 | 0.59 | 0.95 | 0.95 | 0.93 | 0.89 | 0.43 | 0.23 | 0.79 | 0.43 | 0.50 | 0.79 | 0.82 | 0.29 | 0.82 | 0.72 | 0.61 | 0.54 | 0.90 | 0.83 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.68 | 0.83 | 0.97 | 0.97 | 0.93 | 0.96 | 0.61 | 0.12 | 0.81 | 0.51 | 0.04 | 0.82 | 0.91 | 0.34 | 0.69 | 0.76 | 0.45 | 0.50 | 0.86 | 0.87 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.13 | -1.60 | -0.97 | -1.10 | -1.32 | -1.06 | -2.83 | -3.49 | -1.95 | -2.56 | -1.44 | -1.90 | -1.39 | -2.11 | -2.48 | -2.15 | -1.56 | -2.14 | -1.86 | -1.64 | -1.66 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.05 | -2.17 | -1.17 | -1.29 | -1.37 | -1.68 | -2.58 | -3.41 | -1.96 | -2.36 | -2.38 | -1.95 | -2.06 | -2.92 | -1.80 | -2.32 | -1.78 | -2.16 | -1.65 | -1.87 | -1.78 | -1.64|
| full sent prob |  |  |  |  | 0.43 | 0.86 | 0.94 | 0.92 | 0.93 | 0.96 | 0.54 | 0.01 | 0.82 | 0.83 | 0.13 | 0.78 | 0.91 | 0.25 | 0.89 | 0.73 | 0.49 | 0.55 | 0.88 | 0.88 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.26 | -1.60 | -1.27 | -1.49 | -1.38 | -1.11 | -2.49 | -2.07 | -1.80 | -1.38 | -1.65 | -1.99 | -1.35 | -2.63 | -1.62 | -2.18 | -1.56 | -2.13 | -1.79 | -1.56 | -1.70 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -2.97 | -2.17 | -1.14 | -1.25 | -1.37 | -1.68 | -2.56 | -3.44 | -1.96 | -2.45 | -2.40 | -1.93 | -2.06 | -2.88 | -1.93 | -2.30 | -1.79 | -2.17 | -1.67 | -1.88 | -1.78 | -1.63|
| dec-waitktgt |  |  |  |  | on | the | mex@@ | ic@@ | an | side | , | access | is | access | to | a | building | 80 | is | 80 | meters | from | the | border | . | </s>|
| full sent tgt |  |  |  |  | on | the | mex@@ | ic@@ | an | side | , | access | is | access | to | a | building | 80 | is | 80 | meters | from | the | border | . | </s>|
| ref | on | the | mex@@ | ic@@ | an | side | , | the | entrance | is | located | in | a | building | located | 80 | metres | from | the | border | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | laut | behörden | führt | eine | leiter | 20 | meter | in | die | tiefe | zum | eigent@@ | lichen | tun@@ | n@@ | el@@ | eingang | .|
| waitk tgt |  |  |  |  | according | to | the | authorities | , | a | lad@@ | der | leads | into | the | deep | 20 | meters | to | the | actual | tunnel | entrance | . | </s>|
| waitk prob |  |  |  |  | 0.71 | 0.91 | 0.62 | 0.71 | 0.70 | 0.68 | 0.78 | 0.98 | 0.23 | 0.23 | 0.77 | 0.37 | 0.27 | 0.45 | 0.66 | 0.83 | 0.47 | 0.54 | 0.53 | 0.88 | 0.91|
| dec-waitk prob |  |  |  |  | 0.90 | 0.92 | 0.58 | 0.84 | 0.87 | 0.83 | 0.30 | 0.98 | 0.16 | 0.00 | 0.52 | 0.13 | 0.02 | 0.49 | 0.63 | 0.77 | 0.32 | 0.85 | 0.80 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 11 | 0 | 2 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.22 | -1.55 | -2.46 | -1.58 | -1.70 | -1.78 | -3.11 | -0.97 | -3.60 | -1.63 | -2.68 | -1.80 | -4.61 | -2.06 | -2.74 | -2.25 | -3.23 | -1.40 | -1.55 | -1.70 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.29 | -1.63 | -2.35 | -2.56 | -2.23 | -2.36 | -1.59 | -0.96 | -3.78 | -3.53 | -1.84 | -1.78 | -4.20 | -2.15 | -2.54 | -1.89 | -2.88 | -2.47 | -2.41 | -1.80 | -1.62|
| full sent prob |  |  |  |  | 0.68 | 0.91 | 0.59 | 0.81 | 0.73 | 0.78 | 0.36 | 0.99 | 0.12 | 0.01 | 0.69 | 0.13 | 0.07 | 0.53 | 0.58 | 0.79 | 0.39 | 0.88 | 0.72 | 0.89 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.47 | -1.63 | -2.38 | -1.84 | -2.06 | -1.94 | -3.33 | -0.92 | -3.21 | -1.93 | -2.25 | -2.06 | -4.82 | -1.96 | -2.89 | -2.18 | -2.89 | -1.28 | -1.88 | -1.72 | -1.56|
| full sent KL (full->waitk) |  |  |  |  | -2.17 | -1.63 | -2.36 | -2.54 | -2.15 | -2.34 | -1.63 | -0.96 | -3.78 | -3.53 | -1.94 | -1.79 | -4.21 | -2.16 | -2.52 | -1.91 | -2.91 | -2.48 | -2.39 | -1.80 | -1.62|
| dec-waitktgt |  |  |  |  | according | to | the | authorities | , | a | lad@@ | der | takes | 20 | the | dep@@ | tunnel | meters | to | the | actual | tunnel | entrance | . | </s>|
| full sent tgt |  |  |  |  | according | to | the | authorities | , | a | lad@@ | der | takes | 20 | the | depth | 20 | meters | to | the | actual | tunnel | entrance | . | </s>|
| ref | according | to | the | authorities | , | a | lad@@ | der | runs | 20 | metres | underground | to | the | actual | entrance | of | the | tunnel | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | tun@@ | nel | hat | einen | quer@@ | schnitt | von | 1,@@ | 20 | meter | höhe | und | 90 | z@@ | enti@@ | meter | breite | .|
| waitk tgt |  |  |  |  | the | tunnel | has | a | cross | section | of | 1.@@ | 20 | meters | height | and | 90 | cen@@ | time@@ | ters | width | . | </s>|
| waitk prob |  |  |  |  | 0.72 | 0.93 | 0.71 | 0.71 | 0.44 | 0.95 | 0.86 | 0.86 | 0.85 | 0.41 | 0.21 | 0.83 | 0.93 | 0.62 | 0.77 | 0.69 | 0.77 | 0.87 | 0.91|
| dec-waitk prob |  |  |  |  | 0.83 | 0.93 | 0.73 | 0.76 | 0.22 | 0.95 | 0.89 | 0.86 | 0.90 | 0.31 | 0.05 | 0.81 | 0.79 | 0.64 | 0.78 | 0.90 | 0.06 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.93 | -1.22 | -2.45 | -2.17 | -2.01 | -1.20 | -1.62 | -1.44 | -1.45 | -2.15 | -3.15 | -1.78 | -2.21 | -1.48 | -1.21 | -1.08 | -1.05 | -1.67 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.59 | -1.34 | -2.42 | -2.31 | -2.43 | -1.12 | -1.81 | -1.50 | -1.91 | -2.22 | -3.27 | -1.87 | -1.20 | -1.47 | -1.38 | -1.81 | -1.09 | -1.83 | -1.65|
| full sent prob |  |  |  |  | 0.70 | 0.86 | 0.67 | 0.83 | 0.20 | 0.93 | 0.85 | 0.83 | 0.88 | 0.29 | 0.12 | 0.83 | 0.59 | 0.48 | 0.83 | 0.89 | 0.16 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.54 | -1.82 | -2.37 | -1.83 | -3.05 | -1.24 | -1.87 | -1.42 | -1.61 | -2.17 | -3.34 | -1.76 | -2.29 | -1.81 | -1.11 | -1.12 | -1.59 | -1.67 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -2.52 | -1.29 | -2.39 | -2.35 | -2.39 | -1.11 | -1.78 | -1.48 | -1.89 | -2.21 | -3.27 | -1.89 | -1.05 | -1.42 | -1.41 | -1.80 | -1.14 | -1.83 | -1.64|
| dec-waitktgt |  |  |  |  | the | tunnel | has | a | cross-@@ | section | of | 1.@@ | 20 | metres | high | and | 90 | cen@@ | time@@ | ters | wide | . | </s>|
| full sent tgt |  |  |  |  | the | tunnel | has | a | cross-@@ | section | of | 1.@@ | 20 | metres | high | and | 90 | cen@@ | time@@ | ters | wide | . | </s>|
| ref | the | tunnel | has | a | cross-@@ | section | measuring | 1.@@ | 20 | metres | high | and | 90 | cen@@ | ti@@ | metres | across | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | er | wäre | damit | auch | geeignet | gewesen | , | um | die | illegale | einwanderung | richtung | usa | zu | fördern | .|
| waitk tgt |  |  |  |  | it | would | have | been | a | suitable | means | of | preventing | illegal | immigration | towards | the | united | states | . | </s>|
| waitk prob |  |  |  |  | 0.37 | 0.79 | 0.47 | 0.25 | 0.17 | 0.35 | 0.49 | 0.81 | 0.24 | 0.79 | 0.86 | 0.48 | 0.89 | 0.41 | 0.93 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.41 | 0.71 | 0.67 | 0.65 | 0.08 | 0.13 | 0.05 | 0.76 | 0.00 | 0.90 | 0.86 | 0.06 | 0.90 | 0.38 | 0.94 | 0.83 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 1 | 1 | 4 | 0 | 48 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.84 | -2.23 | -1.95 | -2.44 | -4.24 | -2.30 | -4.43 | -1.97 | -4.21 | -1.28 | -1.58 | -2.20 | -1.65 | -2.08 | -1.38 | -1.92 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.18 | -1.85 | -2.32 | -3.39 | -3.79 | -2.40 | -2.56 | -1.80 | -3.38 | -2.10 | -1.60 | -2.38 | -1.70 | -1.89 | -1.40 | -1.63 | -1.64|
| full sent prob |  |  |  |  | 0.46 | 0.79 | 0.41 | 0.31 | 0.18 | 0.06 | 0.11 | 0.82 | 0.00 | 0.90 | 0.85 | 0.07 | 0.90 | 0.38 | 0.93 | 0.83 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 43 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.62 | -1.92 | -2.35 | -3.63 | -4.21 | -2.57 | -2.92 | -1.84 | -1.94 | -1.34 | -1.58 | -2.32 | -1.66 | -2.07 | -1.43 | -1.89 | -1.62|
| full sent KL (full->waitk) |  |  |  |  | -3.20 | -1.89 | -2.25 | -3.33 | -3.79 | -2.37 | -2.61 | -1.83 | -3.39 | -2.09 | -1.60 | -2.38 | -1.70 | -1.90 | -1.39 | -1.63 | -1.64|
| dec-waitktgt |  |  |  |  | it | would | have | been | appropriate | good | way | of | immigration | illegal | immigration | to | the | united | states | . | </s>|
| full sent tgt |  |  |  |  | it | would | have | been | a | good | way | of | encouraging | illegal | immigration | to | the | united | states | . | </s>|
| ref | it | would | thus | be | suitable | to | assist | illegal | immigration | into | the | usa | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zwei | der | ver@@ | dä@@ | chtigen | wurden | in | zusammenhang | mit | dem | ko@@ | ka@@ | in-@@ | f@@ | und | fest@@ | genommen | .|
| waitk tgt |  |  |  |  | two | of | the | susp@@ | ects | were | arrested | in | connection | with | the | co@@ | ca@@ | ine | fund | . | </s>|
| waitk prob |  |  |  |  | 0.79 | 0.71 | 0.74 | 0.96 | 0.91 | 0.48 | 0.35 | 0.68 | 0.71 | 0.90 | 0.83 | 0.83 | 0.92 | 0.79 | 0.72 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.93 | 0.66 | 0.84 | 0.94 | 0.88 | 0.68 | 0.00 | 0.69 | 0.62 | 0.91 | 0.75 | 0.85 | 0.93 | 0.91 | 0.85 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 61 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.21 | -2.41 | -1.84 | -1.28 | -1.54 | -2.42 | -3.75 | -2.33 | -2.14 | -1.62 | -1.95 | -1.43 | -1.13 | -1.33 | -1.64 | -1.75 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.27 | -2.18 | -1.85 | -1.07 | -1.38 | -2.14 | -3.49 | -2.48 | -1.72 | -1.67 | -1.78 | -1.84 | -1.14 | -1.79 | -2.42 | -1.73 | -1.66|
| full sent prob |  |  |  |  | 0.89 | 0.78 | 0.81 | 0.94 | 0.85 | 0.67 | 0.90 | 0.70 | 0.83 | 0.91 | 0.87 | 0.84 | 0.87 | 0.91 | 0.86 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.57 | -1.95 | -1.92 | -1.27 | -1.71 | -1.82 | -0.90 | -2.37 | -1.38 | -1.57 | -1.76 | -1.46 | -1.42 | -1.33 | -1.56 | -1.67 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.25 | -2.25 | -1.83 | -1.07 | -1.36 | -2.17 | -3.75 | -2.48 | -1.84 | -1.68 | -1.85 | -1.84 | -1.09 | -1.79 | -2.43 | -1.74 | -1.66|
| dec-waitktgt |  |  |  |  | two | of | the | susp@@ | ects | were | involved | in | connection | with | the | co@@ | ca@@ | ine | fund | . | </s>|
| full sent tgt |  |  |  |  | two | of | the | susp@@ | ects | were | arrested | in | connection | with | the | co@@ | ca@@ | ine | fund | . | </s>|
| ref | two | of | the | susp@@ | ects | were | de@@ | tained | in | conjunction | with | the | co@@ | ca@@ | ine | find | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | der | dritte | , | ein | mexi@@ | kan@@ | er | , | wurde | wegen | des | besch@@ | lag@@ | nah@@ | m@@ | ten | mar@@ | ih@@ | u@@ | an@@ | as | gefasst | .|
| waitk tgt |  |  |  |  | the | third | , | a | mex@@ | ic@@ | an | , | was | arrested | for | se@@ | ized | mari@@ | ju@@ | ana | , | and | the | government | is | now | in | a | state | of | emergency | . | </s>|
| waitk prob |  |  |  |  | 0.77 | 0.93 | 0.56 | 0.63 | 0.97 | 0.98 | 0.85 | 0.89 | 0.87 | 0.35 | 0.52 | 0.56 | 0.45 | 0.68 | 0.96 | 0.96 | 0.22 | 0.31 | 0.13 | 0.05 | 0.13 | 0.11 | 0.12 | 0.14 | 0.32 | 0.75 | 0.11 | 0.76 | 0.91|
| dec-waitk prob |  |  |  |  | 0.74 | 0.94 | 0.67 | 0.76 | 0.96 | 0.96 | 0.93 | 0.91 | 0.71 | 0.02 | 0.17 | 0.10 | 0.52 | 0.24 | 0.62 | 0.08 | 0.00 | 0.00 | 0.14 | 0.01 | 0.04 | 0.15 | 0.18 | 0.11 | 0.11 | 0.70 | 0.12 | 0.67 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 1 | 0 | 1 | 0 | 2 | 2 | 1 | 1 | 11 | 4 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.95 | -1.31 | -2.32 | -1.97 | -1.09 | -1.24 | -1.28 | -1.58 | -2.54 | -4.33 | -3.95 | -4.20 | -1.88 | -2.62 | -1.71 | -1.73 | -1.63 | -1.32 | -5.20 | -5.75 | -4.64 | -5.00 | -5.10 | -3.49 | -2.23 | -2.52 | -4.88 | -2.50 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.36 | -1.38 | -3.45 | -2.16 | -1.03 | -1.00 | -1.99 | -1.67 | -1.51 | -3.09 | -2.05 | -1.85 | -1.80 | -2.44 | -0.86 | -0.38 | -3.16 | -3.47 | -4.38 | -5.63 | -4.34 | -5.05 | -5.20 | -4.13 | -3.72 | -2.34 | -4.86 | -2.17 | -1.67|
| full sent prob |  |  |  |  | 0.81 | 0.90 | 0.88 | 0.78 | 0.97 | 0.96 | 0.91 | 0.90 | 0.83 | 0.21 | 0.43 | 0.24 | 0.47 | 0.89 | 0.91 | 0.87 | 0.00 | 0.12 | 0.10 | 0.01 | 0.05 | 0.09 | 0.16 | 0.08 | 0.12 | 0.60 | 0.12 | 0.70 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 4 | 3 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.15 | -1.66 | -1.43 | -1.92 | -1.04 | -1.17 | -1.49 | -1.64 | -1.81 | -3.50 | -2.33 | -2.43 | -1.82 | -1.19 | -1.07 | -1.43 | -1.28 | -4.48 | -4.86 | -6.18 | -4.35 | -5.26 | -5.13 | -3.30 | -2.54 | -3.12 | -4.90 | -2.44 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.41 | -1.35 | -3.55 | -2.17 | -1.04 | -1.01 | -1.97 | -1.67 | -1.60 | -3.14 | -2.19 | -1.94 | -1.79 | -2.80 | -1.09 | -1.00 | -3.29 | -3.52 | -4.39 | -5.63 | -4.34 | -5.05 | -5.20 | -4.13 | -3.72 | -2.28 | -4.86 | -2.19 | -1.66|
| dec-waitktgt |  |  |  |  | the | third | , | a | mex@@ | ic@@ | an | , | was | conf@@ | </s> | the | ized | na@@ | ju@@ | an | </s> | </s> | </s> | first | of | now | in | charge | position | of | emergency | . | </s>|
| full sent tgt |  |  |  |  | the | third | , | a | mex@@ | ic@@ | an | , | was | arrested | for | the | ized | mari@@ | ju@@ | ana | . | and | was | first | of | now | in | charge | position | of | emergency | . | </s>|
| ref | the | third | , | a | mex@@ | ic@@ | an | , | was | de@@ | tained | due | to | the | se@@ | iz@@ | ure | of | the | mari@@ | ju@@ | ana | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | allen | drei@@ | en | dro@@ | ht | als | höchst@@ | strafe | lebens@@ | langer | frei@@ | heits@@ | ent@@ | zug | , | wie | beam@@ | te | sagten | .|
| waitk tgt |  |  |  |  | all | three | are | threatened | with | life@@ | -@@ | long | de@@ | priv@@ | ation | of | liber@@ | ty | , | as | officials | have | said | . | </s>|
| waitk prob |  |  |  |  | 0.20 | 0.88 | 0.31 | 0.37 | 0.83 | 0.26 | 0.60 | 0.98 | 0.42 | 0.62 | 0.95 | 0.35 | 0.32 | 0.96 | 0.65 | 0.92 | 0.60 | 0.70 | 0.83 | 0.92 | 0.91|
| dec-waitk prob |  |  |  |  | 0.66 | 0.81 | 0.41 | 0.48 | 0.39 | 0.00 | 0.58 | 0.99 | 0.01 | 0.89 | 0.96 | 0.36 | 0.26 | 0.92 | 0.12 | 0.91 | 0.66 | 0.76 | 0.83 | 0.92 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 6 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.82 | -2.05 | -3.25 | -2.62 | -2.70 | -2.58 | -1.74 | -0.90 | -2.65 | -1.01 | -1.13 | -2.50 | -1.89 | -1.27 | -2.14 | -1.53 | -1.96 | -1.59 | -1.80 | -1.56 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.22 | -1.47 | -2.84 | -3.17 | -1.53 | -3.10 | -2.04 | -0.97 | -2.40 | -2.59 | -1.25 | -2.47 | -2.64 | -1.09 | -1.80 | -1.48 | -2.21 | -1.88 | -1.80 | -1.51 | -1.65|
| full sent prob |  |  |  |  | 0.55 | 0.86 | 0.53 | 0.31 | 0.36 | 0.01 | 0.72 | 0.99 | 0.13 | 0.93 | 0.94 | 0.52 | 0.37 | 0.93 | 0.36 | 0.91 | 0.68 | 0.72 | 0.81 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.75 | -1.81 | -2.48 | -3.00 | -2.44 | -3.46 | -1.90 | -0.93 | -2.56 | -0.93 | -1.28 | -2.34 | -2.04 | -1.25 | -2.18 | -1.54 | -1.80 | -1.68 | -1.87 | -1.64 | -1.55|
| full sent KL (full->waitk) |  |  |  |  | -4.20 | -1.50 | -2.87 | -3.12 | -1.51 | -3.09 | -2.08 | -0.97 | -2.45 | -2.61 | -1.24 | -2.56 | -2.65 | -1.09 | -1.99 | -1.48 | -2.22 | -1.86 | -1.79 | -1.50 | -1.65|
| dec-waitktgt |  |  |  |  | all | three | are | threatened | with | a | -@@ | long | imprison@@ | priv@@ | ation | . | freedom | ty | . | as | officials | have | said | . | </s>|
| full sent tgt |  |  |  |  | all | three | are | threatened | with | a | -@@ | long | imprison@@ | priv@@ | ation | of | freedom | ty | as | as | officials | have | said | . | </s>|
| ref | all | three | face | a | maximum | penalty | of | life | imprison@@ | ment | , | according | to | the | authorities | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | seit | 2006 | seien | acht | derartige | tun@@ | nel | entdeckt | worden | , | hi@@ | e@@ | ß | es | auf | der | presse@@ | konferenz | in | san | die@@ | go | weiter | .|
| waitk tgt |  |  |  |  | since | 2006 | , | eight | such | tun@@ | nels | have | been | discovered | , | they | have | been | said | at | the | press | conference | in | san | di@@ | e@@ | go | . | </s>|
| waitk prob |  |  |  |  | 0.52 | 0.94 | 0.80 | 0.90 | 0.62 | 0.93 | 0.98 | 0.72 | 0.92 | 0.73 | 0.66 | 0.18 | 0.38 | 0.88 | 0.36 | 0.74 | 0.89 | 0.90 | 0.90 | 0.86 | 0.95 | 0.96 | 0.94 | 0.98 | 0.85 | 0.91|
| dec-waitk prob |  |  |  |  | 0.33 | 0.94 | 0.85 | 0.91 | 0.91 | 0.83 | 0.93 | 0.81 | 0.95 | 0.40 | 0.49 | 0.03 | 0.09 | 0.91 | 0.11 | 0.61 | 0.84 | 0.29 | 0.90 | 0.89 | 0.94 | 0.95 | 0.94 | 0.91 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.32 | -1.36 | -1.79 | -1.40 | -1.18 | -1.67 | -1.39 | -1.63 | -1.23 | -2.70 | -2.82 | -4.22 | -2.47 | -1.49 | -4.28 | -2.44 | -1.87 | -1.33 | -1.53 | -1.63 | -1.37 | -1.21 | -1.32 | -1.61 | -1.63 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.53 | -1.30 | -1.90 | -1.47 | -2.59 | -1.16 | -0.96 | -1.78 | -1.53 | -1.77 | -2.11 | -4.17 | -2.57 | -1.68 | -3.10 | -1.87 | -1.71 | -1.15 | -1.61 | -1.81 | -1.19 | -1.17 | -1.33 | -0.98 | -1.99 | -1.63|
| full sent prob |  |  |  |  | 0.25 | 0.91 | 0.68 | 0.87 | 0.82 | 0.91 | 0.95 | 0.58 | 0.94 | 0.47 | 0.70 | 0.07 | 0.14 | 0.54 | 0.03 | 0.27 | 0.85 | 0.18 | 0.93 | 0.90 | 0.94 | 0.95 | 0.94 | 0.91 | 0.89 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 6 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.82 | -1.59 | -2.08 | -1.59 | -1.68 | -1.40 | -1.30 | -2.13 | -1.34 | -2.63 | -2.08 | -3.06 | -2.91 | -2.28 | -4.43 | -2.45 | -1.83 | -1.39 | -1.31 | -1.63 | -1.33 | -1.20 | -1.34 | -1.62 | -1.75 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -2.53 | -1.28 | -1.80 | -1.44 | -2.55 | -1.22 | -0.97 | -1.66 | -1.52 | -1.81 | -2.23 | -4.20 | -2.52 | -1.41 | -3.07 | -1.70 | -1.72 | -1.08 | -1.64 | -1.81 | -1.19 | -1.17 | -1.32 | -0.98 | -1.98 | -1.62|
| dec-waitktgt |  |  |  |  | since | 2006 | , | eight | such | tun@@ | nels | have | been | discovered | , | and | were | been | called | at | the | san | conference | in | san | di@@ | e@@ | go | . | </s>|
| full sent tgt |  |  |  |  | eight | 2006 | , | eight | such | tun@@ | nels | have | been | discovered | , | it | were | been | continued | to | the | san | conference | in | san | di@@ | e@@ | go | . | </s>|
| ref | since | 2006 | , | eight | tun@@ | nels | of | this | type | have | been | discovered | , | the | press | conference | in | san | di@@ | e@@ | go | continued | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | es | sei | aber | das | erste | mal | , | dass | in | einem | solchen | tun@@ | n@@ | el@@ | bau | ko@@ | ka@@ | in | gefunden | wurde | .|
| waitk tgt |  |  |  |  | but | it | is | the | first | time | that | in | such | a | tunnel | building | co@@ | ca@@ | ine | has | been | found | . | </s>|
| waitk prob |  |  |  |  | 0.21 | 0.32 | 0.66 | 0.81 | 0.94 | 0.90 | 0.44 | 0.21 | 0.40 | 0.87 | 0.72 | 0.33 | 0.77 | 0.95 | 0.97 | 0.65 | 0.91 | 0.94 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.47 | 0.27 | 0.44 | 0.87 | 0.95 | 0.93 | 0.65 | 0.02 | 0.76 | 0.90 | 0.88 | 0.08 | 0.96 | 0.94 | 0.93 | 0.64 | 0.87 | 0.85 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.02 | -3.23 | -2.78 | -1.72 | -1.26 | -1.36 | -2.09 | -1.00 | -1.41 | -1.53 | -1.27 | -3.73 | -0.86 | -1.19 | -1.28 | -2.02 | -1.85 | -1.89 | -1.67 | -1.52|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.33 | -2.90 | -2.33 | -2.15 | -1.35 | -1.62 | -2.84 | -3.61 | -2.31 | -1.80 | -2.38 | -2.85 | -1.78 | -1.08 | -0.93 | -1.62 | -1.48 | -1.10 | -1.67 | -1.62|
| full sent prob |  |  |  |  | 0.14 | 0.40 | 0.40 | 0.86 | 0.93 | 0.91 | 0.33 | 0.01 | 0.49 | 0.86 | 0.87 | 0.24 | 0.79 | 0.94 | 0.93 | 0.56 | 0.88 | 0.85 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.26 | -2.56 | -2.30 | -1.79 | -1.44 | -1.59 | -1.69 | -1.28 | -2.09 | -1.72 | -1.45 | -2.33 | -1.27 | -1.19 | -1.22 | -2.09 | -1.83 | -1.92 | -1.71 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.32 | -2.96 | -2.31 | -2.14 | -1.33 | -1.60 | -2.71 | -3.51 | -2.25 | -1.77 | -2.37 | -2.95 | -1.67 | -1.08 | -0.93 | -1.60 | -1.48 | -1.10 | -1.66 | -1.62|
| dec-waitktgt |  |  |  |  | but | it | is | the | first | time | that | such | such | a | tunnel | construction | co@@ | ca@@ | ine | has | been | found | . | </s>|
| full sent tgt |  |  |  |  | it | it | is | the | first | time | co@@ | co@@ | such | a | tunnel | construction | co@@ | ca@@ | ine | has | been | found | . | </s>|
| ref | however | , | this | was | the | first | time | that | co@@ | ca@@ | ine | was | found | in | such | a | tunnel | construction | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | normalerweise | wird | ko@@ | ka@@ | in | in | klein@@ | eren | mengen | und | nicht | durch | tun@@ | nel | gesch@@ | mu@@ | g@@ | gelt | .|
| waitk tgt |  |  |  |  | co@@ | ca@@ | ine | is | usually | produced | in | smaller | quantities | and | not | through | tun@@ | nels | . | </s>|
| waitk prob |  |  |  |  | 0.27 | 0.94 | 0.99 | 0.75 | 0.43 | 0.35 | 0.84 | 0.61 | 0.60 | 0.34 | 0.81 | 0.32 | 0.56 | 0.95 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.00 | 0.98 | 0.76 | 0.18 | 0.40 | 0.06 | 0.57 | 0.69 | 0.83 | 0.22 | 0.88 | 0.03 | 0.46 | 0.82 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 22 | 0 | 0 | 1 | 0 | 5 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.19 | -0.95 | -1.69 | -2.57 | -2.19 | -3.35 | -2.31 | -1.81 | -1.20 | -2.52 | -1.68 | -1.39 | -2.34 | -1.97 | -1.61 | -1.50|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.50 | -1.13 | -0.69 | -1.67 | -1.86 | -3.55 | -1.75 | -1.82 | -1.75 | -2.37 | -1.82 | -3.41 | -2.21 | -1.10 | -1.76 | -1.67|
| full sent prob |  |  |  |  | 0.13 | 0.98 | 0.96 | 0.81 | 0.43 | 0.00 | 0.76 | 0.57 | 0.77 | 0.32 | 0.72 | 0.05 | 0.52 | 0.96 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.04 | -0.94 | -1.11 | -1.92 | -1.56 | -0.83 | -2.25 | -1.88 | -1.43 | -2.29 | -2.07 | -1.98 | -2.39 | -1.14 | -1.64 | -1.56|
| full sent KL (full->waitk) |  |  |  |  | -3.50 | -1.13 | -0.85 | -2.05 | -1.89 | -3.53 | -1.87 | -1.79 | -1.73 | -2.38 | -1.73 | -3.43 | -2.23 | -1.21 | -1.75 | -1.66|
| dec-waitktgt |  |  |  |  | normally | ca@@ | ine | normally | usually | smaller | in | smaller | quantities | , | not | s@@ | tun@@ | nels | . | </s>|
| full sent tgt |  |  |  |  | normally | ca@@ | ine | is | usually | s@@ | in | smaller | quantities | , | not | s@@ | tun@@ | nels | . | </s>|
| ref | normally | co@@ | ca@@ | ine | is | s@@ | mu@@ | gg@@ | led | in | smaller | quantities | and | not | through | tun@@ | nels | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | würden | alles | tun | , | um | in | die | usa | zu | gelangen | .|
| waitk tgt |  |  |  |  | they | would | do | everything | to | go | to | the | us | . | </s>|
| waitk prob |  |  |  |  | 0.67 | 0.81 | 0.91 | 0.58 | 0.39 | 0.22 | 0.77 | 0.86 | 0.43 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.43 | 0.83 | 0.88 | 0.79 | 0.37 | 0.27 | 0.77 | 0.89 | 0.44 | 0.89 | 0.91|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.97 | -1.75 | -1.73 | -1.55 | -1.85 | -2.95 | -1.97 | -1.67 | -2.40 | -1.81 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -1.97 | -1.82 | -1.37 | -2.22 | -2.39 | -3.60 | -2.20 | -1.85 | -1.85 | -1.63 | -1.65|
| full sent prob |  |  |  |  | 0.69 | 0.81 | 0.82 | 0.69 | 0.24 | 0.02 | 0.68 | 0.89 | 0.60 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.02 | -1.92 | -2.04 | -1.85 | -2.19 | -1.86 | -2.00 | -1.65 | -2.10 | -1.70 | -1.63|
| full sent KL (full->waitk) |  |  |  |  | -2.08 | -1.81 | -1.33 | -2.19 | -2.35 | -3.61 | -2.15 | -1.85 | -1.88 | -1.64 | -1.65|
| dec-waitktgt |  |  |  |  | they | would | do | everything | they | go | to | the | us | . | </s>|
| full sent tgt |  |  |  |  | they | would | do | everything | they | get | to | the | us | . | </s>|
| ref | they | will | do | anything | to | make | it | to | the | usa | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | zu | den | fest@@ | genommenen | wurden | keine | einzelheiten | bekannt | gegeben | , | zumindest | einer | sei | mexi@@ | kan@@ | er | , | hi@@ | e@@ | ß | es | .|
| waitk tgt |  |  |  |  | the | de@@ | tain@@ | e@@ | es | have | not | been | given | any | details | , | at | least | one | is | mex@@ | ic@@ | an | , | they | have | been | told | . | </s>|
| waitk prob |  |  |  |  | 0.15 | 0.55 | 0.78 | 0.98 | 0.96 | 0.36 | 0.76 | 0.78 | 0.44 | 0.38 | 0.89 | 0.62 | 0.68 | 0.92 | 0.79 | 0.34 | 0.74 | 0.94 | 0.61 | 0.72 | 0.38 | 0.37 | 0.77 | 0.28 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.07 | 0.70 | 0.80 | 0.85 | 0.95 | 0.55 | 0.77 | 0.70 | 0.18 | 0.36 | 0.83 | 0.74 | 0.77 | 0.90 | 0.52 | 0.26 | 0.95 | 0.95 | 0.43 | 0.39 | 0.44 | 0.08 | 0.70 | 0.30 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.63 | -1.58 | -1.48 | -1.93 | -1.26 | -1.94 | -1.79 | -1.95 | -3.60 | -2.43 | -1.79 | -2.16 | -2.03 | -1.49 | -3.12 | -3.16 | -0.97 | -1.28 | -2.22 | -1.87 | -2.49 | -2.45 | -2.17 | -3.58 | -1.62 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.35 | -2.57 | -1.46 | -0.90 | -1.17 | -2.59 | -1.97 | -1.88 | -3.07 | -2.10 | -1.31 | -2.49 | -2.50 | -1.37 | -1.84 | -3.05 | -1.61 | -1.33 | -2.11 | -2.01 | -3.24 | -2.64 | -2.01 | -3.61 | -1.74 | -1.64|
| full sent prob |  |  |  |  | 0.18 | 0.54 | 0.88 | 0.97 | 0.94 | 0.14 | 0.62 | 0.63 | 0.38 | 0.43 | 0.78 | 0.76 | 0.47 | 0.93 | 0.52 | 0.18 | 0.94 | 0.96 | 0.44 | 0.75 | 0.31 | 0.12 | 0.64 | 0.30 | 0.90 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.82 | -2.42 | -1.22 | -1.08 | -1.32 | -2.25 | -2.06 | -2.04 | -3.44 | -2.66 | -2.12 | -2.07 | -2.37 | -1.32 | -3.27 | -3.19 | -1.05 | -1.20 | -2.18 | -1.99 | -2.53 | -2.53 | -2.29 | -3.47 | -1.62 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -4.35 | -2.50 | -1.51 | -1.00 | -1.17 | -2.56 | -1.89 | -1.84 | -3.13 | -2.09 | -1.28 | -2.50 | -2.35 | -1.38 | -1.83 | -3.04 | -1.60 | -1.34 | -2.11 | -2.18 | -3.22 | -2.65 | -1.97 | -3.61 | -1.74 | -1.63|
| dec-waitktgt |  |  |  |  | to | de@@ | tain@@ | e@@ | es | have | not | been | informed | details | details | , | at | least | one | is | mex@@ | ic@@ | an | . | they | were | been | told | . | </s>|
| full sent tgt |  |  |  |  | no | de@@ | tain@@ | e@@ | es | were | not | been | given | any | details | , | at | least | one | of | mex@@ | ic@@ | an | , | it | were | been | told | . | </s>|
| ref | no | specific | details | were | given | regarding | those | de@@ | tained | , | but | it | is | reported | that | at | least | one | is | mex@@ | ic@@ | an | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sie | müssen | mit | haft@@ | stra@@ | fen | bis | zu | zehn | jahren | rechnen | .|
| waitk tgt |  |  |  |  | they | must | be | pun@@ | ished | with | prison | sent@@ | ences | of | up | to | ten | years | . | </s>|
| waitk prob |  |  |  |  | 0.63 | 0.68 | 0.68 | 0.08 | 0.96 | 0.26 | 0.46 | 0.92 | 0.96 | 0.42 | 0.91 | 0.91 | 0.74 | 0.91 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.25 | 0.64 | 0.44 | 0.02 | 0.90 | 0.18 | 0.49 | 0.67 | 0.94 | 0.51 | 0.91 | 0.92 | 0.75 | 0.94 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 9 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.47 | -2.02 | -2.97 | -3.76 | -1.43 | -2.62 | -1.76 | -2.03 | -1.27 | -2.64 | -1.35 | -1.55 | -1.52 | -1.36 | -1.75 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.54 | -1.97 | -2.21 | -4.04 | -1.08 | -3.01 | -2.62 | -1.00 | -1.10 | -2.30 | -1.34 | -1.65 | -1.65 | -1.60 | -1.76 | -1.66|
| full sent prob |  |  |  |  | 0.73 | 0.11 | 0.08 | 0.00 | 0.82 | 0.01 | 0.62 | 0.88 | 0.95 | 0.52 | 0.90 | 0.92 | 0.77 | 0.93 | 0.89 | 0.92|
| full sent rank |  |  |  |  | 0 | 3 | 1 | 26 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.24 | -3.14 | -1.73 | -3.35 | -1.86 | -1.33 | -2.11 | -1.31 | -1.21 | -2.61 | -1.38 | -1.56 | -1.48 | -1.40 | -1.76 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.76 | -1.69 | -2.01 | -4.03 | -1.02 | -3.00 | -2.66 | -1.16 | -1.11 | -2.30 | -1.33 | -1.65 | -1.65 | -1.59 | -1.76 | -1.66|
| dec-waitktgt |  |  |  |  | you | must | be | given | ished | for | prison | sent@@ | ences | of | up | to | ten | years | . | </s>|
| full sent tgt |  |  |  |  | they | have | expect | expected | ished | for | prison | sent@@ | ences | of | up | to | ten | years | . | </s>|
| ref | they | can | expect | prison | terms | of | up | to | ten | years | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | wieder@@ | kehr | der | ersten | ur@@ | kund@@ | lichen | erwähn@@ | ung | rück@@ | t | immer | näher | .|
| waitk tgt |  |  |  |  | the | first | docum@@ | entary | mention | of | the | town | is | getting | closer | . | </s>|
| waitk prob |  |  |  |  | 0.13 | 0.25 | 0.11 | 0.92 | 0.54 | 0.42 | 0.39 | 0.16 | 0.30 | 0.30 | 0.87 | 0.53 | 0.91|
| dec-waitk prob |  |  |  |  | 0.05 | 0.47 | 0.14 | 0.81 | 0.46 | 0.70 | 0.51 | 0.00 | 0.60 | 0.14 | 0.76 | 0.46 | 0.92|
| dec-waitk rank |  |  |  |  | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 100 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.87 | -2.13 | -4.39 | -1.77 | -3.07 | -2.21 | -2.94 | -2.81 | -2.56 | -3.50 | -2.32 | -2.04 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.50 | -5.08 | -5.39 | -1.13 | -2.74 | -3.51 | -4.21 | -4.65 | -4.17 | -3.49 | -1.41 | -2.23 | -1.65|
| full sent prob |  |  |  |  | 0.39 | 0.29 | 0.50 | 0.85 | 0.38 | 0.04 | 0.48 | 0.15 | 0.72 | 0.12 | 0.66 | 0.34 | 0.92|
| full sent rank |  |  |  |  | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.47 | -2.12 | -2.48 | -1.49 | -3.34 | -1.78 | -3.26 | -4.65 | -1.76 | -3.57 | -2.84 | -2.03 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -4.52 | -5.04 | -5.42 | -1.16 | -2.70 | -3.30 | -4.20 | -4.67 | -4.20 | -3.48 | -1.34 | -2.21 | -1.65|
| dec-waitktgt |  |  |  |  | re@@ | first | written | entary | mention | of | the | return | is | coming | closer | . | </s>|
| full sent tgt |  |  |  |  | the | return | docum@@ | entary | mention | is | the | city | is | coming | closer | and | </s>|
| ref | anniversary | of | the | first | docum@@ | ented | mention | of | the | town | , | are | drawing | closer | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | wenn | in | gut | acht | wochen | das | jahr | zu | ende | geht | , | steht | das | ju@@ | bi@@ | lä@@ | ums@@ | jahr | an | .|
| waitk tgt |  |  |  |  | if | , | in | just | over | eight | weeks | , | the | end | of | the | year | is | over | , | the | anniversary | year | will | be | upon | us | . | </s>|
| waitk prob |  |  |  |  | 0.57 | 0.30 | 0.79 | 0.27 | 0.89 | 0.82 | 0.94 | 0.60 | 0.65 | 0.39 | 0.86 | 0.82 | 0.85 | 0.57 | 0.56 | 0.38 | 0.41 | 0.78 | 0.73 | 0.50 | 0.39 | 0.53 | 0.95 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.37 | 0.02 | 0.80 | 0.14 | 0.17 | 0.86 | 0.95 | 0.88 | 0.74 | 0.00 | 0.88 | 0.82 | 0.88 | 0.46 | 0.20 | 0.04 | 0.27 | 0.36 | 0.86 | 0.42 | 0.16 | 0.13 | 0.97 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 6 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.54 | -2.82 | -2.04 | -3.94 | -1.46 | -1.45 | -1.26 | -1.51 | -2.18 | -2.41 | -1.78 | -1.85 | -1.80 | -3.24 | -3.08 | -1.87 | -2.92 | -2.50 | -1.45 | -2.47 | -2.23 | -3.61 | -1.00 | -1.68 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.65 | -3.18 | -1.92 | -3.14 | -0.69 | -1.59 | -1.35 | -2.04 | -2.32 | -2.54 | -1.78 | -1.81 | -1.98 | -2.44 | -2.58 | -2.86 | -2.64 | -1.53 | -2.45 | -2.22 | -3.28 | -2.20 | -1.13 | -1.66 | -1.63|
| full sent prob |  |  |  |  | 0.17 | 0.05 | 0.82 | 0.19 | 0.55 | 0.84 | 0.94 | 0.83 | 0.80 | 0.00 | 0.89 | 0.84 | 0.88 | 0.49 | 0.43 | 0.85 | 0.70 | 0.43 | 0.89 | 0.46 | 0.13 | 0.13 | 0.97 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 2 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.27 | -2.86 | -1.96 | -3.70 | -2.02 | -1.61 | -1.34 | -1.78 | -1.99 | -1.92 | -1.72 | -1.83 | -1.81 | -2.81 | -2.74 | -1.46 | -2.20 | -2.54 | -1.43 | -2.56 | -2.34 | -3.53 | -0.99 | -1.65 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -2.55 | -3.19 | -1.93 | -3.16 | -0.95 | -1.58 | -1.34 | -2.02 | -2.35 | -2.55 | -1.79 | -1.82 | -1.98 | -2.46 | -2.68 | -2.88 | -2.75 | -1.57 | -2.47 | -2.23 | -3.27 | -2.21 | -1.13 | -1.67 | -1.63|
| dec-waitktgt |  |  |  |  | if | in | in | just | eight | eight | weeks | , | the | year | of | the | year | is | appro@@ | . | then | ju@@ | year | will | come | . | us | . | </s>|
| full sent tgt |  |  |  |  | when | the | in | a | over | eight | weeks | , | the | year | of | the | year | is | over | , | the | anniversary | year | will | come | over | us | . | </s>|
| ref | when | the | year | comes | to | an | end | in | just | eight | weeks | , | the | anniversary | year | will | be | upon | us | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | gei@@ | sin@@ | gen | und | kir@@ | chen@@ | -@@ | haus@@ | en | wurden | 7@@ | 9@@ | 4 | erstmals | ur@@ | kund@@ | lich | zusammen | erwähnt | .|
| waitk tgt |  |  |  |  | go@@ | d@@ | d@@ | ess | and | church | houses | were | built | for | the | first | time | in | 7@@ | 94 | together | . | </s>|
| waitk prob |  |  |  |  | 0.10 | 0.42 | 0.22 | 0.59 | 0.83 | 0.39 | 0.39 | 0.83 | 0.05 | 0.46 | 0.89 | 0.92 | 0.92 | 0.50 | 0.44 | 0.94 | 0.47 | 0.69 | 0.91|
| dec-waitk prob |  |  |  |  | 0.00 | 0.04 | 0.12 | 0.44 | 0.86 | 0.60 | 0.06 | 0.70 | 0.02 | 0.24 | 0.90 | 0.96 | 0.96 | 0.87 | 0.58 | 0.95 | 0.00 | 0.87 | 0.92|
| dec-waitk rank |  |  |  |  | 31 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 19 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -4.07 | -2.52 | -5.09 | -3.20 | -1.80 | -2.40 | -3.55 | -2.59 | -3.71 | -1.82 | -1.59 | -1.12 | -1.12 | -1.30 | -3.04 | -1.19 | -1.31 | -1.59 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -5.00 | -2.60 | -4.24 | -1.47 | -2.05 | -2.42 | -3.14 | -1.68 | -4.75 | -2.58 | -1.73 | -1.50 | -1.51 | -2.54 | -3.08 | -1.23 | -2.35 | -2.45 | -1.62|
| full sent prob |  |  |  |  | 0.00 | 0.01 | 0.01 | 0.16 | 0.83 | 0.38 | 0.35 | 0.82 | 0.00 | 0.17 | 0.75 | 0.94 | 0.87 | 0.61 | 0.28 | 0.96 | 0.05 | 0.49 | 0.91|
| full sent rank |  |  |  |  | 128 | 2 | 15 | 1 | 0 | 0 | 0 | 0 | 77 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.45 | -0.95 | -4.49 | -3.64 | -1.97 | -3.09 | -3.46 | -1.82 | -0.80 | -3.00 | -2.32 | -1.30 | -1.74 | -2.37 | -4.18 | -1.13 | -2.74 | -2.35 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -5.01 | -2.58 | -4.21 | -1.35 | -2.03 | -2.38 | -3.24 | -1.77 | -4.75 | -2.46 | -1.62 | -1.48 | -1.44 | -2.45 | -2.98 | -1.23 | -2.30 | -2.24 | -1.61|
| dec-waitktgt |  |  |  |  | spir@@ | spe@@ | d@@ | ess | and | church | sha@@ | were | 7@@ | in | the | first | time | in | 7@@ | 94 | . | . | </s>|
| full sent tgt |  |  |  |  | ge@@ | is@@ | ingen | esses | and | church | houses | were | first | together | the | first | time | in | 7@@ | 94 | . | . | </s>|
| ref | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | were | first | docum@@ | ented | together | in | the | year | 7@@ | 94 | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | kirchen | wurde | eine | ur@@ | kunde | ge@@ | fertigt | , | in | der | beide | orte | erwähnt | sind | .|
| waitk tgt |  |  |  |  | in | churches | a | certificate | was | produced | , | in | which | both | places | are | mentioned | . | </s>|
| waitk prob |  |  |  |  | 0.19 | 0.77 | 0.38 | 0.43 | 0.62 | 0.21 | 0.15 | 0.31 | 0.92 | 0.85 | 0.56 | 0.76 | 0.87 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.82 | 0.78 | 0.17 | 0.49 | 0.62 | 0.19 | 0.15 | 0.40 | 0.87 | 0.64 | 0.60 | 0.73 | 0.91 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.44 | -2.15 | -3.88 | -1.72 | -1.96 | -3.77 | -4.64 | -3.50 | -1.71 | -2.66 | -2.65 | -1.77 | -1.37 | -1.72 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.79 | -2.07 | -2.32 | -2.37 | -2.19 | -4.03 | -3.48 | -3.85 | -1.45 | -1.52 | -2.74 | -1.93 | -1.60 | -1.63 | -1.63|
| full sent prob |  |  |  |  | 0.27 | 0.31 | 0.37 | 0.11 | 0.54 | 0.37 | 0.23 | 0.20 | 0.95 | 0.74 | 0.61 | 0.67 | 0.92 | 0.91 | 0.91|
| full sent rank |  |  |  |  | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.58 | -3.89 | -2.37 | -1.07 | -2.09 | -3.21 | -3.14 | -3.17 | -1.22 | -2.22 | -2.48 | -1.91 | -1.32 | -1.65 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.75 | -1.78 | -2.44 | -2.36 | -2.16 | -4.05 | -3.53 | -3.81 | -1.51 | -1.59 | -2.74 | -1.89 | -1.61 | -1.64 | -1.63|
| dec-waitktgt |  |  |  |  | in | churches | a | certificate | was | made | </s> | in | which | both | places | are | mentioned | . | </s>|
| full sent tgt |  |  |  |  | a | churches | , | document | was | produced | , | in | which | both | places | are | mentioned | . | </s>|
| ref | a | de@@ | ed | was | drafted | in | kir@@ | chen | , | in | which | both | towns | are | mentioned | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | im | rahmen | des | ju@@ | bi@@ | lä@@ | ums | sind | et@@ | liche | veranstaltungen | sowohl | in | gei@@ | sin@@ | gen | , | als | auch | in | kir@@ | chen@@ | -@@ | haus@@ | en | geplant | .|
| waitk tgt |  |  |  |  | during | the | anniversary | , | several | important | events | have | been | organized | in | the | area | of | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | . | </s>|
| waitk prob |  |  |  |  | 0.18 | 0.70 | 0.47 | 0.34 | 0.38 | 0.04 | 0.87 | 0.23 | 0.46 | 0.24 | 0.29 | 0.26 | 0.06 | 0.83 | 0.35 | 0.95 | 0.88 | 0.39 | 0.81 | 0.80 | 0.98 | 0.92 | 0.85 | 0.87 | 0.91|
| dec-waitk prob |  |  |  |  | 0.02 | 0.69 | 0.21 | 0.02 | 0.00 | 0.00 | 0.76 | 0.08 | 0.40 | 0.01 | 0.13 | 0.04 | 0.06 | 0.74 | 0.30 | 0.95 | 0.34 | 0.30 | 0.31 | 0.67 | 0.99 | 0.63 | 0.93 | 0.85 | 0.92|
| dec-waitk rank |  |  |  |  | 7 | 0 | 1 | 3 | 130 | 125 | 0 | 1 | 0 | 7 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.83 | -2.33 | -1.87 | -3.23 | -3.09 | -4.94 | -2.32 | -2.83 | -2.44 | -1.81 | -2.86 | -2.65 | -5.07 | -2.39 | -3.40 | -1.12 | -3.80 | -2.46 | -3.14 | -1.65 | -0.91 | -1.92 | -1.35 | -1.87 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.99 | -2.14 | -3.11 | -3.27 | -2.96 | -5.56 | -1.65 | -3.00 | -2.22 | -2.69 | -2.91 | -3.80 | -5.16 | -1.94 | -3.95 | -1.18 | -0.95 | -2.13 | -1.49 | -1.25 | -0.99 | -1.16 | -1.95 | -1.74 | -1.64|
| full sent prob |  |  |  |  | 0.13 | 0.78 | 0.31 | 0.33 | 0.19 | 0.00 | 0.73 | 0.04 | 0.82 | 0.03 | 0.49 | 0.03 | 0.14 | 0.78 | 0.65 | 0.98 | 0.42 | 0.36 | 0.60 | 0.77 | 0.98 | 0.66 | 0.92 | 0.85 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 1 | 52 | 0 | 2 | 0 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.88 | -1.85 | -3.29 | -3.20 | -2.92 | -3.08 | -2.48 | -2.09 | -1.79 | -2.28 | -2.19 | -2.66 | -4.49 | -2.19 | -2.09 | -0.97 | -3.41 | -2.28 | -1.99 | -1.54 | -0.96 | -1.98 | -1.42 | -1.87 | -1.57|
| full sent KL (full->waitk) |  |  |  |  | -3.99 | -2.19 | -3.10 | -3.36 | -3.04 | -5.58 | -1.63 | -3.02 | -2.30 | -2.58 | -3.03 | -3.84 | -5.16 | -1.97 | -4.05 | -1.19 | -1.00 | -2.18 | -1.68 | -1.30 | -0.99 | -1.18 | -1.95 | -1.74 | -1.63|
| dec-waitktgt |  |  |  |  | in | the | ju@@ | are | et@@ | </s> | events | are | been | held | . | g@@ | fields | of | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | . | </s>|
| full sent tgt |  |  |  |  | the | the | anniversary | , | a | events | events | are | been | planned | in | ge@@ | area | of | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | . | </s>|
| ref | as | part | of | the | anniversary | celebra@@ | tions | , | a | number | of | events | are | planned | both | in | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | am | freitag | mit | einem | fe@@ | sta@@ | kt | , | am | samstag | und | sonntag | mit | einem | fest | rund | um | die | kir@@ | cht@@ | al@@ | halle | .|
| waitk tgt |  |  |  |  | on | friday | with | a | cere@@ | mony | , | on | saturday | and | sunday | with | a | party | around | the | church | hall | . | </s>|
| waitk prob |  |  |  |  | 0.39 | 0.89 | 0.28 | 0.86 | 0.30 | 0.86 | 0.74 | 0.71 | 0.88 | 0.89 | 0.90 | 0.82 | 0.87 | 0.39 | 0.67 | 0.89 | 0.43 | 0.51 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.29 | 0.95 | 0.53 | 0.86 | 0.23 | 0.03 | 0.72 | 0.13 | 0.83 | 0.91 | 0.93 | 0.71 | 0.74 | 0.25 | 0.37 | 0.87 | 0.50 | 0.48 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.86 | -1.13 | -2.18 | -1.60 | -2.94 | -6.48 | -2.25 | -1.18 | -1.56 | -1.50 | -1.26 | -2.10 | -2.50 | -3.36 | -3.66 | -1.81 | -3.29 | -2.52 | -1.68 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.84 | -1.47 | -3.58 | -1.77 | -2.76 | -0.88 | -2.12 | -1.51 | -1.35 | -1.71 | -1.45 | -1.86 | -1.68 | -3.35 | -2.37 | -1.69 | -1.85 | -3.22 | -1.68 | -1.68|
| full sent prob |  |  |  |  | 0.37 | 0.86 | 0.56 | 0.81 | 0.50 | 0.82 | 0.68 | 0.30 | 0.83 | 0.90 | 0.89 | 0.77 | 0.87 | 0.21 | 0.59 | 0.90 | 0.60 | 0.93 | 0.90 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.23 | -1.58 | -2.23 | -1.94 | -2.22 | -2.04 | -2.11 | -1.61 | -1.59 | -1.60 | -1.48 | -1.82 | -1.77 | -2.97 | -2.71 | -1.66 | -2.76 | -0.95 | -1.68 | -1.61|
| full sent KL (full->waitk) |  |  |  |  | -3.86 | -1.41 | -3.57 | -1.73 | -2.82 | -1.44 | -2.10 | -1.59 | -1.35 | -1.70 | -1.42 | -1.90 | -1.77 | -3.35 | -2.49 | -1.72 | -1.89 | -3.42 | -1.68 | -1.67|
| dec-waitktgt |  |  |  |  | friday | friday | with | a | fe@@ | act | , | saturday | saturday | and | sunday | with | a | party | around | the | church | hall | . | </s>|
| full sent tgt |  |  |  |  | on | friday | with | a | cere@@ | mony | , | saturday | saturday | and | sunday | with | a | fe@@ | around | the | church | hall | . | </s>|
| ref | on | the | friday | there | will | be | a | cere@@ | mony | , | and | on | the | saturday | and | sunday | a | party | will | be | held | at | the | kir@@ | ch@@ | tal@@ | hal@@ | le | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | an | diesem | fest@@ | wochenende | ist | außerdem | noch | das | kir@@ | chen@@ | -@@ | haus@@ | ener | kir@@ | chen@@ | fest | .|
| waitk tgt |  |  |  |  | on | this | weekend | of | the | festival | , | the | church | house | of | the | sa@@ | ints | is | also | open | . | </s>|
| waitk prob |  |  |  |  | 0.16 | 0.59 | 0.54 | 0.26 | 0.44 | 0.41 | 0.21 | 0.50 | 0.34 | 0.41 | 0.60 | 0.30 | 0.21 | 0.76 | 0.25 | 0.16 | 0.14 | 0.75 | 0.91|
| dec-waitk prob |  |  |  |  | 0.03 | 0.70 | 0.74 | 0.63 | 0.12 | 0.04 | 0.08 | 0.28 | 0.48 | 0.27 | 0.75 | 0.09 | 0.00 | 0.88 | 0.23 | 0.55 | 0.08 | 0.65 | 0.92|
| dec-waitk rank |  |  |  |  | 2 | 0 | 0 | 0 | 1 | 4 | 1 | 0 | 0 | 1 | 0 | 2 | 13 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.06 | -2.18 | -1.86 | -2.29 | -3.52 | -3.87 | -1.86 | -3.13 | -3.29 | -3.45 | -2.06 | -3.40 | -3.99 | -1.22 | -4.00 | -3.32 | -4.42 | -2.06 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.10 | -2.46 | -2.87 | -3.43 | -3.03 | -3.16 | -3.06 | -2.80 | -3.16 | -3.49 | -2.94 | -3.24 | -4.65 | -1.72 | -2.85 | -4.40 | -4.07 | -2.08 | -1.65|
| full sent prob |  |  |  |  | 0.05 | 0.64 | 0.40 | 0.30 | 0.36 | 0.16 | 0.15 | 0.40 | 0.71 | 0.31 | 0.56 | 0.47 | 0.00 | 0.75 | 0.36 | 0.31 | 0.09 | 0.40 | 0.92|
| full sent rank |  |  |  |  | 2 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.57 | -2.43 | -3.11 | -2.85 | -2.87 | -3.20 | -3.24 | -3.03 | -2.16 | -3.57 | -2.60 | -3.08 | -4.65 | -1.71 | -3.63 | -4.19 | -4.39 | -2.14 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -4.08 | -2.43 | -2.72 | -3.38 | -3.12 | -3.21 | -3.05 | -2.84 | -3.22 | -3.50 | -2.85 | -3.34 | -4.64 | -1.64 | -2.89 | -4.37 | -4.08 | -1.94 | -1.64|
| dec-waitktgt |  |  |  |  | this | this | weekend | of | christmas | fe@@ | is | the | church | and | of | church | church | ints | is | also | a | . | </s>|
| full sent tgt |  |  |  |  | this | this | weekend | of | the | fe@@ | of | the | church | house | of | the | church | ints | is | also | a | . | </s>|
| ref | the | kir@@ | ch@@ | en-@@ | haus@@ | en | kir@@ | chen@@ | fest | festival | will | also | be | held | on | this | celebr@@ | atory | weekend | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | an@@ | lässlich | des | gei@@ | sin@@ | ger | stadt@@ | ju@@ | bi@@ | lä@@ | ums | wird | auch | noch | eine | neue | ch@@ | roni@@ | k | heraus@@ | gebracht | .|
| waitk tgt |  |  |  |  | on | the | occasion | of | the | ge@@ | is@@ | inger | city | anniversary | , | a | new | chron@@ | ic@@ | le | will | be | released | . | </s>|
| waitk prob |  |  |  |  | 0.23 | 0.80 | 0.91 | 0.91 | 0.80 | 0.92 | 0.90 | 0.94 | 0.52 | 0.75 | 0.27 | 0.44 | 0.89 | 0.89 | 0.93 | 0.68 | 0.41 | 0.62 | 0.54 | 0.73 | 0.91|
| dec-waitk prob |  |  |  |  | 0.35 | 0.88 | 0.99 | 0.93 | 0.70 | 0.62 | 0.97 | 0.86 | 0.70 | 0.55 | 0.62 | 0.29 | 0.88 | 0.96 | 0.90 | 0.89 | 0.30 | 0.51 | 0.75 | 0.69 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.40 | -1.65 | -0.86 | -1.47 | -2.20 | -2.72 | -1.02 | -1.66 | -2.33 | -2.34 | -2.65 | -2.89 | -1.77 | -0.98 | -1.58 | -1.14 | -2.07 | -1.90 | -1.65 | -2.19 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.00 | -2.29 | -1.51 | -1.62 | -1.91 | -1.12 | -1.43 | -1.05 | -1.93 | -2.02 | -2.67 | -2.44 | -1.69 | -1.57 | -1.25 | -2.33 | -2.43 | -1.92 | -2.84 | -2.27 | -1.64|
| full sent prob |  |  |  |  | 0.11 | 0.82 | 0.96 | 0.92 | 0.83 | 0.77 | 0.95 | 0.85 | 0.59 | 0.39 | 0.28 | 0.49 | 0.93 | 0.92 | 0.92 | 0.87 | 0.29 | 0.57 | 0.72 | 0.62 | 0.91|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.76 | -2.04 | -1.03 | -1.52 | -1.93 | -2.16 | -1.13 | -1.70 | -2.91 | -2.87 | -2.75 | -2.56 | -1.36 | -1.24 | -1.38 | -1.39 | -2.13 | -1.92 | -1.86 | -2.42 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.96 | -2.25 | -1.49 | -1.62 | -1.99 | -1.22 | -1.41 | -1.04 | -1.88 | -1.92 | -2.65 | -2.51 | -1.73 | -1.54 | -1.26 | -2.31 | -2.43 | -1.94 | -2.83 | -2.23 | -1.63|
| dec-waitktgt |  |  |  |  | on | the | occasion | of | the | ge@@ | is@@ | inger | city | anniversary | , | a | new | chron@@ | ic@@ | le | is | be | released | . | </s>|
| full sent tgt |  |  |  |  | a | the | occasion | of | the | ge@@ | is@@ | inger | city | anniversary | , | a | new | chron@@ | ic@@ | le | is | be | released | . | </s>|
| ref | on | the | occasion | of | the | ge@@ | is@@ | ingen | town | anniversary | , | a | new | chron@@ | ic@@ | le | will | also | be | published | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | neue | ch@@ | roni@@ | k | soll | dann | am | 21. | oder | 22. | november | in | der | neuen | fest@@ | halle | in | gei@@ | sin@@ | gen | vorgestellt | werden | .|
| waitk tgt |  |  |  |  | the | new | chron@@ | ic@@ | le | will | be | released | on | 21 | or | 22 | november | in | the | new | fe@@ | st@@ | hal@@ | le | in | ge@@ | is@@ | ingen | . | </s>|
| waitk prob |  |  |  |  | 0.57 | 0.81 | 0.87 | 0.71 | 0.67 | 0.47 | 0.59 | 0.27 | 0.41 | 0.52 | 0.69 | 0.93 | 0.94 | 0.55 | 0.78 | 0.72 | 0.30 | 0.76 | 0.90 | 0.96 | 0.87 | 0.97 | 0.97 | 0.89 | 0.81 | 0.91|
| dec-waitk prob |  |  |  |  | 0.77 | 0.79 | 0.95 | 0.83 | 0.90 | 0.16 | 0.35 | 0.03 | 0.59 | 0.26 | 0.72 | 0.95 | 0.95 | 0.30 | 0.60 | 0.50 | 0.23 | 0.90 | 0.96 | 0.99 | 0.86 | 0.94 | 0.99 | 0.63 | 0.86 | 0.91|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.92 | -2.36 | -1.11 | -1.89 | -1.24 | -2.83 | -2.73 | -2.41 | -2.34 | -1.78 | -2.01 | -1.15 | -1.21 | -3.20 | -2.60 | -2.15 | -4.14 | -1.32 | -1.11 | -0.85 | -1.75 | -1.27 | -0.90 | -2.71 | -1.76 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.41 | -2.16 | -1.76 | -2.72 | -2.04 | -2.17 | -2.45 | -3.45 | -2.42 | -1.78 | -2.25 | -1.35 | -1.34 | -2.13 | -2.09 | -2.03 | -3.53 | -2.02 | -1.51 | -1.18 | -1.76 | -0.99 | -1.06 | -1.04 | -2.10 | -1.64|
| full sent prob |  |  |  |  | 0.62 | 0.86 | 0.94 | 0.83 | 0.79 | 0.45 | 0.73 | 0.01 | 0.62 | 0.44 | 0.63 | 0.95 | 0.94 | 0.33 | 0.83 | 0.59 | 0.30 | 0.94 | 0.98 | 0.99 | 0.87 | 0.94 | 0.99 | 0.58 | 0.84 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.91 | -1.82 | -1.16 | -1.90 | -1.70 | -2.32 | -1.87 | -2.29 | -2.25 | -2.08 | -2.33 | -1.16 | -1.28 | -2.29 | -1.91 | -2.02 | -3.32 | -1.11 | -0.95 | -0.85 | -1.75 | -1.23 | -0.91 | -2.85 | -1.88 | -1.65|
| full sent KL (full->waitk) |  |  |  |  | -3.34 | -2.21 | -1.75 | -2.72 | -1.98 | -2.27 | -2.62 | -3.43 | -2.43 | -1.79 | -2.20 | -1.35 | -1.34 | -2.20 | -2.24 | -2.08 | -3.56 | -2.05 | -1.53 | -1.18 | -1.76 | -1.00 | -1.06 | -1.01 | -2.08 | -1.64|
| dec-waitktgt |  |  |  |  | the | new | chron@@ | ic@@ | le | should | be | on | on | november | or | 22 | november | in | the | new | fe@@ | st@@ | hal@@ | le | in | ge@@ | is@@ | ingen | . | </s>|
| full sent tgt |  |  |  |  | the | new | chron@@ | ic@@ | le | will | be | presented | on | 21 | or | 22 | november | at | the | new | fe@@ | st@@ | hal@@ | le | in | ge@@ | is@@ | ingen | . | </s>|
| ref | the | new | chron@@ | ic@@ | le | is | to | be | presented | on | 21 | or | 22 | november | in | the | new | festival | hall | in | ge@@ | is@@ | ingen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | 20@@ | 14 | ist | aber | auch | sonst | ein | jahr | mit | vielen | ju@@ | bi@@ | lä@@ | en | .|
| waitk tgt |  |  |  |  | in | 20@@ | 14 | , | however | , | there | will | be | many | anni@@ | vers@@ | aries | . | </s>|
| waitk prob |  |  |  |  | 0.17 | 0.82 | 0.91 | 0.73 | 0.42 | 0.92 | 0.23 | 0.42 | 0.48 | 0.58 | 0.31 | 0.96 | 0.98 | 0.57 | 0.91|
| dec-waitk prob |  |  |  |  | 0.01 | 0.75 | 0.94 | 0.80 | 0.51 | 0.92 | 0.12 | 0.06 | 0.49 | 0.26 | 0.11 | 0.89 | 0.96 | 0.56 | 0.92|
| dec-waitk rank |  |  |  |  | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.44 | -2.05 | -1.26 | -2.00 | -2.31 | -1.56 | -3.79 | -2.50 | -2.16 | -3.33 | -3.94 | -1.69 | -1.10 | -2.71 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.60 | -1.95 | -1.59 | -2.30 | -3.18 | -1.56 | -3.43 | -2.65 | -2.61 | -2.13 | -3.72 | -1.05 | -1.00 | -2.96 | -1.66|
| full sent prob |  |  |  |  | 0.06 | 0.49 | 0.94 | 0.56 | 0.47 | 0.91 | 0.11 | 0.22 | 0.65 | 0.34 | 0.13 | 0.91 | 0.96 | 0.48 | 0.91|
| full sent rank |  |  |  |  | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.54 | -3.24 | -1.26 | -2.88 | -2.99 | -1.65 | -3.74 | -2.60 | -2.06 | -3.06 | -3.94 | -1.55 | -1.13 | -2.78 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.58 | -1.78 | -1.59 | -2.16 | -3.16 | -1.55 | -3.43 | -2.66 | -2.65 | -2.17 | -3.73 | -1.06 | -1.00 | -2.93 | -1.66|
| dec-waitktgt |  |  |  |  | 20@@ | 20@@ | 14 | , | however | , | it | is | be | many | ju@@ | vers@@ | aries | . | </s>|
| full sent tgt |  |  |  |  | 20@@ | 20@@ | 14 | , | however | , | it | is | be | many | ju@@ | vers@@ | aries | . | </s>|
| ref | however | , | 20@@ | 14 | is | also | a | year | of | many | anni@@ | vers@@ | aries | in | other | respects | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | ur@@ | kunde | wurde | in | kirchen | ( | haus@@ | en | ) | ge@@ | fertigt | , | das | damals | gericht@@ | splatz | war | .|
| waitk tgt |  |  |  |  | the | document | was | written | in | churches | ( | haus@@ | en | ) | , | which | was | then | court | place | . | </s>|
| waitk prob |  |  |  |  | 0.59 | 0.38 | 0.76 | 0.20 | 0.82 | 0.79 | 0.79 | 0.49 | 0.90 | 0.88 | 0.48 | 0.65 | 0.48 | 0.30 | 0.33 | 0.46 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.81 | 0.54 | 0.81 | 0.10 | 0.86 | 0.72 | 0.88 | 0.80 | 0.90 | 0.91 | 0.19 | 0.52 | 0.50 | 0.37 | 0.11 | 0.07 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.97 | -2.73 | -1.86 | -3.60 | -1.73 | -2.54 | -1.74 | -1.59 | -1.65 | -1.57 | -2.49 | -2.66 | -2.80 | -2.91 | -2.03 | -3.04 | -1.77 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.06 | -3.91 | -2.02 | -3.44 | -2.01 | -2.01 | -2.04 | -2.62 | -1.56 | -1.85 | -2.30 | -2.43 | -2.36 | -3.26 | -2.68 | -2.10 | -1.70 | -1.64|
| full sent prob |  |  |  |  | 0.59 | 0.46 | 0.87 | 0.06 | 0.83 | 0.67 | 0.80 | 0.77 | 0.92 | 0.89 | 0.58 | 0.68 | 0.68 | 0.35 | 0.12 | 0.09 | 0.88 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.94 | -3.07 | -1.61 | -3.81 | -1.92 | -2.45 | -1.97 | -1.39 | -1.43 | -1.74 | -2.37 | -2.36 | -2.16 | -2.81 | -2.13 | -3.13 | -1.81 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.96 | -3.89 | -2.05 | -3.41 | -1.99 | -1.99 | -1.99 | -2.61 | -1.58 | -1.84 | -2.48 | -2.51 | -2.42 | -3.26 | -2.68 | -2.07 | -1.69 | -1.63|
| dec-waitktgt |  |  |  |  | the | document | was | given | in | churches | ( | haus@@ | en | ) | . | which | was | then | a | . | . | </s>|
| full sent tgt |  |  |  |  | the | document | was | produced | in | churches | ( | haus@@ | en | ) | , | which | was | then | a | court | . | </s>|
| ref | the | de@@ | ed | was | drawn | up | in | kir@@ | chen | ( | haus@@ | en | ) | , | which | at | the | time | was | the | location | of | the | cour@@ | thouse | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | soll | der | bahn@@ | übergang | &quot; | am | hir@@ | schen | &quot; | auf@@ | w@@ | än@@ | dig | um@@ | gebaut | werden | , | um | die | verkehr@@ | ssicherheit | zu | erhöhen | ?|
| waitk tgt |  |  |  |  | if | the | railway | crossing | is | to | be | lab@@ | ori@@ | ously | converted | , | the | railway | pass | &quot; | am | h@@ | ir@@ | sch@@ | en | &quot; | will | be | extended | to | increase | road | safety | ? | </s>|
| waitk prob |  |  |  |  | 0.24 | 0.62 | 0.37 | 0.23 | 0.59 | 0.74 | 0.78 | 0.39 | 0.78 | 0.62 | 0.18 | 0.20 | 0.19 | 0.10 | 0.19 | 0.20 | 0.96 | 0.83 | 0.94 | 0.88 | 0.98 | 0.91 | 0.31 | 0.53 | 0.14 | 0.30 | 0.37 | 0.53 | 0.92 | 0.48 | 0.91|
| dec-waitk prob |  |  |  |  | 0.01 | 0.37 | 0.01 | 0.07 | 0.53 | 0.76 | 0.41 | 0.00 | 0.83 | 0.36 | 0.06 | 0.07 | 0.06 | 0.00 | 0.02 | 0.31 | 0.34 | 0.90 | 0.80 | 0.95 | 0.98 | 0.88 | 0.27 | 0.58 | 0.02 | 0.26 | 0.30 | 0.64 | 0.93 | 0.25 | 0.92|
| dec-waitk rank |  |  |  |  | 10 | 0 | 9 | 2 | 0 | 0 | 0 | 28 | 0 | 1 | 3 | 5 | 4 | 50 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 0 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -4.44 | -3.49 | -4.41 | -3.78 | -2.98 | -2.32 | -2.96 | -3.86 | -1.29 | -2.02 | -3.74 | -4.48 | -3.37 | -4.83 | -4.12 | -3.51 | -3.22 | -1.47 | -1.52 | -0.93 | -0.98 | -1.74 | -3.54 | -2.98 | -4.80 | -3.14 | -3.30 | -1.91 | -1.29 | -2.33 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.43 | -2.24 | -3.23 | -3.52 | -2.50 | -2.35 | -1.79 | -3.32 | -1.59 | -1.44 | -3.37 | -3.19 | -4.07 | -5.20 | -4.03 | -3.83 | -0.60 | -1.97 | -1.18 | -1.19 | -0.99 | -1.54 | -3.08 | -3.06 | -4.59 | -3.00 | -3.47 | -2.12 | -1.32 | -2.33 | -1.62|
| full sent prob |  |  |  |  | 0.01 | 0.24 | 0.04 | 0.10 | 0.21 | 0.71 | 0.57 | 0.00 | 0.76 | 0.88 | 0.08 | 0.08 | 0.07 | 0.00 | 0.00 | 0.30 | 0.41 | 0.93 | 0.90 | 0.96 | 0.97 | 0.89 | 0.32 | 0.62 | 0.03 | 0.55 | 0.35 | 0.63 | 0.94 | 0.53 | 0.91|
| full sent rank |  |  |  |  | 10 | 0 | 5 | 1 | 1 | 0 | 0 | 93 | 0 | 0 | 3 | 2 | 2 | 19 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.61 | -3.38 | -4.20 | -4.15 | -2.81 | -2.47 | -2.78 | -4.29 | -1.49 | -1.15 | -3.39 | -2.72 | -4.17 | -5.02 | -3.94 | -3.50 | -3.11 | -1.25 | -1.24 | -0.88 | -0.99 | -1.69 | -3.07 | -2.56 | -4.04 | -2.26 | -3.11 | -1.84 | -1.25 | -2.28 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.47 | -2.18 | -3.26 | -3.52 | -2.38 | -2.32 | -1.89 | -3.31 | -1.55 | -1.59 | -3.38 | -3.21 | -4.06 | -5.19 | -4.00 | -3.82 | -0.66 | -2.00 | -1.26 | -1.21 | -0.99 | -1.55 | -3.09 | -3.08 | -4.59 | -3.04 | -3.48 | -2.12 | -1.32 | -2.36 | -1.62|
| dec-waitktgt |  |  |  |  | should | the | bra@@ | transition | is | to | be | &quot; | ori@@ | ous | re@@ | into | &quot; | &quot; | crossing | &quot; | am | h@@ | ir@@ | sch@@ | en | &quot; | will | be | used | . | increase | road | safety | . | </s>|
| full sent tgt |  |  |  |  | should | the | train | transition | &quot; | to | be | &quot; | ori@@ | ously | re@@ | to | in | &quot; | will | &quot; | am | h@@ | ir@@ | sch@@ | en | &quot; | will | be | re@@ | to | increase | road | safety | ? | </s>|
| ref | should | the | &quot; | am | h@@ | ir@@ | sch@@ | en | &quot; | railway | crossing | be | re@@ | constructed | at | great | cost | , | in | order | to | increase | traffic | safety | ? | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | schil@@ | ta@@ | ch | muss | dafür | 2@@ | 20 | 000 | euro | in | die | hand | nehmen | .|
| waitk tgt |  |  |  |  | sch@@ | il@@ | t@@ | ach | must | pay | eur | 2@@ | 20 | 000 | for | this | . | </s>|
| waitk prob |  |  |  |  | 0.25 | 0.90 | 0.93 | 0.76 | 0.30 | 0.65 | 0.79 | 0.96 | 0.84 | 0.92 | 0.45 | 0.65 | 0.79 | 0.91|
| dec-waitk prob |  |  |  |  | 0.47 | 0.53 | 0.81 | 0.04 | 0.71 | 0.50 | 0.14 | 0.93 | 0.91 | 0.93 | 0.57 | 0.63 | 0.70 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.12 | -1.55 | -1.87 | -3.81 | -1.79 | -3.10 | -4.02 | -1.44 | -1.32 | -1.37 | -2.04 | -2.18 | -2.26 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.29 | -0.99 | -1.24 | -1.88 | -3.10 | -2.31 | -1.52 | -1.11 | -1.56 | -1.45 | -2.59 | -2.09 | -2.09 | -1.65|
| full sent prob |  |  |  |  | 0.20 | 0.84 | 0.89 | 0.93 | 0.33 | 0.01 | 0.61 | 0.94 | 0.85 | 0.94 | 0.56 | 0.65 | 0.74 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.72 | -1.32 | -1.58 | -1.18 | -2.74 | -4.37 | -2.73 | -1.36 | -1.54 | -1.28 | -2.14 | -2.05 | -2.17 | -1.60|
| full sent KL (full->waitk) |  |  |  |  | -4.23 | -1.20 | -1.31 | -2.43 | -3.05 | -2.05 | -1.83 | -1.12 | -1.52 | -1.46 | -2.59 | -2.10 | -2.12 | -1.65|
| dec-waitktgt |  |  |  |  | sch@@ | il@@ | t@@ | ta@@ | must | pay | eur | 2@@ | 20 | 000 | for | this | . | </s>|
| full sent tgt |  |  |  |  | sch@@ | il@@ | t@@ | ach | must | therefore | eur | 2@@ | 20 | 000 | for | this | . | </s>|
| ref | sch@@ | il@@ | t@@ | ach | will | have | to | contribute | up | to | eur | 2@@ | 20@@ | ,000 | to | the | project | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | deutsche | bahn | will | im | kommenden | jahr | die | kin@@ | zi@@ | g@@ | tal@@ | -@@ | bahn@@ | strecke | verbessern | .|
| waitk tgt |  |  |  |  | deutsche | bahn | wants | to | introduce | the | kin@@ | zi@@ | g@@ | tal | railway | line | next | year | . | </s>|
| waitk prob |  |  |  |  | 0.27 | 0.97 | 0.21 | 0.77 | 0.04 | 0.62 | 0.17 | 0.88 | 0.92 | 0.60 | 0.70 | 0.73 | 0.33 | 0.92 | 0.89 | 0.91|
| dec-waitk prob |  |  |  |  | 0.10 | 0.94 | 0.67 | 0.49 | 0.00 | 0.06 | 0.67 | 0.34 | 0.93 | 0.40 | 0.47 | 0.64 | 0.41 | 0.92 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 50 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.40 | -1.30 | -1.80 | -2.63 | -3.89 | -3.37 | -2.14 | -2.56 | -1.30 | -2.92 | -2.33 | -2.63 | -2.33 | -1.48 | -1.79 | -1.55|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.30 | -1.02 | -3.51 | -2.09 | -4.71 | -2.46 | -4.42 | -1.22 | -1.35 | -1.48 | -1.99 | -2.11 | -3.27 | -1.52 | -1.78 | -1.62|
| full sent prob |  |  |  |  | 0.09 | 0.97 | 0.30 | 0.88 | 0.00 | 0.09 | 0.20 | 0.51 | 0.87 | 0.62 | 0.52 | 0.68 | 0.01 | 0.93 | 0.86 | 0.92|
| full sent rank |  |  |  |  | 1 | 0 | 0 | 0 | 37 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.09 | -1.08 | -2.72 | -1.68 | -1.49 | -3.20 | -4.37 | -2.34 | -1.68 | -2.19 | -2.42 | -2.53 | -2.98 | -1.41 | -1.88 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.31 | -1.04 | -3.47 | -2.33 | -4.71 | -2.47 | -4.37 | -1.35 | -1.31 | -1.56 | -2.01 | -2.13 | -3.15 | -1.52 | -1.76 | -1.62|
| dec-waitktgt |  |  |  |  | the | bahn | wants | to | see | kin@@ | kin@@ | z@@ | g@@ | tal | railway | line | next | year | . | </s>|
| full sent tgt |  |  |  |  | the | bahn | wants | to | improve | a | kin@@ | zi@@ | g@@ | tal | railway | line | to | year | . | </s>|
| ref | the | deutsche | bahn | hopes | to | improve | the | kin@@ | zi@@ | g@@ | tal | railway | line | in | the | coming | year | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | dort | plan@@ | t | die | stadt | , | in | höhe | des | dor@@ | tigen | tun@@ | n@@ | el@@ | m@@ | un@@ | des | west@@ | lich | der | bahn@@ | glei@@ | se | eine | aus@@ | bu@@ | chtung | zu | bauen | .|
| waitk tgt |  |  |  |  | the | city | plans | to | build | a | new | tunnel | in | the | area | , | which | is | located | west | of | the | railway | track | . | </s>|
| waitk prob |  |  |  |  | 0.22 | 0.54 | 0.35 | 0.79 | 0.18 | 0.22 | 0.09 | 0.03 | 0.15 | 0.63 | 0.15 | 0.24 | 0.10 | 0.31 | 0.16 | 0.51 | 0.88 | 0.77 | 0.53 | 0.71 | 0.55 | 0.91|
| dec-waitk prob |  |  |  |  | 0.33 | 0.46 | 0.28 | 0.69 | 0.01 | 0.06 | 0.07 | 0.13 | 0.04 | 0.36 | 0.29 | 0.01 | 0.08 | 0.36 | 0.05 | 0.38 | 0.89 | 0.78 | 0.55 | 0.22 | 0.85 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 6 | 2 | 0 | 1 | 2 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.80 | -2.58 | -3.30 | -2.53 | -4.94 | -2.54 | -5.61 | -4.29 | -1.57 | -3.84 | -3.59 | -1.56 | -4.71 | -3.81 | -5.06 | -2.98 | -1.68 | -2.30 | -2.10 | -3.10 | -1.67 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.24 | -2.97 | -2.97 | -2.11 | -4.13 | -4.15 | -5.58 | -5.85 | -3.90 | -2.93 | -4.21 | -3.45 | -4.51 | -3.33 | -4.26 | -2.36 | -1.76 | -2.46 | -2.98 | -1.40 | -2.61 | -1.66|
| full sent prob |  |  |  |  | 0.20 | 0.29 | 0.54 | 0.83 | 0.62 | 0.31 | 0.02 | 0.00 | 0.04 | 0.75 | 0.07 | 0.03 | 0.07 | 0.40 | 0.16 | 0.50 | 0.89 | 0.85 | 0.55 | 0.41 | 0.83 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 70 | 4 | 0 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.84 | -3.85 | -2.61 | -2.01 | -2.41 | -2.36 | -5.30 | -5.35 | -3.66 | -2.25 | -4.89 | -1.56 | -2.90 | -3.37 | -3.67 | -2.46 | -1.68 | -1.83 | -1.90 | -2.72 | -1.70 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -4.23 | -2.89 | -3.03 | -2.20 | -4.22 | -4.16 | -5.57 | -5.84 | -3.89 | -3.13 | -4.17 | -3.39 | -4.50 | -3.34 | -4.28 | -2.42 | -1.76 | -2.50 | -2.98 | -1.51 | -2.61 | -1.65|
| dec-waitktgt |  |  |  |  | the | city | plans | to | rise | up | new | tun@@ | there | the | area | . | but | is | located | west | of | the | railway | track | . | </s>|
| full sent tgt |  |  |  |  | the | city | plans | to | build | an | re@@ | extension | to | the | height | west | west | is | located | west | of | the | railway | track | . | </s>|
| ref | at | the | crossing | , | the | town | is | planning | to | increase | the | height | of | the | mouth | of | the | tunnel | to | the | west | of | the | railway | line | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | bürger@@ | meister | thomas | ha@@ | as | wider@@ | sprach | : | der | bahn@@ | übergang | &quot; | hir@@ | schen | &quot; | werde | regelmäßig | für | lang@@ | holz@@ | transpor@@ | te | genutzt | .|
| waitk tgt |  |  |  |  | may@@ | or | thomas | ha@@ | as | dis@@ | agreed | : | the | railway | crossing | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | is | regularly | used | for | long-@@ | wood | trans@@ | ports | . | </s>|
| waitk prob |  |  |  |  | 0.75 | 0.90 | 0.92 | 0.93 | 0.92 | 0.28 | 0.93 | 0.83 | 0.77 | 0.37 | 0.34 | 0.80 | 0.87 | 0.96 | 0.95 | 0.98 | 0.92 | 0.32 | 0.35 | 0.86 | 0.84 | 0.69 | 0.23 | 0.29 | 0.89 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.87 | 0.86 | 0.96 | 0.94 | 0.94 | 0.04 | 0.71 | 0.80 | 0.01 | 0.11 | 0.16 | 0.45 | 0.87 | 0.93 | 0.87 | 0.94 | 0.90 | 0.02 | 0.49 | 0.87 | 0.75 | 0.65 | 0.03 | 0.65 | 0.90 | 0.91 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.60 | -1.91 | -1.12 | -1.31 | -1.31 | -3.75 | -2.11 | -1.93 | -1.72 | -4.23 | -4.45 | -3.26 | -1.75 | -1.29 | -1.41 | -1.29 | -1.63 | -1.80 | -2.51 | -1.68 | -2.05 | -2.10 | -4.23 | -1.64 | -1.13 | -1.63 | -1.51|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.26 | -1.56 | -1.37 | -1.41 | -1.48 | -3.26 | -1.08 | -1.92 | -1.73 | -3.31 | -3.39 | -1.67 | -1.76 | -1.10 | -0.96 | -0.92 | -1.49 | -3.42 | -2.87 | -1.69 | -1.80 | -1.95 | -3.58 | -2.38 | -1.24 | -1.62 | -1.62|
| full sent prob |  |  |  |  | 0.91 | 0.92 | 0.96 | 0.94 | 0.92 | 0.05 | 0.85 | 0.54 | 0.75 | 0.24 | 0.20 | 0.64 | 0.92 | 0.99 | 0.92 | 0.98 | 0.92 | 0.59 | 0.46 | 0.92 | 0.82 | 0.65 | 0.06 | 0.63 | 0.92 | 0.91 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -1.25 | -1.45 | -1.11 | -1.34 | -1.52 | -3.46 | -1.62 | -2.41 | -2.37 | -2.71 | -4.01 | -2.71 | -1.36 | -0.91 | -1.23 | -1.02 | -1.51 | -2.44 | -2.20 | -1.36 | -1.87 | -2.06 | -4.24 | -1.63 | -1.10 | -1.62 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.29 | -1.61 | -1.38 | -1.41 | -1.47 | -3.27 | -1.19 | -1.75 | -2.20 | -3.35 | -3.41 | -1.80 | -1.80 | -1.15 | -1.00 | -0.95 | -1.50 | -3.59 | -2.88 | -1.73 | -1.84 | -1.95 | -3.58 | -2.39 | -1.25 | -1.62 | -1.61|
| dec-waitktgt |  |  |  |  | may@@ | or | thomas | ha@@ | as | opposed | agreed | : | </s> | train | crossing | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | </s> | regularly | used | for | long-@@ | distance | trans@@ | ports | . | </s>|
| full sent tgt |  |  |  |  | may@@ | or | thomas | ha@@ | as | contradic@@ | agreed | : | the | train | transition | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | is | regularly | used | for | long-@@ | distance | trans@@ | ports | . | </s>|
| ref | may@@ | or | thomas | ha@@ | as | re@@ | tor@@ | ted | : | the | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | railway | crossing | is | used | regularly | for | the | transportation | of | long | log@@ | s | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | rä@@ | te | kamen | überein | , | untersuchen | zu | lassen | , | welche | kosten | die | ange@@ | da@@ | chte | verbrei@@ | ter@@ | ung | der | straße | verursachen | würde | .|
| waitk tgt |  |  |  |  | the | counc@@ | ils | agreed | to | allow | an | investigation | into | the | costs | of | the | intended | extension | of | the | road | , | and | the | council | agreed | to | do | so | . | </s>|
| waitk prob |  |  |  |  | 0.63 | 0.91 | 0.89 | 0.92 | 0.80 | 0.18 | 0.29 | 0.53 | 0.58 | 0.68 | 0.56 | 0.39 | 0.44 | 0.57 | 0.21 | 0.88 | 0.65 | 0.82 | 0.29 | 0.27 | 0.16 | 0.03 | 0.56 | 0.39 | 0.23 | 0.69 | 0.79 | 0.91|
| dec-waitk prob |  |  |  |  | 0.67 | 0.83 | 0.94 | 0.94 | 0.85 | 0.03 | 0.13 | 0.67 | 0.75 | 0.66 | 0.54 | 0.59 | 0.55 | 0.14 | 0.30 | 0.84 | 0.84 | 0.64 | 0.00 | 0.17 | 0.09 | 0.07 | 0.08 | 0.54 | 0.43 | 0.79 | 0.72 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 39 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.17 | -1.92 | -1.27 | -1.16 | -1.81 | -3.01 | -4.02 | -1.88 | -1.41 | -2.19 | -1.63 | -2.42 | -2.45 | -3.20 | -2.47 | -1.92 | -1.64 | -2.12 | -1.48 | -3.94 | -4.37 | -6.03 | -4.36 | -2.46 | -3.55 | -1.73 | -2.36 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.70 | -1.32 | -1.71 | -1.31 | -2.09 | -3.70 | -3.17 | -2.14 | -1.64 | -2.14 | -2.20 | -3.23 | -3.51 | -1.70 | -2.85 | -1.72 | -1.99 | -1.51 | -2.67 | -3.64 | -4.13 | -6.04 | -2.35 | -2.27 | -4.37 | -2.00 | -2.14 | -1.63|
| full sent prob |  |  |  |  | 0.66 | 0.89 | 0.92 | 0.96 | 0.85 | 0.03 | 0.27 | 0.76 | 0.57 | 0.51 | 0.47 | 0.51 | 0.52 | 0.04 | 0.07 | 0.90 | 0.82 | 0.56 | 0.00 | 0.10 | 0.09 | 0.03 | 0.12 | 0.60 | 0.38 | 0.80 | 0.86 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 3 | 0 | 0 | 0 | 16 | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -2.44 | -1.33 | -1.45 | -1.05 | -1.85 | -2.90 | -3.54 | -1.52 | -1.79 | -2.34 | -2.35 | -2.61 | -3.28 | -2.77 | -3.35 | -1.67 | -1.64 | -2.12 | -1.58 | -3.79 | -4.33 | -5.96 | -4.10 | -2.28 | -3.60 | -1.66 | -1.78 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -2.69 | -1.36 | -1.69 | -1.33 | -2.09 | -3.71 | -3.20 | -2.18 | -1.60 | -2.07 | -2.16 | -3.20 | -3.50 | -1.67 | -2.79 | -1.77 | -1.98 | -1.46 | -2.86 | -3.63 | -4.14 | -6.04 | -2.37 | -2.28 | -4.36 | -2.00 | -2.24 | -1.63|
| dec-waitktgt |  |  |  |  | the | counc@@ | ils | agreed | to | have | us | investigation | into | the | costs | of | the | thought | extension | of | the | road | </s> | and | </s> | council | agreed | to | do | so | . | </s>|
| full sent tgt |  |  |  |  | the | counc@@ | ils | agreed | to | have | an | investigation | into | the | costs | of | the | thought | wid@@ | of | the | road | . | which | this | costs | agreed | to | do | so | . | </s>|
| ref | the | counc@@ | ill@@ | ors | agreed | to | have | an | investigation | conducted | as | to | what | costs | the | planned | wid@@ | ening | of | the | road | would | inc@@ | ur | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | verantwortung | hierfür | tra@@ | ge | wiederum | die | stadt | als | straßen@@ | bau@@ | last@@ | trä@@ | ger@@ | in | .|
| waitk tgt |  |  |  |  | the | responsibility | for | this | , | in | turn | , | lies | with | the | city | as | a | road | construction | lo@@ | ad@@ | er | . | </s>|
| waitk prob |  |  |  |  | 0.30 | 0.71 | 0.76 | 0.75 | 0.24 | 0.51 | 0.97 | 0.92 | 0.60 | 0.88 | 0.87 | 0.82 | 0.79 | 0.38 | 0.42 | 0.29 | 0.53 | 0.94 | 0.88 | 0.91 | 0.91|
| dec-waitk prob |  |  |  |  | 0.17 | 0.91 | 0.54 | 0.63 | 0.15 | 0.56 | 0.80 | 0.92 | 0.57 | 0.91 | 0.86 | 0.79 | 0.80 | 0.78 | 0.45 | 0.05 | 0.43 | 0.82 | 0.95 | 0.90 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -1.92 | -1.28 | -2.36 | -2.63 | -3.23 | -2.60 | -2.16 | -1.57 | -2.45 | -1.49 | -1.90 | -1.91 | -1.85 | -1.82 | -3.17 | -3.60 | -3.20 | -1.45 | -1.17 | -1.72 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.23 | -2.67 | -1.91 | -1.97 | -3.11 | -2.65 | -0.92 | -1.49 | -2.15 | -1.62 | -1.86 | -1.44 | -1.80 | -2.61 | -3.09 | -3.03 | -3.04 | -1.12 | -1.71 | -1.63 | -1.64|
| full sent prob |  |  |  |  | 0.47 | 0.14 | 0.74 | 0.70 | 0.15 | 0.57 | 0.86 | 0.91 | 0.53 | 0.90 | 0.87 | 0.78 | 0.84 | 0.79 | 0.40 | 0.07 | 0.46 | 0.81 | 0.94 | 0.89 | 0.91|
| full sent rank |  |  |  |  | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.23 | -3.69 | -2.11 | -2.38 | -3.08 | -2.56 | -1.83 | -1.61 | -2.50 | -1.56 | -1.87 | -1.80 | -1.74 | -1.74 | -3.40 | -3.63 | -3.22 | -1.43 | -1.23 | -1.74 | -1.59|
| full sent KL (full->waitk) |  |  |  |  | -3.29 | -2.22 | -2.03 | -2.01 | -3.11 | -2.65 | -0.96 | -1.49 | -2.13 | -1.61 | -1.86 | -1.44 | -1.83 | -2.62 | -3.08 | -3.04 | -3.05 | -1.11 | -1.71 | -1.63 | -1.64|
| dec-waitktgt |  |  |  |  | responsibility | responsibility | for | this | lies | in | turn | , | lies | with | the | city | as | a | road | lo@@ | lo@@ | ad@@ | er | . | </s>|
| full sent tgt |  |  |  |  | the | city | for | this | lies | in | turn | , | lies | with | the | city | as | a | road | lo@@ | lo@@ | ad@@ | er | . | </s>|
| ref | the | town | , | as | the | authority | responsible | for | road | construction | , | would | then | bear | responsibility | for | this | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | selbst | züge | vom | hauptbahnhof | her | müssten | an | dieser | stelle | schon | soweit | ab@@ | geb@@ | re@@ | m@@ | st | sein | , | dass | keine | kol@@ | li@@ | sion | dro@@ | he | .|
| waitk tgt |  |  |  |  | even | trains | from | the | main | station | would | have | to | be | stopped | at | this | point | to | the | point | that | no | col@@ | li@@ | sion | threat@@ | ens | . | </s>|
| waitk prob |  |  |  |  | 0.16 | 0.89 | 0.74 | 0.49 | 0.52 | 0.34 | 0.32 | 0.74 | 0.90 | 0.74 | 0.10 | 0.16 | 0.79 | 0.75 | 0.23 | 0.69 | 0.53 | 0.62 | 0.48 | 0.80 | 0.97 | 0.93 | 0.46 | 0.99 | 0.85 | 0.91|
| dec-waitk prob |  |  |  |  | 0.18 | 0.89 | 0.49 | 0.54 | 0.46 | 0.51 | 0.30 | 0.74 | 0.84 | 0.44 | 0.04 | 0.04 | 0.74 | 0.70 | 0.01 | 0.56 | 0.13 | 0.19 | 0.58 | 0.82 | 0.96 | 0.80 | 0.31 | 0.95 | 0.75 | 0.91|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 0 | 9 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -4.14 | -1.20 | -2.89 | -2.31 | -2.14 | -1.78 | -3.75 | -2.16 | -1.96 | -3.28 | -5.09 | -3.75 | -2.33 | -2.21 | -2.32 | -2.64 | -3.14 | -2.11 | -2.14 | -1.66 | -1.15 | -1.75 | -3.09 | -1.26 | -2.10 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.70 | -1.18 | -2.18 | -2.02 | -1.78 | -1.94 | -3.09 | -2.01 | -1.64 | -1.98 | -4.67 | -3.56 | -1.85 | -1.57 | -3.21 | -2.22 | -1.44 | -1.93 | -2.16 | -1.86 | -1.08 | -1.18 | -2.65 | -0.92 | -1.81 | -1.65|
| full sent prob |  |  |  |  | 0.24 | 0.89 | 0.63 | 0.66 | 0.45 | 0.53 | 0.39 | 0.80 | 0.84 | 0.74 | 0.05 | 0.06 | 0.77 | 0.72 | 0.09 | 0.44 | 0.64 | 0.24 | 0.55 | 0.85 | 0.95 | 0.81 | 0.29 | 0.95 | 0.69 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -4.48 | -1.34 | -2.76 | -2.18 | -2.38 | -1.81 | -2.71 | -1.82 | -1.88 | -2.13 | -4.30 | -3.78 | -2.17 | -2.04 | -3.53 | -2.61 | -1.48 | -1.69 | -2.01 | -1.54 | -1.24 | -1.75 | -3.08 | -1.25 | -2.06 | -1.62|
| full sent KL (full->waitk) |  |  |  |  | -4.70 | -1.18 | -2.26 | -2.04 | -1.77 | -1.94 | -3.15 | -2.05 | -1.64 | -2.17 | -4.68 | -3.57 | -1.87 | -1.58 | -3.26 | -2.16 | -1.61 | -1.96 | -2.16 | -1.88 | -1.07 | -1.19 | -2.64 | -0.92 | -1.77 | -1.65|
| dec-waitktgt |  |  |  |  | even | trains | from | the | main | station | would | have | to | be | bloc@@ | as | this | point | . | the | extent | where | no | col@@ | li@@ | sion | threat@@ | ens | . | </s>|
| full sent tgt |  |  |  |  | even | trains | from | the | main | station | would | have | to | be | bra@@ | to | this | point | , | the | point | where | no | col@@ | li@@ | sion | threat@@ | ens | . | </s>|
| ref | the | trains | themselves | , | coming | from | the | central | station | , | must | also | be | sufficiently | slow@@ | ed | down | so | that | there | is | no | threat | of | col@@ | li@@ | sion | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | 30 | vorschläge | standen | zur | auswahl | , | fünf | sind | noch | im | rennen | .|
| waitk tgt |  |  |  |  | thir@@ | ty | proposals | were | on | the | table | , | five | are | still | in | the | race | . | </s>|
| waitk prob |  |  |  |  | 0.28 | 0.95 | 0.89 | 0.74 | 0.26 | 0.86 | 0.67 | 0.60 | 0.76 | 0.65 | 0.83 | 0.58 | 0.72 | 0.77 | 0.88 | 0.91|
| dec-waitk prob |  |  |  |  | 0.11 | 0.91 | 0.59 | 0.77 | 0.03 | 0.70 | 0.56 | 0.48 | 0.71 | 0.60 | 0.85 | 0.77 | 0.80 | 0.75 | 0.88 | 0.92|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.71 | -1.44 | -2.97 | -2.10 | -3.99 | -2.41 | -2.70 | -2.35 | -2.16 | -2.35 | -1.47 | -1.91 | -2.09 | -2.12 | -1.79 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -2.85 | -1.14 | -1.29 | -1.83 | -3.91 | -1.63 | -2.48 | -2.11 | -1.83 | -2.29 | -1.62 | -2.60 | -2.48 | -2.05 | -1.82 | -1.60|
| full sent prob |  |  |  |  | 0.08 | 0.90 | 0.24 | 0.66 | 0.05 | 0.64 | 0.27 | 0.46 | 0.73 | 0.62 | 0.82 | 0.74 | 0.80 | 0.74 | 0.88 | 0.92|
| full sent rank |  |  |  |  | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.80 | -1.44 | -4.60 | -2.49 | -3.31 | -2.41 | -4.14 | -2.42 | -2.03 | -2.35 | -1.58 | -2.09 | -2.07 | -2.15 | -1.81 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -2.81 | -1.13 | -1.03 | -1.76 | -3.92 | -1.59 | -2.32 | -2.11 | -1.84 | -2.30 | -1.60 | -2.58 | -2.48 | -2.05 | -1.82 | -1.59|
| dec-waitktgt |  |  |  |  | 30 | ty | proposals | were | available | the | table | , | five | are | still | in | the | race | . | </s>|
| full sent tgt |  |  |  |  | 30 | ty | proposals | were | available | the | table | , | five | are | still | in | the | race | . | </s>|
| ref | there | were | 30 | proposals | to | choose | from | , | five | of | which | are | still | in | the | running | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | mehr | als | 1000 | planeten | bei | anderen | ster@@ | nen | haben | ast@@ | ron@@ | omen | bereits | gefunden | .|
| waitk tgt |  |  |  |  | more | than | 1000 | plan@@ | ets | in | other | stars | have | already | found | a@@ | stronom@@ | ers | . | </s>|
| waitk prob |  |  |  |  | 0.33 | 0.92 | 0.52 | 0.88 | 0.97 | 0.38 | 0.79 | 0.68 | 0.87 | 0.51 | 0.67 | 0.98 | 0.94 | 0.82 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.56 | 0.93 | 0.50 | 0.97 | 0.97 | 0.41 | 0.85 | 0.68 | 0.39 | 0.39 | 0.39 | 0.96 | 0.96 | 0.96 | 0.89 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.42 | -1.45 | -2.52 | -0.99 | -1.02 | -2.97 | -1.68 | -2.73 | -2.59 | -2.68 | -3.17 | -1.18 | -1.18 | -1.10 | -1.73 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.01 | -1.51 | -2.34 | -1.74 | -1.03 | -3.08 | -2.14 | -2.33 | -1.14 | -2.14 | -2.16 | -0.96 | -1.31 | -2.27 | -1.72 | -1.65|
| full sent prob |  |  |  |  | 0.28 | 0.91 | 0.47 | 0.92 | 0.98 | 0.33 | 0.82 | 0.68 | 0.83 | 0.38 | 0.59 | 0.97 | 0.94 | 0.95 | 0.88 | 0.92|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.40 | -1.56 | -2.57 | -1.41 | -0.98 | -3.08 | -1.92 | -2.56 | -1.91 | -2.83 | -2.78 | -1.10 | -1.31 | -1.19 | -1.85 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.93 | -1.50 | -2.33 | -1.70 | -1.04 | -3.09 | -2.12 | -2.33 | -1.46 | -2.14 | -2.26 | -0.97 | -1.30 | -2.27 | -1.71 | -1.64|
| dec-waitktgt |  |  |  |  | more | than | 1000 | plan@@ | ets | in | other | stars | have | already | found | a@@ | stronom@@ | ers | . | </s>|
| full sent tgt |  |  |  |  | more | than | 1000 | plan@@ | ets | in | other | stars | have | already | found | a@@ | stronom@@ | ers | . | </s>|
| ref | a@@ | stronom@@ | ers | have | already | found | more | than | 1@@ | ,000 | plan@@ | ets | near | other | stars | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ob | es | zumindest | auf | einigen | davon | leben | gibt | , | weiß | keiner | .|
| waitk tgt |  |  |  |  | whether | it | is | at | least | alive | on | some | of | them | , | nobody | knows | . | </s>|
| waitk prob |  |  |  |  | 0.38 | 0.37 | 0.27 | 0.22 | 0.91 | 0.19 | 0.79 | 0.85 | 0.83 | 0.75 | 0.51 | 0.48 | 0.88 | 0.90 | 0.91|
| dec-waitk prob |  |  |  |  | 0.32 | 0.08 | 0.58 | 0.21 | 0.95 | 0.01 | 0.56 | 0.87 | 0.78 | 0.75 | 0.22 | 0.19 | 0.83 | 0.85 | 0.92|
| dec-waitk rank |  |  |  |  | 0 | 3 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -3.42 | -2.10 | -2.66 | -3.32 | -1.20 | -2.94 | -2.24 | -1.53 | -2.24 | -1.57 | -3.38 | -2.59 | -1.67 | -1.91 | -1.53|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -3.51 | -2.81 | -3.92 | -4.11 | -1.51 | -3.91 | -1.53 | -1.72 | -2.00 | -1.62 | -2.56 | -1.77 | -1.54 | -1.58 | -1.62|
| full sent prob |  |  |  |  | 0.40 | 0.01 | 0.43 | 0.05 | 0.94 | 0.01 | 0.53 | 0.84 | 0.76 | 0.66 | 0.13 | 0.26 | 0.85 | 0.81 | 0.92|
| full sent rank |  |  |  |  | 0 | 4 | 0 | 3 | 0 | 14 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.07 | -1.49 | -2.75 | -3.43 | -1.31 | -3.03 | -2.40 | -1.63 | -2.36 | -1.71 | -3.04 | -2.65 | -1.60 | -2.09 | -1.58|
| full sent KL (full->waitk) |  |  |  |  | -3.53 | -2.80 | -3.89 | -4.09 | -1.50 | -3.91 | -1.51 | -1.70 | -1.98 | -1.57 | -2.53 | -1.77 | -1.55 | -1.55 | -1.62|
| dec-waitktgt |  |  |  |  | whether | or | is | at | least | some | on | some | of | them | , | no | knows | . | </s>|
| full sent tgt |  |  |  |  | whether | there | is | alive | least | some | on | some | of | them | is | no | knows | . | </s>|
| ref | whether | or | not | life | exists | on | at | least | some | of | these | , | no-@@ | one | knows | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | die | auswahl | fällt | schwer | : | soll | man | nach | gra@@ | vi@@ | ta@@ | tions@@ | w@@ | ellen | suchen | ?|
| waitk tgt |  |  |  |  | the | choice | is | difficult | : | if | you | want | to | search | for | gra@@ | vity | waves | ? | </s>|
| waitk prob |  |  |  |  | 0.28 | 0.66 | 0.79 | 0.44 | 0.69 | 0.34 | 0.82 | 0.39 | 0.86 | 0.22 | 0.84 | 0.96 | 0.49 | 0.94 | 0.43 | 0.91|
| dec-waitk prob |  |  |  |  | 0.18 | 0.85 | 0.86 | 0.37 | 0.79 | 0.03 | 0.79 | 0.57 | 0.62 | 0.00 | 0.92 | 0.77 | 0.42 | 0.87 | 0.31 | 0.91|
| dec-waitk rank |  |  |  |  | 1 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 68 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  |  |  | -2.75 | -1.45 | -1.77 | -2.50 | -2.08 | -4.75 | -1.88 | -2.45 | -2.36 | -4.03 | -1.39 | -2.18 | -2.47 | -1.66 | -3.73 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  |  |  | -4.07 | -2.28 | -2.22 | -2.64 | -2.26 | -3.42 | -1.84 | -2.82 | -1.73 | -3.99 | -1.83 | -0.96 | -1.57 | -1.03 | -3.52 | -1.63|
| full sent prob |  |  |  |  | 0.29 | 0.66 | 0.83 | 0.37 | 0.83 | 0.01 | 0.83 | 0.42 | 0.88 | 0.48 | 0.92 | 0.73 | 0.41 | 0.84 | 0.59 | 0.91|
| full sent rank |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  |  |  | -3.34 | -2.02 | -2.00 | -3.00 | -1.80 | -3.09 | -1.69 | -2.51 | -1.73 | -2.40 | -1.47 | -2.39 | -2.48 | -1.74 | -2.80 | -1.64|
| full sent KL (full->waitk) |  |  |  |  | -4.08 | -2.20 | -2.20 | -2.62 | -2.29 | -3.45 | -1.87 | -2.80 | -1.91 | -4.10 | -1.82 | -0.93 | -1.56 | -1.02 | -3.60 | -1.62|
| dec-waitktgt |  |  |  |  | it | choice | is | difficult | : | let | you | want | to | gra@@ | for | gra@@ | vity | waves | ? | </s>|
| full sent tgt |  |  |  |  | the | choice | is | difficult | : | should | you | want | to | search | for | gra@@ | vity | waves | ? | </s>|
| ref | the | choice | is | a | difficult | one | : | should | we | search | for | gra@@ | vit@@ | ational | waves | ? | </s>|

PRED AVG SCORE: -0.6167, PRED PPL: 1.8528
GOLD AVG SCORE: 0.0000, GOLD PPL: 1.0000
