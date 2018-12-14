'''
10/17/2018 Wed
__author__: Kaibo Liu
plot the BLEU-AP figures
'''
import sys
import re
import os
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
'''
AL
de2en/data/de2en.dev.en.bpe.txt -> de2en/data/de2en.dev.de.bpe.txt
27.616716616716616

de2en/data/de2en.test.en.bpe.txt -> de2en/data/de2en.test.de.bpe.txt
26.565237436606733


transformer
27 --------baseline BLEU on dev --------
 28 b=1  BLEU = 24.23, 57.5/30.5/18.4/11.6 (BP=0.981, ratio=0.981, hyp_len=61858, ref_len=63076)
 29 b=11 BLEU = 25.46, 58.2/31.6/19.5/12.4 (BP=0.986, ratio=0.986, hyp_len=62212, ref_len=63076)
 30
 31 --------baseline BLEU on test--------
 32 b=1  BLEU = 26.63, 59.8/33.0/20.8/13.8 (BP=0.971, ratio=0.971, hyp_len=42815, ref_len=44077)
 33 b=11 BLEU = 27.44, 60.1/33.7/21.4/14.2 (BP=0.980, ratio=0.980, hyp_len=43203, ref_len=44077)

'''

def get_data(type_ref, type_dataset):
    file_bleu_rnn = 'rnn/BLEU_rnn_en2de.txt'         # bleu dev: line 4-12, test line 16-24
    file_bleu_trans = 'trans/BLEU_trans_de2en.txt'   # bleu dev: line 4-13, test line 16-25
    #lineNum = 28 if type_dataset=='dev' else 32 
    pattern = 'BLEU = ([^,]+),'
    #line = open('BLEU.md','r').readlines()[lineNum]
    #round(float(re.findall(pattern, line)[0]), 2)

    #from rnn/BLEU_rnn_de2en.txt line 28(greedy),29(beamsearch) for dev, and line 32(greedy), 33(beamsearch) for test 
    trans_bleu_base1, trans_bleu_base2 = (29.46, 28.46) if type_dataset=='dev' else (30.44, 29.92)  # beam search with size 11
    rnn_bleu_base1, rnn_bleu_base2 = (None, None) if type_dataset=='dev' else (20.82, 19.76) # 23.94 #?
    marker_size = 120
    baseline_AL,base_AL_l, base_AL_r = (27.6167166, 26.7, 28) if type_dataset == 'dev' else (28.58, 28, 29.5)

    lineNum = 1 # 1 if mean, 3 if corpus ave 
    trans_AP = list(map(float, open('trans/de2en_trans_{}_AP.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))[:-1]  # remove the last: wait10
    rnn_AP   = list(map(float, open('rnn/en2de_rnn_{}_AP.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))
    trans_AL = list(map(float, open('trans/de2en_trans_{}_AL.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))[:-1]  # remove the last: wait10
    rnn_AL   = list(map(float, open('rnn/en2de_rnn_{}_AL.txt'.format(type_dataset), 'r').readlines()[lineNum].split()))
    x = range(1,10)

    startLine = 3 if type_dataset=='dev' else 15

    trans_bleu = [float(re.findall(pattern, line)[0]) for line in open(file_bleu_trans,'r').readlines()[startLine: startLine+9]] 
    rnn_bleu   = [float(re.findall(pattern, line)[0]) for line in open(file_bleu_rnn,'r').readlines()[startLine: startLine+9]] 
    
    ylabel = '1-ref BLEU' #if type_ref =='4refs' else '1-ref BLEU'

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')   # to use math style font

    plt.rcParams['font.size'] = 18   # global font size
    #plt.gcf().subplots_adjust(bottom=0.5)
    #plt.rcParams.update({'figure.autolayout': True})

    ############ plot BLEU-AP figs #############
    '''
    fig,ax = plt.subplots()
    ax.margins(0.1)           # Default margin is 0.05, value 0 means fit
    #ax.plot(trans_AP, trans_bleu, 's-', label='transk')#+'_'+type_ref+'_'+type_dataset)
    ax.plot(trans_AP, trans_bleu, 's-', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    ax.plot(rnn_AP, rnn_bleu, 'o-', label='RNN')#+'_'+type_ref+'_'+type_dataset)
    
    #offset_rate = 1.25 if type_ref =='4refs' else 0.7
    offset_rate = 0.7
    for i in range(9):
        ax.annotate('k={}'.format(i+1), xy=(trans_AP[i]-0.05*offset_rate ,trans_bleu[i]+1.7*offset_rate), color='C0', rotation=-45, fontsize=15)
        ax.annotate('k={}'.format(i+1), xy=(rnn_AP[i]-0.05*offset_rate,rnn_bleu[i]+1.7*offset_rate), color='C1', rotation=-45,fontsize=15)
        #if i > 0: ax.annotate('k={}'.format(i+1), xy=(rnn_AP[i],rnn_bleu[i]-0.7*offset_rate), color='C1', rotation=-45,fontsize=15)
    #ax.annotate('k=1', xy=(rnn_AP[0]-0.035*offset_rate,rnn_bleu[0]+1.2*offset_rate), color='C1', rotation=-45,fontsize=15)
    #ax.hlines(bleu_base, ax.axis()[0], ax.axis()[1], 'r', linestyles='dashed', label=    'baseline')
    ax.scatter(1, trans_bleu_base1, marker='*', label='Transformer baseline(beam search)',facecolors='none', edgecolors='r',s=marker_size) # c='r', markerfacecolor='green') 
    ax.scatter(1, trans_bleu_base2, marker='*', label='Transformer baseline(greedy)',facecolors='r', edgecolors='r', s=marker_size) # c='r', markerfacecolor='green') 
    ax.plot([1,1],[trans_bleu_base1,trans_bleu_base2],'r',linewidth=0.5)
    ## ax.scatter(1, rnn_bleu_base, c='r', marker='^', label='RNN baseline') 


    ## add points from Jiatao Gu's paper for test set
    if type_dataset=='test': 
        marker_size_gu = 120 
        p =[  (1.000000, 19.125000,1.000000, 16.836538)
        	, (0.800592, 17.125000,0.807101, 15.884615)
        	, (0.740237, 16.903846,0.741420, 16.000000)
        	, (0.720118, 16.971154,0.718343, 15.855769)
        	, (0.659763, 15.894231,0.653846, 15.740385)
        	, (0.680473, 15.673077,0.681657, 15.096154)
        	, (0.630178, 14.461538,0.622485, 14.115385)]
        conf = [('*','k'),('<','g'),('^','g'),('s','r'),('v','r'),('d','g'),('>','r')]
        for i in range(7):
        	ax.scatter(p[i][0], p[i][1], marker=conf[i][0],facecolors='none', edgecolors=conf[i][1],s=marker_size_gu)#, label='Transformer baseline(beam search)')
        	ax.scatter(p[i][2], p[i][3], marker=conf[i][0],facecolors=conf[i][1], edgecolors=conf[i][1],s=marker_size_gu)#, label='Transformer baseline(beam search)')
        	ax.plot([p[i][0],p[i][2]],[p[i][1],p[i][3]],'k',linewidth=0.5)
        ## blue star in Gu's paper, removed
        # p = (0.601775, 12.701923)
        # m, c = '*','b'
        # ax.scatter(p[0], p[1], marker=m,facecolors=c, edgecolors=c,s=marker_size_gu)#, label='Transformer baseline(beam search)')

    ax.set_xlabel('Average Proportion')
    ax.set_ylabel(ylabel)
    #ax.legend(loc='lower right')
    plt.tight_layout()  # make room for the xlabel
    fig.savefig('de2en_bleu_AP_{}.pdf'.format(type_dataset))
    '''
    fig = plt.figure()

    ax0 = fig.add_axes([0.1, 0.15, 0.7, 0.8]) # left, bottom, width, height (range 0 to 1)
    ax1 = fig.add_axes([0.82, 0.15, 0.1, 0.8]) # inset ax0

    ax0.grid(axis='x', linestyle='--') # vertical lines
    ax1.grid(axis='x', linestyle='--') # vertical lines

    ax0.margins(0.1)           # Default margin is 0.05, value 0 means fit
    ax0.plot(trans_AP, trans_bleu, 's-',color='C0', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    ax0.plot(rnn_AP, rnn_bleu, 'o-', color='C1',label='RNN')#+'_'+type_ref+'_'+type_dataset)
    ax0.scatter(1, trans_bleu_base1, marker='*', label='Transformer baseline(beam search)',facecolors='none', edgecolors='C0',s=marker_size) 
    ax0.scatter(1, trans_bleu_base2, marker='*', label='Transformer baseline(greedy)',facecolors='C0', edgecolors='C0',s=marker_size) 
    ax0.scatter(1, rnn_bleu_base1, marker='*', label='RNN baseline(beam search)',facecolors='none', edgecolors='C1',s=marker_size) 
    ax0.scatter(1, rnn_bleu_base2, marker='*', label='RNN baseline(greedy)',facecolors='C1', edgecolors='C1',s=marker_size) 
    ##ax0.scatter(baseline_AP, rnn_bleu_base, c='r', marker='^', label='RNN baseline') 
    ax1.margins(0.1)           # Default margin is 0.05, value 0 means fit
    ax1.plot(trans_AP, trans_bleu, 's-',color='C0', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    ax1.plot(rnn_AP, rnn_bleu, 'o-', color='C1',label='RNN')#+'_'+type_ref+'_'+type_dataset)
    ax1.scatter(1, trans_bleu_base1, marker='*', label='Transformer baseline(beam search)',facecolors='none', edgecolors='C0',s=marker_size) 
    ax1.scatter(1, trans_bleu_base2, marker='*', label='Transformer baseline(greedy)',facecolors='C0', edgecolors='C0',s=marker_size) 
    ax1.scatter(1, rnn_bleu_base1, marker='*', label='RNN baseline(beam search)',facecolors='none', edgecolors='C1',s=marker_size) 
    ax1.scatter(1, rnn_bleu_base2, marker='*', label='RNN baseline(greedy)',facecolors='C1', edgecolors='C1',s=marker_size) 
    ax1.plot([1,1],[trans_bleu_base1,trans_bleu_base2],'C0',linewidth=0.5)
    ax1.plot([1,1],[rnn_bleu_base1,rnn_bleu_base2],'C1',linewidth=0.5)
    ## ax1.scatter(baseline_AP, rnn_bleu_base, c='r', marker='*', label='RNN baseline') 
    '''
    ## add points from Jiatao Gu's paper for test set
    if type_dataset=='test':
        marker_size_gu = 120
        p =[  (1.000000, 19.125000,1.000000, 16.836538)
                , (0.800592, 17.125000,0.807101, 15.884615)
                , (0.740237, 16.903846,0.741420, 16.000000)
                , (0.720118, 16.971154,0.718343, 15.855769)
                , (0.659763, 15.894231,0.653846, 15.740385)
                , (0.680473, 15.673077,0.681657, 15.096154)
                , (0.630178, 14.461538,0.622485, 14.115385)]
        conf = [('*','k'),('<','g'),('^','g'),('s','r'),('v','r'),('d','g'),('>','r')]
        for i in range(7):
                ax0.scatter(p[i][0], p[i][1], marker=conf[i][0],facecolors='none', edgecolors=conf[i][1],s=marker_size_gu)#, label='Transformer baseline(beam search)    ')
                ax0.scatter(p[i][2], p[i][3], marker=conf[i][0],facecolors=conf[i][1], edgecolors=conf[i][1],s=marker_size_gu)#, label='Transformer baseline(beam sea    rch)')
                ax0.plot([p[i][0],p[i][2]],[p[i][1],p[i][3]],'k',linewidth=0.5)
                ax1.scatter(p[i][0], p[i][1], marker=conf[i][0],facecolors='none', edgecolors=conf[i][1],s=marker_size_gu)#, label='Transformer baseline(beam search)    ')
                ax1.scatter(p[i][2], p[i][3], marker=conf[i][0],facecolors=conf[i][1], edgecolors=conf[i][1],s=marker_size_gu)#, label='Transformer baseline(beam sea    rch)')
                ax1.plot([p[i][0],p[i][2]],[p[i][1],p[i][3]],'k',linewidth=0.5)                
    '''


    ax0.set_xlim(0.54, 0.835)  # most of the data
    ax1.set_xlim(0.979,1.021)  # outliers/baseline only
    #ax0.xaxis.set_ticks([0,2,4,6,8,10])
    ax1.xaxis.set_ticks([1])
    # hide the spines between ax and ax1
    ax0.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax0.yaxis.tick_left()
    ax1.tick_params(labelleft='off')  # don't put tick labels at the left
    ax1.yaxis.tick_right()
 
    offset_rate = 0.7
    #for i in range(9):
    #    ax.annotate('k={}'.format(i+1), xy=(trans_AP[i]-0.05*offset_rate ,trans_bleu[i]+1.7*offset_rate), color='C0', rotation=-45, fontsize=15)
    #    ax.annotate('k={}'.format(i+1), xy=(rnn_AP[i]-0.05*offset_rate,rnn_bleu[i]+1.7*offset_rate), color='C1', rotation=-45,fontsize=15)
 
    for i in range(9):
        ax0.annotate('k={}'.format(i+1), xy=(trans_AP[i]-0.035*offset_rate ,trans_bleu[i]+1.7*offset_rate), color='C0', rotation=-45, fontsize=15)
        ax0.annotate('k={}'.format(i+1), xy=(rnn_AP[i]-0.035*offset_rate,rnn_bleu[i]+1.7*offset_rate), color='C1', rotation=-45,fontsize=15)
    from numpy import arange, cos, pi
    d, c = .01, 1.015  # how big to make the diagonal lines in ax0 coordinates
    cut_y = arange(-3*d, 9*d, d/10)
    cut_x = d * cos(cut_y*pi/d/1.8)
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax0.transAxes, color='k', clip_on=False)
    ax0.plot(c+cut_x, 1-cut_y, **kwargs)        # top-left diagonal
    ax0.plot(c+cut_x, cut_y, **kwargs)        # top-left diagonal
    ''' cross mark for the broken axis
    ax0.plot((c - d, c + d), (1 - d, 1 + d), **kwargs)        # top-left diagonal
    ax0.plot((c - d, c + d), (1 + d, 1 - d), **kwargs)        # top-left diagonal
    ax0.plot((c - d, c + d), (-d, +d), **kwargs)  # bottom-left diagonal
    ax0.plot((c - d, c + d), (+d, -d), **kwargs)  # bottom-left diagonal
    '''
    ax0.set_xlabel('Average Proportion')
    ax0.set_ylabel(ylabel)
    #fig.suptitle('big title')
    #ax0.legend(loc=2, prop={'size': 9})
    plt.tight_layout()  # make room for the xlabel
    fig.savefig('de2en_bleu_AP_{}.pdf'.format(type_dataset))



    ############ plot BLEU-AL figs #############
    fig0 = plt.figure()

    axes = fig0.add_axes([0.1, 0.15, 0.7, 0.8]) # left, bottom, width, height (range 0 to 1)
    axes2 = fig0.add_axes([0.82, 0.15, 0.1, 0.8]) # inset axes

    axes.grid(axis='x', linestyle='--') # vertical lines
    axes2.grid(axis='x', linestyle='--') # vertical lines

    axes.margins(0.1)           # Default margin is 0.05, value 0 means fit
    axes.plot(trans_AL, trans_bleu, 's-',color='C0', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    axes.plot(rnn_AL, rnn_bleu, 'o-', color='C1',label='RNN')#+'_'+type_ref+'_'+type_dataset)
    axes.scatter(baseline_AL, trans_bleu_base1, marker='*', facecolors='none', edgecolors='C0',s=marker_size) 
    axes.scatter(baseline_AL, trans_bleu_base2, marker='*', facecolors='C0', edgecolors='C0',s=marker_size) 
    axes.scatter(baseline_AL, rnn_bleu_base1, marker='*', facecolors='none', edgecolors='C1',s=marker_size) 
    axes.scatter(baseline_AL, rnn_bleu_base2, marker='*', facecolors='C1', edgecolors='C1',s=marker_size) 
    ##axes.scatter(baseline_AL, rnn_bleu_base, c='r', marker='^', label='RNN baseline') 
    axes2.margins(0.1)           # Default margin is 0.05, value 0 means fit
    axes2.plot(trans_AL, trans_bleu, 's-',color='C0', label='Transformer')#+'_'+type_ref+'_'+type_dataset)
    axes2.plot(rnn_AL, rnn_bleu, 'o-', color='C1',label='RNN')#+'_'+type_ref+'_'+type_dataset)
    axes2.scatter(baseline_AL, trans_bleu_base1, marker='*',facecolors='none', edgecolors='C0',s=marker_size)#, label='Transformer baseline(beam search)') 
    axes2.scatter(baseline_AL, trans_bleu_base2, marker='*',facecolors='C0', edgecolors='C0',s=marker_size)#, label='Transformer baseline(greedy)') 
    axes2.scatter(baseline_AL, rnn_bleu_base1, marker='*', facecolors='none', edgecolors='C1',s=marker_size) 
    axes2.scatter(baseline_AL, rnn_bleu_base2, marker='*', facecolors='C1', edgecolors='C1',s=marker_size) 

    axes2.plot([baseline_AL,baseline_AL],[trans_bleu_base1,trans_bleu_base2],'C0',linewidth=0.5)
    axes2.plot([baseline_AL,baseline_AL],[rnn_bleu_base1,rnn_bleu_base2],'C1',linewidth=0.5)
    ## axes2.scatter(baseline_AL, rnn_bleu_base, c='r', marker='*', label='RNN baseline') 
    axes.set_xlim(0, 9.1)  # most of the data
    axes2.set_xlim(base_AL_l, base_AL_r)  # outliers/baseline only
    axes.xaxis.set_ticks([0,2,4,6,8])
    #axes.xaxis.set_ticks([0,5,10])
    # hide the spines between ax and ax2
    axes.spines['right'].set_visible(False)
    axes2.spines['left'].set_visible(False)
    axes.yaxis.tick_left()
    axes2.tick_params(labelleft='off')  # don't put tick labels at the left
    axes2.yaxis.tick_right()

    offset_rate = 1
    for i in range(9):
        #if 4 <= i <= 5:
        #    axes.annotate('k={}'.format(i+1), xy=(trans_AL[i]-0.1*offset_rate ,trans_bleu[i]-0.8*offset_rate), color='C0', rotation=-45, fontsize=15)
        #else:
        axes.annotate('k={}'.format(i+1), xy=(trans_AL[i]-0.8*offset_rate ,trans_bleu[i]+1.1*offset_rate), color='C0', rotation=-45, fontsize=15)
        axes.annotate('k={}'.format(i+1), xy=(rnn_AL[i]-0.8*offset_rate,rnn_bleu[i]+1.1*offset_rate), color='C1', rotation=-45,fontsize=15)
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
    axes.legend(loc=2, prop={'size': 17})
    plt.tight_layout()  # make room for the xlabel
    fig0.savefig('de2en_bleu_AL_{}.pdf'.format(type_dataset))

    '''
    fig0,ax0 = plt.subplots()
    ax0.margins(0.1)           # Default margin is 0.05, value 0 means fit
    #ax0.plot(trans_AL, trans_bleu, 's-', label='transk')#+'_'+type_ref+'_'+type_dataset)
    ax0.plot(trans_AL, trans_bleu, 's-', label=r'trans-$k$')#+'_'+type_ref+'_'+type_dataset)
    ax0.plot(rnn_AL, rnn_bleu, 'o-', label='rnn')#+'_'+type_ref+'_'+type_dataset)
    
    for i in range(10):
        ax0.annotate('k={}'.format(i+1), xy=(trans_AL[i]-0.04*offset_rate ,trans_bleu[i]+1.1*offset_rate), color='C0', rotation=-45, fontsize=15)
        if i > 0: ax0.annotate('k={}'.format(i+1), xy=(rnn_AL[i],rnn_bleu[i]-0.7*offset_rate), color='C1', rotation=-45,fontsize=15)
    ax0.annotate('k=1', xy=(rnn_AL[0]-0.035*offset_rate,rnn_bleu[0]+1.2*offset_rate), color='C1', rotation=-45,fontsize=15)
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
    ax2.plot(x, trans_bleu, 's-', label='Transformer')#+'_'+type_ref+'_'+type_dataset) 
    ax2.plot(x, rnn_bleu, 'o-', label='RNN')#+'_'+type_ref+'_'+type_dataset)
    #ax2.hlines(trans_bleu_base1, ax2.axis()[0], ax2.axis()[1], 'r', linestyles='dashed', label='Transformer baseline(beam search)')
    ax2.hlines(trans_bleu_base1, 1, 10, 'C0', linestyles='dashed', label='Transformer baseline(beam search)')
    ax2.hlines(trans_bleu_base2, 1, 10, 'C0', label='Transformer baseline(greedy)')
    ## ax2.hlines(rnn_bleu_base, ax2.axis()[0], ax2.axis()[1], 'r', linestyles='dashed', label='RNN baseline')
    #ax2.plot(x, [bleu_base]*10, '--', label='baseline'+'_'+type_ref+'_'+type_dataset)
    ax2.set_xlabel(r'$k$')
    ax2.set_ylabel(ylabel)
    ax2.legend(loc='lower right', prop={'size': 12})
    plt.tight_layout()  # make room for the xlabel
    fig2.savefig('de2en_bleu_waitk_{}.pdf'.format(type_dataset))

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
    tgt_dir = 'transk'
    plot_all(src, tgt_dir, type_dataset, type_bpe)
    tgt_dir = 'rnn'
    plot_all(src, tgt_dir, type_dataset, type_bpe)
    '''
    #get_data('1ref', 'dev')
    get_data('1ref', 'test')

