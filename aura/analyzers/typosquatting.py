from ..uri_handlers.base import ScanLocation

from .detections import Detection
from .. import typos
from ..utils import Analyzer
from ..type_definitions import AnalyzerReturnType


@Analyzer.ID("typosquatting")
def analyze(*, location: ScanLocation) -> AnalyzerReturnType:
    if not (pkg_name:=location.metadata.get("package_name")):
        return

    typo_names = typos.check_name(pkg_name, full_list=True)

    for x in typo_names:
        yield Detection(
            detection_type = "Typosquatting",
            message = "Located a PyPI package with a similar name",
            informational=True,
            extra={
                "package_name": x
            },
            signature=f"typosquatting#{x}",
            tags={"typosquatting"}
        )
