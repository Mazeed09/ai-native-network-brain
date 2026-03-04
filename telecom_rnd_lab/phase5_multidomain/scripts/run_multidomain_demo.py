"""Load multi-domain YAML-like templates and print experiment cards without external deps."""

from pathlib import Path


def parse_simple_yaml(path: Path) -> dict:
    data = {"parameters": {}}
    in_parameters = False
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line == "parameters:":
            in_parameters = True
            continue
        if in_parameters and ":" in line:
            key, value = [v.strip() for v in line.split(":", 1)]
            data["parameters"][key] = value
        elif ":" in line:
            key, value = [v.strip() for v in line.split(":", 1)]
            data[key] = value
    return data


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    templates = [
        base / "satellite" / "satellite_template.yaml",
        base / "maritime" / "maritime_mesh_template.yaml",
        base / "urban6g" / "urban_6g_template.yaml",
    ]

    for tpl in templates:
        data = parse_simple_yaml(tpl)
        print(f"[{data['scenario']}] {data['description']}")
        for key, val in data["parameters"].items():
            print(f"  - {key}: {val}")


if __name__ == "__main__":
    main()
