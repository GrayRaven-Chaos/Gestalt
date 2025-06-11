import streamlit as st
import time
from PIL import Image
import random

# 设置页面标题和布局
st.set_page_config(page_title="🎶简易音乐播放器🎶", layout="wide")
st.title("🎼简易音乐播放器🎼")

# 模拟音乐库
music_library = [
    {
        "歌名": "「极地暗流」- Narwhal",
        "歌手": "Vanguard Sound / Haloweak",
        "播放时长": "5:40",
        "封面链接": "http://p1.music.126.net/XCkyfA8o2Sb5qScfNPVRXA==/109951164626741397.jpg",
        "歌曲链接": "https://music.163.com/song/media/outer/url?id=1416730484.mp3"
    },
    {
        "歌名": "Twilight road 暮光之路",
        "歌手": "呦猫UNEKO / Kausz",
        "播放时长": "4:16",
        "封面链接": "http://p2.music.126.net/1JAQZP59A1nVjjcgq2jLnQ==/109951170480262656.jpg",
        "歌曲链接": "https://music.163.com/song/media/outer/url?id=2675193406.mp3"
    },
    {
        "歌名": "Burning Vow 誓焰",
        "歌手": "芝麻Mochi",
        "播放时长": "4:15",
        "封面链接": "http://p1.music.126.net/YK01DLPApdrjapYOUlbvNQ==/109951169835050330.jpg",
        "歌曲链接": "https://music.163.com/song/media/outer/url?id=2613308858.mp3"
    },
    {
        "歌名": "N.A.M.E",
        "歌手": "Punishing Gray Raven",
        "播放时长": "3:46",
        "封面链接": "http://p1.music.126.net/cnYoY9qtf8qYZkyZUPS7QA==/109951166960334103.jpg",
        "歌曲链接": "https://music.163.com/song/media/outer/url?id=1913688116.mp3"
    }
]

# 初始化会话状态
if 'current_song_index' not in st.session_state:
    st.session_state.current_song_index = 0
if 'is_playing' not in st.session_state:
    st.session_state.is_playing = False
if 'progress' not in st.session_state:
    st.session_state.progress = 0

# 获取当前歌曲信息
def get_current_song():
    return music_library[st.session_state.current_song_index]

# 播放控制函数
def play_pause():
    st.session_state.is_playing = not st.session_state.is_playing

def next_song():
    st.session_state.current_song_index = (st.session_state.current_song_index + 1) % len(music_library)
    st.session_state.is_playing = True
    st.session_state.progress = 0

def prev_song():
    st.session_state.current_song_index = (st.session_state.current_song_index - 1) % len(music_library)
    st.session_state.is_playing = True
    st.session_state.progress = 0



# 分割线
st.markdown("---")

# 当前歌曲信息
current_song = get_current_song()
col1, col2 = st.columns([1, 3])

with col1:
    # 专辑封面
    st.image(current_song["封面链接"], width=150, caption="专辑封面")

with col2:
    st.subheader(current_song["歌名"])
    st.markdown(f"**歌手**: {current_song['歌手']}")
    st.markdown(f"**时长**: {current_song['播放时长']}")

# 播放控制按钮
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.button("上一首", on_click=prev_song)

with col2:
    if st.session_state.is_playing:
        st.button("暂停", on_click=play_pause)
    else:
        st.button("播放", on_click=play_pause)

with col3:
    st.button("下一首", on_click=next_song)

# 播放进度显示
progress_bar = st.progress(st.session_state.progress)
if st.session_state.is_playing:
    for i in range(100):
        time.sleep(0.1)  # 模拟播放进度
        st.session_state.progress = i + 1
        progress_bar.progress(st.session_state.progress)
        if not st.session_state.is_playing:
            break
    if st.session_state.progress >= 100:
        next_song()

# 音频播放器
st.audio(current_song["歌曲链接"], format="audio/mp3")


# 歌曲列表
st.markdown("## 歌曲列表")
for i, song in enumerate(music_library):
    if st.button(f"{song['歌名']} - {song['歌手']} ({song['播放时长']})", key=f"song_{i}"):
        st.session_state.current_song_index = i
        st.session_state.is_playing = True
        st.session_state.progress = 0
        st.experimental_rerun()
