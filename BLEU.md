## BLEU results  
- [4 ref/ 1 ref of catchup on 09/20/2018 afternoon](#4-ref-catchup-09202018-afternoon)
- [4 ref/ 1 ref of catchup on 09/20/2018 night](#4-ref-catchup-09202018-night)
- [4 ref /1 ref of waitk on 09/20/2018](#4-ref-waitk-09202018)  
- [3 ref of waitk on 09/20/2018](#3-ref-waitk-09202018)  
- [3 ref of catchup on 09/20/2018](#3-ref-catchup-09202018)  
- [decoding in dev/test for waitk and catchup on 09/21/2018](#decoding-09212018)  

#### baseline BLEU
1. dev baseline, located in `/mnt/scratch/mam/proj/opennmt_v726/outfiles`
    ```bash
    perl ../tools/multi-bleu.perl /mnt/data/mam/data/data_zh2en_2M/evaldata/dev_tgt_\*.unbpe < pred.small.90000.b1.unbpe.txt
    4 ref: BLEU = 43.72, 81.0/54.6/36.6/24.6 (BP=0.979, ratio=0.980, hyp_len=22257, ref_len=22720)
    ref 0: BLEU = 25.78, 61.0/32.5/19.4/12.2 (BP=0.985, ratio=0.985, hyp_len=22257, ref_len=22601)
    ref 1: BLEU = 22.22, 61.6/30.7/17.4/10.5 (BP=0.918, ratio=0.921, hyp_len=22257, ref_len=24169)
    ref 2: BLEU = 22.11, 57.7/28.5/16.0/9.4 (BP=0.993, ratio=0.993, hyp_len=22257, ref_len=22421)
    ref 3: BLEU = 19.24, 57.9/27.0/14.0/7.9 (BP=0.943, ratio=0.945, hyp_len=22257, ref_len=23554)
    ref 1 2 3: BLEU = 38.28, 78.1/49.4/31.2/20.0 (BP=0.972, ratio=0.972, hyp_len=22257, ref_len=22890)
    ref 0 2 3: BLEU = 38.94, 76.9/49.2/31.6/20.6 (BP=0.982, ratio=0.983, hyp_len=22257, ref_len=22652)
    ref 0 1 3: BLEU = 39.52, 78.5/50.3/32.7/21.5 (BP=0.968, ratio=0.969, hyp_len=22257, ref_len=22975)
    ref 0 1 2: BLEU = 40.01, 77.6/49.8/32.7/21.8 (BP=0.981, ratio=0.982, hyp_len=22257, ref_len=22675)
    ```
1. test baseline, run in `/mnt/scratch/mam/proj/opennmt_v726`
    ```bash
    python translate.py -model more_tranformermodel/batch2048_h8_ff2048_len256/save_model_step_90000.ppl_5.00_.acc_65.11.pt -src /mnt/data/mam/data/data_zh2en_2M/test_src.bpe -output ~/proj/test_baseline.bpe.txt -verbose -length_penalty avg -beam_size 1 -gpu 0
    ```
    run a script to get the result:
    ```bash
    4 ref: BLEU = 36.29, 73.6/45.7/29.1/19.0 (BP=0.983, ratio=0.983, hyp_len=21864, ref_len=22244)
    ref 0: BLEU = 19.46, 57.6/27.5/15.3/9.1 (BP=0.899, ratio=0.904, hyp_len=21864, ref_len=24188)
    ref 1: BLEU = 19.39, 55.7/26.2/14.4/8.3 (BP=0.948, ratio=0.949, hyp_len=21864, ref_len=23034)
    ref 2: BLEU = 19.03, 52.9/24.3/13.2/7.7 (BP=0.999, ratio=0.999, hyp_len=21864, ref_len=21875)
    ref 3: BLEU = 20.02, 55.9/27.0/14.9/8.8 (BP=0.949, ratio=0.950, hyp_len=21864, ref_len=23010)
    ref 1 2 3:BLEU = 32.71, 70.3/41.4/25.6/16.3 (BP=0.986, ratio=0.986, hyp_len=21864, ref_len=22176)
    ref 0 2 3:BLEU = 33.01, 70.8/41.9/26.0/16.7 (BP=0.979, ratio=0.979, hyp_len=21864, ref_len=22322)
    ref 0 1 3:BLEU = 33.00, 71.4/42.5/26.5/17.0 (BP=0.965, ratio=0.966, hyp_len=21864, ref_len=22642)
    ref 0 1 2:BLEU = 32.70, 70.5/41.5/25.8/16.4 (BP=0.980, ratio=0.980, hyp_len=21864, ref_len=22302)
    ```

#### 4 ref catchup @ 09/20/2018 afternoon
1: 4/1 reference after decoding new catchup models, afternoon 09/20/2018 (/mnt/home/kaibo/proj/fordecoding_catchup)
    ```bash
    #origin
    unbpe finished for wait 2 4 6 10
    4 refences
    wait_2  BLEU = 33.29, 72.6/44.0/26.9/17.1 (BP=0.957, ratio=0.958, hyp_len=22021, ref_len=22995)
    wait_4  BLEU = 35.28, 74.4/45.6/28.1/17.9 (BP=0.975, ratio=0.976, hyp_len=22313, ref_len=22873)
    wait_6  BLEU = 36.62, 75.7/47.4/29.5/18.7 (BP=0.977, ratio=0.977, hyp_len=22284, ref_len=22811)
    wait_10  BLEU = 38.89, 76.5/48.7/31.2/20.3 (BP=0.992, ratio=0.992, hyp_len=22824, ref_len=23003)

    refence 0
    wait_2  BLEU = 19.68, 53.5/25.7/14.3/8.5 (BP=0.974, ratio=0.974, hyp_len=22021, ref_len=22601)
    wait_4  BLEU = 20.23, 54.6/26.1/14.4/8.6 (BP=0.987, ratio=0.987, hyp_len=22313, ref_len=22601)
    wait_6  BLEU = 21.23, 56.0/27.3/15.3/9.2 (BP=0.986, ratio=0.986, hyp_len=22284, ref_len=22601)
    wait_10  BLEU = 22.30, 56.5/28.1/16.0/9.7 (BP=1.000, ratio=1.010, hyp_len=22824, ref_len=22601)
    refence 1
    wait_2  BLEU = 17.61, 54.5/25.0/13.3/7.8 (BP=0.907, ratio=0.911, hyp_len=22021, ref_len=24169)
    wait_4  BLEU = 17.59, 56.0/25.3/13.0/7.2 (BP=0.920, ratio=0.923, hyp_len=22313, ref_len=24169)
    wait_6  BLEU = 17.82, 56.8/25.8/13.3/7.3 (BP=0.919, ratio=0.922, hyp_len=22284, ref_len=24169)
    wait_10  BLEU = 19.15, 57.0/26.5/14.1/8.0 (BP=0.943, ratio=0.944, hyp_len=22824, ref_len=24169)
    refence 2
    wait_2  BLEU = 16.76, 51.1/22.5/11.6/6.3 (BP=0.982, ratio=0.982, hyp_len=22021, ref_len=22421)
    wait_4  BLEU = 18.27, 52.7/23.7/12.6/7.2 (BP=0.995, ratio=0.995, hyp_len=22313, ref_len=22421)
    wait_6  BLEU = 19.39, 53.9/25.1/13.6/7.9 (BP=0.994, ratio=0.994, hyp_len=22284, ref_len=22421)
    wait_10  BLEU = 20.10, 54.3/25.6/14.1/8.3 (BP=1.000, ratio=1.018, hyp_len=22824, ref_len=22421)
    refence 3
    wait_2  BLEU = 14.93, 51.9/21.8/10.3/5.7 (BP=0.933, ratio=0.935, hyp_len=22021, ref_len=23554)
    wait_4  BLEU = 15.57, 52.9/22.3/10.8/5.8 (BP=0.946, ratio=0.947, hyp_len=22313, ref_len=23554)
    wait_6  BLEU = 16.24, 54.0/23.3/11.4/6.1 (BP=0.945, ratio=0.946, hyp_len=22284, ref_len=23554)
    wait_10  BLEU = 17.39, 54.6/24.0/12.1/6.6 (BP=0.969, ratio=0.969, hyp_len=22824, ref_len=23554)

    # catchup_short @31,28,28,37,33,33,27,35,32,39k iter
    4 refences
    wait_1  BLEU = 24.25, 64.8/35.3/20.0/12.0 (BP=0.891, ratio=0.896, hyp_len=20481, ref_len=22846)
    wait_2  BLEU = 27.23, 68.1/38.8/22.7/13.6 (BP=0.905, ratio=0.909, hyp_len=20853, ref_len=22929)
    wait_3  BLEU = 29.17, 69.0/39.4/23.3/14.1 (BP=0.950, ratio=0.951, hyp_len=21953, ref_len=23080)
    wait_4  BLEU = 31.32, 71.2/42.0/25.5/16.1 (BP=0.940, ratio=0.942, hyp_len=21607, ref_len=22939)
    wait_5  BLEU = 32.92, 72.5/43.8/26.5/16.5 (BP=0.959, ratio=0.960, hyp_len=22073, ref_len=23000)
    wait_6  BLEU = 34.62, 74.6/45.8/28.4/18.0 (BP=0.953, ratio=0.954, hyp_len=21709, ref_len=22759)
    wait_7  BLEU = 34.05, 74.5/45.4/27.8/17.4 (BP=0.952, ratio=0.953, hyp_len=21687, ref_len=22749)
    wait_8  BLEU = 36.89, 76.7/48.3/30.4/19.6 (BP=0.957, ratio=0.958, hyp_len=21724, ref_len=22672)
    wait_9  BLEU = 36.53, 75.6/46.9/29.1/18.5 (BP=0.984, ratio=0.984, hyp_len=22643, ref_len=23013)
    wait_10  BLEU = 38.51, 76.8/48.9/31.2/20.0 (BP=0.984, ratio=0.984, hyp_len=22526, ref_len=22896)

    refence 0
    wait_1  BLEU = 14.18, 47.5/20.6/10.6/5.9 (BP=0.902, ratio=0.906, hyp_len=20481, ref_len=22601)
    wait_2  BLEU = 15.93, 50.0/22.3/11.9/6.8 (BP=0.920, ratio=0.923, hyp_len=20853, ref_len=22601)
    wait_3  BLEU = 17.05, 50.8/22.7/12.0/6.9 (BP=0.971, ratio=0.971, hyp_len=21953, ref_len=22601)
    wait_4  BLEU = 17.90, 52.3/24.0/12.9/7.7 (BP=0.955, ratio=0.956, hyp_len=21607, ref_len=22601)
    wait_5  BLEU = 18.92, 53.2/25.1/13.5/7.9 (BP=0.976, ratio=0.977, hyp_len=22073, ref_len=22601)
    wait_6  BLEU = 19.63, 55.2/26.2/14.3/8.5 (BP=0.960, ratio=0.961, hyp_len=21709, ref_len=22601)
    wait_7  BLEU = 19.65, 54.9/26.3/14.4/8.5 (BP=0.959, ratio=0.960, hyp_len=21687, ref_len=22601)
    wait_8  BLEU = 21.34, 57.0/28.2/15.8/9.6 (BP=0.960, ratio=0.961, hyp_len=21724, ref_len=22601)
    wait_9  BLEU = 20.96, 55.6/26.9/14.8/8.7 (BP=1.000, ratio=1.002, hyp_len=22643, ref_len=22601)
    wait_10  BLEU = 21.80, 56.6/27.9/15.6/9.3 (BP=0.997, ratio=0.997, hyp_len=22526, ref_len=22601)
    refence 1
    wait_1  BLEU = 13.05, 48.6/20.5/10.2/5.8 (BP=0.835, ratio=0.847, hyp_len=20481, ref_len=24169)
    wait_2  BLEU = 14.59, 51.5/22.6/11.5/6.4 (BP=0.853, ratio=0.863, hyp_len=20853, ref_len=24169)
    wait_3  BLEU = 14.88, 51.6/22.0/11.0/5.9 (BP=0.904, ratio=0.908, hyp_len=21953, ref_len=24169)
    wait_4  BLEU = 15.50, 53.3/23.3/11.7/6.4 (BP=0.888, ratio=0.894, hyp_len=21607, ref_len=24169)
    wait_5  BLEU = 16.72, 54.5/24.6/12.5/6.8 (BP=0.909, ratio=0.913, hyp_len=22073, ref_len=24169)
    wait_6  BLEU = 16.91, 56.0/25.1/12.9/7.1 (BP=0.893, ratio=0.898, hyp_len=21709, ref_len=24169)
    wait_7  BLEU = 16.71, 55.6/24.9/12.9/6.9 (BP=0.892, ratio=0.897, hyp_len=21687, ref_len=24169)
    wait_8  BLEU = 18.37, 57.8/27.1/14.3/8.0 (BP=0.894, ratio=0.899, hyp_len=21724, ref_len=24169)
    wait_9  BLEU = 18.00, 56.4/25.6/13.1/7.3 (BP=0.935, ratio=0.937, hyp_len=22643, ref_len=24169)
    wait_10  BLEU = 19.15, 57.7/27.2/14.3/8.0 (BP=0.930, ratio=0.932, hyp_len=22526, ref_len=24169)
    refence 2
    wait_1  BLEU = 12.50, 45.9/18.3/9.0/4.7 (BP=0.910, ratio=0.913, hyp_len=20481, ref_len=22421)
    wait_2  BLEU = 13.87, 48.1/19.9/9.9/5.3 (BP=0.928, ratio=0.930, hyp_len=20853, ref_len=22421)
    wait_3  BLEU = 15.48, 48.8/20.8/10.6/5.8 (BP=0.979, ratio=0.979, hyp_len=21953, ref_len=22421)
    wait_4  BLEU = 16.62, 50.5/22.3/11.8/6.7 (BP=0.963, ratio=0.964, hyp_len=21607, ref_len=22421)
    wait_5  BLEU = 16.54, 51.3/22.3/11.3/6.1 (BP=0.984, ratio=0.984, hyp_len=22073, ref_len=22421)
    wait_6  BLEU = 18.01, 53.1/24.0/12.8/7.3 (BP=0.968, ratio=0.968, hyp_len=21709, ref_len=22421)
    wait_7  BLEU = 17.58, 52.7/23.5/12.4/7.1 (BP=0.967, ratio=0.967, hyp_len=21687, ref_len=22421)
    wait_8  BLEU = 19.20, 54.4/25.3/13.8/8.1 (BP=0.968, ratio=0.969, hyp_len=21724, ref_len=22421)
    wait_9  BLEU = 18.90, 53.6/24.6/13.1/7.4 (BP=1.000, ratio=1.010, hyp_len=22643, ref_len=22421)
    wait_10  BLEU = 20.01, 54.5/25.6/14.1/8.2 (BP=1.000, ratio=1.005, hyp_len=22526, ref_len=22421)
    refence 3
    wait_1  BLEU = 10.64, 46.7/17.4/7.6/3.8 (BP=0.861, ratio=0.870, hyp_len=20481, ref_len=23554)
    wait_2  BLEU = 12.14, 48.7/19.2/8.7/4.5 (BP=0.879, ratio=0.885, hyp_len=20853, ref_len=23554)
    wait_3  BLEU = 13.12, 49.2/19.4/8.9/4.7 (BP=0.930, ratio=0.932, hyp_len=21953, ref_len=23554)
    wait_4  BLEU = 13.93, 51.0/20.7/9.8/5.2 (BP=0.914, ratio=0.917, hyp_len=21607, ref_len=23554)
    wait_5  BLEU = 15.32, 52.1/22.1/10.7/5.8 (BP=0.935, ratio=0.937, hyp_len=22073, ref_len=23554)
    wait_6  BLEU = 15.40, 53.3/22.6/11.0/6.0 (BP=0.919, ratio=0.922, hyp_len=21709, ref_len=23554)
    wait_7  BLEU = 15.22, 53.6/22.4/10.9/5.8 (BP=0.918, ratio=0.921, hyp_len=21687, ref_len=23554)
    wait_8  BLEU = 15.87, 54.6/23.3/11.3/6.2 (BP=0.919, ratio=0.922, hyp_len=21724, ref_len=23554)
    wait_9  BLEU = 16.72, 54.2/23.3/11.5/6.3 (BP=0.961, ratio=0.961, hyp_len=22643, ref_len=23554)
    wait_10  BLEU = 17.16, 54.5/23.9/12.1/6.6 (BP=0.955, ratio=0.956, hyp_len=22526, ref_len=23554)

    # catchup_long @31,28,28,37,33,33,27,35,32,39k iter
    4 refences
    wait_1  BLEU = 24.22, 59.7/32.0/17.6/10.2 (BP=1.000, ratio=1.135, hyp_len=27244, ref_len=23995)
    wait_2  BLEU = 27.14, 62.7/35.4/20.3/12.1 (BP=1.000, ratio=1.118, hyp_len=26748, ref_len=23933)
    wait_3  BLEU = 27.95, 64.0/36.2/21.0/12.6 (BP=1.000, ratio=1.111, hyp_len=26513, ref_len=23865)
    wait_4  BLEU = 30.00, 65.5/38.1/22.8/14.2 (BP=1.000, ratio=1.098, hyp_len=26063, ref_len=23743)
    wait_5  BLEU = 31.31, 67.3/40.1/24.0/14.8 (BP=1.000, ratio=1.084, hyp_len=25564, ref_len=23593)
    wait_6  BLEU = 32.87, 69.1/41.8/25.5/15.9 (BP=1.000, ratio=1.072, hyp_len=25025, ref_len=23345)
    wait_7  BLEU = 32.34, 68.8/41.3/25.0/15.4 (BP=1.000, ratio=1.075, hyp_len=25132, ref_len=23388)
    wait_8  BLEU = 35.24, 71.2/44.3/27.6/17.7 (BP=1.000, ratio=1.064, hyp_len=24614, ref_len=23133)
    wait_9  BLEU = 35.09, 70.9/44.1/27.5/17.6 (BP=1.000, ratio=1.075, hyp_len=25160, ref_len=23414)
    wait_10  BLEU = 36.35, 72.0/45.6/28.9/18.4 (BP=1.000, ratio=1.070, hyp_len=24926, ref_len=23306)

    refence 0
    wait_1  BLEU = 13.89, 42.9/18.4/9.3/5.1 (BP=1.000, ratio=1.205, hyp_len=27244, ref_len=22601)
    wait_2  BLEU = 15.49, 45.2/20.1/10.6/6.0 (BP=1.000, ratio=1.183, hyp_len=26748, ref_len=22601)
    wait_3  BLEU = 15.86, 46.4/20.6/10.8/6.1 (BP=1.000, ratio=1.173, hyp_len=26513, ref_len=22601)
    wait_4  BLEU = 16.82, 47.5/21.7/11.5/6.7 (BP=1.000, ratio=1.153, hyp_len=26063, ref_len=22601)
    wait_5  BLEU = 17.56, 48.8/22.8/12.1/7.0 (BP=1.000, ratio=1.131, hyp_len=25564, ref_len=22601)
    wait_6  BLEU = 18.46, 50.5/23.8/12.8/7.5 (BP=1.000, ratio=1.107, hyp_len=25025, ref_len=22601)
    wait_7  BLEU = 18.50, 50.1/23.8/12.9/7.6 (BP=1.000, ratio=1.112, hyp_len=25132, ref_len=22601)
    wait_8  BLEU = 20.30, 52.3/25.8/14.5/8.7 (BP=1.000, ratio=1.089, hyp_len=24614, ref_len=22601)
    wait_9  BLEU = 19.38, 51.5/25.0/13.6/8.1 (BP=1.000, ratio=1.113, hyp_len=25160, ref_len=22601)
    wait_10  BLEU = 20.24, 52.5/25.8/14.4/8.6 (BP=1.000, ratio=1.103, hyp_len=24926, ref_len=22601)
    refence 1
    wait_1  BLEU = 13.61, 44.1/18.3/8.8/4.8 (BP=1.000, ratio=1.127, hyp_len=27244, ref_len=24169)
    wait_2  BLEU = 15.31, 46.8/20.4/10.2/5.6 (BP=1.000, ratio=1.107, hyp_len=26748, ref_len=24169)
    wait_3  BLEU = 15.01, 47.4/20.2/10.0/5.3 (BP=1.000, ratio=1.097, hyp_len=26513, ref_len=24169)
    wait_4  BLEU = 15.73, 48.4/21.0/10.5/5.7 (BP=1.000, ratio=1.078, hyp_len=26063, ref_len=24169)
    wait_5  BLEU = 16.76, 50.2/22.5/11.4/6.2 (BP=1.000, ratio=1.058, hyp_len=25564, ref_len=24169)
    wait_6  BLEU = 17.16, 51.5/22.9/11.7/6.3 (BP=1.000, ratio=1.035, hyp_len=25025, ref_len=24169)
    wait_7  BLEU = 16.87, 50.9/22.6/11.5/6.1 (BP=1.000, ratio=1.040, hyp_len=25132, ref_len=24169)
    wait_8  BLEU = 18.80, 53.3/24.8/13.0/7.3 (BP=1.000, ratio=1.018, hyp_len=24614, ref_len=24169)
    wait_9  BLEU = 18.65, 52.9/24.5/12.9/7.2 (BP=1.000, ratio=1.041, hyp_len=25160, ref_len=24169)
    wait_10  BLEU = 19.18, 53.8/25.3/13.3/7.5 (BP=1.000, ratio=1.031, hyp_len=24926, ref_len=24169)
    refence 2
    wait_1  BLEU = 12.17, 41.5/16.4/7.9/4.1 (BP=1.000, ratio=1.215, hyp_len=27244, ref_len=22421)
    wait_2  BLEU = 13.48, 43.5/18.1/8.9/4.7 (BP=1.000, ratio=1.193, hyp_len=26748, ref_len=22421)
    wait_3  BLEU = 14.19, 44.6/18.8/9.4/5.1 (BP=1.000, ratio=1.183, hyp_len=26513, ref_len=22421)
    wait_4  BLEU = 15.42, 45.8/20.1/10.5/5.9 (BP=1.000, ratio=1.162, hyp_len=26063, ref_len=22421)
    wait_5  BLEU = 15.32, 47.1/20.4/10.3/5.6 (BP=1.000, ratio=1.140, hyp_len=25564, ref_len=22421)
    wait_6  BLEU = 16.70, 48.5/21.7/11.4/6.5 (BP=1.000, ratio=1.116, hyp_len=25025, ref_len=22421)
    wait_7  BLEU = 16.31, 48.0/21.2/11.1/6.3 (BP=1.000, ratio=1.121, hyp_len=25132, ref_len=22421)
    wait_8  BLEU = 18.02, 49.9/23.1/12.5/7.3 (BP=1.000, ratio=1.098, hyp_len=24614, ref_len=22421)
    wait_9  BLEU = 17.73, 49.5/23.0/12.3/7.0 (BP=1.000, ratio=1.122, hyp_len=25160, ref_len=22421)
    wait_10  BLEU = 18.49, 50.7/23.7/13.0/7.5 (BP=1.000, ratio=1.112, hyp_len=24926, ref_len=22421)
    refence 3
    wait_1  BLEU = 10.89, 42.2/15.6/6.6/3.2 (BP=1.000, ratio=1.157, hyp_len=27244, ref_len=23554)
    wait_2  BLEU = 12.61, 44.2/17.6/8.0/4.1 (BP=1.000, ratio=1.136, hyp_len=26748, ref_len=23554)
    wait_3  BLEU = 12.70, 44.9/17.6/8.0/4.1 (BP=1.000, ratio=1.126, hyp_len=26513, ref_len=23554)
    wait_4  BLEU = 13.70, 46.3/18.6/8.7/4.7 (BP=1.000, ratio=1.107, hyp_len=26063, ref_len=23554)
    wait_5  BLEU = 14.90, 47.8/20.2/9.7/5.3 (BP=1.000, ratio=1.085, hyp_len=25564, ref_len=23554)
    wait_6  BLEU = 15.09, 48.8/20.6/9.8/5.3 (BP=1.000, ratio=1.062, hyp_len=25025, ref_len=23554)
    wait_7  BLEU = 14.97, 49.0/20.3/9.8/5.2 (BP=1.000, ratio=1.067, hyp_len=25132, ref_len=23554)
    wait_8  BLEU = 15.74, 50.2/21.3/10.3/5.6 (BP=1.000, ratio=1.045, hyp_len=24614, ref_len=23554)
    wait_9  BLEU = 15.81, 50.0/21.4/10.4/5.6 (BP=1.000, ratio=1.068, hyp_len=25160, ref_len=23554)
    wait_10  BLEU = 16.64, 50.7/22.2/11.1/6.1 (BP=1.000, ratio=1.058, hyp_len=24926, ref_len=23554)
    ```
[***Back to CONTENTS***](#bleu-results)  

---  

#### 4 ref catchup @ 09/20/2018 night
2: 4/1 reference after decoding new catchup models, night 09/20/2018 (/mnt/home/kaibo/proj/fordecoding_catchup)
    ```bash
    # catchup_short @32,29,29,39,35,34,28,37,33,40k iter
    4 refences
    wait_1  BLEU = 24.48, 67.5/37.4/21.8/13.0 (BP=0.842, ratio=0.853, hyp_len=19266, ref_len=22585)
    wait_2  BLEU = 24.81, 68.3/38.4/22.3/13.4 (BP=0.834, ratio=0.846, hyp_len=19312, ref_len=22820)
    wait_3  BLEU = 28.88, 68.8/39.0/22.8/13.8 (BP=0.954, ratio=0.955, hyp_len=21954, ref_len=22995)
    wait_4  BLEU = 31.81, 71.8/42.6/25.9/16.0 (BP=0.947, ratio=0.948, hyp_len=21871, ref_len=23060)
    wait_5  BLEU = 33.33, 73.3/44.2/27.0/16.9 (BP=0.955, ratio=0.956, hyp_len=21770, ref_len=22768)
    wait_6  BLEU = 34.42, 74.2/45.3/28.0/17.8 (BP=0.957, ratio=0.958, hyp_len=21874, ref_len=22844)
    wait_7  BLEU = 34.93, 74.8/45.9/28.4/17.8 (BP=0.962, ratio=0.963, hyp_len=22041, ref_len=22890)
    wait_8  BLEU = 37.00, 76.1/47.7/30.0/19.1 (BP=0.974, ratio=0.975, hyp_len=22275, ref_len=22854)
    wait_9  BLEU = 35.72, 75.8/47.0/29.5/18.9 (BP=0.951, ratio=0.952, hyp_len=21625, ref_len=22707)
    wait_10  BLEU = 38.33, 76.3/48.4/30.8/19.8 (BP=0.989, ratio=0.989, hyp_len=22774, ref_len=23019)

    refence 0
    wait_1  BLEU = 14.25, 49.6/21.6/11.6/6.6 (BP=0.841, ratio=0.852, hyp_len=19266, ref_len=22601)
    wait_2  BLEU = 14.56, 50.2/22.5/11.9/6.6 (BP=0.843, ratio=0.854, hyp_len=19312, ref_len=22601)
    wait_3  BLEU = 16.49, 50.2/22.0/11.5/6.5 (BP=0.971, ratio=0.971, hyp_len=21954, ref_len=22601)
    wait_4  BLEU = 17.84, 52.5/23.9/12.7/7.3 (BP=0.967, ratio=0.968, hyp_len=21871, ref_len=22601)
    wait_5  BLEU = 19.19, 54.0/25.6/13.9/8.2 (BP=0.963, ratio=0.963, hyp_len=21770, ref_len=22601)
    wait_6  BLEU = 19.84, 55.0/26.2/14.4/8.5 (BP=0.967, ratio=0.968, hyp_len=21874, ref_len=22601)
    wait_7  BLEU = 19.95, 54.9/26.3/14.4/8.4 (BP=0.975, ratio=0.975, hyp_len=22041, ref_len=22601)
    wait_8  BLEU = 20.89, 56.1/27.2/15.0/8.8 (BP=0.985, ratio=0.986, hyp_len=22275, ref_len=22601)
    wait_9  BLEU = 20.31, 56.1/27.2/15.0/8.9 (BP=0.956, ratio=0.957, hyp_len=21625, ref_len=22601)
    wait_10  BLEU = 21.99, 56.4/27.9/15.7/9.5 (BP=1.000, ratio=1.008, hyp_len=22774, ref_len=22601)
    refence 1
    wait_1  BLEU = 12.57, 50.9/21.3/10.7/6.0 (BP=0.775, ratio=0.797, hyp_len=19266, ref_len=24169)
    wait_2  BLEU = 13.07, 51.4/22.0/11.3/6.2 (BP=0.778, ratio=0.799, hyp_len=19312, ref_len=24169)
    wait_3  BLEU = 14.74, 51.6/21.8/10.8/5.8 (BP=0.904, ratio=0.908, hyp_len=21954, ref_len=24169)
    wait_4  BLEU = 16.07, 53.5/23.6/12.1/6.6 (BP=0.900, ratio=0.905, hyp_len=21871, ref_len=24169)
    wait_5  BLEU = 16.64, 55.1/24.6/12.6/6.9 (BP=0.896, ratio=0.901, hyp_len=21770, ref_len=24169)
    wait_6  BLEU = 17.36, 55.6/25.4/13.2/7.4 (BP=0.900, ratio=0.905, hyp_len=21874, ref_len=24169)
    wait_7  BLEU = 17.10, 55.9/25.2/12.9/6.9 (BP=0.908, ratio=0.912, hyp_len=22041, ref_len=24169)
    wait_8  BLEU = 18.48, 57.2/26.5/13.9/7.7 (BP=0.918, ratio=0.922, hyp_len=22275, ref_len=24169)
    wait_9  BLEU = 17.48, 57.0/25.9/13.5/7.5 (BP=0.889, ratio=0.895, hyp_len=21625, ref_len=24169)
    wait_10  BLEU = 18.49, 56.5/25.9/13.5/7.6 (BP=0.941, ratio=0.942, hyp_len=22774, ref_len=24169)
    refence 2
    wait_1  BLEU = 12.12, 47.7/19.0/9.4/4.9 (BP=0.849, ratio=0.859, hyp_len=19266, ref_len=22421)
    wait_2  BLEU = 11.91, 48.2/18.9/9.1/4.6 (BP=0.851, ratio=0.861, hyp_len=19312, ref_len=22421)
    wait_3  BLEU = 14.84, 48.3/20.0/10.0/5.4 (BP=0.979, ratio=0.979, hyp_len=21954, ref_len=22421)
    wait_4  BLEU = 16.78, 51.0/22.4/11.8/6.5 (BP=0.975, ratio=0.975, hyp_len=21871, ref_len=22421)
    wait_5  BLEU = 17.42, 52.1/23.3/12.4/6.9 (BP=0.971, ratio=0.971, hyp_len=21770, ref_len=22421)
    wait_6  BLEU = 17.98, 52.8/23.6/12.7/7.3 (BP=0.975, ratio=0.976, hyp_len=21874, ref_len=22421)
    wait_7  BLEU = 18.46, 53.0/24.3/13.0/7.5 (BP=0.983, ratio=0.983, hyp_len=22041, ref_len=22421)
    wait_8  BLEU = 19.38, 54.2/25.1/13.6/7.9 (BP=0.993, ratio=0.993, hyp_len=22275, ref_len=22421)
    wait_9  BLEU = 18.62, 54.0/24.8/13.4/7.8 (BP=0.964, ratio=0.964, hyp_len=21625, ref_len=22421)
    wait_10  BLEU = 19.95, 54.0/25.5/14.1/8.2 (BP=1.000, ratio=1.016, hyp_len=22774, ref_len=22421)
    refence 3
    wait_1  BLEU = 10.87, 48.8/18.6/8.5/4.4 (BP=0.800, ratio=0.818, hyp_len=19266, ref_len=23554)
    wait_2  BLEU = 10.79, 48.8/18.9/8.5/4.2 (BP=0.803, ratio=0.820, hyp_len=19312, ref_len=23554)
    wait_3  BLEU = 12.83, 49.0/19.0/8.6/4.5 (BP=0.930, ratio=0.932, hyp_len=21954, ref_len=23554)
    wait_4  BLEU = 14.36, 51.3/21.0/10.1/5.3 (BP=0.926, ratio=0.929, hyp_len=21871, ref_len=23554)
    wait_5  BLEU = 14.72, 52.7/21.8/10.3/5.5 (BP=0.921, ratio=0.924, hyp_len=21770, ref_len=23554)
    wait_6  BLEU = 15.32, 53.0/22.3/10.8/5.8 (BP=0.926, ratio=0.929, hyp_len=21874, ref_len=23554)
    wait_7  BLEU = 15.82, 53.4/22.7/11.3/6.0 (BP=0.934, ratio=0.936, hyp_len=22041, ref_len=23554)
    wait_8  BLEU = 16.58, 54.6/23.7/11.7/6.3 (BP=0.944, ratio=0.946, hyp_len=22275, ref_len=23554)
    wait_9  BLEU = 15.65, 54.4/23.1/11.2/6.1 (BP=0.915, ratio=0.918, hyp_len=21625, ref_len=23554)
    wait_10  BLEU = 17.52, 54.5/24.0/12.1/6.8 (BP=0.966, ratio=0.967, hyp_len=22774, ref_len=23554)    
    ```
[***Back to CONTENTS***](#bleu-results)  

---  

#### 4 ref waitk @ 09/20/2018
3: 4/1 reference after decoding new waitk models, night 09/20/2018, decoding time \:~4min (/mnt/home/kaibo/proj/fordecoding)
    ```bash
    # wait_short @34,34,34,37,38,41,41,39,37,41k iter
    4 refences
    wait_1  BLEU = 32.30, 71.3/42.4/25.7/16.0 (BP=0.968, ratio=0.969, hyp_len=22368, ref_len=23092)
    wait_2  BLEU = 33.10, 73.3/44.0/26.7/16.7 (BP=0.956, ratio=0.957, hyp_len=21804, ref_len=22787)
    wait_3  BLEU = 33.49, 73.2/44.1/27.0/17.0 (BP=0.960, ratio=0.961, hyp_len=21926, ref_len=22823)
    wait_4  BLEU = 36.18, 73.7/45.9/28.4/18.1 (BP=0.997, ratio=0.997, hyp_len=23012, ref_len=23087)
    wait_5  BLEU = 36.66, 75.6/47.0/29.1/18.3 (BP=0.990, ratio=0.990, hyp_len=22775, ref_len=23015)
    wait_6  BLEU = 37.04, 76.3/48.0/30.0/19.2 (BP=0.971, ratio=0.972, hyp_len=22072, ref_len=22714)
    wait_7  BLEU = 38.17, 77.2/48.6/30.8/20.0 (BP=0.979, ratio=0.979, hyp_len=22235, ref_len=22701)
    wait_8  BLEU = 38.81, 78.0/49.7/31.6/20.2 (BP=0.979, ratio=0.979, hyp_len=22242, ref_len=22718)
    wait_9  BLEU = 39.15, 78.0/50.0/32.2/20.8 (BP=0.974, ratio=0.974, hyp_len=22166, ref_len=22754)
    wait_10  BLEU = 40.00, 77.9/50.1/32.4/21.3 (BP=0.987, ratio=0.987, hyp_len=22569, ref_len=22870)

    refence 0
    wait_1  BLEU = 18.83, 52.3/24.4/13.2/7.7 (BP=0.990, ratio=0.990, hyp_len=22368, ref_len=22601)
    wait_2  BLEU = 19.84, 54.4/26.1/14.6/8.6 (BP=0.964, ratio=0.965, hyp_len=21804, ref_len=22601)
    wait_3  BLEU = 19.28, 54.0/25.6/13.9/8.1 (BP=0.970, ratio=0.970, hyp_len=21926, ref_len=22601)
    wait_4  BLEU = 20.54, 54.1/26.3/14.5/8.6 (BP=1.000, ratio=1.018, hyp_len=23012, ref_len=22601)
    wait_5  BLEU = 20.84, 55.2/26.7/14.7/8.7 (BP=1.000, ratio=1.008, hyp_len=22775, ref_len=22601)
    wait_6  BLEU = 21.68, 56.8/28.1/15.9/9.6 (BP=0.976, ratio=0.977, hyp_len=22072, ref_len=22601)
    wait_7  BLEU = 21.88, 57.1/28.2/15.8/9.6 (BP=0.984, ratio=0.984, hyp_len=22235, ref_len=22601)
    wait_8  BLEU = 22.21, 57.6/28.7/16.1/9.7 (BP=0.984, ratio=0.984, hyp_len=22242, ref_len=22601)
    wait_9  BLEU = 22.15, 57.8/28.7/16.2/9.7 (BP=0.981, ratio=0.981, hyp_len=22166, ref_len=22601)
    wait_10  BLEU = 23.09, 57.6/28.9/16.7/10.3 (BP=0.999, ratio=0.999, hyp_len=22569, ref_len=22601)
    refence 1
    wait_1  BLEU = 17.19, 53.8/24.1/12.6/7.4 (BP=0.923, ratio=0.925, hyp_len=22368, ref_len=24169)
    wait_2  BLEU = 16.90, 55.1/24.7/12.8/7.3 (BP=0.897, ratio=0.902, hyp_len=21804, ref_len=24169)
    wait_3  BLEU = 16.83, 54.6/24.4/12.6/7.2 (BP=0.903, ratio=0.907, hyp_len=21926, ref_len=24169)
    wait_4  BLEU = 18.19, 55.2/25.3/13.2/7.3 (BP=0.951, ratio=0.952, hyp_len=23012, ref_len=24169)
    wait_5  BLEU = 18.14, 56.5/25.8/13.2/7.2 (BP=0.941, ratio=0.942, hyp_len=22775, ref_len=24169)
    wait_6  BLEU = 17.92, 57.5/26.4/13.5/7.3 (BP=0.909, ratio=0.913, hyp_len=22072, ref_len=24169)
    wait_7  BLEU = 18.59, 57.9/26.6/14.0/7.9 (BP=0.917, ratio=0.920, hyp_len=22235, ref_len=24169)
    wait_8  BLEU = 19.40, 58.3/27.7/14.8/8.3 (BP=0.917, ratio=0.920, hyp_len=22242, ref_len=24169)
    wait_9  BLEU = 19.41, 58.7/27.6/14.9/8.5 (BP=0.914, ratio=0.917, hyp_len=22166, ref_len=24169)
    wait_10  BLEU = 20.05, 58.7/28.0/15.1/8.6 (BP=0.932, ratio=0.934, hyp_len=22569, ref_len=24169)
    refence 2
    wait_1  BLEU = 16.11, 50.1/21.5/10.8/5.8 (BP=0.998, ratio=0.998, hyp_len=22368, ref_len=22421)
    wait_2  BLEU = 16.61, 51.5/22.6/11.6/6.3 (BP=0.972, ratio=0.972, hyp_len=21804, ref_len=22421)
    wait_3  BLEU = 17.12, 51.8/22.7/11.9/6.7 (BP=0.978, ratio=0.978, hyp_len=21926, ref_len=22421)
    wait_4  BLEU = 18.48, 52.2/23.9/12.8/7.3 (BP=1.000, ratio=1.026, hyp_len=23012, ref_len=22421)
    wait_5  BLEU = 18.87, 53.4/24.5/13.1/7.4 (BP=1.000, ratio=1.016, hyp_len=22775, ref_len=22421)
    wait_6  BLEU = 18.89, 54.2/25.0/13.3/7.5 (BP=0.984, ratio=0.984, hyp_len=22072, ref_len=22421)
    wait_7  BLEU = 19.70, 54.8/25.6/13.8/8.0 (BP=0.992, ratio=0.992, hyp_len=22235, ref_len=22421)
    wait_8  BLEU = 20.04, 55.4/25.9/14.2/8.2 (BP=0.992, ratio=0.992, hyp_len=22242, ref_len=22421)
    wait_9  BLEU = 20.12, 55.6/26.2/14.3/8.2 (BP=0.989, ratio=0.989, hyp_len=22166, ref_len=22421)
    wait_10  BLEU = 20.35, 55.1/26.0/14.3/8.3 (BP=1.000, ratio=1.007, hyp_len=22569, ref_len=22421)
    refence 3
    wait_1  BLEU = 14.73, 51.4/21.2/10.1/5.3 (BP=0.948, ratio=0.950, hyp_len=22368, ref_len=23554)
    wait_2  BLEU = 14.76, 52.3/21.8/10.4/5.5 (BP=0.923, ratio=0.926, hyp_len=21804, ref_len=23554)
    wait_3  BLEU = 14.60, 52.0/21.4/10.1/5.4 (BP=0.928, ratio=0.931, hyp_len=21926, ref_len=23554)
    wait_4  BLEU = 16.28, 52.5/22.5/10.9/6.0 (BP=0.977, ratio=0.977, hyp_len=23012, ref_len=23554)
    wait_5  BLEU = 16.69, 54.0/23.4/11.4/6.1 (BP=0.966, ratio=0.967, hyp_len=22775, ref_len=23554)
    wait_6  BLEU = 16.34, 54.7/23.5/11.5/6.3 (BP=0.935, ratio=0.937, hyp_len=22072, ref_len=23554)
    wait_7  BLEU = 16.80, 54.9/23.9/11.9/6.5 (BP=0.942, ratio=0.944, hyp_len=22235, ref_len=23554)
    wait_8  BLEU = 17.07, 55.3/24.2/12.2/6.6 (BP=0.943, ratio=0.944, hyp_len=22242, ref_len=23554)
    wait_9  BLEU = 17.47, 55.5/24.7/12.5/7.0 (BP=0.939, ratio=0.941, hyp_len=22166, ref_len=23554)
    wait_10  BLEU = 18.01, 55.6/24.7/12.6/7.2 (BP=0.957, ratio=0.958, hyp_len=22569, ref_len=23554)
    ```
[***Back to CONTENTS***](#bleu-results)  

---  

#### 3 ref waitk @ 09/20/2018
4: 3 reference after decoding new waitk models, night 09/20/2018. (/mnt/home/kaibo/proj/fordecoding)
    ```bash
    22:31:23 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding
    $ bleu3 1 2 3
    tgt 0   BLEU = 45.32, 82.3/55.6/37.6/25.5 (BP=0.990, ratio=0.990, hyp_len=22601, ref_len=22823)
    wait 1  BLEU = 28.61, 68.8/38.6/22.3/13.3 (BP=0.961, ratio=0.961, hyp_len=22368, ref_len=23265)
    wait 2  BLEU = 29.04, 70.5/39.7/22.8/13.6 (BP=0.951, ratio=0.952, hyp_len=21804, ref_len=22893)
    wait 3  BLEU = 29.24, 70.3/39.6/22.8/13.7 (BP=0.957, ratio=0.958, hyp_len=21926, ref_len=22899)
    wait 4  BLEU = 31.87, 70.9/41.5/24.3/14.8 (BP=0.994, ratio=0.994, hyp_len=23012, ref_len=23140)
    wait 5  BLEU = 32.33, 72.8/42.6/25.1/14.9 (BP=0.985, ratio=0.985, hyp_len=22775, ref_len=23118)
    wait 6  BLEU = 32.03, 73.4/43.2/25.2/15.2 (BP=0.965, ratio=0.966, hyp_len=22072, ref_len=22855)
    wait 7  BLEU = 33.25, 74.2/43.9/26.2/16.1 (BP=0.972, ratio=0.972, hyp_len=22235, ref_len=22864)
    wait 8  BLEU = 34.07, 75.0/45.0/27.1/16.5 (BP=0.972, ratio=0.972, hyp_len=22242, ref_len=22873)
    wait 9  BLEU = 34.36, 75.1/45.3/27.6/17.0 (BP=0.968, ratio=0.968, hyp_len=22166, ref_len=22894)
    wait 10  BLEU = 35.05, 75.0/45.4/27.8/17.4 (BP=0.979, ratio=0.979, hyp_len=22569, ref_len=23049)

    22:31:42 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding
    $ bleu3 0 2 3
    tgt 1   BLEU = 37.85, 75.5/47.2/30.0/19.2 (BP=1.000, ratio=1.027, hyp_len=24169, ref_len=23526)
    wait 1  BLEU = 28.62, 67.3/37.8/22.0/13.2 (BP=0.976, ratio=0.976, hyp_len=22368, ref_len=22907)
    wait 2  BLEU = 29.58, 69.4/39.5/23.2/14.1 (BP=0.961, ratio=0.962, hyp_len=21804, ref_len=22674)
    wait 3  BLEU = 29.77, 69.2/39.5/23.2/14.2 (BP=0.966, ratio=0.966, hyp_len=21926, ref_len=22695)
    wait 4  BLEU = 32.12, 69.7/41.0/24.5/15.2 (BP=1.000, ratio=1.005, hyp_len=23012, ref_len=22890)
    wait 5  BLEU = 32.74, 71.4/41.9/25.1/15.5 (BP=0.997, ratio=0.997, hyp_len=22775, ref_len=22849)
    wait 6  BLEU = 33.21, 72.4/43.1/26.2/16.5 (BP=0.975, ratio=0.975, hyp_len=22072, ref_len=22630)
    wait 7  BLEU = 34.05, 73.1/43.7/26.7/16.9 (BP=0.982, ratio=0.982, hyp_len=22235, ref_len=22639)
    wait 8  BLEU = 34.36, 73.8/44.3/27.1/17.0 (BP=0.981, ratio=0.981, hyp_len=22242, ref_len=22662)
    wait 9  BLEU = 34.73, 73.8/44.6/27.7/17.4 (BP=0.978, ratio=0.979, hyp_len=22166, ref_len=22653)
    wait 10  BLEU = 35.70, 73.6/44.8/28.0/18.0 (BP=0.994, ratio=0.994, hyp_len=22569, ref_len=22707)

    22:31:56 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding
    $ bleu3 0 1 3
    tgt 2   BLEU = 41.00, 79.3/51.1/33.6/22.4 (BP=0.980, ratio=0.981, hyp_len=22421, ref_len=22864)
    wait 1  BLEU = 29.51, 68.9/39.1/23.1/14.3 (BP=0.961, ratio=0.962, hyp_len=22368, ref_len=23258)
    wait 2  BLEU = 29.98, 70.9/40.6/24.1/14.8 (BP=0.942, ratio=0.944, hyp_len=21804, ref_len=23096)
    wait 3  BLEU = 30.04, 70.5/40.4/23.9/14.7 (BP=0.950, ratio=0.951, hyp_len=21926, ref_len=23058)
    wait 4  BLEU = 32.41, 71.0/41.8/25.1/15.5 (BP=0.989, ratio=0.989, hyp_len=23012, ref_len=23262)
    wait 5  BLEU = 32.77, 72.9/42.9/25.6/15.6 (BP=0.980, ratio=0.981, hyp_len=22775, ref_len=23225)
    wait 6  BLEU = 33.22, 73.8/43.9/26.6/16.7 (BP=0.960, ratio=0.961, hyp_len=22072, ref_len=22967)
    wait 7  BLEU = 34.06, 74.4/44.4/27.1/17.1 (BP=0.968, ratio=0.969, hyp_len=22235, ref_len=22948)
    wait 8  BLEU = 34.71, 75.0/45.4/27.9/17.4 (BP=0.968, ratio=0.969, hyp_len=22242, ref_len=22960)
    wait 9  BLEU = 35.05, 75.2/45.7/28.4/17.9 (BP=0.963, ratio=0.964, hyp_len=22166, ref_len=23000)
    wait 10  BLEU = 35.83, 75.2/45.8/28.7/18.5 (BP=0.974, ratio=0.974, hyp_len=22569, ref_len=23162)

    22:32:08 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding
    $ bleu3 0 1 2
    tgt 3   BLEU = 34.07, 74.3/43.6/26.0/16.0 (BP=1.000, ratio=1.012, hyp_len=23554, ref_len=23277)
    wait 1  BLEU = 29.17, 67.7/38.2/22.6/14.0 (BP=0.970, ratio=0.971, hyp_len=22368, ref_len=23039)
    wait 2  BLEU = 30.14, 69.8/40.0/23.9/14.8 (BP=0.956, ratio=0.957, hyp_len=21804, ref_len=22791)
    wait 3  BLEU = 30.57, 69.6/40.2/24.2/15.2 (BP=0.960, ratio=0.961, hyp_len=21926, ref_len=22819)
    wait 4  BLEU = 33.00, 70.2/41.7/25.5/16.0 (BP=0.999, ratio=0.999, hyp_len=23012, ref_len=23035)
    wait 5  BLEU = 33.14, 71.8/42.4/25.7/16.0 (BP=0.990, ratio=0.990, hyp_len=22775, ref_len=22994)
    wait 6  BLEU = 33.67, 72.7/43.8/26.8/17.0 (BP=0.970, ratio=0.971, hyp_len=22072, ref_len=22742)
    wait 7  BLEU = 34.81, 73.6/44.3/27.5/17.8 (BP=0.980, ratio=0.980, hyp_len=22235, ref_len=22685)
    wait 8  BLEU = 35.38, 74.3/45.4/28.2/17.9 (BP=0.978, ratio=0.978, hyp_len=22242, ref_len=22731)
    wait 9  BLEU = 35.47, 74.4/45.5/28.6/18.2 (BP=0.974, ratio=0.975, hyp_len=22166, ref_len=22742)
    wait 10  BLEU = 36.44, 74.3/45.7/29.0/18.8 (BP=0.987, ratio=0.987, hyp_len=22569, ref_len=22865)
    ```
[***Back to CONTENTS***](#bleu-results)  

---  

#### 3 ref catchup @ 09/20/2018
5: 3 reference after decoding new catchup models, night 09/20/2018. (/mnt/home/kaibo/proj/fordecoding_catchup)
    ```bash
    22:45:00 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding_catchup
    $ bleu3 1 2 3
    tgt 0   BLEU = 45.32, 82.3/55.6/37.6/25.5 (BP=0.990, ratio=0.990, hyp_len=22601, ref_len=22823)
    wait 1  BLEU = 21.57, 65.1/34.0/18.9/10.9 (BP=0.831, ratio=0.844, hyp_len=19266, ref_len=22831)
    wait 2  BLEU = 21.85, 65.8/34.8/19.2/11.0 (BP=0.827, ratio=0.841, hyp_len=19312, ref_len=22970)
    wait 3  BLEU = 25.44, 66.3/35.4/19.5/11.3 (BP=0.948, ratio=0.949, hyp_len=21954, ref_len=23134)
    wait 4  BLEU = 28.21, 69.2/38.9/22.6/13.4 (BP=0.940, ratio=0.941, hyp_len=21871, ref_len=23230)
    wait 5  BLEU = 29.42, 70.7/40.1/23.3/13.9 (BP=0.949, ratio=0.950, hyp_len=21770, ref_len=22908)
    wait 6  BLEU = 30.38, 71.4/41.2/24.1/14.6 (BP=0.952, ratio=0.953, hyp_len=21874, ref_len=22941)
    wait 7  BLEU = 30.76, 72.0/41.7/24.4/14.6 (BP=0.956, ratio=0.956, hyp_len=22041, ref_len=23044)
    wait 8  BLEU = 32.71, 73.5/43.6/25.9/15.7 (BP=0.968, ratio=0.968, hyp_len=22275, ref_len=23001)
    wait 9  BLEU = 31.30, 72.8/42.5/25.2/15.4 (BP=0.945, ratio=0.947, hyp_len=21625, ref_len=22838)
    wait 10  BLEU = 33.53, 73.2/43.6/26.2/16.1 (BP=0.985, ratio=0.985, hyp_len=22774, ref_len=23117)
    22:45:46 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding_catchup
    $ bleu3 0 2 3
    tgt 1   BLEU = 37.85, 75.5/47.2/30.0/19.2 (BP=1.000, ratio=1.027, hyp_len=24169, ref_len=23526)
    wait 1  BLEU = 21.88, 63.9/33.3/18.9/11.0 (BP=0.848, ratio=0.858, hyp_len=19266, ref_len=22445)
    wait 2  BLEU = 21.93, 64.5/34.2/19.1/10.9 (BP=0.842, ratio=0.853, hyp_len=19312, ref_len=22643)
    wait 3  BLEU = 25.50, 64.7/34.5/19.4/11.4 (BP=0.961, ratio=0.962, hyp_len=21954, ref_len=22831)
    wait 4  BLEU = 28.44, 67.8/38.0/22.4/13.5 (BP=0.957, ratio=0.958, hyp_len=21871, ref_len=22822)
    wait 5  BLEU = 29.62, 69.3/39.5/23.2/14.3 (BP=0.960, ratio=0.961, hyp_len=21770, ref_len=22656)
    wait 6  BLEU = 30.65, 70.1/40.4/24.2/15.0 (BP=0.963, ratio=0.963, hyp_len=21874, ref_len=22707)
    wait 7  BLEU = 31.23, 70.6/41.0/24.6/15.2 (BP=0.967, ratio=0.968, hyp_len=22041, ref_len=22771)
    wait 8  BLEU = 33.00, 72.0/42.7/25.8/16.1 (BP=0.982, ratio=0.982, hyp_len=22275, ref_len=22681)
    wait 9  BLEU = 31.75, 71.8/42.0/25.4/15.9 (BP=0.955, ratio=0.956, hyp_len=21625, ref_len=22611)
    wait 10  BLEU = 34.64, 72.5/43.7/27.1/17.1 (BP=0.995, ratio=0.995, hyp_len=22774, ref_len=22899)
    22:46:03 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding_catchup
    $ bleu3 0 1 3
    tgt 2   BLEU = 41.00, 79.3/51.1/33.6/22.4 (BP=0.980, ratio=0.981, hyp_len=22421, ref_len=22864)
    wait 1  BLEU = 22.10, 65.0/34.5/19.7/11.6 (BP=0.826, ratio=0.840, hyp_len=19266, ref_len=22944)
    wait 2  BLEU = 22.59, 65.8/35.6/20.3/11.9 (BP=0.823, ratio=0.837, hyp_len=19312, ref_len=23069)
    wait 3  BLEU = 25.81, 66.2/35.6/20.1/11.8 (BP=0.944, ratio=0.945, hyp_len=21954, ref_len=23230)
    wait 4  BLEU = 28.26, 69.0/38.8/22.6/13.6 (BP=0.938, ratio=0.940, hyp_len=21871, ref_len=23270)
    wait 5  BLEU = 29.77, 70.8/40.4/23.8/14.5 (BP=0.944, ratio=0.945, hyp_len=21770, ref_len=23034)
    wait 6  BLEU = 30.94, 71.5/41.5/24.8/15.3 (BP=0.949, ratio=0.951, hyp_len=21874, ref_len=23008)
    wait 7  BLEU = 31.08, 72.0/41.6/24.9/15.2 (BP=0.951, ratio=0.952, hyp_len=22041, ref_len=23146)
    wait 8  BLEU = 32.92, 73.5/43.5/26.3/16.2 (BP=0.965, ratio=0.965, hyp_len=22275, ref_len=23080)
    wait 9  BLEU = 31.75, 73.1/42.8/25.9/16.1 (BP=0.939, ratio=0.941, hyp_len=21625, ref_len=22989)
    wait 10  BLEU = 34.13, 73.6/44.0/26.9/16.9 (BP=0.981, ratio=0.981, hyp_len=22774, ref_len=23215)
    22:46:16 kaibo@asimov-8 /mnt/home/kaibo/proj/fordecoding_catchup
    $ bleu3 0 1 2
    tgt 3   BLEU = 34.07, 74.3/43.6/26.0/16.0 (BP=1.000, ratio=1.012, hyp_len=23554, ref_len=23277)
    wait 1  BLEU = 22.12, 64.1/33.8/19.3/11.5 (BP=0.840, ratio=0.852, hyp_len=19266, ref_len=22618)
    wait 2  BLEU = 22.55, 65.0/34.9/19.9/11.9 (BP=0.833, ratio=0.846, hyp_len=19312, ref_len=22838)
    wait 3  BLEU = 26.30, 65.2/35.4/20.3/12.2 (BP=0.956, ratio=0.957, hyp_len=21954, ref_len=22945)
    wait 4  BLEU = 28.85, 68.3/38.6/23.0/14.1 (BP=0.949, ratio=0.950, hyp_len=21871, ref_len=23013)
    wait 5  BLEU = 30.41, 69.7/40.4/24.3/15.1 (BP=0.954, ratio=0.955, hyp_len=21770, ref_len=22799)
    wait 6  BLEU = 31.25, 70.6/41.2/25.0/15.7 (BP=0.955, ratio=0.956, hyp_len=21874, ref_len=22875)
    wait 7  BLEU = 31.72, 71.1/41.8/25.2/15.7 (BP=0.964, ratio=0.964, hyp_len=22041, ref_len=22853)
    wait 8  BLEU = 33.57, 72.4/43.3/26.7/16.8 (BP=0.974, ratio=0.975, hyp_len=22275, ref_len=22853)
    wait 9  BLEU = 32.74, 72.3/43.1/26.6/16.9 (BP=0.952, ratio=0.953, hyp_len=21625, ref_len=22690)
    wait 10  BLEU = 34.66, 72.5/43.8/27.3/17.4 (BP=0.989, ratio=0.989, hyp_len=22774, ref_len=23034)
    ```
[***Back to CONTENTS***](#bleu-results)  

---  



#### decoding @ 09/21/2018
1. wait_short @39,39,39,43,45,48,48,44,44,44k iter, 4ref/1ref/3ref saved in `~/proj/fordecoding/decode_result_0921/BLEU_0921_1523.txt`
1. catchup_short @41,38,35,49,45,39,33,47,43,46k iter, 4ref/1ref/3ref saved in `~/proj/fordecoding_catchup/decode_result_0921/BLEU_0921_1526.txt`
1. detail of waitk model:
    1. BLEU on 4/1 ref
    ```bash

    ```
    1. BLEU on 3 ref

#### decoding @ 09/24/2018
1. waitk_short  @69,69,71,78,82,84,84,82,83,85k iter, 4ref/1ref/3ref saved in `~/proj/fordecoding/decode_result_0924/BLEU_0924.txt`
1. catchup_long @70,62,72,79,83,61,55,89,78,86k iter, 4ref/1ref/3ref saved in `~/proj/fordecoding_catch/decode_result_0924/BLEU_0924.txt`
```bash
waitk
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait1/w1_step_69000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait2/w2_step_69000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait3/w3_step_71000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait4/w4_step_78000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait5/w5_step_82000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait6/w6_step_84000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait7/w7_step_84000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait8/w8_step_82000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait9/w9_step_83000.pt
/mnt/home/kaibo/proj/opennmt_v726_waitk/secondrun/wait10/w10_step_85000.pt
catchup
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait1/w1_step_70000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait2/w2_step_62000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait3/w3_step_72000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait4/w4_step_79000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait5/w5_step_83000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait6/w6_step_61000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait7/w7_step_55000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait8/w8_step_89000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait9/w9_step_78000.pt
/mnt/home/kaibo/proj/opennmt_v726_catchup/secondrun/wait10/w10_step_86000.pt
```
