from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("ABC.mp4", 48, 120, targetname="ABC2.mp4")
