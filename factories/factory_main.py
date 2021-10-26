import songs
import factoryv2 as factory
import yaml_serializer  # I believe this is bad practice.

if __name__ == '__main__':
    song = songs.Song('1', 'big bang', 'cami')
    serializer = factory.ObjectSerializer()

    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))