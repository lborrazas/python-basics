import yaml
from factoryv2 import factory, JsonSerializer


class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)


factory.register_format('YAML', YamlSerializer)
