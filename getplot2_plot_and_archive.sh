mv result_waitk result_waitk_back
mv result_catchup result_catchup_back
mkdir result_waitk
mkdir result_catchup
python AP_value.py dev bpe
python AP_value.py dev unbpe
python AP_value.py test bpe
python AP_value.py test unbpe
python AL_value.py dev bpe
python AL_value.py dev unbpe
python AL_value.py test bpe
python AL_value.py test unbpe

mv wait*.pdf result_waitk
mv catchup*.pdf result_catchup

cp catchup/BLEU* ../../simul_paper/figs/bleu/catchup_BLEU_`date | awk '{print $2"_"$3}'`.txt
cp waitk/BLEU* ../../simul_paper/figs/bleu/waitk_BLEU_`date | awk '{print $2"_"$3}'`.txt

cp result_waitk/* ../../simul_paper/figs/AL_AP_waitk
cp -r result_catchup/* ../../simul_paper/figs/AL_AP_catchup
