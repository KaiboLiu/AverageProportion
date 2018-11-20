'''
10/26/2018 Thu 
__author__: Kaibo Liu
calculate the AP from paper 
src=./testdata/test.txt, from /mnt/scratch/kaibo/proj/fordecoding/test.txt (616 lines)
tgt=./catchup/pred.w<i>.unbpe.txt, from /mnt/scratch/kaibo/proj/fordecoding_catchup/decode_result/pred.w<i>.unbpe.txt (decoded sentences 616 lines)
tgt=./waitk/pred.w<i>.unbpe.txt, from /mnt/scratch/kaibo/proj/fordecoding/decode_result/pred.w<i>.unbpe.txt (decoded sentences 616 lines)
en2de
src=/en2deout_rnn/data/en2de.dev.en.bpe.txt
tst=/en2deout_rnn/dev/w<i>.pred.bpe
'''
import sys
import os
import matplotlib.pyplot as plt


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
    ## continous diagnal
    #s = sum(curr) - x*y/2*(y1/y)**2
    ## step diagnal
    s = sum(curr) - x*y/2*(y1/y)**2 + y1*x/y/2
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
    ## continous diagnal
    #s = sum(curr) - x*y/2*(y1/y)**2
    ## step diagnal
    s = sum(curr) - x*y/2*(y1/y)**2 + y1*x/y/2
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
    

def display_instance(en, de, is_clean, prop, waitk):
    idx = np.argmin(prop[waitk-1])
    print('wait{}_min_prop:{:.3f} @ idx:{}'.format(waitk, prop[waitk-1][idx], idx))
    print('[{} words] {}'.format(*get_n_words(en[idx], is_clean)), end='')
    print('[{} words] {}'.format(*get_n_words(de[idx], is_clean)))

    idx = np.argmax(prop[waitk-1])
    print('wait{}_max_prop:{:.3f} @ idx:{}'.format(waitk, prop[waitk-1][idx], idx))
    print('[{} words] {}'.format(*get_n_words(en[idx], is_clean)), end='')
    print('[{} words] {}'.format(*get_n_words(de[idx], is_clean)))
    #display_instance(en, de, is_clean, prop, idx, disp_k)
    


def APAL_from_file(file_src, dir_tgt, type_dataset, type_bpe, model='trans', is_clean=False, is_weight_ave=False, metric='AP'):
    out_dir = './{}/output/'.format(model)
    title_base = 'en2de_{}_scatter_{}_{}'.format(model, type_dataset, metric)
    k_max = 9 if model=='rnn' else 10
    ave_wait = [[] for i in range(k_max)]
    prop = [[] for i in range(k_max)]   # k_max * count
    APAL_list = []
    len_ys = []
    
    en = open(file_src, 'r').readlines()
    len_x = [get_n_words(x, is_clean)[0] for x in en]
    count = len(len_x)
    for waitk in range(1, k_max+1):
        de = open('{}/w{}.pred.bpe'.format(dir_tgt,waitk), 'r').readlines()
        len_y = [get_n_words(y, is_clean)[0] for y in de]
        len_ys.append(len_y)
        for i, (x, y) in enumerate(zip(len_x, len_y)):
            s = calc_AP(x, y, waitk)[1] if metric=='AP' else calc_AL_waitk(x, y, waitk)
            #s = calc_AP(x, y, waitk)[1] if tgt_dir == 'waitk' else calc_AP_catchup(x, y, waitk)
            #s = calc_AL_wait(x, y, waitk)
            ave_wait[waitk-1].append(s)
            if x < 1 or y < 1: print('{}/w{}.pred.bpe'.format(dir_tgt, waitk), waitk, x, y, i+1)
            ratio = s if metric=='AL' else s/x/y if x > 0 and y > 0 else 0
            #ratio = s/y if y > 0 else 0
            prop[waitk-1].append(ratio)
    
        if is_weight_ave:
            #weights = [x*y for x, y in zip(len_x, len_y)]
            weights = [y for y in len_y] if metric=='AP' else len_x
        else: 
            weights = [1] * count

        f = open(out_dir + title_base + '_wait{}.txt'.format(waitk), 'w')
        for i in range(count):
            f.write('{} {} {} {}\n'.format(len_x[i], len_y[i], ave_wait[waitk-1][i], prop[waitk-1][i]))
        f.close()
        total_weight = sum(weights) 
        APAL = sum(p*w for p,w in zip(prop[waitk-1], weights)) / total_weight
        print('[{} lines] [{}] [weighted_ave] {} [waitk] {} [{}] {:.5f} [range] {:.3f}..{:.3f}'.format(count, type_bpe, is_weight_ave, waitk, metric, APAL, min(prop[waitk-1]), max(prop[waitk-1]))) 
        APAL_list.append(APAL)

    #for disp_k in range(1,11):
    #    display_instance(en, de, is_clean, prop, disp_k)

    
    #draw_k = 3 
    if is_weight_ave and type_dataset == 'dev':
        for draw_k in range(1,k_max+1):
            draw_xy(len_x, len_ys[draw_k-1], prop[draw_k-1], '{}/{}'.format(model, title_base), draw_k)
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
    loerr = [b-min(a) for a,b in zip(prop,APAL_list)]
    uperr = [max(a)-b for a,b in zip(prop,APAL_list)]
    return APAL_list, loerr, uperr, is_weight_ave, prop



    
   
