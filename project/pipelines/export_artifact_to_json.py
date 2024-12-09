from pathlib import Path

from clearml import PipelineDecorator
from clearml.backend_api.session.client import APIClient
# from zenml.client import Client

from steps import export as export_steps


@PipelineDecorator.component()
def export_artifact_to_json(artifact_names: list[str], output_dir: Path = Path("output")) -> None:
    for artifact_name in artifact_names:
        artifact = APIClient()

        data = export_steps.serialize_artifact(artifact=artifact, artifact_name=artifact_name)

        export_steps.to_json(data=data, to_file=output_dir / f"{artifact_name}.json")
