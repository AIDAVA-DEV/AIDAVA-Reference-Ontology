from changes_applier import ChangesApplier
from pathlib import Path

applier = ChangesApplier(Path("base_sphn_rdf_schema.ttl"), Path("changes"))

graph = applier.apply()

graph.serialize("schema.ttl", format="turtle")