def plot_all(src, tgt_dir, type_dataset, model="trans", type_bpe=True, metric='AP'):
    AP_list1, loerr, uperr, is_weight_ave, prop = APAL_from_file(src, tgt_dir, type_dataset, type_bpe, model, is_clean=False, is_weight_ave=False, metric=metric)
    AP_list2, _, _, is_weight_ave, _ = APAL_from_file(src, tgt_dir, type_dataset, type_bpe, model, is_clean=False, is_weight_ave=True, metric=metric)

    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
    fig,ax = plt.subplots()
    k_max = 9 if model=='rnn' else 10
    x = list(range(1,k_max+1))
    #ax.errorbar(x, AP_list1, yerr=[loerr, uperr],marker='s', ecolor='g', fmt='-o', label='mean')
    ax.plot(x, AP_list1, 's-',label='mean')
    ax.plot(x, AP_list2, 'ro-',label='corpus_ave')
    ax.violinplot(prop, showmeans=True, showmedians=True)
    ax.set_xlabel('Wait_k')
    ax.set_ylabel('Average Proportion')
    ax.legend(loc='lower right')
    fig.savefig('{}/en2de_{}_{}_{}.pdf'.format(model, model, type_dataset, metric))
    f = open('{}/en2de_{}_{}_{}.txt'.format(model, model, type_dataset, metric), 'w')
    print('{}/en2de_{}_{}_{}.txt'.format(model, model, type_dataset, metric))
    f.write('mean\n{}\ncorpus\n{}\n'.format(' '.join(map(str,AP_list1)), ' '.join(map(str,AP_list2))))
    f.close
 
def APAL_from_single_tgt_file(file_src, file_tgt, waitk, is_weight_ave=False, metric='AP'):
    k_max = 10
    ave_wait = [[] for i in range(k_max)]
    prop = [[] for i in range(k_max)]   # k_max * count
    APAL_list = []
    len_ys = []
    
    en = open(file_src, 'r').readlines()
    len_x = [get_n_words(x)[0] for x in en]
    count = len(len_x)
    de = open(file_tgt, 'r').readlines()
    len_y = [get_n_words(y)[0] for y in de]
    len_ys.append(len_y)
    for i, (x, y) in enumerate(zip(len_x, len_y)):
        #s = calc_AP(x, y, waitk)[1] if metric=='AP' else calc_AL_waitk(x, y, waitk)
        s = calc_AP_catchup(x, y, waitk) if metric=='AP' else calc_AL_catchup(x, y, waitk)
        #s = calc_AP(x, y, waitk)[1] if tgt_dir == 'waitk' else calc_AP_catchup(x, y, waitk)
        #s = calc_AL_wait(x, y, waitk)
        ave_wait[waitk-1].append(s)
        if x < 1 or y < 1: print('blank: ', file_tgt , waitk, x, y, i+1)
        ratio = s if metric=='AL' else s/x/y if x > 0 and y > 0 else 0
        #ratio = s/y if y > 0 else 0
        prop[waitk-1].append(ratio)
 
    if is_weight_ave:
        #weights = [x*y for x, y in zip(len_x, len_y)]
        weights = [y for y in len_y] if metric=='AP' else len_x
    else: 
        weights = [1] * count

    total_weight = sum(weights) 
    APAL = sum(p*w for p,w in zip(prop[waitk-1], weights)) / total_weight
    #print('[{} lines] [{}] [weighted_ave] {} [waitk] {} [{}] {:.5f} [range] {:.3f}..{:.3f}'.format(count, type_bpe, is_weight_ave, waitk, metric, APAL, min(prop[waitk-1]), max(prop[waitk-1]))) 
    return APAL

  
if __name__=="__main__":
#    if len(sys.argv) < 2:
#        print('please choose rnn/trans as first argument, AP/AL as second argument, and dev/test as third argument')
#    else:
#        model = sys.argv[1]
#        metric = sys.argv[2] if len(sys.argv) >=3 else 'AP'
#        type_dataset = sys.argv[3] if len(sys.argv) == 4 else 'dev'
#
#        src = './data/en2de.{}.en.bpe.txt'.format(type_dataset)
#        tgt_dir = '{}/{}'.format(model, type_dataset)
#        plot_all(src, tgt_dir, type_dataset, model=model, type_bpe=True, metric=metric)
    if len(sys.argv) < 2: 
        print('please assign the src and tgt files as arguments')
    else:
        file_src = sys.argv[1]
        file_tgt = sys.argv[2]
        waitk = int(sys.argv[3])
        AP = APAL_from_single_tgt_file(file_src, file_tgt, waitk, is_weight_ave=False, metric='AP')
        AL = APAL_from_single_tgt_file(file_src, file_tgt, waitk, is_weight_ave=False, metric='AL')
        print('AP: {:.3f}  AL: {:.3f}'.format(AP, AL), end = '  ')
