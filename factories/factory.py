import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


def _serialize_to_json(song):  # Concrete Implementations
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')


def _get_serializer(format):  # Factory
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)


class SongSerializer:
    def serialize(self, song, format):
        serializer = _get_serializer(format)
        return serializer(song)


if __name__ == '__main__':
    song = Song('1', 'idiota', 'morat | danna paola')
    serializer = SongSerializer()

    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
