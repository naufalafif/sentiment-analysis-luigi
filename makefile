run:
	poetry run uvicorn app.main:app --reload

run-pipeline:
	poetry run python ./app/run_pipeline.py Entrypoint

run-luigi:
	poetry run luigid --logdir ./logs