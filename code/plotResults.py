from matplotlib.transforms import BlendedGenericTransform
import matplotlib.pyplot as plt
import numpy as np


x =[1,2,3,4,5]
#Brown
pr =[14.74,12.71,12.52,10.41,9.27,]
pr_rel=[13.6,11.39,10.58,9.0,8.52]
rel=[13.99,13.03,12.52,11.21,10.78]
rand =[28.51,24.05,25.7,19.31,18.05]
#degree =[14.48,13.21,13.01,10.01,9.52]
fig=plt.figure()
plt.subplots_adjust(bottom=0.1, left=.05, right=.99, top=.90, hspace=.35)
ax1 = plt.subplot(211)
p11=plt.plot(x,pr,'rh-',ls ='--',lw=3,label='Page Rank')
p12=plt.plot(x,pr_rel,'bs-',ls ='--',lw=3,label='Page Rank(Relative Coverage)')
p13=plt.plot(x,rel,'g^-',ls ='--',lw=3,label='Relative Coverage')
p14=plt.plot(x,rand,'mD-',ls ='--',lw=3,label='Random')
#plt.ylim((20,6))
#p15=plt.plot(x,degree,'m^-',ls ='--',lw=3,label='Degree')
legend = plt.legend(loc='upper corner', shadow=True,fontsize=20)
plt.setp( ax1.get_xticklabels(), fontsize=25)
plt.setp( ax1.get_yticklabels(), fontsize=25)

pr=[14.8,12.54,10.88,9.22,12.15]
pr_rel =[13.94,11.27,10.65,8.83,12.96]
rel =[14.7,12.86,12.29,9.87,13.36]
rand=[29.5,25.9,23.8,20.25,20.24]
#degree=[15.57,13.62,12.45,10.12,13.36]

ax2 = plt.subplot(212, sharex=ax1,sharey=ax1)

p11=plt.plot(x,pr,'rh-',ls ='--',lw=3,label='Page Rank')
p12=plt.plot(x,pr_rel,'bs-',ls ='--',lw=3,label='Page Rank(Relative Coverage)')
p13=plt.plot(x,rel,'g^-',ls ='--',lw=3,label='Relative Coverage')
p14=plt.plot(x,rand,'mD-',ls ='--',lw=3,label='Random')
#plt.ylim((20,6))
#p15=plt.plot(x,degree,'m^-',ls ='--',lw=3,label='Degree')
#p1=plt.plot(x,pr,'rh-',ls ='--',lw=3,)
#p2=plt.plot(x,pr_rel,'bs-',ls ='--',lw=3)
#p3=plt.plot(x,rel,'g^-',ls ='--',lw=3)
plt.setp( ax2.get_xticklabels(), fontsize=25)
plt.setp( ax2.get_yticklabels(), fontsize=25)
plt.xlabel('Average user level',fontsize=26)
plt.ylabel('% of concepts discovered for grounding',fontsize=26)
# make these tick labels invisible
#ax = fig.add_subplot(312)
#ax.spines['top'].set_color('none')
#ax.spines['bottom'].set_color('none')
#ax.spines['left'].set_color('none')
#ax.spines['right'].set_color('none')
#ax.tick_params( labelcolor='w',top='off', bottom='off', left='off', right='off')
#plt.setp( ax.get_xticklabels(), visible=False)
#plt.setp( ax.get_yticklabels(), visible=False)

#ax.set_xlabel('Average user level')
#ax.set_ylabel('% of discovered concepts for grounding')
ax1.set_title('Brown Corpus',fontsize=26)
ax2.set_title('Gutenberg Corpus',fontsize=26)
labels=('Page Rank','Page Rank(Relative Coverage)','Relative Coverage')
legend = plt.figlegend((p11,p12,p13),labels,loc='upper center',fontsize=18)
#legend = plt.legend((p1,p2,p3),labels,loc='upper center',ncol=5)

plt.show()

#goodness_pr =[1395639,890992,476265,186381,45163]
#goodness_pr_rel =[1674743,952499,589852,289191,45163]
#goodness_rel = [1909233,1227711,642355,275159,18165]

#goodness_pr =[22296,10636 , 8295 ,2948 , 1389]
#goodness_pr_rel = [25353, 10827 , 8480,3464, 1670]
#goodness_rel =[28804 ,15683 ,12760 , 5217 ,2416]

