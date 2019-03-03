norm_stop False

|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | two | sets | of | lights | so | close | to | one | another | : | inten@@ | tional | or | just | a | sil@@ | ly | error | ?|
| waitk tgt |  |  | zwei | lich@@ | ter | , | die | so | nahe | bei@@ | einander | liegen | : | vor@@ | sätz@@ | lich | oder | einfach | nur | ein | sei@@ | den@@ | hafter | fehler | ? | </s>|
| waitk prob |  |  | 0.43 | 0.44 | 0.32 | 0.42 | 0.73 | 0.38 | 0.34 | 0.24 | 0.96 | 0.57 | 0.84 | 0.43 | 0.89 | 0.61 | 0.90 | 0.48 | 0.87 | 0.59 | 0.07 | 0.10 | 0.17 | 0.85 | 0.86 | 0.90|
| dec-waitk prob |  |  | 0.76 | 0.52 | 0.14 | 0.02 | 0.23 | 0.05 | 0.34 | 0.35 | 0.95 | 0.61 | 0.89 | 0.51 | 0.82 | 0.92 | 0.89 | 0.44 | 0.39 | 0.68 | 0.01 | 0.42 | 0.00 | 0.88 | 0.87 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 2 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 31 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.88 | -2.37 | -2.27 | -2.93 | -3.63 | -4.43 | -2.21 | -2.54 | -1.17 | -2.03 | -1.66 | -2.59 | -2.08 | -1.15 | -1.72 | -2.89 | -2.87 | -2.39 | -4.15 | -2.99 | -1.32 | -1.59 | -1.82 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.68 | -2.83 | -2.55 | -3.31 | -2.15 | -3.31 | -2.64 | -3.33 | -1.03 | -2.27 | -1.83 | -3.21 | -1.33 | -2.07 | -1.55 | -2.84 | -1.07 | -2.86 | -5.34 | -4.88 | -4.48 | -1.64 | -1.96 | -1.72|
| full sent prob |  |  | 0.84 | 0.75 | 0.04 | 0.08 | 0.77 | 0.71 | 0.39 | 0.23 | 0.93 | 0.34 | 0.85 | 0.55 | 0.97 | 0.91 | 0.88 | 0.33 | 0.51 | 0.68 | 0.01 | 0.28 | 0.00 | 0.90 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 4 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 11 | 0 | 28 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.61 | -1.60 | -2.97 | -2.93 | -2.23 | -2.04 | -2.01 | -2.66 | -1.30 | -2.22 | -1.81 | -2.54 | -1.00 | -1.16 | -1.79 | -2.20 | -2.55 | -2.21 | -3.89 | -3.77 | -1.11 | -1.50 | -1.61 | -1.66|
| full sent KL (full->waitk) |  |  | -3.71 | -2.90 | -2.52 | -3.37 | -2.47 | -3.52 | -2.66 | -3.31 | -1.01 | -2.15 | -1.81 | -3.23 | -1.44 | -2.07 | -1.54 | -2.84 | -1.15 | -2.87 | -5.34 | -4.87 | -4.48 | -1.65 | -1.99 | -1.72|
| dec-waitktgt |  |  | zwei | lich@@ | ter@@ | schließen | die | sich | nahe | bei@@ | einander | liegen | : | vor@@ | sätz@@ | lich | oder | einfach | nur | ein | al@@ | den@@ | fehler | fehler | ? | </s>|
| full sent tgt |  |  | zwei | lich@@ | ter@@ | so | die | so | nah | zu@@ | einander | liegen | : | vor@@ | sätz@@ | lich | oder | nur | nur | ein | al@@ | den@@ | fehler | fehler | ? | </s>|
| ref | zwei | anlagen | so | nah | bei@@ | einander | : | absicht | oder | schil@@ | d@@ | bürger@@ | st@@ | reich | ? | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | yesterday | , | gu@@ | t@@ | ach@@ | t | &apos;s | may@@ | or | gave | a | clear | answer | to | this | question | .|
| waitk tgt |  |  | gestern | wurde | gut@@ | chen | &apos; | s | bürger@@ | meister | in | einer | klaren | antwort | auf | diese | frage | . | </s>|
| waitk prob |  |  | 0.68 | 0.16 | 0.63 | 0.13 | 0.30 | 0.80 | 0.84 | 0.96 | 0.17 | 0.18 | 0.24 | 0.84 | 0.82 | 0.87 | 0.85 | 0.62 | 0.90|
| dec-waitk prob |  |  | 0.85 | 0.00 | 0.06 | 0.00 | 0.18 | 0.80 | 0.90 | 0.93 | 0.00 | 0.02 | 0.58 | 0.77 | 0.02 | 0.83 | 0.85 | 0.38 | 0.91|
| dec-waitk rank |  |  | 0 | 20 | 4 | 926 | 1 | 0 | 0 | 0 | 26 | 2 | 0 | 0 | 3 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.68 | -3.70 | -3.09 | -4.58 | -3.53 | -2.33 | -1.46 | -1.36 | -3.69 | -3.25 | -2.31 | -2.28 | -1.05 | -1.85 | -1.76 | -3.31 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.61 | -4.15 | -2.51 | -5.29 | -4.02 | -2.17 | -1.70 | -1.00 | -4.38 | -3.62 | -4.50 | -1.91 | -1.30 | -1.59 | -1.79 | -2.81 | -1.72|
| full sent prob |  |  | 0.50 | 0.01 | 0.00 | 0.00 | 0.01 | 0.91 | 0.93 | 0.94 | 0.02 | 0.24 | 0.63 | 0.80 | 0.81 | 0.88 | 0.87 | 0.01 | 0.90|
| full sent rank |  |  | 0 | 8 | 65 | 9793 | 8 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0|
| full sent KL (waitk->full) |  |  | -2.90 | -2.38 | -2.09 | -4.58 | -3.44 | -1.52 | -1.25 | -1.36 | -2.87 | -3.01 | -2.20 | -2.14 | -1.83 | -1.62 | -1.65 | -4.13 | -1.70|
| full sent KL (full->waitk) |  |  | -2.41 | -4.18 | -2.47 | -5.29 | -3.98 | -2.24 | -1.73 | -1.00 | -4.39 | -3.65 | -4.51 | -1.93 | -1.82 | -1.62 | -1.80 | -2.62 | -1.72|
| dec-waitktgt |  |  | gestern | , | gu@@ | ta@@ | </s> | s | bürger@@ | meister | </s> | gu@@ | klaren | antwort | darauf | diese | frage | . | </s>|
| full sent tgt |  |  | gestern | hat | diese | ta@@ | bürger@@ | s | bürger@@ | meister | eine | einer | klaren | antwort | auf | diese | frage | beantwortet | </s>|
| ref | diese | frage | hat | gu@@ | ta@@ | chs | bürger@@ | meister | gestern | klar | beantwortet | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | kl@@ | user | lights | protect | cy@@ | cli@@ | sts | , | as | well | as | those | travelling | by | bus | and | the | residents | of | ber@@ | g@@ | le | .|
| waitk tgt |  |  | die | kl@@ | user | lich@@ | ter | schützen | rad@@ | fahrer | , | sowie | die | rei@@ | senden | mit | dem | bus | und | die | bewohner | von | berg@@ | le | . | </s>|
| waitk prob |  |  | 0.25 | 0.57 | 0.83 | 0.30 | 0.97 | 0.79 | 0.57 | 0.93 | 0.42 | 0.39 | 0.23 | 0.34 | 0.88 | 0.45 | 0.50 | 0.86 | 0.79 | 0.65 | 0.33 | 0.67 | 0.53 | 0.91 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.03 | 0.12 | 0.23 | 0.07 | 0.94 | 0.80 | 0.08 | 0.89 | 0.51 | 0.02 | 0.27 | 0.56 | 0.98 | 0.04 | 0.43 | 0.91 | 0.06 | 0.06 | 0.55 | 0.50 | 0.65 | 0.96 | 0.88 | 0.92|
| dec-waitk rank |  |  | 1 | 2 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -0.79 | -2.46 | -2.30 | -2.00 | -1.28 | -1.80 | -2.61 | -1.36 | -2.84 | -4.18 | -3.27 | -2.70 | -0.90 | -2.51 | -2.63 | -1.37 | -1.76 | -2.71 | -1.80 | -2.41 | -1.56 | -1.15 | -1.86 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.58 | -3.16 | -1.43 | -2.86 | -0.99 | -1.98 | -2.39 | -1.13 | -2.50 | -3.24 | -3.87 | -3.21 | -1.43 | -2.90 | -2.75 | -1.75 | -1.59 | -2.43 | -2.48 | -2.25 | -1.71 | -1.55 | -1.66 | -1.67|
| full sent prob |  |  | 0.63 | 0.31 | 0.54 | 0.05 | 0.93 | 0.72 | 0.15 | 0.88 | 0.38 | 0.10 | 0.17 | 0.01 | 0.97 | 0.74 | 0.63 | 0.92 | 0.85 | 0.51 | 0.61 | 0.80 | 0.59 | 0.96 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.50 | -2.39 | -2.39 | -1.94 | -1.33 | -2.25 | -3.23 | -1.35 | -2.53 | -3.42 | -3.37 | -2.75 | -0.95 | -1.88 | -2.04 | -1.35 | -1.90 | -2.52 | -1.57 | -1.79 | -1.70 | -1.09 | -1.78 | -1.67|
| full sent KL (full->waitk) |  |  | -3.68 | -3.25 | -1.64 | -2.85 | -0.98 | -1.93 | -2.41 | -1.12 | -2.48 | -3.28 | -3.84 | -3.07 | -1.43 | -3.16 | -2.82 | -1.76 | -2.11 | -2.66 | -2.49 | -2.40 | -1.70 | -1.55 | -1.67 | -1.66|
| dec-waitktgt |  |  | kl@@ | lich@@ | u@@ | li@@ | ter | schützen | die | fahrer | , | </s> | die | rei@@ | senden | </s> | dem | bus | </s> | den | bewohner | von | berg@@ | le | . | </s>|
| full sent tgt |  |  | die | leu@@ | user | li@@ | ter | schützen | die | fahrer | , | aber | die | mit | senden | mit | dem | bus | und | die | bewohner | von | berg@@ | le | . | </s>|
| ref | die | klu@@ | ser@@ | -@@ | amp@@ | el | sichere | sowohl | rad@@ | fahrer | als | auch | bus@@ | fahr@@ | gäste | und | die | berg@@ | le-@@ | bewohner | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | system | , | which | officially | became | operational | yesterday | , | is | of | importance | to | the | sul@@ | z@@ | b@@ | ach@@ | we@@ | g | / | kir@@ | ch@@ | stras@@ | se | junction | .|
| waitk tgt |  |  | das | system | , | das | offiziell | gestern | in | betrieb | wurde | , | ist | für | den | sul@@ | z@@ | ba@@ | ch@@ | weg | / | kir@@ | ch@@ | strasse | von | bedeutung | . | </s>|
| waitk prob |  |  | 0.52 | 0.69 | 0.84 | 0.76 | 0.35 | 0.42 | 0.29 | 0.91 | 0.15 | 0.92 | 0.82 | 0.61 | 0.41 | 0.63 | 0.86 | 0.89 | 0.92 | 0.98 | 0.89 | 0.93 | 0.93 | 0.60 | 0.39 | 0.54 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.82 | 0.89 | 0.87 | 0.78 | 0.95 | 0.00 | 0.28 | 0.74 | 0.02 | 0.28 | 0.82 | 0.06 | 0.47 | 0.83 | 0.97 | 0.93 | 0.93 | 0.97 | 0.18 | 0.96 | 0.96 | 0.33 | 0.50 | 0.69 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 76 | 0 | 0 | 6 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.87 | -1.57 | -1.84 | -1.94 | -0.67 | -3.83 | -3.23 | -1.54 | -3.08 | -3.54 | -1.92 | -2.46 | -2.68 | -1.44 | -1.01 | -1.32 | -1.29 | -1.09 | -3.60 | -1.12 | -1.18 | -2.29 | -2.76 | -2.46 | -1.66 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.53 | -2.74 | -1.97 | -2.15 | -3.83 | -3.23 | -3.76 | -1.09 | -3.61 | -1.11 | -1.97 | -2.06 | -2.21 | -2.17 | -1.76 | -1.64 | -1.12 | -0.97 | -1.19 | -1.36 | -1.29 | -2.63 | -3.62 | -2.69 | -1.72 | -1.66|
| full sent prob |  |  | 0.44 | 0.04 | 0.76 | 0.74 | 0.00 | 0.21 | 0.25 | 0.98 | 0.02 | 0.90 | 0.67 | 0.45 | 0.81 | 0.87 | 0.94 | 0.86 | 0.92 | 0.96 | 0.82 | 0.92 | 0.93 | 0.44 | 0.43 | 0.67 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 2 | 0 | 0 | 10 | 1 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.56 | -1.97 | -2.26 | -1.97 | -1.66 | -3.37 | -4.07 | -0.87 | -3.20 | -1.73 | -2.66 | -3.28 | -1.67 | -1.30 | -1.31 | -1.88 | -1.34 | -1.15 | -2.10 | -1.33 | -1.38 | -2.15 | -3.35 | -2.24 | -1.73 | -1.67|
| full sent KL (full->waitk) |  |  | -3.37 | -2.24 | -1.90 | -2.13 | -3.55 | -3.32 | -3.75 | -1.27 | -3.61 | -1.58 | -1.87 | -2.20 | -2.29 | -2.18 | -1.74 | -1.59 | -1.12 | -0.97 | -1.66 | -1.33 | -1.27 | -2.70 | -3.60 | -2.69 | -1.71 | -1.66|
| dec-waitktgt |  |  | das | system | , | das | offiziell | in | in | betrieb | genommen | , | ist | von | den | sul@@ | z@@ | ba@@ | ch@@ | weg | von | kir@@ | ch@@ | strasse | von | bedeutung | . | </s>|
| full sent tgt |  |  | das | gestern | , | das | gestern | seit | in | betrieb | genommen | , | ist | für | den | sul@@ | z@@ | ba@@ | ch@@ | weg | / | kir@@ | ch@@ | strasse | von | bedeutung | . | </s>|
| ref | die | gestern | offiziell | in | betrieb | genommen@@ | e | anlage | sei | wichtig | für | den | kreuz@@ | ungs@@ | bereich | sul@@ | z@@ | ba@@ | ch@@ | weg | / | kir@@ | ch@@ | straße | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | this | was | also | confirmed | by | peter | ar@@ | no@@ | ld | from | the | off@@ | enburg | district | office | .|
| waitk tgt |  |  | dies | wurde | auch | von | peter | ar@@ | n@@ | old | aus | der | offen@@ | burger | bezir@@ | k@@ | s@@ | verwaltung | bestätigt | . | </s>|
| waitk prob |  |  | 0.26 | 0.51 | 0.63 | 0.41 | 0.84 | 0.91 | 0.86 | 0.94 | 0.42 | 0.46 | 0.42 | 0.39 | 0.17 | 0.79 | 0.59 | 0.47 | 0.92 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.12 | 0.31 | 0.65 | 0.72 | 0.84 | 0.97 | 0.95 | 0.99 | 0.01 | 0.11 | 0.92 | 0.11 | 0.02 | 0.94 | 0.91 | 0.65 | 0.92 | 0.91 | 0.92|
| dec-waitk rank |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 2 | 7 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.76 | -3.46 | -2.29 | -2.09 | -1.73 | -1.10 | -1.19 | -0.86 | -1.56 | -1.79 | -0.89 | -4.28 | -3.09 | -1.13 | -1.05 | -2.01 | -1.29 | -1.67 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.68 | -2.54 | -2.57 | -2.35 | -1.76 | -1.64 | -1.96 | -1.19 | -2.26 | -2.18 | -4.13 | -2.36 | -3.91 | -2.25 | -2.41 | -2.46 | -1.32 | -1.65 | -1.68|
| full sent prob |  |  | 0.45 | 0.28 | 0.68 | 0.78 | 0.77 | 0.95 | 0.98 | 0.96 | 0.12 | 0.03 | 0.10 | 0.52 | 0.12 | 0.90 | 0.91 | 0.66 | 0.89 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.01 | -2.83 | -2.29 | -1.65 | -2.11 | -1.20 | -0.94 | -1.01 | -2.25 | -1.53 | -4.34 | -2.90 | -2.11 | -1.40 | -1.04 | -2.01 | -1.48 | -1.67 | -1.62|
| full sent KL (full->waitk) |  |  | -3.72 | -2.55 | -2.58 | -2.37 | -1.71 | -1.64 | -1.99 | -1.17 | -2.38 | -2.09 | -3.84 | -2.46 | -3.94 | -2.23 | -2.41 | -2.46 | -1.29 | -1.65 | -1.68|
| dec-waitktgt |  |  | auch | wurde | auch | von | peter | ar@@ | n@@ | old | bestätigt | dem | offen@@ | burg | nieder@@ | k@@ | s@@ | verwaltung | bestätigt | . | </s>|
| full sent tgt |  |  | dies | wurde | auch | von | peter | ar@@ | n@@ | old | vom | offen@@ | distri@@ | burger | kreis@@ | k@@ | s@@ | verwaltung | bestätigt | . | </s>|
| ref | dies | bestätigt | auch | peter | ar@@ | n@@ | old | vom | land@@ | rat@@ | sam@@ | t | offen@@ | burg | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | and | they | are | also | ener@@ | g@@ | y-@@ | efficient | : | the | older | light | systems | con@@ | sume | around | 100 | wat@@ | ts | , | with | the | new | ones | consum@@ | ing | just | eight | .|
| waitk tgt |  |  | und | sie | sind | auch | energi@@ | es@@ | par@@ | end | : | das | äl@@ | tere | licht@@ | system | verbrau@@ | cht | rund | 100 | wa@@ | tt | , | mit | den | neuen | verbrau@@ | cht | nur | acht | . | </s>|
| waitk prob |  |  | 0.52 | 0.69 | 0.61 | 0.63 | 0.48 | 0.73 | 0.97 | 0.91 | 0.85 | 0.53 | 0.49 | 0.85 | 0.31 | 0.89 | 0.92 | 0.94 | 0.30 | 0.89 | 0.80 | 0.94 | 0.74 | 0.58 | 0.65 | 0.84 | 0.72 | 0.63 | 0.71 | 0.89 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.78 | 0.51 | 0.68 | 0.68 | 0.08 | 0.89 | 0.81 | 0.94 | 0.81 | 0.14 | 0.32 | 0.85 | 0.21 | 0.80 | 0.78 | 0.55 | 0.18 | 0.89 | 0.82 | 0.98 | 0.45 | 0.09 | 0.36 | 0.67 | 0.48 | 0.47 | 0.02 | 0.64 | 0.86 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.96 | -3.07 | -2.61 | -2.53 | -1.99 | -1.33 | -1.78 | -1.19 | -2.18 | -2.79 | -4.16 | -1.85 | -3.97 | -2.21 | -2.07 | -3.56 | -2.35 | -1.59 | -2.11 | -0.98 | -2.69 | -3.62 | -3.05 | -2.32 | -3.48 | -2.65 | -3.00 | -2.35 | -2.00 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.29 | -2.36 | -2.89 | -2.67 | -2.30 | -2.07 | -0.89 | -1.40 | -1.79 | -2.52 | -3.28 | -1.63 | -2.34 | -1.57 | -1.03 | -0.94 | -2.42 | -1.57 | -2.28 | -1.28 | -1.90 | -2.24 | -2.17 | -1.65 | -1.95 | -1.72 | -1.49 | -1.16 | -1.80 | -1.68|
| full sent prob |  |  | 0.19 | 0.48 | 0.73 | 0.43 | 0.15 | 0.92 | 0.90 | 0.89 | 0.84 | 0.01 | 0.47 | 0.87 | 0.18 | 0.71 | 0.78 | 0.90 | 0.19 | 0.90 | 0.91 | 0.95 | 0.66 | 0.01 | 0.07 | 0.78 | 0.04 | 0.53 | 0.04 | 0.78 | 0.83 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 6 | 1 | 0 | 2 | 0 | 2 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.90 | -3.03 | -2.37 | -2.79 | -1.96 | -1.11 | -1.42 | -1.60 | -2.09 | -2.34 | -3.65 | -1.53 | -3.70 | -2.55 | -2.01 | -1.66 | -2.81 | -1.60 | -1.47 | -1.09 | -2.24 | -2.91 | -2.92 | -2.03 | -3.44 | -1.90 | -2.41 | -1.83 | -2.11 | -1.69|
| full sent KL (full->waitk) |  |  | -3.04 | -2.34 | -2.91 | -2.54 | -2.32 | -2.09 | -0.97 | -1.37 | -1.81 | -2.55 | -3.35 | -1.65 | -2.34 | -1.50 | -1.03 | -1.21 | -2.41 | -1.57 | -2.34 | -1.27 | -2.03 | -2.22 | -2.01 | -1.72 | -1.69 | -1.76 | -1.50 | -1.26 | -1.78 | -1.68|
| dec-waitktgt |  |  | und | sie | sind | auch | energie@@ | es@@ | par@@ | end | : | </s> | äl@@ | tere | licht@@ | system | verbrau@@ | cht | ca. | 100 | wa@@ | tt | , | die | den | neuen | verbrau@@ | cht | . | acht | . | </s>|
| full sent tgt |  |  | und | sie | sind | auch | energie@@ | es@@ | par@@ | end | : | die | äl@@ | tere | licht | system | verbrau@@ | cht | etwa | 100 | wa@@ | tt | , | das | nur | neuen | nur | cht | man | acht | . | </s>|
| ref | und | spar@@ | sam | ist | sie | auch | : | die | älteren | lich@@ | tan@@ | lagen | verbrau@@ | chen | etwa | 100 | wa@@ | tt | , | die | neuen | gerade | mal | acht | wa@@ | tt | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ar@@ | no@@ | ld | explained | the | technology | used | by | the | new | system | : | it | is | fitted | with | two | rad@@ | ar | sen@@ | sors | .|
| waitk tgt |  |  | ar@@ | n@@ | old | hat | die | technologie | erläu@@ | tert | , | die | das | neue | system | verwendet | : | es | ist | mit | zwei | ra@@ | dar@@ | sen@@ | sor@@ | en | ausgestattet | . | </s>|
| waitk prob |  |  | 0.63 | 0.91 | 0.94 | 0.41 | 0.60 | 0.53 | 0.20 | 0.93 | 0.88 | 0.75 | 0.36 | 0.85 | 0.94 | 0.34 | 0.82 | 0.67 | 0.52 | 0.81 | 0.90 | 0.90 | 0.95 | 0.53 | 0.94 | 0.97 | 0.57 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.95 | 0.99 | 0.99 | 0.09 | 0.31 | 0.37 | 0.28 | 0.76 | 0.87 | 0.73 | 0.70 | 0.89 | 0.91 | 0.17 | 0.81 | 0.59 | 0.63 | 0.82 | 0.94 | 0.87 | 0.97 | 0.83 | 0.95 | 0.94 | 0.46 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.00 | -0.82 | -0.83 | -1.83 | -2.25 | -3.39 | -1.89 | -2.37 | -1.85 | -2.20 | -1.98 | -1.59 | -1.58 | -3.68 | -1.96 | -2.56 | -2.45 | -1.85 | -1.26 | -1.61 | -1.01 | -1.62 | -1.18 | -1.38 | -2.37 | -1.74 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.09 | -1.62 | -1.24 | -2.35 | -2.80 | -2.27 | -3.13 | -1.24 | -1.74 | -2.13 | -2.92 | -1.96 | -1.31 | -3.04 | -1.90 | -2.06 | -2.65 | -1.90 | -1.51 | -1.47 | -1.19 | -2.95 | -1.35 | -1.12 | -2.31 | -1.76 | -1.66|
| full sent prob |  |  | 0.60 | 0.97 | 0.98 | 0.17 | 0.63 | 0.23 | 0.08 | 0.94 | 0.88 | 0.77 | 0.52 | 0.89 | 0.88 | 0.22 | 0.90 | 0.69 | 0.62 | 0.85 | 0.91 | 0.92 | 0.97 | 0.86 | 0.95 | 0.94 | 0.48 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.87 | -1.00 | -0.92 | -2.34 | -2.78 | -3.40 | -2.99 | -1.29 | -1.80 | -2.11 | -2.64 | -1.59 | -1.78 | -3.19 | -1.36 | -2.19 | -2.30 | -1.78 | -1.48 | -1.37 | -1.05 | -1.49 | -1.15 | -1.36 | -2.36 | -1.73 | -1.68|
| full sent KL (full->waitk) |  |  | -2.90 | -1.61 | -1.23 | -2.33 | -2.96 | -2.21 | -3.10 | -1.38 | -1.75 | -2.16 | -2.87 | -1.96 | -1.28 | -3.06 | -1.95 | -2.11 | -2.65 | -1.92 | -1.49 | -1.51 | -1.19 | -2.96 | -1.36 | -1.12 | -2.32 | -1.76 | -1.65|
| dec-waitktgt |  |  | ar@@ | n@@ | old | erklärte | erklärt | technologie | erklärt | tert | , | die | das | neue | system | verwendet | : | es | ist | mit | zwei | ra@@ | dar@@ | sen@@ | sor@@ | en | ausgestattet | . | </s>|
| full sent tgt |  |  | ar@@ | n@@ | old | erklärte | die | technologie | des | tert | , | die | das | neue | system | verwendet | : | es | ist | mit | zwei | ra@@ | dar@@ | sen@@ | sor@@ | en | ausgestattet | . | </s>|
| ref | ar@@ | n@@ | old | erklärte | die | technik | der | neuen | anlage | : | diese | ist | mit | zwei | ra@@ | dar@@ | sen@@ | sor@@ | en | ausgestattet | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | if | the | pede@@ | strian | pres@@ | ses | the | button | at | the | traffic | lights | , | the | top | rad@@ | ar | sensor | checks | the | traffic | status | .|
| waitk tgt |  |  | wenn | die | fuß@@ | gän@@ | ger@@ | -@@ | pre@@ | ssen | die | ta@@ | ste | an | der | amp@@ | el | , | die | ober@@ | en | ra@@ | dar@@ | -@@ | sen@@ | sor | prüft | den | verkehrs@@ | status | . | </s>|
| waitk prob |  |  | 0.48 | 0.59 | 0.61 | 0.95 | 0.70 | 0.07 | 0.63 | 0.88 | 0.28 | 0.89 | 0.95 | 0.73 | 0.82 | 0.92 | 0.72 | 0.79 | 0.45 | 0.93 | 0.44 | 0.96 | 0.93 | 0.47 | 0.95 | 0.80 | 0.35 | 0.84 | 0.25 | 0.54 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.84 | 0.37 | 0.85 | 0.97 | 0.61 | 0.00 | 0.04 | 0.30 | 0.17 | 0.82 | 0.92 | 0.78 | 0.73 | 0.84 | 0.78 | 0.66 | 0.10 | 0.14 | 0.06 | 0.86 | 0.95 | 0.09 | 0.92 | 0.79 | 0.07 | 0.71 | 0.56 | 0.50 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 11 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.55 | -3.31 | -1.45 | -1.03 | -2.18 | -2.67 | -2.49 | -3.40 | -3.10 | -1.90 | -1.41 | -1.92 | -2.05 | -1.71 | -2.09 | -2.45 | -3.92 | -4.16 | -4.64 | -1.84 | -1.19 | -2.44 | -1.46 | -1.54 | -3.69 | -2.13 | -2.06 | -1.72 | -1.62 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.63 | -2.67 | -3.28 | -1.18 | -1.44 | -5.52 | -2.17 | -1.03 | -3.16 | -1.22 | -1.12 | -1.86 | -1.69 | -1.19 | -1.62 | -1.84 | -2.72 | -0.58 | -1.99 | -1.03 | -1.18 | -2.81 | -1.25 | -1.35 | -2.38 | -1.63 | -2.87 | -1.76 | -1.76 | -1.68|
| full sent prob |  |  | 0.22 | 0.34 | 0.54 | 0.97 | 0.87 | 0.00 | 0.00 | 0.16 | 0.16 | 0.81 | 0.89 | 0.79 | 0.70 | 0.81 | 0.69 | 0.00 | 0.24 | 0.26 | 0.27 | 0.84 | 0.94 | 0.08 | 0.95 | 0.87 | 0.15 | 0.75 | 0.50 | 0.48 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 12 | 22 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.26 | -3.06 | -3.73 | -1.13 | -1.35 | -1.97 | -1.11 | -2.54 | -2.47 | -2.03 | -1.52 | -1.98 | -2.27 | -1.89 | -2.14 | -0.48 | -3.47 | -3.89 | -2.54 | -2.02 | -1.22 | -1.60 | -1.24 | -1.45 | -3.14 | -2.03 | -2.36 | -1.94 | -1.63 | -1.65|
| full sent KL (full->waitk) |  |  | -3.39 | -2.66 | -3.12 | -1.18 | -1.56 | -5.53 | -2.13 | -0.93 | -3.15 | -1.21 | -1.10 | -1.86 | -1.66 | -1.17 | -1.58 | -1.46 | -2.80 | -0.67 | -2.11 | -1.01 | -1.17 | -2.85 | -1.27 | -1.40 | -2.43 | -1.65 | -2.86 | -1.75 | -1.76 | -1.67|
| dec-waitktgt |  |  | wenn | die | fuß@@ | gän@@ | ger@@ | zone | drücken | ssen | auf | ta@@ | ste | an | der | amp@@ | el | , | kontrolliert | sen@@ | ra@@ | ra@@ | dar@@ | sen@@ | sen@@ | sor | überprüft | den | verkehrs@@ | status | . | </s>|
| full sent tgt |  |  | wenn | die | fuß@@ | gän@@ | ger@@ | zone | ta@@ | ssung | an | ta@@ | ste | an | der | amp@@ | el | drücken | die | ober@@ | en | ra@@ | dar@@ | sen@@ | sen@@ | sor | überprüft | den | verkehrs@@ | status | . | </s>|
| ref | drückt | der | fuß@@ | gän@@ | ger | den | amp@@ | el@@ | kno@@ | pf | , | te@@ | stet | der | ober@@ | e | ra@@ | dar@@ | sen@@ | sor | die | verkehrs@@ | lage | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | an | additional | rad@@ | ar | sensor | checks | whether | the | green | phase | for | the | pede@@ | strian | can | be | ended | .|
| waitk tgt |  |  | ein | zusätz@@ | licher | ra@@ | dar@@ | sen@@ | sor | prüft | , | ob | die | grüne | phase | für | die | fuß@@ | gän@@ | ger@@ | zone | beendet | werden | kann | . | </s>|
| waitk prob |  |  | 0.31 | 0.72 | 0.92 | 0.85 | 0.95 | 0.48 | 0.96 | 0.73 | 0.71 | 0.96 | 0.71 | 0.82 | 0.81 | 0.53 | 0.78 | 0.73 | 0.97 | 0.88 | 0.93 | 0.48 | 0.88 | 0.91 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.53 | 0.60 | 0.60 | 0.52 | 0.99 | 0.88 | 0.97 | 0.38 | 0.68 | 0.93 | 0.69 | 0.75 | 0.34 | 0.48 | 0.51 | 0.87 | 0.98 | 0.69 | 0.93 | 0.65 | 0.90 | 0.90 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.93 | -1.70 | -1.76 | -2.71 | -0.88 | -1.14 | -1.07 | -2.35 | -2.06 | -1.47 | -2.43 | -1.61 | -3.73 | -2.58 | -2.70 | -1.59 | -1.03 | -1.58 | -1.32 | -2.15 | -1.50 | -1.63 | -1.60 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.62 | -1.67 | -1.08 | -1.59 | -1.19 | -3.74 | -1.15 | -1.56 | -2.35 | -1.17 | -2.32 | -1.49 | -1.83 | -2.28 | -2.00 | -1.99 | -1.08 | -1.30 | -1.34 | -2.99 | -1.67 | -1.50 | -1.68 | -1.69|
| full sent prob |  |  | 0.67 | 0.38 | 0.93 | 0.65 | 0.98 | 0.87 | 0.96 | 0.34 | 0.67 | 0.93 | 0.60 | 0.72 | 0.58 | 0.32 | 0.51 | 0.89 | 0.98 | 0.71 | 0.93 | 0.71 | 0.91 | 0.90 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.33 | -2.63 | -1.35 | -2.65 | -0.96 | -1.27 | -1.13 | -2.72 | -2.25 | -1.42 | -2.51 | -1.96 | -2.98 | -2.57 | -2.40 | -1.41 | -1.04 | -1.56 | -1.30 | -1.90 | -1.45 | -1.63 | -1.61 | -1.65|
| full sent KL (full->waitk) |  |  | -3.66 | -1.52 | -1.32 | -1.68 | -1.18 | -3.74 | -1.15 | -1.54 | -2.34 | -1.17 | -2.27 | -1.48 | -2.00 | -2.21 | -2.00 | -2.00 | -1.08 | -1.31 | -1.34 | -3.01 | -1.68 | -1.50 | -1.68 | -1.69|
| dec-waitktgt |  |  | ein | zusätz@@ | licher | ra@@ | dar@@ | sen@@ | sor | prüft | , | ob | die | grüne | phase | für | die | fuß@@ | gän@@ | ger@@ | zone | beendet | werden | kann | . | </s>|
| full sent tgt |  |  | ein | zusätz@@ | licher | ra@@ | dar@@ | sen@@ | sor | prüft | , | ob | die | grüne | phase | für | die | fuß@@ | gän@@ | ger@@ | zone | beendet | werden | kann | . | </s>|
| ref | ein | weiteres | ra@@ | dar@@ | sen@@ | sor | prüft | , | ob | die | grün@@ | phase | für | den | fuß@@ | gän@@ | ger | beendet | werden | kann | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | of | course | , | drivers | must | also | play | their | part | and | keep | their | eyes | on | the | road | .|
| waitk tgt |  |  | natürlich | müssen | die | fahrer | auch | ihre | rolle | spielen | und | ihre | augen | vor | den | gefahren | ver@@ | schließen | . | </s>|
| waitk prob |  |  | 0.49 | 0.15 | 0.38 | 0.87 | 0.75 | 0.34 | 0.68 | 0.63 | 0.82 | 0.44 | 0.90 | 0.34 | 0.34 | 0.12 | 0.21 | 0.50 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.75 | 0.04 | 0.38 | 0.63 | 0.59 | 0.20 | 0.82 | 0.72 | 0.86 | 0.18 | 0.94 | 0.48 | 0.51 | 0.01 | 0.17 | 0.71 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.70 | -3.29 | -2.33 | -2.01 | -2.77 | -3.40 | -1.88 | -1.78 | -1.78 | -3.66 | -1.26 | -2.88 | -2.49 | -2.98 | -3.79 | -2.21 | -1.66 | -1.64|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.02 | -3.83 | -2.76 | -1.40 | -2.04 | -3.36 | -2.81 | -2.41 | -1.85 | -2.96 | -1.63 | -2.91 | -2.57 | -4.73 | -3.59 | -3.13 | -1.67 | -1.68|
| full sent prob |  |  | 0.49 | 0.72 | 0.12 | 0.74 | 0.58 | 0.16 | 0.79 | 0.62 | 0.86 | 0.12 | 0.86 | 0.20 | 0.03 | 0.01 | 0.16 | 0.63 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 1 | 2 | 7 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.90 | -1.71 | -1.60 | -2.00 | -2.60 | -2.60 | -2.06 | -2.19 | -1.81 | -3.54 | -1.85 | -2.23 | -1.86 | -4.15 | -4.26 | -2.65 | -1.66 | -1.68|
| full sent KL (full->waitk) |  |  | -2.91 | -3.91 | -2.63 | -1.48 | -2.03 | -3.39 | -2.79 | -2.36 | -1.85 | -2.95 | -1.57 | -2.98 | -2.58 | -4.72 | -3.57 | -3.10 | -1.67 | -1.67|
| dec-waitktgt |  |  | natürlich | auch | die | fahrer | auch | ihre | rolle | spielen | und | behalten | augen | vor | den | straßen@@ | ver@@ | schließen | . | </s>|
| full sent tgt |  |  | natürlich | müssen | auch | fahrer | auch | ihren | rolle | spielen | und | die | augen | auf | der | straßen | ver@@ | schließen | . | </s>|
| ref | natürlich | mü@@ | sse | der | auto@@ | fahrer | hier | als | partner | mit@@ | denken | und | die | fahr@@ | bahn | beobachten | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | however | , | director | fres@@ | ach@@ | er | seems | to | have | little | trust | in | the | text | .|
| waitk tgt |  |  | dennoch | hat | der | direktor | fre@@ | sa@@ | cher | offenbar | wenig | vertrauen | in | den | text | . | </s>|
| waitk prob |  |  | 0.18 | 0.16 | 0.20 | 0.33 | 0.94 | 0.22 | 0.91 | 0.20 | 0.79 | 0.91 | 0.82 | 0.82 | 0.88 | 0.86 | 0.90|
| dec-waitk prob |  |  | 0.01 | 0.01 | 0.15 | 0.78 | 0.97 | 0.28 | 0.97 | 0.04 | 0.87 | 0.88 | 0.86 | 0.78 | 0.89 | 0.90 | 0.91|
| dec-waitk rank |  |  | 9 | 7 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.65 | -3.54 | -2.35 | -1.47 | -1.03 | -4.97 | -0.97 | -3.02 | -1.34 | -1.71 | -1.69 | -1.91 | -1.64 | -1.65 | -1.64|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.83 | -4.67 | -3.79 | -3.68 | -1.27 | -4.75 | -1.43 | -3.67 | -1.77 | -1.42 | -1.99 | -1.75 | -1.74 | -1.90 | -1.69|
| full sent prob |  |  | 0.02 | 0.05 | 0.05 | 0.24 | 0.97 | 0.48 | 0.97 | 0.03 | 0.85 | 0.89 | 0.86 | 0.84 | 0.91 | 0.89 | 0.90|
| full sent rank |  |  | 6 | 2 | 2 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.49 | -1.66 | -2.30 | -2.08 | -1.08 | -3.95 | -0.97 | -2.16 | -1.42 | -1.69 | -1.78 | -1.76 | -1.47 | -1.73 | -1.69|
| full sent KL (full->waitk) |  |  | -3.83 | -4.68 | -3.77 | -3.59 | -1.27 | -4.79 | -1.43 | -3.69 | -1.76 | -1.43 | -1.99 | -1.79 | -1.75 | -1.89 | -1.69|
| dec-waitktgt |  |  | allerdings | : | direktor | direktor | fre@@ | sa@@ | cher | wenig | wenig | vertrauen | in | den | text | . | </s>|
| full sent tgt |  |  | allerdings | scheint | regi@@ | regi@@ | fre@@ | sa@@ | cher | wenig | wenig | vertrauen | in | den | text | . | </s>|
| ref | dabei | scheint | regi@@ | ss@@ | eur | fre@@ | sa@@ | cher | dem | text | wenig | zu | vertrauen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | particular | , | the | ac@@ | t@@ | res@@ | ses | play | a | major | role | in | the | sometimes | rather | du@@ | bi@@ | ous | st@@ | aging | .|
| waitk tgt |  |  | insbesondere | die | ak@@ | ten | , | die | in | der | geschichte | der | europäischen | union | manchmal | eher | du@@ | bio@@ | se | stä@@ | be | spielen | . | </s>|
| waitk prob |  |  | 0.43 | 0.22 | 0.23 | 0.22 | 0.11 | 0.49 | 0.12 | 0.25 | 0.03 | 0.46 | 0.06 | 0.46 | 0.17 | 0.41 | 0.18 | 0.83 | 0.54 | 0.11 | 0.27 | 0.72 | 0.84 | 0.91|
| dec-waitk prob |  |  | 0.67 | 0.36 | 0.06 | 0.05 | 0.01 | 0.01 | 0.01 | 0.16 | 0.02 | 0.03 | 0.03 | 0.62 | 0.02 | 0.48 | 0.08 | 0.00 | 0.65 | 0.00 | 0.06 | 0.05 | 0.74 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 2 | 1 | 2 | 1 | 10 | 1 | 6 | 3 | 0 | 0 | 8 | 0 | 0 | 1 | 0 | 319 | 2 | 4 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.99 | -2.66 | -2.69 | -2.63 | -1.18 | -0.97 | -5.28 | -4.42 | -5.51 | -5.02 | -5.96 | -2.81 | -4.91 | -2.83 | -5.81 | -0.37 | -2.00 | -5.51 | -2.83 | -3.64 | -2.15 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.24 | -4.07 | -4.42 | -4.19 | -4.57 | -3.43 | -4.80 | -4.18 | -5.94 | -2.81 | -5.96 | -3.75 | -4.24 | -3.16 | -4.61 | -0.99 | -2.12 | -5.22 | -3.12 | -1.65 | -1.75 | -1.68|
| full sent prob |  |  | 0.42 | 0.47 | 0.01 | 0.08 | 0.00 | 0.61 | 0.14 | 0.39 | 0.00 | 0.01 | 0.00 | 0.49 | 0.26 | 0.11 | 0.08 | 0.64 | 0.38 | 0.00 | 0.07 | 0.33 | 0.02 | 0.91|
| full sent rank |  |  | 0 | 0 | 6 | 1 | 15 | 0 | 0 | 0 | 444 | 10 | 56 | 0 | 0 | 1 | 2 | 0 | 0 | 9468 | 3 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -2.92 | -2.77 | -2.75 | -5.26 | -0.95 | -2.98 | -4.09 | -3.10 | -2.25 | -2.88 | -5.36 | -3.39 | -3.30 | -3.86 | -3.46 | -1.69 | -3.28 | -5.72 | -2.01 | -3.74 | -1.28 | -1.67|
| full sent KL (full->waitk) |  |  | -3.16 | -4.07 | -4.36 | -4.18 | -4.58 | -3.68 | -4.81 | -4.22 | -5.94 | -2.80 | -5.95 | -3.70 | -4.28 | -3.04 | -4.63 | -1.36 | -2.02 | -5.22 | -3.15 | -1.82 | -1.28 | -1.67|
| dec-waitktgt |  |  | insbesondere | die | ac@@ | t@@ | </s> | </s> | </s> | den | vergangenheit | eine | europäischen | union | eine | eher | du@@ | bi@@ | se | , | mme | bilden | . | </s>|
| full sent tgt |  |  | insbesondere | die | schau@@ | tra@@ | spielen | die | in | der | manchmal | manchmal | manchmal | union | manchmal | etwas | zweifel@@ | bio@@ | se | auftreten | mme | spielen | , | </s>|
| ref | vor | allem | die | schau@@ | spiel@@ | erinnen | kommen | bei | den | mit@@ | unter | etwas | fra@@ | g@@ | würdigen | szen@@ | ischen | um@@ | setzungen | d@@ | ran | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | they | are | man@@ | handled | , | their | heads | held | under | water | , | tack@@ | ed | to | the | wall | by | their | evening | go@@ | wn@@ | s | .|
| waitk tgt |  |  | sie | werden | von | menschen | be@@ | herrscht | , | ihre | kö@@ | pf@@ | e | unter | wasser | gehalten | , | von | ihrem | ab@@ | end@@ | lichen | got@@ | tes@@ | dienst | an | die | wand | ange@@ | pa@@ | ckt | . | </s>|
| waitk prob |  |  | 0.60 | 0.75 | 0.25 | 0.18 | 0.16 | 0.19 | 0.86 | 0.45 | 0.79 | 0.96 | 0.94 | 0.82 | 0.92 | 0.74 | 0.86 | 0.25 | 0.40 | 0.55 | 0.97 | 0.48 | 0.04 | 0.57 | 0.73 | 0.73 | 0.73 | 0.95 | 0.29 | 0.34 | 0.84 | 0.88 | 0.90|
| dec-waitk prob |  |  | 0.45 | 0.43 | 0.01 | 0.01 | 0.12 | 0.33 | 0.76 | 0.04 | 0.78 | 0.84 | 0.94 | 0.47 | 0.97 | 0.01 | 0.55 | 0.06 | 0.01 | 0.46 | 0.81 | 0.43 | 0.00 | 0.93 | 0.27 | 0.35 | 0.57 | 0.95 | 0.07 | 0.03 | 0.97 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 11 | 9 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 19 | 0 | 2 | 8 | 0 | 0 | 0 | 89 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.38 | -2.61 | -3.86 | -3.32 | -3.96 | -3.20 | -2.06 | -3.92 | -2.07 | -2.06 | -1.32 | -2.92 | -0.98 | -3.93 | -2.23 | -3.95 | -2.92 | -3.55 | -2.17 | -3.01 | -4.85 | -0.85 | -2.81 | -3.99 | -2.26 | -0.99 | -4.35 | -1.93 | -0.91 | -1.66 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.73 | -1.97 | -3.62 | -3.72 | -3.62 | -3.55 | -1.68 | -3.06 | -2.05 | -1.07 | -1.29 | -1.48 | -1.22 | -1.41 | -1.57 | -3.30 | -3.45 | -2.20 | -0.92 | -3.20 | -5.24 | -2.35 | -1.95 | -1.93 | -1.91 | -1.14 | -3.48 | -2.25 | -1.36 | -1.73 | -1.71|
| full sent prob |  |  | 0.54 | 0.68 | 0.07 | 0.07 | 0.07 | 0.18 | 0.79 | 0.30 | 0.52 | 0.98 | 0.95 | 0.60 | 0.97 | 0.02 | 0.62 | 0.07 | 0.04 | 0.70 | 0.96 | 0.48 | 0.00 | 0.93 | 0.21 | 0.48 | 0.64 | 0.94 | 0.13 | 0.06 | 0.95 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 2 | 4 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 3 | 0 | 0 | 0 | 60 | 0 | 1 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.19 | -2.36 | -4.56 | -4.33 | -3.80 | -2.42 | -2.01 | -3.51 | -3.06 | -1.00 | -1.26 | -2.62 | -1.04 | -2.23 | -2.08 | -4.36 | -2.60 | -2.49 | -1.13 | -3.14 | -5.04 | -0.83 | -2.70 | -3.26 | -2.21 | -1.04 | -4.24 | -2.28 | -1.03 | -1.68 | -1.69|
| full sent KL (full->waitk) |  |  | -2.77 | -2.11 | -3.62 | -3.73 | -3.62 | -3.56 | -1.70 | -3.15 | -1.88 | -1.18 | -1.30 | -1.57 | -1.21 | -1.44 | -1.63 | -3.30 | -3.52 | -2.29 | -1.05 | -3.22 | -5.24 | -2.35 | -1.91 | -2.01 | -1.94 | -1.14 | -3.50 | -2.25 | -1.35 | -1.73 | -1.70|
| dec-waitktgt |  |  | sie | werden | hand@@ | ihnen | hand@@ | herrscht | , | die | kö@@ | pf@@ | e | unter | wasser | werden | , | die | der | ab@@ | end@@ | lichen | tor@@ | tes@@ | dienst | an | die | wand | ge@@ | griffen | ckt | . | </s>|
| full sent tgt |  |  | sie | werden | hand@@ | ihren | ge@@ | arbeitet | , | ihre | kö@@ | pf@@ | e | unter | wasser | , | , | an | ihren | ab@@ | end@@ | lichen | g@@ | tes@@ | lä@@ | an | die | wand | ge@@ | griffen | ckt | . | </s>|
| ref | sie | werden | hart | ange@@ | fasst | , | mit | dem | kopf | unter | wasser | get@@ | au@@ | cht | , | mit | ihren | ab@@ | end@@ | ro@@ | ben | an | die | wand | ge@@ | ta@@ | ck@@ | ert | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | usually | dul@@ | l | arena | of | highway | planning | has | suddenly | spa@@ | w@@ | ned | intense | debate | and | color@@ | ful | al@@ | li@@ | ances | .|
| waitk tgt |  |  | die | üb@@ | licherweise | lang@@ | wei@@ | lige | ar@@ | ena | der | auto@@ | bahn@@ | planung | hat | plötz@@ | lich | eine | intensi@@ | ve | debatte | und | bun@@ | te | bün@@ | d@@ | nisse | hervor@@ | gerufen | . | </s>|
| waitk prob |  |  | 0.34 | 0.35 | 0.80 | 0.17 | 0.87 | 0.78 | 0.82 | 0.98 | 0.82 | 0.30 | 0.95 | 0.54 | 0.60 | 0.70 | 0.93 | 0.28 | 0.41 | 0.95 | 0.60 | 0.68 | 0.41 | 0.93 | 0.62 | 0.98 | 0.93 | 0.36 | 0.80 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.28 | 0.47 | 0.39 | 0.16 | 0.91 | 0.67 | 0.89 | 0.94 | 0.77 | 0.20 | 0.93 | 0.74 | 0.69 | 0.48 | 0.88 | 0.27 | 0.68 | 0.87 | 0.74 | 0.67 | 0.56 | 0.95 | 0.46 | 0.96 | 0.97 | 0.64 | 0.74 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.14 | -3.28 | -2.92 | -3.71 | -1.16 | -1.81 | -1.47 | -1.36 | -2.11 | -2.96 | -1.21 | -2.19 | -2.23 | -3.00 | -1.77 | -2.97 | -1.97 | -1.87 | -1.44 | -2.47 | -2.79 | -1.21 | -1.49 | -1.16 | -1.06 | -1.66 | -1.34 | -1.73 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.67 | -3.60 | -1.47 | -4.60 | -1.34 | -1.65 | -2.09 | -0.95 | -1.92 | -3.72 | -1.13 | -3.27 | -2.85 | -2.21 | -1.38 | -3.35 | -3.20 | -1.14 | -2.20 | -2.65 | -2.98 | -1.36 | -2.09 | -1.01 | -1.35 | -2.66 | -1.16 | -1.65 | -1.65|
| full sent prob |  |  | 0.52 | 0.56 | 0.58 | 0.32 | 0.80 | 0.77 | 0.94 | 0.95 | 0.74 | 0.18 | 0.97 | 0.74 | 0.80 | 0.82 | 0.91 | 0.22 | 0.66 | 0.93 | 0.70 | 0.73 | 0.59 | 0.95 | 0.46 | 0.96 | 0.97 | 0.61 | 0.69 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.09 | -2.33 | -2.26 | -3.55 | -1.39 | -1.52 | -1.15 | -1.30 | -2.30 | -3.48 | -1.00 | -2.16 | -1.72 | -1.65 | -1.60 | -3.04 | -2.08 | -1.45 | -1.55 | -2.31 | -2.51 | -1.20 | -1.50 | -1.22 | -1.05 | -1.73 | -1.34 | -1.74 | -1.68|
| full sent KL (full->waitk) |  |  | -3.73 | -3.63 | -1.59 | -4.62 | -1.27 | -1.71 | -2.13 | -0.96 | -1.89 | -3.70 | -1.17 | -3.27 | -2.90 | -2.41 | -1.40 | -3.33 | -3.20 | -1.19 | -2.19 | -2.68 | -2.99 | -1.36 | -2.10 | -1.01 | -1.35 | -2.66 | -1.13 | -1.65 | -1.64|
| dec-waitktgt |  |  | die | üb@@ | licherweise | dum@@ | wei@@ | lige | ar@@ | ena | der | straßen@@ | bahn@@ | planung | hat | plötz@@ | lich | eine | intensi@@ | ve | debatte | und | bun@@ | te | bün@@ | d@@ | nisse | hervor@@ | gerufen | . | </s>|
| full sent tgt |  |  | die | üb@@ | licherweise | lang@@ | wei@@ | lige | ar@@ | ena | der | straßen@@ | bahn@@ | planung | hat | plötz@@ | lich | intensi@@ | intensi@@ | ve | debatte | und | bun@@ | te | bün@@ | d@@ | nisse | hervor@@ | gerufen | . | </s>|
| ref | das | normalerweise | eher | lang@@ | wei@@ | lige | gebiet | der | straßen@@ | planung | hat | plötz@@ | lich | eine | intensi@@ | ve | debatte | mit | bun@@ | ten | allian@@ | zen | ent@@ | fa@@ | cht | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | american | civil | liberties | union | is | deeply | concerned | , | too | , | raising | a | variety | of | privacy | issues | .|
| waitk tgt |  |  | die | amerikanischen | bürger@@ | rechts@@ | union | ist | zu@@ | tief@@ | st | besorgt | darüber | , | dass | eine | vielzahl | von | datenschutz@@ | fragen | aufge@@ | worfen | werden | . | </s>|
| waitk prob |  |  | 0.28 | 0.30 | 0.66 | 0.51 | 0.23 | 0.71 | 0.53 | 0.98 | 0.96 | 0.76 | 0.30 | 0.91 | 0.72 | 0.19 | 0.50 | 0.78 | 0.19 | 0.79 | 0.26 | 0.98 | 0.67 | 0.85 | 0.91|
| dec-waitk prob |  |  | 0.41 | 0.31 | 0.95 | 0.01 | 0.60 | 0.57 | 0.60 | 0.98 | 0.96 | 0.27 | 0.01 | 0.79 | 0.35 | 0.08 | 0.53 | 0.80 | 0.04 | 0.71 | 0.31 | 0.95 | 0.27 | 0.34 | 0.91|
| dec-waitk rank |  |  | 0 | 1 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.52 | -3.04 | -0.89 | -1.05 | -2.90 | -2.98 | -1.99 | -1.00 | -1.17 | -1.91 | -2.51 | -2.29 | -3.31 | -2.63 | -1.71 | -2.08 | -1.76 | -2.02 | -2.75 | -1.09 | -1.90 | -2.85 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.26 | -3.50 | -2.77 | -2.59 | -3.09 | -2.07 | -2.55 | -1.01 | -1.16 | -1.35 | -2.33 | -1.53 | -2.01 | -3.88 | -1.65 | -2.14 | -3.74 | -1.61 | -2.49 | -0.91 | -1.89 | -1.45 | -1.65|
| full sent prob |  |  | 0.48 | 0.01 | 0.83 | 0.06 | 0.66 | 0.64 | 0.04 | 0.97 | 0.95 | 0.45 | 0.26 | 0.90 | 0.75 | 0.08 | 0.57 | 0.78 | 0.05 | 0.68 | 0.35 | 0.94 | 0.27 | 0.76 | 0.91|
| full sent rank |  |  | 0 | 9 | 0 | 4 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.32 | -2.71 | -1.46 | -3.67 | -2.58 | -2.64 | -2.57 | -1.12 | -1.33 | -2.40 | -2.32 | -1.74 | -2.12 | -2.06 | -1.72 | -2.06 | -1.70 | -2.15 | -2.41 | -1.12 | -2.14 | -2.08 | -1.67|
| full sent KL (full->waitk) |  |  | -3.25 | -3.49 | -2.71 | -2.53 | -3.10 | -2.11 | -2.29 | -1.00 | -1.14 | -1.44 | -2.49 | -1.61 | -2.24 | -3.89 | -1.66 | -2.13 | -3.74 | -1.58 | -2.50 | -0.90 | -1.87 | -1.75 | -1.65|
| dec-waitktgt |  |  | die | bürger@@ | bürger@@ | lichen | union | ist | zu@@ | tief@@ | st | beunruhi@@ | . | , | dass | sie | vielzahl | von | fragen | fragen | aufge@@ | worfen | wird | . | </s>|
| full sent tgt |  |  | die | amerikanische | bürger@@ | lichen | union | ist | ebenfalls | tief@@ | st | besorgt | , | , | dass | sie | vielzahl | von | fragen | fragen | aufge@@ | worfen | wird | . | </s>|
| ref | die | amerikanische | bürger@@ | rechts@@ | vereinigung | ( | ac@@ | l@@ | u | ) | ist | ebenfalls | zu@@ | tief@@ | st | besorgt | und | äuß@@ | ert | eine | reihe | von | datenschutz@@ | bedenken | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | and | while | congress | can | &apos;t | agree | on | whether | to | proceed | , | several | states | are | not | waiting | .|
| waitk tgt |  |  | und | während | der | kongre@@ | ss | sich | nicht | einigen | kann | , | ob | er | fort@@ | fahren | soll | , | warten | mehrere | staaten | nicht | . | </s>|
| waitk prob |  |  | 0.55 | 0.54 | 0.69 | 0.91 | 0.83 | 0.57 | 0.79 | 0.25 | 0.86 | 0.88 | 0.89 | 0.53 | 0.17 | 0.70 | 0.51 | 0.90 | 0.87 | 0.19 | 0.91 | 0.88 | 0.66 | 0.90|
| dec-waitk prob |  |  | 0.69 | 0.12 | 0.51 | 0.98 | 0.88 | 0.26 | 0.73 | 0.05 | 0.92 | 0.81 | 0.83 | 0.08 | 0.11 | 0.63 | 0.69 | 0.80 | 0.90 | 0.14 | 0.76 | 0.76 | 0.79 | 0.92|
| dec-waitk rank |  |  | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.59 | -3.71 | -2.93 | -0.94 | -1.59 | -2.93 | -2.40 | -2.32 | -1.40 | -2.08 | -2.02 | -3.49 | -2.30 | -2.33 | -1.81 | -2.03 | -1.27 | -3.56 | -2.31 | -2.31 | -1.83 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.89 | -1.96 | -2.26 | -1.56 | -1.46 | -2.24 | -2.08 | -2.38 | -1.84 | -1.78 | -1.63 | -2.32 | -3.50 | -2.33 | -2.18 | -1.64 | -1.46 | -3.46 | -1.32 | -1.56 | -2.18 | -1.71|
| full sent prob |  |  | 0.70 | 0.51 | 0.26 | 0.95 | 0.88 | 0.48 | 0.81 | 0.04 | 0.91 | 0.86 | 0.89 | 0.42 | 0.16 | 0.72 | 0.71 | 0.89 | 0.93 | 0.18 | 0.78 | 0.82 | 0.74 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.32 | -2.34 | -1.67 | -1.24 | -1.43 | -2.52 | -2.06 | -2.26 | -1.45 | -1.94 | -1.69 | -2.89 | -2.18 | -1.84 | -1.66 | -1.74 | -1.17 | -3.49 | -2.13 | -2.05 | -2.02 | -1.67|
| full sent KL (full->waitk) |  |  | -2.90 | -2.17 | -2.14 | -1.54 | -1.47 | -2.33 | -2.14 | -2.38 | -1.84 | -1.82 | -1.67 | -2.47 | -3.51 | -2.38 | -2.19 | -1.71 | -1.47 | -3.47 | -1.33 | -1.60 | -2.15 | -1.70|
| dec-waitktgt |  |  | und | der | der | kongre@@ | ss | nicht | nicht | einig | kann | , | ob | es | weiter@@ | fahren | soll | , | warten | nicht | staaten | nicht | . | </s>|
| full sent tgt |  |  | und | während | sich | kongre@@ | ss | sich | nicht | darüber | kann | , | ob | er | weiter@@ | fahren | soll | , | warten | mehrere | staaten | nicht | . | </s>|
| ref | doch | während | man | sich | im | kongre@@ | ss | nicht | auf | ein | vorgehen | einigen | kann | , | warten | mehrere | bundes@@ | staaten | nicht | länger | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | thousands | of | mo@@ | tori@@ | sts | have | already | taken | the | black | boxes | , | some | of | which | have | g@@ | ps | monitoring | , | for | a | test | drive | .|
| waitk tgt |  |  | tausende | von | auto@@ | fahr@@ | ern | haben | bereits | die | schwarzen | scha@@ | cht@@ | eln | genommen | , | von | denen | einige | g@@ | p@@ | s-@@ | überwachung | haben | , | für | ein | test@@ | lauf@@ | werk | . | </s>|
| waitk prob |  |  | 0.66 | 0.40 | 0.62 | 0.64 | 0.95 | 0.63 | 0.49 | 0.29 | 0.59 | 0.29 | 0.50 | 0.97 | 0.35 | 0.89 | 0.62 | 0.94 | 0.83 | 0.66 | 0.69 | 0.95 | 0.36 | 0.60 | 0.84 | 0.62 | 0.51 | 0.83 | 0.62 | 0.96 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.81 | 0.52 | 0.36 | 0.97 | 0.97 | 0.34 | 0.37 | 0.12 | 0.23 | 0.25 | 0.42 | 0.88 | 0.48 | 0.57 | 0.47 | 0.90 | 0.73 | 0.43 | 0.74 | 0.92 | 0.16 | 0.46 | 0.00 | 0.11 | 0.08 | 0.40 | 0.63 | 0.94 | 0.88 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 4 | 1 | 3 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.57 | -2.39 | -1.85 | -0.74 | -1.06 | -2.98 | -2.99 | -3.00 | -3.03 | -2.29 | -1.90 | -1.49 | -3.18 | -2.56 | -2.87 | -1.66 | -2.10 | -3.40 | -1.77 | -1.49 | -2.99 | -3.18 | -1.04 | -4.29 | -2.44 | -2.95 | -2.51 | -1.37 | -1.90 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.78 | -3.28 | -2.31 | -2.72 | -1.23 | -2.18 | -2.57 | -2.68 | -2.51 | -2.73 | -1.87 | -0.93 | -3.46 | -1.46 | -2.38 | -1.28 | -1.62 | -2.24 | -1.60 | -1.16 | -2.15 | -2.05 | -1.39 | -2.15 | -2.06 | -1.31 | -2.37 | -1.11 | -1.65 | -1.67|
| full sent prob |  |  | 0.74 | 0.22 | 0.58 | 0.93 | 0.94 | 0.74 | 0.41 | 0.54 | 0.12 | 0.12 | 0.84 | 0.92 | 0.05 | 0.85 | 0.52 | 0.93 | 0.72 | 0.37 | 0.77 | 0.93 | 0.15 | 0.60 | 0.86 | 0.10 | 0.12 | 0.49 | 0.67 | 0.94 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.08 | -2.16 | -1.98 | -0.91 | -1.31 | -2.43 | -2.87 | -2.91 | -3.95 | -3.14 | -1.10 | -1.38 | -3.31 | -1.89 | -2.58 | -1.41 | -2.09 | -3.43 | -1.49 | -1.40 | -3.57 | -2.51 | -1.89 | -2.46 | -2.21 | -2.50 | -2.30 | -1.36 | -1.82 | -1.67|
| full sent KL (full->waitk) |  |  | -2.74 | -3.22 | -2.41 | -2.71 | -1.20 | -2.34 | -2.58 | -2.75 | -2.45 | -2.68 | -1.94 | -0.96 | -3.37 | -1.67 | -2.40 | -1.30 | -1.61 | -2.21 | -1.62 | -1.17 | -2.17 | -2.12 | -1.99 | -2.20 | -2.09 | -1.37 | -2.39 | -1.12 | -1.65 | -1.67|
| dec-waitktgt |  |  | tausende | von | kraft@@ | fahr@@ | ern | sind | bereits | schwar@@ | bla@@ | bo@@ | ch@@ | eln | genommen | , | von | denen | einige | g@@ | p@@ | s-@@ | prüf@@ | haben | . | um | einen | test@@ | lauf@@ | werk | . | </s>|
| full sent tgt |  |  | tausende | auto@@ | auto@@ | fahr@@ | ern | haben | bereits | die | bla@@ | ki@@ | cht@@ | eln | , | , | von | denen | einige | g@@ | p@@ | s-@@ | überwach@@ | haben | , | um | einen | test@@ | lauf@@ | werk | . | </s>|
| ref | tausende | von | auto@@ | fahr@@ | ern | haben | die | fahr@@ | ten@@ | schrei@@ | ber | , | von | denen | einige | mit | g@@ | p@@ | s-@@ | überwachung | ausgestattet | sind | , | bereits | ge@@ | te@@ | stet | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | there | is | going | to | be | a | change | in | how | we | pay | these | taxes | .|
| waitk tgt |  |  | es | wird | eine | reihe | von | änderungen | geben | , | wie | wir | diese | steuern | zahlen | . | </s>|
| waitk prob |  |  | 0.38 | 0.71 | 0.18 | 0.08 | 0.58 | 0.37 | 0.71 | 0.88 | 0.61 | 0.78 | 0.84 | 0.82 | 0.62 | 0.81 | 0.91|
| dec-waitk prob |  |  | 0.27 | 0.69 | 0.08 | 0.00 | 0.81 | 0.25 | 0.92 | 0.04 | 0.01 | 0.45 | 0.79 | 0.91 | 0.57 | 0.79 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 24 | 0 | 1 | 0 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.36 | -2.23 | -5.14 | -5.33 | -1.77 | -1.14 | -1.18 | -2.52 | -2.02 | -3.17 | -2.00 | -1.26 | -2.28 | -2.01 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.70 | -2.31 | -4.44 | -5.26 | -3.11 | -3.80 | -2.22 | -1.14 | -2.34 | -1.81 | -1.64 | -1.95 | -1.68 | -1.91 | -1.69|
| full sent prob |  |  | 0.44 | 0.86 | 0.52 | 0.00 | 0.80 | 0.46 | 0.23 | 0.83 | 0.49 | 0.78 | 0.83 | 0.91 | 0.48 | 0.82 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 15 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.82 | -1.66 | -2.67 | -1.97 | -1.83 | -1.82 | -3.05 | -1.97 | -2.58 | -1.99 | -1.90 | -1.28 | -2.37 | -1.89 | -1.68|
| full sent KL (full->waitk) |  |  | -3.76 | -2.41 | -4.50 | -5.26 | -3.10 | -3.84 | -1.83 | -1.71 | -2.59 | -2.01 | -1.66 | -1.95 | -1.65 | -1.93 | -1.69|
| dec-waitktgt |  |  | es | wird | eine | gemeinsame | von | veränderungen | geben | . | </s> | wir | diese | steuern | zahlen | . | </s>|
| full sent tgt |  |  | es | wird | eine | änderung | von | änderungen | in | , | wie | wir | diese | steuern | zahlen | . | </s>|
| ref | die | art | und | weise | , | wie | wir | diese | steuern | zahlen | , | wird | sich | verändern | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | americans | don | &apos;t | buy | as | much | gas | as | they | used | to | .|
| waitk tgt |  |  | die | amerikaner | kaufen | nicht | so | viel | gas | , | wie | sie | es | früher | waren | . | </s>|
| waitk prob |  |  | 0.57 | 0.86 | 0.83 | 0.62 | 0.78 | 0.87 | 0.85 | 0.46 | 0.87 | 0.73 | 0.53 | 0.39 | 0.53 | 0.92 | 0.90|
| dec-waitk prob |  |  | 0.06 | 0.95 | 0.77 | 0.65 | 0.53 | 0.97 | 0.93 | 0.25 | 0.83 | 0.47 | 0.67 | 0.30 | 0.23 | 0.90 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -0.78 | -1.08 | -2.10 | -2.72 | -2.71 | -0.99 | -1.15 | -2.56 | -2.06 | -2.74 | -2.10 | -3.04 | -2.52 | -1.74 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.67 | -1.85 | -1.77 | -2.69 | -1.86 | -1.44 | -1.89 | -2.02 | -1.75 | -1.92 | -2.37 | -2.58 | -2.33 | -1.56 | -1.70|
| full sent prob |  |  | 0.68 | 0.87 | 0.86 | 0.66 | 0.55 | 0.95 | 0.93 | 0.33 | 0.87 | 0.45 | 0.71 | 0.36 | 0.23 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.17 | -1.72 | -1.62 | -2.21 | -2.11 | -1.15 | -1.20 | -1.90 | -1.71 | -2.74 | -1.96 | -2.83 | -2.94 | -1.70 | -1.69|
| full sent KL (full->waitk) |  |  | -2.90 | -1.79 | -1.83 | -2.70 | -1.88 | -1.42 | -1.89 | -2.06 | -1.78 | -1.90 | -2.38 | -2.60 | -2.32 | -1.57 | -1.70|
| dec-waitktgt |  |  | amerikaner | amerikaner | kaufen | nicht | so | viel | gas | wie | wie | sie | es | früher | hatten | . | </s>|
| full sent tgt |  |  | die | amerikaner | kaufen | nicht | so | viel | gas | wie | wie | sie | es | früher | hatten | . | </s>|
| ref | doch | in | amerika | wird | nicht | mehr | so | viel | get@@ | an@@ | kt | wie | früher | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | politicians | are | lo@@ | ath | to | raise | the | tax | even | one | pen@@ | ny | when | gas | prices | are | high | .|
| waitk tgt |  |  | politiker | sind | es | nicht | , | die | steuer | nur | einen | einzigen | pf@@ | en@@ | ni@@ | g | zu | erheben | , | wenn | die | ga@@ | sp@@ | reise | hoch | sind | . | </s>|
| waitk prob |  |  | 0.52 | 0.35 | 0.13 | 0.26 | 0.47 | 0.67 | 0.61 | 0.12 | 0.18 | 0.25 | 0.23 | 0.88 | 0.85 | 0.99 | 0.40 | 0.55 | 0.91 | 0.86 | 0.78 | 0.68 | 0.95 | 0.97 | 0.78 | 0.90 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.88 | 0.26 | 0.00 | 0.15 | 0.10 | 0.64 | 0.59 | 0.01 | 0.41 | 0.00 | 0.11 | 0.53 | 0.96 | 0.98 | 0.48 | 0.48 | 0.02 | 0.81 | 0.72 | 0.49 | 0.97 | 0.98 | 0.87 | 0.88 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 24 | 1 | 0 | 0 | 0 | 7 | 0 | 10 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.14 | -4.07 | -3.56 | -3.26 | -4.59 | -2.55 | -1.66 | -3.02 | -2.67 | -0.83 | -0.91 | -3.91 | -1.04 | -0.96 | -2.11 | -2.03 | -1.52 | -1.98 | -2.37 | -2.21 | -1.03 | -0.96 | -1.57 | -1.81 | -1.73 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.41 | -3.96 | -4.44 | -3.76 | -3.44 | -2.64 | -2.08 | -3.97 | -3.62 | -4.17 | -4.52 | -1.22 | -1.99 | -0.93 | -2.31 | -1.91 | -0.95 | -1.73 | -2.09 | -2.21 | -1.24 | -1.08 | -2.13 | -1.60 | -1.63 | -1.69|
| full sent prob |  |  | 0.40 | 0.34 | 0.02 | 0.11 | 0.05 | 0.59 | 0.56 | 0.01 | 0.57 | 0.00 | 0.02 | 0.80 | 0.94 | 0.99 | 0.31 | 0.26 | 0.92 | 0.86 | 0.84 | 0.59 | 0.97 | 0.98 | 0.87 | 0.87 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 5 | 2 | 2 | 0 | 0 | 11 | 0 | 6 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.48 | -3.37 | -4.34 | -4.08 | -5.05 | -2.75 | -1.98 | -3.14 | -2.42 | -0.90 | -0.30 | -2.29 | -1.27 | -0.95 | -1.93 | -2.37 | -1.57 | -1.82 | -1.85 | -2.22 | -1.01 | -0.96 | -1.57 | -1.87 | -1.70 | -1.65|
| full sent KL (full->waitk) |  |  | -2.28 | -3.98 | -4.44 | -3.75 | -3.41 | -2.61 | -2.06 | -3.97 | -3.64 | -4.17 | -4.51 | -1.42 | -1.97 | -0.93 | -2.32 | -1.85 | -1.63 | -1.77 | -2.17 | -2.27 | -1.24 | -1.08 | -2.13 | -1.60 | -1.64 | -1.68|
| dec-waitktgt |  |  | politiker | sind | ung@@ | ung@@ | , | die | steuer | zu | einen | c@@ | c@@ | en@@ | ni@@ | g | zu | erheben | . | wenn | die | ga@@ | sp@@ | reise | hoch | sind | . | </s>|
| full sent tgt |  |  | politiker | sind | nicht | schwer | einmal | die | steuer | zu | einen | c@@ | c@@ | en@@ | ni@@ | g | anzu@@ | erhöhen | , | wenn | die | ga@@ | sp@@ | reise | hoch | sind | . | </s>|
| ref | politiker | wagen | bei | hohen | sp@@ | rit@@ | preisen | nicht | , | die | steuer | auch | nur | um | einen | c@@ | ent | anzu@@ | heben | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | &quot; | this | works | out | as | the | most | logical | alternative | over | the | long | term | , | &quot; | he | said | .|
| waitk tgt |  |  | &quot; | das | funktioniert | wie | die | logi@@ | sch@@ | ste | alternative | über | die | dauer | , | &quot; | sagte | er | . | </s>|
| waitk prob |  |  | 0.45 | 0.37 | 0.48 | 0.28 | 0.38 | 0.77 | 0.95 | 0.92 | 0.89 | 0.30 | 0.47 | 0.23 | 0.39 | 0.90 | 0.71 | 0.88 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.09 | 0.32 | 0.21 | 0.54 | 0.21 | 0.52 | 0.96 | 0.81 | 0.83 | 0.27 | 0.42 | 0.06 | 0.06 | 0.48 | 0.03 | 0.52 | 0.88 | 0.92|
| dec-waitk rank |  |  | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.82 | -3.84 | -3.39 | -2.80 | -2.68 | -3.04 | -1.08 | -1.87 | -2.08 | -3.64 | -2.97 | -4.13 | -2.50 | -2.04 | -2.06 | -4.18 | -1.82 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.43 | -3.34 | -3.20 | -3.45 | -2.75 | -1.68 | -1.18 | -1.31 | -1.54 | -3.39 | -2.52 | -3.33 | -2.53 | -1.35 | -1.70 | -1.54 | -1.80 | -1.65|
| full sent prob |  |  | 0.51 | 0.41 | 0.45 | 0.00 | 0.61 | 0.15 | 0.98 | 0.93 | 0.90 | 0.07 | 0.49 | 0.05 | 0.04 | 0.83 | 0.83 | 0.81 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 20 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 3 | 4 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.99 | -2.75 | -3.27 | -2.82 | -2.36 | -4.81 | -0.92 | -1.40 | -1.47 | -2.79 | -2.54 | -3.59 | -2.88 | -2.10 | -1.63 | -2.32 | -1.67 | -1.65|
| full sent KL (full->waitk) |  |  | -3.58 | -3.39 | -3.30 | -3.32 | -2.79 | -1.45 | -1.20 | -1.41 | -1.59 | -3.39 | -2.55 | -3.36 | -2.49 | -1.62 | -2.17 | -1.76 | -1.82 | -1.64|
| dec-waitktgt |  |  | das | das | funktioniert | wie | das | logi@@ | sch@@ | ste | alternative | über | die | zukunft | &quot; | &quot; | </s> | er | . | </s>|
| full sent tgt |  |  | &quot; | das | funktioniert | auf | die | lo@@ | sch@@ | ste | alternative | auf | die | lange | &quot; | &quot; | sagte | er | . | </s>|
| ref | „ | das | stellt | die | langfristig | sinn@@ | voll@@ | ste | alternative | dar | \“ | , | sagte | er | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | won@@ | ks | call | it | a | mil@@ | e@@ | ag@@ | e-@@ | based | user | fee | .|
| waitk tgt |  |  | fragt | sich | , | ob | es | ein | mei@@ | len@@ | basi@@ | erter | benutzer@@ | beitrag | ist | . | </s>|
| waitk prob |  |  | 0.17 | 0.79 | 0.69 | 0.18 | 0.37 | 0.38 | 0.78 | 0.99 | 0.77 | 0.44 | 0.23 | 0.30 | 0.60 | 0.89 | 0.90|
| dec-waitk prob |  |  | 0.01 | 0.36 | 0.67 | 0.54 | 0.50 | 0.20 | 0.65 | 0.99 | 0.00 | 0.48 | 0.15 | 0.26 | 0.72 | 0.90 | 0.92|
| dec-waitk rank |  |  | 9 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.39 | -3.22 | -2.10 | -1.91 | -2.89 | -3.25 | -2.76 | -0.88 | -0.49 | -1.76 | -4.31 | -2.93 | -1.99 | -1.69 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.49 | -1.70 | -2.48 | -3.58 | -2.83 | -2.59 | -2.21 | -0.92 | -1.59 | -1.85 | -3.29 | -3.93 | -2.33 | -1.74 | -1.70|
| full sent prob |  |  | 0.00 | 0.67 | 0.80 | 0.28 | 0.34 | 0.04 | 0.43 | 0.97 | 0.62 | 0.24 | 0.28 | 0.18 | 0.71 | 0.88 | 0.91|
| full sent rank |  |  | 23 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.06 | -2.16 | -2.07 | -3.42 | -2.87 | -2.40 | -3.04 | -1.05 | -2.77 | -1.74 | -3.65 | -3.26 | -2.04 | -1.78 | -1.65|
| full sent KL (full->waitk) |  |  | -4.46 | -1.91 | -2.54 | -3.54 | -2.79 | -2.61 | -2.07 | -0.90 | -1.98 | -1.84 | -3.32 | -3.91 | -2.33 | -1.73 | -1.69|
| dec-waitktgt |  |  | won@@ | sich | , | ob | es | mi@@ | mei@@ | len@@ | stein | erter | benutzer@@ | beitrag | ist | . | </s>|
| full sent tgt |  |  | man | sich | , | ob | es | eine | mei@@ | len@@ | basi@@ | ertes | benutzer@@ | beitrag | ist | . | </s>|
| ref | büro@@ | kraten | be@@ | zeichnen | es | als | mei@@ | len@@ | basi@@ | erte | benutz@@ | ergeb@@ | ü@@ | hr | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | u.s. | sen@@ | ate | approved | a | $ | 9@@ | 0-@@ | million | pilot | project | last | year | that | would | have | involved | about | 10@@ | ,000 | cars | .|
| waitk tgt |  |  | der | us-@@ | sen@@ | at | genehmi@@ | gte | ein | $ | 9@@ | 0-@@ | milli@@ | on@@ | en-@@ | pi@@ | lot@@ | projekt | im | vergangenen | jahr | , | das | etwa | 10@@ | .000 | autos | beteiligt | gewesen | wäre | . | </s>|
| waitk prob |  |  | 0.28 | 0.58 | 0.98 | 0.93 | 0.29 | 0.91 | 0.28 | 0.40 | 0.63 | 0.91 | 0.60 | 0.59 | 0.90 | 0.85 | 0.93 | 0.91 | 0.72 | 0.45 | 0.94 | 0.82 | 0.48 | 0.22 | 0.89 | 0.90 | 0.71 | 0.28 | 0.70 | 0.47 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.14 | 0.28 | 0.95 | 0.94 | 0.57 | 0.81 | 0.02 | 0.04 | 0.53 | 0.78 | 0.45 | 0.85 | 0.72 | 0.04 | 0.98 | 0.89 | 0.45 | 0.48 | 0.93 | 0.78 | 0.28 | 0.27 | 0.87 | 0.89 | 0.66 | 0.11 | 0.55 | 0.72 | 0.91 | 0.92|
| dec-waitk rank |  |  | 1 | 1 | 0 | 0 | 0 | 0 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.12 | -2.18 | -1.17 | -1.27 | -2.17 | -1.65 | -2.37 | -3.24 | -2.41 | -1.73 | -2.29 | -1.13 | -1.59 | -4.22 | -0.96 | -1.46 | -2.02 | -1.55 | -1.49 | -2.07 | -2.20 | -2.66 | -1.71 | -1.43 | -1.90 | -3.85 | -2.66 | -1.60 | -1.63 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.54 | -2.20 | -1.00 | -1.32 | -3.05 | -1.28 | -3.09 | -3.79 | -2.03 | -1.32 | -1.93 | -1.70 | -1.08 | -1.25 | -1.30 | -1.29 | -1.98 | -1.71 | -1.30 | -2.12 | -2.30 | -3.35 | -1.29 | -1.33 | -1.76 | -3.67 | -1.99 | -2.40 | -1.64 | -1.67|
| full sent prob |  |  | 0.55 | 0.65 | 0.95 | 0.92 | 0.51 | 0.92 | 0.09 | 0.04 | 0.68 | 0.83 | 0.37 | 0.38 | 0.97 | 0.81 | 0.90 | 0.90 | 0.80 | 0.44 | 0.94 | 0.86 | 0.44 | 0.13 | 0.90 | 0.87 | 0.80 | 0.44 | 0.55 | 0.71 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.84 | -2.04 | -1.29 | -1.41 | -2.23 | -1.35 | -1.47 | -4.76 | -2.29 | -1.72 | -2.32 | -1.54 | -0.92 | -2.21 | -1.45 | -1.50 | -1.75 | -1.56 | -1.38 | -1.85 | -2.59 | -3.60 | -1.52 | -1.54 | -1.44 | -3.22 | -2.58 | -1.64 | -1.80 | -1.65|
| full sent KL (full->waitk) |  |  | -3.59 | -2.35 | -0.99 | -1.31 | -3.05 | -1.37 | -3.07 | -3.78 | -2.09 | -1.35 | -1.90 | -1.58 | -1.26 | -1.80 | -1.24 | -1.30 | -2.17 | -1.72 | -1.31 | -2.18 | -2.41 | -3.31 | -1.31 | -1.32 | -1.83 | -3.74 | -2.00 | -2.40 | -1.62 | -1.67|
| dec-waitktgt |  |  | die | amerikanische | sen@@ | at | genehmi@@ | gte | 9@@ | volumen | 9@@ | 0-@@ | milli@@ | on@@ | en-@@ | dollar | lot@@ | projekt | im | vergangenen | jahr | , | an | rund | 10@@ | .000 | autos | umfassen | gewesen | wäre | . | </s>|
| full sent tgt |  |  | der | us-@@ | sen@@ | at | genehmi@@ | gte | im | pi@@ | 9@@ | 0-@@ | millionen | on | en-@@ | pi@@ | lot@@ | projekt | im | letzten | jahr | , | das | rund | 10@@ | .000 | autos | beteiligt | gewesen | wäre | . | </s>|
| ref | der | us-@@ | sen@@ | at | genehmi@@ | gte | letz@@ | tes | jahr | ein | 90 | millionen | dollar | teu@@ | res | pi@@ | lot@@ | projekt | , | das | 10@@ | .000 | autos | umfasst | hätte | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | several | states | and | cities | are | nonetheless | moving | ahead | on | their | own | .|
| waitk tgt |  |  | mehrere | staaten | und | städte | bewegen | sich | jedoch | auf | ihrem | eigenen | weg | vor@@ | an | . | </s>|
| waitk prob |  |  | 0.36 | 0.77 | 0.88 | 0.87 | 0.50 | 0.92 | 0.29 | 0.17 | 0.18 | 0.59 | 0.78 | 0.24 | 0.84 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.85 | 0.82 | 0.87 | 0.96 | 0.83 | 0.84 | 0.18 | 0.23 | 0.02 | 0.26 | 0.44 | 0.79 | 0.81 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 8 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.07 | -1.64 | -1.85 | -1.05 | -1.40 | -2.13 | -2.96 | -2.95 | -3.35 | -3.21 | -3.16 | -1.18 | -1.79 | -1.64 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.35 | -1.93 | -1.81 | -1.73 | -3.00 | -1.52 | -3.04 | -3.89 | -3.13 | -2.10 | -1.34 | -3.40 | -1.38 | -1.59 | -1.69|
| full sent prob |  |  | 0.21 | 0.79 | 0.90 | 0.94 | 0.06 | 0.87 | 0.28 | 0.01 | 0.01 | 0.44 | 0.31 | 0.63 | 0.85 | 0.91 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 4 | 9 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.49 | -1.78 | -1.69 | -1.22 | -3.59 | -1.81 | -2.77 | -1.81 | -2.75 | -3.63 | -3.65 | -1.58 | -1.47 | -1.67 | -1.70|
| full sent KL (full->waitk) |  |  | -3.17 | -1.91 | -1.83 | -1.71 | -2.69 | -1.54 | -3.07 | -3.82 | -3.14 | -2.14 | -1.26 | -3.39 | -1.41 | -1.58 | -1.68|
| dec-waitktgt |  |  | mehrere | staaten | und | städte | bewegen | sich | trotzdem | auf | eigene | weg | weg | vor@@ | an | . | </s>|
| full sent tgt |  |  | mehrere | staaten | und | städte | machen | sich | jedoch | all@@ | eigene | eigenen | weg | vor@@ | an | . | </s>|
| ref | mehrere | bundes@@ | staaten | und | groß@@ | städte | bewegen | sich | nicht@@ | s@@ | de@@ | st@@ | ot@@ | ro@@ | tz | auf | eigene | fau@@ | st | in | diese | richtung | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | most | e@@ | ager | is | o@@ | reg@@ | on | , | which | is | en@@ | li@@ | sting | 5@@ | ,000 | drivers | in | the | country | &apos;s | biggest | experim@@ | ent | .|
| waitk tgt |  |  | die | ei@@ | fri@@ | gste | ist | ore@@ | g@@ | on | , | die | mit | der | auf@@ | li@@ | stung | von | 5@@ | .000 | fahr@@ | ern | in | der | größten | experi@@ | ment@@ | ellen | zeit | des | landes | . | </s>|
| waitk prob |  |  | 0.31 | 0.48 | 0.89 | 0.56 | 0.52 | 0.96 | 0.97 | 0.97 | 0.87 | 0.46 | 0.15 | 0.13 | 0.06 | 0.46 | 0.96 | 0.81 | 0.84 | 0.77 | 0.37 | 0.94 | 0.57 | 0.29 | 0.82 | 0.54 | 0.31 | 0.36 | 0.05 | 0.86 | 0.92 | 0.32 | 0.90|
| dec-waitk prob |  |  | 0.57 | 0.25 | 0.37 | 0.14 | 0.61 | 0.49 | 0.98 | 0.96 | 0.77 | 0.18 | 0.00 | 0.18 | 0.08 | 0.34 | 0.45 | 0.87 | 0.91 | 0.57 | 0.26 | 0.56 | 0.39 | 0.15 | 0.84 | 0.29 | 0.15 | 0.31 | 0.00 | 0.73 | 0.88 | 0.85 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 18 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 38 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.41 | -4.15 | -4.68 | -5.58 | -3.21 | -3.55 | -1.03 | -1.16 | -2.16 | -3.34 | -1.24 | -3.76 | -3.46 | -4.32 | -2.92 | -1.62 | -1.39 | -2.60 | -3.01 | -3.63 | -2.67 | -2.95 | -1.81 | -3.06 | -3.05 | -1.70 | -3.40 | -2.04 | -1.78 | -1.63 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.69 | -3.58 | -0.95 | -1.69 | -3.81 | -0.72 | -1.08 | -1.11 | -1.81 | -2.77 | -4.51 | -4.78 | -5.51 | -2.00 | -0.70 | -1.98 | -1.91 | -1.35 | -3.44 | -0.97 | -2.23 | -2.91 | -1.79 | -2.92 | -3.17 | -4.01 | -4.55 | -1.66 | -1.42 | -3.44 | -1.69|
| full sent prob |  |  | 0.08 | 0.08 | 0.94 | 0.70 | 0.44 | 0.66 | 0.97 | 0.95 | 0.85 | 0.08 | 0.01 | 0.01 | 0.29 | 0.29 | 0.98 | 0.84 | 0.82 | 0.68 | 0.35 | 0.97 | 0.24 | 0.14 | 0.80 | 0.55 | 0.20 | 0.54 | 0.00 | 0.79 | 0.89 | 0.04 | 0.90|
| full sent rank |  |  | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 7 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 1 | 0 | 32 | 0 | 0 | 5 | 0|
| full sent KL (waitk->full) |  |  | -2.36 | -4.37 | -1.12 | -2.18 | -3.79 | -2.44 | -1.05 | -1.29 | -1.95 | -2.86 | -2.68 | -1.30 | -3.40 | -2.74 | -1.02 | -1.80 | -2.01 | -1.86 | -3.61 | -1.00 | -3.29 | -2.87 | -2.12 | -2.48 | -3.12 | -1.64 | -3.49 | -2.10 | -1.76 | -4.48 | -1.69|
| full sent KL (full->waitk) |  |  | -3.58 | -3.52 | -1.37 | -1.94 | -3.74 | -0.85 | -1.08 | -1.10 | -1.86 | -2.77 | -4.51 | -4.74 | -5.51 | -2.01 | -1.13 | -1.96 | -1.84 | -1.42 | -3.46 | -1.29 | -2.16 | -2.88 | -1.76 | -3.03 | -3.18 | -4.07 | -4.54 | -1.71 | -1.43 | -3.24 | -1.69|
| dec-waitktgt |  |  | die | ei@@ | fri@@ | gsten | ist | ore@@ | g@@ | on | , | nämlich | en@@ | dem | 5@@ | li@@ | stung | von | 5@@ | .000 | fahr@@ | ern | in | dem | größten | experi@@ | ment | elle | entwicklung | des | landes | . | </s>|
| full sent tgt |  |  | am | meisten | fri@@ | gste | ist | ore@@ | g@@ | on | , | das | 5@@ | 5@@ | auf@@ | li@@ | stung | von | 5@@ | .000 | fahr@@ | ern | im | das | größten | experi@@ | ment | ellen | entwicklung | des | landes | ist | </s>|
| ref | am | enga@@ | gi@@ | er@@ | testen | ist | ore@@ | g@@ | on | , | das | derzeit | 5@@ | .000 | fahrer | für | das | größte | experi@@ | ment | des | landes | an@@ | wir@@ | bt | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | those | drivers | will | soon | pay | the | mil@@ | e@@ | age | fees | instead | of | gas | taxes | to | the | state | .|
| waitk tgt |  |  | diese | fahrer | zahlen | bald | den | mei@@ | len@@ | betrag | anstatt | den | ga@@ | s-@@ | steuern | an | den | staat | . | </s>|
| waitk prob |  |  | 0.41 | 0.74 | 0.29 | 0.19 | 0.42 | 0.72 | 0.96 | 0.19 | 0.28 | 0.19 | 0.25 | 0.22 | 0.41 | 0.52 | 0.82 | 0.88 | 0.67 | 0.90|
| dec-waitk prob |  |  | 0.18 | 0.64 | 0.05 | 0.20 | 0.04 | 0.93 | 0.87 | 0.23 | 0.00 | 0.07 | 0.15 | 0.10 | 0.27 | 0.00 | 0.84 | 0.91 | 0.90 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 10 | 1 | 2 | 1 | 0 | 5 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.59 | -2.55 | -1.66 | -3.41 | -2.78 | -1.06 | -1.27 | -3.65 | -2.09 | -2.78 | -2.86 | -4.39 | -3.64 | -2.17 | -1.90 | -1.48 | -1.49 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.46 | -2.09 | -2.36 | -4.05 | -2.49 | -2.49 | -0.95 | -4.25 | -2.50 | -3.97 | -4.68 | -4.30 | -3.12 | -2.37 | -1.81 | -1.71 | -2.04 | -1.71|
| full sent prob |  |  | 0.47 | 0.76 | 0.11 | 0.29 | 0.01 | 0.83 | 0.91 | 0.17 | 0.27 | 0.10 | 0.23 | 0.15 | 0.45 | 0.77 | 0.91 | 0.92 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 0 | 6 | 0 | 0 | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.30 | -1.95 | -1.87 | -2.72 | -2.78 | -1.50 | -1.30 | -3.15 | -2.03 | -3.00 | -2.85 | -4.21 | -3.18 | -1.92 | -1.52 | -1.44 | -1.46 | -1.66|
| full sent KL (full->waitk) |  |  | -3.54 | -2.16 | -2.36 | -4.07 | -2.45 | -2.43 | -0.98 | -4.25 | -2.62 | -3.97 | -4.70 | -4.31 | -3.19 | -2.71 | -1.85 | -1.71 | -2.04 | -1.71|
| dec-waitktgt |  |  | die | fahrer | werden | in | die | mei@@ | len@@ | betrag | . | der | gas@@ | se@@ | steuern | . | den | staat | . | </s>|
| full sent tgt |  |  | diese | fahrer | werden | bald | die | mei@@ | len@@ | preis | anstatt | der | gas@@ | s-@@ | steuern | an | den | staat | . | </s>|
| ref | diese | fahrer | werden | bald | die | mei@@ | len@@ | gebühren | statt | der | miner@@ | al@@ | öl@@ | steuer | an | den | bundes@@ | staat | zahlen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | il@@ | lin@@ | o@@ | is | is | trying | it | on | a | limited | basis | with | tr@@ | uc@@ | ks | .|
| waitk tgt |  |  | il@@ | lin@@ | o@@ | is | versucht | es | auf | begrenz@@ | ter | basis | mit | l@@ | kw | . | </s>|
| waitk prob |  |  | 0.40 | 0.95 | 0.94 | 0.96 | 0.72 | 0.59 | 0.44 | 0.19 | 0.71 | 0.44 | 0.77 | 0.42 | 0.62 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.36 | 0.98 | 0.94 | 0.97 | 0.10 | 0.33 | 0.22 | 0.03 | 0.24 | 0.73 | 0.52 | 0.41 | 0.09 | 0.85 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.83 | -1.00 | -1.36 | -1.11 | -3.12 | -3.58 | -4.43 | -2.36 | -4.16 | -1.42 | -3.25 | -2.73 | -3.58 | -2.01 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.69 | -1.23 | -1.38 | -1.19 | -1.82 | -2.39 | -3.50 | -3.40 | -1.56 | -3.61 | -1.95 | -2.96 | -1.24 | -1.73 | -1.68|
| full sent prob |  |  | 0.66 | 0.92 | 0.92 | 0.95 | 0.51 | 0.54 | 0.29 | 0.27 | 0.85 | 0.85 | 0.79 | 0.68 | 0.16 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.37 | -1.54 | -1.49 | -1.25 | -3.11 | -2.37 | -3.23 | -2.67 | -1.45 | -1.31 | -2.06 | -1.34 | -1.04 | -1.75 | -1.68|
| full sent KL (full->waitk) |  |  | -3.79 | -1.18 | -1.37 | -1.17 | -2.07 | -2.50 | -3.54 | -3.44 | -1.90 | -3.64 | -2.12 | -3.04 | -1.39 | -1.77 | -1.67|
| dec-waitktgt |  |  | il@@ | lin@@ | o@@ | is | </s> | es | auf | eine | ter | basis | mit | l@@ | k@@ | . | </s>|
| full sent tgt |  |  | il@@ | lin@@ | o@@ | is | versucht | es | auf | einer | ter | basis | mit | l@@ | k@@ | . | </s>|
| ref | il@@ | lin@@ | o@@ | is | te@@ | stet | es | in | eingeschrän@@ | k@@ | tem | maße | mit | l@@ | k@@ | ws | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | if | you | can | do | that | , | kh@@ | an | said | , | the | public | gets | more | comfortable | .|
| waitk tgt |  |  | wenn | sie | das | tun | können | , | sagte | k@@ | h@@ | an | , | die | öffentlichkeit | wird | komfort@@ | ab@@ | ler | . | </s>|
| waitk prob |  |  | 0.53 | 0.58 | 0.50 | 0.38 | 0.72 | 0.90 | 0.60 | 0.95 | 0.96 | 0.95 | 0.89 | 0.30 | 0.70 | 0.37 | 0.26 | 0.95 | 0.95 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.75 | 0.33 | 0.42 | 0.54 | 0.76 | 0.89 | 0.64 | 0.92 | 0.98 | 0.95 | 0.59 | 0.68 | 0.68 | 0.11 | 0.31 | 0.91 | 0.97 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.04 | -3.41 | -2.96 | -2.65 | -1.73 | -1.75 | -1.99 | -1.37 | -0.99 | -1.24 | -2.51 | -2.44 | -2.52 | -3.27 | -3.22 | -1.57 | -1.07 | -1.62 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.15 | -2.09 | -2.56 | -3.13 | -2.18 | -1.66 | -2.36 | -1.22 | -1.05 | -1.27 | -1.46 | -3.59 | -2.10 | -3.58 | -3.39 | -1.19 | -1.23 | -1.70 | -1.71|
| full sent prob |  |  | 0.46 | 0.24 | 0.55 | 0.36 | 0.78 | 0.90 | 0.44 | 0.93 | 0.95 | 0.95 | 0.88 | 0.33 | 0.85 | 0.40 | 0.35 | 0.94 | 0.97 | 0.91 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.78 | -3.14 | -2.34 | -3.06 | -1.80 | -1.72 | -2.52 | -1.33 | -1.17 | -1.32 | -1.73 | -2.82 | -1.80 | -3.08 | -2.85 | -1.36 | -1.08 | -1.64 | -1.70|
| full sent KL (full->waitk) |  |  | -3.02 | -2.06 | -2.61 | -3.08 | -2.19 | -1.67 | -2.26 | -1.23 | -1.03 | -1.27 | -1.67 | -3.54 | -2.19 | -3.68 | -3.40 | -1.21 | -1.23 | -1.70 | -1.70|
| dec-waitktgt |  |  | wenn | sie | das | tun | können | , | sagte | k@@ | h@@ | an | , | die | öffentlichkeit | werde | komfort@@ | ab@@ | ler | . | </s>|
| full sent tgt |  |  | wenn | sie | das | tun | können | , | sagte | k@@ | h@@ | an | , | die | öffentlichkeit | wird | komfort@@ | ab@@ | ler | . | </s>|
| ref | damit | , | so | k@@ | h@@ | an | , | wäre | auch | die | öffentlichkeit | beru@@ | hi@@ | gter | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | hun@@ | t | for | that | technology | has | led | some | state | agencies | to | a | small | california | star@@ | tup | called | true | mil@@ | e@@ | age | .|
| waitk tgt |  |  | die | jag@@ | d | auf | diese | technologie | hat | einige | staatliche | behörden | zu | einem | kleinen | kali@@ | for@@ | nischen | start | namens | tru@@ | e | mi@@ | le@@ | age | geführt | . | </s>|
| waitk prob |  |  | 0.49 | 0.60 | 0.96 | 0.48 | 0.87 | 0.73 | 0.74 | 0.41 | 0.64 | 0.28 | 0.43 | 0.48 | 0.86 | 0.76 | 0.96 | 0.83 | 0.34 | 0.42 | 0.91 | 0.93 | 0.64 | 0.81 | 0.98 | 0.84 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.74 | 0.96 | 0.94 | 0.37 | 0.82 | 0.72 | 0.67 | 0.47 | 0.81 | 0.39 | 0.29 | 0.25 | 0.88 | 0.90 | 1.00 | 0.86 | 0.42 | 0.01 | 0.40 | 0.94 | 0.66 | 0.87 | 0.81 | 0.86 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.33 | -0.76 | -1.35 | -1.85 | -1.89 | -1.72 | -2.52 | -2.98 | -1.57 | -1.96 | -3.04 | -2.77 | -1.55 | -1.35 | -0.84 | -1.29 | -2.42 | -2.80 | -2.98 | -1.32 | -1.69 | -1.47 | -2.40 | -1.65 | -1.71 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.58 | -2.61 | -1.15 | -2.30 | -1.61 | -1.76 | -1.87 | -3.24 | -2.64 | -2.90 | -2.80 | -2.30 | -1.70 | -2.16 | -1.18 | -1.54 | -2.44 | -2.93 | -0.91 | -1.39 | -2.23 | -1.74 | -0.89 | -1.60 | -1.66 | -1.67|
| full sent prob |  |  | 0.50 | 0.84 | 0.94 | 0.26 | 0.86 | 0.77 | 0.52 | 0.83 | 0.67 | 0.26 | 0.50 | 0.81 | 0.87 | 0.96 | 0.99 | 0.91 | 0.73 | 0.50 | 0.53 | 0.94 | 0.50 | 0.83 | 0.83 | 0.87 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.37 | -1.35 | -1.33 | -1.94 | -1.72 | -1.48 | -2.76 | -1.48 | -2.27 | -1.89 | -2.65 | -1.56 | -1.63 | -0.89 | -0.95 | -1.30 | -1.39 | -2.53 | -2.40 | -1.31 | -1.91 | -1.69 | -2.26 | -1.44 | -1.67 | -1.63|
| full sent KL (full->waitk) |  |  | -3.48 | -2.56 | -1.15 | -2.28 | -1.63 | -1.79 | -1.79 | -3.36 | -2.57 | -2.87 | -2.86 | -2.44 | -1.70 | -2.20 | -1.17 | -1.57 | -2.50 | -3.06 | -1.00 | -1.40 | -2.16 | -1.71 | -0.90 | -1.61 | -1.66 | -1.67|
| dec-waitktgt |  |  | die | jag@@ | d | nach | diese | technologie | hat | einige | staatliche | behörden | in | einer | kleinen | kali@@ | for@@ | nischen | start | geführt | tru@@ | e | mi@@ | le@@ | age | geführt | . | </s>|
| full sent tgt |  |  | die | jag@@ | d | nach | diese | technologie | hat | einige | staatliche | agenturen | zu | einem | kleinen | kali@@ | for@@ | nischen | start | namens | tru@@ | e | mi@@ | le@@ | age | geführt | . | </s>|
| ref | die | jag@@ | d | nach | dieser | technologie | hat | einige | behörden | zu | einem | kleinen | star@@ | tu@@ | p-@@ | unternehmen | namens | tru@@ | e | mi@@ | le@@ | age | in | kali@@ | for@@ | nien | geführt | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | firm | was | not | originally | in | the | business | of | helping | states | tax | drivers | .|
| waitk tgt |  |  | die | firma | war | ursprünglich | nicht | im | geschäft | , | staaten | zu | helfen | steuer@@ | fahrer | . | </s>|
| waitk prob |  |  | 0.32 | 0.59 | 0.27 | 0.64 | 0.80 | 0.52 | 0.44 | 0.59 | 0.56 | 0.31 | 0.50 | 0.65 | 0.10 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.23 | 0.83 | 0.59 | 0.76 | 0.78 | 0.26 | 0.61 | 0.08 | 0.07 | 0.19 | 0.86 | 0.05 | 0.03 | 0.84 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 2 | 6 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.20 | -1.42 | -2.56 | -1.77 | -2.06 | -3.70 | -2.06 | -1.99 | -2.73 | -2.91 | -1.28 | -2.63 | -5.01 | -2.06 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.95 | -2.67 | -3.58 | -2.45 | -2.02 | -2.01 | -3.09 | -2.44 | -2.28 | -2.55 | -2.71 | -1.68 | -5.03 | -1.65 | -1.70|
| full sent prob |  |  | 0.30 | 0.58 | 0.47 | 0.82 | 0.88 | 0.10 | 0.41 | 0.67 | 0.05 | 0.19 | 0.90 | 0.34 | 0.04 | 0.83 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 | 4 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.24 | -2.30 | -2.90 | -1.52 | -1.61 | -2.81 | -3.46 | -2.61 | -2.81 | -2.43 | -1.07 | -2.32 | -5.28 | -1.99 | -1.65|
| full sent KL (full->waitk) |  |  | -3.94 | -2.57 | -3.54 | -2.48 | -2.08 | -1.91 | -3.02 | -2.70 | -2.27 | -2.56 | -2.72 | -1.87 | -5.03 | -1.64 | -1.69|
| dec-waitktgt |  |  | das | firma | war | ursprünglich | nicht | im | geschäft | mit | den | steuer@@ | helfen | . | pflich@@ | . | </s>|
| full sent tgt |  |  | die | firma | war | ursprünglich | nicht | damit | geschäft | , | den | steuer@@ | helfen | , | trei@@ | . | </s>|
| ref | die | firma | ist | ursprünglich | nicht | ange@@ | treten | , | um | bundes@@ | staaten | bei | der | besteuerung | von | auto@@ | fahr@@ | ern | zu | helfen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | there | have | been | some | big | mistakes | in | some | of | these | state | pilot | programs | .|
| waitk tgt |  |  | seit | dem | letzten | jahr | gab | es | in | einigen | dieser | staatlichen | pi@@ | lot@@ | programme | einige | große | fehler | . | </s>|
| waitk prob |  |  | 0.60 | 0.23 | 0.09 | 0.08 | 0.38 | 0.90 | 0.32 | 0.70 | 0.88 | 0.50 | 0.86 | 0.91 | 0.74 | 0.33 | 0.66 | 0.89 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.01 | 0.01 | 0.01 | 0.10 | 0.49 | 0.91 | 0.05 | 0.79 | 0.79 | 0.33 | 0.89 | 0.97 | 0.72 | 0.24 | 0.69 | 0.93 | 0.90 | 0.91|
| dec-waitk rank |  |  | 8 | 7 | 16 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.65 | -3.09 | -4.27 | -4.58 | -2.49 | -1.65 | -2.67 | -2.00 | -2.07 | -2.76 | -1.38 | -1.03 | -2.13 | -3.22 | -2.20 | -1.31 | -1.69 | -1.64|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.15 | -3.87 | -4.65 | -5.32 | -2.59 | -1.70 | -2.66 | -2.20 | -1.50 | -2.94 | -1.82 | -1.45 | -2.33 | -2.87 | -2.49 | -1.61 | -1.67 | -1.70|
| full sent prob |  |  | 0.00 | 0.12 | 0.01 | 0.23 | 0.02 | 0.91 | 0.16 | 0.44 | 0.55 | 0.56 | 0.87 | 0.97 | 0.75 | 0.20 | 0.66 | 0.91 | 0.89 | 0.91|
| full sent rank |  |  | 80 | 0 | 31 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.85 | -4.36 | -4.54 | -4.81 | -4.43 | -1.65 | -4.28 | -3.48 | -3.37 | -2.90 | -1.56 | -1.02 | -2.04 | -3.61 | -2.40 | -1.45 | -1.74 | -1.67|
| full sent KL (full->waitk) |  |  | -2.12 | -3.88 | -4.66 | -5.32 | -2.44 | -1.70 | -2.59 | -2.00 | -1.33 | -3.00 | -1.81 | -1.45 | -2.34 | -2.85 | -2.47 | -1.60 | -1.66 | -1.69|
| dec-waitktgt |  |  | es | einiger | gab | tag | gab | es | einige | einigen | dieser | staatlichen | pi@@ | lot@@ | programme | große | große | fehler | . | </s>|
| full sent tgt |  |  | es | dem | 1. | jahr | ist | es | in | einigen | dieser | staatlichen | pi@@ | lot@@ | programme | große | große | fehler | . | </s>|
| ref | in | einigen | dieser | öffentlichen | pi@@ | lot@@ | programme | wurden | große | fehler | gemacht | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | there | are | a | lot | less | expensive | and | less | in@@ | tru@@ | sive | ways | to | do | this | .|
| waitk tgt |  |  | es | gibt | viel | weniger | t@@ | eure | und | weniger | ein@@ | drin@@ | gliche | wege | , | dies | zu | tun | . | </s>|
| waitk prob |  |  | 0.39 | 0.74 | 0.37 | 0.69 | 0.33 | 0.58 | 0.84 | 0.95 | 0.61 | 0.96 | 0.80 | 0.36 | 0.62 | 0.54 | 0.90 | 0.81 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.42 | 0.82 | 0.67 | 0.64 | 0.26 | 0.40 | 0.85 | 0.94 | 0.42 | 0.35 | 0.50 | 0.38 | 0.55 | 0.48 | 0.86 | 0.78 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.47 | -1.78 | -2.05 | -2.14 | -4.01 | -2.54 | -1.97 | -1.26 | -2.30 | -2.84 | -1.62 | -3.25 | -2.71 | -2.92 | -1.92 | -1.93 | -1.65 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.80 | -2.38 | -3.24 | -2.49 | -3.54 | -1.71 | -2.02 | -1.15 | -2.60 | -0.55 | -1.34 | -2.60 | -2.47 | -2.38 | -1.58 | -1.92 | -1.60 | -1.70|
| full sent prob |  |  | 0.29 | 0.88 | 0.35 | 0.51 | 0.69 | 0.86 | 0.89 | 0.85 | 0.29 | 0.87 | 0.78 | 0.58 | 0.69 | 0.53 | 0.88 | 0.76 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.69 | -1.53 | -3.11 | -2.93 | -1.80 | -1.18 | -1.62 | -1.68 | -2.67 | -1.39 | -1.55 | -2.32 | -2.36 | -2.75 | -1.81 | -2.05 | -1.62 | -1.66|
| full sent KL (full->waitk) |  |  | -3.76 | -2.42 | -3.15 | -2.41 | -3.66 | -1.88 | -2.05 | -1.08 | -2.54 | -0.96 | -1.52 | -2.66 | -2.55 | -2.41 | -1.59 | -1.91 | -1.60 | -1.69|
| dec-waitktgt |  |  | es | gibt | viel | weniger | t@@ | eure | und | weniger | ein@@ | drin@@ | gliche | wege | , | dies | zu | tun | . | </s>|
| full sent tgt |  |  | es | gibt | viel | weniger | t@@ | eure | und | weniger | auf@@ | drin@@ | gliche | wege | , | dies | zu | tun | . | </s>|
| ref | es | gibt | wesentlich | billi@@ | gere | und | weniger | in@@ | tru@@ | sive | möglichkeiten | , | dies | umzusetzen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | o@@ | reg@@ | on | , | pl@@ | ann@@ | ers | are | experim@@ | enting | with | giving | drivers | different | choices | .|
| waitk tgt |  |  | in | ore@@ | g@@ | on | , | plan@@ | ern | sind | experi@@ | men@@ | tieren | mit | dem | geben | der | fahrer | verschiedene | optionen | . | </s>|
| waitk prob |  |  | 0.48 | 0.99 | 0.97 | 0.96 | 0.28 | 0.93 | 0.76 | 0.68 | 0.25 | 0.54 | 0.74 | 0.46 | 0.38 | 0.38 | 0.28 | 0.77 | 0.38 | 0.15 | 0.85 | 0.91|
| dec-waitk prob |  |  | 0.02 | 0.97 | 0.98 | 0.96 | 0.49 | 0.50 | 0.05 | 0.34 | 0.47 | 0.02 | 0.06 | 0.18 | 0.09 | 0.06 | 0.20 | 0.14 | 0.13 | 0.16 | 0.89 | 0.92|
| dec-waitk rank |  |  | 4 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 1 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.54 | -1.07 | -1.00 | -1.16 | -2.36 | -3.05 | -2.90 | -3.88 | -3.13 | -1.78 | -2.48 | -3.27 | -3.48 | -5.62 | -2.65 | -4.77 | -4.51 | -3.22 | -1.76 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.24 | -0.91 | -1.08 | -1.20 | -4.32 | -0.98 | -1.36 | -2.12 | -3.00 | -1.72 | -1.38 | -1.96 | -2.68 | -4.16 | -3.00 | -1.27 | -2.43 | -3.67 | -1.94 | -1.68|
| full sent prob |  |  | 0.59 | 0.97 | 0.97 | 0.94 | 0.00 | 0.01 | 0.30 | 0.03 | 0.30 | 0.11 | 0.10 | 0.47 | 0.21 | 0.37 | 0.43 | 0.85 | 0.49 | 0.12 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 21 | 6 | 1 | 3 | 0 | 2 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.78 | -1.06 | -1.12 | -1.33 | -1.33 | -3.73 | -2.22 | -3.19 | -3.09 | -1.62 | -1.97 | -1.99 | -2.93 | -4.08 | -2.64 | -1.53 | -2.42 | -3.15 | -1.68 | -1.67|
| full sent KL (full->waitk) |  |  | -3.48 | -0.91 | -1.07 | -1.19 | -4.20 | -0.61 | -1.51 | -1.95 | -2.98 | -1.76 | -1.41 | -2.06 | -2.75 | -4.26 | -3.03 | -1.73 | -2.57 | -3.67 | -1.94 | -1.68|
| dec-waitktgt |  |  | ore@@ | ore@@ | g@@ | on | , | plan@@ | er | sind | experi@@ | mente | tier@@ | </s> | verschiedenen | treffen | von | fahrer | . | möglichkeiten | . | </s>|
| full sent tgt |  |  | in | ore@@ | g@@ | on | experi@@ | experi@@ | er | experi@@ | experi@@ | mente | tier@@ | mit | der | geben | der | fahrer | verschiedene | möglichkeiten | . | </s>|
| ref | in | ore@@ | g@@ | on | experi@@ | men@@ | tieren | die | plan@@ | er | damit | , | auto@@ | fahr@@ | ern | eine | reihe | von | aus@@ | wahl@@ | möglichkeiten | zu | geben | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | they | can | choose | a | device | with | or | without | g@@ | ps | .|
| waitk tgt |  |  | sie | können | ein | gerät | mit | oder | ohne | g@@ | ps | wählen | . | </s>|
| waitk prob |  |  | 0.52 | 0.76 | 0.40 | 0.82 | 0.74 | 0.89 | 0.96 | 0.92 | 0.90 | 0.41 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.64 | 0.72 | 0.11 | 0.87 | 0.56 | 0.90 | 0.93 | 0.95 | 0.88 | 0.28 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.35 | -2.44 | -2.76 | -1.58 | -2.31 | -1.63 | -1.43 | -1.22 | -1.54 | -1.73 | -1.70 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.31 | -2.06 | -3.08 | -2.10 | -2.19 | -1.55 | -1.19 | -1.46 | -1.34 | -2.46 | -1.58 | -1.66|
| full sent prob |  |  | 0.48 | 0.81 | 0.58 | 0.93 | 0.84 | 0.87 | 0.92 | 0.92 | 0.87 | 0.25 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.45 | -1.95 | -2.93 | -1.25 | -1.84 | -1.75 | -1.56 | -1.55 | -1.55 | -1.97 | -1.68 | -1.65|
| full sent KL (full->waitk) |  |  | -3.24 | -2.11 | -3.23 | -2.14 | -2.36 | -1.53 | -1.18 | -1.43 | -1.33 | -2.44 | -1.58 | -1.66|
| dec-waitktgt |  |  | sie | können | wählen | gerät | mit | oder | ohne | g@@ | ps | auswählen | . | </s>|
| full sent tgt |  |  | sie | können | ein | gerät | mit | oder | ohne | g@@ | ps | auswählen | . | </s>|
| ref | sie | können | sich | für | ein | gerät | mit | oder | ohne | g@@ | ps | entscheiden | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | if | we | do | this | , | hundreds | of | millions | of | drivers | will | be | concerned | about | their | privacy | and | a | host | of | other | things | .|
| waitk tgt |  |  | wenn | wir | das | tun | , | werden | hunder@@ | te | millionen | von | fahr@@ | ern | um | ihre | privat@@ | sphäre | und | eine | vielzahl | anderer | dinge | besorgt | sein | . | </s>|
| waitk prob |  |  | 0.75 | 0.75 | 0.47 | 0.82 | 0.90 | 0.57 | 0.65 | 0.95 | 0.55 | 0.32 | 0.31 | 0.93 | 0.16 | 0.75 | 0.83 | 0.94 | 0.58 | 0.36 | 0.46 | 0.49 | 0.89 | 0.72 | 0.94 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.86 | 0.72 | 0.30 | 0.82 | 0.83 | 0.01 | 0.66 | 0.93 | 0.82 | 0.49 | 0.51 | 0.95 | 0.00 | 0.77 | 0.94 | 0.91 | 0.76 | 0.62 | 0.54 | 0.52 | 0.93 | 0.74 | 0.72 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.58 | -2.51 | -2.63 | -1.80 | -2.17 | -1.63 | -2.40 | -1.42 | -1.31 | -2.94 | -2.41 | -1.14 | -3.39 | -1.67 | -1.16 | -1.46 | -1.89 | -2.42 | -2.03 | -2.11 | -1.23 | -2.23 | -1.91 | -1.66 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.36 | -2.16 | -2.07 | -1.78 | -1.66 | -2.40 | -2.61 | -1.18 | -1.88 | -3.48 | -3.77 | -1.36 | -3.69 | -1.77 | -1.94 | -1.26 | -2.18 | -3.00 | -1.91 | -2.23 | -1.53 | -1.94 | -1.12 | -1.66 | -1.66|
| full sent prob |  |  | 0.74 | 0.84 | 0.42 | 0.62 | 0.89 | 0.61 | 0.74 | 0.92 | 0.61 | 0.49 | 0.73 | 0.91 | 0.14 | 0.80 | 0.94 | 0.96 | 0.83 | 0.49 | 0.32 | 0.58 | 0.91 | 0.83 | 0.93 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.32 | -1.92 | -2.42 | -2.54 | -1.81 | -2.41 | -1.90 | -1.44 | -1.73 | -2.67 | -1.73 | -1.47 | -3.34 | -1.56 | -1.10 | -1.17 | -1.71 | -2.66 | -2.05 | -2.29 | -1.35 | -1.72 | -1.46 | -1.68 | -1.66|
| full sent KL (full->waitk) |  |  | -2.28 | -2.23 | -2.10 | -1.65 | -1.70 | -2.67 | -2.66 | -1.17 | -1.83 | -3.49 | -3.81 | -1.33 | -3.75 | -1.80 | -1.95 | -1.29 | -2.20 | -2.97 | -1.84 | -2.23 | -1.51 | -2.00 | -1.28 | -1.66 | -1.65|
| dec-waitktgt |  |  | wenn | wir | dies | tun | , | hunder@@ | hunder@@ | te | millionen | von | fahr@@ | ern | besorgt | ihre | privat@@ | sphäre | und | eine | vielzahl | anderer | dinge | besorgt | sein | . | </s>|
| full sent tgt |  |  | wenn | wir | das | tun | , | werden | hunder@@ | te | millionen | von | fahr@@ | ern | über | ihre | privat@@ | sphäre | und | eine | menge | anderer | dinge | besorgt | sein | . | </s>|
| ref | wenn | wir | das | tun | , | machen | sich | hunder@@ | te | millionen | von | auto@@ | fahr@@ | ern | sorgen | über | ihre | privat@@ | sphäre | und | zahlreiche | andere | dinge | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | kö@@ | ni@@ | gs@@ | fel@@ | d | : | small | team | gives | a | spi@@ | ri@@ | ted | performance|
| waitk tgt |  |  | die | köni@@ | gs@@ | feld | : | kleines | team | gibt | eine | spi@@ | rit@@ | ed | performan@@ | ce | in | der | geschichte | von | &quot; | the | world | &quot; | . | </s>|
| waitk prob |  |  | 0.12 | 0.26 | 0.97 | 0.77 | 0.83 | 0.24 | 0.91 | 0.47 | 0.10 | 0.19 | 0.40 | 0.18 | 0.89 | 0.94 | 0.15 | 0.20 | 0.03 | 0.24 | 0.02 | 0.04 | 0.04 | 0.40 | 0.37 | 0.82|
| dec-waitk prob |  |  | 0.00 | 0.01 | 0.86 | 0.42 | 0.04 | 0.07 | 0.69 | 0.04 | 0.05 | 0.06 | 0.04 | 0.00 | 0.45 | 0.93 | 0.00 | 0.16 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.04 | 0.08 | 0.91|
| dec-waitk rank |  |  | 32 | 5 | 0 | 0 | 1 | 2 | 0 | 1 | 4 | 3 | 2 | 514 | 0 | 0 | 9 | 0 | 23 | 10 | 2 | 5 | 131 | 3 | 2 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.85 | -6.18 | -1.63 | -3.65 | -1.72 | -3.56 | -3.07 | -2.17 | -3.86 | -4.61 | -1.86 | -5.16 | -3.65 | -1.42 | -1.10 | -4.74 | -2.81 | -1.26 | -5.81 | -4.29 | -5.47 | -4.07 | -2.24 | -1.54|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.36 | -4.37 | -0.89 | -1.48 | -1.40 | -3.58 | -1.36 | -3.14 | -4.23 | -4.59 | -2.22 | -4.74 | -1.08 | -1.24 | -3.78 | -4.54 | -5.98 | -3.31 | -6.20 | -6.28 | -5.66 | -3.29 | -3.50 | -2.19|
| full sent prob |  |  | 0.00 | 0.00 | 0.87 | 0.51 | 0.61 | 0.02 | 0.74 | 0.19 | 0.17 | 0.02 | 0.00 | 0.00 | 0.78 | 0.92 | 0.00 | 0.16 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.04 | 0.08 | 0.92|
| full sent rank |  |  | 512 | 1272 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 8 | 4 | 267 | 0 | 0 | 5 | 0 | 29 | 16 | 3 | 4 | 154 | 3 | 1 | 0|
| full sent KL (waitk->full) |  |  | -1.66 | -5.32 | -1.69 | -2.84 | -2.99 | -3.38 | -2.82 | -4.65 | -4.33 | -4.97 | -1.31 | -5.09 | -2.09 | -1.44 | -0.98 | -4.40 | -2.76 | -1.39 | -5.78 | -3.80 | -5.27 | -4.14 | -2.27 | -1.52|
| full sent KL (full->waitk) |  |  | -4.40 | -4.37 | -0.90 | -1.54 | -1.79 | -3.53 | -1.40 | -3.20 | -4.23 | -4.59 | -2.20 | -4.74 | -1.32 | -1.23 | -3.77 | -4.54 | -5.98 | -3.31 | -6.20 | -6.28 | -5.66 | -3.29 | -3.49 | -2.19|
| dec-waitktgt |  |  | köni@@ | medien@@ | gs@@ | feld | </s> | kleine | team | </s> | ein | </s> | r@@ | -@@ | performan@@ | ce | </s> | der | hand | </s> | </s> | </s> | mi@@ | : | </s> | </s>|
| full sent tgt |  |  | köni@@ | klein@@ | gs@@ | feld | : | das | team | gibt | eine | er@@ | r@@ | ver@@ | performan@@ | ce | </s> | der | hand | </s> | </s> | </s> | mi@@ | : | </s> | </s>|
| ref | köni@@ | gs@@ | feld | : | kleine | mann@@ | schaft | schlägt | sich | wa@@ | cker | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | voluntary | fire | service | bra@@ | vely | came | through | the | main | autumn | test | run | in | spite | of | a | lack | of | personnel | .|
| waitk tgt |  |  | die | freiwilli@@ | ge | feuer@@ | w@@ | ehr | kam | mu@@ | tig | durch | die | haupt@@ | her@@ | b@@ | st@@ | test@@ | strecke | , | obwohl | es | an | personal | mangel@@ | te | . | </s>|
| waitk prob |  |  | 0.23 | 0.65 | 0.76 | 0.89 | 0.97 | 0.98 | 0.15 | 0.38 | 0.96 | 0.69 | 0.43 | 0.34 | 0.68 | 0.97 | 0.85 | 0.78 | 0.26 | 0.67 | 0.49 | 0.35 | 0.40 | 0.87 | 0.28 | 0.67 | 0.92 | 0.91|
| dec-waitk prob |  |  | 0.05 | 0.67 | 0.81 | 0.95 | 0.84 | 0.97 | 0.15 | 0.91 | 0.95 | 0.72 | 0.49 | 0.04 | 0.18 | 0.98 | 0.90 | 0.61 | 0.21 | 0.43 | 0.23 | 0.21 | 0.17 | 0.96 | 0.36 | 0.80 | 0.91 | 0.92|
| dec-waitk rank |  |  | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.74 | -2.47 | -1.95 | -1.04 | -1.57 | -1.09 | -3.05 | -0.93 | -1.19 | -2.10 | -2.33 | -2.33 | -3.80 | -0.95 | -1.22 | -1.89 | -2.96 | -3.34 | -3.27 | -3.72 | -4.00 | -1.01 | -2.57 | -1.55 | -1.63 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.23 | -2.75 | -1.58 | -1.22 | -0.93 | -0.99 | -3.84 | -3.76 | -1.16 | -2.33 | -2.31 | -3.40 | -2.36 | -1.12 | -1.42 | -1.77 | -2.71 | -2.24 | -1.49 | -3.21 | -3.42 | -1.60 | -3.46 | -2.22 | -1.57 | -1.68|
| full sent prob |  |  | 0.24 | 0.63 | 0.88 | 0.95 | 0.76 | 0.98 | 0.07 | 0.62 | 0.97 | 0.52 | 0.48 | 0.12 | 0.12 | 0.98 | 0.85 | 0.40 | 0.09 | 0.10 | 0.16 | 0.20 | 0.25 | 0.96 | 0.43 | 0.79 | 0.92 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.19 | -2.74 | -1.55 | -1.04 | -1.80 | -1.03 | -3.74 | -1.74 | -1.08 | -3.01 | -2.03 | -3.85 | -4.28 | -0.96 | -1.45 | -2.46 | -1.84 | -1.02 | -2.35 | -3.66 | -3.81 | -1.00 | -2.31 | -1.61 | -1.53 | -1.62|
| full sent KL (full->waitk) |  |  | -3.30 | -2.73 | -1.62 | -1.22 | -0.87 | -0.99 | -3.83 | -3.67 | -1.16 | -2.21 | -2.33 | -3.38 | -2.32 | -1.12 | -1.38 | -1.63 | -2.74 | -2.15 | -1.55 | -3.20 | -3.45 | -1.60 | -3.47 | -2.22 | -1.58 | -1.68|
| dec-waitktgt |  |  | freiwilli@@ | freiwilli@@ | ge | feuer@@ | w@@ | ehr | ist | mu@@ | tig | durch | die | her@@ | her@@ | b@@ | st@@ | test@@ | strecke | , | trotz | es | an | personal | mangel@@ | te | . | </s>|
| full sent tgt |  |  | der | freiwilli@@ | ge | feuer@@ | w@@ | ehr | hat | mu@@ | tig | durch | die | her@@ | versu@@ | b@@ | st@@ | test@@ | lauf | trotz | trotz | es | an | personal | mangel@@ | te | . | </s>|
| ref | die | freiwilli@@ | ge | feuer@@ | w@@ | ehr | be@@ | wä@@ | lti@@ | gte | ihre | her@@ | b@@ | st@@ | haupt@@ | pro@@ | be | trotz | personal@@ | mangel@@ | s | mit | bra@@ | vo@@ | ur | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | two | people | were | in@@ | ju@@ | red | by | the | resulting | fire | and | the | spread | of | smo@@ | ke | , | however | , | one | was | able | to | make | an | emergency | call | .|
| waitk tgt |  |  | zwei | personen | wurden | verletzt | durch | die | re@@ | su@@ | lti@@ | erende | bran@@ | d | und | die | aus@@ | brei@@ | tung | des | rau@@ | ch@@ | ens | , | aber | man | konnte | einen | not@@ | ruf | machen | . | </s>|
| waitk prob |  |  | 0.52 | 0.45 | 0.83 | 0.63 | 0.52 | 0.47 | 0.19 | 0.97 | 0.98 | 0.82 | 0.34 | 0.67 | 0.85 | 0.78 | 0.57 | 0.95 | 0.94 | 0.45 | 0.71 | 0.54 | 0.99 | 0.85 | 0.30 | 0.68 | 0.79 | 0.55 | 0.82 | 0.98 | 0.55 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.90 | 0.24 | 0.68 | 0.88 | 0.00 | 0.76 | 0.08 | 0.38 | 0.87 | 0.40 | 0.05 | 0.46 | 0.77 | 0.67 | 0.51 | 0.84 | 0.96 | 0.21 | 0.71 | 0.67 | 0.48 | 0.37 | 0.26 | 0.44 | 0.59 | 0.41 | 0.96 | 0.98 | 0.17 | 0.90 | 0.92|
| dec-waitk rank |  |  | 0 | 1 | 0 | 0 | 5 | 0 | 1 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.22 | -1.71 | -2.06 | -1.25 | -3.00 | -2.19 | -4.70 | -4.12 | -1.85 | -3.73 | -3.61 | -3.43 | -2.19 | -2.36 | -2.52 | -1.82 | -1.18 | -1.73 | -2.07 | -1.45 | -3.94 | -2.67 | -3.77 | -3.16 | -2.69 | -3.44 | -0.95 | -0.98 | -3.05 | -1.70 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.43 | -2.63 | -1.73 | -2.48 | -2.18 | -2.39 | -4.25 | -0.57 | -0.89 | -0.96 | -3.09 | -1.78 | -1.87 | -1.99 | -1.45 | -1.03 | -1.35 | -1.81 | -1.45 | -2.14 | -0.50 | -1.61 | -3.72 | -2.20 | -1.78 | -2.26 | -1.91 | -0.94 | -2.29 | -1.66 | -1.68|
| full sent prob |  |  | 0.38 | 0.38 | 0.81 | 0.01 | 0.80 | 0.11 | 0.11 | 0.90 | 0.96 | 0.77 | 0.29 | 0.91 | 0.86 | 0.81 | 0.75 | 0.82 | 0.95 | 0.34 | 0.66 | 0.19 | 0.93 | 0.84 | 0.07 | 0.77 | 0.69 | 0.54 | 0.96 | 0.97 | 0.21 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 1 | 0 | 6 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.55 | -2.41 | -1.86 | -1.29 | -1.42 | -1.56 | -3.83 | -1.65 | -1.20 | -1.70 | -2.38 | -1.29 | -1.80 | -1.91 | -1.59 | -1.91 | -1.30 | -1.99 | -1.98 | -2.09 | -1.34 | -1.99 | -2.84 | -1.93 | -2.25 | -2.67 | -0.93 | -1.02 | -3.09 | -1.74 | -1.66|
| full sent KL (full->waitk) |  |  | -3.21 | -2.65 | -1.82 | -2.04 | -2.52 | -2.24 | -4.27 | -1.00 | -0.96 | -1.21 | -3.16 | -2.01 | -1.93 | -2.08 | -1.55 | -1.01 | -1.34 | -1.80 | -1.44 | -1.98 | -0.87 | -1.93 | -3.67 | -2.39 | -1.85 | -2.32 | -1.91 | -0.94 | -2.31 | -1.65 | -1.67|
| dec-waitktgt |  |  | zwei | menschen | wurden | verletzt | </s> | die | folge | su@@ | lti@@ | erende | brand@@ | d | und | die | aus@@ | brei@@ | tung | von | rau@@ | ch@@ | ens | . | aber | man | konnte | einen | not@@ | ruf | durchführen | . | </s>|
| full sent tgt |  |  | zwei | menschen | wurden | durch | durch | das | ent@@ | su@@ | lti@@ | erende | feuer | d | und | die | aus@@ | brei@@ | tung | von | rau@@ | chs | ens | , | konnte | man | konnte | einen | not@@ | ruf | . | . | </s>|
| ref | durch | den | ent@@ | stehenden | bran@@ | d | und | die | rau@@ | ch@@ | entwicklung | wurden | zwei | menschen | verletzt | , | einer | davon | konnte | aber | noch | einen | not@@ | ruf | ab@@ | senden | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | after | a | short | time | they | managed | to | find | the | first | person | and | direct | them | out | of | the | building | .|
| waitk tgt |  |  | nach | kurzer | zeit | schaff@@ | ten | sie | es | , | die | erste | person | zu | finden | und | sie | aus | dem | gebäude | zu | führen | . | </s>|
| waitk prob |  |  | 0.63 | 0.64 | 0.92 | 0.18 | 0.86 | 0.83 | 0.59 | 0.70 | 0.44 | 0.84 | 0.85 | 0.75 | 0.92 | 0.84 | 0.28 | 0.69 | 0.90 | 0.70 | 0.54 | 0.32 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.60 | 0.85 | 0.91 | 0.11 | 0.60 | 0.28 | 0.84 | 0.61 | 0.36 | 0.83 | 0.80 | 0.76 | 0.93 | 0.90 | 0.27 | 0.64 | 0.86 | 0.62 | 0.70 | 0.10 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.67 | -1.40 | -1.61 | -4.59 | -2.58 | -2.57 | -1.49 | -2.60 | -2.39 | -1.88 | -2.20 | -2.26 | -1.30 | -1.53 | -2.93 | -2.54 | -1.89 | -2.45 | -2.13 | -2.75 | -1.70 | -1.64|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.90 | -2.39 | -1.49 | -3.44 | -1.51 | -1.51 | -2.47 | -2.28 | -2.74 | -1.92 | -1.72 | -2.11 | -1.34 | -1.85 | -3.21 | -2.36 | -1.58 | -2.03 | -2.86 | -2.88 | -1.73 | -1.70|
| full sent prob |  |  | 0.60 | 0.71 | 0.91 | 0.04 | 0.79 | 0.49 | 0.90 | 0.68 | 0.49 | 0.82 | 0.80 | 0.76 | 0.92 | 0.89 | 0.40 | 0.65 | 0.87 | 0.66 | 0.61 | 0.08 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.94 | -1.90 | -1.63 | -3.43 | -1.57 | -2.48 | -1.27 | -2.37 | -2.35 | -2.03 | -2.24 | -2.21 | -1.38 | -1.60 | -2.65 | -2.53 | -1.81 | -2.30 | -2.32 | -2.86 | -1.70 | -1.69|
| full sent KL (full->waitk) |  |  | -2.90 | -2.32 | -1.49 | -3.46 | -1.65 | -1.65 | -2.49 | -2.32 | -2.77 | -1.91 | -1.72 | -2.11 | -1.33 | -1.84 | -3.24 | -2.36 | -1.59 | -2.05 | -2.82 | -2.88 | -1.73 | -1.69|
| dec-waitktgt |  |  | nach | kurzer | zeit | schaff@@ | ten | es | es | , | den | erste | person | zu | finden | und | aus | aus | dem | gebäude | zu | leiten | . | </s>|
| full sent tgt |  |  | nach | kurzer | zeit | ge@@ | ten | sie | es | , | die | erste | person | zu | finden | und | sie | aus | dem | gebäude | zu | leiten | . | </s>|
| ref | nach | kurzer | zeit | ge@@ | lang | es | , | die | erste | person | zu | finden | und | ins | freie | zu | ge@@ | leiten | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | this | was | not | so | simple | as | they | also | had | to | negotiate | a | narrow | sta@@ | ir@@ | well | .|
| waitk tgt |  |  | das | war | nicht | so | einfach | , | da | sie | auch | ein | en@@ | ges | tre@@ | ppen@@ | haus | ver@@ | handeln | mussten | . | </s>|
| waitk prob |  |  | 0.31 | 0.84 | 0.62 | 0.84 | 0.91 | 0.79 | 0.21 | 0.55 | 0.63 | 0.24 | 0.25 | 0.91 | 0.96 | 0.98 | 0.90 | 0.49 | 0.93 | 0.63 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.37 | 0.85 | 0.70 | 0.58 | 0.93 | 0.40 | 0.01 | 0.44 | 0.52 | 0.01 | 0.27 | 0.90 | 0.94 | 0.93 | 0.95 | 0.34 | 0.53 | 0.82 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 9 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.68 | -1.66 | -2.42 | -1.84 | -1.26 | -2.36 | -1.97 | -3.14 | -3.00 | -1.97 | -2.88 | -1.44 | -1.27 | -1.26 | -1.11 | -2.97 | -2.87 | -1.24 | -1.75 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.63 | -1.71 | -2.83 | -1.36 | -1.35 | -1.70 | -3.12 | -2.67 | -2.74 | -3.20 | -3.43 | -1.53 | -1.13 | -0.95 | -1.48 | -2.34 | -0.87 | -1.67 | -1.69 | -1.71|
| full sent prob |  |  | 0.16 | 0.46 | 0.68 | 0.71 | 0.91 | 0.66 | 0.14 | 0.38 | 0.59 | 0.18 | 0.13 | 0.91 | 0.95 | 0.94 | 0.96 | 0.40 | 0.65 | 0.83 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.85 | -3.57 | -2.56 | -2.23 | -1.43 | -2.22 | -3.20 | -3.05 | -3.05 | -3.28 | -2.49 | -1.55 | -1.23 | -1.14 | -1.08 | -3.09 | -2.68 | -1.24 | -1.70 | -1.68|
| full sent KL (full->waitk) |  |  | -3.55 | -1.44 | -2.82 | -1.45 | -1.33 | -1.86 | -3.08 | -2.65 | -2.78 | -3.29 | -3.43 | -1.53 | -1.13 | -0.95 | -1.48 | -2.36 | -0.96 | -1.68 | -1.69 | -1.71|
| dec-waitktgt |  |  | das | war | nicht | so | einfach | wie | wie | sie | auch | ver@@ | en@@ | ges | tre@@ | ppen@@ | haus | ver@@ | handeln | mussten | . | </s>|
| full sent tgt |  |  | das | war | nicht | so | einfach | , | als | sie | auch | eine | sch@@ | ges | tre@@ | ppen@@ | haus | ver@@ | handeln | mussten | . | </s>|
| ref | dies | war | nicht | so | einfach | , | da | auch | eine | enge | tre@@ | ppe | zu | überwinden | war | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | building | , | a | workshop | with | integrated | stab@@ | ling | for | two | horses | , | was | not | easy | to | secure | .|
| waitk tgt |  |  | das | gebäude | , | ein | work@@ | shop | mit | integri@@ | er@@ | tem | st@@ | all | für | zwei | pfer@@ | de | , | war | nicht | leicht | zu | sichern | . | </s>|
| waitk prob |  |  | 0.52 | 0.56 | 0.79 | 0.42 | 0.67 | 0.96 | 0.87 | 0.81 | 0.58 | 0.93 | 0.60 | 0.75 | 0.87 | 0.88 | 0.92 | 0.92 | 0.88 | 0.87 | 0.84 | 0.47 | 0.77 | 0.70 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.75 | 0.89 | 0.83 | 0.48 | 0.47 | 0.72 | 0.85 | 0.86 | 0.95 | 0.95 | 0.43 | 0.44 | 0.89 | 0.94 | 0.96 | 0.91 | 0.74 | 0.82 | 0.84 | 0.48 | 0.81 | 0.66 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.15 | -1.35 | -1.88 | -1.99 | -3.49 | -2.83 | -1.84 | -1.54 | -0.83 | -1.24 | -2.47 | -2.81 | -1.67 | -1.21 | -1.14 | -1.44 | -2.13 | -1.91 | -1.92 | -2.05 | -1.88 | -2.42 | -1.62 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.51 | -3.24 | -2.18 | -2.54 | -2.13 | -0.98 | -1.76 | -1.77 | -1.59 | -1.31 | -2.33 | -1.16 | -1.81 | -1.63 | -1.52 | -1.35 | -1.64 | -1.59 | -1.93 | -1.59 | -1.98 | -2.28 | -1.71 | -1.69|
| full sent prob |  |  | 0.46 | 0.82 | 0.75 | 0.31 | 0.16 | 0.93 | 0.84 | 0.87 | 0.86 | 0.97 | 0.56 | 0.72 | 0.87 | 0.93 | 0.95 | 0.92 | 0.86 | 0.87 | 0.88 | 0.49 | 0.73 | 0.65 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.15 | -1.70 | -2.31 | -2.45 | -4.32 | -1.34 | -1.80 | -1.44 | -1.31 | -1.08 | -2.43 | -2.15 | -1.79 | -1.30 | -1.28 | -1.50 | -1.89 | -1.69 | -1.71 | -1.88 | -2.06 | -2.41 | -1.68 | -1.64|
| full sent KL (full->waitk) |  |  | -3.39 | -3.21 | -2.12 | -2.53 | -1.98 | -1.15 | -1.76 | -1.77 | -1.56 | -1.33 | -2.39 | -1.31 | -1.79 | -1.62 | -1.50 | -1.35 | -1.73 | -1.62 | -1.96 | -1.60 | -1.93 | -2.28 | -1.71 | -1.69|
| dec-waitktgt |  |  | das | gebäude | , | ein | work@@ | shop | mit | integri@@ | er@@ | tem | st@@ | all | für | zwei | pfer@@ | de | , | war | nicht | leicht | zu | sichern | . | </s>|
| full sent tgt |  |  | das | gebäude | , | eine | werk@@ | shop | mit | integri@@ | er@@ | tem | st@@ | all | für | zwei | pfer@@ | de | , | war | nicht | leicht | zu | sichern | . | </s>|
| ref | das | gebäude | , | eine | werk@@ | statt | mit | integri@@ | erter | st@@ | all@@ | ung | für | zwei | pfer@@ | de | , | war | nicht | einfach | zu | sichern | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | there | were | large | quantities | of | wood | and | bal@@ | es | of | stra@@ | w | stored | inside | .|
| waitk tgt |  |  | es | gab | große | mengen | an | holz | und | bal@@ | es | von | stro@@ | h | in | innen@@ | räumen | ge@@ | la@@ | gert | . | </s>|
| waitk prob |  |  | 0.33 | 0.65 | 0.41 | 0.76 | 0.31 | 0.77 | 0.87 | 0.47 | 0.37 | 0.44 | 0.96 | 0.93 | 0.12 | 0.31 | 0.48 | 0.27 | 0.87 | 0.98 | 0.87 | 0.91|
| dec-waitk prob |  |  | 0.38 | 0.49 | 0.66 | 0.62 | 0.11 | 0.91 | 0.88 | 0.01 | 0.12 | 0.01 | 0.96 | 0.93 | 0.08 | 0.00 | 0.76 | 0.00 | 0.92 | 0.98 | 0.89 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 2 | 6 | 0 | 0 | 3 | 13 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.15 | -2.86 | -2.27 | -2.11 | -2.15 | -1.34 | -1.81 | -1.27 | -4.19 | -1.89 | -1.15 | -1.12 | -2.87 | -3.05 | -1.83 | -1.28 | -1.23 | -0.98 | -1.72 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.93 | -2.17 | -3.46 | -1.73 | -2.91 | -2.09 | -1.85 | -2.64 | -3.81 | -2.25 | -1.03 | -1.08 | -3.88 | -2.76 | -2.61 | -3.02 | -1.47 | -0.98 | -1.83 | -1.65|
| full sent prob |  |  | 0.31 | 0.37 | 0.64 | 0.88 | 0.07 | 0.80 | 0.88 | 0.04 | 0.35 | 0.45 | 0.96 | 0.99 | 0.20 | 0.11 | 0.40 | 0.26 | 0.92 | 0.98 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.52 | -2.61 | -2.37 | -1.57 | -2.20 | -2.22 | -1.78 | -1.17 | -3.95 | -2.66 | -1.17 | -0.87 | -3.30 | -2.89 | -3.68 | -2.48 | -1.24 | -0.98 | -1.77 | -1.67|
| full sent KL (full->waitk) |  |  | -3.92 | -2.12 | -3.45 | -1.87 | -2.91 | -2.02 | -1.85 | -2.65 | -3.88 | -2.43 | -1.03 | -1.12 | -3.87 | -2.81 | -2.47 | -3.02 | -1.47 | -0.97 | -1.82 | -1.65|
| dec-waitktgt |  |  | es | gab | große | mengen | holz | holz | und | b@@ | nen | </s> | stro@@ | h | , | der | räumen | . | la@@ | gert | . | </s>|
| full sent tgt |  |  | es | gab | große | mengen | von | holz | und | b@@ | es | von | stro@@ | h | in | innen | räumen | gespeichert | la@@ | gert | . | </s>|
| ref | es | lager@@ | te | viel | holz | und | auch | stro@@ | h@@ | b@@ | allen | darin | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | first | attempt | to | ext@@ | ingu@@ | ish | the | fire | was | made | using | the | tan@@ | k | on | the | fire | engine | .|
| waitk tgt |  |  | der | erste | versuch | , | die | alte | feuer@@ | stelle | zu | löschen | , | wurde | mit | dem | tan@@ | k | auf | der | feuer@@ | stelle | gemacht | . | </s>|
| waitk prob |  |  | 0.54 | 0.93 | 0.92 | 0.71 | 0.40 | 0.01 | 0.44 | 0.25 | 0.63 | 0.55 | 0.66 | 0.63 | 0.53 | 0.54 | 0.71 | 0.91 | 0.58 | 0.67 | 0.74 | 0.11 | 0.36 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.70 | 0.96 | 0.87 | 0.12 | 0.25 | 0.00 | 0.16 | 0.00 | 0.70 | 0.85 | 0.84 | 0.52 | 0.57 | 0.38 | 0.51 | 0.87 | 0.23 | 0.43 | 0.86 | 0.02 | 0.19 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 44 | 1 | 26 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.33 | -1.20 | -1.78 | -2.76 | -3.49 | -5.64 | -2.13 | -4.31 | -2.03 | -1.35 | -1.81 | -2.82 | -3.01 | -2.77 | -1.80 | -1.70 | -2.87 | -2.07 | -1.45 | -5.19 | -2.91 | -1.67 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.17 | -1.39 | -1.38 | -2.01 | -3.74 | -6.42 | -3.23 | -3.96 | -2.48 | -2.96 | -2.15 | -2.55 | -3.10 | -1.97 | -2.05 | -1.45 | -2.33 | -1.95 | -1.99 | -4.81 | -3.50 | -1.70 | -1.68|
| full sent prob |  |  | 0.39 | 0.84 | 0.71 | 0.50 | 0.03 | 0.00 | 0.24 | 0.03 | 0.73 | 0.88 | 0.83 | 0.58 | 0.69 | 0.62 | 0.50 | 0.90 | 0.34 | 0.45 | 0.91 | 0.02 | 0.23 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 2 | 854 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.62 | -2.05 | -2.62 | -3.05 | -1.83 | -2.49 | -2.14 | -3.39 | -1.99 | -1.18 | -1.80 | -2.40 | -2.38 | -2.19 | -2.39 | -1.52 | -2.67 | -1.98 | -1.17 | -5.28 | -3.19 | -1.70 | -1.68|
| full sent KL (full->waitk) |  |  | -3.03 | -1.29 | -1.27 | -2.22 | -3.72 | -6.42 | -3.26 | -3.98 | -2.50 | -2.97 | -2.15 | -2.58 | -3.15 | -2.06 | -2.04 | -1.47 | -2.39 | -1.96 | -2.01 | -4.80 | -3.51 | -1.70 | -1.67|
| dec-waitktgt |  |  | der | erste | versuch | der | die | lü@@ | fla@@ | s@@ | zu | löschen | , | wurde | mit | dem | tan@@ | k | des | der | feuer@@ | maschine | unternommen | . | </s>|
| full sent tgt |  |  | der | erste | versuch | , | das | feuer@@ | fla@@ | w@@ | zu | löschen | , | wurde | mit | dem | tan@@ | k | auf | der | feuer@@ | maschine | unternommen | . | </s>|
| ref | der | erste | lö@@ | sch@@ | angriff | erfol@@ | gte | über | den | tan@@ | k | im | fahrzeug | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | another | line | was | taken | from | the | surface | hy@@ | dr@@ | ant | around | 100 | metres | away | .|
| waitk tgt |  |  | eine | weitere | linie | wurde | von | der | ober@@ | flächen@@ | hy@@ | dro@@ | se | etwa | 100 | meter | entfernt | . | </s>|
| waitk prob |  |  | 0.46 | 0.51 | 0.41 | 0.63 | 0.49 | 0.71 | 0.54 | 0.47 | 0.83 | 0.34 | 0.16 | 0.32 | 0.91 | 0.62 | 0.91 | 0.46 | 0.91|
| dec-waitk prob |  |  | 0.72 | 0.45 | 0.50 | 0.40 | 0.23 | 0.76 | 0.76 | 0.80 | 0.62 | 0.10 | 0.01 | 0.07 | 0.88 | 0.67 | 0.92 | 0.01 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 9 | 3 | 0 | 0 | 0 | 11 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.83 | -1.97 | -3.38 | -3.61 | -3.49 | -2.35 | -1.56 | -1.86 | -1.99 | -2.89 | -5.76 | -3.75 | -1.66 | -1.80 | -1.29 | -2.21 | -1.64|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.39 | -1.92 | -3.87 | -2.56 | -3.00 | -2.21 | -1.63 | -1.56 | -1.65 | -2.25 | -5.41 | -2.74 | -1.28 | -2.21 | -1.37 | -3.07 | -1.65|
| full sent prob |  |  | 0.32 | 0.61 | 0.66 | 0.38 | 0.23 | 0.34 | 0.28 | 0.77 | 0.72 | 0.21 | 0.02 | 0.04 | 0.86 | 0.69 | 0.80 | 0.01 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 6 | 5 | 0 | 0 | 0 | 6 | 0|
| full sent KL (waitk->full) |  |  | -3.90 | -2.06 | -2.40 | -3.84 | -3.43 | -2.06 | -4.64 | -1.89 | -1.76 | -3.12 | -5.52 | -3.77 | -1.77 | -1.64 | -1.84 | -2.76 | -1.67|
| full sent KL (full->waitk) |  |  | -3.23 | -1.93 | -3.92 | -2.55 | -3.01 | -1.97 | -1.40 | -1.55 | -1.71 | -2.27 | -5.41 | -2.73 | -1.27 | -2.23 | -1.28 | -3.07 | -1.65|
| dec-waitktgt |  |  | eine | weitere | linie | wurde | von | der | ober@@ | flächen@@ | hy@@ | d@@ | xi@@ | um | 100 | meter | entfernt | genommen | </s>|
| full sent tgt |  |  | eine | weitere | linie | wurde | von | dem | ober@@ | flächen@@ | hy@@ | d@@ | xi@@ | um | 100 | meter | entfernt | genommen | </s>|
| ref | eine | weitere | leitung | erfol@@ | gte | über | einen | über@@ | fl@@ | ur@@ | - | hy@@ | d@@ | ran@@ | ten | in | rund | 100 | meter | entfernung | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | a | hol@@ | low-@@ | stream | no@@ | zz@@ | le | in | the | building | was | also | used | .|
| waitk tgt |  |  | eine | hol@@ | lo@@ | w-@@ | stre@@ | am@@ | -@@ | dü@@ | se | im | gebäude | wurde | ebenfalls | verwendet | . | </s>|
| waitk prob |  |  | 0.22 | 0.25 | 0.71 | 0.67 | 0.96 | 0.87 | 0.91 | 0.97 | 0.94 | 0.67 | 0.76 | 0.66 | 0.51 | 0.38 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.02 | 0.18 | 0.91 | 0.68 | 0.98 | 0.93 | 0.97 | 0.88 | 0.85 | 0.59 | 0.82 | 0.43 | 0.86 | 0.44 | 0.90 | 0.91|
| dec-waitk rank |  |  | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.65 | -5.18 | -1.33 | -1.44 | -1.01 | -1.06 | -1.08 | -1.61 | -1.91 | -2.96 | -1.71 | -3.21 | -1.27 | -2.66 | -1.73 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.86 | -5.03 | -2.58 | -2.05 | -1.18 | -1.37 | -1.45 | -0.98 | -1.17 | -2.31 | -2.07 | -2.63 | -1.85 | -2.60 | -1.69 | -1.67|
| full sent prob |  |  | 0.07 | 0.14 | 0.60 | 0.53 | 0.96 | 0.81 | 0.87 | 0.94 | 0.95 | 0.35 | 0.74 | 0.61 | 0.79 | 0.41 | 0.90 | 0.91|
| full sent rank |  |  | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.99 | -4.87 | -3.37 | -1.61 | -1.16 | -1.56 | -1.40 | -1.29 | -1.13 | -3.02 | -2.17 | -2.77 | -1.53 | -2.81 | -1.73 | -1.66|
| full sent KL (full->waitk) |  |  | -3.87 | -5.02 | -2.40 | -1.97 | -1.17 | -1.28 | -1.38 | -1.02 | -1.25 | -2.19 | -2.02 | -2.73 | -1.84 | -2.60 | -1.69 | -1.67|
| dec-waitktgt |  |  | ho@@ | hol@@ | lo@@ | w-@@ | stre@@ | am@@ | -@@ | dü@@ | se | im | gebäude | wurde | ebenfalls | verwendet | . | </s>|
| full sent tgt |  |  | auch | ho@@ | lo@@ | w-@@ | stre@@ | am@@ | -@@ | dü@@ | se | im | gebäude | wurde | ebenfalls | verwendet | . | </s>|
| ref | zum | einsatz | kam | auch | im | gebäude | ein | ho@@ | hl@@ | strahl@@ | ro@@ | hr | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | in | case | of | emergency | , | support | is | provided | by | the | kö@@ | ni@@ | gs@@ | fel@@ | d | day@@ | time | task | force | .|
| waitk tgt |  |  | bei | not@@ | fällen | wird | die | unterstützung | durch | die | kö@@ | ni@@ | gs@@ | fel@@ | d-@@ | tages@@ | zeit@@ | -@@ | ta@@ | sk@@ | for@@ | ce | geleistet | . | </s>|
| waitk prob |  |  | 0.31 | 0.45 | 0.61 | 0.19 | 0.33 | 0.59 | 0.66 | 0.35 | 0.72 | 0.93 | 0.88 | 0.67 | 0.73 | 0.68 | 0.41 | 0.40 | 0.70 | 0.74 | 0.71 | 0.95 | 0.37 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.03 | 0.73 | 0.52 | 0.03 | 0.30 | 0.42 | 0.06 | 0.26 | 0.99 | 0.94 | 0.75 | 0.70 | 0.51 | 0.16 | 0.06 | 0.02 | 0.69 | 0.15 | 0.67 | 0.97 | 0.14 | 0.90 | 0.91|
| dec-waitk rank |  |  | 2 | 0 | 0 | 4 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 12 | 0 | 1 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.59 | -1.91 | -2.06 | -4.01 | -3.48 | -2.89 | -1.78 | -2.34 | -0.74 | -1.33 | -2.38 | -2.56 | -2.81 | -3.70 | -2.96 | -5.13 | -2.19 | -1.15 | -2.56 | -1.04 | -2.32 | -1.75 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.45 | -3.43 | -2.25 | -3.70 | -3.51 | -2.91 | -1.84 | -2.47 | -2.44 | -1.41 | -1.20 | -1.56 | -2.00 | -1.81 | -1.45 | -3.56 | -2.44 | -1.07 | -1.95 | -1.32 | -2.90 | -1.66 | -1.65|
| full sent prob |  |  | 0.10 | 0.58 | 0.80 | 0.32 | 0.57 | 0.04 | 0.53 | 0.86 | 0.00 | 0.08 | 0.74 | 0.20 | 0.95 | 0.06 | 0.06 | 0.50 | 0.74 | 0.22 | 0.69 | 0.97 | 0.29 | 0.90 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 205 | 1 | 0 | 1 | 0 | 1 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.20 | -2.58 | -1.40 | -3.58 | -2.68 | -4.68 | -2.26 | -1.41 | -0.75 | -2.73 | -2.71 | -1.61 | -1.01 | -0.47 | -3.83 | -3.34 | -2.14 | -1.23 | -2.01 | -1.03 | -2.67 | -1.75 | -1.67|
| full sent KL (full->waitk) |  |  | -3.43 | -3.37 | -2.37 | -3.74 | -3.58 | -2.71 | -2.13 | -2.54 | -1.86 | -0.75 | -1.19 | -1.33 | -2.26 | -1.73 | -1.36 | -3.72 | -2.46 | -1.10 | -1.97 | -1.32 | -2.93 | -1.66 | -1.64|
| dec-waitktgt |  |  | im | not@@ | fällen | , | die | unterstützung | gewährt | das | kö@@ | ni@@ | gs@@ | fel@@ | d-@@ | da@@ | zeitung | stelle | ta@@ | sk | for@@ | ce | gewährt | . | </s>|
| full sent tgt |  |  | im | not@@ | fällen | wird | die | ta@@ | durch | die | ta@@ | pf@@ | gs@@ | feld | d-@@ | ta@@ | einsatz@@ | -@@ | ta@@ | sk | for@@ | ce | geleistet | . | </s>|
| ref | im | ernst@@ | fall | erfolgt | eine | unterstützung | über | die | tages@@ | einsatz@@ | gruppe | köni@@ | gs@@ | feld | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | comm@@ | ander | expressed | his | satisfaction | following | the | exercise | .|
| waitk tgt |  |  | der | komman@@ | dan@@ | t | äuß@@ | erte | seine | zufriedenheit | nach | der | ü@@ | bung | . | </s>|
| waitk prob |  |  | 0.44 | 0.71 | 0.52 | 0.91 | 0.37 | 0.94 | 0.67 | 0.46 | 0.26 | 0.66 | 0.50 | 0.97 | 0.84 | 0.91|
| dec-waitk prob |  |  | 0.41 | 0.82 | 0.44 | 0.93 | 0.21 | 0.89 | 0.73 | 0.62 | 0.07 | 0.37 | 0.63 | 0.95 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.06 | -1.57 | -1.70 | -1.37 | -2.80 | -1.66 | -2.08 | -1.56 | -2.86 | -2.55 | -2.30 | -1.26 | -1.70 | -1.65|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.70 | -2.06 | -2.10 | -1.35 | -2.84 | -1.27 | -1.91 | -2.96 | -3.52 | -2.23 | -2.67 | -1.06 | -2.10 | -1.68|
| full sent prob |  |  | 0.49 | 0.68 | 0.67 | 0.95 | 0.31 | 0.91 | 0.53 | 0.67 | 0.10 | 0.39 | 0.67 | 0.95 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.35 | -2.29 | -1.42 | -1.19 | -2.97 | -1.58 | -2.53 | -1.50 | -2.78 | -2.55 | -2.19 | -1.27 | -1.73 | -1.68|
| full sent KL (full->waitk) |  |  | -3.74 | -1.97 | -2.16 | -1.37 | -2.86 | -1.28 | -1.81 | -2.97 | -3.53 | -2.24 | -2.68 | -1.05 | -2.10 | -1.68|
| dec-waitktgt |  |  | der | komman@@ | de@@ | t | brachte | erte | seine | zufriedenheit | über | der | ü@@ | bung | . | </s>|
| full sent tgt |  |  | der | komman@@ | dan@@ | t | äuß@@ | erte | seine | zufriedenheit | über | der | ü@@ | bung | . | </s>|
| ref | der | komman@@ | dan@@ | t | zeigte | sich | mit | dem | ablauf | der | ü@@ | bung | zufrieden | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | during | the | presentation | , | wol@@ | f | seemed | impres@@ | sed | by | the | educational | pilot | project | .|
| waitk tgt |  |  | während | der | präsentation | wurde | wol@@ | f | von | der | idee | des | pä@@ | da@@ | go@@ | gischen | pi@@ | lot@@ | projekts | beein@@ | druckt | . | </s>|
| waitk prob |  |  | 0.35 | 0.76 | 0.70 | 0.11 | 0.79 | 0.93 | 0.43 | 0.21 | 0.02 | 0.17 | 0.40 | 0.91 | 0.97 | 0.87 | 0.93 | 0.82 | 0.69 | 0.85 | 0.98 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.75 | 0.85 | 0.67 | 0.00 | 0.93 | 0.94 | 0.03 | 0.13 | 0.00 | 0.13 | 0.10 | 0.85 | 0.97 | 0.96 | 0.92 | 0.96 | 0.68 | 0.80 | 0.94 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 16 | 0 | 0 | 2 | 0 | 47 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.01 | -1.79 | -2.30 | -2.56 | -1.12 | -1.33 | -2.63 | -4.35 | -5.19 | -3.32 | -3.90 | -1.80 | -1.09 | -1.04 | -1.38 | -0.96 | -1.71 | -1.78 | -1.40 | -1.69 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.40 | -2.09 | -2.22 | -4.77 | -1.98 | -1.44 | -3.32 | -3.82 | -6.18 | -3.36 | -3.14 | -1.42 | -1.12 | -1.52 | -1.39 | -1.52 | -1.65 | -1.37 | -0.92 | -1.59 | -1.66|
| full sent prob |  |  | 0.45 | 0.80 | 0.68 | 0.02 | 0.65 | 0.94 | 0.29 | 0.05 | 0.01 | 0.50 | 0.08 | 0.97 | 0.96 | 0.90 | 0.91 | 0.96 | 0.65 | 0.78 | 0.94 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 1 | 13 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.25 | -2.04 | -2.14 | -2.74 | -2.45 | -1.38 | -2.50 | -1.88 | -4.72 | -2.71 | -3.45 | -1.03 | -1.21 | -1.33 | -1.46 | -0.98 | -1.63 | -1.91 | -1.31 | -1.68 | -1.65|
| full sent KL (full->waitk) |  |  | -3.32 | -2.06 | -2.23 | -4.77 | -1.80 | -1.44 | -3.37 | -3.83 | -6.18 | -3.37 | -3.12 | -1.51 | -1.11 | -1.48 | -1.38 | -1.52 | -1.63 | -1.35 | -0.93 | -1.59 | -1.66|
| dec-waitktgt |  |  | während | der | präsentation | von | wol@@ | f | beein@@ | der | begeist@@ | der | pä@@ | da@@ | go@@ | gischen | pi@@ | lot@@ | projekts | beein@@ | druckt | . | </s>|
| full sent tgt |  |  | während | der | präsentation | schi@@ | wol@@ | f | vom | dem | initiative | des | e@@ | da@@ | go@@ | gischen | pi@@ | lot@@ | projekts | beein@@ | druckt | . | </s>|
| ref | dabei | zeigte | sich | wol@@ | f | beein@@ | druckt | über | die | modell@@ | projekte | zur | ausbildung | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | he | also | p@@ | raised | the | family-@@ | friendly | approach | within | the | district | .|
| waitk tgt |  |  | er | lob@@ | te | auch | die | familien@@ | freundliche | heran@@ | gehensweise | innerhalb | des | bezir@@ | ks | . | </s>|
| waitk prob |  |  | 0.44 | 0.62 | 0.96 | 0.54 | 0.58 | 0.64 | 0.87 | 0.37 | 0.95 | 0.33 | 0.82 | 0.34 | 0.62 | 0.89 | 0.91|
| dec-waitk prob |  |  | 0.62 | 0.30 | 0.87 | 0.49 | 0.68 | 0.76 | 0.60 | 0.21 | 0.93 | 0.28 | 0.75 | 0.31 | 0.78 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.87 | -3.52 | -1.87 | -2.88 | -2.32 | -1.45 | -1.44 | -3.04 | -1.31 | -2.75 | -2.04 | -2.39 | -1.61 | -1.71 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.75 | -1.88 | -1.08 | -2.47 | -2.16 | -2.01 | -1.30 | -3.15 | -1.21 | -2.32 | -1.83 | -2.96 | -1.90 | -1.76 | -1.68|
| full sent prob |  |  | 0.30 | 0.31 | 0.94 | 0.53 | 0.41 | 0.54 | 0.90 | 0.13 | 0.94 | 0.45 | 0.78 | 0.27 | 0.82 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.06 | -3.27 | -1.38 | -2.58 | -2.32 | -2.30 | -1.28 | -4.15 | -1.34 | -2.41 | -2.00 | -2.39 | -1.41 | -1.78 | -1.67|
| full sent KL (full->waitk) |  |  | -3.64 | -1.89 | -1.14 | -2.49 | -2.07 | -1.91 | -1.52 | -3.11 | -1.21 | -2.37 | -1.85 | -2.96 | -1.91 | -1.76 | -1.68|
| dec-waitktgt |  |  | er | lob@@ | te | auch | die | familien@@ | freundliche | haltung | gehensweise | innerhalb | des | bezir@@ | ks | . | </s>|
| full sent tgt |  |  | er | lob@@ | te | auch | die | familien@@ | freundliche | haltung | gehensweise | innerhalb | des | distri@@ | ks | . | </s>|
| ref | außerdem | lob@@ | te | er | die | familien@@ | freundlichkeit | im | land@@ | kreis | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | he | also | stated | that | an | increasing | number | of | employed | persons | are | looking | after | the | long-term | care | and | support | of | rela@@ | tives | .|
| waitk tgt |  |  | er | hat | auch | erklärt | , | dass | immer | mehr | beschäfti@@ | gte | sich | mit | der | langfristigen | betreuung | und | unterstützung | von | ver@@ | wand@@ | ten | befassen | . | </s>|
| waitk prob |  |  | 0.55 | 0.22 | 0.43 | 0.31 | 0.90 | 0.68 | 0.33 | 0.93 | 0.19 | 0.98 | 0.37 | 0.42 | 0.56 | 0.52 | 0.51 | 0.88 | 0.38 | 0.46 | 0.36 | 0.98 | 0.94 | 0.48 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.46 | 0.29 | 0.40 | 0.29 | 0.89 | 0.50 | 0.42 | 0.94 | 0.12 | 0.96 | 0.02 | 0.24 | 0.36 | 0.14 | 0.44 | 0.88 | 0.68 | 0.70 | 0.59 | 0.97 | 0.92 | 0.40 | 0.89 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 4 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.66 | -2.72 | -3.15 | -2.16 | -1.74 | -2.85 | -2.86 | -1.24 | -2.14 | -1.23 | -3.37 | -2.13 | -2.78 | -2.34 | -1.81 | -1.79 | -1.82 | -2.03 | -1.73 | -1.13 | -1.52 | -1.43 | -1.70 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.06 | -3.19 | -2.82 | -3.18 | -1.67 | -2.12 | -2.97 | -1.28 | -3.80 | -1.03 | -3.51 | -2.79 | -2.18 | -2.29 | -2.27 | -1.80 | -2.42 | -2.82 | -2.61 | -0.98 | -1.28 | -1.84 | -1.80 | -1.69|
| full sent prob |  |  | 0.53 | 0.19 | 0.39 | 0.27 | 0.90 | 0.83 | 0.32 | 0.93 | 0.29 | 0.94 | 0.58 | 0.08 | 0.76 | 0.27 | 0.60 | 0.88 | 0.49 | 0.75 | 0.62 | 0.94 | 0.91 | 0.43 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.96 | -2.95 | -2.65 | -2.83 | -1.73 | -1.69 | -2.42 | -1.37 | -2.40 | -1.33 | -2.15 | -1.51 | -2.17 | -2.61 | -1.51 | -1.79 | -2.21 | -1.88 | -1.74 | -1.32 | -1.58 | -1.82 | -1.76 | -1.67|
| full sent KL (full->waitk) |  |  | -3.09 | -3.19 | -2.82 | -3.15 | -1.68 | -2.31 | -2.98 | -1.27 | -3.79 | -1.02 | -3.69 | -2.79 | -2.35 | -2.34 | -2.32 | -1.80 | -2.41 | -2.84 | -2.63 | -0.96 | -1.27 | -1.83 | -1.79 | -1.69|
| dec-waitktgt |  |  | er | hat | auch | gesagt | , | dass | immer | mehr | arbeitnehmer | gte | beschäftigt | um | der | lang@@ | betreuung | und | unterstützung | von | ver@@ | wand@@ | ten | beschäftigen | . | </s>|
| full sent tgt |  |  | er | erklärte | auch | erklärt | , | dass | immer | mehr | beschäfti@@ | gte | sich | um | der | lang@@ | betreuung | und | unterstützung | von | ver@@ | wand@@ | ten | befassen | . | </s>|
| ref | außerdem | führte | er | an | , | dass | sich | immer | mehr | beschäfti@@ | gte | um | die | pflege | und | betreuung | ihrer | an@@ | gehörigen | kü@@ | mm@@ | erten | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | however | , | nobody | can | afford | to | lose | qualified | workers | , | &quot; | he | added | .|
| waitk tgt |  |  | niemand | kann | es | sich | jedoch | leisten | , | qualifizi@@ | erte | arbeitskrä@@ | fte | zu | verlieren | &quot; | , | fü@@ | gte | er | hinzu | . | </s>|
| waitk prob |  |  | 0.21 | 0.78 | 0.59 | 0.82 | 0.63 | 0.85 | 0.91 | 0.74 | 0.90 | 0.41 | 0.94 | 0.80 | 0.95 | 0.41 | 0.87 | 0.75 | 0.98 | 0.90 | 0.94 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.11 | 0.70 | 0.20 | 0.92 | 0.60 | 0.80 | 0.89 | 0.88 | 0.91 | 0.57 | 0.92 | 0.82 | 0.93 | 0.47 | 0.78 | 0.77 | 0.96 | 0.85 | 0.95 | 0.92 | 0.91|
| dec-waitk rank |  |  | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.66 | -2.53 | -3.11 | -1.40 | -1.93 | -1.67 | -1.80 | -1.44 | -1.59 | -1.89 | -1.51 | -1.89 | -1.33 | -2.45 | -1.90 | -1.74 | -1.22 | -2.02 | -1.13 | -1.57 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.76 | -2.08 | -2.07 | -1.92 | -2.05 | -1.33 | -1.64 | -2.35 | -1.67 | -2.32 | -1.32 | -1.96 | -1.12 | -2.63 | -1.70 | -1.33 | -0.98 | -1.60 | -1.10 | -1.71 | -1.64|
| full sent prob |  |  | 0.05 | 0.85 | 0.83 | 0.94 | 0.31 | 0.93 | 0.88 | 0.93 | 0.90 | 0.38 | 0.95 | 0.82 | 0.95 | 0.59 | 0.85 | 0.86 | 0.96 | 0.88 | 0.96 | 0.92 | 0.91|
| full sent rank |  |  | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.46 | -1.77 | -1.58 | -1.26 | -2.12 | -1.19 | -1.79 | -1.09 | -1.56 | -2.36 | -1.29 | -1.80 | -1.22 | -2.39 | -1.89 | -1.34 | -1.18 | -1.85 | -1.10 | -1.56 | -1.68|
| full sent KL (full->waitk) |  |  | -3.75 | -2.17 | -2.29 | -1.94 | -1.89 | -1.41 | -1.63 | -2.38 | -1.66 | -2.25 | -1.34 | -1.96 | -1.14 | -2.68 | -1.75 | -1.39 | -0.99 | -1.61 | -1.10 | -1.71 | -1.63|
| dec-waitktgt |  |  | aber | kann | sich | sich | jedoch | leisten | , | qualifizi@@ | erte | arbeitskrä@@ | fte | zu | verlieren | &quot; | , | fü@@ | gte | er | hinzu | . | </s>|
| full sent tgt |  |  | doch | kann | es | sich | leisten | leisten | , | qualifizi@@ | erte | arbeitskrä@@ | fte | zu | verlieren | &quot; | , | fü@@ | gte | er | hinzu | . | </s>|
| ref | aber | niemand | könne | es | sich | leisten | , | qualifizi@@ | erte | arbeitskrä@@ | fte | zu | verlieren | , | sagte | er | weiter | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | another | , | particularly | important | factor | is | that | of | net@@ | working | between | universities | and | companies | .|
| waitk tgt |  |  | ein | weiterer | , | besonders | wichtiger | faktor | ist | die | ver@@ | ne@@ | tzung | zwischen | universitäten | und | unternehmen | . | </s>|
| waitk prob |  |  | 0.44 | 0.53 | 0.39 | 0.68 | 0.88 | 0.68 | 0.79 | 0.61 | 0.67 | 0.92 | 0.98 | 0.38 | 0.77 | 0.90 | 0.85 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.44 | 0.45 | 0.38 | 0.92 | 0.80 | 0.77 | 0.73 | 0.67 | 0.88 | 0.98 | 0.98 | 0.41 | 0.47 | 0.91 | 0.90 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.65 | -1.66 | -2.89 | -1.12 | -1.88 | -1.67 | -2.17 | -2.09 | -1.30 | -0.90 | -1.05 | -1.74 | -1.86 | -1.60 | -1.40 | -1.69 | -1.64|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.13 | -2.28 | -2.96 | -2.43 | -1.39 | -1.98 | -1.97 | -2.21 | -2.64 | -1.23 | -1.04 | -2.38 | -1.52 | -1.72 | -1.64 | -1.70 | -1.67|
| full sent prob |  |  | 0.71 | 0.62 | 0.54 | 0.90 | 0.76 | 0.85 | 0.81 | 0.77 | 0.87 | 0.97 | 0.98 | 0.53 | 0.49 | 0.91 | 0.90 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.06 | -2.24 | -2.52 | -1.22 | -2.08 | -1.48 | -1.97 | -1.88 | -1.50 | -1.00 | -1.01 | -1.77 | -1.84 | -1.62 | -1.41 | -1.72 | -1.68|
| full sent KL (full->waitk) |  |  | -3.19 | -2.33 | -3.01 | -2.43 | -1.37 | -2.02 | -2.02 | -2.25 | -2.63 | -1.22 | -1.04 | -2.39 | -1.53 | -1.72 | -1.64 | -1.70 | -1.67|
| dec-waitktgt |  |  | ein | weiterer | , | besonders | wichtiger | faktor | ist | die | ver@@ | ne@@ | tzung | von | universitäten | und | unternehmen | . | </s>|
| full sent tgt |  |  | ein | weiterer | , | besonders | wichtiger | faktor | ist | die | ver@@ | ne@@ | tzung | zwischen | universitäten | und | unternehmen | . | </s>|
| ref | ein | weiterer | , | besonders | wichtiger | faktor | sei | die | ver@@ | ne@@ | tzung | von | hoch@@ | schulen | und | unternehmen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | for | it | is | only | if | a | sufficient | number | of | educational | places | can | be | provided | that | the | need | for | skilled | workers | can | be | covered | .|
| waitk tgt |  |  | denn | nur | wenn | ein | ausreich@@ | ender | teil | der | bildungs@@ | einrichtungen | in | den | mitgliedstaaten | der | europäischen | union | die | notwendigkeit | von | qualifizi@@ | erten | arbeitskrä@@ | ften | decken | kann | . | </s>|
| waitk prob |  |  | 0.57 | 0.52 | 0.69 | 0.35 | 0.74 | 0.51 | 0.46 | 0.75 | 0.47 | 0.43 | 0.18 | 0.15 | 0.30 | 0.12 | 0.57 | 0.91 | 0.08 | 0.20 | 0.28 | 0.48 | 0.87 | 0.62 | 0.94 | 0.09 | 0.83 | 0.85 | 0.91|
| dec-waitk prob |  |  | 0.13 | 0.14 | 0.11 | 0.08 | 0.62 | 0.71 | 0.29 | 0.69 | 0.24 | 0.25 | 0.02 | 0.03 | 0.02 | 0.02 | 0.07 | 0.27 | 0.02 | 0.11 | 0.10 | 0.43 | 0.39 | 0.66 | 0.98 | 0.05 | 0.81 | 0.86 | 0.91|
| dec-waitk rank |  |  | 1 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 4 | 3 | 7 | 1 | 0 | 6 | 0 | 2 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.81 | -3.49 | -3.09 | -3.71 | -2.46 | -1.91 | -3.18 | -2.65 | -3.79 | -2.34 | -4.94 | -3.03 | -4.35 | -4.39 | -5.25 | -4.76 | -4.50 | -4.32 | -3.31 | -1.99 | -3.62 | -2.25 | -1.01 | -3.79 | -1.82 | -1.91 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.58 | -2.27 | -1.93 | -3.08 | -1.74 | -1.85 | -2.96 | -2.10 | -2.55 | -1.63 | -4.73 | -4.10 | -3.88 | -4.89 | -1.52 | -0.96 | -4.75 | -3.95 | -3.01 | -2.45 | -1.27 | -2.44 | -1.30 | -4.61 | -1.86 | -1.96 | -1.68|
| full sent prob |  |  | 0.67 | 0.81 | 0.71 | 0.03 | 0.88 | 0.75 | 0.04 | 0.73 | 0.32 | 0.17 | 0.01 | 0.06 | 0.00 | 0.02 | 0.17 | 0.97 | 0.03 | 0.32 | 0.25 | 0.16 | 0.82 | 0.49 | 0.95 | 0.10 | 0.87 | 0.57 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 7 | 0 | 0 | 3 | 0 | 0 | 1 | 12 | 2 | 23 | 9 | 2 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.76 | -1.35 | -2.07 | -3.02 | -1.38 | -1.51 | -3.15 | -2.36 | -3.31 | -2.06 | -3.76 | -1.72 | -2.07 | -4.39 | -3.08 | -1.02 | -4.66 | -3.34 | -3.20 | -1.55 | -1.77 | -2.45 | -1.27 | -3.56 | -1.70 | -2.64 | -1.66|
| full sent KL (full->waitk) |  |  | -2.83 | -2.54 | -2.26 | -3.10 | -1.90 | -1.87 | -2.86 | -2.13 | -2.58 | -1.65 | -4.74 | -4.09 | -3.90 | -4.89 | -1.62 | -1.49 | -4.75 | -3.98 | -3.04 | -2.41 | -1.58 | -2.36 | -1.28 | -4.61 | -1.90 | -1.76 | -1.68|
| dec-waitktgt |  |  | er | er | , | </s> | ausreich@@ | ender | teil | der | bildungs@@ | stätten | sein | ausreich@@ | genu@@ | erb@@ | union | union | benötigt | notwendigkeit | der | qualifizi@@ | erten | arbeitskrä@@ | ften | er@@ | kann | . | </s>|
| full sent tgt |  |  | denn | nur | wenn | eine | ausreich@@ | ender | bildungs@@ | der | bildungs@@ | stätten | zur | anspruch | genu@@ | für | union | union | für | notwendigkeit | von | fach@@ | erten | arbeitskrä@@ | ften | er@@ | kann | . | </s>|
| ref | denn | nur | wenn | ausreichend | aus@@ | bild@@ | ungsp@@ | lätze | angeboten | würden | , | könne | auch | der | fach@@ | kräf@@ | te@@ | bedarf | ge@@ | deckt | werden | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | previously | , | the | elderly | citizens | were | ho@@ | sted | in | the | service | station | can@@ | teen | .|
| waitk tgt |  |  | früher | waren | die | älteren | bürger | gast@@ | geber | in | der | dienstleistungs@@ | station | can@@ | te@@ | en | . | </s>|
| waitk prob |  |  | 0.19 | 0.15 | 0.49 | 0.79 | 0.67 | 0.51 | 0.88 | 0.24 | 0.30 | 0.18 | 0.45 | 0.65 | 0.80 | 0.60 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.33 | 0.18 | 0.11 | 0.87 | 0.61 | 0.85 | 0.84 | 0.06 | 0.19 | 0.02 | 0.32 | 0.74 | 0.98 | 0.98 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 2 | 7 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.58 | -4.17 | -2.74 | -1.48 | -2.09 | -1.39 | -1.75 | -3.08 | -2.55 | -4.55 | -3.66 | -1.95 | -0.83 | -0.71 | -1.73 | -1.64|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.35 | -4.29 | -2.54 | -1.85 | -2.06 | -3.15 | -1.46 | -2.77 | -3.07 | -4.20 | -3.66 | -2.14 | -2.25 | -3.59 | -1.70 | -1.68|
| full sent prob |  |  | 0.38 | 0.18 | 0.52 | 0.79 | 0.51 | 0.03 | 0.79 | 0.17 | 0.75 | 0.01 | 0.50 | 0.82 | 0.98 | 0.98 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.14 | -3.34 | -2.69 | -1.93 | -2.89 | -2.72 | -2.03 | -2.45 | -1.92 | -4.61 | -3.59 | -1.53 | -0.81 | -0.73 | -1.78 | -1.69|
| full sent KL (full->waitk) |  |  | -3.33 | -4.30 | -2.70 | -1.80 | -1.99 | -2.84 | -1.42 | -2.79 | -3.16 | -4.20 | -3.72 | -2.18 | -2.25 | -3.59 | -1.70 | -1.67|
| dec-waitktgt |  |  | früher | waren | es | älteren | bürger | gast@@ | geber | der | diesem | tan@@ | station | can@@ | te@@ | en | . | </s>|
| full sent tgt |  |  | früher | wurden | die | älteren | bürger | in | geber | der | der | service@@ | station | can@@ | te@@ | en | . | </s>|
| ref | früher | wurden | die | älteren | mit@@ | bürger | in | der | ra@@ | st@@ | stä@@ | tte | be@@ | wir@@ | tet | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | coffee | afternoon | is | now | held | in | the | st. | jo@@ | se@@ | f | nur@@ | sing | home | .|
| waitk tgt |  |  | der | kaffe@@ | e@@ | nachmittag | findet | nun | im | st. | jo@@ | se@@ | f | pf@@ | le@@ | ge@@ | haus | statt | . | </s>|
| waitk prob |  |  | 0.25 | 0.36 | 0.27 | 0.83 | 0.36 | 0.31 | 0.49 | 0.35 | 0.89 | 0.94 | 0.76 | 0.20 | 0.75 | 0.41 | 0.41 | 0.92 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.50 | 0.62 | 0.28 | 0.83 | 0.46 | 0.10 | 0.08 | 0.54 | 0.94 | 0.98 | 0.92 | 0.00 | 0.73 | 0.28 | 0.28 | 0.89 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 130 | 0 | 1 | 1 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.20 | -1.73 | -3.45 | -1.54 | -2.26 | -2.24 | -1.90 | -2.99 | -1.27 | -0.95 | -1.32 | -2.82 | -2.38 | -2.01 | -2.78 | -1.71 | -1.72 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.12 | -3.40 | -3.88 | -1.85 | -2.71 | -3.22 | -2.12 | -4.22 | -1.37 | -1.28 | -1.83 | -4.49 | -2.32 | -2.69 | -3.35 | -1.31 | -1.60 | -1.65|
| full sent prob |  |  | 0.46 | 0.40 | 0.26 | 0.88 | 0.43 | 0.20 | 0.60 | 0.01 | 0.93 | 0.94 | 0.90 | 0.71 | 0.93 | 0.23 | 0.22 | 0.83 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.35 | -3.21 | -3.40 | -1.53 | -2.24 | -3.19 | -2.29 | -0.56 | -1.37 | -1.34 | -1.39 | -1.93 | -1.14 | -1.71 | -2.05 | -2.09 | -1.74 | -1.67|
| full sent KL (full->waitk) |  |  | -4.11 | -3.32 | -3.89 | -1.88 | -2.71 | -3.21 | -2.20 | -4.06 | -1.36 | -1.25 | -1.82 | -4.62 | -2.45 | -2.69 | -3.34 | -1.26 | -1.60 | -1.65|
| dec-waitktgt |  |  | der | kaffe@@ | e@@ | nachmittag | findet | jetzt | in | st. | jo@@ | se@@ | f | statt | le@@ | gehei@@ | heim | statt | . | </s>|
| full sent tgt |  |  | der | kaffe@@ | e@@ | nachmittag | findet | jetzt | im | pf@@ | jo@@ | se@@ | f | pf@@ | le@@ | gehei@@ | heim | statt | . | </s>|
| ref | mittlerweile | findet | dieser | nachmittag | im | pf@@ | le@@ | gehei@@ | m | st. | jo@@ | se@@ | f | statt | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | residents | of | the | home | were | delighted | with | the | delicious | ca@@ | kes | and | tar@@ | ts | .|
| waitk tgt |  |  | die | bewohner | des | hauses | waren | sehr | erfreut | über | die | kö@@ | stlichen | ku@@ | chen | und | tar@@ | ts | . | </s>|
| waitk prob |  |  | 0.61 | 0.42 | 0.42 | 0.52 | 0.55 | 0.25 | 0.39 | 0.74 | 0.62 | 0.57 | 0.91 | 0.96 | 0.98 | 0.89 | 0.44 | 0.38 | 0.89 | 0.90|
| dec-waitk prob |  |  | 0.41 | 0.46 | 0.62 | 0.48 | 0.39 | 0.17 | 0.62 | 0.72 | 0.61 | 0.37 | 0.84 | 0.86 | 0.93 | 0.83 | 0.05 | 0.87 | 0.89 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.61 | -1.98 | -1.97 | -2.62 | -3.12 | -2.84 | -2.21 | -2.37 | -2.17 | -2.69 | -1.68 | -1.49 | -1.33 | -2.02 | -2.58 | -1.25 | -1.78 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.07 | -1.96 | -2.51 | -2.29 | -2.65 | -3.20 | -3.13 | -2.19 | -2.32 | -2.53 | -1.22 | -1.04 | -0.96 | -1.70 | -3.55 | -4.32 | -1.74 | -1.70|
| full sent prob |  |  | 0.69 | 0.50 | 0.59 | 0.83 | 0.39 | 0.05 | 0.19 | 0.35 | 0.81 | 0.49 | 0.92 | 0.91 | 0.95 | 0.89 | 0.07 | 0.89 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.63 | -2.13 | -2.34 | -1.45 | -3.53 | -2.80 | -3.75 | -2.93 | -1.86 | -2.55 | -1.32 | -1.24 | -1.22 | -1.79 | -2.73 | -1.15 | -1.75 | -1.67|
| full sent KL (full->waitk) |  |  | -3.22 | -1.95 | -2.48 | -2.42 | -2.64 | -3.21 | -3.00 | -1.98 | -2.41 | -2.58 | -1.28 | -1.09 | -0.97 | -1.75 | -3.55 | -4.33 | -1.74 | -1.69|
| dec-waitktgt |  |  | die | bewohner | des | hauses | waren | begeist@@ | erfreut | über | die | kö@@ | stlichen | ku@@ | chen | und | tor@@ | ts | . | </s>|
| full sent tgt |  |  | die | bewohner | des | hauses | waren | mit | erfreut | über | die | kö@@ | stlichen | ku@@ | chen | und | tor@@ | ts | . | </s>|
| ref | die | heim@@ | bewohner | freu@@ | ten | sich | auf | die | le@@ | ck@@ | eren | ku@@ | chen | und | tor@@ | ten | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | a | decision | is | expected | to | be | made | in | the | coming | year | .|
| waitk tgt |  |  | es | wird | erwartet | , | dass | in | der | kommenden | saison | eine | entscheidung | getroffen | wird | . | </s>|
| waitk prob |  |  | 0.23 | 0.76 | 0.46 | 0.91 | 0.72 | 0.25 | 0.31 | 0.51 | 0.09 | 0.78 | 0.88 | 0.70 | 0.79 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.01 | 0.60 | 0.59 | 0.90 | 0.75 | 0.05 | 0.22 | 0.55 | 0.00 | 0.57 | 0.91 | 0.67 | 0.91 | 0.90 | 0.91|
| dec-waitk rank |  |  | 8 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.47 | -2.22 | -2.03 | -1.70 | -1.93 | -2.77 | -2.10 | -1.79 | -2.81 | -2.44 | -1.48 | -1.97 | -1.40 | -1.70 | -1.66|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.90 | -1.76 | -2.75 | -1.61 | -2.02 | -3.41 | -3.10 | -1.73 | -4.95 | -1.96 | -1.73 | -2.08 | -1.93 | -1.68 | -1.67|
| full sent prob |  |  | 0.21 | 0.75 | 0.69 | 0.89 | 0.70 | 0.03 | 0.03 | 0.34 | 0.05 | 0.68 | 0.91 | 0.67 | 0.89 | 0.90 | 0.90|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 2 | 4 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.72 | -1.83 | -1.84 | -1.78 | -1.91 | -2.33 | -3.85 | -1.51 | -3.87 | -2.34 | -1.47 | -1.99 | -1.48 | -1.71 | -1.69|
| full sent KL (full->waitk) |  |  | -3.92 | -1.84 | -2.78 | -1.60 | -2.00 | -3.48 | -3.06 | -1.72 | -4.93 | -2.03 | -1.73 | -2.08 | -1.92 | -1.68 | -1.67|
| dec-waitktgt |  |  | eine | wird | erwartet | , | dass | eine | dem | kommenden | jahres@@ | eine | entscheidung | getroffen | wird | . | </s>|
| full sent tgt |  |  | eine | wird | erwartet | , | dass | im | den | nächsten | zeit | eine | entscheidung | getroffen | wird | . | </s>|
| ref | eine | entscheidung | darüber | wird | voraus@@ | sichtlich | bereits | im | kommenden | jahr | fallen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | deep | cr@@ | acks | in | a | number | of | individual | stones | testi@@ | fy | to | the | weather | damage | , | however | , | at | present | the | wall | is | not | in | danger | of | collapse | .|
| waitk tgt |  |  | tiefe | ri@@ | sse | in | einer | reihe | von | einzel@@ | st@@ | einen | be@@ | zeugen | den | we@@ | tter@@ | schaden | , | aber | derzeit | ist | die | wand | nicht | in | gefahr | , | zusammen@@ | brechen | . | </s>|
| waitk prob |  |  | 0.31 | 0.66 | 0.95 | 0.82 | 0.32 | 0.72 | 0.71 | 0.26 | 0.27 | 0.98 | 0.21 | 0.66 | 0.39 | 0.77 | 0.97 | 0.68 | 0.45 | 0.24 | 0.27 | 0.29 | 0.79 | 0.62 | 0.81 | 0.60 | 0.64 | 0.52 | 0.42 | 0.36 | 0.88 | 0.90|
| dec-waitk prob |  |  | 0.82 | 0.93 | 0.91 | 0.56 | 0.62 | 0.31 | 0.72 | 0.48 | 0.45 | 0.96 | 0.28 | 0.26 | 0.59 | 0.40 | 0.95 | 0.65 | 0.21 | 0.14 | 0.25 | 0.24 | 0.77 | 0.41 | 0.75 | 0.74 | 0.99 | 0.30 | 0.21 | 0.36 | 0.28 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.13 | -0.99 | -1.46 | -2.18 | -2.25 | -2.41 | -2.19 | -1.85 | -3.32 | -1.13 | -3.53 | -1.27 | -2.08 | -4.44 | -1.22 | -3.05 | -3.14 | -3.69 | -3.34 | -4.24 | -2.20 | -1.54 | -2.16 | -1.77 | -0.67 | -3.59 | -3.38 | -3.03 | -1.65 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.85 | -2.83 | -1.10 | -1.80 | -2.84 | -1.80 | -2.38 | -3.63 | -4.79 | -0.99 | -3.20 | -1.34 | -2.60 | -2.11 | -1.08 | -2.84 | -3.10 | -4.33 | -3.02 | -3.98 | -2.14 | -1.60 | -2.02 | -2.60 | -2.02 | -3.10 | -3.26 | -2.56 | -1.38 | -1.71|
| full sent prob |  |  | 0.40 | 0.93 | 0.96 | 0.80 | 0.31 | 0.58 | 0.64 | 0.50 | 0.65 | 0.98 | 0.50 | 0.16 | 0.67 | 0.67 | 0.96 | 0.46 | 0.76 | 0.40 | 0.25 | 0.51 | 0.81 | 0.33 | 0.88 | 0.45 | 0.97 | 0.32 | 0.25 | 0.45 | 0.88 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.07 | -1.07 | -1.09 | -2.15 | -3.08 | -2.22 | -2.13 | -1.73 | -2.20 | -1.02 | -2.60 | -1.15 | -1.99 | -2.94 | -1.16 | -4.47 | -1.94 | -2.54 | -3.08 | -2.27 | -2.03 | -1.55 | -1.64 | -3.23 | -0.76 | -3.41 | -3.42 | -2.61 | -1.75 | -1.69|
| full sent KL (full->waitk) |  |  | -3.76 | -2.83 | -1.14 | -1.96 | -2.78 | -1.95 | -2.34 | -3.64 | -4.83 | -1.00 | -3.24 | -1.31 | -2.60 | -2.28 | -1.09 | -2.73 | -3.30 | -4.39 | -3.02 | -4.04 | -2.16 | -1.57 | -2.11 | -2.45 | -2.02 | -3.12 | -3.27 | -2.60 | -1.81 | -1.70|
| dec-waitktgt |  |  | tiefe | ri@@ | sse | in | einer | anzahl | von | einzel@@ | st@@ | einen | be@@ | legen | den | we@@ | tter@@ | schaden | . | </s> | derzeit | ist | die | mauer | nicht | in | gefahr | , | zu | brechen | zu | </s>|
| full sent tgt |  |  | tiefe | ri@@ | sse | in | einer | reihe | von | einzel@@ | st@@ | einen | be@@ | legen | den | we@@ | tter@@ | schaden | , | aber | derzeit | ist | die | mauer | nicht | in | gefahr | , | zusammen@@ | brechen | . | </s>|
| ref | tiefe | ri@@ | sse | in | einzelnen | st@@ | einen | zeugen | von | wi@@ | tter@@ | ungs@@ | schäden | , | jedoch | ist | die | mauer | derzeit | nicht | ein@@ | stur@@ | z@@ | gefährdet | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ö@@ | z@@ | dem@@ | ir | wants | jazz | training | in | stutt@@ | gart|
| waitk tgt |  |  | ö@@ | z@@ | de@@ | mir | möchte | ja@@ | z@@ | z | training | in | st@@ | utt@@ | gar@@ | t | und | in | st@@ | utt@@ | gar@@ | t | absol@@ | vi@@ | eren | . | </s>|
| waitk prob |  |  | 0.73 | 0.95 | 0.91 | 0.97 | 0.36 | 0.40 | 0.71 | 0.93 | 0.81 | 0.78 | 0.95 | 0.95 | 0.94 | 0.95 | 0.07 | 0.11 | 0.20 | 0.95 | 0.94 | 0.94 | 0.12 | 0.96 | 0.91 | 0.73 | 0.91|
| dec-waitk prob |  |  | 0.79 | 0.90 | 0.89 | 0.02 | 0.00 | 0.82 | 0.72 | 0.89 | 0.14 | 0.79 | 0.99 | 0.98 | 0.97 | 0.85 | 0.00 | 0.04 | 0.59 | 0.98 | 0.97 | 0.77 | 0.01 | 0.73 | 0.81 | 0.21 | 0.93|
| dec-waitk rank |  |  | 0 | 0 | 0 | 9 | 6 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 30 | 1 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 1 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.91 | -1.66 | -1.59 | -3.71 | -2.07 | -1.46 | -1.78 | -1.59 | -3.34 | -2.07 | -0.90 | -1.01 | -1.04 | -2.11 | -3.59 | -2.83 | -2.90 | -1.03 | -1.05 | -2.72 | -3.64 | -2.65 | -2.34 | -3.03 | -1.44|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.33 | -1.17 | -1.31 | -0.23 | -2.28 | -3.50 | -1.45 | -1.33 | -1.22 | -2.27 | -1.28 | -1.30 | -1.42 | -1.18 | -4.64 | -5.20 | -4.30 | -1.26 | -1.40 | -1.22 | -4.61 | -0.93 | -1.44 | -1.81 | -1.67|
| full sent prob |  |  | 0.72 | 0.96 | 0.94 | 0.65 | 0.23 | 0.16 | 0.59 | 0.78 | 0.15 | 0.86 | 0.99 | 0.98 | 0.97 | 0.85 | 0.00 | 0.16 | 0.86 | 0.97 | 0.97 | 0.80 | 0.01 | 0.80 | 0.82 | 0.26 | 0.93|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 19 | 1 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -2.33 | -1.17 | -1.24 | -2.57 | -2.43 | -3.47 | -2.17 | -2.22 | -2.80 | -1.69 | -0.88 | -1.02 | -1.05 | -2.12 | -4.21 | -3.61 | -1.27 | -1.05 | -1.05 | -2.50 | -3.86 | -2.21 | -2.21 | -3.25 | -1.48|
| full sent KL (full->waitk) |  |  | -2.28 | -1.22 | -1.35 | -0.74 | -2.45 | -3.29 | -1.39 | -1.25 | -1.23 | -2.32 | -1.29 | -1.30 | -1.42 | -1.18 | -4.65 | -5.21 | -4.34 | -1.26 | -1.40 | -1.24 | -4.61 | -0.98 | -1.45 | -1.84 | -1.67|
| dec-waitktgt |  |  | ö@@ | z@@ | de@@ | mi@@ | </s> | ja@@ | z@@ | z | in | in | st@@ | utt@@ | gar@@ | t | </s> | </s> | st@@ | utt@@ | gar@@ | t | </s> | vi@@ | eren | </s> | </s>|
| full sent tgt |  |  | ö@@ | z@@ | de@@ | mir | will | ja@@ | z@@ | z | in | in | st@@ | utt@@ | gar@@ | t | </s> | </s> | st@@ | utt@@ | gar@@ | t | </s> | vi@@ | eren | </s> | </s>|
| ref | ö@@ | z@@ | de@@ | mir | will | ja@@ | zz@@ | ausbildung | in | st@@ | utt@@ | gar@@ | t | erhalten | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | jazz | and | classical | music | belong | together | at | the | jazz | location | of | stutt@@ | gart | .|
| waitk tgt |  |  | ja@@ | z@@ | z | und | klassi@@ | sche | musik | gehören | zusammen | an | der | ja@@ | zz@@ | -@@ | location | st@@ | utt@@ | gar@@ | t | . | </s>|
| waitk prob |  |  | 0.52 | 0.78 | 0.96 | 0.84 | 0.93 | 0.75 | 0.96 | 0.77 | 0.59 | 0.50 | 0.86 | 0.76 | 0.61 | 0.24 | 0.25 | 0.34 | 0.97 | 0.95 | 0.73 | 0.83 | 0.91|
| dec-waitk prob |  |  | 0.72 | 0.92 | 0.97 | 0.88 | 0.95 | 0.53 | 0.96 | 0.65 | 0.10 | 0.13 | 0.65 | 0.80 | 0.86 | 0.09 | 0.64 | 0.51 | 0.95 | 0.96 | 0.26 | 0.89 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.09 | -1.24 | -1.05 | -1.74 | -1.20 | -2.77 | -1.12 | -2.48 | -3.51 | -1.69 | -2.37 | -2.10 | -0.94 | -1.93 | -1.98 | -2.11 | -1.32 | -1.16 | -1.71 | -1.75 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.54 | -1.38 | -1.18 | -2.06 | -1.34 | -1.64 | -1.18 | -1.83 | -2.19 | -2.34 | -1.65 | -2.47 | -1.48 | -4.32 | -4.34 | -2.61 | -1.06 | -1.32 | -1.81 | -2.00 | -1.66|
| full sent prob |  |  | 0.54 | 0.92 | 0.95 | 0.88 | 0.94 | 0.50 | 0.93 | 0.59 | 0.11 | 0.07 | 0.71 | 0.75 | 0.84 | 0.09 | 0.74 | 0.51 | 0.95 | 0.96 | 0.38 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.09 | -1.05 | -1.22 | -1.79 | -1.33 | -1.77 | -1.39 | -2.74 | -3.12 | -1.19 | -2.20 | -2.41 | -1.00 | -1.94 | -1.64 | -2.12 | -1.30 | -1.15 | -1.90 | -1.75 | -1.66|
| full sent KL (full->waitk) |  |  | -3.46 | -1.38 | -1.16 | -2.06 | -1.32 | -1.64 | -1.16 | -1.79 | -2.19 | -2.31 | -1.69 | -2.44 | -1.48 | -4.33 | -4.36 | -2.61 | -1.06 | -1.32 | -1.86 | -2.00 | -1.66|
| dec-waitktgt |  |  | ja@@ | z@@ | z | und | klassi@@ | sche | musik | gehören | am | am | der | ja@@ | zz@@ | location | location | st@@ | utt@@ | gar@@ | ts | . | </s>|
| full sent tgt |  |  | ja@@ | z@@ | z | und | klassi@@ | sche | musik | gehören | am | am | der | ja@@ | zz@@ | location | location | st@@ | utt@@ | gar@@ | ts | . | </s>|
| ref | ja@@ | z@@ | z | und | klassi@@ | k | gehören | gerade | am | ja@@ | zz@@ | standort | st@@ | utt@@ | gar@@ | t | zusammen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | according | to | the | details | provided | , | the | tunnel | had | not | yet | been | put | into | use | .|
| waitk tgt |  |  | nach | den | angaben | , | die | zur | verfügung | gestellt | wurden | , | war | der | tun@@ | nel | noch | nicht | in | betrieb | . | </s>|
| waitk prob |  |  | 0.25 | 0.58 | 0.42 | 0.33 | 0.84 | 0.12 | 0.94 | 0.88 | 0.68 | 0.92 | 0.42 | 0.74 | 0.95 | 0.92 | 0.79 | 0.92 | 0.59 | 0.52 | 0.54 | 0.90|
| dec-waitk prob |  |  | 0.17 | 0.26 | 0.48 | 0.44 | 0.66 | 0.03 | 0.92 | 0.36 | 0.81 | 0.88 | 0.64 | 0.76 | 0.97 | 0.94 | 0.85 | 0.89 | 0.68 | 0.89 | 0.04 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.99 | -3.39 | -2.96 | -3.36 | -2.83 | -3.47 | -1.42 | -2.13 | -1.60 | -1.80 | -2.32 | -1.97 | -1.06 | -1.23 | -1.66 | -1.69 | -2.31 | -1.00 | -1.61 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.53 | -2.52 | -2.90 | -3.87 | -1.78 | -4.09 | -1.31 | -1.09 | -1.98 | -1.55 | -2.72 | -2.08 | -1.30 | -1.38 | -1.91 | -1.42 | -3.09 | -2.54 | -2.61 | -1.71|
| full sent prob |  |  | 0.17 | 0.63 | 0.10 | 0.23 | 0.87 | 0.04 | 0.92 | 0.54 | 0.77 | 0.90 | 0.62 | 0.73 | 0.95 | 0.94 | 0.84 | 0.88 | 0.73 | 0.86 | 0.04 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0|
| full sent KL (waitk->full) |  |  | -3.87 | -2.51 | -3.84 | -3.11 | -1.84 | -4.10 | -1.45 | -2.07 | -1.61 | -1.77 | -2.25 | -2.09 | -1.24 | -1.21 | -1.68 | -1.74 | -2.10 | -1.12 | -1.57 | -1.66|
| full sent KL (full->waitk) |  |  | -3.52 | -2.68 | -2.77 | -3.82 | -1.93 | -4.09 | -1.31 | -1.22 | -1.96 | -1.56 | -2.71 | -2.06 | -1.28 | -1.38 | -1.91 | -1.42 | -3.11 | -2.53 | -2.61 | -1.70|
| dec-waitktgt |  |  | gemäß | den | angaben | , | die | gemacht | verfügung | standen | wurden | , | war | der | tun@@ | nel | noch | nicht | in | betrieb | genommen | </s>|
| full sent tgt |  |  | nach | den | einzelheiten | war | die | gemacht | verfügung | gestellt | wurden | , | war | der | tun@@ | nel | noch | nicht | in | betrieb | genommen | </s>|
| ref | der | tun@@ | nel | war | den | angaben | zufolge | noch | nicht | in | gebrauch | genommen | worden | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | both | the | us | authorities | and | the | mex@@ | ic@@ | an | security | forces | are | engaged | in | an | ongoing | battle | against | the | drug | car@@ | te@@ | ls | .|
| waitk tgt |  |  | sowohl | die | us-@@ | behörden | als | auch | die | mexi@@ | kanischen | sicherheit@@ | skrä@@ | fte | sind | in | einem | ständigen | kampf | gegen | die | drogen@@ | kar@@ | t@@ | elle | tätig | . | </s>|
| waitk prob |  |  | 0.70 | 0.87 | 0.63 | 0.89 | 0.88 | 0.92 | 0.69 | 0.98 | 0.86 | 0.85 | 0.96 | 0.91 | 0.20 | 0.37 | 0.43 | 0.34 | 0.83 | 0.88 | 0.61 | 0.86 | 0.96 | 0.95 | 0.95 | 0.12 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.16 | 0.74 | 0.70 | 0.85 | 0.93 | 0.91 | 0.59 | 0.99 | 0.35 | 0.95 | 0.97 | 0.91 | 0.28 | 0.22 | 0.20 | 0.40 | 0.78 | 0.92 | 0.48 | 0.96 | 0.96 | 0.94 | 0.94 | 0.10 | 0.91 | 0.91|
| dec-waitk rank |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.05 | -2.48 | -1.50 | -1.59 | -1.36 | -1.60 | -2.27 | -0.92 | -2.67 | -1.04 | -1.01 | -1.58 | -3.85 | -3.21 | -2.93 | -2.43 | -2.12 | -1.52 | -2.53 | -0.99 | -1.16 | -1.13 | -1.11 | -3.26 | -1.67 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -1.78 | -1.61 | -2.12 | -1.48 | -1.65 | -1.55 | -2.11 | -0.99 | -1.25 | -1.58 | -1.15 | -1.51 | -3.57 | -3.20 | -2.54 | -2.94 | -1.78 | -1.83 | -2.08 | -1.58 | -1.09 | -1.19 | -1.05 | -3.83 | -1.61 | -1.66|
| full sent prob |  |  | 0.83 | 0.89 | 0.77 | 0.73 | 0.91 | 0.90 | 0.90 | 0.90 | 0.86 | 0.95 | 0.97 | 0.92 | 0.06 | 0.65 | 0.56 | 0.32 | 0.81 | 0.92 | 0.87 | 0.96 | 0.96 | 0.94 | 0.90 | 0.07 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.46 | -1.75 | -1.42 | -2.04 | -1.51 | -1.73 | -1.49 | -1.51 | -1.78 | -1.09 | -1.01 | -1.49 | -2.93 | -2.30 | -2.62 | -2.39 | -2.06 | -1.46 | -1.57 | -1.04 | -1.13 | -1.14 | -1.34 | -3.73 | -1.68 | -1.67|
| full sent KL (full->waitk) |  |  | -2.15 | -1.71 | -2.16 | -1.39 | -1.64 | -1.54 | -2.28 | -0.92 | -1.60 | -1.58 | -1.16 | -1.52 | -3.54 | -3.32 | -2.68 | -2.92 | -1.80 | -1.84 | -2.24 | -1.57 | -1.09 | -1.19 | -1.02 | -3.82 | -1.61 | -1.65|
| dec-waitktgt |  |  | beide | die | us-@@ | behörden | als | auch | die | mexi@@ | kanische | sicherheit@@ | skrä@@ | fte | sind | in | einer | ständigen | kampf | gegen | die | drogen@@ | kar@@ | t@@ | elle | ver@@ | . | </s>|
| full sent tgt |  |  | sowohl | die | us-@@ | behörden | als | auch | die | mexi@@ | kanischen | sicherheit@@ | skrä@@ | fte | führen | in | einem | ständigen | kampf | gegen | die | drogen@@ | kar@@ | t@@ | elle | . | . | </s>|
| ref | sowohl | die | us-@@ | behörden | als | auch | die | mexi@@ | kanischen | sicherheit@@ | skrä@@ | fte | befinden | sich | in | einem | dauer@@ | -@@ | kampf | gegen | die | drogen@@ | kar@@ | t@@ | elle | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | since | 2006 | , | more | than | 7@@ | 7@@ | ,000 | people | have | been | killed | in | conjunction | with | drug | crime | in | mexico | .|
| waitk tgt |  |  | seit | 2006 | sind | mehr | als | 7@@ | 7@@ | .000 | menschen | get@@ | ö@@ | tet | worden | , | die | im | zusammenhang | mit | der | drogen@@ | kriminalität | in | mexiko | sind | . | </s>|
| waitk prob |  |  | 0.69 | 0.92 | 0.22 | 0.44 | 0.91 | 0.86 | 0.77 | 0.87 | 0.77 | 0.19 | 0.98 | 0.93 | 0.78 | 0.48 | 0.25 | 0.23 | 0.74 | 0.90 | 0.53 | 0.91 | 0.84 | 0.86 | 0.93 | 0.09 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.77 | 0.96 | 0.00 | 0.08 | 0.88 | 0.96 | 0.91 | 0.79 | 0.89 | 0.54 | 0.96 | 0.95 | 0.89 | 0.04 | 0.01 | 0.14 | 0.95 | 0.90 | 0.51 | 0.86 | 0.87 | 0.82 | 0.96 | 0.01 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 12 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 27 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.37 | -1.09 | -1.57 | -1.87 | -1.85 | -1.13 | -1.20 | -1.92 | -1.34 | -2.01 | -1.16 | -1.29 | -1.60 | -3.16 | -2.67 | -4.15 | -0.98 | -1.72 | -2.09 | -1.68 | -1.75 | -2.09 | -1.11 | -4.54 | -1.65 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.59 | -1.41 | -3.66 | -2.41 | -1.63 | -1.86 | -1.93 | -1.36 | -1.97 | -3.28 | -1.02 | -1.40 | -2.03 | -2.48 | -3.50 | -2.75 | -2.22 | -1.71 | -2.11 | -1.32 | -1.89 | -1.99 | -1.35 | -5.20 | -1.69 | -1.69|
| full sent prob |  |  | 0.83 | 0.93 | 0.32 | 0.09 | 0.91 | 0.95 | 0.74 | 0.88 | 0.92 | 0.00 | 0.97 | 0.92 | 0.91 | 0.44 | 0.14 | 0.08 | 0.94 | 0.91 | 0.62 | 0.90 | 0.84 | 0.91 | 0.96 | 0.00 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 38 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.77 | -1.36 | -2.09 | -2.48 | -1.68 | -1.13 | -1.66 | -1.57 | -1.21 | -1.92 | -1.08 | -1.48 | -1.36 | -2.52 | -3.42 | -2.92 | -1.02 | -1.67 | -1.95 | -1.47 | -1.95 | -1.62 | -1.10 | -4.14 | -1.72 | -1.67|
| full sent KL (full->waitk) |  |  | -2.63 | -1.38 | -3.76 | -2.44 | -1.65 | -1.86 | -1.82 | -1.42 | -1.99 | -3.27 | -1.03 | -1.38 | -2.04 | -2.65 | -3.54 | -2.78 | -2.21 | -1.72 | -2.14 | -1.35 | -1.87 | -2.05 | -1.35 | -5.21 | -1.69 | -1.68|
| dec-waitktgt |  |  | seit | 2006 | mehr | es | als | 7@@ | 7@@ | .000 | menschen | get@@ | ö@@ | tet | worden | . | </s> | in | zusammenhang | mit | der | drogen@@ | kriminalität | in | mexiko | ver@@ | . | </s>|
| full sent tgt |  |  | seit | 2006 | wurden | in | als | 7@@ | 7@@ | .000 | menschen | in | ö@@ | tet | worden | , | zusammen | in | zusammenhang | mit | der | drogen@@ | kriminalität | in | mexiko | ums | . | </s>|
| ref | seit | 2006 | wurden | in | mexiko | mehr | als | 7@@ | 7. | 000 | menschen | im | zusammenhang | mit | der | drogen@@ | kriminalität | get@@ | ö@@ | tet | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | railway | system | was | equipped | in | such | a | way | that | electr@@ | ically | powered | car@@ | ts | could | be | used | on | it | .|
| waitk tgt |  |  | das | eisenbahn@@ | system | wurde | so | ausgestattet | , | dass | elekt@@ | rische | energie | betrie@@ | bene | wagen | in | einem | einzigen | fahrzeug | eingesetzt | werden | können | . | </s>|
| waitk prob |  |  | 0.45 | 0.48 | 0.85 | 0.52 | 0.82 | 0.30 | 0.91 | 0.77 | 0.20 | 0.28 | 0.07 | 0.11 | 0.94 | 0.35 | 0.09 | 0.09 | 0.04 | 0.09 | 0.33 | 0.90 | 0.39 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.32 | 0.74 | 0.58 | 0.22 | 0.08 | 0.71 | 0.05 | 0.08 | 0.00 | 0.65 | 0.43 | 0.00 | 0.45 | 0.07 | 0.01 | 0.01 | 0.00 | 0.03 | 0.01 | 0.87 | 0.27 | 0.89 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 1 | 1 | 0 | 2 | 1 | 65 | 0 | 0 | 104 | 0 | 3 | 5 | 6 | 34 | 1 | 26 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.96 | -1.35 | -1.94 | -2.88 | -3.11 | -1.65 | -3.19 | -3.25 | -2.80 | -2.35 | -3.28 | -1.26 | -3.79 | -3.55 | -4.78 | -3.92 | -5.87 | -5.37 | -4.84 | -1.75 | -2.42 | -1.75 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.29 | -2.55 | -1.55 | -2.61 | -1.22 | -3.43 | -0.98 | -1.06 | -3.24 | -4.55 | -4.97 | -4.57 | -0.83 | -3.02 | -4.95 | -4.83 | -5.74 | -5.23 | -3.46 | -1.63 | -2.91 | -1.67 | -1.68|
| full sent prob |  |  | 0.57 | 0.58 | 0.62 | 0.35 | 0.83 | 0.52 | 0.90 | 0.60 | 0.02 | 0.66 | 0.00 | 0.03 | 0.96 | 0.20 | 0.01 | 0.00 | 0.00 | 0.12 | 0.04 | 0.88 | 0.17 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 182 | 6 | 0 | 0 | 14 | 31 | 32 | 0 | 3 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.54 | -1.90 | -2.54 | -2.70 | -1.69 | -1.92 | -1.76 | -1.99 | -3.62 | -2.31 | -3.76 | -4.19 | -1.07 | -3.44 | -3.51 | -3.74 | -5.32 | -4.78 | -4.40 | -1.84 | -1.79 | -1.71 | -1.69|
| full sent KL (full->waitk) |  |  | -3.39 | -2.50 | -1.58 | -2.68 | -1.71 | -3.41 | -1.62 | -1.43 | -3.26 | -4.55 | -4.95 | -4.58 | -1.23 | -3.07 | -4.96 | -4.81 | -5.74 | -5.24 | -3.47 | -1.64 | -2.92 | -1.68 | -1.68|
| dec-waitktgt |  |  | eisenbahn@@ | eisenbahn@@ | system | ist | in | ausgestattet | </s> | </s> | </s> | rische | energie | </s> | bene | autos | </s> | betrieb | </s> | zustand | betrieben | werden | konnten | . | </s>|
| full sent tgt |  |  | das | eisenbahn@@ | system | wurde | so | ausgestattet | , | dass | auf | rische | kar@@ | auf | bene | wagen | darauf | das | system | fahrzeug | unter@@ | werden | konnten | . | </s>|
| ref | die | glei@@ | san@@ | lage | war | so | ausgestattet | , | dass | dort | elektri@@ | sch | betrie@@ | bene | wagen | eingesetzt | werden | konnten | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | on | the | mex@@ | ic@@ | an | side | , | the | entrance | is | located | in | a | building | located | 80 | metres | from | the | border | .|
| waitk tgt |  |  | auf | der | mexi@@ | kanischen | seite | hat | der | eingang | sich | in | einem | gebäude | , | das | 80 | m | vom | grenz@@ | übergang | entfernt | liegt | . | </s>|
| waitk prob |  |  | 0.24 | 0.66 | 0.95 | 0.95 | 0.94 | 0.09 | 0.53 | 0.68 | 0.08 | 0.48 | 0.49 | 0.68 | 0.17 | 0.51 | 0.65 | 0.41 | 0.66 | 0.32 | 0.27 | 0.94 | 0.63 | 0.69 | 0.90|
| dec-waitk prob |  |  | 0.14 | 0.18 | 0.96 | 0.88 | 0.97 | 0.00 | 0.25 | 0.80 | 0.03 | 0.32 | 0.38 | 0.89 | 0.07 | 0.56 | 0.78 | 0.40 | 0.57 | 0.47 | 0.74 | 0.56 | 0.20 | 0.84 | 0.92|
| dec-waitk rank |  |  | 1 | 1 | 0 | 0 | 0 | 64 | 0 | 0 | 6 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.66 | -2.10 | -1.11 | -1.21 | -1.12 | -1.57 | -3.87 | -1.69 | -3.23 | -3.19 | -2.82 | -1.30 | -1.79 | -2.60 | -1.54 | -1.82 | -2.87 | -2.37 | -1.55 | -3.17 | -1.94 | -1.80 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.88 | -2.08 | -1.23 | -1.12 | -1.41 | -4.88 | -2.50 | -2.17 | -4.54 | -2.69 | -2.25 | -2.71 | -3.63 | -3.22 | -2.16 | -2.35 | -1.88 | -4.10 | -4.18 | -0.87 | -1.95 | -2.53 | -1.70|
| full sent prob |  |  | 0.25 | 0.36 | 0.93 | 0.96 | 0.98 | 0.00 | 0.16 | 0.69 | 0.01 | 0.79 | 0.71 | 0.33 | 0.30 | 0.78 | 0.75 | 0.27 | 0.05 | 0.05 | 0.51 | 0.56 | 0.39 | 0.71 | 0.91|
| full sent rank |  |  | 0 | 1 | 0 | 0 | 0 | 12 | 1 | 0 | 8 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.87 | -1.76 | -1.34 | -1.10 | -0.97 | -2.12 | -2.66 | -2.22 | -3.38 | -1.87 | -2.27 | -2.21 | -2.82 | -1.60 | -1.72 | -1.63 | -2.19 | -2.73 | -2.78 | -3.14 | -2.03 | -1.97 | -1.67|
| full sent KL (full->waitk) |  |  | -3.91 | -2.17 | -1.21 | -1.19 | -1.43 | -4.89 | -2.47 | -2.11 | -4.54 | -2.83 | -2.34 | -2.39 | -3.62 | -3.31 | -2.15 | -2.35 | -1.69 | -4.02 | -4.13 | -0.87 | -2.03 | -2.46 | -1.70|
| dec-waitktgt |  |  | über | mexi@@ | mexi@@ | kanischen | seite | </s> | der | eingang | seinen | in | einem | gebäude | befindet | das | 80 | meter | vom | grenz@@ | übergang | entfernt | ist | . | </s>|
| full sent tgt |  |  | auf | mexi@@ | mexi@@ | kanischen | seite | befindet | man | eingang | einen | in | einem | 80 | befindet | das | 80 | meter | von | rand | übergang | entfernt | ist | . | </s>|
| ref | auf | mexi@@ | kan@@ | ischer | seite | liegt | der | zugang | in | einem | gebäude | , | das | 80 | meter | von | der | grenze | entfernt | ist | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | according | to | the | authorities | , | a | lad@@ | der | runs | 20 | metres | underground | to | the | actual | entrance | of | the | tunnel | .|
| waitk tgt |  |  | nach | angaben | der | behörden | wird | eine | leiter | 20 | meter | unter@@ | halb | der | eigent@@ | lichen | ein@@ | fahrt | des | tun@@ | n@@ | els | . | </s>|
| waitk prob |  |  | 0.25 | 0.59 | 0.90 | 0.80 | 0.10 | 0.42 | 0.58 | 0.65 | 0.55 | 0.58 | 0.54 | 0.25 | 0.31 | 0.91 | 0.63 | 0.76 | 0.82 | 0.95 | 0.93 | 0.96 | 0.20 | 0.91|
| dec-waitk prob |  |  | 0.17 | 0.69 | 0.85 | 0.90 | 0.00 | 0.74 | 0.76 | 0.21 | 0.65 | 0.62 | 0.06 | 0.43 | 0.22 | 0.87 | 0.93 | 0.89 | 0.84 | 0.87 | 0.95 | 0.98 | 0.04 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 25 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.99 | -1.88 | -1.94 | -1.38 | -3.40 | -1.91 | -1.82 | -3.27 | -1.68 | -2.36 | -1.94 | -2.74 | -4.38 | -1.75 | -1.09 | -1.34 | -1.66 | -1.84 | -1.18 | -0.99 | -4.24 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.53 | -2.42 | -1.57 | -2.18 | -4.24 | -3.56 | -3.16 | -2.45 | -1.91 | -2.17 | -2.32 | -2.90 | -3.89 | -1.49 | -2.69 | -1.63 | -1.96 | -1.13 | -1.33 | -1.15 | -3.82 | -1.66|
| full sent prob |  |  | 0.18 | 0.64 | 0.82 | 0.65 | 0.01 | 0.68 | 0.84 | 0.53 | 0.47 | 0.15 | 0.03 | 0.13 | 0.00 | 0.73 | 0.69 | 0.90 | 0.79 | 0.92 | 0.95 | 0.97 | 0.12 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 27 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -3.83 | -2.34 | -1.98 | -2.80 | -3.52 | -2.12 | -1.56 | -2.64 | -1.96 | -2.16 | -1.16 | -1.70 | -2.63 | -2.23 | -2.36 | -1.16 | -2.03 | -1.48 | -1.20 | -1.04 | -3.83 | -1.68|
| full sent KL (full->waitk) |  |  | -3.52 | -2.39 | -1.54 | -2.01 | -4.24 | -3.54 | -3.20 | -2.62 | -1.87 | -2.02 | -2.34 | -2.92 | -3.83 | -1.39 | -2.57 | -1.63 | -1.93 | -1.17 | -1.33 | -1.14 | -3.84 | -1.66|
| dec-waitktgt |  |  | gemäß | angaben | der | behörden | , | eine | leiter | von | meter | unter@@ | ir@@ | der | eigent@@ | lichen | ein@@ | fahrt | des | tun@@ | n@@ | els | durch@@ | </s>|
| full sent tgt |  |  | nach | angaben | der | behörden | fährt | eine | leiter | 20 | meter | unter | ir@@ | des | unter@@ | lichen | ein@@ | fahrt | des | tun@@ | n@@ | els | ver@@ | </s>|
| ref | laut | behörden | führt | eine | leiter | 20 | meter | in | die | tiefe | zum | eigent@@ | lichen | tun@@ | n@@ | el@@ | eingang | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | tunnel | has | a | cross-@@ | section | measuring | 1.@@ | 20 | metres | high | and | 90 | cen@@ | ti@@ | metres | across | .|
| waitk tgt |  |  | der | tun@@ | nel | hat | einen | quer@@ | schnitt | von | 1,@@ | 20 | metern | hoch | und | 90 | z@@ | enti@@ | meter | über | . | </s>|
| waitk prob |  |  | 0.56 | 0.93 | 0.95 | 0.57 | 0.45 | 0.81 | 0.85 | 0.42 | 0.77 | 0.89 | 0.40 | 0.25 | 0.87 | 0.93 | 0.63 | 0.95 | 0.92 | 0.43 | 0.26 | 0.91|
| dec-waitk prob |  |  | 0.63 | 0.95 | 0.89 | 0.44 | 0.54 | 0.95 | 0.89 | 0.86 | 0.89 | 0.93 | 0.16 | 0.08 | 0.77 | 0.91 | 0.96 | 0.98 | 0.66 | 0.07 | 0.02 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.06 | -1.20 | -1.73 | -3.28 | -2.46 | -0.97 | -1.45 | -1.40 | -1.22 | -1.29 | -2.49 | -3.17 | -2.21 | -1.30 | -0.80 | -0.95 | -1.77 | -3.75 | -1.32 | -1.66|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.16 | -1.43 | -1.13 | -2.36 | -2.02 | -1.83 | -1.38 | -3.19 | -1.84 | -1.70 | -2.12 | -2.96 | -1.73 | -1.34 | -2.36 | -1.21 | -0.98 | -3.42 | -3.13 | -1.62|
| full sent prob |  |  | 0.42 | 0.93 | 0.93 | 0.39 | 0.63 | 0.91 | 0.93 | 0.71 | 0.82 | 0.94 | 0.29 | 0.11 | 0.84 | 0.62 | 0.80 | 0.98 | 0.56 | 0.15 | 0.02 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 0|
| full sent KL (waitk->full) |  |  | -3.65 | -1.33 | -1.31 | -2.82 | -1.99 | -1.31 | -1.17 | -1.94 | -1.48 | -1.28 | -2.02 | -2.64 | -1.96 | -2.77 | -1.72 | -0.99 | -1.67 | -3.67 | -1.83 | -1.70|
| full sent KL (full->waitk) |  |  | -3.07 | -1.41 | -1.17 | -2.35 | -2.05 | -1.80 | -1.41 | -3.15 | -1.80 | -1.70 | -2.16 | -2.98 | -1.78 | -1.12 | -2.28 | -1.21 | -0.91 | -3.44 | -3.13 | -1.61|
| dec-waitktgt |  |  | der | tun@@ | nel | hat | einen | quer@@ | schnitt | von | 1,@@ | 20 | m | höhe | und | 90 | z@@ | enti@@ | meter | qu@@ | dem | </s>|
| full sent tgt |  |  | der | tun@@ | nel | hat | einen | quer@@ | schnitt | von | 1,@@ | 20 | m | höhe | und | 90 | z@@ | enti@@ | meter | qu@@ | dem | </s>|
| ref | der | tun@@ | nel | hat | einen | quer@@ | schnitt | von | 1,@@ | 20 | meter | höhe | und | 90 | z@@ | enti@@ | meter | breite | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | it | would | thus | be | suitable | to | assist | illegal | immigration | into | the | usa | .|
| waitk tgt |  |  | es | wäre | daher | angebracht | , | illegale | einwanderung | in | die | usa | zu | unterstützen | . | </s>|
| waitk prob |  |  | 0.33 | 0.88 | 0.50 | 0.23 | 0.90 | 0.29 | 0.58 | 0.68 | 0.59 | 0.87 | 0.88 | 0.74 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.06 | 0.64 | 0.22 | 0.09 | 0.88 | 0.23 | 0.67 | 0.59 | 0.38 | 0.85 | 0.79 | 0.65 | 0.91 | 0.91|
| dec-waitk rank |  |  | 4 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.34 | -2.59 | -2.74 | -3.43 | -1.74 | -3.21 | -1.96 | -2.19 | -2.51 | -1.68 | -2.14 | -2.06 | -1.65 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.44 | -1.35 | -2.13 | -3.19 | -1.72 | -3.28 | -2.26 | -2.39 | -2.09 | -1.55 | -1.66 | -1.57 | -1.70 | -1.66|
| full sent prob |  |  | 0.30 | 0.85 | 0.35 | 0.21 | 0.90 | 0.05 | 0.63 | 0.83 | 0.91 | 0.87 | 0.91 | 0.69 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.97 | -1.65 | -2.33 | -3.14 | -1.69 | -2.15 | -1.83 | -1.76 | -1.35 | -1.57 | -1.54 | -1.74 | -1.67 | -1.67|
| full sent KL (full->waitk) |  |  | -3.51 | -1.51 | -2.18 | -3.20 | -1.73 | -3.32 | -2.24 | -2.53 | -2.29 | -1.57 | -1.75 | -1.60 | -1.70 | -1.66|
| dec-waitktgt |  |  | das | wäre | also | sinnvoll | , | illegale | einwanderung | in | die | usa | zu | unterstützen | . | </s>|
| full sent tgt |  |  | es | wäre | daher | angebracht | , | die | einwanderung | in | die | usa | zu | unterstützen | . | </s>|
| ref | er | wäre | damit | auch | geeignet | gewesen | , | um | die | illegale | einwanderung | richtung | usa | zu | fördern | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | two | of | the | susp@@ | ects | were | de@@ | tained | in | conjunction | with | the | co@@ | ca@@ | ine | find | .|
| waitk tgt |  |  | zwei | der | ver@@ | dä@@ | chtigen | wurden | in | verbindung | mit | der | ko@@ | ka@@ | in@@ | suche | in@@ | haf@@ | tiert | . | </s>|
| waitk prob |  |  | 0.54 | 0.56 | 0.72 | 0.95 | 0.88 | 0.73 | 0.44 | 0.62 | 0.92 | 0.36 | 0.24 | 0.94 | 0.50 | 0.34 | 0.43 | 0.97 | 0.91 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.32 | 0.27 | 0.71 | 0.95 | 0.83 | 0.68 | 0.25 | 0.83 | 0.91 | 0.29 | 0.82 | 0.93 | 0.39 | 0.04 | 0.09 | 0.92 | 0.94 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.30 | -2.29 | -2.53 | -1.23 | -1.46 | -1.63 | -2.73 | -1.48 | -1.64 | -2.41 | -1.47 | -1.22 | -2.13 | -5.27 | -1.75 | -1.46 | -1.34 | -1.67 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.11 | -2.65 | -2.42 | -1.16 | -1.48 | -2.18 | -3.19 | -2.76 | -1.51 | -2.40 | -4.58 | -1.13 | -2.06 | -3.26 | -1.73 | -1.02 | -1.59 | -1.73 | -1.69|
| full sent prob |  |  | 0.54 | 0.54 | 0.82 | 0.94 | 0.79 | 0.84 | 0.42 | 0.80 | 0.92 | 0.39 | 0.51 | 0.93 | 0.77 | 0.17 | 0.16 | 0.94 | 0.94 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.10 | -2.21 | -1.86 | -1.25 | -1.39 | -1.50 | -2.52 | -1.55 | -1.57 | -1.95 | -3.04 | -1.25 | -1.37 | -2.90 | -2.08 | -1.29 | -1.33 | -1.69 | -1.67|
| full sent KL (full->waitk) |  |  | -3.20 | -2.75 | -2.49 | -1.16 | -1.46 | -2.27 | -3.27 | -2.74 | -1.52 | -2.46 | -4.52 | -1.13 | -2.19 | -3.34 | -1.71 | -1.04 | -1.59 | -1.73 | -1.68|
| dec-waitktgt |  |  | zwei | ver@@ | ver@@ | dä@@ | chtigen | wurden | in | verbindung | mit | den | ko@@ | ka@@ | in@@ | fin@@ | fest@@ | haf@@ | tiert | . | </s>|
| full sent tgt |  |  | zwei | der | ver@@ | dä@@ | chtigen | wurden | in | verbindung | mit | dem | ko@@ | ka@@ | in@@ | fin@@ | fest@@ | haf@@ | tiert | . | </s>|
| ref | zwei | der | ver@@ | dä@@ | chtigen | wurden | in | zusammenhang | mit | dem | ko@@ | ka@@ | in-@@ | f@@ | und | fest@@ | genommen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | third | , | a | mex@@ | ic@@ | an | , | was | de@@ | tained | due | to | the | se@@ | iz@@ | ure | of | the | mari@@ | ju@@ | ana | .|
| waitk tgt |  |  | die | dritte | , | eine | mexi@@ | kanische | , | wurde | in | haft | genommen | , | weil | sie | die | macht | des | mari@@ | ju@@ | ana | er@@ | griff | . | </s>|
| waitk prob |  |  | 0.20 | 0.91 | 0.67 | 0.45 | 0.95 | 0.79 | 0.86 | 0.72 | 0.18 | 0.09 | 0.22 | 0.58 | 0.62 | 0.37 | 0.08 | 0.05 | 0.23 | 0.28 | 0.92 | 0.75 | 0.24 | 0.41 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.02 | 0.92 | 0.05 | 0.06 | 0.96 | 0.90 | 0.18 | 0.02 | 0.04 | 0.60 | 0.23 | 0.06 | 0.02 | 0.06 | 0.07 | 0.01 | 0.17 | 0.55 | 0.87 | 0.81 | 0.17 | 0.10 | 0.89 | 0.92|
| dec-waitk rank |  |  | 4 | 0 | 3 | 2 | 0 | 0 | 0 | 4 | 3 | 0 | 1 | 2 | 3 | 3 | 1 | 18 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.42 | -1.43 | -4.21 | -1.98 | -1.16 | -1.28 | -4.68 | -2.98 | -2.22 | -2.12 | -2.27 | -2.52 | -2.77 | -3.74 | -4.48 | -5.57 | -3.21 | -3.37 | -1.68 | -1.26 | -3.23 | -2.63 | -1.72 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.12 | -1.52 | -2.61 | -2.22 | -1.21 | -1.68 | -1.43 | -1.80 | -3.95 | -5.24 | -3.44 | -2.16 | -1.79 | -3.17 | -4.72 | -6.02 | -3.49 | -4.03 | -1.35 | -1.83 | -3.26 | -2.81 | -1.67 | -1.70|
| full sent prob |  |  | 0.26 | 0.84 | 0.80 | 0.05 | 0.97 | 0.84 | 0.84 | 0.86 | 0.01 | 0.67 | 0.11 | 0.57 | 0.62 | 0.05 | 0.35 | 0.00 | 0.08 | 0.18 | 0.87 | 0.92 | 0.31 | 0.32 | 0.91 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 5 | 0 | 2 | 0 | 0 | 1 | 0 | 45 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.20 | -1.96 | -2.16 | -2.10 | -1.07 | -1.24 | -2.04 | -1.54 | -1.75 | -1.56 | -2.69 | -2.41 | -2.43 | -2.10 | -3.59 | -2.01 | -2.01 | -1.86 | -1.78 | -1.14 | -3.38 | -2.27 | -1.61 | -1.68|
| full sent KL (full->waitk) |  |  | -3.12 | -1.46 | -3.02 | -2.31 | -1.22 | -1.65 | -1.90 | -2.30 | -3.96 | -5.25 | -3.42 | -2.42 | -2.11 | -3.22 | -4.74 | -6.02 | -3.56 | -4.05 | -1.36 | -1.88 | -3.29 | -2.88 | -1.68 | -1.69|
| dec-waitktgt |  |  | das | dritte | ist | die | mexi@@ | kanische | , | </s> | fest@@ | haft | gehalten | . | </s> | die | fest@@ | besch@@ | er@@ | mari@@ | ju@@ | ana | über@@ | lan@@ | . | </s>|
| full sent tgt |  |  | der | dritte | , | ein | mexi@@ | kanische | , | wurde | aufgrund | haft | gehalten | , | weil | die | die | mar@@ | der | mar@@ | ju@@ | ana | er@@ | griff | . | </s>|
| ref | der | dritte | , | ein | mexi@@ | kan@@ | er | , | wurde | wegen | des | besch@@ | lag@@ | nah@@ | m@@ | ten | mar@@ | ih@@ | u@@ | an@@ | as | gefasst | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | all | three | face | a | maximum | penalty | of | life | imprison@@ | ment | , | according | to | the | authorities | .|
| waitk tgt |  |  | alle | drei | haben | eine | maxi@@ | male | strafe | für | lebens@@ | lange | gefän@@ | g@@ | nis@@ | strafe | , | laut | den | behörden | . | </s>|
| waitk prob |  |  | 0.53 | 0.89 | 0.19 | 0.45 | 0.34 | 0.88 | 0.59 | 0.48 | 0.53 | 0.90 | 0.29 | 0.64 | 0.77 | 0.67 | 0.72 | 0.19 | 0.33 | 0.88 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.60 | 0.90 | 0.06 | 0.33 | 0.46 | 0.88 | 0.15 | 0.40 | 0.51 | 0.43 | 0.09 | 0.72 | 0.57 | 0.15 | 0.06 | 0.01 | 0.40 | 0.84 | 0.88 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 2 | 5 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.50 | -1.59 | -4.15 | -3.15 | -2.10 | -1.38 | -1.61 | -3.35 | -2.53 | -3.18 | -2.09 | -1.58 | -1.76 | -2.52 | -2.42 | -3.28 | -2.72 | -1.99 | -1.89 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.27 | -1.61 | -4.36 | -3.15 | -3.50 | -1.43 | -2.57 | -3.12 | -2.67 | -0.87 | -2.29 | -1.58 | -1.20 | -1.64 | -2.00 | -3.12 | -3.18 | -1.60 | -1.68 | -1.68|
| full sent prob |  |  | 0.25 | 0.91 | 0.04 | 0.09 | 0.20 | 0.90 | 0.36 | 0.44 | 0.63 | 0.61 | 0.13 | 0.72 | 0.69 | 0.28 | 0.52 | 0.08 | 0.56 | 0.88 | 0.88 | 0.91|
| full sent rank |  |  | 0 | 0 | 4 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.38 | -1.52 | -3.75 | -2.66 | -4.32 | -1.50 | -2.08 | -2.86 | -2.30 | -1.95 | -2.19 | -1.59 | -1.59 | -2.23 | -3.04 | -3.48 | -2.27 | -1.70 | -1.88 | -1.66|
| full sent KL (full->waitk) |  |  | -3.11 | -1.62 | -4.37 | -3.04 | -3.41 | -1.44 | -2.65 | -3.14 | -2.72 | -1.01 | -2.30 | -1.58 | -1.26 | -1.71 | -2.26 | -3.13 | -3.20 | -1.64 | -1.67 | -1.68|
| dec-waitktgt |  |  | alle | drei | müssen | eine | maxi@@ | male | lebens@@ | für | lebens@@ | lange | haft | g@@ | nis@@ | stra@@ | . | wie | den | behörden | . | </s>|
| full sent tgt |  |  | alle | drei | werden | laut | höchst@@ | male | strafe | für | lebens@@ | lange | haft | g@@ | nis@@ | stra@@ | , | wie | den | behörden | . | </s>|
| ref | allen | drei@@ | en | dro@@ | ht | als | höchst@@ | strafe | lebens@@ | langer | frei@@ | heits@@ | ent@@ | zug | , | wie | beam@@ | te | sagten | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | since | 2006 | , | eight | tun@@ | nels | of | this | type | have | been | discovered | , | the | press | conference | in | san | di@@ | e@@ | go | continued | .|
| waitk tgt |  |  | seit | 2006 | wurden | acht | tun@@ | nel | dieser | art | in | der | region | entdeckt | , | die | presse@@ | konferenz | in | san | die@@ | go | fort@@ | gesetzt | . | </s>|
| waitk prob |  |  | 0.69 | 0.93 | 0.22 | 0.79 | 0.66 | 0.84 | 0.76 | 0.90 | 0.14 | 0.15 | 0.04 | 0.34 | 0.82 | 0.46 | 0.69 | 0.96 | 0.85 | 0.93 | 0.98 | 0.96 | 0.11 | 0.84 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.77 | 0.96 | 0.00 | 0.86 | 0.84 | 0.46 | 0.73 | 0.91 | 0.06 | 0.00 | 0.00 | 0.58 | 0.59 | 0.36 | 0.73 | 0.97 | 0.88 | 0.97 | 0.96 | 0.97 | 0.00 | 0.82 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 69 | 0 | 0 | 1 | 0 | 0 | 4 | 99 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.37 | -1.13 | -2.18 | -1.41 | -1.82 | -1.59 | -1.99 | -1.49 | -4.06 | -3.87 | -4.31 | -3.15 | -2.56 | -3.34 | -2.51 | -1.05 | -1.66 | -1.05 | -1.15 | -1.09 | -1.09 | -1.26 | -1.64 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.59 | -1.37 | -3.48 | -1.88 | -3.10 | -1.22 | -2.00 | -1.54 | -4.62 | -4.84 | -5.52 | -4.34 | -1.78 | -3.34 | -2.52 | -1.22 | -1.89 | -1.43 | -0.98 | -1.20 | -4.08 | -1.39 | -1.67 | -1.67|
| full sent prob |  |  | 0.81 | 0.92 | 0.65 | 0.87 | 0.89 | 0.60 | 0.75 | 0.89 | 0.00 | 0.02 | 0.01 | 0.34 | 0.70 | 0.60 | 0.82 | 0.96 | 0.75 | 0.94 | 0.94 | 0.95 | 0.16 | 0.85 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 5 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.93 | -1.37 | -1.98 | -1.47 | -1.40 | -1.96 | -1.98 | -1.70 | -1.22 | -5.12 | -4.14 | -3.05 | -2.18 | -2.13 | -1.96 | -1.18 | -2.19 | -1.32 | -1.32 | -1.24 | -3.60 | -1.40 | -1.66 | -1.66|
| full sent KL (full->waitk) |  |  | -2.62 | -1.34 | -3.62 | -1.88 | -3.13 | -1.30 | -2.01 | -1.52 | -4.61 | -4.85 | -5.52 | -4.27 | -1.86 | -3.44 | -2.57 | -1.21 | -1.80 | -1.40 | -0.96 | -1.19 | -4.07 | -1.40 | -1.67 | -1.66|
| dec-waitktgt |  |  | seit | 2006 | acht | acht | tun@@ | n@@ | dieser | art | eingesetzt | betrieb | hand | entdeckt | , | die | presse@@ | konferenz | in | san | die@@ | go | . | gesetzt | . | </s>|
| full sent tgt |  |  | seit | 2006 | wurden | acht | tun@@ | nel | dieser | art | entdeckt | entdeckt | stadt | entdeckt | , | die | presse@@ | konferenz | in | san | die@@ | go | setzte | gesetzt | . | </s>|
| ref | seit | 2006 | seien | acht | derartige | tun@@ | nel | entdeckt | worden | , | hi@@ | e@@ | ß | es | auf | der | presse@@ | konferenz | in | san | die@@ | go | weiter | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | however | , | this | was | the | first | time | that | co@@ | ca@@ | ine | was | found | in | such | a | tunnel | construction | .|
| waitk tgt |  |  | dies | war | jedoch | der | erste | zeitpunkt | , | an | dem | co@@ | ca@@ | ine | in | einer | solchen | tun@@ | n@@ | el@@ | konstruktion | gefunden | wurde | . | </s>|
| waitk prob |  |  | 0.13 | 0.50 | 0.58 | 0.36 | 0.88 | 0.06 | 0.85 | 0.17 | 0.93 | 0.41 | 0.80 | 0.45 | 0.51 | 0.36 | 0.62 | 0.66 | 0.98 | 0.94 | 0.63 | 0.68 | 0.85 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.18 | 0.61 | 0.67 | 0.11 | 0.87 | 0.15 | 0.27 | 0.17 | 0.93 | 0.01 | 0.69 | 0.11 | 0.14 | 0.29 | 0.79 | 0.87 | 0.96 | 0.93 | 0.66 | 0.21 | 0.86 | 0.91 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.84 | -2.42 | -1.82 | -2.34 | -1.84 | -4.34 | -2.64 | -2.96 | -1.43 | -0.61 | -1.37 | -1.24 | -3.72 | -2.25 | -1.68 | -1.49 | -1.15 | -1.29 | -1.93 | -3.63 | -1.59 | -1.64 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.72 | -2.94 | -2.49 | -2.47 | -1.68 | -5.61 | -1.55 | -3.26 | -1.41 | -2.58 | -1.79 | -2.37 | -2.98 | -2.39 | -2.66 | -2.78 | -0.96 | -1.20 | -2.36 | -2.17 | -1.70 | -1.64 | -1.70|
| full sent prob |  |  | 0.06 | 0.74 | 0.57 | 0.01 | 0.84 | 0.02 | 0.71 | 0.21 | 0.93 | 0.01 | 0.76 | 0.14 | 0.73 | 0.08 | 0.77 | 0.81 | 0.97 | 0.94 | 0.61 | 0.39 | 0.86 | 0.91 | 0.91|
| full sent rank |  |  | 3 | 0 | 0 | 3 | 0 | 5 | 0 | 0 | 0 | 10 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.30 | -2.13 | -2.16 | -1.78 | -2.04 | -4.68 | -2.30 | -3.23 | -1.44 | -2.56 | -1.53 | -1.75 | -2.11 | -1.84 | -1.66 | -1.99 | -1.07 | -1.25 | -2.18 | -3.33 | -1.59 | -1.68 | -1.67|
| full sent KL (full->waitk) |  |  | -3.69 | -2.99 | -2.44 | -2.48 | -1.66 | -5.60 | -1.86 | -3.25 | -1.41 | -2.44 | -1.83 | -2.35 | -3.23 | -2.39 | -2.65 | -2.75 | -0.96 | -1.21 | -2.33 | -2.27 | -1.70 | -1.63 | -1.70|
| dec-waitktgt |  |  | aber | war | jedoch | die | erste | fall | , | als | dem | ko@@ | ca@@ | in | enthalten | einem | solchen | tun@@ | n@@ | el@@ | konstruktion | gefunden | wurde | . | </s>|
| full sent tgt |  |  | es | war | jedoch | das | erste | fall | , | an | dem | ko@@ | ca@@ | in | in | einem | solchen | tun@@ | n@@ | el@@ | konstruktion | gefunden | wurde | . | </s>|
| ref | es | sei | aber | das | erste | mal | , | dass | in | einem | solchen | tun@@ | n@@ | el@@ | bau | ko@@ | ka@@ | in | gefunden | wurde | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | normally | co@@ | ca@@ | ine | is | s@@ | mu@@ | gg@@ | led | in | smaller | quantities | and | not | through | tun@@ | nels | .|
| waitk tgt |  |  | normalerweise | ko@@ | ka@@ | in | wird | in | der | eu | in | klein@@ | eren | mengen | und | nicht | durch | tun@@ | nel | gesch@@ | mu@@ | g@@ | gelt | . | </s>|
| waitk prob |  |  | 0.31 | 0.11 | 0.81 | 0.83 | 0.66 | 0.16 | 0.11 | 0.20 | 0.62 | 0.33 | 0.83 | 0.95 | 0.34 | 0.92 | 0.34 | 0.81 | 0.74 | 0.40 | 0.99 | 0.98 | 0.88 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.85 | 0.58 | 0.98 | 0.88 | 0.00 | 0.00 | 0.21 | 0.02 | 0.00 | 0.31 | 0.93 | 0.95 | 0.10 | 0.85 | 0.76 | 0.77 | 0.72 | 0.49 | 0.99 | 0.98 | 0.94 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 6 | 17 | 0 | 4 | 36 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.01 | -2.63 | -0.84 | -1.47 | -2.28 | -3.53 | -3.65 | -4.42 | -2.63 | -2.23 | -1.20 | -1.13 | -2.63 | -2.06 | -1.55 | -2.49 | -1.66 | -2.96 | -0.92 | -1.05 | -1.14 | -1.71 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.24 | -4.62 | -2.08 | -1.72 | -2.26 | -4.17 | -4.80 | -4.17 | -2.57 | -2.89 | -1.89 | -1.15 | -2.97 | -1.47 | -2.65 | -2.05 | -1.49 | -3.32 | -0.89 | -1.03 | -1.54 | -1.60 | -1.70|
| full sent prob |  |  | 0.61 | 0.00 | 0.96 | 0.84 | 0.76 | 0.85 | 0.00 | 0.00 | 0.77 | 0.35 | 0.93 | 0.92 | 0.21 | 0.91 | 0.60 | 0.81 | 0.70 | 0.81 | 0.99 | 0.98 | 0.94 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 120 | 0 | 0 | 0 | 0 | 25 | 60 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.29 | -1.87 | -0.98 | -1.80 | -2.06 | -1.36 | -2.13 | -3.24 | -2.16 | -2.33 | -1.22 | -1.25 | -1.66 | -1.63 | -2.05 | -2.18 | -1.75 | -1.43 | -0.92 | -1.05 | -1.15 | -1.69 | -1.67|
| full sent KL (full->waitk) |  |  | -4.18 | -4.63 | -2.07 | -1.70 | -2.67 | -4.27 | -4.77 | -4.17 | -2.96 | -2.90 | -1.89 | -1.12 | -3.02 | -1.51 | -2.63 | -2.08 | -1.48 | -3.42 | -0.89 | -1.03 | -1.54 | -1.60 | -1.69|
| dec-waitktgt |  |  | normalerweise | ko@@ | ka@@ | in | </s> | gesch@@ | der | regel | gesch@@ | gerin@@ | eren | mengen | gesch@@ | nicht | durch | tun@@ | nel | gesch@@ | mu@@ | g@@ | gelt | . | </s>|
| full sent tgt |  |  | normalerweise | wird | ka@@ | in | wird | in | klein@@ | regel | in | klein@@ | eren | mengen | gesch@@ | nicht | durch | tun@@ | nel | gesch@@ | mu@@ | g@@ | gelt | . | </s>|
| ref | normalerweise | wird | ko@@ | ka@@ | in | in | klein@@ | eren | mengen | und | nicht | durch | tun@@ | nel | gesch@@ | mu@@ | g@@ | gelt | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | they | will | do | anything | to | make | it | to | the | usa | .|
| waitk tgt |  |  | sie | werden | alles | tun | , | um | es | den | usa | zu | ermöglichen | . | </s>|
| waitk prob |  |  | 0.55 | 0.80 | 0.44 | 0.37 | 0.90 | 0.67 | 0.34 | 0.52 | 0.86 | 0.64 | 0.54 | 0.90 | 0.90|
| dec-waitk prob |  |  | 0.36 | 0.78 | 0.40 | 0.66 | 0.83 | 0.60 | 0.28 | 0.60 | 0.86 | 0.80 | 0.34 | 0.91 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.02 | -1.94 | -3.23 | -1.96 | -1.92 | -2.23 | -3.43 | -2.54 | -1.57 | -2.05 | -3.31 | -1.64 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.81 | -1.95 | -3.16 | -2.74 | -1.63 | -1.95 | -3.01 | -2.70 | -1.57 | -2.98 | -2.54 | -1.70 | -1.69|
| full sent prob |  |  | 0.65 | 0.81 | 0.62 | 0.51 | 0.90 | 0.74 | 0.40 | 0.48 | 0.86 | 0.77 | 0.31 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.68 | -2.03 | -2.50 | -2.23 | -1.70 | -1.99 | -2.75 | -2.68 | -1.58 | -2.23 | -3.24 | -1.66 | -1.66|
| full sent KL (full->waitk) |  |  | -2.94 | -1.97 | -3.24 | -2.70 | -1.67 | -2.01 | -3.05 | -2.66 | -1.57 | -2.96 | -2.53 | -1.70 | -1.69|
| dec-waitktgt |  |  | sie | werden | alles | tun | , | um | es | den | usa | zu | ermöglichen | . | </s>|
| full sent tgt |  |  | sie | werden | alles | tun | , | um | es | den | usa | zu | ermöglichen | . | </s>|
| ref | sie | würden | alles | tun | , | um | in | die | usa | zu | gelangen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | no | specific | details | were | given | regarding | those | de@@ | tained | , | but | it | is | reported | that | at | least | one | is | mex@@ | ic@@ | an|
| waitk tgt |  |  | es | wurden | keine | konkreten | angaben | zu | den | in@@ | haf@@ | tierten | gemacht | , | aber | es | wird | berichtet | , | dass | mindestens | eine | mexi@@ | kanische | in@@ | haf@@ | tierung | in | mexi@@ | kanischen | gefän@@ | gnissen | ist | . | </s>|
| waitk prob |  |  | 0.26 | 0.72 | 0.82 | 0.44 | 0.41 | 0.71 | 0.70 | 0.41 | 0.99 | 0.97 | 0.45 | 0.90 | 0.50 | 0.53 | 0.52 | 0.75 | 0.92 | 0.72 | 0.43 | 0.30 | 0.92 | 0.83 | 0.27 | 0.98 | 0.48 | 0.10 | 0.23 | 0.32 | 0.46 | 0.96 | 0.23 | 0.67 | 0.91|
| dec-waitk prob |  |  | 0.03 | 0.21 | 0.93 | 0.10 | 0.64 | 0.43 | 0.46 | 0.82 | 0.98 | 0.96 | 0.73 | 0.78 | 0.24 | 0.72 | 0.51 | 0.80 | 0.91 | 0.80 | 0.45 | 0.07 | 0.85 | 0.33 | 0.03 | 0.85 | 0.08 | 0.01 | 0.12 | 0.05 | 0.02 | 0.91 | 0.38 | 0.85 | 0.91|
| dec-waitk rank |  |  | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 5 | 0 | 2 | 17 | 1 | 3 | 4 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.99 | -2.56 | -1.17 | -2.85 | -1.80 | -2.79 | -2.92 | -1.28 | -0.97 | -1.13 | -2.10 | -1.96 | -3.45 | -2.15 | -2.76 | -1.88 | -1.64 | -1.72 | -2.22 | -2.48 | -1.75 | -1.90 | -5.03 | -1.59 | -3.30 | -4.52 | -1.89 | -4.77 | -5.35 | -1.40 | -4.13 | -1.81 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.15 | -1.59 | -1.75 | -2.52 | -2.74 | -1.75 | -2.18 | -2.83 | -0.92 | -1.09 | -3.29 | -1.58 | -3.10 | -3.03 | -2.52 | -2.20 | -1.54 | -2.15 | -2.71 | -2.22 | -1.21 | -1.20 | -4.16 | -0.91 | -2.53 | -4.20 | -3.70 | -2.66 | -3.32 | -1.02 | -4.05 | -2.06 | -1.67|
| full sent prob |  |  | 0.34 | 0.84 | 0.83 | 0.13 | 0.45 | 0.58 | 0.64 | 0.69 | 0.94 | 0.91 | 0.69 | 0.88 | 0.58 | 0.70 | 0.48 | 0.78 | 0.91 | 0.84 | 0.67 | 0.07 | 0.74 | 0.41 | 0.06 | 0.87 | 0.09 | 0.01 | 0.11 | 0.07 | 0.02 | 0.91 | 0.28 | 0.82 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 3 | 0 | 2 | 21 | 1 | 1 | 4 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.53 | -1.41 | -1.68 | -2.81 | -2.05 | -2.26 | -2.67 | -1.81 | -1.25 | -1.56 | -2.22 | -1.74 | -2.28 | -2.24 | -2.84 | -1.99 | -1.63 | -1.67 | -1.62 | -2.25 | -2.28 | -1.87 | -4.74 | -1.45 | -3.67 | -4.53 | -3.81 | -4.27 | -5.14 | -1.43 | -4.50 | -1.91 | -1.63|
| full sent KL (full->waitk) |  |  | -4.18 | -1.96 | -1.68 | -2.53 | -2.71 | -1.83 | -2.29 | -2.79 | -0.88 | -1.04 | -3.28 | -1.66 | -3.25 | -3.02 | -2.51 | -2.19 | -1.54 | -2.17 | -2.77 | -2.22 | -1.12 | -1.25 | -4.16 | -0.93 | -2.54 | -4.19 | -3.66 | -2.69 | -3.32 | -1.02 | -4.03 | -2.05 | -1.67|
| dec-waitktgt |  |  | keine | gab | keine | genau@@ | angaben | zu | den | in@@ | haf@@ | tierten | gemacht | , | es | es | wird | berichtet | , | dass | mindestens | ein | mexi@@ | kan@@ | staats@@ | haf@@ | tiert | ist | mexiko | kan@@ | einrichtungen | gnissen | ist | . | </s>|
| full sent tgt |  |  | es | wurden | keine | genau@@ | angaben | zu | den | in@@ | haf@@ | tierten | gemacht | , | aber | es | wird | berichtet | , | dass | mindestens | ein | mexi@@ | kan@@ | staats@@ | haf@@ | tierte | hat | mexiko | kan@@ | einrichtungen | gnissen | ist | . | </s>|
| ref | zu | den | fest@@ | genommenen | wurden | keine | einzelheiten | bekannt | gegeben | , | zumindest | einer | sei | mexi@@ | kan@@ | er | , | hi@@ | e@@ | ß | es | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | they | can | expect | prison | terms | of | up | to | ten | years | .|
| waitk tgt |  |  | sie | können | mit | gefän@@ | g@@ | nis@@ | stra@@ | fen | bis | zu | zehn | jahren | rechnen | . | </s>|
| waitk prob |  |  | 0.55 | 0.69 | 0.17 | 0.34 | 0.86 | 0.95 | 0.83 | 0.93 | 0.44 | 0.83 | 0.81 | 0.80 | 0.95 | 0.88 | 0.91|
| dec-waitk prob |  |  | 0.34 | 0.36 | 0.08 | 0.38 | 0.96 | 0.96 | 0.91 | 0.97 | 0.44 | 0.86 | 0.62 | 0.80 | 0.97 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.04 | -3.08 | -4.30 | -1.92 | -0.97 | -0.93 | -1.30 | -1.06 | -2.11 | -1.67 | -1.81 | -1.95 | -0.97 | -1.74 | -1.67|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.01 | -2.09 | -3.65 | -3.31 | -1.44 | -1.03 | -1.62 | -1.29 | -1.98 | -1.95 | -1.59 | -1.77 | -1.08 | -1.82 | -1.66|
| full sent prob |  |  | 0.66 | 0.69 | 0.32 | 0.32 | 0.88 | 0.94 | 0.82 | 0.95 | 0.54 | 0.88 | 0.65 | 0.86 | 0.94 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.56 | -2.45 | -2.90 | -1.09 | -1.34 | -1.00 | -1.65 | -1.24 | -2.00 | -1.64 | -1.80 | -1.76 | -1.21 | -1.70 | -1.70|
| full sent KL (full->waitk) |  |  | -3.15 | -2.27 | -3.68 | -3.31 | -1.39 | -1.01 | -1.55 | -1.28 | -1.98 | -1.96 | -1.61 | -1.80 | -1.05 | -1.82 | -1.66|
| dec-waitktgt |  |  | sie | können | sich | haft@@ | g@@ | nis@@ | stra@@ | fen | bis | zu | zehn | jahren | rechnen | . | </s>|
| full sent tgt |  |  | sie | können | mit | haft@@ | g@@ | nis@@ | stra@@ | fen | bis | zu | zehn | jahren | rechnen | . | </s>|
| ref | sie | müssen | mit | haft@@ | stra@@ | fen | bis | zu | zehn | jahren | rechnen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | anniversary | of | the | first | docum@@ | ented | mention | of | the | town | , | are | drawing | closer | .|
| waitk tgt |  |  | jahre@@ | stag | der | ersten | doku@@ | men@@ | tierten | erwähn@@ | ung | der | stadt | , | näher@@ | n | sich | . | </s>|
| waitk prob |  |  | 0.28 | 0.96 | 0.63 | 0.90 | 0.40 | 0.92 | 0.91 | 0.96 | 0.94 | 0.80 | 0.92 | 0.70 | 0.81 | 0.49 | 0.82 | 0.78 | 0.91|
| dec-waitk prob |  |  | 0.94 | 0.96 | 0.43 | 0.70 | 0.38 | 0.90 | 0.86 | 0.78 | 0.92 | 0.79 | 0.87 | 0.23 | 0.71 | 0.44 | 0.83 | 0.87 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -0.65 | -1.20 | -1.85 | -2.89 | -2.65 | -1.66 | -1.87 | -2.27 | -1.52 | -2.09 | -1.82 | -3.90 | -1.98 | -2.21 | -2.11 | -1.81 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.89 | -1.08 | -1.68 | -1.45 | -2.81 | -1.51 | -1.40 | -0.92 | -1.34 | -2.05 | -1.43 | -2.36 | -1.68 | -2.41 | -2.00 | -2.22 | -1.64|
| full sent prob |  |  | 0.29 | 0.93 | 0.72 | 0.82 | 0.78 | 0.93 | 0.82 | 0.70 | 0.92 | 0.84 | 0.94 | 0.73 | 0.55 | 0.67 | 0.85 | 0.82 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.50 | -1.28 | -1.85 | -1.77 | -1.60 | -1.45 | -2.07 | -2.66 | -1.51 | -1.85 | -1.34 | -2.36 | -2.68 | -1.87 | -2.02 | -2.04 | -1.67|
| full sent KL (full->waitk) |  |  | -3.76 | -1.06 | -1.76 | -1.54 | -2.92 | -1.53 | -1.37 | -0.85 | -1.34 | -2.08 | -1.48 | -2.66 | -1.57 | -2.48 | -2.01 | -2.19 | -1.64|
| dec-waitktgt |  |  | jahre@@ | stag | des | ersten | doku@@ | men@@ | tierten | erwähn@@ | ung | der | stadt | . | näher@@ | n | sich | . | </s>|
| full sent tgt |  |  | jahre@@ | stag | der | ersten | doku@@ | men@@ | tierten | erwähn@@ | ung | der | stadt | , | näher@@ | n | sich | . | </s>|
| ref | wieder@@ | kehr | der | ersten | ur@@ | kund@@ | lichen | erwähn@@ | ung | rück@@ | t | immer | näher | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | when | the | year | comes | to | an | end | in | just | eight | weeks | , | the | anniversary | year | will | be | upon | us | .|
| waitk tgt |  |  | als | das | jahr | zu | ende | geht | , | ist | es | nur | acht | wochen | her | , | dass | das | ju@@ | bi@@ | lä@@ | ums@@ | jahr | vor | uns | liegt | . | </s>|
| waitk prob |  |  | 0.39 | 0.42 | 0.84 | 0.32 | 0.93 | 0.60 | 0.79 | 0.10 | 0.27 | 0.14 | 0.64 | 0.87 | 0.55 | 0.88 | 0.63 | 0.58 | 0.53 | 0.96 | 0.94 | 0.49 | 0.94 | 0.10 | 0.90 | 0.53 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.04 | 0.65 | 0.84 | 0.01 | 0.99 | 0.28 | 0.01 | 0.00 | 0.04 | 0.00 | 0.14 | 0.89 | 0.00 | 0.13 | 0.03 | 0.51 | 0.09 | 0.96 | 0.92 | 0.56 | 0.93 | 0.01 | 0.77 | 0.40 | 0.89 | 0.92|
| dec-waitk rank |  |  | 3 | 0 | 0 | 5 | 0 | 1 | 2 | 16 | 2 | 18 | 1 | 0 | 14 | 2 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.96 | -2.64 | -2.03 | -3.04 | -0.87 | -3.51 | -1.24 | -0.98 | -1.94 | -2.84 | -3.22 | -1.61 | -1.11 | -2.84 | -3.24 | -3.01 | -2.26 | -1.13 | -1.46 | -1.74 | -1.44 | -4.27 | -2.40 | -2.63 | -1.75 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.26 | -3.62 | -2.10 | -4.11 | -1.21 | -2.34 | -1.51 | -4.53 | -3.56 | -4.45 | -2.15 | -1.87 | -1.34 | -1.22 | -1.83 | -2.78 | -1.52 | -1.12 | -1.26 | -2.29 | -1.30 | -4.29 | -1.49 | -2.23 | -1.66 | -1.68|
| full sent prob |  |  | 0.00 | 0.68 | 0.88 | 0.00 | 0.81 | 0.44 | 0.83 | 0.09 | 0.11 | 0.16 | 0.25 | 0.91 | 0.15 | 0.74 | 0.51 | 0.24 | 0.30 | 0.93 | 0.94 | 0.66 | 0.92 | 0.02 | 0.86 | 0.41 | 0.90 | 0.91|
| full sent rank |  |  | 20 | 0 | 0 | 13 | 0 | 0 | 0 | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.68 | -2.17 | -1.71 | -1.59 | -1.83 | -3.67 | -1.95 | -3.80 | -3.14 | -3.42 | -2.21 | -1.51 | -2.50 | -2.22 | -2.72 | -2.24 | -2.76 | -1.37 | -1.37 | -1.58 | -1.58 | -4.29 | -1.93 | -2.43 | -1.72 | -1.66|
| full sent KL (full->waitk) |  |  | -3.30 | -3.63 | -2.13 | -4.11 | -1.07 | -2.40 | -2.05 | -4.56 | -3.60 | -4.48 | -2.25 | -1.89 | -1.57 | -1.66 | -2.08 | -2.67 | -1.59 | -1.09 | -1.27 | -2.32 | -1.29 | -4.29 | -1.56 | -2.25 | -1.67 | -1.67|
| dec-waitktgt |  |  | wann | das | jahr | kommt | ende | kommt | </s> | </s> | </s> | </s> | </s> | wochen | </s> | . | </s> | das | jahr | bi@@ | lä@@ | ums@@ | jahr | an@@ | uns | liegt | . | </s>|
| full sent tgt |  |  | wenn | das | jahr | in | ende | geht | , | wird | das | in | noch | wochen | , | , | dass | wir | ju@@ | bi@@ | lä@@ | ums@@ | jahr | auf | uns | liegt | . | </s>|
| ref | wenn | in | gut | acht | wochen | das | jahr | zu | ende | geht | , | steht | das | ju@@ | bi@@ | lä@@ | ums@@ | jahr | an | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | were | first | docum@@ | ented | together | in | the | year | 7@@ | 94 | .|
| waitk tgt |  |  | gei@@ | sin@@ | gen | und | kir@@ | chen@@ | -@@ | haus@@ | en | wurden | erstmals | gemeinsam | in | der | zeit | 7@@ | 9@@ | 4 | zusammen | doku@@ | men@@ | tiert | . | </s>|
| waitk prob |  |  | 0.48 | 0.60 | 0.96 | 0.87 | 0.92 | 0.92 | 0.88 | 0.91 | 0.95 | 0.59 | 0.44 | 0.43 | 0.46 | 0.52 | 0.07 | 0.41 | 0.89 | 0.92 | 0.25 | 0.65 | 0.94 | 0.89 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.61 | 0.53 | 0.96 | 0.87 | 0.92 | 0.93 | 0.15 | 0.97 | 0.94 | 0.02 | 0.51 | 0.84 | 0.00 | 0.22 | 0.00 | 0.62 | 0.96 | 0.95 | 0.00 | 0.83 | 0.95 | 0.93 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 0 | 0 | 9 | 1 | 37 | 0 | 0 | 0 | 344 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -3.13 | -2.90 | -1.11 | -1.82 | -1.43 | -1.22 | -1.06 | -0.97 | -1.39 | -3.39 | -2.97 | -1.39 | -1.32 | -2.58 | -2.14 | -2.91 | -1.10 | -1.18 | -1.55 | -1.67 | -1.28 | -1.37 | -1.63 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.67 | -2.78 | -1.13 | -1.84 | -1.44 | -1.12 | -0.94 | -1.49 | -1.24 | -2.17 | -3.03 | -2.65 | -2.31 | -2.48 | -5.37 | -3.62 | -1.74 | -1.34 | -3.22 | -2.82 | -1.33 | -1.78 | -1.66 | -1.66|
| full sent prob |  |  | 0.17 | 0.88 | 0.98 | 0.89 | 0.94 | 0.93 | 0.19 | 0.96 | 0.94 | 0.72 | 0.55 | 0.09 | 0.02 | 0.12 | 0.19 | 0.16 | 0.94 | 0.95 | 0.00 | 0.86 | 0.95 | 0.93 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 2 | 0 | 0 | 199 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.69 | -1.22 | -1.03 | -1.76 | -1.30 | -1.19 | -1.45 | -1.07 | -1.32 | -2.15 | -2.51 | -3.38 | -1.68 | -3.44 | -3.90 | -3.18 | -1.31 | -1.18 | -1.62 | -1.49 | -1.31 | -1.36 | -1.64 | -1.63|
| full sent KL (full->waitk) |  |  | -3.50 | -2.96 | -1.14 | -1.85 | -1.45 | -1.12 | -0.97 | -1.48 | -1.24 | -2.51 | -3.04 | -2.40 | -2.53 | -2.34 | -5.37 | -3.48 | -1.72 | -1.34 | -3.22 | -2.84 | -1.33 | -1.78 | -1.66 | -1.66|
| dec-waitktgt |  |  | gei@@ | sin@@ | gen | und | kir@@ | chen@@ | haus@@ | haus@@ | en | </s> | erstmals | gemeinsam | doku@@ | den | jahres@@ | 7@@ | 9@@ | 4 | doku@@ | doku@@ | men@@ | tiert | . | </s>|
| full sent tgt |  |  | gei@@ | sin@@ | gen | und | kir@@ | chen@@ | haus@@ | haus@@ | en | wurden | erstmals | im | im | 7@@ | zeit | von | 9@@ | 4 | doku@@ | doku@@ | men@@ | tiert | . | </s>|
| ref | gei@@ | sin@@ | gen | und | kir@@ | chen@@ | -@@ | haus@@ | en | wurden | 7@@ | 9@@ | 4 | erstmals | ur@@ | kund@@ | lich | zusammen | erwähnt | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | a | de@@ | ed | was | drafted | in | kir@@ | chen | , | in | which | both | towns | are | mentioned | .|
| waitk tgt |  |  | ein | de@@ | al | wurde | in | kir@@ | chen | ent@@ | worfen | , | in | dem | beide | städte | erwähnt | werden | . | </s>|
| waitk prob |  |  | 0.22 | 0.30 | 0.16 | 0.72 | 0.63 | 0.33 | 0.68 | 0.22 | 0.92 | 0.87 | 0.55 | 0.58 | 0.66 | 0.80 | 0.66 | 0.68 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.04 | 0.01 | 0.01 | 0.45 | 0.68 | 0.54 | 0.75 | 0.33 | 0.93 | 0.27 | 0.62 | 0.27 | 0.61 | 0.91 | 0.79 | 0.46 | 0.90 | 0.91|
| dec-waitk rank |  |  | 3 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.55 | -4.49 | -1.30 | -2.69 | -2.30 | -2.43 | -2.00 | -3.24 | -1.26 | -3.23 | -2.57 | -2.63 | -2.50 | -1.30 | -1.71 | -2.33 | -1.68 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.95 | -4.28 | -4.60 | -2.21 | -2.73 | -4.01 | -2.70 | -3.33 | -1.39 | -1.34 | -2.46 | -2.52 | -2.51 | -1.97 | -2.00 | -2.07 | -1.66 | -1.70|
| full sent prob |  |  | 0.03 | 0.36 | 0.06 | 0.70 | 0.88 | 0.47 | 0.78 | 0.32 | 0.87 | 0.85 | 0.73 | 0.87 | 0.75 | 0.91 | 0.80 | 0.53 | 0.90 | 0.91|
| full sent rank |  |  | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.59 | -4.10 | -4.17 | -2.21 | -1.62 | -2.11 | -2.11 | -3.39 | -1.54 | -1.92 | -2.15 | -1.48 | -2.00 | -1.28 | -1.61 | -2.42 | -1.68 | -1.68|
| full sent KL (full->waitk) |  |  | -3.89 | -4.36 | -4.59 | -2.36 | -2.84 | -4.01 | -2.71 | -3.33 | -1.35 | -1.76 | -2.51 | -2.81 | -2.59 | -1.98 | -2.01 | -2.11 | -1.66 | -1.69|
| dec-waitktgt |  |  | eine | akt | kre@@ | wurde | in | kir@@ | chen | ent@@ | worfen | . | in | beiden | beide | städte | erwähnt | werden | . | </s>|
| full sent tgt |  |  | in | de@@ | ed | wurde | in | kir@@ | chen | ent@@ | worfen | , | in | dem | beide | städte | erwähnt | werden | . | </s>|
| ref | in | kirchen | wurde | eine | ur@@ | kunde | ge@@ | fertigt | , | in | der | beide | orte | erwähnt | sind | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | as | part | of | the | anniversary | celebra@@ | tions | , | a | number | of | events | are | planned | both | in | ge@@ | is@@ | ingen | and | kir@@ | ch@@ | en-@@ | haus@@ | en | .|
| waitk tgt |  |  | im | rahmen | des | ju@@ | bi@@ | lä@@ | ums | werden | einige | veranstaltungen | in | der | ganzen | welt | geplant | . | </s>|
| waitk prob |  |  | 0.39 | 0.83 | 0.69 | 0.82 | 0.96 | 1.00 | 0.83 | 0.18 | 0.16 | 0.50 | 0.10 | 0.13 | 0.04 | 0.52 | 0.21 | 0.42 | 0.91|
| dec-waitk prob |  |  | 0.02 | 0.74 | 0.83 | 0.41 | 0.86 | 0.98 | 0.75 | 0.00 | 0.23 | 0.55 | 0.00 | 0.07 | 0.01 | 0.36 | 0.34 | 0.80 | 0.93|
| dec-waitk rank |  |  | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 27 | 0 | 0 | 27 | 2 | 20 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.32 | -2.60 | -1.82 | -2.04 | -1.65 | -1.03 | -1.51 | -1.42 | -4.00 | -3.12 | -2.09 | -4.12 | -5.46 | -3.78 | -3.02 | -2.00 | -1.48|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.17 | -1.74 | -2.30 | -1.19 | -1.02 | -0.87 | -1.30 | -4.12 | -3.84 | -2.29 | -4.58 | -5.02 | -5.78 | -3.00 | -3.58 | -2.41 | -1.69|
| full sent prob |  |  | 0.40 | 0.95 | 0.23 | 0.97 | 0.92 | 0.99 | 0.34 | 0.11 | 0.03 | 0.59 | 0.28 | 0.00 | 0.00 | 0.49 | 0.36 | 0.37 | 0.90|
| full sent rank |  |  | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 5 | 0 | 1 | 107 | 144 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.72 | -1.09 | -1.94 | -0.92 | -1.38 | -0.92 | -1.77 | -2.94 | -3.32 | -2.76 | -2.20 | -0.52 | -3.56 | -2.46 | -3.11 | -2.32 | -1.69|
| full sent KL (full->waitk) |  |  | -3.20 | -1.88 | -2.02 | -1.53 | -1.06 | -0.87 | -1.04 | -4.14 | -3.82 | -2.29 | -4.58 | -5.01 | -5.79 | -3.07 | -3.59 | -2.33 | -1.67|
| dec-waitktgt |  |  | als | rahmen | des | jahre@@ | bi@@ | lä@@ | ums | </s> | einige | veranstaltungen | durchgeführt | angriff | regel | welt | geplant | . | </s>|
| full sent tgt |  |  | im | rahmen | der | ju@@ | bi@@ | lä@@ | ums@@ | sind | in | veranstaltungen | sowohl | gei@@ | stadt | welt | geplant | . | </s>|
| ref | im | rahmen | des | ju@@ | bi@@ | lä@@ | ums | sind | et@@ | liche | veranstaltungen | sowohl | in | gei@@ | sin@@ | gen | , | als | auch | in | kir@@ | chen@@ | -@@ | haus@@ | en | geplant | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | on | the | friday | there | will | be | a | cere@@ | mony | , | and | on | the | saturday | and | sunday | a | party | will | be | held | at | the | kir@@ | ch@@ | tal@@ | hal@@ | le | .|
| waitk tgt |  |  | am | freitag | wird | es | eine | zer@@ | e@@ | moni@@ | e | geben | , | und | am | samstag | und | sonntag | wird | eine | part@@ | y | an | der | kir@@ | cht@@ | al@@ | halle | stattfinden | . | </s>|
| waitk prob |  |  | 0.66 | 0.94 | 0.22 | 0.51 | 0.27 | 0.78 | 0.97 | 0.97 | 0.94 | 0.82 | 0.71 | 0.86 | 0.93 | 0.93 | 0.89 | 0.91 | 0.48 | 0.65 | 0.69 | 0.95 | 0.19 | 0.74 | 0.87 | 0.50 | 0.96 | 0.93 | 0.50 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.59 | 0.91 | 0.29 | 0.81 | 0.14 | 0.10 | 0.98 | 0.99 | 0.95 | 0.91 | 0.65 | 0.67 | 0.69 | 0.89 | 0.86 | 0.90 | 0.58 | 0.37 | 0.50 | 0.03 | 0.01 | 0.80 | 0.93 | 0.51 | 0.02 | 0.96 | 0.67 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 1 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 18 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.78 | -1.24 | -2.73 | -1.94 | -2.89 | -4.51 | -0.96 | -0.89 | -1.27 | -1.41 | -2.23 | -2.27 | -2.44 | -1.41 | -1.81 | -1.42 | -2.73 | -2.72 | -2.89 | -5.63 | -4.18 | -2.06 | -1.24 | -1.60 | -0.94 | -1.14 | -1.85 | -1.74 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.67 | -1.25 | -3.35 | -3.06 | -3.33 | -1.42 | -1.14 | -1.10 | -1.31 | -1.78 | -1.84 | -1.79 | -1.12 | -1.25 | -1.68 | -1.36 | -2.87 | -2.51 | -2.21 | -0.56 | -3.01 | -2.06 | -1.71 | -1.73 | -0.30 | -1.24 | -2.37 | -1.70 | -1.66|
| full sent prob |  |  | 0.58 | 0.80 | 0.26 | 0.25 | 0.59 | 0.46 | 0.98 | 0.96 | 0.95 | 0.73 | 0.59 | 0.33 | 0.82 | 0.84 | 0.83 | 0.94 | 0.28 | 0.32 | 0.67 | 0.89 | 0.08 | 0.91 | 0.94 | 0.79 | 0.77 | 0.90 | 0.40 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.13 | -1.82 | -2.20 | -2.77 | -2.57 | -2.38 | -1.02 | -1.20 | -1.27 | -1.89 | -2.10 | -2.71 | -1.97 | -1.80 | -2.09 | -1.24 | -2.06 | -2.61 | -2.25 | -1.73 | -1.73 | -1.52 | -1.27 | -1.40 | -2.46 | -1.58 | -2.48 | -1.78 | -1.68|
| full sent KL (full->waitk) |  |  | -2.67 | -1.16 | -3.42 | -2.84 | -3.38 | -1.66 | -1.14 | -1.07 | -1.31 | -1.66 | -1.83 | -1.55 | -1.22 | -1.21 | -1.65 | -1.39 | -2.80 | -2.49 | -2.30 | -1.24 | -3.07 | -2.12 | -1.72 | -1.75 | -0.90 | -1.20 | -2.28 | -1.70 | -1.66|
| dec-waitktgt |  |  | am | freitag | </s> | es | ein | fei@@ | e@@ | moni@@ | e | geben | , | und | am | samstag | und | sonntag | wird | eine | part@@ | fei@@ | stattfinden | der | kir@@ | cht@@ | tal@@ | halle | stattfinden | . | </s>|
| full sent tgt |  |  | am | freitag | findet | eine | eine | zer@@ | e@@ | moni@@ | e | geben | , | am | am | samstag | und | sonntag | findet | eine | part@@ | y | in | der | kir@@ | cht@@ | al@@ | halle | stattfinden | . | </s>|
| ref | am | freitag | mit | einem | fe@@ | sta@@ | kt | , | am | samstag | und | sonntag | mit | einem | fest | rund | um | die | kir@@ | cht@@ | al@@ | halle | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | kir@@ | ch@@ | en-@@ | haus@@ | en | kir@@ | chen@@ | fest | festival | will | also | be | held | on | this | celebr@@ | atory | weekend | .|
| waitk tgt |  |  | die | kir@@ | chen@@ | -@@ | haus@@ | en | kir@@ | chen@@ | fest | wird | auch | im | rahmen | der | feier@@ | lichkeiten | vom | 18. | bis | 19. | september | stattfinden | . | </s>|
| waitk prob |  |  | 0.25 | 0.54 | 0.90 | 0.90 | 0.90 | 0.58 | 0.87 | 0.89 | 0.72 | 0.29 | 0.49 | 0.17 | 0.14 | 0.26 | 0.05 | 0.62 | 0.18 | 0.09 | 0.60 | 0.39 | 0.11 | 0.36 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.20 | 0.68 | 0.98 | 0.16 | 0.95 | 0.85 | 0.03 | 0.97 | 0.76 | 0.64 | 0.23 | 0.00 | 0.08 | 0.25 | 0.42 | 0.83 | 0.00 | 0.02 | 0.49 | 0.21 | 0.24 | 0.40 | 0.89 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 13 | 1 | 1 | 0 | 0 | 24 | 11 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.59 | -2.22 | -0.85 | -1.73 | -1.15 | -1.49 | -2.38 | -0.97 | -1.10 | -2.44 | -3.03 | -2.35 | -4.61 | -2.53 | -2.50 | -1.39 | -1.35 | -4.05 | -2.37 | -2.86 | -3.18 | -3.30 | -1.75 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.41 | -3.40 | -1.15 | -1.05 | -1.38 | -2.57 | -1.04 | -1.35 | -1.82 | -3.35 | -2.97 | -3.34 | -4.49 | -2.74 | -5.59 | -1.65 | -3.86 | -3.53 | -2.37 | -2.61 | -3.21 | -3.16 | -1.65 | -1.70|
| full sent prob |  |  | 0.03 | 0.14 | 0.96 | 0.35 | 0.87 | 0.57 | 0.90 | 0.97 | 0.84 | 0.17 | 0.36 | 0.00 | 0.42 | 0.09 | 0.36 | 0.51 | 0.01 | 0.01 | 0.55 | 0.21 | 0.22 | 0.28 | 0.89 | 0.90|
| full sent rank |  |  | 5 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 11 | 0 | 2 | 0 | 0 | 15 | 22 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.02 | -5.77 | -1.04 | -2.17 | -1.31 | -2.73 | -1.50 | -1.02 | -1.09 | -2.51 | -3.34 | -2.30 | -3.60 | -2.38 | -3.51 | -1.92 | -2.86 | -5.11 | -2.37 | -2.93 | -3.40 | -3.74 | -1.75 | -1.69|
| full sent KL (full->waitk) |  |  | -3.39 | -3.15 | -1.13 | -1.20 | -1.33 | -2.46 | -1.67 | -1.35 | -1.85 | -3.33 | -3.01 | -3.37 | -4.53 | -2.73 | -5.58 | -1.51 | -3.86 | -3.52 | -2.40 | -2.61 | -3.21 | -3.12 | -1.65 | -1.70|
| dec-waitktgt |  |  | kir@@ | kir@@ | chen@@ | haus@@ | haus@@ | en | </s> | chen@@ | fest | wird | ebenfalls | stattfinden | anschluss | des | feier@@ | lichkeiten | stattfinden | 16. | bis | 19. | september | stattfinden | . | </s>|
| full sent tgt |  |  | das | kir@@ | chen@@ | haus@@ | haus@@ | en | kir@@ | chen@@ | fest | findet | auch | an | rahmen | des | feier@@ | lichkeiten | stattfinden | freitag | bis | 19. | september | stattfinden | . | </s>|
| ref | an | diesem | fest@@ | wochenende | ist | außerdem | noch | das | kir@@ | chen@@ | -@@ | haus@@ | ener | kir@@ | chen@@ | fest | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | on | the | occasion | of | the | ge@@ | is@@ | ingen | town | anniversary | , | a | new | chron@@ | ic@@ | le | will | also | be | published | .|
| waitk tgt |  |  | an@@ | lässlich | des | ge@@ | si@@ | in@@ | ger | stadt@@ | ju@@ | bi@@ | lä@@ | ums | wurde | eine | neue | ch@@ | roni@@ | k | veröffentlicht | . | </s>|
| waitk prob |  |  | 0.59 | 0.94 | 0.46 | 0.27 | 0.11 | 0.20 | 0.54 | 0.49 | 0.70 | 0.97 | 0.95 | 0.93 | 0.37 | 0.22 | 0.76 | 0.78 | 0.89 | 0.85 | 0.46 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.03 | 0.78 | 0.31 | 0.96 | 0.00 | 0.00 | 0.69 | 0.48 | 0.53 | 0.94 | 0.95 | 0.95 | 0.00 | 0.38 | 0.84 | 0.94 | 0.89 | 0.83 | 0.82 | 0.90 | 0.92|
| dec-waitk rank |  |  | 6 | 0 | 1 | 0 | 71 | 180 | 0 | 0 | 0 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.62 | -1.76 | -1.84 | -0.58 | -4.55 | -5.62 | -1.63 | -2.02 | -3.14 | -1.19 | -1.28 | -1.17 | -2.59 | -2.85 | -1.83 | -1.15 | -1.64 | -2.02 | -1.34 | -1.69 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.60 | -1.09 | -1.81 | -4.97 | -4.45 | -4.53 | -1.95 | -2.38 | -2.26 | -1.08 | -1.24 | -1.32 | -2.96 | -3.53 | -2.55 | -2.46 | -1.55 | -1.90 | -3.70 | -1.70 | -1.66|
| full sent prob |  |  | 0.30 | 0.90 | 0.88 | 0.11 | 0.01 | 0.00 | 0.89 | 0.82 | 0.64 | 0.96 | 0.98 | 0.97 | 0.00 | 0.16 | 0.72 | 0.93 | 0.93 | 0.97 | 0.67 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 1 | 10 | 56 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.96 | -1.34 | -1.37 | -3.81 | -4.32 | -2.34 | -1.10 | -1.29 | -2.73 | -1.15 | -0.96 | -1.06 | -1.94 | -3.57 | -2.22 | -1.22 | -1.25 | -1.01 | -2.15 | -1.74 | -1.66|
| full sent KL (full->waitk) |  |  | -2.74 | -1.18 | -1.83 | -4.78 | -4.45 | -4.54 | -2.02 | -2.52 | -2.33 | -1.09 | -1.27 | -1.34 | -3.01 | -3.49 | -2.48 | -2.46 | -1.59 | -2.00 | -3.64 | -1.69 | -1.65|
| dec-waitktgt |  |  | das | lässlich | der | ge@@ | gei@@ | zin@@ | ger | stadt@@ | ju@@ | bi@@ | lä@@ | ums | </s> | eine | neue | ch@@ | roni@@ | k | veröffentlicht | . | </s>|
| full sent tgt |  |  | an@@ | lässlich | des | stadt@@ | wei@@ | sin@@ | ger | stadt@@ | ju@@ | bi@@ | lä@@ | ums | wird | auch | neue | ch@@ | roni@@ | k | veröffentlicht | . | </s>|
| ref | an@@ | lässlich | des | gei@@ | sin@@ | ger | stadt@@ | ju@@ | bi@@ | lä@@ | ums | wird | auch | noch | eine | neue | ch@@ | roni@@ | k | heraus@@ | gebracht | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | new | chron@@ | ic@@ | le | is | to | be | presented | on | 21 | or | 22 | november | in | the | new | festival | hall | in | ge@@ | is@@ | ingen | .|
| waitk tgt |  |  | die | neue | ch@@ | roni@@ | k | ist | in | der | woche | vom | 21. | bis | 22. | november | in | der | neuen | fest@@ | halle | in | gei@@ | sin@@ | gen | zu | sehen | . | </s>|
| waitk prob |  |  | 0.39 | 0.67 | 0.79 | 0.90 | 0.67 | 0.25 | 0.11 | 0.25 | 0.10 | 0.41 | 0.73 | 0.47 | 0.91 | 0.90 | 0.53 | 0.50 | 0.80 | 0.53 | 0.34 | 0.88 | 0.89 | 0.65 | 0.96 | 0.55 | 0.37 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.20 | 0.88 | 0.97 | 0.92 | 0.92 | 0.03 | 0.05 | 0.29 | 0.00 | 0.00 | 0.57 | 0.57 | 0.96 | 0.95 | 0.35 | 0.40 | 0.86 | 0.88 | 0.20 | 0.65 | 0.95 | 0.86 | 0.97 | 0.48 | 0.34 | 0.90 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 454 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.09 | -1.53 | -0.93 | -1.36 | -1.21 | -2.29 | -4.33 | -3.47 | -4.13 | -4.14 | -2.03 | -2.59 | -1.07 | -1.17 | -3.39 | -3.99 | -1.72 | -1.07 | -1.63 | -2.56 | -1.13 | -1.28 | -1.08 | -3.21 | -2.90 | -1.67 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.44 | -3.08 | -2.39 | -1.57 | -3.02 | -2.97 | -4.16 | -4.31 | -5.21 | -2.82 | -1.64 | -2.56 | -1.30 | -1.65 | -2.30 | -2.94 | -2.17 | -3.24 | -2.66 | -1.48 | -1.60 | -2.74 | -1.18 | -2.84 | -2.37 | -1.67 | -1.68|
| full sent prob |  |  | 0.36 | 0.78 | 0.94 | 0.95 | 0.98 | 0.06 | 0.01 | 0.58 | 0.00 | 0.28 | 0.85 | 0.87 | 0.93 | 0.91 | 0.53 | 0.48 | 0.91 | 0.78 | 0.25 | 0.67 | 0.95 | 0.84 | 0.97 | 0.44 | 0.31 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.89 | -2.04 | -1.19 | -1.18 | -0.77 | -2.36 | -1.65 | -2.61 | -0.65 | -3.39 | -1.54 | -1.31 | -1.31 | -1.50 | -2.60 | -2.66 | -1.32 | -1.64 | -2.22 | -2.77 | -1.14 | -1.40 | -1.09 | -3.45 | -2.86 | -1.68 | -1.69|
| full sent KL (full->waitk) |  |  | -3.43 | -3.03 | -2.37 | -1.59 | -3.05 | -2.96 | -4.20 | -4.38 | -5.22 | -2.92 | -1.79 | -2.66 | -1.28 | -1.62 | -2.41 | -2.97 | -2.21 | -3.20 | -2.64 | -1.49 | -1.60 | -2.73 | -1.18 | -2.82 | -2.37 | -1.67 | -1.67|
| dec-waitktgt |  |  | der | neue | ch@@ | roni@@ | k | soll | da | der | lage | 21 | 21. | bis | 22. | november | in | der | neuen | fest@@ | spiel@@ | in | gei@@ | sin@@ | gen | zu | sehen | . | </s>|
| full sent tgt |  |  | die | neue | ch@@ | roni@@ | k | soll | am | der | neuen | vom | 21. | bis | 22. | november | in | der | neuen | fest@@ | spiel@@ | in | gei@@ | sin@@ | gen | zu | sehen | . | </s>|
| ref | die | neue | ch@@ | roni@@ | k | soll | dann | am | 21. | oder | 22. | november | in | der | neuen | fest@@ | halle | in | gei@@ | sin@@ | gen | vorgestellt | werden | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | however | , | 20@@ | 14 | is | also | a | year | of | many | anni@@ | vers@@ | aries | in | other | respects | .|
| waitk tgt |  |  | 20@@ | 14 | ist | aber | auch | ein | jahr | vieler | jahre@@ | sta@@ | ge | in | anderen | bereichen | . | </s>|
| waitk prob |  |  | 0.26 | 0.96 | 0.44 | 0.30 | 0.76 | 0.79 | 0.83 | 0.29 | 0.42 | 0.71 | 0.91 | 0.73 | 0.87 | 0.31 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.01 | 0.97 | 0.68 | 0.43 | 0.86 | 0.84 | 0.91 | 0.39 | 0.17 | 0.67 | 0.93 | 0.11 | 0.86 | 0.07 | 0.89 | 0.91|
| dec-waitk rank |  |  | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.52 | -1.07 | -2.19 | -2.51 | -1.69 | -1.99 | -1.52 | -2.87 | -3.99 | -1.91 | -1.23 | -2.20 | -1.79 | -3.56 | -1.80 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.49 | -1.19 | -3.31 | -3.70 | -2.37 | -2.21 | -2.14 | -3.42 | -3.26 | -2.04 | -1.32 | -1.63 | -1.63 | -4.16 | -1.68 | -1.67|
| full sent prob |  |  | 0.19 | 0.94 | 0.84 | 0.42 | 0.80 | 0.08 | 0.87 | 0.40 | 0.89 | 0.98 | 0.91 | 0.39 | 0.40 | 0.38 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.48 | -1.35 | -1.59 | -2.56 | -1.95 | -2.78 | -1.58 | -2.90 | -0.96 | -0.81 | -1.35 | -3.14 | -2.94 | -3.29 | -1.76 | -1.67|
| full sent KL (full->waitk) |  |  | -3.47 | -1.17 | -3.36 | -3.70 | -2.33 | -1.71 | -2.11 | -3.43 | -3.51 | -2.22 | -1.30 | -1.82 | -1.29 | -4.23 | -1.69 | -1.67|
| dec-waitktgt |  |  | allerdings | 14 | ist | aber | auch | ein | jahr | vieler | jahre@@ | sta@@ | ge | . | anderen | punkten | . | </s>|
| full sent tgt |  |  | 20@@ | 14 | ist | aber | auch | ander@@ | jahr | vieler | jahre@@ | sta@@ | ge | in | anderen | bereichen | . | </s>|
| ref | 20@@ | 14 | ist | aber | auch | sonst | ein | jahr | mit | vielen | ju@@ | bi@@ | lä@@ | en | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | de@@ | ed | was | drawn | up | in | kir@@ | chen | ( | haus@@ | en | ) | , | which | at | the | time | was | the | location | of | the | cour@@ | thouse | .|
| waitk tgt |  |  | die | tat | wurde | von | der | regierung | in | kir@@ | chen | ( | haus@@ | en | ) | ausge@@ | arbeitet | , | die | damals | der | ort | der | hö@@ | hle | war | . | </s>|
| waitk prob |  |  | 0.44 | 0.16 | 0.72 | 0.17 | 0.17 | 0.08 | 0.24 | 0.45 | 0.67 | 0.86 | 0.91 | 0.94 | 0.89 | 0.15 | 0.90 | 0.88 | 0.72 | 0.42 | 0.24 | 0.64 | 0.44 | 0.14 | 0.19 | 0.93 | 0.91 | 0.90|
| dec-waitk prob |  |  | 0.85 | 0.76 | 0.47 | 0.00 | 0.40 | 0.18 | 0.14 | 0.45 | 0.90 | 0.82 | 0.95 | 0.89 | 0.92 | 0.04 | 0.90 | 0.02 | 0.23 | 0.61 | 0.52 | 0.42 | 0.07 | 0.00 | 0.00 | 0.91 | 0.90 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 26 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 62 | 24 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.61 | -1.98 | -2.69 | -2.67 | -3.72 | -4.08 | -1.62 | -2.48 | -1.30 | -1.96 | -1.06 | -1.77 | -1.54 | -3.07 | -1.40 | -1.75 | -3.86 | -1.98 | -2.72 | -2.43 | -1.57 | -4.61 | -2.77 | -1.43 | -1.70 | -1.59|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.34 | -5.33 | -2.20 | -4.09 | -4.95 | -5.57 | -4.36 | -3.61 | -2.87 | -1.64 | -1.45 | -1.28 | -1.78 | -3.30 | -1.40 | -1.11 | -2.12 | -2.40 | -3.68 | -2.10 | -1.94 | -4.61 | -3.81 | -1.29 | -1.62 | -1.71|
| full sent prob |  |  | 0.38 | 0.05 | 0.68 | 0.01 | 0.05 | 0.01 | 0.22 | 0.27 | 0.89 | 0.82 | 0.89 | 0.90 | 0.89 | 0.03 | 0.93 | 0.85 | 0.26 | 0.57 | 0.25 | 0.13 | 0.08 | 0.00 | 0.00 | 0.89 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 2 | 0 | 2 | 3 | 14 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 7 | 10 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.50 | -4.28 | -2.34 | -1.35 | -5.13 | -4.99 | -3.79 | -3.65 | -1.49 | -1.94 | -1.44 | -1.67 | -1.79 | -3.52 | -1.20 | -1.91 | -3.00 | -2.35 | -3.13 | -2.56 | -1.95 | -2.65 | -3.10 | -1.54 | -1.65 | -1.67|
| full sent KL (full->waitk) |  |  | -3.18 | -5.25 | -2.32 | -4.14 | -4.89 | -5.56 | -4.32 | -3.54 | -2.86 | -1.64 | -1.40 | -1.29 | -1.76 | -3.29 | -1.43 | -1.71 | -2.13 | -2.38 | -3.65 | -1.97 | -2.12 | -4.62 | -3.82 | -1.28 | -1.63 | -1.70|
| dec-waitktgt |  |  | die | tat | wurde | erstellt | der | regierung | kir@@ | kir@@ | chen | ( | haus@@ | en | ) | erstellt | arbeitet | . | die | damals | der | ort | war | gerichts@@ | f@@ | war | . | </s>|
| full sent tgt |  |  | die | de@@ | wurde | in | kir@@ | da@@ | kir@@ | kirchen | chen | ( | haus@@ | en | ) | erstellt | arbeitet | , | die | damals | der | sitz | des | gerichts@@ | fe | war | . | </s>|
| ref | die | ur@@ | kunde | wurde | in | kirchen | ( | haus@@ | en | ) | ge@@ | fertigt | , | das | damals | gericht@@ | splatz | war | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | should | the | &quot; | am | h@@ | ir@@ | sch@@ | en | &quot; | railway | crossing | be | re@@ | constructed | at | great | cost | , | in | order | to | increase | traffic | safety | ?|
| waitk tgt |  |  | sollte | das | &quot; | am | hir@@ | schen | &quot; | -@@ | bahn@@ | kreu@@ | z | re@@ | konstru@@ | iert | werden | , | um | die | fahr@@ | preise | zu | erhöhen | ? | </s>|
| waitk prob |  |  | 0.30 | 0.25 | 0.42 | 0.74 | 0.99 | 0.97 | 0.92 | 0.28 | 0.45 | 0.75 | 0.92 | 0.20 | 0.94 | 0.96 | 0.79 | 0.37 | 0.29 | 0.15 | 0.03 | 0.17 | 0.56 | 0.78 | 0.89 | 0.90|
| dec-waitk prob |  |  | 0.51 | 0.21 | 0.81 | 0.96 | 1.00 | 0.90 | 0.93 | 0.01 | 0.30 | 0.38 | 0.88 | 0.08 | 0.95 | 0.91 | 0.85 | 0.44 | 0.10 | 0.07 | 0.00 | 0.01 | 0.70 | 0.92 | 0.84 | 0.91|
| dec-waitk rank |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 11 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 1 | 34 | 14 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.92 | -2.64 | -1.89 | -0.94 | -0.87 | -1.32 | -1.42 | -4.35 | -2.39 | -3.52 | -1.30 | -3.68 | -1.11 | -1.49 | -1.73 | -2.99 | -3.92 | -4.79 | -2.30 | -4.25 | -2.51 | -1.06 | -2.07 | -1.61|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.89 | -2.88 | -4.04 | -2.77 | -0.95 | -0.99 | -1.57 | -3.89 | -2.54 | -1.73 | -1.34 | -3.98 | -1.23 | -1.14 | -2.01 | -3.07 | -3.97 | -4.74 | -6.07 | -3.52 | -2.93 | -1.73 | -1.69 | -1.69|
| full sent prob |  |  | 0.22 | 0.05 | 0.01 | 0.97 | 0.99 | 0.95 | 0.92 | 0.23 | 0.50 | 0.44 | 0.93 | 0.00 | 0.96 | 0.94 | 0.87 | 0.71 | 0.75 | 0.63 | 0.00 | 0.00 | 0.75 | 0.80 | 0.86 | 0.90|
| full sent rank |  |  | 1 | 2 | 8 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 199 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 36 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.13 | -2.25 | -2.93 | -0.90 | -0.91 | -1.07 | -1.54 | -2.33 | -1.59 | -3.37 | -1.34 | -3.76 | -1.08 | -1.29 | -1.65 | -2.03 | -1.99 | -2.40 | -0.85 | -2.06 | -2.24 | -1.40 | -1.75 | -1.71|
| full sent KL (full->waitk) |  |  | -3.84 | -2.96 | -3.76 | -2.77 | -0.95 | -1.03 | -1.56 | -3.97 | -2.61 | -1.76 | -1.38 | -3.96 | -1.24 | -1.16 | -2.03 | -3.17 | -4.11 | -4.80 | -6.06 | -3.51 | -2.96 | -1.66 | -1.71 | -1.69|
| dec-waitktgt |  |  | sollte | &quot; | &quot; | am | hir@@ | schen | &quot; | </s> | eisenbahn@@ | kreu@@ | z | </s> | konstru@@ | iert | werden | , | und | das | kosten | gäste | zu | erhöhen | ? | </s>|
| full sent tgt |  |  | soll | die | eisenbahn@@ | am | hir@@ | schen | &quot; | eisenbahn@@ | bahn@@ | kreu@@ | z | zu | konstru@@ | iert | werden | , | um | die | verkehr@@ | sicherheit | zu | erhöhen | ? | </s>|
| ref | soll | der | bahn@@ | übergang | &quot; | am | hir@@ | schen | &quot; | auf@@ | w@@ | än@@ | dig | um@@ | gebaut | werden | , | um | die | verkehr@@ | ssicherheit | zu | erhöhen | ? | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | sch@@ | il@@ | t@@ | ach | will | have | to | contribute | up | to | eur | 2@@ | 20@@ | ,000 | to | the | project | .|
| waitk tgt |  |  | schil@@ | ta@@ | ch | wird | sich | an | der | entwicklung | der | europäischen | union | bis | zu | 2@@ | 20@@ | .000 | euro | beteiligen | müssen | . | </s>|
| waitk prob |  |  | 0.84 | 0.46 | 0.90 | 0.58 | 0.08 | 0.27 | 0.22 | 0.05 | 0.24 | 0.05 | 0.10 | 0.29 | 0.70 | 0.83 | 0.84 | 0.97 | 0.49 | 0.81 | 0.86 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.21 | 0.95 | 0.55 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.04 | 0.46 | 0.69 | 0.89 | 0.94 | 0.94 | 0.77 | 0.76 | 0.93 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 1 | 30 | 14 | 2 | 102 | 11 | 52 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -4.12 | -0.85 | -3.82 | -0.79 | -4.40 | -5.41 | -4.21 | -6.10 | -3.15 | -4.80 | -5.43 | -3.70 | -2.53 | -1.52 | -1.04 | -1.30 | -1.72 | -1.99 | -1.17 | -1.67 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  | -1.12 | -3.33 | -1.27 | -2.59 | -4.71 | -3.77 | -3.48 | -5.88 | -2.96 | -5.86 | -4.90 | -2.74 | -2.34 | -1.90 | -1.58 | -1.00 | -1.81 | -1.85 | -1.71 | -1.67 | -1.68|
| full sent prob |  |  | 0.95 | 0.99 | 0.94 | 0.45 | 0.01 | 0.03 | 0.10 | 0.03 | 0.04 | 0.00 | 0.08 | 0.00 | 0.81 | 0.82 | 0.81 | 0.96 | 0.74 | 0.74 | 0.85 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 6 | 3 | 2 | 2 | 6 | 111 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.05 | -0.50 | -1.34 | -2.78 | -2.41 | -3.21 | -2.71 | -4.60 | -3.27 | -6.08 | -5.52 | -1.59 | -1.90 | -1.97 | -1.54 | -1.17 | -1.56 | -2.26 | -1.57 | -1.69 | -1.69|
| full sent KL (full->waitk) |  |  | -1.64 | -3.35 | -1.57 | -2.81 | -4.72 | -3.79 | -3.52 | -5.88 | -2.99 | -5.86 | -4.91 | -2.66 | -2.41 | -1.85 | -1.50 | -1.01 | -1.82 | -1.84 | -1.66 | -1.67 | -1.67|
| dec-waitktgt |  |  | schil@@ | ta@@ | ch | </s> | </s> | mü@@ | </s> | bei@@ | bis | mittel | 2@@ | bis | zu | 2@@ | 20@@ | .000 | euro | beteiligen | müssen | . | </s>|
| full sent tgt |  |  | schil@@ | ta@@ | ch | wird | bis | mit | dem | finanzierung | bis | projekte | union | beteiligen | zu | 2@@ | 20@@ | .000 | euro | beteiligen | müssen | . | </s>|
| ref | schil@@ | ta@@ | ch | muss | dafür | 2@@ | 20 | 000 | euro | in | die | hand | nehmen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | deutsche | bahn | hopes | to | improve | the | kin@@ | zi@@ | g@@ | tal | railway | line | in | the | coming | year | .|
| waitk tgt |  |  | die | deutsche | bahn | ho@@ | fft | , | die | kin@@ | zi@@ | g@@ | tal@@ | bahn | in | den | kommenden | jahren | zu | verbessern | . | </s>|
| waitk prob |  |  | 0.37 | 0.90 | 0.95 | 0.52 | 0.98 | 0.71 | 0.34 | 0.28 | 0.93 | 0.79 | 0.54 | 0.39 | 0.42 | 0.87 | 0.58 | 0.90 | 0.60 | 0.81 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.42 | 0.84 | 0.96 | 0.45 | 0.99 | 0.68 | 0.37 | 0.95 | 0.62 | 0.86 | 0.46 | 0.57 | 0.17 | 0.35 | 0.51 | 0.90 | 0.68 | 0.83 | 0.91 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -1.98 | -1.90 | -1.14 | -2.54 | -0.94 | -2.33 | -2.84 | -0.71 | -3.56 | -1.63 | -2.12 | -2.00 | -4.16 | -3.13 | -1.40 | -1.50 | -2.28 | -1.97 | -1.67 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.67 | -1.43 | -1.26 | -2.58 | -1.03 | -2.43 | -2.97 | -4.85 | -1.15 | -2.05 | -2.30 | -1.96 | -2.60 | -1.32 | -1.39 | -1.61 | -2.65 | -2.10 | -1.72 | -1.66|
| full sent prob |  |  | 0.49 | 0.90 | 0.96 | 0.56 | 0.96 | 0.48 | 0.45 | 0.38 | 0.81 | 0.74 | 0.29 | 0.36 | 0.10 | 0.38 | 0.45 | 0.87 | 0.55 | 0.79 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.57 | -1.51 | -1.10 | -2.54 | -1.15 | -2.45 | -2.51 | -4.14 | -2.38 | -2.47 | -2.23 | -2.32 | -2.33 | -3.99 | -1.27 | -1.68 | -2.59 | -2.15 | -1.69 | -1.67|
| full sent KL (full->waitk) |  |  | -3.69 | -1.48 | -1.27 | -2.62 | -1.01 | -2.32 | -2.97 | -4.72 | -1.29 | -1.97 | -2.26 | -1.93 | -2.72 | -1.34 | -1.38 | -1.59 | -2.60 | -2.07 | -1.71 | -1.66|
| dec-waitktgt |  |  | deutsche | deutsche | bahn | ho@@ | fft | , | die | kin@@ | zi@@ | g@@ | tal@@ | bahn | in | den | kommenden | jahren | zu | verbessern | . | </s>|
| full sent tgt |  |  | die | deutsche | bahn | ho@@ | fft | , | die | kin@@ | zi@@ | g@@ | tal | bahn | im | den | nächsten | jahren | zu | verbessern | . | </s>|
| ref | die | deutsche | bahn | will | im | kommenden | jahr | die | kin@@ | zi@@ | g@@ | tal@@ | -@@ | bahn@@ | strecke | verbessern | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | at | the | crossing | , | the | town | is | planning | to | increase | the | height | of | the | mouth | of | the | tunnel | to | the | west | of | the | railway | line | .|
| waitk tgt |  |  | an | der | kreu@@ | zung | befindet | sich | die | stadt | , | um | die | höhe | des | mün@@ | des | des | tun@@ | n@@ | els | im | westen | der | eisenbahn@@ | linie | zu | erhöhen | . | </s>|
| waitk prob |  |  | 0.28 | 0.88 | 0.96 | 0.99 | 0.25 | 0.91 | 0.58 | 0.55 | 0.48 | 0.63 | 0.72 | 0.81 | 0.51 | 0.60 | 0.42 | 0.79 | 0.94 | 0.96 | 0.97 | 0.40 | 0.89 | 0.50 | 0.40 | 0.58 | 0.73 | 0.80 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.38 | 0.88 | 0.81 | 0.94 | 0.07 | 0.87 | 0.64 | 0.92 | 0.08 | 0.32 | 0.70 | 0.81 | 0.42 | 0.06 | 0.64 | 0.68 | 0.88 | 0.82 | 0.82 | 0.06 | 0.76 | 0.40 | 0.40 | 0.72 | 0.81 | 0.75 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 1 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.71 | -1.85 | -1.75 | -1.37 | -3.26 | -1.89 | -2.69 | -1.11 | -4.39 | -2.80 | -2.43 | -1.94 | -1.98 | -1.10 | -3.00 | -2.51 | -1.68 | -2.16 | -1.85 | -1.78 | -1.64 | -2.27 | -1.48 | -1.53 | -1.97 | -1.96 | -1.72 | -1.63|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.97 | -1.70 | -0.98 | -0.92 | -3.56 | -1.56 | -2.68 | -3.71 | -3.18 | -2.12 | -2.44 | -2.10 | -2.01 | -1.92 | -3.81 | -2.01 | -1.25 | -1.03 | -0.97 | -3.04 | -1.39 | -1.85 | -2.24 | -2.24 | -2.40 | -1.65 | -1.67 | -1.68|
| full sent prob |  |  | 0.13 | 0.75 | 0.65 | 0.97 | 0.01 | 0.89 | 0.35 | 0.52 | 0.29 | 0.06 | 0.65 | 0.20 | 0.39 | 0.18 | 0.18 | 0.80 | 0.58 | 0.96 | 0.97 | 0.12 | 0.82 | 0.74 | 0.27 | 0.75 | 0.77 | 0.76 | 0.90 | 0.90|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 19 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -4.17 | -2.27 | -2.49 | -1.08 | -4.05 | -1.74 | -3.09 | -3.65 | -3.71 | -2.59 | -2.60 | -3.70 | -1.94 | -3.27 | -4.16 | -2.01 | -2.94 | -1.16 | -1.03 | -3.24 | -1.68 | -2.07 | -1.88 | -1.58 | -2.15 | -1.99 | -1.73 | -1.71|
| full sent KL (full->waitk) |  |  | -3.91 | -1.61 | -0.84 | -0.95 | -3.50 | -1.57 | -2.55 | -3.52 | -3.26 | -2.01 | -2.41 | -1.69 | -2.01 | -1.93 | -3.66 | -2.09 | -1.01 | -1.14 | -1.10 | -3.07 | -1.43 | -1.89 | -2.21 | -2.25 | -2.37 | -1.66 | -1.67 | -1.67|
| dec-waitktgt |  |  | an | der | kreu@@ | zung | ist | sich | die | stadt | vor | die | die | höhe | der | m@@ | des | des | tun@@ | n@@ | els | west@@ | westen | des | bahn@@ | linie | zu | erhöhen | . | </s>|
| full sent tgt |  |  | an | der | kreu@@ | zung | plan@@ | sich | die | stadt | , | die | die | m@@ | der | m@@ | dungs@@ | des | tun@@ | n@@ | els | in | westen | der | bahn@@ | linie | zu | erhöhen | . | </s>|
| ref | dort | plan@@ | t | die | stadt | , | in | höhe | des | dor@@ | tigen | tun@@ | n@@ | el@@ | m@@ | un@@ | des | west@@ | lich | der | bahn@@ | glei@@ | se | eine | aus@@ | bu@@ | chtung | zu | bauen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | may@@ | or | thomas | ha@@ | as | re@@ | tor@@ | ted | : | the | &quot; | h@@ | ir@@ | sch@@ | en | &quot; | railway | crossing | is | used | regularly | for | the | transportation | of | long | log@@ | s | .|
| waitk tgt |  |  | bürger@@ | meister | thomas | ha@@ | as | re@@ | tor@@ | tierte | : | die | &quot; | hir@@ | schen | &quot; | bahn | kreu@@ | zung | wird | regelmäßig | für | die | be@@ | förderung | von | langen | lo@@ | gs | verwendet | . | </s>|
| waitk prob |  |  | 0.31 | 0.93 | 0.94 | 0.92 | 0.93 | 0.27 | 0.92 | 0.37 | 0.80 | 0.27 | 0.46 | 0.98 | 0.96 | 0.92 | 0.35 | 0.20 | 0.63 | 0.63 | 0.57 | 0.55 | 0.51 | 0.55 | 0.97 | 0.44 | 0.49 | 0.43 | 0.69 | 0.38 | 0.90 | 0.91|
| dec-waitk prob |  |  | 0.31 | 0.97 | 0.90 | 0.91 | 0.95 | 0.08 | 0.74 | 0.33 | 0.37 | 0.02 | 0.47 | 0.91 | 0.74 | 0.91 | 0.00 | 0.00 | 0.03 | 0.06 | 0.39 | 0.10 | 0.62 | 0.41 | 0.89 | 0.54 | 0.11 | 0.10 | 0.51 | 0.24 | 0.89 | 0.92|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 218 | 439 | 3 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.55 | -0.98 | -1.60 | -1.45 | -1.27 | -3.82 | -2.66 | -2.90 | -2.93 | -1.84 | -3.58 | -1.44 | -1.58 | -1.55 | -1.82 | -0.86 | -1.99 | -5.21 | -3.84 | -4.40 | -2.37 | -2.83 | -1.46 | -2.59 | -1.89 | -5.01 | -1.93 | -2.47 | -1.74 | -1.57|
| dec-waitk KL (dec-waitk->waitk) |  |  | -4.03 | -1.31 | -1.27 | -1.46 | -1.42 | -3.57 | -1.27 | -2.96 | -1.84 | -2.87 | -3.53 | -0.96 | -0.88 | -1.54 | -2.38 | -3.38 | -1.21 | -2.17 | -2.88 | -2.62 | -2.94 | -3.06 | -0.97 | -3.21 | -2.76 | -3.56 | -2.45 | -2.65 | -1.69 | -1.65|
| full sent prob |  |  | 0.59 | 0.89 | 0.89 | 0.94 | 0.95 | 0.11 | 0.84 | 0.13 | 0.79 | 0.21 | 0.32 | 0.98 | 0.93 | 0.93 | 0.13 | 0.17 | 0.94 | 0.77 | 0.64 | 0.48 | 0.10 | 0.77 | 0.95 | 0.74 | 0.36 | 0.20 | 0.64 | 0.28 | 0.89 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.74 | -1.54 | -1.67 | -1.26 | -1.29 | -2.98 | -2.04 | -2.04 | -2.40 | -2.80 | -3.44 | -0.95 | -1.12 | -1.43 | -2.25 | -3.05 | -0.92 | -2.07 | -2.05 | -2.41 | -1.53 | -1.67 | -1.19 | -1.84 | -2.47 | -4.35 | -1.88 | -2.57 | -1.74 | -1.66|
| full sent KL (full->waitk) |  |  | -4.10 | -1.25 | -1.26 | -1.48 | -1.42 | -3.60 | -1.35 | -2.99 | -2.12 | -2.98 | -3.47 | -1.02 | -1.03 | -1.55 | -2.51 | -3.44 | -1.66 | -2.55 | -3.00 | -2.80 | -2.81 | -3.22 | -1.02 | -3.28 | -2.82 | -3.60 | -2.52 | -2.65 | -1.68 | -1.65|
| dec-waitktgt |  |  | ober@@ | meister | thomas | ha@@ | as | wider@@ | tor@@ | tierte | : | </s> | &quot; | hir@@ | schen | &quot; | </s> | </s> | z | </s> | regelmäßig | genutzt | die | be@@ | förderung | von | lang@@ | lo@@ | gs | genutzt | . | </s>|
| full sent tgt |  |  | bürger@@ | meister | thomas | ha@@ | as | beri@@ | tor@@ | ted | : | der | &quot; | hir@@ | schen | &quot; | bahn@@ | über@@ | zung | wird | regelmäßig | für | den | be@@ | förderung | von | lang@@ | lo@@ | gs | verwendet | . | </s>|
| ref | bürger@@ | meister | thomas | ha@@ | as | wider@@ | sprach | : | der | bahn@@ | übergang | &quot; | hir@@ | schen | &quot; | werde | regelmäßig | für | lang@@ | holz@@ | transpor@@ | te | genutzt | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | counc@@ | ill@@ | ors | agreed | to | have | an | investigation | conducted | as | to | what | costs | the | planned | wid@@ | ening | of | the | road | would | inc@@ | ur | .|
| waitk tgt |  |  | der | rat | stimm@@ | te | zu | , | eine | untersuchung | durchzuführen | , | um | welche | kosten | die | geplan@@ | te | erweiterung | der | straßen@@ | be@@ | förderung | für | die | dauer | der | strecke | verursachen | würde | . | </s>|
| waitk prob |  |  | 0.33 | 0.75 | 0.37 | 0.87 | 0.38 | 0.89 | 0.53 | 0.79 | 0.28 | 0.89 | 0.30 | 0.71 | 0.89 | 0.41 | 0.83 | 0.88 | 0.34 | 0.53 | 0.31 | 0.18 | 0.52 | 0.22 | 0.36 | 0.06 | 0.34 | 0.07 | 0.22 | 0.70 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.54 | 0.89 | 0.06 | 0.93 | 0.64 | 0.42 | 0.35 | 0.87 | 0.13 | 0.02 | 0.03 | 0.04 | 0.92 | 0.21 | 0.83 | 0.27 | 0.67 | 0.09 | 0.08 | 0.02 | 0.67 | 0.00 | 0.35 | 0.02 | 0.48 | 0.01 | 0.17 | 0.41 | 0.90 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 | 0 | 1 | 0 | 1 | 2 | 12 | 0 | 77 | 0 | 8 | 0 | 15 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.21 | -1.42 | -2.53 | -1.33 | -2.03 | -3.22 | -2.98 | -1.38 | -3.20 | -2.16 | -3.10 | -3.32 | -1.39 | -2.79 | -1.53 | -2.21 | -1.53 | -3.29 | -2.20 | -4.16 | -1.73 | -3.88 | -3.03 | -5.27 | -2.50 | -4.77 | -3.72 | -2.23 | -1.71 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.32 | -2.29 | -2.56 | -1.77 | -3.24 | -1.39 | -2.79 | -2.01 | -3.17 | -1.08 | -3.25 | -1.52 | -1.68 | -2.95 | -1.60 | -1.30 | -2.74 | -1.74 | -3.41 | -3.84 | -2.73 | -3.39 | -2.94 | -4.94 | -3.00 | -4.92 | -3.72 | -1.71 | -1.59 | -1.69|
| full sent prob |  |  | 0.02 | 0.87 | 0.13 | 0.92 | 0.56 | 0.87 | 0.41 | 0.86 | 0.06 | 0.88 | 0.10 | 0.08 | 0.91 | 0.32 | 0.83 | 0.91 | 0.51 | 0.18 | 0.02 | 0.01 | 0.53 | 0.00 | 0.23 | 0.02 | 0.52 | 0.01 | 0.18 | 0.73 | 0.91 | 0.91|
| full sent rank |  |  | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 19 | 0 | 47 | 0 | 1 | 0 | 10 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -1.96 | -1.59 | -3.36 | -1.47 | -2.11 | -1.86 | -2.41 | -1.47 | -3.01 | -1.77 | -2.90 | -2.76 | -1.50 | -2.74 | -1.49 | -1.60 | -3.02 | -2.00 | -1.88 | -3.95 | -2.21 | -3.18 | -3.58 | -4.54 | -2.62 | -4.64 | -3.60 | -1.78 | -1.60 | -1.68|
| full sent KL (full->waitk) |  |  | -3.33 | -2.28 | -2.56 | -1.76 | -3.21 | -1.72 | -2.82 | -2.00 | -3.15 | -1.72 | -3.30 | -1.56 | -1.68 | -2.98 | -1.59 | -1.76 | -2.68 | -1.96 | -3.42 | -3.85 | -2.67 | -3.40 | -2.93 | -4.94 | -3.01 | -4.92 | -3.71 | -1.88 | -1.60 | -1.68|
| dec-waitktgt |  |  | der | rat | eini@@ | te | zu | , | eine | untersuchung | nach | </s> | </s> | die | kosten | es | geplan@@ | ten | erweiterung | zu | straße | verkehrs@@ | förderung | verursachen | die | zukunft | der | reise | verursachen | würde | . | </s>|
| full sent tgt |  |  | die | rat | hat | te | zu | , | eine | untersuchung | darüber | , | welche | zu | kosten | die | geplan@@ | te | erweiterung | des | straße | verkehrs@@ | förderung | verursachen | die | zukunft | der | reise | verursachen | würde | . | </s>|
| ref | die | rä@@ | te | kamen | überein | , | untersuchen | zu | lassen | , | welche | kosten | die | ange@@ | da@@ | chte | verbrei@@ | ter@@ | ung | der | straße | verursachen | würde | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | town | , | as | the | authority | responsible | for | road | construction | , | would | then | bear | responsibility | for | this | .|
| waitk tgt |  |  | die | stadt | , | als | die | für | den | straßen@@ | bau | verantwor@@ | tliche | behörde | , | würde | dann | dafür | verantwortlich | sein | . | </s>|
| waitk prob |  |  | 0.40 | 0.77 | 0.39 | 0.50 | 0.40 | 0.47 | 0.36 | 0.79 | 0.88 | 0.36 | 0.92 | 0.72 | 0.86 | 0.43 | 0.65 | 0.50 | 0.46 | 0.71 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.40 | 0.94 | 0.42 | 0.30 | 0.26 | 0.13 | 0.19 | 0.91 | 0.93 | 0.03 | 0.95 | 0.21 | 0.42 | 0.03 | 0.04 | 0.51 | 0.30 | 0.79 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.19 | -1.10 | -1.91 | -3.18 | -3.00 | -4.08 | -2.15 | -1.15 | -1.32 | -1.31 | -1.21 | -2.83 | -2.59 | -3.92 | -2.95 | -2.12 | -2.71 | -2.29 | -1.66 | -1.58|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.92 | -2.41 | -3.21 | -2.76 | -3.64 | -3.53 | -2.52 | -1.74 | -1.70 | -2.37 | -1.27 | -1.90 | -1.67 | -3.45 | -2.14 | -2.56 | -2.84 | -2.38 | -1.67 | -1.68|
| full sent prob |  |  | 0.30 | 0.44 | 0.22 | 0.20 | 0.38 | 0.49 | 0.77 | 0.81 | 0.95 | 0.11 | 0.92 | 0.48 | 0.90 | 0.22 | 0.27 | 0.59 | 0.33 | 0.77 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -3.42 | -3.83 | -3.10 | -2.75 | -3.45 | -3.17 | -1.66 | -1.61 | -1.17 | -1.88 | -1.36 | -3.30 | -1.67 | -3.57 | -3.60 | -2.05 | -2.58 | -2.33 | -1.68 | -1.66|
| full sent KL (full->waitk) |  |  | -3.89 | -2.09 | -3.13 | -2.73 | -3.68 | -3.66 | -2.58 | -1.67 | -1.71 | -2.37 | -1.25 | -2.06 | -2.01 | -3.53 | -2.27 | -2.58 | -2.85 | -2.37 | -1.67 | -1.68|
| dec-waitktgt |  |  | die | stadt | als | die | die | behörde | die | straßen@@ | bau | zu@@ | tliche | stadt | , | </s> | dafür | dafür | verantwortlich | sein | . | </s>|
| full sent tgt |  |  | die | stadt | als | die | die | für | den | straßen@@ | bau | zu@@ | tliche | behörde | , | würde | dann | dafür | verantwortlich | sein | . | </s>|
| ref | die | verantwortung | hierfür | tra@@ | ge | wiederum | die | stadt | als | straßen@@ | bau@@ | last@@ | trä@@ | ger@@ | in | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | trains | themselves | , | coming | from | the | central | station | , | must | also | be | sufficiently | slow@@ | ed | down | so | that | there | is | no | threat | of | col@@ | li@@ | sion | .|
| waitk tgt |  |  | die | züge | selbst | , | die | aus | dem | hauptbahnhof | kommen | , | müssen | auch | ausreichend | ver@@ | lang@@ | sam@@ | t | werden | , | damit | es | keine | gefahr | des | kol@@ | li@@ | sion@@ | s | gibt | . | </s>|
| waitk prob |  |  | 0.45 | 0.81 | 0.34 | 0.53 | 0.68 | 0.46 | 0.77 | 0.83 | 0.80 | 0.90 | 0.84 | 0.55 | 0.55 | 0.78 | 0.95 | 0.93 | 0.94 | 0.73 | 0.91 | 0.42 | 0.30 | 0.73 | 0.68 | 0.19 | 0.69 | 0.95 | 0.68 | 0.55 | 0.85 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.53 | 0.84 | 0.63 | 0.62 | 0.68 | 0.43 | 0.89 | 0.82 | 0.73 | 0.78 | 0.84 | 0.24 | 0.49 | 0.48 | 0.99 | 0.90 | 0.93 | 0.83 | 0.06 | 0.34 | 0.07 | 0.38 | 0.27 | 0.08 | 0.80 | 0.94 | 0.40 | 0.33 | 0.90 | 0.91 | 0.92|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 6 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.49 | -1.53 | -1.88 | -2.56 | -2.53 | -2.68 | -1.56 | -1.78 | -2.09 | -2.39 | -1.80 | -2.46 | -1.98 | -2.47 | -0.89 | -1.43 | -1.41 | -1.74 | -1.76 | -3.77 | -2.41 | -2.79 | -2.47 | -3.06 | -1.18 | -1.30 | -1.49 | -3.01 | -1.54 | -1.65 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.72 | -1.82 | -3.34 | -2.47 | -2.57 | -2.51 | -2.01 | -1.65 | -1.76 | -1.57 | -1.71 | -2.55 | -2.47 | -1.70 | -1.27 | -1.34 | -1.30 | -2.09 | -0.99 | -2.48 | -3.24 | -1.95 | -1.72 | -3.30 | -1.39 | -1.25 | -1.68 | -2.77 | -1.79 | -1.66 | -1.68|
| full sent prob |  |  | 0.26 | 0.87 | 0.65 | 0.55 | 0.87 | 0.09 | 0.89 | 0.75 | 0.64 | 0.89 | 0.86 | 0.30 | 0.40 | 0.29 | 0.97 | 0.94 | 0.92 | 0.83 | 0.90 | 0.49 | 0.14 | 0.23 | 0.00 | 0.09 | 0.70 | 0.94 | 0.42 | 0.37 | 0.89 | 0.91 | 0.91|
| full sent rank |  |  | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.75 | -1.45 | -2.19 | -2.18 | -1.66 | -1.84 | -1.57 | -1.92 | -2.59 | -1.80 | -1.71 | -2.27 | -2.46 | -2.96 | -1.05 | -1.21 | -1.54 | -1.82 | -1.72 | -2.22 | -2.97 | -2.90 | -0.25 | -3.35 | -1.34 | -1.34 | -1.57 | -2.81 | -1.57 | -1.64 | -1.65|
| full sent KL (full->waitk) |  |  | -3.62 | -1.84 | -3.35 | -2.45 | -2.68 | -2.40 | -2.01 | -1.61 | -1.69 | -1.65 | -1.72 | -2.61 | -2.42 | -1.58 | -1.25 | -1.37 | -1.29 | -2.08 | -1.62 | -2.55 | -3.22 | -1.86 | -1.57 | -3.30 | -1.35 | -1.25 | -1.69 | -2.79 | -1.78 | -1.66 | -1.67|
| dec-waitktgt |  |  | die | züge | selbst | , | die | aus | dem | hauptbahnhof | kommen | , | müssen | ausreichend | ausreichend | ver@@ | lang@@ | sam@@ | t | werden | . | damit | keine | keine | kol@@ | gibt | kol@@ | li@@ | sions@@ | s | gibt | . | </s>|
| full sent tgt |  |  | auch | züge | selbst | , | die | vom | dem | hauptbahnhof | kommen | , | müssen | ebenfalls | ausreichend | ver@@ | lang@@ | sam@@ | t | werden | , | damit | keine | nicht | kol@@ | von | kol@@ | li@@ | sions@@ | s | gibt | . | </s>|
| ref | selbst | züge | vom | hauptbahnhof | her | müssten | an | dieser | stelle | schon | soweit | ab@@ | geb@@ | re@@ | m@@ | st | sein | , | dass | keine | kol@@ | li@@ | sion | dro@@ | he | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | there | were | 30 | proposals | to | choose | from | , | five | of | which | are | still | in | the | running | .|
| waitk tgt |  |  | es | gab | 30 | vorschläge | , | aus | denen | fünf | , | die | noch | in | der | lauf@@ | bahn | sind | , | ausgewählt | wurden | . | </s>|
| waitk prob |  |  | 0.37 | 0.40 | 0.81 | 0.79 | 0.57 | 0.36 | 0.84 | 0.23 | 0.05 | 0.31 | 0.62 | 0.22 | 0.45 | 0.32 | 0.36 | 0.49 | 0.79 | 0.29 | 0.46 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.17 | 0.47 | 0.84 | 0.90 | 0.44 | 0.68 | 0.95 | 0.00 | 0.00 | 0.02 | 0.53 | 0.03 | 0.27 | 0.02 | 0.59 | 0.77 | 0.81 | 0.45 | 0.34 | 0.91 | 0.91|
| dec-waitk rank |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 89 | 227 | 5 | 0 | 3 | 1 | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.72 | -2.35 | -1.89 | -1.38 | -2.29 | -1.94 | -1.10 | -3.41 | -2.79 | -2.24 | -3.13 | -3.61 | -2.89 | -4.56 | -2.16 | -1.75 | -1.86 | -2.29 | -1.81 | -1.65 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.55 | -2.72 | -2.09 | -2.26 | -2.40 | -2.67 | -1.70 | -2.97 | -5.17 | -4.04 | -2.68 | -3.84 | -3.17 | -3.99 | -3.24 | -2.54 | -1.85 | -3.54 | -1.97 | -1.68 | -1.68|
| full sent prob |  |  | 0.61 | 0.35 | 0.77 | 0.85 | 0.54 | 0.06 | 0.95 | 0.00 | 0.00 | 0.27 | 0.73 | 0.26 | 0.02 | 0.01 | 0.68 | 0.77 | 0.90 | 0.57 | 0.40 | 0.91 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 46 | 39 | 1 | 0 | 0 | 6 | 16 | 0 | 0 | 0 | 0 | 1 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.72 | -2.90 | -2.32 | -1.72 | -2.12 | -1.86 | -1.19 | -3.82 | -2.40 | -1.65 | -1.90 | -3.19 | -1.73 | -3.85 | -2.09 | -1.77 | -1.63 | -2.00 | -1.78 | -1.63 | -1.67|
| full sent KL (full->waitk) |  |  | -3.67 | -2.69 | -2.04 | -2.23 | -2.44 | -2.58 | -1.70 | -2.97 | -5.17 | -4.11 | -2.79 | -3.88 | -3.04 | -3.99 | -3.25 | -2.54 | -1.90 | -3.56 | -1.98 | -1.68 | -1.68|
| dec-waitktgt |  |  | 30 | gab | 30 | vorschläge | , | aus | denen | wir | ausgewählt | von | noch | nicht | den | an@@ | bahn | sind | , | ausgewählt | werden | . | </s>|
| full sent tgt |  |  | es | gab | 30 | vorschläge | , | von | denen | man | noch | von | noch | in | arbeit | hand | bahn | sind | , | ausgewählt | werden | . | </s>|
| ref | 30 | vorschläge | standen | zur | auswahl | , | fünf | sind | noch | im | rennen | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | a@@ | stronom@@ | ers | have | already | found | more | than | 1@@ | ,000 | plan@@ | ets | near | other | stars | .|
| waitk tgt |  |  | ast@@ | ron@@ | omen | haben | bereits | mehr | als | 1.@@ | 000 | planeten | in | der | nähe | anderer | sterne | gefunden | . | </s>|
| waitk prob |  |  | 0.52 | 0.95 | 0.97 | 0.69 | 0.71 | 0.66 | 0.92 | 0.48 | 0.95 | 0.91 | 0.68 | 0.78 | 0.94 | 0.77 | 0.60 | 0.72 | 0.91 | 0.91|
| dec-waitk prob |  |  | 0.60 | 0.96 | 0.81 | 0.61 | 0.71 | 0.90 | 0.86 | 0.59 | 0.98 | 0.48 | 0.53 | 0.78 | 0.86 | 0.53 | 0.66 | 0.79 | 0.90 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.03 | -1.16 | -1.70 | -2.70 | -1.96 | -1.35 | -1.90 | -1.40 | -0.95 | -3.76 | -2.34 | -1.95 | -1.91 | -2.20 | -2.27 | -1.71 | -1.68 | -1.62|
| dec-waitk KL (dec-waitk->waitk) |  |  | -2.90 | -1.24 | -0.91 | -2.50 | -2.06 | -1.89 | -1.52 | -1.72 | -1.19 | -1.01 | -2.23 | -2.15 | -1.15 | -1.61 | -2.37 | -2.20 | -1.65 | -1.68|
| full sent prob |  |  | 0.59 | 0.96 | 0.96 | 0.70 | 0.72 | 0.68 | 0.93 | 0.74 | 0.95 | 0.90 | 0.75 | 0.87 | 0.95 | 0.69 | 0.67 | 0.77 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.62 | -1.20 | -1.16 | -2.51 | -1.77 | -2.32 | -1.47 | -1.29 | -1.18 | -1.41 | -2.10 | -1.77 | -1.22 | -1.88 | -2.03 | -1.74 | -1.70 | -1.67|
| full sent KL (full->waitk) |  |  | -2.88 | -1.24 | -1.03 | -2.56 | -2.07 | -1.78 | -1.58 | -1.74 | -1.17 | -1.33 | -2.35 | -2.20 | -1.22 | -1.71 | -2.37 | -2.19 | -1.65 | -1.67|
| dec-waitktgt |  |  | ast@@ | ron@@ | omen | haben | bereits | mehr | als | 1.@@ | 000 | planeten | in | der | nähe | anderer | sterne | gefunden | . | </s>|
| full sent tgt |  |  | ast@@ | ron@@ | omen | haben | bereits | mehr | als | 1.@@ | 000 | planeten | in | der | nähe | anderer | sterne | gefunden | . | </s>|
| ref | mehr | als | 1000 | planeten | bei | anderen | ster@@ | nen | haben | ast@@ | ron@@ | omen | bereits | gefunden | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | whether | or | not | life | exists | on | at | least | some | of | these | , | no-@@ | one | knows | .|
| waitk tgt |  |  | ob | das | leben | auf | europäischer | ebene | zumindest | auf | einigen | dieser | , | niemand | weiß | . | </s>|
| waitk prob |  |  | 0.53 | 0.46 | 0.88 | 0.65 | 0.19 | 0.70 | 0.38 | 0.22 | 0.54 | 0.72 | 0.40 | 0.44 | 0.87 | 0.57 | 0.91|
| dec-waitk prob |  |  | 0.74 | 0.04 | 0.93 | 0.12 | 0.00 | 0.15 | 0.00 | 0.08 | 0.59 | 0.16 | 0.00 | 0.28 | 0.94 | 0.12 | 0.92|
| dec-waitk rank |  |  | 0 | 3 | 0 | 1 | 847 | 0 | 1760 | 1 | 0 | 0 | 32 | 1 | 0 | 3 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.53 | -2.15 | -1.38 | -3.55 | -3.52 | -5.19 | -2.56 | -3.98 | -2.69 | -3.34 | -5.10 | -2.98 | -1.22 | -2.44 | -1.56|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.31 | -3.07 | -1.77 | -2.47 | -4.12 | -2.20 | -3.33 | -4.03 | -2.85 | -2.04 | -4.01 | -3.21 | -1.60 | -2.20 | -1.66|
| full sent prob |  |  | 0.74 | 0.06 | 0.93 | 0.06 | 0.00 | 0.88 | 0.45 | 0.13 | 0.60 | 0.26 | 0.00 | 0.00 | 0.92 | 0.27 | 0.91|
| full sent rank |  |  | 0 | 3 | 0 | 2 | 6266 | 0 | 0 | 2 | 0 | 0 | 217 | 10 | 0 | 1 | 0|
| full sent KL (waitk->full) |  |  | -2.27 | -2.79 | -1.40 | -2.73 | -3.74 | -1.50 | -2.76 | -2.99 | -2.28 | -3.28 | -4.50 | -0.97 | -1.32 | -2.29 | -1.65|
| full sent KL (full->waitk) |  |  | -3.32 | -3.06 | -1.77 | -2.44 | -4.09 | -2.62 | -3.48 | -4.03 | -2.86 | -2.10 | -4.01 | -3.11 | -1.58 | -2.28 | -1.65|
| dec-waitktgt |  |  | ob | leben | leben | weiter@@ | der | ebene | existiert | in | einigen | dieser | personen | nie@@ | weiß | es | </s>|
| full sent tgt |  |  | ob | es | leben | zumindest | zumindest | ebene | zumindest | bei | einigen | dieser | länder | weiß | weiß | es | </s>|
| ref | ob | es | zumindest | auf | einigen | davon | leben | gibt | , | weiß | keiner | . | </s>|


|  -  | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | -|
| src | the | choice | is | a | difficult | one | : | should | we | search | for | gra@@ | vit@@ | ational | waves | ?|
| waitk tgt |  |  | die | wahl | ist | schwierig | : | sollte | man | nach | einer | get@@ | rei@@ | de@@ | w@@ | ellen | suchen | ? | </s>|
| waitk prob |  |  | 0.47 | 0.38 | 0.66 | 0.81 | 0.86 | 0.48 | 0.75 | 0.41 | 0.16 | 0.10 | 0.98 | 0.93 | 0.40 | 0.74 | 0.91 | 0.89 | 0.90|
| dec-waitk prob |  |  | 0.74 | 0.66 | 0.66 | 0.88 | 0.61 | 0.39 | 0.20 | 0.07 | 0.14 | 0.00 | 0.91 | 0.74 | 0.19 | 0.44 | 0.88 | 0.86 | 0.91|
| dec-waitk rank |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0|
| dec-waitk KL (waitk->dec-waitk) |  |  | -2.26 | -1.90 | -2.51 | -1.38 | -3.18 | -3.87 | -3.70 | -3.50 | -2.73 | -1.96 | -1.44 | -1.80 | -4.02 | -4.30 | -1.62 | -1.93 | -1.60|
| dec-waitk KL (dec-waitk->waitk) |  |  | -3.44 | -3.01 | -2.68 | -1.72 | -1.42 | -2.56 | -1.62 | -3.69 | -4.73 | -4.73 | -0.91 | -1.18 | -2.69 | -2.02 | -1.42 | -1.76 | -1.70|
| full sent prob |  |  | 0.53 | 0.52 | 0.73 | 0.72 | 0.82 | 0.09 | 0.73 | 0.72 | 0.02 | 0.00 | 0.69 | 0.86 | 0.26 | 0.25 | 0.81 | 0.90 | 0.91|
| full sent rank |  |  | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 4 | 616 | 0 | 0 | 1 | 0 | 0 | 0 | 0|
| full sent KL (waitk->full) |  |  | -2.78 | -2.60 | -2.38 | -2.33 | -1.89 | -2.75 | -1.85 | -2.12 | -2.69 | -3.74 | -2.75 | -1.65 | -2.42 | -5.51 | -2.20 | -1.65 | -1.65|
| full sent KL (full->waitk) |  |  | -3.36 | -2.98 | -2.72 | -1.62 | -1.57 | -2.49 | -1.93 | -3.90 | -4.70 | -4.72 | -0.74 | -1.27 | -2.79 | -1.90 | -1.36 | -1.80 | -1.69|
| dec-waitktgt |  |  | die | wahl | ist | schwierig | : | sollte | man | suchen | der | gra@@ | rei@@ | de@@ | w@@ | ellen | suchen | ? | </s>|
| full sent tgt |  |  | die | wahl | ist | schwierig | : | sollten | man | nach | gra@@ | gra@@ | rei@@ | de@@ | welle | ellen | suchen | ? | </s>|
| ref | die | auswahl | fällt | schwer | : | soll | man | nach | gra@@ | vi@@ | ta@@ | tions@@ | w@@ | ellen | suchen | ? | </s>|

PRED AVG SCORE: -0.6272, PRED PPL: 1.8724
GOLD AVG SCORE: 0.0000, GOLD PPL: 1.0000
