from pathlib import Path
from rdflib import Graph
import importlib.util
from tqdm import tqdm


class ChangesApplier:
    def __init__(self, graphPath: Path, changesPath: Path):
        self.graphPath = graphPath
        self.changeFolders = [
            f
            for f in changesPath.glob("**/*")
            if f.is_dir() and f.name.split("/")[-1].isdigit()
        ]
        self.changeFolders.sort(key=lambda x: int(x.name.split("/")[-1]))
        self.loadApplyFunctions()

    def loadApplyFunctions(self):
        self.applyFunctions = []
        for folder in self.changeFolders:
            applyPath = folder / "apply.py"
            if applyPath.exists():
                spec = importlib.util.spec_from_file_location(
                    "apply", applyPath
                )
                if spec is None:
                    raise Exception(f"Missing apply function in {folder}")
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)  # type: ignore
                if not hasattr(module, "apply"):
                    raise Exception(f"Missing apply function in {folder}")

                self.applyFunctions.append(
                    {"folder": folder, "apply": module.apply}
                )
            else:
                raise Exception(f"Missing apply.py in {folder}")

    def apply(self):
        graph = Graph()
        graph.parse(self.graphPath)
        p_bar = tqdm(
            self.applyFunctions, desc="Applying changes", unit="change"
        )
        for applyFunction in p_bar:
            p_bar.set_description(
                f"Applying changes from {applyFunction['folder']}"
            )
            applyFunction["apply"](graph)
        return graph
