"""
CLI to prepare the datasets for training
"""
from pathlib import Path

import fire
import transformers

from axolotl.cli import (
    check_accelerate_default_config,
    load_cfg,
    load_datasets,
    print_axolotl_text_art,
)
from axolotl.common.cli import TrainerCliArgs


def do_cli(config: Path = Path("examples/"), **kwargs):
    # pylint: disable=duplicate-code
    print_axolotl_text_art()
    check_accelerate_default_config()
    parser = transformers.HfArgumentParser((TrainerCliArgs))
    parsed_cli_args, _ = parser.parse_args_into_dataclasses(
        return_remaining_strings=True
    )
    parsed_cli_args.prepare_ds_only = True
    parsed_cfg = load_cfg(config, **kwargs)

    load_datasets(cfg=parsed_cfg, cli_args=parsed_cli_args)


if __name__ == "__main__":
    fire.Fire(do_cli)