"""Localiza e baixa arquivos publicados nas páginas oficiais do INEP.

Uso:
    python scripts/download_fontes.py

Os arquivos são salvos em data/raw e não devem ser versionados.
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urljoin

import requests

SOURCES = {
    "censo_escolar": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar",
    "taxas_rendimento": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar",
}
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def links_from_page(url: str) -> list[str]:
    response = requests.get(url, timeout=60, headers={"User-Agent": "Educadata/1.0"})
    response.raise_for_status()
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', response.text, flags=re.I)
    return [urljoin(url, href) for href in hrefs if any(x in href.lower() for x in (".zip", ".csv", ".xlsx", ".ods"))]


def download(url: str) -> Path:
    filename = url.split("/")[-1].split("?")[0] or "arquivo_oficial"
    destination = RAW / filename
    with requests.get(url, stream=True, timeout=120, headers={"User-Agent": "Educadata/1.0"}) as response:
        response.raise_for_status()
        with destination.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    handle.write(chunk)
    return destination


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    for name, page in SOURCES.items():
        try:
            links = links_from_page(page)
            if not links:
                print(f"{name}: nenhum arquivo diretamente detectado; consulte a página oficial.")
                continue
            print(f"{name}: {len(links)} arquivo(s) detectado(s). Primeiro: {links[0]}")
        except requests.RequestException as exc:
            print(f"{name}: falha ao consultar a fonte oficial: {exc}")


if __name__ == "__main__":
    main()