fig=plt.figure()
ax1 = plt.subplot(211)
goodness_pr =[64.19, 47.87, 51.1,40.32, 36.48]
goodness_pr_rel =[78.52, 59.69,60.26, 54.17, 38.02]
goodness_rel = [81.98,68.62, 60.5,57.41, 75.48]
#goodness_degree=[83.77,73.69,71.19,58.41,50.6]
goodness_rand =[45.18,41.05,35.46,40.5,32.65]

p1=plt.plot(x,goodness_pr,'rh-',ls ='--',lw=3,label='Page Rank')
p2=plt.plot(x,goodness_pr_rel,'bs-',ls ='--',lw=3,label='Page Rank(Relative Coverage)')
p3=plt.plot(x,goodness_rel,'g^-',ls ='--',lw=3,label='Relative Coverage')
p4=plt.plot(x,goodness_rand,'mD-',ls ='--',lw=3,label='Random')
#p5=plt.plot(x,goodness_degree,'m^-',ls ='--',lw=3,label='Degree')
legend = plt.legend(loc='upper corner', shadow=True)
plt.setp( ax1.get_xticklabels(), fontsize=25)
plt.setp( ax1.get_yticklabels(), fontsize=25)
#plt.xlabel('Grade of Average users')
#plt.ylabel('Goodness Score')
#plt.legend([p1,p2,p3],['Page Rank','Page Rank(Relative Coverage)' ,'Relative Coverage'])
#legend = plt.legend(loc='upper center', shadow=True)
#plt.show()


ax2 = plt.subplot(212, sharex=ax1,sharey=ax1)
#Gutenberg
"""
pr=[14.8,12.54,10.88,9.22,12.15]
pr_rel =[13.94,11.27,10.65,8.83,12.96]
rel =[14.7,12.86,12.29,9.87,13.36]
plt.figure()
p1=plt.plot(x,pr,'rh-',ls ='--',lw=3,label='Page Rank')
p2=plt.plot(x,pr_rel,'bs-',ls ='--',lw=3,label='Page Rank(Relative Coverage)')
p3=plt.plot(x,rel,'g^-',ls ='--',lw=3,label='Relative Coverage')
"""
#plt.xlabel('Grade of Average users')
#plt.ylabel('Percentage of Concepts to be Grounded')
#legend = plt.legend(loc='upper center', shadow=True)
#plt.show()

#goodness_pr =[1059693, 454796, 289010,46505,46453]
#goodness_pr_rel =[1336350, 553473,399848,193670,46453 ]
#goodness_rel =[1717767, 1014145,712566,171954,19455 ]

goodness_pr =[72.15 , 53.98, 59.67 , 41.52, 46.3]
goodness_pr_rel =[87.12 , 61.16, 62.35, 50.94, 52.18]
goodness_rel =[93.82 , 77.64 , 81.27 ,  68.64,  73.21]
#goodness_degree =[87.31,82.31,83.59,63.87,48.09]
goodness_rand=[52.9,43.77,51.03,36.33,38.86]
p1=plt.plot(x,goodness_pr,'rh-',ls ='--',lw=3,label='Page Rank')
p2=plt.plot(x,goodness_pr_rel,'bs-',ls ='--',lw=3,label='Page Rank(Relative Coverage)')
p3=plt.plot(x,goodness_rel,'g^-',ls ='--',lw=3,label='Relative Coverage')
p4=plt.plot(x,goodness_rand,'mD-',ls ='--',lw=3,label='Random')
#p5=plt.plot(x,goodness_degree,'m^-',ls ='--',lw=3,label='Degree')
plt.setp( ax2.get_xticklabels(), fontsize=25)
plt.setp( ax2.get_yticklabels(), fontsize=25)
plt.xlabel('Average user level',fontsize=26)
plt.ylabel('Goodness Score',fontsize=26)
ax1.set_title('Brown Corpus',fontsize=26)
ax2.set_title('Gutenberg Corpus',fontsize=26)
#plt.xlabel('Grade of Average users')
#plt.ylabel('Goodness Score')
#legend = plt.legend(loc='upper center', shadow=True)
plt.show()


x=[1,2,3,4,5,6,7,8]
word_freq =[1211,1773,2203,2784,3464, 4638, 5106,6111]
plt.figure()
plt.plot(x,word_freq,'b*-')
plt.xlabel('Grade of Average users')
plt.ylabel('No of words in the learning blanket')
plt.show()
