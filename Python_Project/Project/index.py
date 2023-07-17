import pygame
import random

# Initialize pygame
pygame.init()

# Set the frequency and size of the audio
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

#List of MOODS
mood_list=["Happy","Depression","Alone","Love","Beast Mood"]

# List of songs
happy_list=["Sodakku-Mela-Sodakku-MassTamilan.com.mp3","Mersalayitten.mp3","Yaaraiyum-Ivlo-Azhaga-MassTamilan.io.mp3","Aalaporan-Thamizhan-MassTamilan.com.mp3","Marana-Mass-MassTamilan.org.mp3"]
depression_list=["Poi-Vazhva.mp3","Kanave-Kanave-MassTamilan.com.mp3","Yean-Ennai-Pirindhaai-MassTamilan.org.mp3","Ennodu-Nee-Irundhal.mp3","Yennai-Maatrum-Kadhale.mp3"]
alone_list=["En-Iniya-Thanimaye-MassTamilan.io.mp3","Enakenna-Yaarum-Illaye-(Zingaroe-Remix)-MassTamilan.com.mp3","Idhuvum-Kadandhu-Pogum-(The-Healing-Song)-MassTamilan.fm.mp3","Kadhal-Valarthen.mp3","Othayilae.mp3"]
love_list=["Rowdy-Baby-MassTamilan.org.mp3","Otha-Sollaala.mp3","Idhazhin-Oram.mp3","Vilambara-Idaiveli-MassTamilan.com.mp3","Yaanji-MassTamilan.com.mp3"]
beast_list=["Vaathi-Raid-MassTamilan.io.mp3","Danga-Maari-Oodhari.mp3","Mersalayitten.mp3","Vilayadu-Mangatha.mp3","Guleba-Sokama-Sokama-MassTamilan.com.mp3"]

# Display the list of songs to the user
print("Song Catagories")
for i, mood in enumerate(mood_list):
    print(f"{i + 1}. {mood}")

# Prompt the user to enter the song number
mood_number = int(input("What is Your MOOD "))

# Load the selected song
match(mood_number):
    case 1:
        selected_song = pygame.mixer.music.load(random.choice(happy_list))
    case 2:
        selected_song = pygame.mixer.music.load(random.choice(depression_list))
    case 3:
        selected_song = pygame.mixer.music.load(random.choice(alone_list))
    case 4:
        selected_song = pygame.mixer.music.load(random.choice(love_list))
    case 5:
        selected_song = pygame.mixer.music.load(random.choice(beast_list))
    
# Play the selected song
pygame.mixer.music.play()

# Wait until the song finishes playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Cleanup when finished
pygame.mixer.quit()
pygame.quit()
