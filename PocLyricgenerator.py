import pygame
pygame.mixer.init()
def play(songname):
    #songname=songname.replace(" ","_")
    pygame.mixer.music.load(f"music/{songname[2:]}.mp3")
    #pygame.mixer.music.load(".mp3")
    pygame.mixer.music.play(loops=0)
l={}
lyrics={}
with open('lyric_name.txt','r',encoding='utf-8') as f:
    for i in f:
        temp = i[:-1].split(",")
        l[temp[0]] = temp[1]
with open('album_lyrics.txt','r') as m:
    for i in m:
        temp = i[:-1].split(",")
        lyrics[temp[0]] = temp[1]

name=input("Enter your name:")
print(f'Welcome to {name} this is lyrical songs you can choose the option')
for j in l.keys():
    print(j,'\n')
def lyrics_gen():
    global lyrics
    global l
    n=[]
    u=[]
    for i in lyrics:
        q=(input("Do you want quit the lyrics (YES|NO):").lower()).strip()
        if q=='yes':
            break
        elif q=='no':
            pass
        else:
            e=lyrics_gen()
            if e is None:
                break
            
        while True:
            select=int(input("If you want any lyric song you can give the number above here:"))
            if select<1 or select>10:
                print("Please enter valid number")
            else:
                u.append(select)
                break
                
        for g in l.keys():
            n.append(g)
        print(f"\n{'-'*10}{n[u[0]-1]}{'-'*10}\n")
        x=lyrics.get(f'{u[0]}')
        print(x)
        play(n[select-1])
        u.pop()
        while True:
            c=(input("Do you want another song press '*' or Do you want quit the song lyrics press 'yes':").lower()).strip()
            pygame.mixer.music.stop()
            if c=='*':
                while True:
                    Another_song=int(input("press the number of the song you want in this lyric song:"))
                    if Another_song<1 or Another_song>10:
                        print("Please enter valid number")
                    else:
                        u.append(Another_song)
                        print(f"\n{'-'*10}{n[u[0]-1]}{'-'*10}\n")
                        y=lyrics.get(f'{u[0]}')
                        print(y)
                        play(n[Another_song-1])
                        break
            if c=='yes':
                break
                print()
        break

lyrics_gen()
