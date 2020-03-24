from pytube import YouTube


def getFiles(name):
    """ Get links from a txt file """

    links = [link.strip() for link in open(name, "r")]

    return links


def writeRemaining(name, remaining):
    """ If there are links without download write them into a file """

    with open(name, "w") as f:
        for link in remaining:
            f.write(link + "\n")


def newFile(name):
    """ After do all the links create a new file with 0 links """

    with open(name) as f:
        f.write()


def downloadFiles(folder, links):
    """ Download and save the file in his corresponding folder """
    try:
        if folder == "audios":
            count = 0
            links_len = len(links)
            while count < links_len:
                link = links.pop(0)
                audio = YouTube(link)
                title = audio.title
                audio = audio.streams.filter(only_audio=True)
                audio = audio.first()
                audio.download(f".\\{folder}")
                count += 1
                print(f"{title} descargado")

            newFile(f"{folder}.txt")

        if folder == "videos":
            count = 0
            links_len = len(links)
            while count < links_len:
                link = links.pop(0)
                video = YouTube(link)
                title = video.title
                video = video.streams.first()
                video.download(f".\\{folder}")
                count += 1
                print(f"{title} descargado")

            newFile(f"{folder}.txt")

    except KeyboardInterrupt:
        """ Write the remaining links to the txt """
        writeRemaining(f"{folder}.txt", links)

    except:
        """ Write the remaining links to the txt """
        writeRemaining(f"{folder}.txt", links)

    return print(f"Se descargaron {count} {folder}")


# Main function

if __name__ == "__main__":

    # Get the audio and video links
    audios = getFiles("audios.txt")
    videos = getFiles("videos.txt")

    # Download each file in audios and videos list
    downloadFiles("audios", audios)
    downloadFiles("videos", videos)


# To finish, delete the links used in the txt files
# Convert the audio files to mp3

