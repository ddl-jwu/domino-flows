import os
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask, GitRef, EnvironmentRevisionSpecification, EnvironmentRevisionType, DatasetSnapshot
from flytekit.loggers import logger

api_key=os.environ.get('DOMINO_USER_API_KEY')
CommitId="43d7dd73a00f7ab5f2c114f1dae635d6bf48a80e" # DFS artifacts git commit

def define_job(
    name: str, 
    command: str, 
    environmentId: str, 
    hardware_tier: str,
    inputs: dict = None,
    outputs: dict = None
) -> DominoJobTask:

    # Hardcoding some values for now
    job_config = DominoJobConfig(
        ApiKey=api_key,
        Command=command,
        EnvironmentId="65cd54180df82f018c4fb7cf",
        CommitId=CommitId, # DFS commit
        MainRepoGitRef=GitRef(Type="head"),
        EnvironmentRevisionSpec=EnvironmentRevisionSpecification(
            EnvironmentRevisionType=EnvironmentRevisionType.SomeRevision,
            EnvironmentRevisionId="65cd542f0df82f018c4fb7d3",
        ),
        HardwareTierId=hardware_tier,
        VolumeSizeGiB=10,
        ExternalVolumeMountIds=[],
        DatasetSnapshots=[DatasetSnapshot(DatasetId="65e90e8dd54c6242a080e81c", SnapshotVersion=1)]
    )

    job = DominoJobTask(
        name,
        job_config,
        inputs=inputs,
        outputs=outputs
    )

    return job



 