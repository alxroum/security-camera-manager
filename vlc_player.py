import vlc
import time

player = vlc.Instance()

# creating a new media list
media_list = player.media_list_new()

# creating a media player object
media_player = player.media_list_player_new()

# creating a new media
media = player.media_new("")

# adding media to media list
media_list.add_media(media)

# setting media list to the mediaplayer
media_player.set_media_list(media_list)

# playing the media
player.vlm_play_media("death_note")

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)