import string
def designerPdfViewer(h, word):
    # Write your code here

    alpha = list(string.ascii_lowercase)
    wlist = []
    for i in word:
        wlist.append(alpha.index(i))
        
    hlist = []
    for j in wlist:
        hlist.append(h[j])
    
    rec = max(hlist)*len(word)
    
    return rec