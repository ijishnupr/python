color_dict = {'red':'#FF0000',
'green':'#008000',
'black':'#000000',
'white':'#FFFFFF'}
li=list(color_dict.keys())
li.sort()
print(li)
newdict={i: color_dict[i] for i in li}
print(newdict)