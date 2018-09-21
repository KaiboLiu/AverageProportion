'''
09/12/2018 Wed
__author__: Kaibo Liu
calculate the AP from paper 
sec=/mnt/data/mam/data/data_zh2en_2M/dev_06.zh.bpe
tgt=/mnt/data/mam/data/data_zh2en_2M/dev_06.en.0.bpe
'''
import sys
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np


def calc_AP(x,y,waitk):
    '''
    math 
        s=sum{k..x}+x*(y-x+k-1)  , if y>=x-k+1
        s=sum{k..k+y-1}          , if y<=x-k+1
        s=sum{k..x}=sum{k..k+y-1}, if y==x-k+1
    list:
        list of y elements, starting from k, increased by 1, upper bound to x
    '''
    a = [i if i < x else x for i in range(waitk, waitk+y)]
    return a, sum(a)
    #return sum(i if i < x else x for i in range(waitk, waitk+y)) 

def get_n_words(s, is_clean=False):
    if is_clean:
        s = s.replace('@@ ','')
    return len(s.strip().split()), s 
    
def draw_xy(pos, color, figPath, draw_k):
    a = np.array(pos)
    #plt.scatter(a[:,0], a[:,1], c=y, s=40, cmap=plt.cm.Spectral)
    #  Set default x-axis tick labels on the top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

    xy_max = max(max(a[:,1]), max(a[:,0]))+5
    #fig = plt.figure(figsize=(6,6)) 
    fig, ax = plt.subplots(figsize=(8,6))
    #ax[0].scatter(a[:,1], a[:,0], s=40, cmap=plt.cm.Spectral)
    #ax[0].plot([1, xy_max], [1, xy_max],c='b')
   
    ax.plot([1, xy_max], [1, xy_max],c='r')

    sc = ax.scatter(a[:,1], a[:,0], c=color,
               vmin=min(color), vmax=max(color), s=20, 
               edgecolors='b',
               #cmap=plt.cm.get_cmap('RdYlBu'))
               cmap=plt.cm.get_cmap('cool'))
               #cmap='PuBu_r')
               #cmap='Blues')
    #fig.colorbar(sc, ax=ax[0],extend='max')
    fig.colorbar(sc)


    #plt.scatter(a[:,1], a[:,0], s=40, cmap=plt.cm.Spectral)
    #plt.plot([1, xy_max], [1, xy_max],c='b')
    plt.xlim([0,xy_max])
    plt.ylim([0,xy_max])
    #plt.ylabel('source length |X|')
    #plt.xlabel('target length')
    #ax.set_xlabel('target length |X|')
    ax.set_title('target length |Y|', pad=24)
    ax.set_ylabel('source length |X|')
    plt.gca().invert_yaxis()   # put origin at top
    #plt.show()
    fig.savefig('{}_wait{}.png'.format(figPath, draw_k))
    

def display_instance(zh, en, is_clean, prop, waitk):
    idx = np.argmin(prop[waitk-1])
    print('wait{}_min_prop:{:.3f} @ idx:{}'.format(waitk, prop[waitk-1][idx], idx))
    print('[{} words] {}'.format(*get_n_words(zh[idx], is_clean)), end='')
    print('[{} words] {}'.format(*get_n_words(en[idx], is_clean)))

    idx = np.argmax(prop[waitk-1])
    print('wait{}_max_prop:{:.3f} @ idx:{}'.format(waitk, prop[waitk-1][idx], idx))
    print('[{} words] {}'.format(*get_n_words(zh[idx], is_clean)), end='')
    print('[{} words] {}'.format(*get_n_words(en[idx], is_clean)))
    #display_instance(zh, en, is_clean, prop, idx, disp_k)
    


