from mytoto.lib import whats_my_name


def test_whoami():

    res = whats_my_name()

    assert "Judith" in res.split()