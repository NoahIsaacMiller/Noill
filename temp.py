from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from PIL import Image  # 用于处理图片
import io, os, json


class MP3Metadata:
    def __init__(self, title, artist, album, artwork_path, file_path, duration):
        self.file_path = file_path
        self.title = title
        self.artist = artist
        self.album = album
        self.artwork_path = artwork_path
        self.duration = duration
    
    def toDict(self):
        return {
            "title": self.title,
            "author": self.artist,
            "coverUrl": self.artwork_path,
            "musicUrl": self.file_path,
            "duration": self.duration
        }

        



def get_mp3_metadata(file_path):
    try:
        audio = MP3(file_path)
        title = audio.get('TIT2').text[0] if 'TIT2' in audio else None
        artist = audio.get('TPE1').text[0] if 'TPE1' in audio else None
        album = audio.get('TALB').text[0] if 'TALB' in audio else None
        # 时长
        duration = audio.info.length
        artwork = None

        if 'APIC:' in audio:
            artwork_data = audio['APIC:'].data
            artwork = Image.open(io.BytesIO(artwork_data))

        return artist, title, album, artwork, duration

    except ID3NoHeaderError:
        print(f"文件 '{file_path}' 没有ID3标签。")
        return None, None, None, None
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到。")
        return None, None, None, None
    except Exception as e:
        print(f"处理文件 '{file_path}' 时发生错误: {e}")
        return None, None, None, None

def tackle(mp3_file):
    mp3_file = "./public/music/" + mp3_file  # 替换为你的MP3文件路径
    artist, title, album, artwork, duration = get_mp3_metadata(mp3_file)

    if artist:
        print(f"作者: {artist}")
    if title:
        print(f"标题: {title}")
    if album:
        print(f"专辑: {album}")
    
    if duration:
        print(f"时长: {duration} 秒")

    if artwork:
        # artwork.show()  # 显示专辑封面图片
        # 你也可以将图片保存到本地

        file_name = f"{title} {f'({album})' if '(' not in album and album else ''} - {artist}"
        artwork.save(f"./public/music/cover/{file_name}.png")
    print("--------------------")
    return MP3Metadata(title, artist, album, f"/music/cover/{file_name}.png", mp3_file[8:], duration).toDict()

if __name__ == "__main__":
    mp3 = []
    music_info = {
        "data": mp3,
        "total": len(mp3)
    }
    for file in os.listdir("./public/music"):
        if file.endswith(".mp3"):
            mp3.append(tackle(file))
    with open("./public/music/music-info.json", "w",encoding="utf8") as f:

        json.dump(music_info, f,ensure_ascii=False, indent=4)