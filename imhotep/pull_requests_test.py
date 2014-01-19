import json

from imhotep.testing_utils import fixture_path, Requester
from imhotep.pull_requests import PRInfo, get_pr_info


# via https://api.github.com/repos/justinabrahms/imhotep/pulls/10
with open(fixture_path('remote_pr.json')) as f:
    remote_json_fixture = json.loads(f.read())

# via https://api.github.com/repos/justinabrahms/imhotep/pulls/1
with open(fixture_path('non_remote_pr.json')) as f:
    not_remote_json = json.loads(f.read())

remote_pr = PRInfo(remote_json_fixture)
non_remote_pr = PRInfo(not_remote_json)


def test_pr_info_base_sha():
    assert remote_pr.base_sha == '02c774e4a8d74154468211b14f631748c1d23ef6'


def test_pr_info_head_sha():
    assert remote_pr.head_sha == '9216c7b61c6dbf547a22e5a5ad282252acc9735f'


def test_pr_info_has_remote_repo():
    assert remote_pr.has_remote_repo


def test_pr_info_doesnt_have_remote():
    assert not non_remote_pr.has_remote_repo


def test_pr_info_remote_repo():
    remote = remote_pr.remote_repo
    assert remote.name == 'scottjab'
    assert remote.url == 'https://github.com/scottjab/imhotep.git'


def test_pr_info():
    r = Requester(remote_json_fixture)
    get_pr_info(r, 'justinabrahms/imhotep', 10)
    assert r.url == 'https://api.github.com/repos/justinabrahms/imhotep/pulls/10'
