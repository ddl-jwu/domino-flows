import os
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask, GitRef, EnvironmentRevisionSpecification, EnvironmentRevisionType, DatasetSnapshot
from flytekit.loggers import logger

api_key=os.environ.get('DOMINO_USER_API_KEY')

def define_job(
    name: str, 
    command: str, 
    environment: str = "65cd54180df82f018c4fb7cf", # HARDCODING DEFAULT FOR NOW. NEED TO UPDATE THIS TO TAKE IN PROJECT DEFAULT 
    hardware_tier: str = "small-k8s", # HARDCODING DEFAULT FOR NOW. NEED TO UPDATE THIS TO TAKE IN PROJECT DEFAULT
    inputs: dict = None,
    outputs: dict = None
) -> DominoJobTask:

    # Hardcoding some values for now
    job_config = DominoJobConfig(
        ApiKey=api_key,
        Command=command,
        EnvironmentId="65cd54180df82f018c4fb7cf", # HARDCODING DEFAULT FOR NOW. NEED TO UPDATE THIS TO MAP FROM NAME -> ID
        CommitId="43d7dd73a00f7ab5f2c114f1dae635d6bf48a80e", # DFS COMMIT ID -- HARDCODING TO RANDOM COMMIT FOR NOW SINCE THIS REPO DOESN'T USE DFS
        MainRepoGitRef=GitRef(Type="head"),
        EnvironmentRevisionSpec=EnvironmentRevisionSpecification(
            EnvironmentRevisionType=EnvironmentRevisionType.SomeRevision,
            EnvironmentRevisionId="65cd542f0df82f018c4fb7d3",
        ),
        HardwareTierId=hardware_tier,
        VolumeSizeGiB=10,
        ExternalVolumeMountIds=[],
        DatasetSnapshots=[
            DatasetSnapshot(DatasetId="65e90e8dd54c6242a080e81c", SnapshotVersion=1),
            DatasetSnapshot(DatasetId="65e90ea0d54c6242a080e81f", SnapshotVersion=1)
        ] 
    )

    job = DominoJobTask(
        name,
        job_config,
        inputs=inputs,
        outputs=outputs
    )

    return job



 