
def connection_pytest(connection_test):
    """Getting status code"""
    status_code =  connection_test.status
    status_info = connection_test.reason
    assert status_code == 200, "connection established"
    assert status_info == 'OK'
    
