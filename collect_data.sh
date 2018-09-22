rm -fr catchup waitk testdata
# dev/test pred
scp -r kaibo@asimov-0-log.svail.baidu.com:/mnt/scratch/kaibo/proj/fordecoding_catchup/decode_result ./catchup
scp -r kaibo@asimov-0-log.svail.baidu.com:/mnt/scratch/kaibo/proj/fordecoding/decode_result ./waitk
# dev/test ref
scp -r  kaibo@asimov-0-log.svail.baidu.com:/mnt/data/mam/data/data_zh2en_2M/evaldata ./testdata
# test set src
scp  kaibo@asimov-0-log.svail.baidu.com:/mnt/data/mam/data/data_zh2en_2M/test_src.bpe ./testdata/
scp  kaibo@asimov-0-log.svail.baidu.com:/mnt/data/mam/data/data_zh2en_2M/test_src.text ./testdata/
# dev set src
scp  kaibo@asimov-0-log.svail.baidu.com:/mnt/data/mam/data/data_zh2en_2M/dev_06.zh.bpe ./testdata/
scp  kaibo@asimov-0-log.svail.baidu.com:/mnt/data/mam/data/data_zh2en_2M/dev_06.zh ./testdata/
