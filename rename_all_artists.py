import os

music_dir = 'music'

artists = {
    "divine": ("hindi", [
        "Baazigar.mp3",
        "Rain.mp3",
        "Hisaab.mp3",
        "100 Million.mp3",
        "3_59.mp3",
        "Aag.mp3",
        "Baazigar.mp3",
        "Bornfire.mp3",
        "Mera Bhai.mp3",
        "Mirchi.mp3",
        "O Sajna.mp3",
        "Rain.mp3",
        "Shehnai.mp3",
        "Straight Ballin.mp3",
        "Flex Kar.mp3",
        "Punya Paap.mp3",
        "Bornfire.mp3",
        # Add more Divine songs here
    ]),
    "arijit": ("hindi", [
        "Kaise Hua.mp3",
        "Apna Bana Le.mp3",
        "Bekhayali.mp3",

        # Add more Arijit songs here
    ]),
    "emiway": ("hindi", [
        "Pain.mp3",
        "Tu Tera Dekhe.mp3",
        
    ]),
    "raftar": ("hindi", [
        "Never Back Down.mp3",
        "RAASHAH.mp",
        "Paagal.mp3",
    ]),
    "krsna": ("hindi", [
        "Been a While.mp3",
        "Blowing Up.mp3",
    ]),
        "hip-hop": ("hindi", [
        
        "11K.mp3",
        "Aaina.mp3",
        "AAJ BHI AAP.mp3",
        "Alvida.mp3",
        "Balenciaga.mp3",
        "Better life.mp3",
        "BLUE EYES.mp3",
        "Changed.mp3",
        "Desi Kalakaar.mp3",
        "Dheere Dheere.mp3",
        "Dope Shope.mp3",
        "Drill Karte.mp3",
        "G-Yaan.mp3",
        "Galat Karam.mp3",
        "God Dam.mp3",
        "Google Pay.mp3",
        "GUESS.mp3",
        "Hola Amigo.mp3",
        "I Guess.mp3",
        "Jealous.mp3",
        "Joota Japani.mp3",
        "K.Y.U.mp3",
        "Kaley Sheshe.mp3",
        "Khatta Flow.mp3",
        "Knock Knock.mp3",
        "Laal Pari.mp3",
        "Lil Bunty.mp3",
        "Luka Chippi.mp3",
        "Lungi Dance.mp3",
        "Machayenge 4.mp3",
        "Millionaire.mp3",
        "Momma.mp3",
        "Narmahat.mp3",
        "NGL.mp3",
        "No Chaina.mp3",
        "ONE THOUSAND MILES.mp3",
        "Pal Pal.mp3",
        "Payal.mp3",
        "RAASHAH.mp3",
        "REGRET.mp3",
        "Sheikh Chilli.mp3",
        "Sitara.mp3",
        "Snake.mp3",
        "Sunny Sunny.mp3",
        "Tere Sang.mp3",
        "Thanks To My Haters.mp3",
        "TRAP PRAA.mp3",
        "TT.Shoutdown.mp3",
        "Wavy.mp3",
        "Woh Raat.mp3",
        "Word to the Wise.mp3",
        "YADON SE.mp3",
        "Yakeen.mp3",
        "You know.mp3",
        "Zindagi.mp3"
    ]),

        "hindi": ("hindi", [
        "Finding Her FM.mp3",
        "Finding Her.mp3",
        "Gulabi Aankhen.mp3",
        "Heeriye.mp3",
        "Iktara.mp3",
        "Ishq Sufiyana.mp3",
        "Jo Tum Mere Ho.mp3",
        "Le Aaunga.mp3",
        "Param Sundari.mp3",
        "Raataan Lambiyan.mp3",
        "Saiyaara (Movie Saiyaara).mp3",
        "Sanu Ek Pal.mp3",
        "Soch Na Sake.mp3",
        "Soniyo.mp3",
        "Tera Ban Jaunga.mp3",
        "Tera Chehra.mp3",
        "Tose Naina.mp3",
        "Tu Har Lamha.mp3",
        "Tu Hi Mera.mp3",
        "Ulala Ulala.mp3"
    ]),

        "english": ("hindi", [
        "Alone, Pt. II.mp3",
        "Attention.mp3",
        "Baby.mp3",
        "Believe.mp3",
        "Calm Down.mp3",
        "Closer.mp3",
        "Die With A Smile.mp3",
        "Dusk Till Dawn.mp3",
        "Faded.mp3",
        "Godzilla.mp3",
        "Intentions.mp3",
        "Let Me Down Slowly.mp3",
        "Let Me Love You.mp3",
        "Lily.mp3",
        "Memories.mp3",
        "People.mp3",
        "Perfect.mp3",
        "Shape of You.mp3",
        "Sorry.mp3",
        "Sunflower.mp3",
        "Thunder.mp3",
        "We Dont Talk Anymore.mp3"
    ]),
    # Add more artists here
}

for artist, (language, song_list) in artists.items():
    for old_name in song_list:
        if old_name.lower().endswith('.mp3'):
            title = old_name[:-4]
            new_name = f"{artist}-{language}-{title}.mp3"
            old_path = os.path.join(music_dir, old_name)
            new_path = os.path.join(music_dir, new_name)
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} -> {new_name}")
            else:
                print(f"File not found: {old_name}")