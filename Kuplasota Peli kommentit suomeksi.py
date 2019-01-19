"""Seuraavassa projektissa hyödynnetään kaikkia opittuja tietoja pelin tekemiseen
Pelin kulkua ohjaavat seuraavat pääsäännöt: 1. Pelaaja ohjaa sukellusvenettä
2. Nuolinäppäimet siirtävät sukellusvenettä, 3. Kuplien puhkomisestä saa pisteitä
4. Ajastin saa alussa arvon 30 sek. 1000 pisteellä saa lisäaikaa
5. Peli päättyy kun aika loppuu
Aloita luomalla näkymä. Tämä luo ikkunan peliä varten ja sukellusveneen jota pelaaja ohjaa:"""
from tkinter import*
HEIGHT = 500#Nämä määrittävät
WIDTH = 800#pelissä käytettävän ikkunan koon
window = Tk()
window.title('Kuplasota')#Tämä antaa pelille iskevän nimen
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')#Muodostaa taustan ja sen värin, jolle peli piirretään.
c.pack()
"""Tässä pelissä sukellusvenettä esittää yksinkertainen kuvio. Käytä sen tekemiseen Tkinter-modulin piirtofunktiota.
Sukellusvenettä esittää kolmio ympyrän sisällä:"""
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')#piirtää sukellusvenettä esittävän punaisen kolmion
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')#piirtää punaisen ympyrän ääriviivaksi
SHIP_R = 15#Sukellusveneen säde (koko)
MID_X = WIDTH / 2#Muuttujat MID_X ja MID_Y tarkoittavat
MID_Y = HEIGHT / 2#näytön keskipisteen koordinaatteja
c.move(ship_id, MID_X, MID_Y)#Siirtää sukellusveneen molemmat
c.move(ship_id2, MID_X, MID_Y)#osat näytön keskipisteeseen
"""Seuraava vaihe ohjelmaa tehtäessä on kirjoittaa lauseet, jotka siirtävät sukellusvenettä nuolinäppäimillä
Alla olevat lauseet määrittelevät funktion, jota sanotaan "tapahtumakäsittelijäksi".
Se tarkistaa mitä näppäintä on painettu, ja siirtää sukellusvenettä vastaavasti
Kirjoita seuraavat lauseet, joista moudostuu "move_ship"-funktio.
Tämä funktio siirtää sukellusvenettä oikeaan suuntaan, kun kohdistinpainiketta on painettu:"""
SHIP_SPD = 10#Sukellusvene siirtyy tämän matkan näppäimen painamisen jälkeen.
def move_ship(event):#Tämä funktio siirtää sukellusvenettä oikeaan suuntaan, kun kohdistinpainiketta on painettu
    if event.keysym == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)#Siirtävät sukellusveneen kahta osaa ylöspäin,
        c.move(ship_id2, 0, -SHIP_SPD)#kun ylös-näppäintä on painettu.
    elif event.keysym == 'Down':
        c.move(ship_id, 0, SHIP_SPD)#Siirtävät sukellusveneen kahta osaa alaspäin,
        c.move(ship_id2, 0, SHIP_SPD)#kun alas-näppäintä on painettu.
    elif event.keysym == 'Left':
        c.move(ship_id, -SHIP_SPD, 0)#Siirtävät sukellusveneen kahta osaa vasemmalle,
        c.move(ship_id2, -SHIP_SPD, 0)#kun vasemmalle osoittavaa nuolinäppäintä on painettu.
    elif event.keysym == 'Right':
        c.move(ship_id, SHIP_SPD, 0)#Siirtävät sukellusveneen kahta osaa oikealle,
        c.move(ship_id2, SHIP_SPD, 0)#kun oikealle osoittavaa nuolinäppäintä on painettu.
