import csv
f=open('songs.csv','r',encoding='utf-8')
s=f.read().split('\n')[1:-1]
data=12+5*30+2023*365

for i in s:
    st=i.split(';')
    if st[-1].split('.')[-1]=='2002'and st[-1].split('.')[1]=='01' and st[-1].split('.')[0]=='01':
        print(f'{st[2]} - {st[1]} - {st[0]}')
    if int(st[-1].split('.')[-1])<2002:
        print(f'{st[2]} - {st[1]} - {st[0]}')
        
with  open('songs.csv','r',encoding='utf-8') as file:
    with open('songs_new.csv','w',encoding='utf-8',newline='') as songsnew:
        s=file.read().split('\n')
        wr=csv.writer(songsnew,delimiter=';')
        wr.writerow(s[0].split(';'))
        s=s[1:]
        for i in s:
            st=i.split(';')
            if st[0]=='0':
                dt=int(st[-1].split('.')[0])+int(st[-1].split('.')[1])*30+int(st[-1].split('.')[2])*365
                streams=abs(data-dt)//(len(st[1])+len(st[2]))*10000
                st[0]=streams
            wr.writerow(st)
                
        