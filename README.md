
Comment/uncomment the build-backend stuff in pyproject.toml, then run `uv run demonstrate`.
If uv build-backend is used, the assertions will fail.
NOTE: When using setuptools, egg-info is created that will cause it to still work! Delete that!
