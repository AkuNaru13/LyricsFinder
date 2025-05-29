from dotenv import load_dotenv
import lyricsgenius
import os

load_dotenv()


GENIUS_API_TOKEN = os.getenv("GENIUS_API_TOKEN")


#fetch lyrics
def fetch_lyrics(genius, song_title, artist_name):
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            print(f"\n Lyrics for '{song_title}' by {artist_name}:\n")
            print(song.lyrics)
            return song.lyrics
        else:
            print("Song not found.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# save lyrics
def save_lyrics_to_file(song_title, lyrics):
    filename = f"{song_title.replace(' ', '_')}_lyrics.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(lyrics)
    print(f"\n Lyrics saved to {filename}")


def main():
    genius = lyricsgenius.Genius(
        GENIUS_API_TOKEN,
        skip_non_songs=True,
        excluded_terms=["(Remix)", "(Live)"]
    )

    while True:
        song_title = input("\nEnter song title (or type 'q' to quit): ").strip()
        if song_title.lower() == "q":
            break

        artist_name = input("Enter artist name: ").strip()
        lyrics = fetch_lyrics(genius, song_title, artist_name)

        if lyrics:
            save = input("Do you want to save the lyrics to a file? (y/n): ").strip().lower()
            if save == 'y':
                save_lyrics_to_file(song_title, lyrics)

if __name__ == "__main__":
    main()
