
def connection_pytest(connection_test):
    """Getting status code"""
    status_code =  connection_test.status
    status_info = connection_test.reason
    assert status_code == 200, "Status code is 200"
    assert status_info == 'OK', "Connection test passed"
    
