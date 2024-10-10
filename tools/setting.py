import yaml
import argparse


class ModelConfig:

    def __init__(self) -> None:
        self.config = self.config_read()
        self.llm = self.config['llm']
        self.telegram = self.config['telegram']

    def config_read(self):
        with open('/opt/configs/setting.yaml', 'r') as file:
            config = yaml.safe_load(file)
        return config


if __name__ == '__main__':
    config = ModelConfig()
