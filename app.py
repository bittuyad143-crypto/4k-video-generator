import streamlit as st
import asyncio
import edge_tts
from moviepy.editor import ImageClip,
AudioFileClip, ColorClip
import os
st.set_page_config(page_title="4K Video Generator", page_icon="曾", layout="centered")
st.title("曾 AI 4K Video Generator")st.write("Type your script, upload a thumbnail, and generate your 4K video instantly.")
# User Inputs
script_text =st.text_area("I Script
Text","Line 1:Why did the AI cross the road?\nLine 2:To render the 4K video in the cloud!", height=150)
voice_name = st.selectbox("售Select
Voice Actor", ["en-US-
ChristopherNeural", "en-US-GuyNeural", 
"en-US- JennyNeural", "en-GB-
RyanNeural"])
uploaded_file = st.file_uploader("回Upload Thumbnail Image", type=["jpg","jpeg", "png"])
if st.button("分Generate 4K Video",
type="primary")：
if not script_text.strip()：
st.error("Please enter a
script first.")
else:
with st.spinner("Generating
Voiceover...")：
audio_path=
"voiceover.mp3"
async def make_audio()：
communicate =
edge_tts.Communicate(script_text, 
voice_name)
await
communicate.save(audio_path)
asyncio.run(make_audio())
with st.spinner("了Rendering
4K Video...(Takes ~1-2 mins)")：
audio_clip
=
AudioFileclip(audio_path)
duration=
audio_clip.duration
thumbnail_path = None
if uploaded_file is not
None:
thumbnail_path =
f"temp_fuploaded_file.namej"
with
open(thumbnail_path, "wb") as f:
f.write(uploaded_file.getbuffer())
TARGET_WIDTH = 3840
TARGET HEIGHT = 2160
if thumbnail_path and
os.path.exists(thumbnail_path)：
bg_clip = ImageClip(th
umbnail_path).set_duration(duration).r
esize(newsize=(TARGET_WIDTH, 
TARGET_HEIGHT))
else:
bg_clip=
ColorClip(size=(TARGET_WIDTH, TARGET_HEIGHT),color=(0，0，0)).set_duration(duration)
final_video=
bg_clip.set_audio(audio_clip)
output_filename=
"final_output_4k.mp4"
final_video.write_videofile(
output_filename, 
fps=30，
codec="libx264" 
audio_codec="aac", 
bitrate="15000k"
√
st.success("x 4K Video Render
Complete!")
st.video(output_filename)
with open(output_filename,
rb") as file:
st.download_button(
label="A [Download 4K
Video to Phone",
data=file, 
file_name=""final_output_4k.mp4"，
mime="video/mp4"