c.bind_all('<Key>', move_ship)#Käskee Pythonia suorittamaan funktion
"""Luo kuplia, joita pelaajan pitää poksautella.
Kukin kupla on erikokoinen ja liikkuu eri nopeudella kuin muut.
Jokaisella kuplalla pitää olla tunnusnumero, jotta ohjelma osaa erottaa kuplat toisistaan.
Lisäksi jokaisella kuplalla on oma koko ja nopeus:"""
from random import randint
bub_id = list()#Luovat 3 tyhjää listaa, joihin tallennetaan kunkin kuplan tunnusnro,
bub_r = list()#  säde ja 
bub_speed = list()# nopeus.
MIN_BUB_R = 10# Asettavat kuplien minimisäteeksi 10
MAX_BUB_R = 30# ja maksimisäteeksi 30.
MAX_BUB_SPD = 10
GAP = 100
def create_bubble():
    x = WIDTH + GAP# Asettevat kuplan
    y = randint(0, HEIGHT)# sijainnin piirtoalueella.
    r = randint(MIN_BUB_R, MAX_BUB_R)# Valitsee kuplalle satunnaisen koon ylä- ja alarajan.
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')#Muodostaa kuplakuvion
    bub_id.append(id1)#Lisäävät kuplan tunnusnron,
    bub_r.append(r)# säteen ja 
    bub_speed.append(randint(1, MAX_BUB_SPD))#nopeuden kaikkiin kolmeen listaan jotka tyhjinä yllä.
"""Ohjelmassa on nyt listat, jotka sisältävät tunnusnron, sekä satunnaisesti valitut koot ja nopeudet.
Seuraava vaihe on kirjoittaa lauseet, jotka saavat kuplat liikkumaan näytöllä."""
def move_bubbles():#Tämä funktio käy läpi kuplalistan ja siirtää kutakin kuplaa vuorollaan.
    for i in range(len(bub_id)):#Käy läpi listan kaikki kuplat
        c.move(bub_id[i], -bub_speed[i], 0)#Siirtää kuplaa näytöllä nopeuden mukaisesti.
"""Seuraavaksi luodaan hyödyllinen funktio, jolla selvitetään kuplan sijainti tunnusnumeron perusteella.
Seuraavat lauseet pitää lisätä ohjelmaan heti vaiheessa 5 kirjoitetun funktion jälkeen (move_bubbles)."""
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2# Laskee kuplan keskipisteen x-koordinaatin.
    y = (pos[1] + pos[3])/2# Laskee kuplan keskipisteen y-koordinaatin.
    return x, y# palauttaa sisäisesti funktion x ja y muuttujat
"""Pelaaja saa pisteitä onnistuessaan kuplanpuhkaisussa, joten ohjelman on osattava hävittää kuplia näytöltä.
Seuraavat funktiot hoitavat tämän tehtävän. Se tuhoaa kuplan kaikista listoista ja piirtoalueelta.
Nämä lauseet pitää lisätä suoraan edellisen funktion jälkeen."""
def del_bubble(i):#Tämä funktio poistaa kuplan, jonka tunnusnumero on "i".
    del bub_r[i]# Poistavat kuplan säde- ja
    del bub_speed[i]# nopeuslistoista.
    c.delete(bub_id[i])#Poistaa kuplan piirtoalueelta.
    del bub_id[i]# Poistaa kuplan tunnusnumerolistasta.
#Seuraava funktio tuhoaa näytön ulkopuolelle ajautuneet kuplat:
def clean_up_bubs():#ALLA: Tämä silmukka käy kuplalistan takaperin läpi, jotta kuplia poistettaessa
    for i in range(len(bub_id)-1, -1, -1):# ei aiheudu virheitä.
        x, y = get_coords(bub_id[i])#Selvittää kuplan sijainnin.
        if x < -GAP:
            del_bubble(i)#Jos kupla on näytön ulkopuolella, se poistetaan. Muuten se hidastaa peliä.
#Tämä funktio laskee kahden kohteen välisen etäisyyden:
from math import sqrt#Lataa math-modulista sqrt-funktion.
def distance(id1, id2):
    x1, y1 = get_coords(id1)#Lukee ensimmäisen kohteen sijainnin.
    x2, y2 = get_coords(id2)#Lukee toisen kohteen sijainnin.
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)#Palauttaa kohteidenväalisen etäisyyden.
"""Pelaaja kerää pisteitä puhkomalla kuplia. Isoista ja nopeista kuplista saa eniten pisteitä.
Seuraava funktio laskee säteen perusteella milloin kupla puhkeaa.
Kun sukellusvene ja kupla törmäävät, ohjelman pitää puhkaista kupla ja päivittää pistemäärä"""
def collision():
    points = 0#Tämä muuttuja pitää kirjaa saaduista pisteistä (lähtö nollasta ja huomaa lopuksi palautus).
    for bub in range(len(bub_id)-1, -1, -1):#Tämä silmukka käy koko kuplalistan läpi takaperin, jottei tule virheitä.
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):#Tarkistaa että törmäys on tapahtunut.
            points += (bub_r[bub] + bub_speed[bub])#Laskee kuplan arvon pisteinä ja lisää sen arvon muuttujaan-points.
            del_bubble(bub)#poistaa kuplan
    return points#Palauttaa pistemäärään.
