'''
09/24/2018 Thu 
__author__: Kaibo Liu
plot the BLEU-AP figures
'''
import sys
import re
import os
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np


def get_data(type_ref, type_dataset):
    file_bleu_cat = 'catchup/BLEU_0924_cat_short.txt'
    file_bleu_wait = 'waitk/BLEU_0924.txt'
    file_bleu_rnn = 'zh2en_rnn/rnn/{}/{}2.bleu.unbpe'.format(type_dataset,type_dataset)

    lineNums = [12, 15, 28, 31]
    lineNum = lineNums[2* (0 if type_dataset == 'dev' else 1) + (0 if type_ref == '4refs' else 1)]
    pattern = 'BLEU = ([^,]+),'
    line = open('BLEU.md','r').readlines()[lineNum]
    bleu_base = round(float(re.findall(pattern, line)[0]), 2)  # 22.11 on dev, 19.03 on test
    bleu_base1 = 23.69 if type_dataset == 'dev' else 20.29 # beam11
     
    bleu_base_rnn = 15.51 if type_dataset == 'dev' else 15.08 # greedy
    bleu_base_rnn1 = 16.57 if type_dataset == 'dev' else 16.40 # beam 5
    lineNum = 1 # 1 if mean, 3 if corpus ave

    wait_AP = list(map(float, open('waitk_{}_AP.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))
    cat_AP = list(map(float, open('catchup_{}_AP.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))
    wait_AL = list(map(float, open('waitk_{}_AL.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))
    cat_AL = list(map(float, open('catchup_{}_AL.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))

    rnn_AP = list(map(float, open('zh2en_rnn/rnn/zh2en_rnn_{}_AP.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))
    rnn_AL = list(map(float, open('zh2en_rnn/rnn/zh2en_rnn_{}_AL.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))
    
    marker_size = 120

    startLine = 0
    if type_dataset == 'dev':
        startLine = 4 if type_ref =='4refs' else 38
        #startLine = 110 if type_ref =='4refs' else 144 
    else: 
        startLine = 110 if type_ref =='4refs' else 144

    wait_bleu = [float(re.findall(pattern, line)[0]) for line in open(file_bleu_wait,'r').readlines()[startLine: startLine+10]] 
    cat_bleu = [float(re.findall(pattern, line)[0]) for line in open(file_bleu_cat,'r').readlines()[startLine: startLine+10]] 
    rnn_bleu = [float(re.findall(pattern, line)[0]) for line in open(file_bleu_rnn,'r').readlines()[0:10]] 
    
    eos_apply_index = 5  # wait1..wait5 use softeos
    if type_dataset == 'dev':
        # zh2en+dev+catchup+threshold_0.01+detla_10, files in /mnt/home/kaibo/proj/fordecoding_catchup_softeos/decode_APALBLEU_dev_catchup_threshold0.01+detla10_softEOS.txt
        cat_AP[:eos_apply_index] = [0.519  ,0.560  ,0.590  ,0.623  ,0.654  ,0.689  ,0.709  ,0.734  ,0.763  , 0.781][:eos_apply_index]
        cat_AL[:eos_apply_index] = [0.168, 1.714, 2.444, 3.335, 4.360, 5.636, 6.359, 7.263, 8.570, 9.426][:eos_apply_index]
        cat_bleu[:eos_apply_index] = [14.16, 14.79, 16.52, 17.52, 18.47, 18.53, 19.61, 20.19, 19.93,  20.27 ][:eos_apply_index]

    x = range(1,11)
    ylabel = '4-ref BLEU' if type_ref =='4refs' else '1-ref BLEU'

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')   # to use math style font

    plt.rcParams['font.size'] = 18   # global font size
    #plt.gcf().subplots_adjust(bottom=0.5)
    #plt.rcParams.update({'figure.autolayout': True})

    ############ plot BLEU-AP figs #############
    fig,ax = plt.subplots()
    ax.grid(axis='x', linestyle='--') # vertical lines
    ax.margins(0.1)           # Default margin is 0.05, value 0 means fit
    #ax.plot(wait_AP, wait_bleu, 's-', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    #ax.plot(cat_AP, cat_bleu, 'o-', label='+catchup')#+'_'+type_ref+'_'+type_dataset)
    ax.plot(wait_AP, wait_bleu, 's-',color='C0', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    ax.plot(cat_AP, cat_bleu, 'o-', color='C2',label='+catchup')#+'_'+type_ref+'_'+type_dataset)
    

    offset_rate = 1.25 if type_ref =='4refs' else 0.7
    for i in range(10):
        ax.annotate('k={}'.format(i+1), xy=(wait_AP[i]-0.08*offset_rate ,wait_bleu[i]+1.5*offset_rate), color='C0', rotation=-45, fontsize=15)
        ax.annotate('k={}'.format(i+1), xy=(cat_AP[i],cat_bleu[i]-0.8*offset_rate), color='C2', rotation=-45,fontsize=15)
        if i == 0:
            ax.annotate('k={}'.format(i+1), xy=(rnn_AP[i],rnn_bleu[i]-0.5*offset_rate), color='C1', rotation=-45,fontsize=15)
        elif i in (4,7):
            ax.annotate('k={}'.format(i+1), xy=(rnn_AP[i]-0.01,rnn_bleu[i]-0.8*offset_rate), color='C1', rotation=-45,fontsize=15)
        else:
            ax.annotate('k={}'.format(i+1), xy=(rnn_AP[i],rnn_bleu[i]-0.8*offset_rate), color='C1', rotation=-45,fontsize=15)
    #ax.annotate('k=1', xy=(cat_AP[0]-0.035*offset_rate,cat_bleu[0]+1.2*offset_rate), color='C1', rotation=-45,fontsize=15)
    #ax.hlines(bleu_base, ax.axis()[0], ax.axis()[1], 'r', linestyles='dashed', label=    'baseline')

    ax.scatter(1, bleu_base1, marker='*', facecolors='none', edgecolors='C0', s=120)#, label='baseline') 
    ax.scatter(1, bleu_base, marker='*', color='C0', s=120)#, label='baseline') 
    ax.plot([1,1],[bleu_base1,bleu_base],'C0',linewidth=0.5)

    ax.plot(rnn_AP, rnn_bleu,'D-', color='C1',label='RNN')
    ax.scatter(1, bleu_base_rnn1, marker='*', facecolors='none', edgecolors='C1', s=120)#, label='baseline') 
    ax.scatter(1, bleu_base_rnn, marker='*', color='C1', s=120)#, label='baseline') 
    ax.plot([1,1],[bleu_base_rnn1,bleu_base_rnn],'C1',linewidth=0.5)
    ax.set_xlabel('Average Proportion')
    ax.set_ylabel(ylabel)
    ax.legend(loc=2, prop={'size': 10})
    plt.tight_layout()  # make room for the xlabel
    fig.savefig('bleu_AP_{}_{}.pdf'.format(type_dataset, type_ref))


    ############ plot BLEU-AL figs #############
    #baseline_AL,base_AL_l, base_AL_r = (33.1412, 32.5, 34) if type_dataset == 'dev' else (28.7366, 28, 29.5)
    baseline_AL,base_AL_l, base_AL_r = (33.1412, 31.16, 34) if type_dataset == 'dev' else (28.7366, 27.76, 29.5)
    fig0 = plt.figure()

    axes = fig0.add_axes([0.1, 0.15, 0.7, 0.8]) # left, bottom, width, height (range 0 to 1)
    axes2 = fig0.add_axes([0.82, 0.15, 0.1, 0.8]) # inset axes
    axes.grid(axis='x', linestyle='--') # vertical lines
    axes2.grid(axis='x', linestyle='--') # vertical lines

    axes.margins(0.1)           # Default margin is 0.05, value 0 means fit
    axes.plot(wait_AL, wait_bleu, 's-',color='C0', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    axes.plot(cat_AL, cat_bleu, 'o-', color='C2',label='+catchup')#+'_'+type_ref+'_'+type_dataset)

    axes.scatter(baseline_AL, bleu_base1, marker='*',facecolors='none', edgecolors='C0',s=marker_size)#, label='baseline')#, label='Transformer baseline(beam search)')
    axes.scatter(baseline_AL, bleu_base, marker='*',facecolors='C0', edgecolors='C0',s=marker_size)#, label='baseline')#, label='Transformer baseline(greedy)')
    axes.plot([baseline_AL,baseline_AL],[bleu_base1,bleu_base],'C0',linewidth=0.5)

    axes.scatter(baseline_AL, bleu_base_rnn1, marker='*',facecolors='none', edgecolors='C1',s=marker_size)#, label='baseline')#, label='Transformer baseline(beam search)')
    axes.scatter(baseline_AL, bleu_base_rnn, marker='*',facecolors='C1', edgecolors='C1',s=marker_size)#, label='baseline')#, label='Transformer baseline(greedy)')
    axes.plot([baseline_AL,baseline_AL],[bleu_base_rnn1,bleu_base_rnn],'C1',linewidth=0.5)

    axes.plot(rnn_AL, rnn_bleu, 'D-', color='C1',label='RNN')#+'_'+type_ref+'_'+type_dataset)

    axes2.margins(0.1)           # Default margin is 0.05, value 0 means fit
    axes2.plot(wait_AL, wait_bleu, 's-',color='C0', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    axes2.plot(cat_AL, cat_bleu, 'o-', color='C2',label='+catchup')#+'_'+type_ref+'_'+type_dataset)
    axes2.plot(rnn_AL, rnn_bleu, 'D-', color='C1',label='RNN')#+'_'+type_ref+'_'+type_dataset)

    axes2.scatter(baseline_AL, bleu_base1, marker='*',facecolors='none', edgecolors='C0',s=marker_size)#, label='baseline')#, label='Transformer baseline(beam search)')
    axes2.scatter(baseline_AL, bleu_base, marker='*',facecolors='C0', edgecolors='C0',s=marker_size)#, label='baseline')#, label='Transformer baseline(greedy)')
    axes2.plot([baseline_AL,baseline_AL],[bleu_base1,bleu_base],'C0',linewidth=0.5)

    axes2.scatter(baseline_AL, bleu_base_rnn1, marker='*',facecolors='none', edgecolors='C1',s=marker_size)#, label='baseline')#, label='Transformer baseline(beam search)')
    axes2.scatter(baseline_AL, bleu_base_rnn, marker='*',facecolors='C1', edgecolors='C1',s=marker_size)#, label='baseline')#, label='Transformer baseline(greedy)')
    axes2.plot([baseline_AL,baseline_AL],[bleu_base_rnn1,bleu_base_rnn],'C1',linewidth=0.5)

    axes.set_xlim(-2, 11.9)  # most of the data
    axes2.set_xlim(base_AL_l, base_AL_r)  # outliers/baseline only
    # hide the spines between ax and ax2
    axes.spines['right'].set_visible(False)
    axes2.spines['left'].set_visible(False)
    axes.yaxis.tick_left()
    axes2.tick_params(labelleft='off')  # don't put tick labels at the left
    axes2.yaxis.tick_right()

    #for i in (0,9):
    for i in range(10):
        axes.annotate('k={}'.format(i+1), xy=(wait_AL[i]-2*offset_rate ,wait_bleu[i]+1.7*offset_rate), color='C0', rotation=-45, fontsize=15)
        axes.annotate('k={}'.format(i+1), xy=(cat_AL[i],cat_bleu[i]-0.8*offset_rate), color='C2',rotation=-45, fontsize=15)
        axes.annotate('k={}'.format(i+1), xy=(rnn_AL[i],rnn_bleu[i]-0.8*offset_rate), color='C1',rotation=-45, fontsize=15)
    from numpy import arange, cos, pi
    d, c = .01, 1.015  # how big to make the diagonal lines in axes coordinates
    cut_y = arange(-3*d, 9*d, d/10)
    cut_x = d * cos(cut_y*pi/d/1.8)
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=axes.transAxes, color='k', clip_on=False)
    axes.plot(c+cut_x, 1-cut_y, **kwargs)        # top-left diagonal
    axes.plot(c+cut_x, cut_y, **kwargs)        # top-left diagonal
    ''' cross mark for the broken axis
    axes.plot((c - d, c + d), (1 - d, 1 + d), **kwargs)        # top-left diagonal
    axes.plot((c - d, c + d), (1 + d, 1 - d), **kwargs)        # top-left diagonal
    axes.plot((c - d, c + d), (-d, +d), **kwargs)  # bottom-left diagonal
    axes.plot((c - d, c + d), (+d, -d), **kwargs)  # bottom-left diagonal
    '''
    axes.set_xlabel('Average Lagging')
    axes.set_ylabel(ylabel)
    #fig0.suptitle('big title')
    axes.legend(loc=2, prop={'size': 10})
    plt.tight_layout()  # make room for the xlabel
    fig0.savefig('bleu_AL_{}_{}.pdf'.format(type_dataset, type_ref))

    '''
    fig0,ax0 = plt.subplots()
    ax0.margins(0.1)           # Default margin is 0.05, value 0 means fit
    #ax0.plot(wait_AL, wait_bleu, 's-', label='waitk')#+'_'+type_ref+'_'+type_dataset)
    ax0.plot(wait_AL, wait_bleu, 's-', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    ax0.plot(cat_AL, cat_bleu, 'o-', label='+catchup')#+'_'+type_ref+'_'+type_dataset)
    
    for i in range(10):
        ax0.annotate('k={}'.format(i+1), xy=(wait_AL[i]-0.04*offset_rate ,wait_bleu[i]+1.1*offset_rate), color='C0', rotation=-45, fontsize=15)
        if i > 0: ax0.annotate('k={}'.format(i+1), xy=(cat_AL[i],cat_bleu[i]-0.7*offset_rate), color='C1', rotation=-45,fontsize=15)
    ax0.annotate('k=1', xy=(cat_AL[0]-0.035*offset_rate,cat_bleu[0]+1.2*offset_rate), color='C1', rotation=-45,fontsize=15)
    #ax0.hlines(bleu_base, ax0.axis()[0], ax0.axis()[1], 'r', linestyles='dashed', label=    'baseline')
    ax0.scatter(15, bleu_base, c='r', marker='*', label='baseline') 
    ax0.set_xlabel('Average Lagging')
    ax0.set_ylabel(ylabel)
    ax0.legend(loc='lower right')
    plt.tight_layout()  # make room for the xlabel
    fig0.savefig('bleu_AL_{}_{}.pdf'.format(type_dataset, type_ref))
    '''


    ############ plot BLEU-k figs #############
    fig2,ax2 = plt.subplots()
    ax2.plot(x, wait_bleu, 'C0','s-', label='Transformer')#+'_'+type_ref+'_'+type_dataset) 
    ax2.plot(x, cat_bleu, 'C2','o-', label='+catchup')#+'_'+type_ref+'_'+type_dataset)
    ax2.plot(x, rnn_bleu, 'C1','D-', label='RNN')
    ax2.hlines(bleu_base, ax2.axis()[0], ax2.axis()[1], 'r', linestyles='dashed', label='baseline')
    #ax2.plot(x, [bleu_base]*10, '--', label='baseline'+'_'+type_ref+'_'+type_dataset)
    ax2.set_xlabel(r'$k$')
    ax2.set_ylabel(ylabel)
    ax2.legend(loc='lower right')
    plt.tight_layout()  # make room for the xlabel
    fig2.savefig('bleu_waitk_{}_{}.pdf'.format(type_dataset, type_ref))


# diagonal of catchup 1112
def calc_AP_catchup(x,y,waitk):
    if y == 0: return 0
    if waitk > x: return x*y
    inc = [1,1,1,1,0]
    start = 1
    curr = [waitk]
    for i in range(1, y):
        newval = curr[-1]+inc[i % 5] if curr[-1] < x else x
        curr.append(newval)
    return sum(curr)


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
def AP_from_file(file_src, dir_tgt, type_dataset, type_bpe, is_clean=False, is_weight_ave=False):
    title_base = '{}_scatter_{}_{}_AP'.format(dir_tgt, type_dataset, type_bpe)
    k_max = 10
    ave_wait = [[] for i in range(k_max)]
    prop = [[] for i in range(k_max)]   # k_max * count
    AP_list = []
    len_ys = []
    
    zh = open(file_src, 'r').readlines()
    len_x = [get_n_words(x, is_clean)[0] for x in zh]
    count = len(len_x)
    for waitk in range(1, k_max+1):
        en = open('{}/{}_pred.w{}.{}.txt'.format(dir_tgt, type_dataset, waitk, type_bpe), 'r').readlines()
        len_y = [get_n_words(y, is_clean)[0] for y in en]
        len_ys.append(len_y)
        for i, (x, y) in enumerate(zip(len_x, len_y)):
            #s = calc_AP(x, y, waitk)[1]
            s = calc_AP(x, y, waitk)[1] if tgt_dir == 'waitk' else calc_AP_catchup(x, y, waitk)
            #s = calc_AL_wait(x, y, waitk)
            ave_wait[waitk-1].append(s)
            if x < 1 or y < 1: print('{}/{}_pred.w{}.{}.txt'.format(dir_tgt, type_dataset, waitk, type_bpe), waitk, x, y, i+1)
            ratio = s/x/y if x > 0 and y > 0 else 0
            #ratio = s/y if y > 0 else 0
            prop[waitk-1].append(ratio)
    
        if is_weight_ave:
            #weights = [x*y for x, y in zip(len_x, len_y)]
            weights = [y for y in len_y]
        else: 
            weights = [1] * count

        f = open(out_dir + title_base + '_wait{}.txt'.format(waitk), 'w')
        for i in range(count):
            f.write('{} {} {} {}\n'.format(len_x[i], len_y[i], ave_wait[waitk-1][i], prop[waitk-1][i]))
        f.close()
        total_weight = sum(weights) 
        AP = sum(p*w for p,w in zip(prop[waitk-1], weights)) / total_weight
        print('[{} lines] [{}] [weighted_ave] {} [waitk] {} [AP] {:.5f} [range] {:.3f}..{:.3f}'.format(count, type_bpe, is_weight_ave, waitk, AP, min(prop[waitk-1]), max(prop[waitk-1]))) 
        AP_list.append(AP)

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
    loerr = [b-min(a) for a,b in zip(prop,AP_list)]
    uperr = [max(a)-b for a,b in zip(prop,AP_list)]
    ax2.errorbar(x, AP_list, yerr=[loerr, uperr],marker='s', ecolor='g', fmt='-o')
    ax2.set_xlabel('Wait_k')
    ax2.set_ylabel('Average Proportion')
    fig2.savefig('corpus_{}.pdf'.format(title_base))
    '''
    loerr = [b-min(a) for a,b in zip(prop,AP_list)]
    uperr = [max(a)-b for a,b in zip(prop,AP_list)]
    return AP_list, loerr, uperr, is_weight_ave, prop



def plot_all(src, tgt_dir, type_dataset, type_bpe):
    AP_list1, loerr, uperr, is_weight_ave, prop = AP_from_file(src, tgt_dir, type_dataset, type_bpe, is_clean=False, is_weight_ave=False)
    AP_list2, _, _, is_weight_ave, _ = AP_from_file(src, tgt_dir, type_dataset, type_bpe, is_clean=False, is_weight_ave=True)

    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
    fig,ax = plt.subplots()
    x = list(range(1,11))
    #ax.errorbar(x, AP_list1, yerr=[loerr, uperr],marker='s', ecolor='g', fmt='-o', label='mean')
    ax.plot(x, AP_list1, 's-',label='mean')
    ax.plot(x, AP_list2, 'ro-',label='corpus_ave')
    ax.violinplot(prop, showmeans=True, showmedians=True)
    ax.set_xlabel('Wait_k')
    ax.set_ylabel('Average Proportion')
    ax.legend(loc='lower right')
    fig.savefig('{}_{}_{}_AP.pdf'.format(tgt_dir, type_dataset, type_bpe))
   
if __name__=="__main__":
    '''
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
    '''
    #get_data('4refs', 'dev')
    #get_data('4refs', 'test')
    get_data('ref2', 'dev')
    #get_data('ref2', 'test')

