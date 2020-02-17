import matplotlib.pyplot as plt

def hello():
    print('Hello, world!')

    
y = [
     2.5,2.5,
     3.0,3.0,3.0,3.0,3.0,
     3.5,3.5,3.5,3.5,3.5,3.5,3.5,
     4.0,4.0,4.0,4.0,4.0,4.0,4.0,
     4.5,4.5,4.5,4.5,4.5,4.5,4.5,
     5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,
     5.5,5.5,5.5,5.5,5.5,5.5,5.5,
     6.0,6.0,6.0,6.0,6.0,
     6.5,6.5
    ]
x = [ 
       11,13,
       6, 8,10,12,14,
       5, 7, 9,11,13,15,17,
       6, 8,10,12,14,16,18,
       5, 7, 9,11,13,15,17,
       4, 6, 8,10,12,14,16,18,
       5, 7, 9,11,13,15,17,
       8,10,12,14,16, 
       9,11
    ]
N = [
       56, 57, 
      53, 32, 33, 34, 35, 
      52, 31, 16, 17, 18, 36, 60, 
      30, 15,  6,  7, 19, 37, 61,
      29, 14,  5,  1,  2,  8, 20,
      49, 28, 13,  4,  3,  9, 21, 39,
      48, 27, 12, 11, 10, 22, 40,
      26, 25, 24, 23, 41, 
      45, 44
    ]
C = [ 127 for i in range(len(N))]
xmin = min(x)-3
xmax = max(x)+3
ymin = min(y)-1
ymax = max(y)+1
#print(len(N))


def plot_events(data, events):
    ysize = 3.3 * ((len(events) + 4) // 5)

    plt.rcParams['axes.linewidth'] = 0.0
    plt.rcParams['font.size'] = 12

    fig, axn = plt.subplots( (len(events) + 4) // 5, 5, sharex=True, sharey=True, figsize=(18,ysize))
    for i in range(len(events)):
        event = events[i]
        axn[i//5][i%5].axis([xmin, xmax, ymin, ymax])
        axn[i//5][i%5].axes.get_xaxis().set_visible(False)
        axn[i//5][i%5].axes.get_yaxis().set_visible(False)

        axn[i//5][i%5].set_title(str(events[i]))

        suma = data[data.event == event].values[0][13:13+61]
        amp = []
        for ch in range(len(N)):
            amp.append( suma[N[ch]-1])

        #hb = axn[i].hexbin(x, y, C=np.log10(amp),gridsize=(10,6), 
        hb = axn[i//5][i%5].hexbin(x, y, C=amp, gridsize=8, 
                            #cmap="gist_yarg", 
                            edgecolor='gray',                
                            #cbar_ax  = None if i else cbar_ax,
                            #cbar_kws = None if i else cbar_kws
                    )   
