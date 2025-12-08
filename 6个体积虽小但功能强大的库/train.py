# pip install hydra-core 安装需要使用这个命令，如果直接 hydra 会报错
import hydra
from omegaconf import DictConfig

@hydra.main(config_path='config', config_name='trainer/base.yaml', version_base=None)
def train(cfg: DictConfig):
    print(cfg.model.name)
    print(cfg.dataset.name)

if __name__ == '__main__':
    train()