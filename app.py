import os
import asyncio
import edge_tts
import streamlit as st
from moviepy.editor import (
ImageClip,
AudioFileClip, 
ColorClip
）
st.set_page_config(
page_title="4K Generator", 
layout="centered"
(
st.title("AI 4K Video Generator")
script_text = st.text_area(
"Script Text",
"Line 1:Hello World\nLine 2：AI
Video Test",
height=120
√
voice_name = st.selectbox(
"Voice Actor", 
["en-US-ChristopherNeural", 
"en-US-GuyNeural", 
en-US- JennyNeural"]
√
uploaded_file = st.file_uploader(
"Upload Thumbnail", 
type=["jpg","jpeg","png"]
√
if st.button("Generate 4K Video", 
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
comm=
edge_tts.Communicate(
script_text,
voice_name
√
await
comm.save(audio_path)
asyncio.run(make_audio())
with st.spinner("Rendering 4K
Video...")：
audio=
AudioFileclip(audio_path)
dur = audio.duration
t_path = None
if uploaded_file is not
None:
t_path=
f"temp_fuploaded_file.namej"
with open(t_path,
"wb") as f:
f.write(uploaded_file.getbuffer())
WH= 3840，2160
if t_path and
os.path.exists(t_path)：
bg= ImageClip(t_path)
.set_duration(dur).resize((W, H))
else:
bg= ColorClip((W, H)，
color=(0，0， 0)).set_duration(dur)
video=
bg.set_audio(audio)
output =
"final_output_4k.mp4"
video.write_videofile(
output, 
fps=30，
codec="libx264", 
audio_codec="aac", 
bitrate="15000k"
√
st.success("4K Video Render
Complete!")
st.video(output)
with open(output, "rb")as f:
st.download_button(
label="Download 4K
Video to Phone", 
data=f, 
file_name=output, 
mime="video/mp4"
)
