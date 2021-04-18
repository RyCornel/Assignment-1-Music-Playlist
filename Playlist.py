from Song import Song 

class Playlist:
  def __init__(self):
    self.__first_song = None
    self.count = 0


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song
    self.count += 1


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

  def find_song(self, title):
    index_position = 0
    song = self.__first_song
    while song is not None:
        if song.get_title() == title:
            return index_position
        index_position += 1
        song = song.get_next_song()

    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    song = self.__first_song

    if song.get_title() == title:
        self.__first_song = song.get_next_song()
        self.count -= 1
        return

    while song is not None:
        if song.get_next_song() is None:
            break
        elif song.get_next_song().get_title() == title:
            song.set_next_song(song.get.get_next_song().get_next_song())
            self.count -= 1
            break
        else:
            song = song.get_next_song()



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    pass


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    pass

  