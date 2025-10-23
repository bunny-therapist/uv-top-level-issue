import importlib_metadata as metadata
# from importlib import metadata


if __name__ == "__main__":
    # uv run demonstrate.py
    dists = metadata.packages_distributions()
    print(dists)
    importable_package_name = "uv_top_level_issue"
    distribution_package_name = "uv-top-level-issue"
    assert importable_package_name in dists
    assert distribution_package_name in dists[importable_package_name]
    # Asserts pass with setuptools build-backend
    #   {'_distutils_hack': ['setuptools'], 'pkg_resources': ['setuptools'], 'setuptools': ['setuptools'], 'pip': ['pip'], 'the_package_name': ['uv-top-level-issue'], 'uv': ['uv']
    # Asserts fail with uv build-backend
    #   {'_distutils_hack': ['setuptools'], 'pkg_resources': ['setuptools'], 'setuptools': ['setuptools'], 'pip': ['pip'], 'uv': ['uv']}
    # NOTE: uv sync with setuptools build-backend creates egg-info that still makes it work! delete that first