def show_score(score):
    c.itemconfig(score_text, text=str(score))#Näyttää pistemäärän
def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))#Näyttää jäljelläolevan ajan.
time_text = c.create_text(50, 50, fill='white' )# Asettavat pistemäärän ja 
score_text = c.create_text(150, 50, fill='white' )# jäljellä olevan ajan.
#Tämä on pelin pääsilmukka, joka toistuu yhä uudelleen peliä pelattaessa:
from time import sleep, time#Tuo tarvittavat funktiot Time-modulista.
BUB_CHANCE = 10
TIME_LIMIT = 100
#Aloittaa pelin käyttäen aikarajana 30 sekuntia.
BONUS_SCORE = 1000#Määrää, milloin tulee bonusaika, kun pelaaja on saanut 1000 pistettä.
score = 0#Muuttuja-score määritetty alla. Tämä lisäys nollaa pistemäärän kun peli alkaa.
bonus = 0
end = time() + TIME_LIMIT#Tallentaa päättymisajan muuttujaan "end".
while time() < end:#PELIN PÄÄSILMUKKA. while-looppi toistaa pääsilmukkaa kunnes peli päättyy.
    if randint(1, BUB_CHANCE) == 1:#Jos satunnaisluku on 1,
        create_bubble()#  ohjelma luo uuden kuplan (keskimäärin joka 10s kerta ettei kuplia tule liikaa.
    move_bubbles()# kutsuu funktiota move_bubbles.
    clean_up_bubs()#Funktio, joka poistaa näytön ulkopuolelle joutuneet kuplat (ks. määritys alla).
    score += collision()#Lisää puhkaistun kuplan arvon kokonaispistemäärään.
    if (int(score / BONUS_SCORE)) > bonus:#Laskee milloin pelaaja saa bonusaikaa
        bonus += 1
        end += TIME_LIMIT
    show_score(score)#Tämä tuli print(scoren) tilalle. Näyttää pistemäärän peli-ikkunassa.
    show_time(int(end - time()))# Näyttää jäljelläolevan ajan.
    window.update()#Päivittää ikkunan piirtämällä siirtyneet kuplat uudelleen.
    sleep(0.10)# Hidastaapeliä, jotta se ei ole liian nopea pelattavaksi
"""Pelin pääosat ovat nyt valmiit. Sinun tarvitsee vain lisätä viimeistely eli näyttää pelaajan pistemäärä
 ja asettaa ajastin, joka laskee alaspäin pelin päättymiseen asti.
Seuraavat lauseet käskevät näyttämään pelaajan pistemäärän ja jäljellä olevan peliajan:"""
c.create_text(50, 30, text='AIKA', fill='white' )#Luovat otsikot "AIKA" ja 
c.create_text(150, 30, text='PISTEET', fill='white' )# "PISTEET", jotta pelaaja tietää, mitä luvut tarkoittavat.
"""Määritä aikaraja ja pistemäärä, jonka saavuttamalla saa bonusaikaa ja laske pelin päättymisaika.
Näiden lauseiden pitää olla juuri ennen pääsilmukkaa. ks. kohta "from time import..."
Lisätään vielä loppuun lauseet, jotka näyttävät että peli on ohi sekä loppupisteen ja sekä saatu bonusaika:"""
c.create_text(MID_X, MID_Y, \
    text='PELI OHI', fill='white', font=('Helvetica',30))
c.create_text(MID_X, MID_Y + 30, \
    text='Pisteet: '+str(score), fill='white')#Ilmoittaa pistemäärän
c.create_text(MID_X, MID_Y + 45, \
    text='Bonusaika: '+str(bonus*TIME_LIMIT), fill='white')#Näyttää paljonko bonusaikaa pelaaja sai.
