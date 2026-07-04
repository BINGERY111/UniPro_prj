"""检查 urequests 是否可用"""
try:
    import urequests
    print('urequests OK:', dir(urequests))
except ImportError:
    print('urequests 不可用')
