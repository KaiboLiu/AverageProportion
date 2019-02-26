### /Users/kaibo/kaibo@Baidu/MT/mt_result/AverageProportion/en2de

#### trans
`/Users/kaibo/kaibo@Baidu/MT/mt_result/AverageProportion/en2de/trans/BLEU_trans_en2de.txt`
----------BLEU on test----------
wait_1  BLEU = 16.15, 47.2/20.8/11.1/6.3 (BP=1.000, ratio=1.081, hyp_len=47633, ref_len=44077)
wait_2  BLEU = 19.17, 51.3/24.3/13.6/8.0 (BP=1.000, ratio=1.043, hyp_len=45963, ref_len=44077)
wait_3  BLEU = 21.55, 53.8/26.9/15.6/9.6 (BP=1.000, ratio=1.039, hyp_len=45778, ref_len=44077)
wait_4  BLEU = 22.86, 54.7/28.3/16.9/10.5 (BP=1.000, ratio=1.043, hyp_len=45993, ref_len=44077)
wait_5  BLEU = 23.91, 56.4/29.4/17.7/11.2 (BP=1.000, ratio=1.019, hyp_len=44908, ref_len=44077)
wait_6  BLEU = 24.91, 57.4/30.5/18.6/11.9 (BP=1.000, ratio=1.013, hyp_len=44628, ref_len=44077)
wait_7  BLEU = 25.65, 58.7/31.5/19.4/12.4 (BP=0.992, ratio=0.992, hyp_len=43731, ref_len=44077)
wait_8  BLEU = 26.03, 59.0/31.9/19.8/12.8 (BP=0.990, ratio=0.990, hyp_len=43646, ref_len=44077)
wait_9  BLEU = 26.44, 59.0/32.1/20.0/12.9 (BP=1.000, ratio=1.000, hyp_len=44089, ref_len=44077)
wait_10  BLEU = 26.25, 59.2/32.2/20.0/12.9 (BP=0.991, ratio=0.991, hyp_len=43674, ref_len=44077)

--------baseline BLEU on test--------
b=1  BLEU = 26.63, 59.8/33.0/20.8/13.8 (BP=0.971, ratio=0.971, hyp_len=42815, ref_len=44077)
b=11 BLEU = 27.44, 60.1/33.7/21.4/14.2 (BP=0.980, ratio=0.980, hyp_len=43203, ref_len=44077)


AP on test
`/Users/kaibo/kaibo@Baidu/MT/mt_result/AverageProportion/en2de/trans/en2de_trans_test_AP.txt`
0.5784994478260032 0.607910328195512 0.6482199788215002 0.6843616345834324 0.7127288610638083 0.7430176307831231 0.7663689672737969 0.7891156178242913 0.8124497118957906 0.8301380077652728

[0.58, 0.61, 0.65, 0.68, 0.71, 0.74, 0.77, 0.79, 0.81, 0.83]

#### rnn
`/Users/kaibo/kaibo@Baidu/MT/mt_result/AverageProportion/en2de/rnn/BLEU_rnn_en2de.txt`
only wait1..9 available

----------BLEU on test----------
BLEU = 12.03, 42.9/16.4/7.7/3.9 (BP=1.000, ratio=1.063, hyp_len=46837, ref_len=44077)
BLEU = 14.29, 46.1/18.9/9.4/5.1 (BP=1.000, ratio=1.050, hyp_len=46293, ref_len=44077)
BLEU = 16.32, 48.7/21.3/11.1/6.1 (BP=1.000, ratio=1.034, hyp_len=45568, ref_len=44077)
BLEU = 17.06, 49.4/22.1/11.7/6.6 (BP=1.000, ratio=1.030, hyp_len=45409, ref_len=44077)
BLEU = 18.08, 51.1/23.3/12.5/7.2 (BP=1.000, ratio=1.017, hyp_len=44813, ref_len=44077)
BLEU = 18.19, 51.2/23.5/12.6/7.2 (BP=1.000, ratio=1.022, hyp_len=45041, ref_len=44077)
BLEU = 18.63, 51.1/23.9/13.1/7.6 (BP=1.000, ratio=1.025, hyp_len=45198, ref_len=44077)
BLEU = 18.87, 51.5/24.1/13.2/7.7 (BP=1.000, ratio=1.018, hyp_len=44858, ref_len=44077)
BLEU = 18.76, 51.7/24.1/13.1/7.6 (BP=1.000, ratio=1.017, hyp_len=44828, ref_len=44077)

20.82, 19.76

1 1

AP on test
`/Users/kaibo/kaibo@Baidu/MT/mt_result/AverageProportion/en2de/rnn/en2de_rnn_test_AP.txt`
0.5728732249397088 0.6094514086466446 0.6447000129417935 0.6787314392929858 0.7103118225638209 0.7401714109818349 0.7664002153721315 0.7876638428164799 0.8098093198791925
[0.57, 0.61, 0.64, 0.68, 0.71, 0.74, 0.77, 0.79, 0.81]



def dig(s):
   a = map(float, s.split())
   return list( map(lambda x: round(x,2), a) )



policy | AP(trans) | BLEU(trans) | AP(rnn) | BLEU(rnn)
 :-: | :-: | :-: | :-: | :-: 
k=1 | 0.58 | 16.15 | 0.57 | 12.03
k=2 | 0.61 | 19.17 | 0.61 | 14.29
k=3 | 0.65 | 21.55 | 0.64 | 16.32
k=4 | 0.68 | 22.86 | 0.68 | 17.06
k=5 | 0.71 | 23.91 | 0.71 | 18.08
k=6 | 0.74 | 24.91 | 0.74 | 18.19
k=7 | 0.77 | 25.65 | 0.77 | 18.63
k=8 | 0.79 | 26.03 | 0.79 | 18.87
k=9 | 0.81 | 26.44 | 0.81 | 18.76
baseline | 1 | 26.63 | 1 | 19.76
baseline+<br>beam search | 1 | 27.44 | 1 | 20.82









