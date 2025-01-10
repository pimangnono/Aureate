#import pianovis
#video = pianovis.Video((1920,1080), 30, 0.5)

#video.add_midi('resources/samples/output.mid')

#video.export('output.mp4')




# # some video settings
# VIDEO_DPI = 1000
# VIDEO_FPS = 60
# VIDEO_WIDTH = 1080
# VIDEO_HEIGHT = 720

# # the proportion of keyboard display
# KB_RATIO = 0.1

# # speed of the falling tiles (pixels per sec)
# # notice that this value also affect the height of each tile
# TILE_VELOCITY = 500

# import sys
# sys.path.append('')

# from midi2Tiles import pianoTileCreator

# ptc = pianoTileCreator.PianoTileCreator(video_width=VIDEO_WIDTH,
#                                         video_height=VIDEO_HEIGHT,
#                                         video_dpi=VIDEO_DPI,
#                                         video_fps=VIDEO_FPS,
#                                         KB_ratio=KB_RATIO,
#                                         tile_velocity=TILE_VELOCITY,
#                                         key_color="green",
#                                         showKeyVelocity=True)

# ptc.loadMidiFile('resources/samples/output.mid',verbose=True)
# ptc.render('resources/samples/output.mid',verbose=True)

from synthviz import create_video

create_video('resources/samples/hbd.mid') 
