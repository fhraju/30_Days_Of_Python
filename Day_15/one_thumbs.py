import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import*
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)

clip = VideoFileClip(source_path)
print(clip.reader.fps) # fps meaning frame per second
print(clip.reader.nframes)
print(clip.duration) # second
duration = clip.duration # clip.reader.duration
max_duration = int(duration) + 1
for i in range(0, max_duration):
    # print(f"frame at {i} seconds")
    frame = clip.get_frame(i)
    # print(frame)     # np.array numpy array # inference
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)

fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps * 1.0)

for i, frame in enumerate(clip.iter_frames()):
    # print(frame)     # np.array numpy array # inference
    fphs = int(fps/2.0)
    if i % fphs ==0:
        current_ms = int((i / fps) * 1000) # turning it miliseconds
        new_img_filepath = os.path.join(thumbnail_per_frame_dir, f"{current_ms}.jpg")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)