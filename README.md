# 🎵 Genius Lyrics Fetcher

This is a simple Python CLI tool to fetch and optionally save song lyrics using the [Genius API](https://genius.com/developers). It allows users to search for a song by title and artist, displays the lyrics in the terminal, and provides the option to save them as a `.txt` file.

---

## 🔧 Features

- Search and fetch lyrics by song title and artist.
- Display lyrics in the terminal.
- Option to save lyrics to a text file.
- Skips non-song results like live versions and remixes.

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/genius-lyrics-fetcher.git
cd genius-lyrics-fetcher

### 2. Install Dependencies
Ensure you have Python 3 installed. Then, install required packages:

pip install lyricsgenius python-dotenv

### 3. Get Your Genius API Token

Go to: Genius API Client Management
Create a new API client.
Copy the Access Token.

### 4. 4. Create a .env File

Create a .env file in the project root with the following:

GENIUS_API_TOKEN=your_genius_api_token_here


### 5. Run the script:

**main.py**

Follow the prompts:
Enter the song title.
Enter the artist name.
View the lyrics in the terminal.
Choose whether to save them to a file.

**Output**

Saved lyrics will be stored in the project directory with the file name format:
<Song_Title>_lyrics.txt


**Example**
Enter song title (or type 'q' to quit): Shape of You
Enter artist name: Ed Sheeran

Lyrics for 'Shape of You' by Ed Sheeran:

[Verse 1]
The club isn't the best place to find a lover...
...

Do you want to save the lyrics to a file? (y/n): y

Lyrics saved to Shape_of_You_lyrics.txt


**License**
This project is licensed under the MIT License.

**Acknowledgements**

Genius API
lyricsgenius
python-dotenv
