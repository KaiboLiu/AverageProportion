'''
09/20/2018 Thu 
__author__: Kaibo Liu
calculate the AL from paper 
src=./testdata/test.txt, from /mnt/scratch/kaibo/proj/fordecoding/test.txt (616 lines)
tgt=./catchup/pred.w<i>.unbpe.txt, from /mnt/scratch/kaibo/proj/fordecoding_catchup/decode_result/pred.w<i>.unbpe.txt (decoded sentences 616 lines)
tgt=./waitk/pred.w<i>.unbpe.txt, from /mnt/scratch/kaibo/proj/fordecoding/decode_result/pred.w<i>.unbpe.txt (decoded sentences 616 lines)
'''
import sys
import os
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


# diagonal of x, y
'''
def calc_AL_waitk(x,y,waitk):
    return y*(waitk-1)+y*waitk*(waitk-1)/2/x
'''
def calc_AL_waitk(x, y, k):
    if y == 0: return 0
    #y1 = min(max(x-k+1, 1), y)
    #a = list(range(k, k+y1))
    curr = list(range(k, x+1))[:y] if x >=k else [x]
    y1 = len(curr)
    s = sum(curr) - x*y/2*(y1/y)**2
    return s/y1

# diagonal of catchup 1112 
'''
def calc_AL_catchup(x,y,waitk):
    if y == 0: return 0

    inc = [1,1,1,1,0]
    start = 1
    base, curr = [start], [waitk]
    for i in range(1, y): 
        newval = base[-1]+inc[i % 5] if base[-1] < x else x 
        base.append(newval)
        newval = curr[-1]+inc[i % 5] if curr[-1] < x else x 
        curr.append(newval)
    return sum(b-a for a,b in zip(base, curr))
'''
def calc_AL_catchup(x,y,k):
    if y == 0: return 0

    inc = [1,1,1,1,0]
    start = 1
    curr = [k] if x >=k else [x]
    for i in range(1, y): 
        if curr[-1] == x: break
        newval = curr[-1]+inc[i % 5]
        curr.append(newval)
    y1 = len(curr)
    s = sum(curr) - x*y/2*(y1/y)**2
    return s/y1


def get_n_words(s, is_clean=False):
    if is_clean:
        s = s.replace('@@ ','')
    return len(s.strip().split()), s 
    
