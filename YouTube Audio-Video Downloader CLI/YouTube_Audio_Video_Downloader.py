# COMMANDS FOR INSTALLATION OF REQUIRED LIBRARIES
#
# sudo apt install pytube3
# sudo apt install ffmpeg
# pip install ffmpeg-python

import os
import pytube
import ffmpeg


# Function called when both audio and video is to be downloaded (Option 1)
def audio_video_download(yt):  # Takes YouTube object as input

    all_streams = yt.streams.filter(only_video=True, file_extension="mp4")

    print("The list of available media format for given video are:")
    for i in range(len(all_streams)):
        print("#", i + 1, ": ", all_streams[i])

    print()
    stream_num = int(
        input("Select the serial number, in which you want to download the media: ")
    )

    # Invalid entry passed. Hence, choosing video of highest resolution
    if stream_num == "" or 0 > int(stream_num) or int(stream_num) > len(all_streams):
        print("Downloading video of highest resolution")
        video_stream = yt.streams.filter(only_video=True, file_extension="mp4").first()
    else:
        print("Downloading video in selected format")
        video_stream = all_streams[stream_num - 1]
    print()

    # Selecting audio stream of highest quality
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

    audio_stream.download(filename="audio")
    video_stream.download(filename="video")

    # Combining audio-only and video-only files
    audio_input = ffmpeg.input("audio.mp4")
    video_input = ffmpeg.input("video.mp4")
    ffmpeg.output(audio_input, video_input, yt.title + ".mp4").run()

    # Deleting audio and video files used to create final file
    os.remove("audio.mp4")
    os.remove("video.mp4")


# Function called when only audio is to be downloaded (Option 2)
def audio_only_download(yt):  # Takes YouTube object as input
    # Selecting audio stream of highest quality
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
    audio_stream.download(filename=yt.title)


# Function called when only video is to be downloaded (Option 3)
def video_only_download(yt):  # Takes YouTube object as input

    all_streams = yt.streams.filter(only_video=True, file_extension="mp4")

    print("The list of available media format for given video are:")
    for i in range(len(all_streams)):
        print("#", i + 1, ": ", all_streams[i])

    print()
    stream_num = int(
        input("Select the serial number, in which you want to download the media: ")
    )

    # Invalid entry passed. Hence, choosing video of highest resolution
    if stream_num == "" or 0 > int(stream_num) or int(stream_num) > len(all_streams):
        print("Downloading video of highest resolution")
        video_stream = yt.streams.filter(only_video=True, file_extension="mp4").first()
    else:
        print("Downloading video in selected format")
        video_stream = all_streams[stream_num - 1]
    print()

    video_stream.download(filename=yt.title)


if __name__ == "__main__":
    print("=" * 50)
    num_videos = int(input("Enter the number of files to be downloaded: "))
    # path = input('Enter download path (or leave blank to download in current directory): ')

    for _ in range(num_videos):
        print("=" * 50)
        url = input("Enter the URL of video: ")
        yt = pytube.YouTube(url)
        print("=" * 50)

        # Checking presence of audio format
        if len(yt.streams.filter(only_audio=True)) == 0:
            audio_availability = 0
        else:
            audio_availability = 1

        # Checking presence of video format
        if len(yt.streams.filter(only_video=True)) == 0:
            video_availability = 0
        else:
            video_availability = 1

        # Asking choice of download format
        if video_availability == 1 and audio_availability == 1:
            print(
                "Available options (All in .mp4 format only): [1] Audio-Video  [2] Audio Only  [3] Video Only"
            )
            choice = int(input("What do you want to download [1/2/3] (Default = 1) ? "))
            if choice == 2:
                audio_only_download(yt)
            elif choice == 3:
                video_only_download(yt)
            else:
                audio_video_download(yt)

        elif audio_availability == 1:
            print("Only audio format of given video is available for download")
            audio_only_download(yt)

        elif video_availability == 1:
            print("Only video format of given video is available for download")
            video_only_download(yt)

        # Removing forbidden characters from file name
        name = yt.title
        name = (
            name.replace("\ ", "")
            .replace("/", "")
            .replace(":", "")
            .replace("?", "")
            .replace("<", "")
            .replace(">", "")
            .replace("|", "")
        )
        name = name.replace(".", "")
        name += ".mp4"

        # Calculating size of downloaded file
        try:
            filesize = os.stat(name).st_size

            if 2 ** 10 > filesize > 0:
                size = str(filesize) + " B"
            elif 2 ** 20 > filesize > 2 ** 10:
                size = str(round(filesize / 2 ** 10, 2)) + " KB"
            elif filesize > 2 ** 20:
                size = str(round(filesize / 2 ** 20, 2)) + " MB"
            else:
                size = str(round(filesize / 2 ** 30, 2)) + " GB"

            print(name + " has finished downloading")
            print("Filesize: ", size)
            print("=" * 50)
        except:
            print(name + " has finished downloading")
