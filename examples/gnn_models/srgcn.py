from cogdl import experiment
from cogdl.utils import build_args_from_dict

DATASET_REGISTRY = {}


def default_parameter():
    args = {
        "lr": 0.005,
        "max_epoch": 1000,
        "seed": [
            0,
        ],
    }
    return build_args_from_dict(args)


def register_func(name):
    def register_func_name(func):
        DATASET_REGISTRY[name] = func
        return func

    return register_func_name


@register_func("cora")
def cora_config(args):
    args.dropout = 0.6
    return args


@register_func("citeseer")
def citeseer_config(args):
    args.dropout = 0.6
    return args


@register_func("pubmed")
def pubmed_config(args):
    return args


def run(dataset_name):
    args = default_parameter()
    args = DATASET_REGISTRY[dataset_name](args).__dict__
    results = experiment(task="node_classification", dataset=dataset_name, model="srgcn", **args)
    return results


if __name__ == "__main__":
    datasets = ["cora", "citeseer", "pubmed"]
    for x in datasets:
        run(x)