out_dir = './output/'
def AP_from_file(file_zh, file_en, is_clean=False, is_weight_ave=False):
    k_max = 10
    ave_wait = [[] for i in range(k_max)]
    prop = [[] for i in range(k_max)]
    AP_list = []
    length = []

    zh = open(file_zh, 'r').readlines()
    en = open(file_en, 'r').readlines()
    count = 0
    for src, tgt in zip(zh, en):
        count += 1
        x = get_n_words(src, is_clean)[0]
        y = get_n_words(tgt, is_clean)[0]
        length.append([x,y])
        for waitk in range(1, k_max+1):
            s = calc_AP(x, y, waitk)[1]
            ave_wait[waitk-1].append(s)
            prop[waitk-1].append(s/x/y)
    

    title_base = 'gold_clean{}_weight{}'.format(str(is_clean)[0], str(is_weight_ave)[0])
    if is_weight_ave:
        weights = [x[0]*x[1] for x in length]
    else: 
        weights = [1] * count
    for waitk in range(1, k_max+1):
        f = open(out_dir + title_base + '_wait{}.txt'.format(waitk), 'w')
        for i in range(count):
            f.write('{} {} {} {}\n'.format(length[i][0], length[i][1], ave_wait[waitk-1][i], prop[waitk-1][i]))
        f.close()
        total_weight = sum(weights) 
        AP = sum(p*w for p,w in zip(prop[waitk-1], weights)) / total_weight
        print('[{} lines] [clean_bpe_mark] {} [weighted_ave] {} [waitk] {} [AP] {:.5f} [range] {:.3f}..{:.3f}'.format(count, is_clean, is_weight_ave, waitk, AP, min(prop[waitk-1]), max(prop[waitk-1]))) 
        AP_list.append(AP)

    for disp_k in range(1,11):
        display_instance(zh, en, is_clean, prop, disp_k)

    
    #draw_k = 3 
    if is_weight_ave:
        for draw_k in range(1,11):
            draw_xy(length, prop[draw_k-1], title_base, draw_k)
    print()
    
    '''
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
    fig2,ax2 = plt.subplots()
    x = list(range(1,11))
    loerr = [b-min(a) for a,b in zip(prop,AP_list)]
    uperr = [max(a)-b for a,b in zip(prop,AP_list)]
    ax2.errorbar(x, AP_list, yerr=[loerr, uperr],marker='s', ecolor='g', fmt='-o')
    ax2.set_xlabel('Wait_k')
    ax2.set_ylabel('Average Proportion')
    fig2.savefig('corpus_{}.png'.format(title_base))
    '''
    loerr = [b-min(a) for a,b in zip(prop,AP_list)]
    uperr = [max(a)-b for a,b in zip(prop,AP_list)]
    return AP_list, loerr, uperr, is_weight_ave, prop



def curvex2(f1, f2):
    AP_list1, loerr, uperr, is_weight_ave, prop = AP_from_file(f1, f2, is_clean=False, is_weight_ave=False)
    AP_list2, _, _, is_weight_ave, _ = AP_from_file(f1, f2, is_clean=False, is_weight_ave=True)

    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
    fig,ax = plt.subplots()
    x = list(range(1,11))
    #ax.errorbar(x, AP_list1, yerr=[loerr, uperr],marker='s', ecolor='g', fmt='-o', label='mean')
    ax.plot(x, AP_list1, 's-',label='mean')
    ax.plot(x, AP_list2, 'ro-',label='weighted_ave')
    ax.violinplot(prop, showmeans=True, showmedians=True)
    ax.set_xlabel('Wait_k')
    ax.set_ylabel('Average Proportion')
    ax.legend(loc='lower right')
    fig.savefig('gold_corpus_AP.png')
   
if __name__=="__main__":
#    print(5,6,1, calc_AP(5,6,1))
#    print(5,6,2, calc_AP(5,6,2))
#    print(5,4,1, calc_AP(5,4,1))
#    print(6,9,2, calc_AP(6,9,2))
    if len(sys.argv) == 3:
        f1 = sys.argv[1]
        f2 = sys.argv[2]
    else:
        f1 = 'dev_06.zh.bpe'
        f2 = 'dev_06.en.0.bpe' 
    #AP_from_file(f1, f2, is_clean=False, is_weight_ave=False)
    #AP_from_file(f1, f2, is_clean=True,  is_weight_ave=False)
    #AP_from_file(f1, f2, is_clean=False, is_weight_ave=True)
    #AP_from_file(f1, f2, is_clean=True,  is_weight_ave=True)
    curvex2(f1, f2)
