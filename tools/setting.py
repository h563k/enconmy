import yaml
import argparse


class ModelConfig:

    def __init__(self) -> None:
        self.config = self.config_read()
        self.llm = self.config['llm']
        self.telegram = self.config['telegram']
        self.model = self.config['model']

    def config_read(self):
        with open('/opt/configs/setting.yaml', 'r') as file:
            config = yaml.safe_load(file)
        return config

    @property
    def qwen(self):
        return self.config_read()['llm']['qwen']

    @property
    def kimi(self):
        return self.config_read()['llm']['kimi']

    @property
    def glm(self):
        return self.config_read()['llm']['glm']

    @property
    def spark(self):
        return self.config_read()['llm']['spark']


if __name__ == '__main__':
    config = ModelConfig()