def draw_xy(x, y, color, figPath, draw_k):
    #plt.scatter(a[:,0], a[:,1], c=y, s=40, cmap=plt.cm.Spectral)
    #  Set default x-axis tick labels on the top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

    xy_max = max(max(y), max(x))+5
    #fig = plt.figure(figsize=(6,6)) 
    fig, ax = plt.subplots(figsize=(8,6))
    #ax[0].scatter(a[:,1], a[:,0], s=40, cmap=plt.cm.Spectral)
    #ax[0].plot([1, xy_max], [1, xy_max],c='b')
   
    ax.plot([1, xy_max], [1, xy_max],c='r')

    sc = ax.scatter(y, x, c=color,
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
    fig.savefig('{}_wait{}.pdf'.format(figPath, draw_k))
    

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
def AL_from_file(src_file, tgt_dir, type_dataset, type_bpe, is_clean=False, is_weight_ave=False):
    title_base = '{}_scatter_{}_{}_AL'.format(tgt_dir, type_dataset, type_bpe)
    k_max = 10
    ave_wait = [[] for i in range(k_max)]
    prop = [[] for i in range(k_max)]   # k_max * count
    AL_list = []
    len_ys = []
    
    zh = open(src_file, 'r').readlines()
    len_x = [get_n_words(x, is_clean)[0] for x in zh]
    count = len(len_x)
    for waitk in range(1, k_max+1):
        en = open('{}/{}_pred.w{}.{}.txt'.format(tgt_dir, type_dataset, waitk, type_bpe), 'r').readlines()
        len_y = [get_n_words(y, is_clean)[0] for y in en]
        len_ys.append(len_y)
        for i, (x, y) in enumerate(zip(len_x, len_y)):
            #s = calc_AP(x, y, waitk)[1]
            s = calc_AL_waitk(x, y, waitk) if tgt_dir == 'waitk' else calc_AL_catchup(x, y, waitk)
            ave_wait[waitk-1].append(s)
            #if s < -18 or x < 1 or y < 1: print('{}/{}_pred.w{}.{}.txt'.format(tgt_dir, type_dataset, waitk, type_bpe), waitk, x, y, i+1, s)
            #ratio = s/x/y if x > 0 and y > 0 else 0
            #ratio = s/y if y > 0 else 0
            ratio = s
            prop[waitk-1].append(ratio)
    
        if is_weight_ave:
            #weights = [x*y for x, y in zip(len_x, len_y)]
            #weights = [y for y in len_y]
            weights = len_x
        else: 
            weights = [1] * count

        f = open(out_dir + title_base + '_wait{}.txt'.format(waitk), 'w')
        for i in range(count):
            f.write('{} {} {} {}\n'.format(len_x[i], len_y[i], ave_wait[waitk-1][i], prop[waitk-1][i]))
        f.close()
        total_weight = sum(weights) 
        AL = sum(p*w for p,w in zip(prop[waitk-1], weights)) / total_weight
        print('[{} lines] [{}] [weighted_ave] {} [waitk] {} [AL] {:.5f} [range] {:.3f}..{:.3f}'.format(count, type_bpe, is_weight_ave, waitk, AL, min(prop[waitk-1]), max(prop[waitk-1]))) 
        AL_list.append(AL)

    #for disp_k in range(1,11):
    #    display_instance(zh, en, is_clean, prop, disp_k)

    
    #draw_k = 3 
    if is_weight_ave and type_dataset == 'dev':
        for draw_k in range(1,11):
            draw_xy(len_x, len_ys[draw_k-1], prop[draw_k-1], title_base, draw_k)
    print()
    
    '''
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
    fig2,ax2 = plt.subplots()
    x = list(range(1,11))
    loerr = [b-min(a) for a,b in zip(prop,AL_list)]
    uperr = [max(a)-b for a,b in zip(prop,AL_list)]
    ax2.errorbar(x, AL_list, yerr=[loerr, uperr],marker='s', ecolor='g', fmt='-o')
    ax2.set_xlabel('Wait_k')
    ax2.set_ylabel('Average Proportion')
    fig2.savefig('corpus_{}.pdf'.format(title_base))
    '''
    loerr = [b-min(a) for a,b in zip(prop,AL_list)]
    uperr = [max(a)-b for a,b in zip(prop,AL_list)]
    return AL_list, loerr, uperr, is_weight_ave, prop



def plot_all(src, tgt_dir, type_dataset, type_bpe):
    AL_list1, loerr, uperr, is_weight_ave, prop = AL_from_file(src, tgt_dir, type_dataset, type_bpe, is_clean=False, is_weight_ave=False)
    AL_list2, _, _, is_weight_ave, _ = AL_from_file(src, tgt_dir, type_dataset, type_bpe, is_clean=False, is_weight_ave=True)

    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
    fig,ax = plt.subplots()
    x = list(range(1,11))
    #ax.errorbar(x, AL_list1, yerr=[loerr, uperr],marker='s', ecolor='g', fmt='-o', label='mean')
    ax.plot(x, AL_list1, 's-',label='mean')
    ax.plot(x, AL_list2, 'ro-',label='corpus_ave')
    ax.violinplot(prop, showmeans=True, showmedians=True)
    ax.set_xlabel('Wait_k')
    ax.set_ylabel('Average Lagging')
    ax.legend(loc='upper left')
    fig.savefig('{}_{}_{}_AL.pdf'.format(tgt_dir, type_dataset, type_bpe))   

    f = open('{}_{}_AL.txt'.format(tgt_dir, type_dataset), 'w')
    print('{}_{}_AL.txt'.format(tgt_dir, type_dataset))
    f.write('mean\n{}\ncorpus\n{}\n'.format(' '.join(map(str,AL_list1)), ' '.join(map(str,AL_list2))))
    f.close
if __name__=="__main__":
    if len(sys.argv) == 3:
        type_dataset = sys.argv[1]
        type_bpe = sys.argv[2]
    else:
        type_dataset = 'dev'
        type_bpe = 'bpe'

    os.system("cp ./testdata/test_src.text ./testdata/test_src")
    os.system("cp ./testdata/dev_06.zh ./testdata/dev_src")
    os.system("cp ./testdata/dev_06.zh.bpe ./testdata/dev_src.bpe")

    src = './testdata/{}_src'.format(type_dataset)
    if type_bpe == 'bpe': src += '.bpe'
    tgt_dir = 'waitk'
    plot_all(src, tgt_dir, type_dataset, type_bpe)
    tgt_dir = 'catchup'
    plot_all(src, tgt_dir, type_dataset, type_bpe)
