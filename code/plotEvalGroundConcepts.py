import matplotlib.pyplot as plt
import numpy as np

def per_val(a,b):
  return (float(a)/float(b))*100

N=3
y1 =[per_val(66,578),per_val(52,412),0]
y2 =[per_val(61,578),per_val(44,412),0]
y3 =[per_val(47,578),per_val(40,412),0]
y4 =[per_val(60,578),per_val(46,412),0]
y5 =[per_val(46,578),per_val(41,412),0]

fig = plt.figure()
ax = fig.add_subplot(111)
index = np.arange(N)
width = 0.1
opacity = 0.4
error_config = {'ecolor': '0.3'}
rects1 = ax.bar(index, y1, width, alpha=opacity, color='r',error_kw=error_config, label='Imp')
rects2 = ax.bar(index+width, y2, width, alpha=opacity, color='c',error_kw=error_config, label='Relative Coverage')
rects3 = ax.bar(index+width*2, y3, width, alpha=opacity, color='m',error_kw=error_config, label='Page Rank')
rects4 = ax.bar(index+width*3, y4, width, alpha=opacity, color='b',error_kw=error_config, label='Page Rank with Imp')
rects5 = ax.bar(index+width*4, y5, width, alpha=opacity, color='g',error_kw=error_config, label='Page Rank (Rel Cov)')

#plt.xlabel('Methods')
plt.ylabel('Percentage of Grounded Concepts')
plt.title('Percentage of Grounded Concepts for each methods')
plt.xticks(index+width, ('Brown', 'Gutenberg',''))
plt.legend()
plt.ylim(ymax=20)


def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

plt.tight_layout()
plt.show()

N=3
y1 =[per_val(101,1004),per_val(72,695),0]
y2 =[per_val(112,1004),per_val(79,695),0]

fig = plt.figure()
ax = fig.add_subplot(111)
index = np.arange(N)
width = 0.1
opacity = 0.4
error_config = {'ecolor': '0.3'}
rects1 = ax.bar(index, y1, width, alpha=opacity, color='r',error_kw=error_config, label='Imp')
rects2 = ax.bar(index+width, y2, width, alpha=opacity, color='c',error_kw=error_config, label='Relative Coverage')
#plt.xlabel('Methods')
plt.ylabel('Percentage of Eliminated Dependencies')
plt.title('Percentage of Eliminated Dependences for each methods')
plt.xticks(index+width, ('Brown', 'Gutenberg',''))
plt.legend()
plt.ylim(ymax=20)
plt.tight_layout()
plt.show()
