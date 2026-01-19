import oxigenpy as oxy

def test_now_pid_tid_str():
    str_now = oxy.strings.now_pid_tid_str()
    assert "-pid" in str_now
    assert "-tid" in str_now
